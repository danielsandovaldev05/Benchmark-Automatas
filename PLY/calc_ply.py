import sys
import ply.lex as lex
import ply.yacc as yacc

tokens = ('NUMBER', 'NEWLINE')
literals = ['+', '-', '*', '/', '(', ')']

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n'
    return t

def t_error(t):
    t.lexer.skip(1)

# Corregido: lex.lex() solo usa optimize (0 para desarrollo/sin escribir tablas de optimización forzosa)
lexer = lex.lex(optimize=0)

def p_input(p):
    '''input :
             | input line'''
    pass

def p_line(p):
    '''line : NEWLINE
            | expr NEWLINE'''
    pass

def p_expr(p):
    '''expr : NUMBER
            | expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | '(' expr ')' '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/' and p[3] != 0:
        p[0] = p[1] / p[3]
    elif len(p) == 4 and p[1] == '(':
        p[0] = p[2]

def p_error(p):
    pass

parser = yacc.yacc(write_tables=False, debug=False)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
        parser.parse(content, lexer=lexer)