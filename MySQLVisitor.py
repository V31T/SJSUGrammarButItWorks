import sqlite3
from SQLParser import SQLParser
from SQLVisitor import SQLVisitor

class MySQLVisitor(SQLVisitor):
    def __init__(self):
        super().__init__()
        self.tables = {}  # Keep track of table structures
        self.stack = []

    def visitCreateStatement(self, ctx):
        # Semantic check: Check if query is correct
        print("Creating table...")
        if ctx.TABLE().getText() != 'TABLE':
            raise ValueError(f"Creation error: Create is not a valid query, "
                             f" use CREATE TABLE")
        table_name = ctx.tableName().getText()
        # Semantic check: Check if table exists
        if table_name in self.tables:
            raise ValueError(f"Table creation error: Table '{table_name}' "
                             f"already exists")

        column_spec_list = ctx.columnSpecList().columnSpec()
        primary_count = 0
        column_names = list()
        column_data = list()
        col_name = col_data = col_constraint = ''

        for column_spec in column_spec_list:
            col_name = column_spec.ID().getText()
            col_data = column_spec.columnType().getText().upper()
            col_constraint = column_spec.columnConstraint()

            # Column duplicate check
            column_names.append(col_name)
            column_data.append(col_data)
            if len(column_names) != len(set(column_names)):
                raise ValueError(f"Table creation error: duplicate columns")

            # Check for primary key
            if col_constraint is not None:
                primary = col_constraint.PRIMARY()
                key = col_constraint.KEY()
                if primary is None or primary.getText().upper() != "PRIMARY":
                    raise ValueError(
                        f"Table creation error: Constraint not properly set, "
                        f"PRIMARY KEY is only supported")
                else:
                    if key is None or key.getText().upper() != "KEY":
                        raise ValueError(
                            f"Table creation error: Missing KEY for PRIMARY, use PRIMARY KEY")
                    else:
                        primary_count += 1
                col_constraint = f"{primary.getText().upper()} " \
                                 f"{key.getText().upper()}"

            if primary_count > 1:
                raise ValueError(f"Table creation error: Too many primary "
                                 f"keys")
        if primary_count == 0:
            raise ValueError(f"Table creation error: no primary key")

        self.tables[table_name] = dict(zip(column_names, column_data))
        self.stack.append(f"Created TABLE: {table_name}")
        return self.visitChildren(ctx)

    def visitInsertStatement(self, ctx):
        print("Inserting...")
        if ctx.INTO().getText() != 'INTO':
            raise ValueError(f"Insert error: missing INTO keyword")

        table_name = ctx.tableName().getText()
        # Semantic check: Check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Insert error: Table '{table_name}' does "
                             f"not exist.")

        column_list = ctx.columnList().ID()
        col_names = list()
        val_contents = list()
        for ID in column_list:
            col = ID.getText()
            col_names.append(col)

        value_list = ctx.valueList().literal()
        for literal in value_list:
            val = literal.getText()
            val_contents.append(val)

        # Check to see if number of columns match values
        if len(col_names) != len(val_contents):
            raise ValueError(f"Insert error: Number of columns and values "
                             f"are mismatched.")

        # Check to see if datatype matches
        for col_name, value in zip(col_names, val_contents):
            col_data_type = self.tables[table_name][col_name]
            if not self.is_data_type_compatible(value, col_data_type):
                raise ValueError(f"Insertion error: Data type mismatch for "
                                 f"column '{col_name}' in '{table_name}'.")

        self.stack.append(f"Inserted into {table_name} into the columns "
                f"{col_names} with values {val_contents}")
        return self.visitChildren(ctx)

    def visitSelectStatement(self, ctx):
        print("Selecting...")
        if ctx.FROM() is None or ctx.FROM().getText() != 'FROM':
            raise ValueError(f"Selection error: mission FROM keyword")
        table_name = ctx.tableName().getText()

        # Semantic check: Check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Selection error: Table '{table_name}' does "
                             f"not exist.")

        column_list = ctx.columnList().ID()
        col_names = list()
        for ID in column_list:
            col = ID.getText()
            col_names.append(col)
            # Check for valid columns
            if col not in self.tables[table_name]:
                raise ValueError(f"Selection error: {col} is not a valid "
                                f"column")

        get_cols = list(self.tables[table_name].keys())
        self.stack.append(f"Selected: {get_cols}")
        return self.visitChildren(ctx)

    def visitDropStatement(self, ctx):
        print("Dropping table...")
        table_name = ctx.tableName().getText()
        # Semantic check: Check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Drop error: Table '{table_name}' does "
                             f"not exist.")

        del self.tables[table_name]  # Remove the table from tracking

        self.stack.append(f"Dropped TABLE: {table_name}")
        return self.visitChildren(ctx)

    def get_data_type(self, column_definition_ctx):
        data_type_token = column_definition_ctx.columnType().start
        return data_type_token.text.upper()

    def is_data_type_compatible(self, value, data_type):
        if data_type == 'INT':
            return value.isdigit()
        elif data_type.startswith('VARCHAR'):
            return value.startswith("'") and value.endswith("'")
        elif data_type == 'DATE':
            # Add more date validation if needed
            return True
        else:
            # Add more data type checks as needed
            return False


    # Helper method to check if columns in a condition exist in the specified table
    def check_columns_exist_in_table(self, condition, table_name):
        column_names = self.tables[table_name].keys()
        for column_name in column_names:
            if condition.getText().find(column_name) == -1:
                raise ValueError(
                    f"Condition error: Column '{column_name}' does not exist in '{table_name}'.")
