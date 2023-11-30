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
        for column_spec in column_spec_list:
            col_name = column_spec.ID().getText()
            col_data = column_spec.columnType().getText().upper()
            col_constraint = column_spec.columnConstraint()

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
                            f"Table creation error: Constraint please use "
                            f"PRIMARY KEY not PRIMARY")
                    else:
                        primary_count += 1
                col_constraint = f"{primary.getText().upper()} " \
                                 f"{key.getText().upper()}"

            print(f"Column: {col_name}, Data Type: {col_data}, "
                 f"Key: {col_constraint}")
            if primary_count > 1:
                raise ValueError(f"Table creation error: Too many primary "
                                 f"keys")
        if primary_count == 0:
            raise ValueError(f"Table creation error: no primary key")

        return self.visitChildren(ctx)

    def visitInsertStatement(self, ctx):
        if ctx.INTO().getText() != 'INTO':
            raise ValueError(f"Insert error: missing INTO keyword")

        table_name = ctx.tableName().getText()
        Semantic check: Check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Insert error: Table '{table_name}' does "
                             f"not exist.")

        column_list = ctx.columnList().ID()
        col_names = list()
        val_content = list()
        for ID in column_list:
            col = ID.getText()
            col_names.append(col)

        value_list = ctx.valueList().literal()
        for literal in value_list:
            val = literal.getText()
            val_content.append(val)

        return self.visitChildren(ctx)

    def visitSelectStatement(self, ctx):
        if ctx.FROM() is None or ctx.FROM().getText() != 'FROM':
            raise ValueError(f"Select error: mission FROM keyword")
        table_name = ctx.tableName().getText()
        # Semantic check: Check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Insert error: Table '{table_name}' does "
                             f"not exist.")

        column_list = ctx.columnList().ID()
        col_names = list()
        for ID in column_list:
            col = ID.getText()
            col_names.append(col)
            print(col)
        return self.visitChildren(ctx)

    def visitDropStatement(self, ctx):
        table_name = ctx.tableName().getText()
        # Semantic check: Check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Drop error: Table '{table_name}' does "
                             f"not exist.")

        del self.tables[tabel_name]  # Remove the table from tracking

        self.stack.append(f"Dropped {table_name}")
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
