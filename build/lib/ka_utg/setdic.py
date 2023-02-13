class SetDic:

    @staticmethod
    def sh(dic):
        dic_new = {}
        for key, value in dic.items():
            f_key = frozenset(key.split(','))
            dic_new[f_key] = value
        return dic_new
