import pymysql.cursors
from os import system
from time import sleep

class Connection:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',  # IP
            user='root',
            password='',
            db='pizzaRestaurant',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )


    def commitBD(self, query, successMessage, failMessage):
        '''Access database and commit changes (INSERT)

        Args:
            query (string): query to run on DB
            successMessage (string): Message to indicate success
            failMessage (string): Message to indicate fail
        '''

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                self.conn.commit()
                #self.message(successMessage)

        except Exception as e:
            print(failMessage, '\n', e)


    def selectBD(self, query, failMessage):
        '''Get database data with fetchall (SELECT)

        Args:
            query (string): query to run on DB
            failMessage (string): Message to indicate fail

        Returns:
            [dictionary]: result - select response
        '''

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            return result
        except Exception as e:
            print(failMessage, '\n', e)

