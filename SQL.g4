grammar SQL;

sqlScript: statement+ EOF;

statement: selectStatement
     | createStatement
     | dropStatement
     | insertStatement
     ;

// Statements
insertStatement: INSERT INTO tableName ('(' columnList ')')? VALUES '('valueList ')';
dropStatement: DROP TABLE tableName;
selectStatement: SELECT (columnList)? FROM tableName;
createStatement: CREATE TABLE tableName '(' columnSpecList ')';

condition: ID operator literal;
valueList: literal (',' literal)*;
setValList: setVal (',' setVal)*;
setVal: ID '=' literal;

// Column stuff
columnList: ID (',' ID)* | '*';
columnSpecList: columnSpec (',' columnSpec)*;
columnSpec: ID columnType columnConstraint?;
columnType: INT | VARCHAR ('(' INT_LITERAL ')')? | DATE;
columnConstraint: PRIMARY KEY;

tableName: ID;
literal: INT_LITERAL | STRING_LITERAL;

// Most Common Queries
CREATE: 'CREATE';
SELECT: 'SELECT';
INSERT: 'INSERT';
DROP: 'DROP';
DELETE: 'DELETE';
UPDATE: 'UPDATE';

// Most Common Keywords
INTO: 'INTO';
FROM: 'FROM';
PRIMARY: 'PRIMARY';
KEY: 'KEY';
TABLE:'TABLE';
VALUES: 'VALUES';
SET: 'SET';

// Common Data types
INT: 'INT';
VARCHAR: 'VARCHAR';
DATE: 'DATE';

// Common Operators
AND: 'AND';
OR: 'OR';
XOR: 'XOR';
operator: '=' | '<>' | '<' | '>' | '<=' | '>=' | '!=';

ID: [a-zA-Z_] [a-zA-Z_0-9]*;
NEWLINE : [\r\n]+ ;
INT_LITERAL     : [0-9]+ ;
STRING_LITERAL  : '\'' ~('\'' | '\r' | '\n')* '\'' ;
WS      : [ \t\r\n] -> channel(HIDDEN);
