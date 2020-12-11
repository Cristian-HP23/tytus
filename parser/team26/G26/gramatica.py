reservadas = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : "PRECISION",
    'money' : 'MONEY',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'use' : 'USE',
    'timestamp' : 'TIMESTAMP',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'boolean' : 'BOLEANO',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'between' : 'BETWEEN',
    'in' : 'IN',
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'isnull' : 'ISNULL',
    'is' : 'IS',
    'notnull' : 'NOTNULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'unknown' : 'UNKNOWN',
    'null' : 'NULL',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'count' : 'COUNT',
    'max' : 'MAX',
    'min' : 'MIN',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'replace' : 'REPLACE',
    'databases' : 'DATABASES',
    'database' : 'DATABASE',
    'if' : 'IF',
    'not' : 'NOT',
    'exists' : 'EXISTS',
    'owner' : 'OWNER',
    'mode' : 'MODE',
    'like' : 'LIKE',
    'alter' : 'ALTER',
    'rename' : 'RENAME',
    'to' : 'TO',
    'drop' : 'DROP',
    'table' : 'TABLE',
    'default' : 'DEFAULT',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'drop' : 'DROP',
    'alter' : 'ALTER',
    'add' : 'ADD',
    'column' : 'COLUMN',
    'delete' : 'DELETE',
    'from' : 'FROM',
    'only' : 'ONLY',
    'using' : 'USING',
    'where' : 'WHERE',
    'current' : 'CURRENT',
    'of' : 'OF',
    'returning' : 'RETURNING',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'set' : 'SET',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'having' : 'HAVING',
    'substring' : 'SUBSTRING',
    'exists' : 'EXISTS',
    'join' : 'JOIN',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'on' : 'ON',
    'natural' : 'NATURAL',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'all' : 'ALL',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceiling' : 'CEILING',
    'ceil' : 'CEIL',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'EXP',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'log10' : 'LOGDIEZ',
    'min_scale' : 'MINSCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM',
    'truc' : 'TRUC',
    'width_bucket' : 'BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATANDOS',
    'atan2d' : 'ATANDOSD',
    'cos' : 'COS',
    'cosd' : 'COSD',
    'cot' : 'COT',
    'cotd' : 'COTD',
    'sin' : 'SIN',
    'sind' : 'SIND',
    'tan' : 'TAN',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    'length' : 'LENGHT',
    'get_byte' : 'GETBYTE',
    'factorial' : 'FACTORIAL',
    'md5' : 'MD5',
    'set_byte' : 'SETBYTE',
    'sha256' : 'SHA',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    'date_part' : 'DATEPART',
    'now' : 'NOW',
    'extract' : 'EXTRACT',
    'current_date' : 'CURRENTDATE',
    'current_time' : 'CURRENTTIME',
    'date' : 'DATE',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'show'  :   'SHOW',
    'symmetric' : 'SYMMETRIC'
}

tokens = [
    'PTCOMA',
    'LLAVEIZQ',
    'LLAVEDER',
    'PARENIZQ',
    'PARENDER',
    'IGUAL',
    'MAS',
    'GUION',
    'BARRA',
    'ASTERISCO',
    'MAYORQUE',
    'MENORQUE',
    'MENORIGUALQUE',
    'MAYORIGUALQUE',
    'DIFERENTE',
    'DIFERENTELL',
    'PUNTO',
    'COMA',
    'ENTERO',
    'DECIMALVALOR',
    'CADENA',
    'ID',
    'BACKSPACE',
    'FEED',
    'NEWLINE',
    'RETURN',
    'TAB',
    'FECHA',
    'SFACTORIAL',
    'PORCENTAJE',
    'POTENCIA'
] + list(reservadas.values())

#tokens
t_PTCOMA        = r';'
t_LLAVEIZQ      = r'{'
t_LLAVEDER      = r'}'
t_PARENIZQ      = r'\('
t_PARENDER      = r'\)'
t_IGUAL         = r'='
t_MAS           = r'\+'
t_GUION         = r'-'
t_ASTERISCO     = r'\*'
t_BARRA         = r'/'
t_MAYORIGUALQUE = r'>='
t_MAYORQUE      = r'>'
t_MENORIGUALQUE = r'<'
t_MENORQUE      = r'<='
t_DIFERENTELL   = r'<>'
t_DIFERENTE     = r'!='
t_PUNTO         = r'.'
t_COMA          = r'\,'
t_BACKSPACE     = r'\\b'
t_FEED          = r'\\f'
t_NEWLINE       = r'\\n'
t_RETURN        = r'\\r'
t_TAB           = r'\\r'
t_PORCENTAJE    = r'%'
t_SFACTORIAL    = r'!'
t_POTENCIA      = r'\^'

def t_DECIMALVALOR(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_FECHA(t):
    r'\'\d+-\d+-\d+ \d+:\d+:\d+\''
    return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

from imports import *

precedence = (
    ('left','MAS','GUION'),
    ('left','ASTERISCO','BARRA', 'PORCENTAJE'),
    ('left','POTENCIA'),
    ('right','UMENOS', 'UMAS'),
    )

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instruciones(t):
    'instrucciones : instruccion'''
    t[0] = [t[1]]


def p_instruccion(t) :
    '''instruccion      : CREATE create
                        | USE use
                        | SHOW show
                        | DROP drop
                        | ALTER alter
                        | DELETE delete
                        | INSERT insert
                        | UPDATE update
                        | AS condicions'''
    t[0] = t[2]

def p_create_instruccion(t) :
    '''create : TYPE createenum
              | TABLE createtable
              | OR REPLACE DATABASE createdatabase
              | DATABASE createdatabase'''
    if t[1].lower() == 'type' : t[0] = create.Create('type', t[2])
    elif t[1].lower() == 'table' : t[0] = create.Create('table', [])
    elif t[1].lower() == 'or' : t[0] = create.Create('replace', [])
    elif t[1].lower() == 'database' : t[0] = create.Create('database', [])

def p_createenum(t):
    'createenum : ID AS ENUM PARENIZQ listacadenas PARENDER PTCOMA'

def p_listacadenas(t):
    '''listacadenas : listacadenas COMA CADENA
                    | CADENA'''

def p_createdatabase(t):
    '''createdatabase : IF NOT EXISTS ID databaseowner
                      | ID databaseowner'''

def p_databaseowner(t):
    '''databaseowner : OWNER IGUAL ID databasemode
                     | OWNER ID databasemode
                     | databasemode'''

def p_databasemode(t):
    '''databasemode : MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA'''

def p_createtable(t):
    'createtable : ID PARENIZQ tabledescriptions PARENDER tableherencia'

def p_tableherencia(t):
    '''tableherencia : INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA'''

def p_tabledescriptions(t):
    '''tabledescriptions : tabledescriptions COMA tabledescription
                         | tabledescription'''

'''
################################################################################
################################################################################
AGREGAR TIPO, LISTAIDS
'''

def p_tabledescription(t):
    '''tabledescription : ID tipo tablekey
                        | PRIMARY KEY PARENIZQ PARENDER
                        | FOREIGN KEY PARENIZQ PARENDER REFERENCES ID PARENIZQ PARENDER
                        | CONSTRAINT ID CHECK finalconstraintcheck
                        | CHECK finalconstraintcheck
                        | UNIQUE finalunique'''

def p_tablekey(t):
    '''tablekey : PRIMARY KEY tabledefault
                | REFERENCES ID tabledefault
                | '''

'''
################################################################################
################################################################################
AGREGAR VALUE
'''

def p_tabledefault(t):
    '''tabledefault : DEFAULT tablenull
                    | tablenull'''

def p_tablenull(t):
    '''tablenull : NOT NULL tableconstraintunique
                 | NULL tableconstraintunique'''

def p_tableconstraintunique(t):
    '''tableconstraintunique : CONSTRAINT ID UNIQUE tableconstraintcheck
                             | UNIQUE tableconstraintcheck'''

'''
################################################################################
################################################################################
AGREGAR CONDICIONES
'''

def p_tableconstraintcheck(t):
    '''tableconstraintcheck : CONSTRAINT ID CHECK PARENIZQ PARENDER
                            | CHECK PARENIZQ PARENDER
                            | '''

def p_finalconstraintcheck(t):
    'finalconstraintcheck : PARENIZQ PARENDER'

'''
################################################################################
################################################################################
AGREGAR LISTAIDS
'''

def p_finalunique(t):
    'finalunique : PARENIZQ PARENDER'


def p_tipo(t):
    '''tipo : SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE PRECISION
            | MONEY
            | CHARACTER tipochar
            | VARCHAR PARENIZQ ENTERO PARENDER
            | CHAR PARENIZQ ENTERO PARENDER
            | TEXT
            | TIMESTAMP precision
            | TIME precision
            | DATE
            | INTERVAL fields precision
            | BOLEANO
            | ID'''

def p_tipochar(t):
    '''tipochar : VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER'''

def p_precision(t):
    '''precision : PARENIZQ ENTERO PARENDER
                 | '''

def p_fields(t):
    '''fields : MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR
              | '''

###########USE
def p_use(t):
    'use    :  ID PTCOMA'

##########SHOW
def p_show(t):
    'show   :    DATABASES likeopcional'

def p_likeopcional(t):
    '''likeopcional   :   LIKE CADENA PTCOMA
                    | PTCOMA '''

##########DROP
def p_drop(t):
    '''drop :   DATABASE dropdb PTCOMA
            |   TABLE ID PTCOMA '''

def p_dropdb(t):
    '''dropdb : IF EXISTS ID
                |   ID'''

###########ALTER
def p_alter(t):
    '''alter    :   DATABASE ID alterdb PTCOMA
                |   TABLE ID altertable '''
#alter database
def p_alterdb(t):
    '''alterdb  :   RENAME TO ID
                |   OWNER TO tipodeowner'''

def p_tipodeowner(t):
    '''tipodeowner  :   ID
                    |   CURRENT_USER
                    |   SESSION_USER'''
#alter table
def p_altertable(t):
    '''altertable    :   ADD alteradd PTCOMA
                    |   ALTER COLUMN ID SET opcionesalterset PTCOMA
                    |   DROP tipodedrop PTCOMA
                    | RENAME COLUMN ID TO ID PTCOMA'''
#agregar tipo, condiciones, listaids opcionsalter
def p_alteradd(t):
    ''' alteradd   :   COLUMN ID tipo
                    |  CHECK PARENIZQ PARENDER
                    |  CONSTRAINT ID UNIQUE PARENIZQ ID PARENDER
                    |  FOREIGN KEY PARENIZQ PARENDER REFERENCES ID PARENIZQ PARENDER '''

def p_opcionesalterset(t):
    '''opcionesalterset :   NOT NULL
                            | NULL '''

def p_tipodedrop(t):
    '''tipodedrop   :   COLUMN ID
                        | CONSTRAINT  ID'''


#------------------------------------------------------------DELETE----------------------------------------------------
def p_instrucciones_delete(t) :
    '''delete    : FROM ID WHERE condiciones PTCOMA'''

#-------------------------------------------------------INSERT-------------------------------------------
def p_instrucciones_insert(t):
    '''insert    : INTO ID VALUES PARENIZQ values PARENDER PTCOMA'''

def p_values(t):
    '''values   : values COMA value
                | value'''

def p_value(t):
    '''value   : ENTERO
                | DECIMAL
                | CADENA
                | boleano'''

#-------------------------------------------------------UPDATE-------------------------------------------
def p_instrucciones_update(t):
    '''update    : ID SET asignaciones WHERE condiciones PTCOMA'''

def p_asignaciones(t):
    '''asignaciones     : asignaciones COMA ID IGUAL argument PTCOMA
                        | ID IGUAL argument'''

#------------------------------------------------------CONDICIONES-----------------------------------------
def p_condiciones(t):
    '''condiciones    : condiciones comparacionlogica condicion
                        | condicion'''

def p_comparacionlogica(t):
    '''comparacionlogica    : AND
                            | OR'''

def p_condicion(t):
    '''condicion    : NOT condicions
                    | condicions'''

def p_condicions(t):
    '''condicions : argument MENORQUE argument
                  | argument MAYORQUE argument
                  | argument IGUAL argument
                  | argument MENORIGUALQUE argument
                  | argument MAYORIGUALQUE argument
                  | argument DIFERENTELL argument
                  | argument BETWEEN betweenopcion
                  | argument NOT BETWEEN argument AND argument
                  | argument ISNULL
                  | argument NOTNULL
                  | argument IS isopcion'''
    if t[2] == '<'    : t[0] = condicion.Condicionales(t[1], t[3], '<', None)
    elif t[2] == '>'  : t[0] = condicion.Condicionales(t[1], t[3], '>', None)
    elif t[2] == '='  : t[0] = condicion.Condicionales(t[1], t[3], '=', None)
    elif t[2] == '<=' : t[0] = condicion.Condicionales(t[1], t[3], '<=', None)
    elif t[2] == '>=' : t[0] = condicion.Condicionales(t[1], t[3], '>=', None)
    elif t[2] == '<>' : t[0] = condicion.Condicionales(t[1], t[3], '<>', None)
    elif t[2].lower() == 'between' : t[0] = condicion.Condicionales(t[1], t[3], 'between', None)
    elif t[2].lower() == 'not' : t[0] = condicion.Condicionales(t[1], t[3], 'not', t[6])
    elif t[2].lower() == 'isnull' : t[0] = condicion.Condicionales(t[1], None, 'isnull', None)
    elif t[2].lower() == 'notnull' : t[0] = condicion.Condicionales(t[1], None, 'notnull', None)
    elif t[2].lower() == 'is' : t[0] = condicion.Condicionales(t[1], t[3], 'is', None)

def p_betweenopcion(t):
    '''betweenopcion    : SYMMETRIC argument AND argument
                        | argument AND argument'''
    if t[1].lower() == 'symmetric' : t[0] = condicion.Between(True, t[2], t[4])
    else : t[0] = condicion.Between(False, t[2], t[4])

def p_isopcion(t):
    '''isopcion : DISTINCT FROM argument
                | NULL
                | TRUE
                | FALSE
                | UNKNOWN
                | NOT isnotoptions'''
    if t[1].lower() == 'distinct' : t[0] = condicion.IsNotOptions(False, t[3], True)
    elif t[1].lower() == 'null' : t[0] = condicion.IsNotOptions(False, 'null', False)
    elif t[1].lower() == 'true' : t[0] = condicion.IsNotOptions(False, 'true', False)
    elif t[1].lower() == 'false' : t[0] = condicion.IsNotOptions(False, 'false', False)
    elif t[1].lower() == 'unknown' : t[0] = condicion.IsNotOptions(False, 'unknown', False)
    elif t[1].lower() == 'not' : t[0] = condicions.IsNotOptions(True, t[2], False)

def p_isnotoptions(t):
    '''isnotoptions : FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM argument'''
    if t[1].lower() == 'null' : t[0] = 'null'
    elif t[1].lower() == 'true' : t[0] = 'true'
    elif t[1].lower() == 'false' : t[0] = 'false'
    elif t[1].lower() == 'unknown' : t[0] = 'unknown'
    elif t[1].lower() == 'distinct' :t[0] = condicion.IsNotOptions(False, t[3], True)

def p_argument_binary(t):
    '''argument : argument MAS argument
                | argument GUION argument
                | argument BARRA argument
                | argument ASTERISCO argument
                | argument PORCENTAJE argument
                | argument POTENCIA argument
                | boleano'''
    if t[2] == '+'   : t[0] = arit.Arithmetic(t[1], t[3], '+')
    elif t[2] == '-' : t[0] = arit.Arithmetic(t[1], t[3], '+')
    elif t[2] == '/' : t[0] = arit.Arithmetic(t[1], t[3], '+')
    elif t[2] == '*' : t[0] = arit.Arithmetic(t[1], t[3], '+')
    elif t[2] == '%' : t[0] = arit.Arithmetic(t[1], t[3], '+')
    elif t[2] == '\^' : t[0] = arit.Arithmetic(t[1], t[3], '+')
    else : t[0] = t[1]

def p_argument_unary(t):
    '''argument : MAS argument %prec UMAS
                | GUION argument %prec UMENOS'''
    if t[1] == '+' : t[0] = Primitive(t[2])
    else : t[0] =  t[0] = Primitive(t[2])

def p_argument_agrupacion(t):
    '''argument : PARENIZQ argument PARENDER'''
    t[0] = t[2]

def p_argument_number(t):
    '''argument : ENTERO
                | DECIMAL'''
    t[0] = t[1]

def p_argument_cadena(t):
    '''argument : CADENA'''
    t[0] = t[1]

def p_argument_id(t):
    '''argument : ID'''
    t[0] = t[1]

def p_argument_idpid(t):
    '''argument : ID PUNTO ID'''
    t[0] = t[1] + '\.' + t[3]

def p_boleano(t):
    '''boleano  : TRUE
                | FALSE'''
    if t[1].lower() == 'true' : t[0] = 'true'
    else : t[0] = 'false'

def p_error(t):
    # print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
