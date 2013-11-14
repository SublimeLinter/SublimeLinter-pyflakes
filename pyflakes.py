#
# pyflakes.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ryan Hileman and Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-pyflakes
# License: MIT
#

import re
import sublime
import sys

from SublimeLinter.lint import Linter
from SublimeLinter.lint.util import which

SHEBANG_RE = re.compile(r'#!(?:(?:/[^/]+)*[/ ])?python3')
NAME_RE = re.compile(r'.*\'(\w+)\'')


class Pyflakes(Linter):
    language = 'python'
    executable = 'pyflakes'
    regex = r'''
        .+?:\s*               # filename
        (?P<line>\d+):\s*     # line number

        # The rest of the line is the error message.
        # Within that, capture anything within single quotes as 'near'.
        (?P<error>[^\'\n\r]+(?P<near>\'.+?\')?.*)

        # The error message may be followed by the offending line of code...
        (?:\r?\n.*

        # and then another line with a caret (preceded by spaces)
        # pointing to the position where the error occurred.
        \r?\n(?P<col>\s+)\^)?
    '''
    re_flags = re.VERBOSE
    multiline = True
    comment_re = r'\s*#'
    python3 = None
    pyflakes = None

    def cmd(self):
        use_python3 = False

        if (self.filename or '').startswith(sublime.packages_path()):
            if sys.version_info >= (3, 0):
                use_python3 = True

        if not use_python3:
            use_python3 = SHEBANG_RE.match(self.code) is not None

            if not use_python3:
                use_python3 = self.get_view_settings().get('language') == 'python3'

        if use_python3:
            if self.python3 is None:
                self.python3 = which('python3') or ''

            if self.python3:
                return (self.python3, self.executable_path)
            else:
                return None
        else:
            return self.executable_path
