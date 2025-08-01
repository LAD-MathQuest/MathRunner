#------------------------------------------------------------------------------#
'''Describes game objects'''

#------------------------------------------------------------------------------#
class MetaObject:

    #--------------------------------------------------------------------------#
    def __init__(self, image, score=0, sound=None, volume=1.0 ):

        self.image  = image   # MetaImage
        self.score  = score
        self.sound  = sound   # Sound path
        self.volume = volume  # Sound volume

#------------------------------------------------------------------------------#