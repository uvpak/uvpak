from uvicore.configuration import env
from uvicore.typing import OrderedDict


# --------------------------------------------------------------------------
# Database Connections
#
# Uvicore allows for multiple database connections (backends) each with
# their own connection name.  Use 'default' to set the default connection.
# Database doesn't just mean a local relational DB connection.  Uvicore
# ORM can also query remote APIs, CSVs, JSON files and smash them all
# together as if from a local database join!
# --------------------------------------------------------------------------
database = {
    'default': env('DATABASE_DEFAULT', 'uvpak'),
    'connections': {
        # SQLite Example
        'uvpak': {
            'backend': env('DB_UVPAK_BACKEND', 'sqlalchemy'),
            'dialect': env('DB_UVPAK_DIALECT', 'sqlite'),
            'driver': env('DB_UVPAK_DRIVER', 'aiosqlite'),
            'database': env('DB_UVPAK_DB', ':memory:'),
            'prefix': env('DB_UVPAK_PREFIX', None),
            # If 'url' is defined using sqlalchemy backend,
            # it will be used instead of deriving one from the properties above.
            # 'url': '',
        },

        # MySQL Example
        # 'uvpak': {
        #     'backend': 'sqlalchemy',
        #     'dialect': env('DB_UVPAK_DIALECT', 'mysql'),
        #     'driver': env('DB_UVPAK_DRIVER', 'aiomysql'),
        #     'host': env('DB_UVPAK_HOST', '127.0.0.1'),
        #     'port': env.int('DB_UVPAK_PORT', 3306),
        #     'database': env('DB_UVPAK_DB', 'uvpak'),
        #     'username': env('DB_UVPAK_USER', 'root'),
        #     'password': env('DB_UVPAK_PASSWORD', 'techie'),
        #     'prefix': env('DB_UVPAK_PREFIX', None),
        #     # If 'url' is defined using sqlalchemy backend,
        #     # it will be used instead of deriving one from the properties above.
        #     'url': '',
        #     # All options passed directly as **kwargs to the backends connect, create_pool,
        #     # create_engine or other backend specific create methods
        #     # Example enable SSL using pymysql driver
        #     # 'options': {
        #     #     'ssl_ca': '/etc/ssl/certs/ca-certificates.crt',
        #     # },
        #     # Example enable SSL using aiomysql driver
        #     # 'options': {
        #     #     'ssl': True
        #     # }
        # },
    },
}


# --------------------------------------------------------------------------
# Redis Connections
#
# Uvicore allows for multiple redis connections (backends) each with
# their own connection name.  Use 'default' to set the default connection.
# --------------------------------------------------------------------------
redis = {
    'default': env('REDIS_DEFAULT', 'uvpak'),
    'connections': {
        'uvpak': {
            'host': env('REDIS_UVPAK_HOST', '127.0.0.1'),
            'port': env.int('REDIS_UVPAK_PORT', 6379),
            'database': env.int('REDIS_UVPAK_DB', 0),
            'password': env('REDIS_UVPAK_PASSWORD', None),
        },
        'cache': {
            'host': env('REDIS_CACHE_HOST', '127.0.0.1'),
            'port': env.int('REDIS_CACHE_PORT', 6379),
            'database': env.int('REDIS_CACHE_DB', 2),
            'password': env('REDIS_CACHE_PASSWORD', None),
        },
    },
}
