from SublimeLinter.lint import PythonLinter


class Pyflakes(PythonLinter):
    cmd = 'pyflakes'
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
    defaults = {
        'selector': 'source.python'
    }
