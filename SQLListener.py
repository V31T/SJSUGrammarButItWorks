# Generated from SQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#sqlScript.
    def enterSqlScript(self, ctx:SQLParser.SqlScriptContext):
        pass

    # Exit a parse tree produced by SQLParser#sqlScript.
    def exitSqlScript(self, ctx:SQLParser.SqlScriptContext):
        pass


    # Enter a parse tree produced by SQLParser#statement.
    def enterStatement(self, ctx:SQLParser.StatementContext):
        pass

    # Exit a parse tree produced by SQLParser#statement.
    def exitStatement(self, ctx:SQLParser.StatementContext):
        pass


    # Enter a parse tree produced by SQLParser#createStatement.
    def enterCreateStatement(self, ctx:SQLParser.CreateStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#createStatement.
    def exitCreateStatement(self, ctx:SQLParser.CreateStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#insertStatement.
    def enterInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#insertStatement.
    def exitInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#selectStatement.
    def enterSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#selectStatement.
    def exitSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#dropStatement.
    def enterDropStatement(self, ctx:SQLParser.DropStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#dropStatement.
    def exitDropStatement(self, ctx:SQLParser.DropStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#condition.
    def enterCondition(self, ctx:SQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by SQLParser#condition.
    def exitCondition(self, ctx:SQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by SQLParser#operator.
    def enterOperator(self, ctx:SQLParser.OperatorContext):
        pass

    # Exit a parse tree produced by SQLParser#operator.
    def exitOperator(self, ctx:SQLParser.OperatorContext):
        pass


    # Enter a parse tree produced by SQLParser#columnName.
    def enterColumnName(self, ctx:SQLParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by SQLParser#columnName.
    def exitColumnName(self, ctx:SQLParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by SQLParser#tableName.
    def enterTableName(self, ctx:SQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SQLParser#tableName.
    def exitTableName(self, ctx:SQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SQLParser#columnDefinition.
    def enterColumnDefinition(self, ctx:SQLParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by SQLParser#columnDefinition.
    def exitColumnDefinition(self, ctx:SQLParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by SQLParser#dataType.
    def enterDataType(self, ctx:SQLParser.DataTypeContext):
        pass

    # Exit a parse tree produced by SQLParser#dataType.
    def exitDataType(self, ctx:SQLParser.DataTypeContext):
        pass


    # Enter a parse tree produced by SQLParser#literalValue.
    def enterLiteralValue(self, ctx:SQLParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by SQLParser#literalValue.
    def exitLiteralValue(self, ctx:SQLParser.LiteralValueContext):
        pass



del SQLParser