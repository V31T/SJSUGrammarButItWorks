import sys

from antlr4 import *
from SQLLexer import SQLLexer
from SQLParser import SQLParser
from MySQLVisitor import MySQLVisitor

def main(argv):
    # Provide the path to your SQL file
    sql_file_path = "./example.txt"

    # Read the content of the SQL file & stores each line into a list
    with open(sql_file_path, 'r') as file:
        sql_statements = file.readlines()

    # Create a custom visitor
    visitor = MySQLVisitor()

    # Process each SQL statement
    for sql_statement in sql_statements:
        # Skip empty lines
        if not sql_statement.strip():
            continue

        # Create an input stream for each SQL statement
        input_stream = InputStream(sql_statement)

        # Create a lexer
        lexer = SQLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SQLParser(token_stream)
        tree = parser.sqlScript()

        # Visit the parse tree with the custom visitor
        visitor.visit(tree)

    print("Stack contents:")
    for item in visitor.stack:
        print(item)


if __name__ == '__main__':
    main(sys.argv)