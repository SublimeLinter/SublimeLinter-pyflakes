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
    regex = (
        r'^.+?:(?P<line>\d+):\s*(?P<error>[^\']+(?P<near>\'.+?\')?.*)'
        r'(?:\n(?P<code>.+)'
        r'\n(?P<pos>\s+)\^)?'
    )
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

    def split_match(self, match):
        match, row, col, error_type, error, near = super().split_match(match)
        pos = match.group('pos')

        if pos:
            col = len(pos)

        return match, row, col, error_type, error, near
