# hb\_organiser

[![PyPI](https://img.shields.io/pypi/v/hb-organiser.svg)](https://pypi.python.org/pypi/hb-organiser)
[![image](https://img.shields.io/pypi/pyversions/hb-organiser.svg)](https://python.org/pypi/hb-organiser)
[![Downloads](https://pepy.tech/badge/hb-organiser)](https://pepy.tech/project/hb-organiser)
[![Unittests](https://github.com/WhaleJ84/hb_organiser/workflows/Unittests/badge.svg)](https://github.com/WhaleJ84/hb_organiser/actions?query=workflow%3AUnittests)
[![codecov](https://codecov.io/gh/WhaleJ84/hb_organiser/branch/main/graph/badge.svg?token=IJSKBUAP81)](https://codecov.io/gh/WhaleJ84/hb_organiser)

Organises Humble Bundle bundles based on their platform.
Designed to work around the structure created via Talonius' [hb-downloader](https://github.com/talonius/hb-downloader).
Other automated HB downloaders may not work with this out of the box.

![An image of hb-organiser copying files](https://raw.githubusercontent.com/WhaleJ84/readme_media/main/hb_organiser_demo.png)

## Install

As it's packaged as a Pip module, `python3-pip` is required. Run `pip install --user hb-organiser` to install only for your user and omit `--user` to install for all. See `hb_organiser -h` for help.

## Why is this needed?

I mainly use Humble Bundle to purchase book bundles (that I'll totally read at some point, I swear!) and have accumulated thousands of books over the years.
I would like to have all these books hosted via a [Calibre](https://calibre-ebook.com/) web server for easy access but trying to weed out the books from the default structure left behind by automated downloads is a headache.

To alleviate this issue, I'm making this script that will organise my libraries with a click of a key.
Duplicate items across different bundles will be ignored, all the books will be easily discovered via Calibre, and my sanity will be saved.

## Features

- Calculates number of tasks so that you're not left in the dark and can tell the progress.

- A crude way of tracking files being corrupted via a cancelled transfer by logging what is being operated upon and clearing it once complete. If it doesn't get cleared, chances are it was corrupted.

- Skips copying of duplicate files by checking for its existence first (although there is a chance it may skip newer files such as updated editions of books (see [issue 6](https://github.com/WhaleJ84/hb_organiser/issues/6))).
