import MySQLdb as mdb
from SQLManager import SQLManager

__author__ = 'pedro'


class MySQLManager(SQLManager):
    def __init__(self, host, login, password, database):
        # Create the basic database configuration
        self.host = host
        self.login = login
        self.password = password
        self.database = database

        # Set the connected to false
        self.connected = False

        # Set the connection to None
        self.connection = None

        # We set the cursor to none
        self.cursor = None

    def connect_to_database(self):
        """
        Connect to database using current configuration
        :return:
        """
        # Try to connect to the database
        try:
            self.connection = mdb.connect(self.host, self.login, self.password, self.database)
        except:
            raise Exception("Unable to Connect to the Database")
        else:
            self.connected = True
            self.cursor = self.connection.cursor()

    def query_insert(self, table, columns, values):
        """
        Insert a new data into the table
        :param table: string table name
        :param columns:
        :param values:
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # First we set the query
        super().query_insert(table, columns, values)

        # Then we try to do the query
        self.query_without_result()

    def query_update(self, table, columns, values, where):
        """
        Update the table query
        :param table: string with table name
        :param columns: string/list with columns values
        :param values: string/list with values
        :param where: list with where statement
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # First we set the query
        super().query_update(table, columns, values, where)

        # Then we try to do the query
        self.query_without_result()

    def query_delete(self, table, where):
        """
        Delete query constructor
        :param table: string table
        :param where: list of where
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # First we set the query
        super().query_delete(table, where)

        # Then we try to do the query
        self.query_without_result()

    def query_select(self, table, columns, where=None, order=None, desc=True):
        """
        Query a selection of data
        :param table: string with table name
        :param columns: string/list with columns to be queried
        :param where: list with conditions for where
        :param order: string with the column name to order
        :param desc: boolean if the data should asc or desc
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # Then we proceed to create the query
        super().query_select(table, columns, where, order, desc)

        # Now we can get the result of the query
        result = self.query_with_result()

        # If we are selecting all columns
        if columns == "*":
            # Then we query the columns for the table
            columns = self.query_columns_names(table)

        # With the result and columns names we can create an array of dictionary with
        # the values we want
        return [{columns[j]: result[i][j] for j in range(len(columns))} for i in range(len(result))]

    def query_columns_names(self, table):
        """
        Query the columns from the table
        :param table:
        :return:
        """
        # First we check to see if there is a connection with the database
        # If there is not we make a connection
        if not self.connected:
            self.connect_to_database()

        # We create the query
        super().query_columns(table)

        # Then we execute the query for the columns
        result = self.query_with_result()

        # Then we get the columns names
        return [r[0] for r in result]

    def query_without_result(self):
        """
        Try to do a query without returning a result
        :return:
        """
        try:
            self.cursor.execute(self.query)
        except:
            raise Exception("Fail to Execute Database Query")
        else:
            self.connection.commit()

    def query_with_result(self):
        """
        Try to do a query with a result
        :return:
        """
        try:
            self.cursor.execute(self.query)
        except:
            raise Exception("Fail to Execute Database Query")
        else:
            return self.cursor.fetchall()