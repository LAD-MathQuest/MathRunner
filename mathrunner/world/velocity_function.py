#------------------------------------------------------------------------------#
'''This module defines the function objects.

    The VelocityFunction  is used to compute scrolling velocity
    The BoundaryFunctions is used to compute track boundaries

    The computed values are proportional to the screen, i.e.,
    the velocity is computed in screens per second and the boundaries are
    computed as proportion of screen.
'''

from .math_function import parse_function, eval_function

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
        self.fvel_raw  = parse_function(func_orig)
        self.fvel      = parse_function(f'max(0.01,{self.fvel_raw})')

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
        return eval_function(time, self.fvel_raw, 't')

    #--------------------------------------------------------------------------#
    def eval(self, time):
        return eval_function(time, self.fvel, 't')

#------------------------------------------------------------------------------#
