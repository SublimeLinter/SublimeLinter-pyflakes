from SublimeLinter.lint import PythonLinter
import re


class Pyflakes(PythonLinter):
    cmd = 'pyflakes'
    regex = r'''(?x)
        ^(?P<filename>[^:\n]+):(?P<line>\d+):((?P<col>\d+):)?\s

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

            match = re.search(pattern, text)
            if match:
                return line, match.start(1), match.end(1)

        return super().reposition_match(line, col, match, vv)
