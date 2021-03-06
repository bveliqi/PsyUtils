# PsyUtils

[![DOI](https://zenodo.org/badge/4023/tomwallis/PsyUtils.svg)](https://zenodo.org/badge/latestdoi/4023/tomwallis/PsyUtils)

[![Build Status](https://travis-ci.org/tomwallis/PsyUtils.svg?branch=master)](https://travis-ci.org/tomwallis/PsyUtils)

[![Coverage Status](https://coveralls.io/repos/github/tomwallis/PsyUtils/badge.svg?branch=master)](https://coveralls.io/github/tomwallis/PsyUtils?branch=master)

The ``psyutils`` package is a collection of utility functions useful
for generating visual stimuli and image analysis in Python. It is a work in progress, and changes as I work. It includes various helper functions for dealing with images, including creating and applying various filters in the frequency domain.

It is **NOT** an experimental display software package. It is intended
to compliment something like [PsychoPy](http://www.psychopy.org).

It is intended only for internal use in [my](http://www.tomwallis.info) science at this stage. It is provided publicly to facilitate reproducibility of research. *Use these functions at your own risk.* Everything, including testing, is incomplete and open to change at any time.

## Submodules

 * ``image``. The ``image`` subpackage includes functions for filtering
  images and creating filtered noise stimuli, and otherwise interacting
  with images.
 * ``dist``: functions for creating probability distributions over axes. Currently just used to create filters.
 * ``im_data``. The ``im_data`` subpackage includes images and data for
  testing purposes.
 * ``files``: contains helper functions for working with directories and file structures.
  * ``misc``. This is a miscellaneous subpackage.

## Example Use

You could do things like this::

    import numpy as np
    import psyutils as pu
    im = np.random.uniform(size=(256, 256))
    filt = pu.image.make_filter_lowpass(im_size, cutoff=8)
    im2 = pu.image.filter_image(im, filt)
    pu.image.show_im(im2)


## Dependencies

See `setup.py` for current dependencies.

## Building

To build the package, use:

```
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```

## Testing

You can run unit tests by typing

`nosetests -v --with-coverage --cover-package=psyutils`

from the command line in the project's parent directory.

## TODO
  * more unit tests for filters, axes, windowing, misc
  * check documentation for filters
  * improve sphinx docs and linking

## Contributions

Thomas Wallis wrote the package. Many image processing functions are based on Matlab code from Peter Bex's lab. I also adapted some stuff from the scikit-image package.

## Thanks To

Many of the image processing functions are based on Matlab functions originally written by Peter Bex. Tom Wallis also thanks Matthias Kümmerer and David Janssen for Python help and suggestions.
