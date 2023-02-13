import re
import sys


class Cmdline:

    RE_CMD_LEX1 = r'''
      "((?:\\["\\]|[^"])*)"|'([^']*)'|(\\.)|(&&?|\|\|?|\d?\>|[<])|([^\s'"\\&|<>]+)|(\s+)|(.)
    '''
    RE_CMD_LEX0 = r'''
      "((?:""|\\["\\]|[^"])*)"?()|(\\\\(?=\\*")|\\")|(&&?|\|\|?|\d?>|[<])|([^\s"&|<>]+)|(\s+)|(.)
    '''
    FIELDS_PATTERN = re.compile(r"(?:\"(.*?)\"|(\S+))")

    @classmethod
    def split_by_re0(cls, s, platform='this'):
        """Multi-platform variant of shlex.split() for command-line splitting.
        For use with subprocess, for argv injection etc. Using fast REGEX.

        platform: 'this' = auto from current platform;
                  1 = POSIX;
                  0 = Windows/CMD
                  (other values reserved)
        """
        if platform == 'this':
            platform = (sys.platform != 'win32')
        if platform == 1:
            RE_CMD_LEX = cls.RE_CMD_LEX1
        elif platform == 0:
            RE_CMD_LEX = cls.RE_CMD_LEX0
        else:
            raise AssertionError('unkown platform %r' % platform)

        args = []
        accu = None   # collects pieces of one arg
        for qs, qss, esc, pipe, word, white, fail in re.findall(RE_CMD_LEX, s):
            if word:
                pass   # most frequent
            elif esc:
                word = esc[1]
            elif white or pipe:
                if accu is not None:
                    args.append(accu)
                if pipe:
                    args.append(pipe)
                accu = None
                continue
            elif fail:
                raise ValueError(f"invalid or incomplete shell string: {s}")
            elif qs:
                word = qs.replace('\\"', '"').replace('\\\\', '\\')
                if platform == 0:
                    word = word.replace('""', '"')
            else:
                word = qss   # may be even empty; must be last

            accu = (accu or '') + word

        if accu is not None:
            args.append(accu)

        return args

    @classmethod
    def split_by_re1(cls, string):
        """
        Given an argument string this attempts to split it into small parts.
        """
        rv = []
        for match in re.finditer(r"('([^'\\]*(?:\\.[^'\\]*)*)'"
                                 r'|"([^"\\]*(?:\\.[^"\\]*)*)"'
                                 r'|\S+)\s*', string, re.S):
            arg = match.group().strip()
            if arg[:1] == arg[-1:] and arg[:1] in '"\'':
                arg = arg[1:-1].encode('ascii', 'backslashreplace') \
                    .decode('unicode-escape')
            try:
                arg = type(string)(arg)
            except UnicodeError:
                pass
            rv.append(arg)
        return rv

    @classmethod
    def split_by_re2(cls, data):
        return [x[0] or x[1] for x in cls.FIELDS_PATTERN.findall(data)]
