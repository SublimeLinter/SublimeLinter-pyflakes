#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Pyflakes plugin linter class."""

from io import StringIO
from SublimeLinter.lint import PythonLinter


class Pyflakes(PythonLinter):

    """Provides an interface to the pyflakes python module/script."""

    syntax = 'python'
    cmd = 'pyflakes@python'
    regex = r'''(?x)
        .+?:\s*               # filename
        (?P<line>\d+):\s*     # line number

        # The rest of the line is the error message.
        # Within that, capture anything within single quotes as 'near'.
        (?P<message>[^\'\n\r]+(?P<near>\'.+?\')?.*)

        # The error message may be followed by the offending line of code...
        (?:\r?\n.*

        # and then another line with a caret (preceded by spaces)
        # pointing to the position where the error occurred.
        \r?\n(?P<col>[ ]+)\^)?
    '''
    multiline = True
    module = 'pyflakes.api'
    check_version = True

    # Internal
    reporter = None

    def check(self, code, filename):
        """Run pyflakes.check on code and return the output."""

        output = StringIO()
        reporter = self.get_reporter()
        reporter = reporter(output, output)

        self.module.check(code, filename, reporter=reporter)
        return output.getvalue()

    def get_reporter(self):
        """Return pyflakes.Reporter. Must be deferred to runtime."""
        if self.reporter is None:
            from pyflakes.reporter import Reporter
            self.__class__.reporter = Reporter

        return self.reporter
