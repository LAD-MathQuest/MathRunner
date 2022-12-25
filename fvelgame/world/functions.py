#------------------------------------------------------------------------------#

'''This module defines the function objects.

    The VelocityFunction is used to compute scrolling velocity
    The MarginFunctions  is used to compute track margins

    The computed values are proportional to the screen, i.e.,
    the velocity is computed in screens per second and the margins are
    computed as proportion of screen.
'''

#------------------------------------------------------------------------------#
class VelocityFunction:
    '''Define the scrolling velocity in screens per second

    velocity = 1 means the length of the screen scrolls completelly 
    in one second.
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #--------------------------------------------------------------------------#
    def eval(self, time):
        return self.a + time * self.b

#------------------------------------------------------------------------------#
class MarginFunctions:
    '''Define minimal and maximal (left and rigth) track margins.'''

    #--------------------------------------------------------------------------#
    def __init__(self, min_, max_):
        self.const_min = min_
        self.const_max = max_

    #--------------------------------------------------------------------------#
    def eval_min(self, time):
        return self.const_min

    #--------------------------------------------------------------------------#
    def eval_max(self, time):
        return self.const_max

    #--------------------------------------------------------------------------#
    def eval(self, time):
        '''Eval margins and return minimum and length'''
        return ( self.const_min, self.const_max-self.const_min )

#------------------------------------------------------------------------------#
