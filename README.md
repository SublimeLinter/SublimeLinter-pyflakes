SublimeLinter-pyflakes
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-pyflakes.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-pyflakes)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [pyflakes](https://github.com/pyflakes/pyflakes).
It will be used with files that have the "Python" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, ensure that `pyflakes` (0.7.3 or later) is installed on your system.
To install `pyflakes`, do the following:

1. Install [Python](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html). If you plan to code in Python 3, you will need to install `pip` for Python 3 as well.

1. Install `pyflakes` by typing the following in a terminal, replacing ‘x’ with the minor version installed on your system:
   ```
   # For python 2.x
   [sudo] pip-2.x install pyflakes

   # For python 3.x
   [sudo] pip-3.x install pyflakes
   ```

Please make sure that the path to `pyflakes` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html


