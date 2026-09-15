from django.test import SimpleTestCase


class DatabaseSettingsTests(SimpleTestCase):
    def test_default_database_uses_sqlite_when_postgres_is_unconfigured(self):
        from django.conf import settings

        database = settings.DATABASES['default']
        self.assertEqual(database['ENGINE'], 'django.db.backends.sqlite3')
