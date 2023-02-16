from connection import Connection
from register import Register
from product import Product
from order import Order
from stats import Stats
from tkinter import *


if __name__ == "__main__":

    def window():
        wind = Tk()
        wind.title('Management System')
        wind.geometry('800x300') # width x height
        wind.resizable(False, False)
        
        wind.mainloop()

    window()
    
    auth = False
    while not auth:
        decisao = int(input("Type 1 to LogIn or 2 to Register: "))
        query = 'SELECT * FROM users;'
        result = Connection.selectBD(Connection, query, 'Error to connect to database')

        auth, userMaster = Register().loginRegister(decisao, result)

        print('Registers:\n', result)
        print('Authenticated: ', auth,
              '\nStatus usuario master: ', userMaster)

    options = 'Type: 0 to Leave\n'\
        '1 to Register a product\n'\
        '2 to List registered Products\n'\
        '3 to List Orders\n'\
        '4 to Create Statistcss\n'\
        '5 to Register new Order (waiter)\n> '

    if auth:
        Message("Authenticated!")
        if userMaster:
            userDecision = 1
            while userDecision != 0:
                userDecision = int(input(options))
                if userDecision == 1:
                    Product().registerProduct()
                elif userDecision == 2:
                    Product().listProduct()
                    delete = int(
                        input("Type 1 to delete a product\n2 to Leave\n"))
                    if delete == 1:
                        Product().deleteProduct()
                elif userDecision == 3:
                    Order().listOrders()
                elif userDecision == 4:
                    Stats().createStatiscs()
                elif userDecision == 5:
                    Order().registerOrders()
