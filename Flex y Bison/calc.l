%{
#include "calc.tab.h"
#include <stdlib.h>
%}

%%
[0-9]+          { yylval = atoi(yytext); return NUMBER; }
[ \t]+          ; /* Ignorar espacios y tabulaciones */
\n              { return NEWLINE; }
[-+*/()]        { return yytext[0]; }
.               ; /* Ignorar otros caracteres */
%%

int yywrap() { return 1; }