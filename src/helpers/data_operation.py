import pandas as pd
from sqlalchemy.sql import text


class DataOperations:
    """This class is holding the database connection and operation related to that"""

    def __init__(self):
        """setting up logger for the class"""
        self.conn = None

    def set_database_connection(self, conn):
        """This function sets database connection

        Args:
            conn (mysql_conn): database connection for db operation
        """
        print("Setting database connection")
        self.conn = conn

    def get_data(self, query):
        """This function is for to get the data based on query

        Args:
            query (string): Query to run on database
        """
        print("Runner query and creating dataframe")
        query_result = pd.read_sql(query, self.conn)
        df = pd.DataFrame(query_result)
        return df

    def put_data(self, df, table_name):
        """This function is for to put the data in database

        Args:
            table_name (string): Name of the table where we upload the records
            df (pandas dataframe):
        """
        print(f"Running put data to put the data in {table_name} table")
        df.to_sql(name=table_name, con=self.conn, if_exists="append", index=False, chunksize=50000)

    def replace_data(self, df, table_name):
        def mysql_replace_into(table, conn, keys, data_iter):
            from sqlalchemy.ext.compiler import compiles
            from sqlalchemy.sql.expression import Insert

            @compiles(Insert)
            def replace_string(insert, compiler, **kw):
                s = compiler.visit_insert(insert, **kw)
                s = s.replace("INSERT INTO", "REPLACE INTO")
                return s

            data = [dict(zip(keys, row)) for row in data_iter]

            conn.execute(table.table.insert(), data)

        if len(df.index) != 0:
            df.to_sql(
                name=table_name,
                con=self.conn,
                if_exists="append",
                index=False,
                method=mysql_replace_into,
                chunksize=50000,
            )

    def run_raw_query(self, query):
        """This function runs raw sql queries on the connected database

        Args:
            query (string): Query to execute on database

        Returns:
            bool: return True or False as the per the operation state
        """
        try:
            conn = self.conn.connect()
            conn.execute(text(query))
            return True
        except Exception as e:
            print(str(e))
            raise Exception(e)
