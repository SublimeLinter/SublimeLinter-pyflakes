SublimeLinter-pyflakes
=========================

[![Build Status](https://khancdn.eu/badges.php?service=https%3A%2F%2Ftravis-ci.org%2FSublimeLinter%2FSublimeLinter-pyflakes.png%3Fbranch%3Dmaster)](https://travis-ci.org/SublimeLinter/SublimeLinter-pyflakes)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [pyflakes](https://github.com/pyflakes/pyflakes). It will be used with files that have the “Python” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `pyflakes` is installed on your system. To install `pyflakes`, do the following:

1. Install [Python](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html). If you plan to code in Python 3, you will need to install `pip` for Python 3 as well.

1. Install `pyflakes` by typing the following in a terminal, replacing ‘x’ with the minor version installed on your system:
   ```
   # For python 2.x
   [sudo] pip-2.x install pyflakes

   # For python 3.x
   [sudo] pip-3.x install pyflakes
   ```

**Note:** This plugin requires `pyflakes` 0.7.3 or later.

### Linter configuration
In order for `pyflakes` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `pyflakes` is installed and configured, you can proceed to install the SublimeLinter-pyflakes plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `pyflakes`. Among the entries you should see `SublimeLinter-pyflakes`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-pyflakes provides its own settings. Those marked as “Inline Setting” may also be [used inline](http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings).

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|@python|A meta setting that indicates the [python version](http://sublimelinter.readthedocs.org/en/latest/meta_settings.html#python) of your source files. Use this inline or at the global level, not within the linter’s settings.|&#10003;| |

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass pyflakes and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
