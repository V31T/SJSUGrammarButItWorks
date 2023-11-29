import sqlite3
from SQLParser import SQLParser
from SQLVisitor import SQLVisitor

class MySQLVisitor(SQLVisitor):
    def __init__(self):
        super().__init__()
        self.tables = {}  # Keep track of table structures
        self.stack = []

    def visitCreateStatement(self, ctx):
        object_type = ctx.getChild(1).getText()  # TABLE or DATABASE
        object_name = ctx.ID().getText()
        print(f"Creating {object_type}: {object_name}")

        if object_type == "TABLE":
            # Semantic check: Ensure table does not already exist
            if object_name in self.tables:
                raise ValueError(f"Table creation error: Table '{object_name}' already exists.")

            # Semantic check: Ensure no duplicate column names
            column_names = [column.getText() for column in ctx.columnName()]
            if len(column_names) != len(set(column_names)):
                raise ValueError(f"Table creation error: Duplicate column names in '{object_name}'.")

            # Add table to the tracking dictionary with data types
            column_data_types = [self.get_data_type(col) for col in ctx.columnDefinition()]
            self.tables[object_name] = dict(zip(column_names, column_data_types))

        self.stack.append(f"Created {object_type}: {object_name}")
        return self.visitChildren(ctx)

    def visitInsertStatement(self, ctx):
        table_name = ctx.ID(0).getText()
        print(f"Inserting into {table_name}")

        # Semantic check: Ensure the table exists
        if table_name not in self.tables:
            raise ValueError(f"Insertion error: Table '{table_name}' does not exist.")

        # Semantic check: Ensure the number of values matches the number of columns
        column_names = list(self.tables[table_name].keys())
        values = [value.getText() for value in ctx.literalValue()]
        if len(column_names) != len(values):
            raise ValueError(f"Insertion error: Number of values does not match the number of columns in '{table_name}'.")

        # Semantic check: Check data type compatibility
        for col_name, value in zip(column_names, values):
            col_data_type = self.tables[table_name][col_name]
            if not self.is_data_type_compatible(value, col_data_type):
                raise ValueError(f"Insertion error: Data type mismatch for column '{col_name}' in '{table_name}'.")

        self.stack.append(f"Inserted into {table_name}")
        return self.visitChildren(ctx)

    def visitSelectStatement(self, ctx):
        # Get table name
        table_name = ctx.ID().getText()

        # Semantic check: Ensure the table exists
        if table_name not in self.tables:
            raise ValueError(f"Selection error: Table '{table_name}' does not exist.")

        # Get column names and aliases
        select_clause = ctx.selectClause()
        if select_clause.WILDCARD() is not None:
            # All columns selected
            selected_columns = list(self.tables[table_name].keys())
        else:
            selected_columns = [col.getText() for col in select_clause.selectColumn()]

        # Semantic check: Ensure selected columns exist in the table
        for column in selected_columns:
            if column not in self.tables[table_name]:
                raise ValueError(f"Selection error: Column '{column}' does not exist in '{table_name}'.")

        # Get condition (if present)
        condition = ctx.condition()
        condition_str = f"WHERE {condition.getText()}" if condition is not None else ""

        # Build the output string
        output_str = (
            f"Selecting from {table_name}\n"
            f"  Columns selected: {', '.join(selected_columns)}\n"
            f"{condition_str}"
        )

        self.stack.append(output_str)
        return self.visitChildren(ctx)

    def visitDropStatement(self, ctx):
        object_type = ctx.getChild(1).getText()  # TABLE or DATABASE
        object_name = ctx.ID().getText()
        print(f"Dropping {object_type}: {object_name}")

        # Semantic check: Ensure the table exists
        if object_name not in self.tables:
            raise ValueError(f"Dropping error: {object_type} '{object_name}' does not exist.")

        del self.tables[object_name]  # Remove the table from tracking

        self.stack.append(f"Dropped {object_type}: {object_name}")
        return self.visitChildren(ctx)

    def get_data_type(self, column_definition_ctx):
        # This is a simplified function; you might need a more sophisticated approach based on your grammar
        data_type_token = column_definition_ctx.dataType().start
        return data_type_token.text.upper()

    def is_data_type_compatible(self, value, data_type):
        # This is a simplified function; you might need a more sophisticated type checking based on your grammar
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