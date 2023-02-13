# coding=utf-8


class EvtHandle:
    """Event Handler Class
    """
    @staticmethod
    def sh_evargs(env, type, action):
        return {'env': env, 'type': type, 'action': action}
