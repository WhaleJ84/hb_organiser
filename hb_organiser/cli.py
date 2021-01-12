#!/usr/bin/env python3.8
"""
Contains the code pertaining to the CLI. All back-end logic is located elsewhere.
"""
import argparse
from os.path import abspath
from sys import argv

from hb_organiser.check import source_exists
from hb_organiser.organiser import HBOrganiser


def cli(args=None):
    """
    Contains the code pertaining to the CLI. All back-end logic is located elsewhere.

    :return:
    """
    parser = argparse.ArgumentParser(description="organises humble bundle bundles based on their platform.")
    parser.add_argument(
        "platform", nargs="+", type=str,
        help="specifies what platform of bundles to be organised.",
        # choices=['all', 'android', 'audio', 'ebook', 'humble play', 'key', 'linux',
        #          'mac', 'origin', 'steam', 'unique links', 'video', 'windows']
        choices=['all', 'android', 'audio', 'ebook', 'linux', 'mac', 'video', 'windows']
    )
    parser.add_argument(
        "-c", "--conf", type=str,
        metavar="PATH",
        help="points to configuration file containing arguments such as source and destination. "
             "one argument is expected per line in KEY=VALUE format (e.g. SRC=/path/to/file). "
             "manually specified flags will overwrite any values specified in the file."
    )
    parser.add_argument(
        "-s", "--source", type=str,
        metavar="SRC",
        help="source directory of bundles. overrides SRC specified in config file if present."
    )
    parser.add_argument(
        "-d", "--dest", type=str,
        metavar="DEST",
        help="destination directory of sorted bundles. overrides DEST specified in config file if present. "
             "if no destination is given, a dry-run will occur - displaying what would have happened."
    )
    parser.add_argument(
        "-D", "--dry-run",
        action='store_true',
        help="performs a dry-run, not actually performing any copy operations. "
             "requires a source be specified via flag or config file to run. "
             "overwrites destination specified via flag and config file if present."
    )

    if args is not None:
        return parser.parse_args(args)
    return parser.parse_args()


def read_config(path):
    """
    Reads pre-defined arguments from the specified path.

    :param path: Path to the config file.
    :type path: str
    :return:
    """
    arguments = {}
    with open(abspath(path)) as conf:
        for line in conf:
            key, value = line.partition("=")[::2]
            arguments[key.strip()] = str(value).strip('\n')
    conf.close()
    return arguments


def verify_args(args):
    """
    Determines if the arguments given suffice or need to be overwritten.

    :param args:
    :return:
    :rtype: list
    """
    source = None
    destination = None

    if args.conf:
        conf_args = read_config(args.conf)
        source = conf_args["SRC"]
        destination = conf_args["DEST"]

    if args.source:
        source = args.source

    if args.dest:
        destination = args.dest

    if args.dry_run:
        destination = None

    if not source_exists(source):
        return [None, destination, args.platform]
    return [source, destination, args.platform]


def main():
    """
    Performs the list of tasks to be completed when called as a pip module.

    :return:
    """
    pip_arg = verify_args(cli())
    if pip_arg[0] is not None:
        pip_organiser = HBOrganiser(pip_arg[0], pip_arg[1], pip_arg[2])
        pip_organiser.loop_through_bundles()


if __name__ == '__main__':
    arg = verify_args(cli(argv[1:]))
    if arg[0] is not None:
        organiser = HBOrganiser(arg[0], arg[1], arg[2])
        organiser.loop_through_bundles()
