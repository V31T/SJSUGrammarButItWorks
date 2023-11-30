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


    # Visit a parse tree produced by SQLParser#insertStatement.
    def visitInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dropStatement.
    def visitDropStatement(self, ctx:SQLParser.DropStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#selectStatement.
    def visitSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#createStatement.
    def visitCreateStatement(self, ctx:SQLParser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#condition.
    def visitCondition(self, ctx:SQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#valueList.
    def visitValueList(self, ctx:SQLParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#setValList.
    def visitSetValList(self, ctx:SQLParser.SetValListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#setVal.
    def visitSetVal(self, ctx:SQLParser.SetValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnList.
    def visitColumnList(self, ctx:SQLParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnSpecList.
    def visitColumnSpecList(self, ctx:SQLParser.ColumnSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnSpec.
    def visitColumnSpec(self, ctx:SQLParser.ColumnSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnType.
    def visitColumnType(self, ctx:SQLParser.ColumnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnConstraint.
    def visitColumnConstraint(self, ctx:SQLParser.ColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#tableName.
    def visitTableName(self, ctx:SQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#literal.
    def visitLiteral(self, ctx:SQLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#operator.
    def visitOperator(self, ctx:SQLParser.OperatorContext):
        return self.visitChildren(ctx)



del SQLParser