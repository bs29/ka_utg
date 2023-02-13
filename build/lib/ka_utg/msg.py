# coding=utf-8
"""
Koskya Utilities Module
contains the Kosakya Utilitiy Classes
"""

from .com import Com as KaCom
from .col import Col as KaCol


class Level:
    """Log Level specific Text Formatting Class
    """

    @staticmethod
    def sh_color(level):
        if level == 'CRITICAL':
            return KaCol.sh_bold_red(level)
        elif level == 'ERROR':
            return KaCol.sh_bold_magenta(level)
        elif level == 'WARNING':
            return KaCol.sh_bold_yellow(level)
        elif level == 'DEBUG':
            return KaCol.sh_bold_light_green(level)
        elif level == 'INFO':
            return KaCol.sh_bold_cyan(level)
        else:
            return level


class Msg:
    """Message Class
    """

    @staticmethod
    def get(**kwargs):
        MSGS = kwargs.get('MSGS')
        if MSGS is None:
            MSGS = KaCom.MSGS
        env = kwargs.get('env')
        type = kwargs.get('type')
        fnc = kwargs.get('fnc')
        action = kwargs.get('action')
        arr = kwargs.get('arr')

        msg = MSGS[env][type][fnc][action]
        if not arr:
            return msg
        return msg.format(arr)

    @staticmethod
    def get_objs(**kwargs):
        MSGS = kwargs.get('MSGS')
        if MSGS is None:
            MSGS = KaCom.MSGS
        env = kwargs.get('env')
        type = kwargs.get('type')
        fnc = kwargs.get('fnc')
        arr = kwargs.get('arr')
        if type.endswith('class'):
            type_ = f'{type}(es)'
        else:
            type_ = f'{type}(s)'
        action = kwargs.get('action')
        if arr:
            msg = MSGS[env]['objs'][fnc][action]
            return msg.format(type_, arr)
        else:
            if action == 'ver_sel':
                msg = MSGS[env]['objs'][fnc][action]
                return msg.format(type_)
            else:
                msg = MSGS[env]['objs'][fnc]['all']
                return msg.format(type_)


class MsgFmt:
    """Message Formatting Class
    """

    @staticmethod
    def out(out, caller, out_typ='MSG'):
        if caller:
            if out:
                return f'[{caller}] {out_typ}: {out}'
            else:
                return f'[{caller}] {out_typ}: '
        else:
            if out:
                return f'{out_typ}: {out}'
            else:
                return f'{out_typ}: '

    @classmethod
    def msg(cls, msg, caller):
        return cls.out(msg, caller, out_typ='MSG')

    @classmethod
    def exc(cls, exc, caller):
        return cls.out(exc, caller, out_typ='EXC')

    @staticmethod
    def prefix(msg, prefix=None, sw_short=False):
        if not prefix:
            return msg
        if sw_short:
            prefix = prefix.split('.')[0]
        if isinstance(msg, (list, tuple)):
            msg_arr = msg.splitlines()
            zmsg = [f"[{prefix}] {line}" for line in msg_arr]
            return '\n'.join(zmsg)
        else:
            return f"[{prefix}] {msg}"

    @classmethod
    def status(cls, msg, exit_code=None, exc=None):
        if exit_code == 0:
            return cls.success(msg, exit_code)
        else:
            return cls.failed(msg, exit_code, exc)

    @classmethod
    def status_host_cmd(cls, host, cmd, exit_code, exc=None):
        msg = f"Host: [{host}] Command: [{cmd}]"
        return cls.status(msg, exit_code, exc)

    @staticmethod
    def success(msg, exit_code=None):
        if isinstance(msg, (list, tuple)):
            msg = " ".join(msg)
        success = KaCol.sh_bold_green('SUCCESS')
        if exit_code == 0:
            return f"{msg} Exit-Code:[{exit_code}] [{success}]"
        else:
            return f"{msg} [{success}]"

    @staticmethod
    def failed(msg, exit_code=None, exc=None):
        if isinstance(msg, (list, tuple)):
            msg = " ".join(msg)
        failed = KaCol.sh_bold_red('FAILED')
        if exit_code is not None:
            if exc:
                return f"{msg} Exit-Code:[{exit_code}] [{failed}] error:{exc}"
            else:
                return f"{msg} Exit-Code:[{exit_code}] [{failed}]"
        else:
            if exc:
                return f"{msg} [{failed}] error:{exc}"
            else:
                return f"{msg} [{failed}] "
