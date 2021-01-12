"""
Contains methods used to check given input before operating upon it.
"""
from pathlib import Path
from os import listdir
from os.path import isdir, abspath, join

from hb_organiser.bundle_objects import Library, Bundle, Item, File


def source_exists(source):
    """
    Confirms the given library path exists.

    :param source: Absolute or relative path to downloaded library location.
    :type source: str
    :return:
    :rtype: bool
    """
    if isdir(abspath(source)):
        # for some reason this returns true when given an empty string
        # following statement should root those cases out
        if not source:
            print("ERROR: no path given")
            return False
        return True
    print(f"ERROR: specified source does not exist: {abspath(source)}")
    return False


def source_levels(source, target=None):
    """
    Tries to confirm the given library path contains bundles in the correct format.

    :param source: Absolute or relative path to downloaded library location.
    :type source: str
    :param target: Specifies the target it will check. Defaults to none.
    :type target: str
    :return:
    :rtype: bool
    """
    library = Path(abspath(source))

    # TODO: This needs to be a method within a method or something similar
    test = 'bundle'
    level = library
    try:
        if target is not None:
            bundle = abspath(f"{level}/{target}")
        else:
            bundle = Path(list(level.glob('*'))[0])

        test = 'item'
        level = bundle
        if target is not None:
            item = abspath(f"{level}/{target}")
        else:
            item = Path(list(level.glob('*'))[0])

        test = 'platform'
        level = item
        if target is not None:
            platform = abspath(f"{level}/{target}/")
        else:
            platform = Path(list(level.glob('*'))[0])
            if not isdir(platform):
                print(f"ERROR: detecting file: {platform} as platform directory")
                return False
        return True
    except IndexError:
        print(f"ERROR: could not determine {test} directory in \"{level}\"")
        return False


def number_of_items(source, filters):
    """
    Attempts to calculate how many items exist within the library that will be operated upon.

    :param source:
    :type source: str
    :param filters:
    :type filters: list
    :return:
    :rtype: int
    """
    print("[ / ] INFO: Calculating relevant items in library\r", end="", flush=True)
    library = Library(source.split('/')[-1], source)
    print(f"[ /{library.items}] INFO: Calculating relevant items in library\r", end="", flush=True)
    items = 0

    for bundle in library.contents:
        current_bundle = Bundle(bundle, library.path)

        for item in current_bundle.contents:
            current_item = Item(item, current_bundle.path)

            for platform in current_item.platforms:
                files = listdir(join(current_item.path, platform))

                for file in files:
                    current_file = File(str(file), join(current_item.path), platform)
                    if current_file.platform in filters and current_file.filetype != 'md5'\
                            or 'all' in filters and current_file.filetype != 'md5':
                        items += 1
    print(f"[{items}/{library.items}] DONE: Calculating relevant items in library", flush=True)
    return items
