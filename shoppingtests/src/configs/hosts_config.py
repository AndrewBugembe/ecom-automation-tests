
import os
import logging as logger

class MainConfigs:


    API_HOSTS = {
        "test": {
            "base_url": "http://localhost:8888/shopping/"
        },
        "dev": {
            "base_url": "http://localhost:8888/shopping/"
        },
        "prod": {
            "base_url": ""
        }
    }

    # Rest of your code ...

    @staticmethod
    def get_base_url():
        base_url = os.environ.get('BASE_URL')
        if not base_url:
            environment = os.environ.get('ENV', 'test')
            return MainConfigs.API_HOSTS[environment.lower()]['base_url']
        else:
            return base_url

    @staticmethod
    def get_db_configs():
        environment = os.environ.get('ENV', 'test')
        db_configs = MainConfigs.DB_HOSTS[environment.lower()]
        DB_PORT_OVERRIDE = os.environ.get("DB_PORT_OVERRIDE")
        DB_HOST_OVERRIDE = os.environ.get("DB_HOST_OVERRIDE")
        DB_DATABASE_OVERRIDE = os.environ.get("DB_DATABASE_OVERRIDE")
        DB_TABLE_PREFIX_OVERRIDE = os.environ.get("DB_TABLE_PREFIX_OVERRIDE")

        if DB_PORT_OVERRIDE:
            db_configs['port'] = int(DB_PORT_OVERRIDE)
        if DB_HOST_OVERRIDE:
            db_configs['db_host'] = DB_HOST_OVERRIDE
        if DB_DATABASE_OVERRIDE:
            db_configs['database'] = DB_DATABASE_OVERRIDE
        if DB_TABLE_PREFIX_OVERRIDE:
            db_configs['table_prefix'] = DB_TABLE_PREFIX_OVERRIDE
        logger.info("ppppppppppp")
        logger.info(db_configs)
        logger.info("ppppppppppp")
        return db_configs
