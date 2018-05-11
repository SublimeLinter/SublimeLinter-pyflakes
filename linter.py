from SublimeLinter.lint import PythonLinter


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
