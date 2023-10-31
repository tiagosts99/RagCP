from django.core.management.base import BaseCommand
from django.db import connections
from django.conf import settings

from ragcp.settings import logger

tables = ['login', 'char']

class Command(BaseCommand):

    def handle(self, database="default", *args, **options):
        if database in settings.DATABASES:
            database_settings = settings.DATABASES[database]
            host = database_settings.get('HOST', None)
            
            if host is not None:
                cursor = connections[database].cursor()

                cursor.execute("SHOW TABLE STATUS")

                for row in cursor.fetchall():
                    if row[1] != "InnoDB" and row[0] in tables:
                        table_name = row[0]
                        cursor.execute("ALTER TABLE `%s` ENGINE=InnoDB" % table_name)
                        logger.info("Converted %s to InnoDB" % table_name)
            else:
                logger.warning("Database host is not defined in settings for database '%s'" % database)
        else:
            logger.warning("Database configuration for database '%s' not found in settings" % database)
