grammar SQL;

// Parser rules
sqlScript: statement+ EOF;

statement: createStatement
         | insertStatement
         | selectStatement
         | dropStatement;

createStatement: 'CREATE' ('TABLE' | 'DATABASE') ID '(' columnDefinition (',' columnDefinition)* ')' ';';

insertStatement: 'INSERT' 'INTO' ID '(' columnName (',' columnName)* ')' 'VALUES' '(' literalValue (',' literalValue)* ')' ';';

selectStatement: 'SELECT' ('*' | columnName (',' columnName)*) 'FROM' ID ('WHERE' condition)? ';';

dropStatement: 'DROP' ('TABLE' | 'DATABASE') ID ';';

// Conditions
condition: columnName operator literalValue;

operator: '=' | '<>' | '<' | '>' | '<=' | '>=' | '!=';

// Lexer rules
columnName: ID;
tableName: ID;

columnDefinition: columnName dataType;

dataType: 'INT' | 'VARCHAR' '(' INT ')' | 'DATE';

literalValue: STRING | INT | 'NULL';

// Common lexer rules
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '\'' ~('\'' | '\r' | '\n')* '\'';
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip; // skip whitespace