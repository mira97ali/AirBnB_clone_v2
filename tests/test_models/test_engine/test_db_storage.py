#!/usr/bin/python3
""" Module for testing db storage"""
import os
import unittest
from unittest.mock import mock

from models.state import State
from models import DBStorage

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Setup test environment"""
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """Cleanup test environment"""
        self.storage.__session.close()
        self.storage.__engine.dispose()

    @mock.patch.dict(os.environ, {
        'HBNB_MYSQL_USER': 'user',
        'HBNB_MYSQL_PWD': 'password',
        'HBNB_MYSQL_DB': 'test_db',
        'HBNB_MYSQL_HOST': 'localhost',
        'HBNB_ENV': 'test'
    })
    def test_init(self):
        """Test DBStorage initialization"""
        self.assertIsNotNone(self.storage._DBStorage__engine)
        self.assertIsNotNone(self.storage._DBStorage__session)

    def test_all(self):
        """Test retrieving all objects"""
        initial_count = len(self.storage.all())
        new_state = State(name="TestState")
        self.storage.new(new_state)
        self.storage.save()
        self.assertEqual(len(self.storage.all()), initial_count + 1)
        self.storage.delete(new_state)
        self.storage.save()

    def test_new(self):
        """Test adding a new object"""
        new_state = State(name="NewState")
        self.storage.new(new_state)
        self.assertIn(new_state, self.storage._DBStorage__session.new)

    def test_save(self):
        """Test saving changes to the database"""
        new_state = State(name="AnotherState")
        self.storage.new(new_state)
        self.storage.save()
        self.assertIn(new_state, self.storage.all().values())

    def test_delete(self):
        """Test object deletion"""
        new_state = State(name="DeleteState")
        self.storage.new(new_state)
        self.storage.save()
        self.storage.delete(new_state)
        self.storage.save()
        self.assertNotIn(new_state, self.storage.all().values())

    def test_reload(self):
        """Test reloading the session and engine"""
        self.storage.reload()
        self.assertIsNotNone(self.storage._DBStorage__session)


if __name__ == '__main__':
    unittest.main()
