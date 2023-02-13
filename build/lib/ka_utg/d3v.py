# coding=utf-8

from datetime import date

from ka_uts.csv import Csv as IoCsv

from typing import Dict, List, Any


class D3V:

    @staticmethod
    def set(d3_v: Dict, keys: List, value: Any) -> Dict:
        key0 = keys[0]
        key1 = keys[1]
        key2 = keys[2]
        if key0 not in d3_v:
            d3_v[key0] = {}
        if key1 not in d3_v[key0]:
            d3_v[key0][key1] = {}
        d3_v[key0][key1][key2] = value
        return d3_v

    @staticmethod
    def yield_values(d3_v: Dict):
        for key1, d2_v in d3_v.items():
            for key2, d1_v in d2_v.items():
                for key3, value in d1_v.items():
                    if isinstance(value, (list, tuple)):
                        yield (key1, key2, key3, *value)
                    else:
                        yield (key1, key2, key3, value)

    class Csv:

        @staticmethod
        def write(d3, cfg_io_out, d3_nm, **kwargs):
            _sw = kwargs.get('sw_' + d3_nm)
            if not _sw:
                return
            # _path = cfg_io_out[d3_nm]["csv"]["path"]
            _keys = cfg_io_out[d3_nm]["keys"]
            _aoa = D3V.yield_values(d3)
            today = date.today().strftime("%Y%m%d")
            _path = kwargs.get(f'path_out_{d3_nm}').format(today=today)
            IoCsv.AoA.write(_aoa, _path, _keys, **kwargs)
