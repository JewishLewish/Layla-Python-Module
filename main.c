#include "tinyexpr.c"
#include "tinyexpr.h"

int eval(const char *a)
{
    return te_interp(a, 0);
}