# -*- coding: utf-8 -*-


class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'SHYJU@#'
    HOST = "192.168.20.203"
    PORT = "80"
    DOCKER_HOST = "unix://var/run/docker.sock"


class ConfigurationSqlite(Configuration):
    DATABASE = {
        'name': './example.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }


class ConfigurationMysql(Configuration):
    DATABASE = {
        'name': '',
        'engine': 'peewee.MySQLDatabase',
        'host': '',
        'user': '',
        'passwd': '',
    }
