#------------------------------------------------------------------------------#

'''This module defines the function objects.

    The VelocityFunction  is used to compute scrolling velocity
    The BoundaryFunctions is used to compute track boundaries

    The computed values are proportional to the screen, i.e.,
    the velocity is computed in screens per second and the boundaries are
    computed as proportion of screen.
'''

import world.math_function as mf

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class VelocityFunction:
    '''Define the scrolling velocity in screens per second

    The velocity is a function of time in seconds

    Velocity = 1 means the length of the screen scrolls completelly
    in one second.
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, func_orig: str = '') -> None:
        self.set_function(func_orig)

    #--------------------------------------------------------------------------#
    def set_function(self, func_orig: str) -> None:
        self.fvel_orig = func_orig
        self.fvel_raw  = mf.parse_function(func_orig)
        self.fvel      = mf.parse_function(f'max(0.01,{self.fvel_raw})')

    #--------------------------------------------------------------------------#
    def get_function_orig(self) -> str:
        return self.fvel_orig

    #--------------------------------------------------------------------------#
    def get_function_raw(self) -> str:
        return self.fvel_raw

    #--------------------------------------------------------------------------#
    def get_function(self) -> str:
        return self.fvel

    #--------------------------------------------------------------------------#
    def eval_raw(self, time):
        return mf.eval_function(time, self.fvel_raw, 't')

    #--------------------------------------------------------------------------#
    def eval(self, time):
        return mf.eval_function(time, self.fvel, 't')

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class BoundaryFunctions:
    '''Define minimal and maximal (left and rigth) track boundaries

    Boundaries are funcion of the displacement in screen units

    The values are in fractions of the screen length
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, f_min: str = '', f_max: str = '') -> None:
        self.set_function_min(f_min)
        self.set_function_max(f_max)

    #--------------------------------------------------------------------------#
    def set_functions(self, f_min: str, f_max: str) -> None:
        self.set_function_min(f_min)
        self.set_function_max(f_max)

    #--------------------------------------------------------------------------#
    def set_function_min(self, func_orig: str) -> None:
        self.fmin_orig = func_orig
        self.fmin_raw  = mf.parse_function(func_orig)
        self.fmin      = mf.parse_function(f'min(100, max(0,{self.fmin_raw}))')

    #--------------------------------------------------------------------------#
    def set_function_max(self, func_orig: str) -> None:
        self.fmax_orig = func_orig
        self.fmax_raw  = mf.parse_function(func_orig)
        self.fmax      = mf.parse_function(f'min(100, max(0,{self.fmax_raw}))')

    #--------------------------------------------------------------------------#
    def get_function_min_orig(self) -> str:
        return self.fmin_orig

    #--------------------------------------------------------------------------#
    def get_function_min_raw(self) -> str:
        return self.fmin_raw

    #--------------------------------------------------------------------------#
    def get_function_min(self) -> str:
        return self.fmin

    #--------------------------------------------------------------------------#
    def get_function_max_orig(self) -> str:
        return self.fmax_orig

    #--------------------------------------------------------------------------#
    def get_function_max_raw(self) -> str:
        return self.fmax_raw

    #--------------------------------------------------------------------------#
    def get_function_max(self) -> str:
        return self.fmax

    #--------------------------------------------------------------------------#
    def eval_raw(self, xx):
        return (
            mf.eval_function(xx, self.fmin_raw, 'x'),
            mf.eval_function(xx, self.fmax_raw, 'x')
        )

    #--------------------------------------------------------------------------#
    def eval(self, xx):
        return (
            mf.eval_function(xx, self.fmin, 'x'),
            mf.eval_function(xx, self.fmax, 'x')
        )

    #--------------------------------------------------------------------------#
    def eval_min_raw(self, xx):
        return mf.eval_function(xx, self.fmin_raw, 'x')

    #--------------------------------------------------------------------------#
    def eval_min(self, xx):
        return mf.eval_function(xx, self.fmin, 'x')

    #--------------------------------------------------------------------------#
    def eval_max_raw(self, xx):
        return mf.eval_function(xx, self.fmax_raw, 'x')

    #--------------------------------------------------------------------------#
    def eval_max(self, xx):
        return mf.eval_function(xx, self.fmax, 'x')

#------------------------------------------------------------------------------#
