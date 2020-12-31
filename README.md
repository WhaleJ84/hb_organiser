# hb-organiser

Organises Humble Bundle bundles based on their platform.
Designed to work around the structure created via Talonius' [hb-downloader](https://github.com/talonius/hb-downloader).
Other automated HB downloaders may not work with this out of the box.

## Why is this needed?

I mainly use Humble Bundle to purchase book bundles (that I'll totally read at some point, I swear!) and have accumulated thousands of books over the years.
I would like to have all these books hosted via a [Calibre](https://calibre-ebook.com/) web server for easy access but trying to weed out the books from the default structure left behind by automated downloads is a headache.

To alleviate this issue, I'm making this script that will organise my libraries with a click of a key.
Duplicate items across different bundles will be ignored, all the books will be easily discovered via Calibre, and my sanity will be saved.

## Immediate roadmap

The immediate goal is to put out something working.
To keep development more direct I'll outline pressing matters below:

- Publish Pip module
    - At the moment it currently runs as a series of scripts.
      This needs to change ASAP.
- Cut down on operation times
    - Organising thousands of files in one go is very time-consuming - especially when working with game bundles.
      Speeding this up will save millions of hours of collective time over the years via optimisation.

## Future plans

Longer term goals than those outlined above will be put here:

- Abstract all the things
    - Quite a few values are hard-coded at the moment.
      To make it more convenient for others, this should be changed to allow for more options.
- Abstract them even further
    - Why does this have to be limited to Humble Bundles?
      All its doing is moving one category of files from one place to another.
      This could be useful in other situations such as organising music.
