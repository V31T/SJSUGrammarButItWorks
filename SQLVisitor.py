# Generated from SQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQLParser#sqlScript.
    def visitSqlScript(self, ctx:SQLParser.SqlScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#statement.
    def visitStatement(self, ctx:SQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#createStatement.
    def visitCreateStatement(self, ctx:SQLParser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#insertStatement.
    def visitInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#selectStatement.
    def visitSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dropStatement.
    def visitDropStatement(self, ctx:SQLParser.DropStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#condition.
    def visitCondition(self, ctx:SQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#operator.
    def visitOperator(self, ctx:SQLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnName.
    def visitColumnName(self, ctx:SQLParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#tableName.
    def visitTableName(self, ctx:SQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnDefinition.
    def visitColumnDefinition(self, ctx:SQLParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dataType.
    def visitDataType(self, ctx:SQLParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#literalValue.
    def visitLiteralValue(self, ctx:SQLParser.LiteralValueContext):
        return self.visitChildren(ctx)



del SQLParser