# coding=utf-8

from typing import NewType
from typing import Dict, List, Union

AoD = NewType('AoD', List[Dict])
Value = NewType('Value', Union[str, List, Dict])


class ArgumentError(Exception):
    """ Argument Error Exception Class
    """
    pass


class Exc:
    """ Manage Exception
    """

    @staticmethod
    def sh_d_trace(exc, sw_traceback=True):
        """ Show Exception type, message and traceback
        """
        trace_ = []
        tb_ = exc.__traceback__

        while tb_ is not None:
            trace_.append(
                {"filename": tb_.tb_frame.f_code.co_filename,
                 "name": tb_.tb_frame.f_code.co_name,
                 "lineno": tb_.tb_lineno}
            )
            # if not sw_traceback:
            #     break
            tb_ = tb_.tb_next
        d_trace = {}
        d_trace['trace'] = trace_
        d_trace['type'] = type(exc).__name__
        d_trace['exc'] = str(exc)
        return d_trace

    @staticmethod
    def sh_exc(exc, sw_traceback=True, sw_json=True):
        """ Show Exception type, message and traceback
        """
        trace_ = []
        tb_ = exc.__traceback__
        while tb_ is not None:
            trace_.append(
                {"filename": tb_.tb_frame.f_code.co_filename,
                 "name": tb_.tb_frame.f_code.co_name,
                 "lineno": tb_.tb_lineno}
            )
            if not sw_traceback:
                break
            tb_ = tb_.tb_next
        type_ = type(exc).__name__
        msg_ = str(exc)
        if sw_json:
            return {'type': type_, 'message': msg_, 'trace': trace_}
        else:
            return f"type: {type_}, message: {msg_}, trace: {trace_}"

    def get_exc(exc):
        exc_arr = list(exc.args)
        exc_msg = exc_arr.pop(0)
        return exc_msg % tuple(exc_arr)


class ExcNo(Exception):
    pass


class ExcStop(Exception):
    pass
