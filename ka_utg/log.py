# coding=utf-8

from .com import Com


class Eq:
    """ Manage Equate Class
    """
    @staticmethod
    def sh(key, value):
        """ Show Key, Value as Equate
        """
        return f"{key} = {value}"


class Log:
    """Logging Class
    """
    class Eq:
        @staticmethod
        def debug(key, value):
            Com.Log.debug(Eq.sh(key, value), stacklevel=2)

        @staticmethod
        def info(key, value):
            Com.Log.info(Eq.sh(key, value), stacklevel=2)

    @staticmethod
    def debug(*args, **kwargs):
        Com.Log.debug(*args, stacklevel=2, **kwargs)

    @staticmethod
    def error(*args, **kwargs):
        Com.Log.error(*args, stacklevel=2, **kwargs)

    @staticmethod
    def info(*args, **kwargs):
        Com.Log.info(*args, stacklevel=2, **kwargs)

    @staticmethod
    def warning(*args, **kwargs):
        Com.Log.warning(*args, stacklevel=2, **kwargs)

    @staticmethod
    def finished(*args, **kwargs):
        Com.Log.info(
          Com.cfg.profs.msgs.finished, stacklevel=2)
        Com.Log.info(
          Com.cfg.profs.msgs.etime.format(etime=Com.ts_etime),
          stacklevel=2)
