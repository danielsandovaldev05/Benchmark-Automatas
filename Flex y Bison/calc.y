%{
#include <stdio.h>
#include <stdlib.h>
extern FILE *yyin;
void yyerror(const char *s);
int yylex();
%}

%token NUMBER NEWLINE
%left '+' '-'
%left '*' '/'

%%
input:
    | input line
    ;

line: NEWLINE
    | expr NEWLINE
    ;

expr: NUMBER            { $$ = $1; }
    | expr '+' expr     { $$ = $1 + $3; }
    | expr '-' expr     { $$ = $1 - $3; }
    | expr '*' expr     { $$ = $1 * $3; }
    | expr '/' expr     { $$ = $1 / $3; }
    | '(' expr ')'      { $$ = $2; }
    ;
%%

void yyerror(const char *s) {
    // Silenciar errores para el benchmark
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *f = fopen(argv[1], "r");
        if (f) yyin = f;
    }
    yyparse();
    return 0;
}