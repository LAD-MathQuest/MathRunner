#------------------------------------------------------------------------------#
'''This module defines the function objects.

    The VelocityFunction  is used to compute scrolling velocity
    The BoundaryFunctions is used to compute track boundaries

    The computed values are proportional to the screen, i.e.,
    the velocity is computed in screens per second and the boundaries are
    computed as proportion of screen.
'''

import numpy        as np
import numpy.typing as npt
import numexpr      as ne

#------------------------------------------------------------------------------#
def parse_function(func: str) -> str:

    func = pt_to_numexpr         (func)
    func = replace_min_with_where(func)
    func = replace_max_with_where(func)

    return func

#------------------------------------------------------------------------------#
def eval_function(values: npt.NDArray, func: str, var_name: str) -> npt.NDArray:

    ff = ne.evaluate(func, local_dict={var_name:values, 'e':np.e, 'pi':np.pi})

    if type(values) is np.ndarray and values.size != 1 and ff.size == 1:
        ff = np.full(values.shape, ff)

    return ff

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#

translation = [['^',       '**'     ],
               ['sen',     'sin'    ],
               ['tg',      'tan'    ],
               ['arcsen',  'arcsin' ],
               ['arctg',   'arctan' ],
               ['arctg2',  'arctan2'],
               ['senh',    'sinh'   ],
               ['tgh',     'tanh'   ],
               ['arcsenh', 'arcsinh'],
               ['arctgh',  'arctanh'],
               ['ln',      'log'    ],
               ['raiz',    'sqrt'   ],
               ['módulo',  'abs'    ]]

#------------------------------------------------------------------------------#
def pt_to_numexpr(func: str) -> str:

    for ex in translation:
        func = func.replace(ex[0], ex[1])

    return func

#------------------------------------------------------------------------------#
def numexpr_to_pt(func: str) -> str:

    for ex in translation:
        func = func.replace(ex[1], ex[0])

    return func

#------------------------------------------------------------------------------#
def replace_min_with_where(s: str) -> str:

    result = ''
    i = 0

    while i < len(s):

        if s[i:i+4] == 'min(':
            i += 4
            start = i
            depth = 1
            arg1 = ''
            arg2 = ''
            comma_found = False

            while i < len(s) and depth > 0:
                if s[i] == '(':
                    depth += 1
                elif s[i] == ')':
                    depth -= 1
                elif s[i] == ',' and depth == 1 and not comma_found:
                    arg1 = s[start:i].strip()
                    start = i + 1
                    comma_found = True
                i += 1

            if comma_found:
                arg2 = s[start:i-1].strip()
                replacement = f'where({arg1}<{arg2}, {arg1}, {arg2})'
                result += replacement
            else:
                # fallback: malformed min call, keep original
                result += 'min('
        else:
            result += s[i]
            i += 1

    return result

#------------------------------------------------------------------------------#
def replace_max_with_where(s: str) -> str:

    result = ''
    i = 0

    while i < len(s):

        if s[i:i+4] == 'max(':
            i += 4
            start = i
            depth = 1
            arg1 = ''
            arg2 = ''
            comma_found = False

            while i < len(s) and depth > 0:
                if s[i] == '(':
                    depth += 1
                elif s[i] == ')':
                    depth -= 1
                elif s[i] == ',' and depth == 1 and not comma_found:
                    arg1 = s[start:i].strip()
                    start = i + 1
                    comma_found = True
                i += 1

            if comma_found:
                arg2 = s[start:i-1].strip()
                replacement = f'where({arg1}>{arg2}, {arg1}, {arg2})'
                result += replacement
            else:
                # fallback: malformed max call, keep original
                result += 'max('
        else:
            result += s[i]
            i += 1

    return result

#-----------------------------------------------------------------------------#