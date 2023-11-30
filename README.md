Simple Stats
============

This package allows you to compute simple stats over a set of numbers.

## Installation

Create your own virtual environment and, within it, run the following command:

    $ python3 setup.py install

## Usage

Use this in your Python REPL:

    from simple_stats import Capture
    capture = Capture()
    capture.add(3)
    capture.add(10)
    capture.add(4)
    capture.add(9)
    capture.add(7)

**Notes:** Trying to add a value not in the integer range 0 to 999 will result in an error.

Then, compute the stats:

_please note: according to the rules, computing the stats does not depend on the number of input elements. It actually depends on the maximum allowed value._

    stats = capture.build_stats()
    stats.less(7)  # will return 2 in this example
    stats.less(3)  # will return 0 in this example
    stats.greater(7)  # will return 2 in this example
    stats.greater(9)  # will return 1 in this example
    stats.greater(10)  # will return 0 in this example
    stats.between(4, 9)  # will return 3
    stats.between(-1, 7)  # will return 3
    stats.between(9, 13)  # will return 2

## Testing

If you want to test this repository then just do this after cloning this repo:

    $ pip install -U pytest
    $ cd challenge-team-international/
    $ pytest
