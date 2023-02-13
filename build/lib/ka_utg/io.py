# coding=utf-8

from datetime import date

import pprint

from .com import Com
from .d3v import D3V
from .log import Log

from ka_uts.json import Json
from ka_uts.csv import Csv


class Arr:
    """ io for Array
    """
    @staticmethod
    def write(arr, path):
        with open(path, 'wt') as fd:
            string = '\n'.join(arr)
            fd.write(string)


class XmlStr:
    """ io for Xml String
    """
    def write(xmlstr, path_):
        with open(path_, 'w') as fd:
            fd.write(xmlstr)


class AoA:
    """ io for Dictionary
    """
    class Csv:

        @staticmethod
        def xwrite(aoa, path_, keys_, delimiter=',', quote='"'):
            Csv.AoA.write(
              aoa, path_, keys_, delimiter=delimiter, quote=quote)


class Dic:
    """ io for Dictionary
    """
    class Csv:

        class Arr:

            @staticmethod
            def xwrite(dic, keys_dic, delimiter):
                return Csv.Dic.write(dic, keys_dic, delimiter)

        @staticmethod
        def xwrite(aod, path_, keys_dic, delimiter=',', quote='"'):
            Csv.AoD.write(
              aod, path_, keys_dic, delimiter=delimiter, quote=quote)

    class Txt:
        def write(dic, path_, indent=2):
            data = pprint.pformat(dic, indent=indent)
            with open(path_, 'w') as fd:
                fd.write(data)

    class Json:
        def write(dic, path_, indent=2):
            Json.Dic.write(dic, path_, indent=indent)


class D3:

    class Csv:

        def xwrite(d3, d3_nm, **kwargs):
            d3_sw = kwargs.get('sw_' + d3_nm)
            Log.Eq.info("d3_sw", d3_sw)
            if not d3_sw:
                return
            today = date.today().strftime("%Y%m%d")
            d3_cfg = Com.cfg["io"]["out"][d3_nm]
            d3_path = kwargs.get(f'path_out_{d3_nm}')
            # d3_path = d3_cfg["csv"]["path"]
            d3_path = d3_path.format(today=today)
            d3_keys = d3_cfg["keys"]
            d3_aoa = D3V.yield_values(d3)
            AoA.Csv.write(d3_aoa, d3_path, d3_keys)
