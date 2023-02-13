# coding=utf-8

from typing import NewType
from typing import Dict, List, Union

# AoD = NewType('AoD', List[Dict])
Value = NewType('Value', Union[str, List, Dict])


class DoO:
    """ Manage Dictionary of Objects
    """
    @classmethod
    def replace_keys(cls, d_old, keys):
        """ recurse through the dictionary while building a new one
            with new keys from a keys dictionary
        """
        d_new = {}
        for key in d_old.keys():
            if key in keys:
                key_new = keys[key]
            else:
                key_new = key
            if isinstance(d_old[key], dict):
                d_new[key_new] = cls.replace_keys(d_old[key], keys)
            elif isinstance(d_old[key], (list, tuple)):
                aod_old = d_old[key]
                aod_new = []
                for item in aod_old:
                    if isinstance(item, dict):
                        item_new = cls.replace_keys(item, keys)
                        aod_new.append(item_new)
                d_new[key_new] = aod_new
                # d_new[key_new] = AoD.replace_keys(d_old[key], keys)
            else:
                d_new[key_new] = d_old[key]
        return d_new
