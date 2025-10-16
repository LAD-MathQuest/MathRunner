#------------------------------------------------------------------------------#
'''Describes game objects'''

from io import BytesIO
from .meta_image import MetaImage

#------------------------------------------------------------------------------#
class MetaObject:

    #--------------------------------------------------------------------------#
    def __init__(
        self,
        image: MetaImage,
        score: float = 0.0,
        sound: BytesIO | None = None,
        volume: float = 1.0
    ) -> None:
        """
        Create a MetaObject
        :param image: The object image
        :type  image: MetaImage
        :param score: Points gain if player touch the object
        :type  score: float
        :param sound: The sound to play of player touch the object
        :type  sound: BytesIO | None
        :param volume: Sound volume
        :param volume: float
        """

        self.image  = image
        self.score  = score
        self.sound  = sound
        self.volume = volume

#------------------------------------------------------------------------------#