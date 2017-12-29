SublimeLinter-pyflakes
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-pyflakes.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-pyflakes)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [pyflakes](https://github.com/pyflakes/pyflakes). It will be used with files that have the “Python” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `pyflakes` (0.7.3 or later) is installed on your system. To install `pyflakes`, do the following:

1. Install [Python](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html). If you plan to code in Python 3, you will need to install `pip` for Python 3 as well.

1. Install `pyflakes` by typing the following in a terminal, replacing ‘x’ with the minor version installed on your system:
   ```
   # For python 2.x
   [sudo] pip-2.x install pyflakes

   # For python 3.x
   [sudo] pip-3.x install pyflakes
   ```

In order for `pyflakes` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-pyflakes settings:

|Setting|Description|
|:------|:----------|
|python|A meta setting that indicates the [python version](http://sublimelinter.readthedocs.org/en/latest/meta_settings.html#python) of your source files.|

