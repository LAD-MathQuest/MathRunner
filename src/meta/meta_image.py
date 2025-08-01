#------------------------------------------------------------------------------#
'''Describes an image to be used on game'''

from typing import Self

from .read_bytes_io import read_bytes_io

#------------------------------------------------------------------------------#
class MetaImage:

    #--------------------------------------------------------------------------#
    def __init__(
        self,
        size = None,
        color = (0, 0, 0)
    ) -> None:
        """
        Create an empty MetaImage

        :param size: (width, height)
        :param color: (R,G,B)
        """

        self.size  = size
        self.color = color
        self.data  = None

    #--------------------------------------------------------------------------#
    @classmethod
    def from_file(cls, path, size = None) -> Self:
        """
        Load a file and store it as a BytesIO

        :param path: Image file path
        :param size: Optional image size (width, height)
        """

        meta = cls(size = size)
        meta.data = read_bytes_io(path)

        return meta

#------------------------------------------------------------------------------#