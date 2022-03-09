import unittest
from python_sql_assign.python_to_postgres import MyDatabase


class TestClass(unittest.TestCase):
    def setUp(self):
        self.db = MyDatabase()

    def test_check_connection_cursor(self):
        self.assertTrue(self.db)

    def test_select_query(self):
        select_query = "select 'db'"
        res = self.db.query(select_query)
        assert res == [('db',)]

    def test_update_query(self):
        update_query = "update"
        assert self.db.update(update_query) is None

    def test_close_connection(self):
        assert self.db.close() is None

    def tearDown(self):
        self.db.close()