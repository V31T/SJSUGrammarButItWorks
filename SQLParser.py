# Generated from SQL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,3,1,
        3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,5,4,86,8,4,10,4,12,4,89,9,4,3,4,91,8,4,1,4,1,4,1,4,1,4,3,4,
        97,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,
        8,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,125,
        8,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,3,
        1,0,2,3,1,0,16,22,2,0,26,26,28,29,127,0,27,1,0,0,0,2,37,1,0,0,0,
        4,39,1,0,0,0,6,54,1,0,0,0,8,80,1,0,0,0,10,100,1,0,0,0,12,105,1,0,
        0,0,14,109,1,0,0,0,16,111,1,0,0,0,18,113,1,0,0,0,20,115,1,0,0,0,
        22,124,1,0,0,0,24,126,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,
        1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,1,
        32,1,1,0,0,0,33,38,3,4,2,0,34,38,3,6,3,0,35,38,3,8,4,0,36,38,3,10,
        5,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,
        1,0,0,0,39,40,5,1,0,0,40,41,7,0,0,0,41,42,5,27,0,0,42,43,5,4,0,0,
        43,48,3,20,10,0,44,45,5,5,0,0,45,47,3,20,10,0,46,44,1,0,0,0,47,50,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,
        51,52,5,6,0,0,52,53,5,7,0,0,53,5,1,0,0,0,54,55,5,8,0,0,55,56,5,9,
        0,0,56,57,5,27,0,0,57,58,5,4,0,0,58,63,3,16,8,0,59,60,5,5,0,0,60,
        62,3,16,8,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,
        0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,6,0,0,67,68,5,10,0,0,68,
        69,5,4,0,0,69,74,3,24,12,0,70,71,5,5,0,0,71,73,3,24,12,0,72,70,1,
        0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,
        74,1,0,0,0,77,78,5,6,0,0,78,79,5,7,0,0,79,7,1,0,0,0,80,90,5,11,0,
        0,81,91,5,12,0,0,82,87,3,16,8,0,83,84,5,5,0,0,84,86,3,16,8,0,85,
        83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,
        0,89,87,1,0,0,0,90,81,1,0,0,0,90,82,1,0,0,0,91,92,1,0,0,0,92,93,
        5,13,0,0,93,96,5,27,0,0,94,95,5,14,0,0,95,97,3,12,6,0,96,94,1,0,
        0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,7,0,0,99,9,1,0,0,0,100,101,
        5,15,0,0,101,102,7,0,0,0,102,103,5,27,0,0,103,104,5,7,0,0,104,11,
        1,0,0,0,105,106,3,16,8,0,106,107,3,14,7,0,107,108,3,24,12,0,108,
        13,1,0,0,0,109,110,7,1,0,0,110,15,1,0,0,0,111,112,5,27,0,0,112,17,
        1,0,0,0,113,114,5,27,0,0,114,19,1,0,0,0,115,116,3,16,8,0,116,117,
        3,22,11,0,117,21,1,0,0,0,118,125,5,23,0,0,119,120,5,24,0,0,120,121,
        5,4,0,0,121,122,5,29,0,0,122,125,5,6,0,0,123,125,5,25,0,0,124,118,
        1,0,0,0,124,119,1,0,0,0,124,123,1,0,0,0,125,23,1,0,0,0,126,127,7,
        2,0,0,127,25,1,0,0,0,9,29,37,48,63,74,87,90,96,124
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'TABLE'", "'DATABASE'", "'('", 
                     "','", "')'", "';'", "'INSERT'", "'INTO'", "'VALUES'", 
                     "'SELECT'", "'*'", "'FROM'", "'WHERE'", "'DROP'", "'='", 
                     "'<>'", "'<'", "'>'", "'<='", "'>='", "'!='", "'INT'", 
                     "'VARCHAR'", "'DATE'", "'NULL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "INT", "WS" ]

    RULE_sqlScript = 0
    RULE_statement = 1
    RULE_createStatement = 2
    RULE_insertStatement = 3
    RULE_selectStatement = 4
    RULE_dropStatement = 5
    RULE_condition = 6
    RULE_operator = 7
    RULE_columnName = 8
    RULE_tableName = 9
    RULE_columnDefinition = 10
    RULE_dataType = 11
    RULE_literalValue = 12

    ruleNames =  [ "sqlScript", "statement", "createStatement", "insertStatement", 
                   "selectStatement", "dropStatement", "condition", "operator", 
                   "columnName", "tableName", "columnDefinition", "dataType", 
                   "literalValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    ID=27
    STRING=28
    INT=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SqlScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(SQLParser.StatementContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_sqlScript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlScript" ):
                listener.enterSqlScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlScript" ):
                listener.exitSqlScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlScript" ):
                return visitor.visitSqlScript(self)
            else:
                return visitor.visitChildren(self)




    def sqlScript(self):

        localctx = SQLParser.SqlScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sqlScript)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 35074) != 0)):
                    break

            self.state = 31
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createStatement(self):
            return self.getTypedRuleContext(SQLParser.CreateStatementContext,0)


        def insertStatement(self):
            return self.getTypedRuleContext(SQLParser.InsertStatementContext,0)


        def selectStatement(self):
            return self.getTypedRuleContext(SQLParser.SelectStatementContext,0)


        def dropStatement(self):
            return self.getTypedRuleContext(SQLParser.DropStatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.createStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.insertStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.selectStatement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.dropStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def columnDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnDefinitionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnDefinitionContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_createStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStatement" ):
                listener.enterCreateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStatement" ):
                listener.exitCreateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateStatement" ):
                return visitor.visitCreateStatement(self)
            else:
                return visitor.visitChildren(self)




    def createStatement(self):

        localctx = SQLParser.CreateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(SQLParser.T__0)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 41
            self.match(SQLParser.ID)
            self.state = 42
            self.match(SQLParser.T__3)
            self.state = 43
            self.columnDefinition()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 44
                self.match(SQLParser.T__4)
                self.state = 45
                self.columnDefinition()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(SQLParser.T__5)
            self.state = 52
            self.match(SQLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnNameContext,i)


        def literalValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.LiteralValueContext)
            else:
                return self.getTypedRuleContext(SQLParser.LiteralValueContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_insertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStatement" ):
                listener.enterInsertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStatement" ):
                listener.exitInsertStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStatement" ):
                return visitor.visitInsertStatement(self)
            else:
                return visitor.visitChildren(self)




    def insertStatement(self):

        localctx = SQLParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_insertStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SQLParser.T__7)
            self.state = 55
            self.match(SQLParser.T__8)
            self.state = 56
            self.match(SQLParser.ID)
            self.state = 57
            self.match(SQLParser.T__3)
            self.state = 58
            self.columnName()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 59
                self.match(SQLParser.T__4)
                self.state = 60
                self.columnName()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(SQLParser.T__5)
            self.state = 67
            self.match(SQLParser.T__9)
            self.state = 68
            self.match(SQLParser.T__3)
            self.state = 69
            self.literalValue()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 70
                self.match(SQLParser.T__4)
                self.state = 71
                self.literalValue()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(SQLParser.T__5)
            self.state = 78
            self.match(SQLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnNameContext,i)


        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStatement" ):
                return visitor.visitSelectStatement(self)
            else:
                return visitor.visitChildren(self)




    def selectStatement(self):

        localctx = SQLParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SQLParser.T__10)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 81
                self.match(SQLParser.T__11)
                pass
            elif token in [27]:
                self.state = 82
                self.columnName()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 83
                    self.match(SQLParser.T__4)
                    self.state = 84
                    self.columnName()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 92
            self.match(SQLParser.T__12)
            self.state = 93
            self.match(SQLParser.ID)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 94
                self.match(SQLParser.T__13)
                self.state = 95
                self.condition()


            self.state = 98
            self.match(SQLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_dropStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropStatement" ):
                listener.enterDropStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropStatement" ):
                listener.exitDropStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropStatement" ):
                return visitor.visitDropStatement(self)
            else:
                return visitor.visitChildren(self)




    def dropStatement(self):

        localctx = SQLParser.DropStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dropStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SQLParser.T__14)
            self.state = 101
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 102
            self.match(SQLParser.ID)
            self.state = 103
            self.match(SQLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(SQLParser.ColumnNameContext,0)


        def operator(self):
            return self.getTypedRuleContext(SQLParser.OperatorContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(SQLParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = SQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.columnName()
            self.state = 106
            self.operator()
            self.state = 107
            self.literalValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = SQLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8323072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = SQLParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(SQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = SQLParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(SQLParser.ColumnNameContext,0)


        def dataType(self):
            return self.getTypedRuleContext(SQLParser.DataTypeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_columnDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDefinition" ):
                listener.enterColumnDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDefinition" ):
                listener.exitColumnDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnDefinition" ):
                return visitor.visitColumnDefinition(self)
            else:
                return visitor.visitChildren(self)




    def columnDefinition(self):

        localctx = SQLParser.ColumnDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_columnDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.columnName()
            self.state = 116
            self.dataType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = SQLParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dataType)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(SQLParser.T__22)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(SQLParser.T__23)
                self.state = 120
                self.match(SQLParser.T__3)
                self.state = 121
                self.match(SQLParser.INT)
                self.state = 122
                self.match(SQLParser.T__5)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(SQLParser.T__24)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SQLParser.STRING, 0)

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralValue" ):
                return visitor.visitLiteralValue(self)
            else:
                return visitor.visitChildren(self)




    def literalValue(self):

        localctx = SQLParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 872415232) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





