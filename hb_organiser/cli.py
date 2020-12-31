#!/usr/bin/env python3.8
"""
Contains the code pertaining to the CLI. All back-end logic is located elsewhere.
"""
import argparse
from sys import exit as sys_exit

from hb_organiser.check import source_exists
from hb_organiser.config import Config
from hb_organiser.organiser import HBOrganiser
from hb_organiser.logger import logger


def cli():
    """
    Contains the code pertaining to the CLI. All back-end logic is located elsewhere.

    :return:
    """
    parser = argparse.ArgumentParser(description="organises humble bundle bundles based on their platform.")
    parser.add_argument(
        "platform", nargs="+", type=str,
        help="specifies what platform of bundles to be organised.",
        choices=['all', 'android', 'audio', 'ebook', 'humble play', 'key', 'linux',
                 'mac', 'origin', 'steam', 'unique links', 'video', 'windows']
    )
    parser.add_argument(
        "-s", "--source", type=str,
        metavar='SRC',
        help="source directory of bundles. overrides location specified in config file."
    )
    parser.add_argument(
        "-d", "--destination", type=str,
        metavar='DEST',
        help="destination directory of sorted bundles. overrides location specified in config file. "
             "if no destination is given, a dry run will occur - displaying what would have happened."
    )
    args = parser.parse_args()

    if args.source:
        source = args.source
    else:
        try:
            source = Config.SOURCE
            logger.debug('No source given via CLI. Reading "%s" from config', Config.SOURCE)
        except KeyError:
            source = None
            logger.debug('No source given via CLI or config. Defaulting to None')

    if args.destination:
        destination = args.destination
    else:
        try:
            destination = Config.DESTINATION
            logger.debug('No destination given via CLI. Reading "%s" from config', Config.DESTINATION)
        except KeyError:
            destination = None
            logger.debug('No destination given via CLI or config. Defaulting to None')

    if not source_exists(source):
        sys_exit(1)
    organiser = HBOrganiser(source, destination, args.platform)
    organiser.loop_through_bundles()


if __name__ == '__main__':
    cli()
