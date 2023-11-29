import sys

from antlr4 import *
from SQLLexer import SQLLexer
from SQLParser import SQLParser
from MySQLVisitor import MySQLVisitor

def main(argv):
    # Provide the path to your SQL file
    sql_file_path = r"C:\Users\Henry Pham\Desktop\VSCode\CS152proj\example.sql"

    # Read the content of the SQL file
    with open(sql_file_path, 'r') as file:
        sql_input = file.read()

    # Split the input into individual lines (assuming each line contains a separate SQL statement)
    sql_statements = sql_input.split('\n')

    # Create a custom visitor
    visitor = MySQLVisitor()

    # Process each SQL statement
    for sql_statement in sql_statements:
        # Skip empty lines
        if not sql_statement.strip():
            continue

        # Create an input stream for each SQL statement
        input_stream = FileStream(sql_statement)

        # Create a lexer
        lexer = SQLLexer(input_stream)

        # Create a token stream
        token_stream = CommonTokenStream(lexer)

        # Create a parser
        parser = SQLParser(token_stream)

        # Parse the SQL statement to get the parse tree
        tree = parser.sqlScript()

        # Visit the parse tree with the custom visitor
        visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)