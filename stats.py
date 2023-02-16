from connection import Connection
import matplotlib.pyplot as plt


class Stats:
    def __init__(self):
        self.__name, self.__group, self.__price = '', '', 0
        x = Connection().selectBD('SELECT * FROM soldStatistics',
                               "It was not possible to get the data")
        print('x= ', x)
        for i in x:
            print(i)

    ### GETTERSs e SETTERSs ###
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


    ### Methods ###
    def createStatiscs(self):
        '''Allows for building graph related to sold items - quantity and/or value
        '''
        productsKey = []
        productsKey.clear()  # reset everytime the method is called

        # Get product data
        productsQuery = 'SELECT * FROM products'
        listProducts = Connection().selectBD(
            productsQuery, "It was not possible to access system products")
        
        # Get statistics data
        statisticsQuery = 'SELECT * FROM soldStatistics'
        soldList = Connection().selectBD(
            statisticsQuery, "Error consulting sold statistcs")

        state = (input(
            "Type 0 to Leave\n1 to analyse by Name\n2 to analyse by Grupo\n> "))
        if state == "1":
            decision = int(input(
                "Type 1 to analyse by Money\n2 to analyse by Quantity\n> "))
            if decision == 1:
                for i in listProducts:
                    productsKey.append(i['name'])

                values = []
                values.clear()
                for h in range(0, len(productsKey)):
                    valueSum = -1
                    for i in soldList:  # to each name runs the full list
                        if i['name'] == productsKey[h]:
                            valueSum += i['price']  # search by money
                    if valueSum == -1:
                        values.append(0)
                    elif valueSum > 0:
                        values.append(valueSum+1)
                print(values)
                plt.plot(productsKey, values)  # axesX, axesY
                plt.ylabel('Sold Quantity in monetary value')
                plt.xlabel('Products')
                plt.show()

            elif decision == 2:
                singleGroup = []
                singleGroup.clear()

                for i in listProducts:
                    singleGroup.append(i['name'])

                # remove duplicate and order list
                singleGroup = sorted(set(singleGroup))

                finalQuantity = []
                finalQuantity.clear()

                for h in range(0, len(singleGroup)):
                    singleQuantity = 0
                    for i in soldList:
                        if singleGroup[h] == i['name']:
                            singleQuantity += 1
                    finalQuantity.append(singleQuantity)

                plt.plot(singleGroup, finalQuantity)
                plt.ylabel("Sold Quantity")
                plt.xlabel("Products")
                plt.show()

        elif state == "2":
            decision = int(input(
                "Type 1 to analyse by Money\n2 to analyse by Quantity\n> "))
            if decision == 1:
                for i in listProducts:
                    productsKey.append(i['prodGroup'])

                values = []
                values.clear()
                for h in range(0, len(productsKey)):
                    valueSum = -1
                    for i in soldList:  # to each name runs the full list
                        if i['group'] == productsKey[h]:
                            valueSum += i['price']  # search by money
                    if valueSum == -1:
                        values.append(0)
                    elif valueSum > 0:
                        values.append(valueSum+1)
                
                print(values)
                plt.plot(productsKey, values)  # axesX, axesY
                plt.ylabel('Sold Quantity in monetary value')
                plt.xlabel('Products')
                plt.show()
            
            elif decision == 2:
                singleGroup = []
                singleGroup.clear()
                for i in listProducts:
                    singleGroup.append(i['prodGroup'])

                # remove duplicate and order list
                singleGroup = sorted(set(singleGroup))

                finalQuantity = []
                finalQuantity.clear()

                for h in range(0, len(singleGroup)):
                    singleQuantity = 0
                    for i in soldList:
                        if singleGroup[h] == i['prodGroup']:
                            singleQuantity += 1
                    finalQuantity.append(singleQuantity)

                plt.plot(singleGroup, finalQuantity)
                plt.ylabel("Sold Quantity")
                plt.xlabel("Products")
                plt.show()
