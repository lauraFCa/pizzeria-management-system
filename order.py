from connection import Connection


class Order:
    def __init__(self):
        self.__name, self.__group, self.__ingredients, self.__deliveryAddress, self.__notes = '', '', '', '', ''

    ### GETs e SETs ###
    @property  # GET
    def name(self):
        return self.__name

    @name.setter  # SET
    def name(self, name):
        self.__name = name

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self.__ingredients = ingredients

    @property
    def deliveryAddress(self):
        return self.__deliveryAddress

    @deliveryAddress.setter
    def deliveryAddress(self, deliveryAddress):
        self.__deliveryAddress = deliveryAddress

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    ### Methods ###
    def deleteOrder(self):
        '''
        Allow user to define order as delivered\n Move order to sold statistics
        '''

        group, index = None, 0
        deleteId = int(input("Type order ID to be delivered: "))

        query = 'SELECT name FROM orders WHERE id = {};'.format(deleteId)
        name = Connection().selectBD(query, "It was not possible to get order's name!")
        name = name[0]['name']

        queryProdutos = 'SELECT * FROM products;'
        products = Connection().selectBD(
            queryProdutos, "It was not possible to get products")

        for p in products:
            index += 1
            if name == p['name']:
                group = p['prodGroup']
                price = p['price']
                break

        if group != None:
            queryEstatisticas = 'INSERT INTO soldStatistics(name, statsGroup, price) VALUES ("{}", "{}", {});'.format(
                name, group, price)
            Connection().commitBD(queryEstatisticas, "The order is acconted for!",
                               "It was not possible to account for the order")

            queryDelete = 'DELETE FROM orders WHERE id = {};'.format(
                deleteId)
            Connection().commitBD(queryDelete, "Order successfully delivered!",
                               "Error accessing database")
        else:
            print("It was not posssible to deliver the order.\nProduct not found!")


    def listOrders(self):
        '''
        Allow user to access list of made orders \nAlso allow to delete delivered orders
        '''
        orders = []
        decideOrder = 0

        while decideOrder != 2:
            orders.clear()  # sempre limpa variavel para na acumular (quando order eh entregue ele eh apagado)
            query = 'SELECT * FROM orders'
            listaOrders = Connection().selectBD(query, "Fail to connect to database")

            for i in listaOrders:
                orders.append(i)

            if len(orders) != 0:
                for i in range(0, len(orders)):
                    print(orders[i])

            else:
                print("No orders to be done")

            decideOrder = int(
                input("Type 1 to mark as delivered\nType 2 to go back\n"))
            if decideOrder == 1:
                self.deleteOrder()


    # Function for waiter phones
    def registerOrders(self):
        '''Waiters register orders
        '''
        group = None
        index = 0
        name = input("Type order name: ")

        query = 'SELECT * FROM products'
        products = Connection().selectBD(
            query, "It was not possible to get registeres products!")

        for p in products:
            index += 1
            if name == p['name']:
                ingredients = p['ingredients']
                group = p['prodGroup']
                break
            elif index == len(products):
                print(
                    "No registered products found!\nRegister a product before making an order")

        if group != None:
            deliveryAddress = input(
                "Type in the table or delivery address: ")
            notes = input("Type in order notes: ")

        query1 = 'INSERT INTO orders(name, ingredients, orderGroup, deliveryAddress, notes) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(
            name, ingredients, group, deliveryAddress, notes)
        Connection().commitBD(query1, "Order successfully made!", "It was not possible to make the order!")

