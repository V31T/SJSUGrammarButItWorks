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


    # Enter a parse tree produced by SQLParser#insertStatement.
    def enterInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#insertStatement.
    def exitInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#dropStatement.
    def enterDropStatement(self, ctx:SQLParser.DropStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#dropStatement.
    def exitDropStatement(self, ctx:SQLParser.DropStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#selectStatement.
    def enterSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#selectStatement.
    def exitSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#createStatement.
    def enterCreateStatement(self, ctx:SQLParser.CreateStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#createStatement.
    def exitCreateStatement(self, ctx:SQLParser.CreateStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#condition.
    def enterCondition(self, ctx:SQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by SQLParser#condition.
    def exitCondition(self, ctx:SQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by SQLParser#valueList.
    def enterValueList(self, ctx:SQLParser.ValueListContext):
        pass

    # Exit a parse tree produced by SQLParser#valueList.
    def exitValueList(self, ctx:SQLParser.ValueListContext):
        pass


    # Enter a parse tree produced by SQLParser#setValList.
    def enterSetValList(self, ctx:SQLParser.SetValListContext):
        pass

    # Exit a parse tree produced by SQLParser#setValList.
    def exitSetValList(self, ctx:SQLParser.SetValListContext):
        pass


    # Enter a parse tree produced by SQLParser#setVal.
    def enterSetVal(self, ctx:SQLParser.SetValContext):
        pass

    # Exit a parse tree produced by SQLParser#setVal.
    def exitSetVal(self, ctx:SQLParser.SetValContext):
        pass


    # Enter a parse tree produced by SQLParser#columnList.
    def enterColumnList(self, ctx:SQLParser.ColumnListContext):
        pass

    # Exit a parse tree produced by SQLParser#columnList.
    def exitColumnList(self, ctx:SQLParser.ColumnListContext):
        pass


    # Enter a parse tree produced by SQLParser#columnSpecList.
    def enterColumnSpecList(self, ctx:SQLParser.ColumnSpecListContext):
        pass

    # Exit a parse tree produced by SQLParser#columnSpecList.
    def exitColumnSpecList(self, ctx:SQLParser.ColumnSpecListContext):
        pass


    # Enter a parse tree produced by SQLParser#columnSpec.
    def enterColumnSpec(self, ctx:SQLParser.ColumnSpecContext):
        pass

    # Exit a parse tree produced by SQLParser#columnSpec.
    def exitColumnSpec(self, ctx:SQLParser.ColumnSpecContext):
        pass


    # Enter a parse tree produced by SQLParser#columnType.
    def enterColumnType(self, ctx:SQLParser.ColumnTypeContext):
        pass

    # Exit a parse tree produced by SQLParser#columnType.
    def exitColumnType(self, ctx:SQLParser.ColumnTypeContext):
        pass


    # Enter a parse tree produced by SQLParser#columnConstraint.
    def enterColumnConstraint(self, ctx:SQLParser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by SQLParser#columnConstraint.
    def exitColumnConstraint(self, ctx:SQLParser.ColumnConstraintContext):
        pass


    # Enter a parse tree produced by SQLParser#tableName.
    def enterTableName(self, ctx:SQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SQLParser#tableName.
    def exitTableName(self, ctx:SQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SQLParser#literal.
    def enterLiteral(self, ctx:SQLParser.LiteralContext):
        pass

    # Exit a parse tree produced by SQLParser#literal.
    def exitLiteral(self, ctx:SQLParser.LiteralContext):
        pass


    # Enter a parse tree produced by SQLParser#operator.
    def enterOperator(self, ctx:SQLParser.OperatorContext):
        pass

    # Exit a parse tree produced by SQLParser#operator.
    def exitOperator(self, ctx:SQLParser.OperatorContext):
        pass



del SQLParser