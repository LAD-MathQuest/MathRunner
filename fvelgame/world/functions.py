#------------------------------------------------------------------------------#

'''This module defines the function objects.

    The VelocityFunction  is used to compute scrolling velocity
    The BoundaryFunctions is used to compute track boundaries

    The computed values are proportional to the screen, i.e.,
    the velocity is computed in screens per second and the boundaries are
    computed as proportion of screen.
'''

import numpy   as np
import numexpr as ne

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
def pt_to_numexpr(func):

    for ex in translation:
        func = func.replace(ex[0], ex[1])

    return func

#------------------------------------------------------------------------------#
def numexpr_to_pt(func):

    for ex in translation:
        func = func.replace(ex[1], ex[0])

    return func

#------------------------------------------------------------------------------#
def eval_function(values, func, var_name):

    ff = ne.evaluate(func, local_dict={var_name:values, 'e':np.e, 'pi':np.pi})

    if type(values) == np.ndarray and values.size != 1 and ff.size == 1:
        ff = np.full(values.shape, ff)

    return ff

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class VelocityFunction:
    '''Define the scrolling velocity in screens per second

    The velocity is a function of time in seconds

    Velocity = 1 means the length of the screen scrolls completelly
    in one second.
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, func=''):
        self.func = pt_to_numexpr(func)

    #--------------------------------------------------------------------------#
    def set_function(self, func):
        self.func = pt_to_numexpr(func)

    #--------------------------------------------------------------------------#
    def get_function(self):
        return numexpr_to_pt(self.func)

    #--------------------------------------------------------------------------#
    def eval(self, time):
        return eval_function(time, self.func, 't')

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class BoundaryFunctions:
    '''Define minimal and maximal (left and rigth) track boundaries

    Boundaries are funcion of the displacement in screen units

    The values are in fractions of the screen length
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, func_min='', func_max=''):
        self.func_min = pt_to_numexpr(func_min)
        self.func_max = pt_to_numexpr(func_max)

    #--------------------------------------------------------------------------#
    def set_function_min(self, func):
        self.func_min = pt_to_numexpr(func)

    #--------------------------------------------------------------------------#
    def set_function_max(self, func):
        self.func_max = pt_to_numexpr(func)

    #--------------------------------------------------------------------------#
    def get_function_min(self):
        return numexpr_to_pt(self.func_min)

    #--------------------------------------------------------------------------#
    def get_function_max(self):
        return numexpr_to_pt(self.func_max)

    #--------------------------------------------------------------------------#
    def eval(self, xx):
        mm = eval_function(xx, self.func_min, 'x')
        MM = eval_function(xx, self.func_max, 'x')
        return (mm, MM)

    #--------------------------------------------------------------------------#
    def eval_min(self, xx):
        return eval_function(xx, self.func_min, 'x')

    #--------------------------------------------------------------------------#
    def eval_max(self, xx):
        return eval_function(xx, self.func_max, 'x')

    #--------------------------------------------------------------------------#
    def eval_length(self, xx):
        '''Eval Boundaries and return minimum and length'''

        mm = eval_function(xx, self.func_min, 'x')
        MM = eval_function(xx, self.func_max, 'x')

        return (mm, MM-mm)

#------------------------------------------------------------------------------#
