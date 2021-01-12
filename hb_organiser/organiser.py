"""
The bulk of the main project logic is here.
"""
from os import listdir
from os.path import isdir, isfile, join
from pathlib import Path
from shutil import copyfile

from hb_organiser.bundle_objects import Library, Bundle, Item, File
from hb_organiser.check import number_of_items, source_levels


class HBOrganiser:
    """
    Main program. Contains the methods used to organise the library.
    """
    def __init__(self, source, destination=None, *filtered_platforms):  # pylint: disable=keyword-arg-before-vararg
        print("INFO: Connecting to library\r", end="")
        self.library = Library(source.split('/')[-1], source)
        print("DONE: Connecting to library\r", end="", flush=True)
        self.destination = destination

        # TODO: clean this up. by default it would be a list within a list: [['all']]
        self.filtered_platforms = []
        for platform in filtered_platforms:
            self.filtered_platforms.append(platform)
        self.filtered_platforms = self.filtered_platforms[0]

        self.tasks = number_of_items(source, self.filtered_platforms)

    def ensure_directory_exists(self, target, task=None):
        """
        Ensures destination directory exists.
        Creates it if not.

        :param target: A path to the destination directory required.
        :type target: str
        :param task: An optional progress indicator passed through.
        :type task: str
        :return:
        """
        destination = join(self.destination, target)
        if not isdir(destination):
            print(f"{task} MKDIR: {destination}")
            Path(destination).mkdir(parents=True, exist_ok=True)

    def copy_file(self, source, destination, task=None):
        """
        Copies the source to the destination.
        Before each operation, the source file is logged.
        Should the program end unexpectedly, the file will not be cleared from the log.

        Upon next copy operation, said file will be re-copied in case of corruption.

        :param source: The path to the source file that will be copied.
        :type source: str
        :param destination: The path to the destination that the source will be copied to.
        :type destination: str
        :param task: An optional progress indicator passed through.
        :type task: str
        :return:
        """
        complete = 'DONE'
        try:
            log = open('queue.txt')
            if source not in log and not isfile(destination):
                log.close()
                print(f"{task} COPYING: {source} {destination}\r", end="", flush=True)
                complete = 'COPIED'
                log = open('queue.txt', 'w')
                log.write(source)
                log.close()
            elif source in log:
                log.close()
                print(f"{task} RE-COPING: {source} {destination}\r", end="", flush=True)
                complete = 'RE-COPIED'
            else:
                log.close()
                print(f"{task} SKIPPED: {destination}")
                return True
        except FileNotFoundError:
            print(f"{task} INFO: Creating queue.txt")
            open('queue.txt', 'x')
            self.copy_file(source, destination, task)

        copyfile(source, destination)
        print(f"{task} {complete}: {source} {destination}\r", flush=True)

        entries = []
        log = open('queue.txt')
        for entry in log:
            if source not in entry:
                entries.append(entry)
        log.close()

        log = open('queue.txt', 'w')
        log.writelines(entries)
        log.close()
        return True

    def loop_through_bundles(self):
        """
        Loops through specific bundles in the library based on the filters given.
        On each relevant hit, if a destination was given it will copy the source there.
        Without a destination, the program will do a dry-run and output what would have happened.

        :return:
        :rtype: bool
        """
        try:  # pylint: disable=too-many-nested-blocks
            task = 1
            # Go through every bundle in library
            for bundle in self.library.contents:
                source_levels(self.library.path, bundle)
                current_bundle = Bundle(bundle, self.library.path)

                # Go through every item in bundle
                for item in current_bundle.contents:
                    current_item = Item(item, current_bundle.path)

                    # Go through every platform item has
                    for platform in current_item.platforms:
                        files = listdir(join(current_item.path, platform))

                        # Go through every file the item's platform has
                        for file in files:
                            current_file = File(str(file), join(current_item.path, platform), platform)
                            if current_file.platform in self.filtered_platforms or 'all' in self.filtered_platforms:
                                current_task = f'[{task}/{self.tasks}]'
                                if current_file.filetype != 'md5':
                                    if not self.destination:
                                        print(f"{current_task} {current_file.name} > "
                                              f"$DESTINATION/{current_file.platform}/{current_file.name}")
                                    else:
                                        target = join(self.destination, f"{current_file.platform}/{current_item.name}")
                                        self.ensure_directory_exists(target, current_task)
                                        self.copy_file(current_file.path, f"{target}/{current_file.name}", current_task)

                                    task += 1
            return True
        except KeyboardInterrupt:
            print('\nINFO: Manual intervention. exiting.')
            return False
