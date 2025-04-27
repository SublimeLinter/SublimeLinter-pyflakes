from SublimeLinter.lint import PythonLinter
import re


class Pyflakes(PythonLinter):
    cmd = 'pyflakes'
    regex = r'''(?x)
        ^(?P<filename>.+?):(?P<line>\d+):((?P<col>\d+):?)?\s

        # The rest of the line is the error message.
        # Within that, capture anything within single quotes as `near`.
        (?P<message>[^\'\n\r]*(?P<near>\'.+?\')?.*)
    '''
    multiline = True
    # stderr has all syntax errors, parse it via our regex
    on_stderr = None
    defaults = {
        'selector': 'source.python'
    }
    warning_msg_regex = r'''(?x)
        \b(?:
        used|
        unused|
        redefines|
        shadowed|
        (may\sbe)
        )\b
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.warning_msg_regex = re.compile(self.warning_msg_regex, 0)

    def split_match(self, match):
        # mark properly the type error message

        error = super().split_match(match)
        if self.warning_msg_regex.search(error['message']):
            error['error_type'] = 'warning'
        else:
            error['error_type'] = 'error'

        return error

    def reposition_match(self, line, col, match, vv):
        if 'imported but unused' in match.message:
            # Consider:
            #   from foo import bar
            #   import foo.bar
            # In both cases `pyflakes` reports `'foo.bar' ... unused`.

            import_id = re.escape(match.near[1:-1])  # unquote
            last_part = import_id.split('.')[-1]

            # So we match either `bar` or `foo.bar` against the line content
            text = vv.select_line(line)
            pattern = r"\s({}|{})".format(last_part, import_id)

            re_match = re.search(pattern, text)
            if re_match:
                return line, re_match.start(1), re_match.end(1)

        return super().reposition_match(line, col, match, vv)
