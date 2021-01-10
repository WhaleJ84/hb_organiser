"""
Contains the objects used to define what makes a bundle and its components.
"""
from glob import glob
from os import listdir
from os.path import join


class Base:
    """
    The base class that contains traits shared by all classes below it.
    """
    def __init__(self, name, path):
        """

        :param name: Name of the file/directory.
        :type name: str
        :param path: Path of object.
        :type path: str
        """
        self.name = name
        self.path = join(path, self.name)

        # FileNotFound error thrown if `/path/to/file` given instead of `/path/to/file/`
        # As it creates `/path/to/file/file`. This appears to resolve that
        if self.path.split('/')[-2] == self.name:
            self.path = path

        self.items = len(glob(f"{self.path}/**", recursive=True))-1


class Library(Base):
    """
    The highest class that contains all those below it.
    """
    def __init__(self, name, path):
        """

        :param name: Name of the library.
        :type name: str
        :param path: Path of the library.
        :type path: str
        """
        super().__init__(name, path)
        self.contents = listdir(self.path)


class Bundle(Base):
    """
    Contained inside a library, and holds those below it.
    """
    def __init__(self, name, path):
        """

        :param name: Name of the bundle.
        :type name: str
        :param path: Path of bundle.
        :type path: str
        """
        super().__init__(name, path)
        self.contents = listdir(self.path)


class Item(Base):
    """
    Contained inside bundles, and has multiple files that are different platforms of the item.
    """
    def __init__(self, name, path):
        """

        :param name: Name of the item.
        :type name: str
        :param path: Path of the item.
        :type path: str
        """
        super().__init__(name, path)
        self.platforms = listdir(self.path)
        self.items = self.items - len(self.platforms)


class File(Base):
    """
    The lowest form of object. Each file is a different platform/extension of the item above it.
    """
    def __init__(self, name, path, platform):
        """

        :param name: Name of the file.
        :type name: str
        :param path: Path of the file.
        :type path: str
        :param platform: Platform of the file.
        :type platform: str
        """
        super().__init__(name, path)
        self.platform = platform
        self.filetype = name.split('.')[-1]
