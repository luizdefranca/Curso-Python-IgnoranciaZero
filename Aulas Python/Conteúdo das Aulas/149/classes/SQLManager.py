__author__ = 'pedro'


class SQLManager (object):
    def __init__(self):
        """
        :return:
        """
        self.query = ""

    def order_with_separator(self, array, bet="`", sep=","):
        """
        Order array as a string with the selected separator
        :param array:
        :return: string
        """

    def query_where(self, where):
        """
        Create a query for the where statement
        :param where: list with the where statement
        :return:
        """

    def query_insert(self, table, columns, values):
        """
        Insert a new data into the table
        :param table: string table name
        :param columns:
        :param values:
        :return:
        """

    def query_update(self, table, columns, values, where):
        """
        Update the table query
        :param table: string with table name
        :param columns: string/list with columns values
        :param values: string/list with values
        :param where: list with where statement
        :return:
        """

    def query_delete(self, table, where):
        """
        Delete query constructor
        :param table: string table
        :param where: list of where
        :return:
        """

    def query_select(self, table, columns, where=None, order=None, desc=True):
        """
        Create the select query
        :param table: string with table name
        :param columns: string/list with columns to be queried
        :param where: list with conditions for where
        :param order: string with the column name to order
        :param desc: boolean if the data should asc or desc
        :return:
        """


    def query_columns(self, table):
        """
        Get the query for the columns of the table
        :param table:
        :return:
        """

    def custom_query(self, query):
        """
        Set a custom query
        :param query: string custom query
        :return:
        """
