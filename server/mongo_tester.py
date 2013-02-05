#coding: utf-8
from django.test.simple import DjangoTestSuiteRunner
from django.conf import settings

from mongoengine.python_support import PY3
from mongoengine import connect

try:
    from django.test import TestCase
except Exception as err:
    if PY3:
        from unittest import TestCase
        # Dummy value so no error
        class settings:
            MONGO_DATABASE_NAME = 'dummy'
    else:
        raise err

def skip_django_tests(suite):
    # skipping django tests
    tests = []
    for case in suite:
        pkg = case.__class__.__module__.split('.')[0]
        if pkg != 'django' and pkg != 'south':
            tests.append(case)
    suite._tests = tests
    return suite


class AdvancedTestSuiteRunnerMixin(object):
    """
        DjangoTestSuiteRunner that skips the django tests
    """
    def build_suite(self, *args, **kwargs):
        suite = super(AdvancedTestSuiteRunnerMixin, self).build_suite(*args, **kwargs)
        return skip_django_tests(suite)


class MongoTestRunner(AdvancedTestSuiteRunnerMixin, DjangoTestSuiteRunner):
    """
        A test runner that can be used to create, connect to, disconnect from, 
        and destroy a mongo test database for standard django testing.

        NOTE:
            The MONGO_PORT and MONGO_DATABASE_NAME settings must exist, create them
            if necessary.
        
        REFERENCE:
            http://nubits.org/post/django-mongodb-mongoengine-testing-with-custom-test-runner/
    """

    mongodb_name = 'test_%s' % (settings.MONGO_DATABASE_NAME, )

    def setup_test_environment(self, **kwargs):
        # disabling GEOCODE (saving on google api requests)
        settings.ORIGINAL_GEOCODE = getattr(settings, 'GEOCODE', None)
        settings.GEOCODE = False

        return super(MongoTestRunner, self).setup_test_environment(**kwargs)

    def teardown_test_environment(self, **kwargs):
        # restoring old GEOCODE value
        settings.GEOCODE = settings.ORIGINAL_GEOCODE
        return super(MongoTestRunner, self).teardown_test_environment(**kwargs)

    def setup_databases(self, **kwargs):
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.mongodb_name)
        print 'Creating mongo test database ' + self.mongodb_name
        return super(MongoTestRunner, self).setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        print 'Dropping mongo test database: ' + self.mongodb_name
        disconnect()
        super(MongoTestRunner, self).teardown_databases(old_config, **kwargs)