# coding=utf-8

import calendar
import logging
import logging.config
import os
import pkg_resources
import time

from ka_uts.yaml import Yaml
from ka_uts.jinja2 import Jinja2

from .pacmod import Pacmod

from typing import Dict


class Com:

    """Communication Class
    """
    cfg = None
    pid = None
    Log = None
    pacmod_curr = None
    ts_start = None
    ts_end = None
    ts_etime = None
    d_timer = None

    class Main:

        class Log:
            cfg = None
            log = None

            @classmethod
            def read(cls, pacmod: Dict):
                tenant = pacmod['tenant']
                package = pacmod['package']
                module = pacmod['module']
                pid = Com.pid
                ts = Com.ts_start
                filename = 'log.main.tenant.yml'
                path = Pacmod.Path.Log.sh_cfg(filename=filename)
                print("==================================")
                print(f"path = {path}")
                print("==================================")
                log_main = Jinja2.read(
                    path,
                    tenant=tenant,
                    package=package,
                    module=module,
                    pid=pid,
                    ts=ts)
                return log_main

            @classmethod
            def init_handler(cls, handler, key, value):
                cls.cfg['handlers'][handler][key] = value

            @classmethod
            def set_level(cls, sw_debug):
                if sw_debug:
                    cls.init_handler(
                      'main_debug_console', 'level', logging.DEBUG)
                    cls.init_handler(
                      'main_debug_file', 'level', logging.DEBUG)
                else:
                    cls.init_handler(
                      'main_debug_console', 'level', logging.INFO)
                    cls.init_handler(
                      'main_debug_file', 'level', logging.INFO)

            @classmethod
            def init(cls, **kwargs):
                pacmod_curr = Com.pacmod_curr
                sw_debug = kwargs.get('sw_debug')
                if cls.log is not None:
                    return
                cls.cfg = cls.read(pacmod_curr)
                cls.set_level(sw_debug)
                logging.config.dictConfig(cls.cfg)
                cls.log = logging.getLogger('main')
                Com.Log = cls.log

    class Mgo:

        client = None

    class Person:

        class Log:

            cfg = None
            log = None

            @classmethod
            def read(cls, pacmod, person):
                package = pacmod.package
                module = pacmod.module
                person = person
                pid = Com.pid
                ts = Com.ts_start
                filename = 'log.person.yml'
                path = Pacmod.Path.Log.sh_cfg(filename=filename)
                return Jinja2.read(
                    path,
                    package=package,
                    module=module,
                    person=person,
                    pid=pid,
                    ts=ts)

            @classmethod
            def init_handler(cls, handler, key, value):
                cls.cfg['handlers'][handler][key] = value

            @classmethod
            def set_level(cls, person, sw_debug):
                if sw_debug:
                    cls.init_handler(
                      f'{person}_debug_console', 'level', logging.DEBUG)
                    cls.init_handler(
                      f'{person}_debug_file', 'level', logging.DEBUG)
                else:
                    cls.init_handler(
                      f'{person}_debug_console', 'level', logging.INFO)
                    cls.init_handler(
                      f'{person}_debug_file', 'level', logging.INFO)

            @classmethod
            def init(cls, pacmod: Dict, person, sw_debug):
                # if cls.log is not None:
                #     return
                cfg = cls.read(pacmod, person)
                if cfg is None:
                    return
                cls.cfg = cfg
                cls.set_level(person, sw_debug)

                logging.config.dictConfig(cls.cfg)
                cls.log = logging.getLogger(person)
                Com.Log = cls.log

    class Msh:

        msh = None
        cfg = None

        @classmethod
        def init(cls, pacmod: Dict):
            """ the package data directory has to contain a __init__.py
                file otherwise the objects notation {package}.data to
                locate the package data directory is invalid
            """
            if cls.mah is not None:
                return
            try:
                package_ = f"{pacmod.package}.data"
                file_ = f"{pacmod.module}.yml"
                zpath = pkg_resources.resource_filename(package_, file_)
                cls.cfg = Yaml.read(zpath)
            except Exception as e:
                Com.Log.log.error(e, exc_info=True)
                raise

    class App:

        sw_init = False
        httpmod = None
        sw_replace_keys = None
        keys = None
        reqs = {}
        app = {}

        @classmethod
        def init(cls, **kwargs):
            if cls.sw_init:
                return
            cls.sw_init = True
            cls.httpmod = kwargs.get('httpmod')
            sw_replace_keys = kwargs.get('sw_replace_keys', False)
            cls.sw_replace_keys = sw_replace_keys

            try:
                pacmod = kwargs.get('pacmod_curr')
                if sw_replace_keys:
                    cls.keys = Yaml.read(Pacmod.Pmd.sh_path_keys(pacmod))
            except Exception as e:
                Com.Log.error(e, exc_info=True)
                raise

    class Cfg:

        @classmethod
        def init(cls, pacmod):
            """ the package data directory has to contain a __init__.py
                file otherwise the objects notation {package}.data to
                locate the package data directory is invalid
            """
            path_ = Pacmod.Cfg.sh_path(pacmod)
            return Yaml.read(path_)

    class Exit:

        sw_critical = False
        sw_stop = False
        sw_interactive = False

    @classmethod
    def init(cls, **kwargs):
        """ set log and application (module) configuration
        """
        if cls.cfg is not None:
            return

        pacmod_curr = kwargs.get('pacmod_curr')
        cls.pacmod_curr = pacmod_curr

        cls.ts_start = calendar.timegm(time.gmtime())
        cls.pid = os.getpid()

        cls.cfg = cls.Cfg.init(pacmod_curr)
        cls.Main.Log.init(**kwargs)
        cls.App.init(**kwargs)

        cls.d_timer = {}

    @classmethod
    def terminate(cls):
        """ set log and application (module) configuration
        """
        cls.Log = cls.Main.Log.log
        cls.ts_end = calendar.timegm(time.gmtime())
        cls.ts_etime = cls.ts_end - cls.ts_start
