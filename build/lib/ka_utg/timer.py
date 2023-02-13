# coding=utf-8

from datetime import datetime
# import pendulum

from .com import Com


class Timer:
    """ Timer Management
    """
    def start(package: str, module: str):
        """ start Timer
        """
        if package not in Com.d_timer:
            Com.d_timer[package] = {}
        if module is not None:
            if module not in Com.d_timer[package]:
                Com.d_timer[package][module] = {}
            Com.d_timer[package][module]["start"] = datetime.now()
            # Com.d_timer[package][module]["start"] = pendulum.now()
        else:
            Com.d_timer[package]["start"] = datetime.now()
            # Com.d_timer[package]["start"] = pendulum.now()

    def end(package: str, module: str):
        """ end Timer
        """
        if module is not None:
            start = Com.d_timer[package][module]["start"]
            end = datetime.now()
            # end = pendulum.now()
            # elapse_time = end-start
            elapse_time_sec = end.timestamp()-start.timestamp()
            # elapse_time_sec = end.diff(start).in_words()
            msg = f"{package}.{module} elapse time [sec] = {elapse_time_sec}"
        else:
            start = Com.d_timer[package]["start"]
            end = datetime.now()
            # end = pendulum.now()
            # elapse_time = end-start
            elapse_time_sec = end.timestamp()-start.timestamp()
            # elapse_time_sec = end.diff(start).in_words()
            msg = f"{package} elapse time [sec] = {elapse_time_sec}"

        Com.Log.info(msg, stacklevel=2)
