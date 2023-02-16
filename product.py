from connection import Connection


class Product:
    def __init__(self):
        self.__name, self.__group, self.__ingredients, self.__price = '', '', '', 0

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
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


    ### Methods ###
    def registerProduct(self):
        '''Adm user can register products on the sistema
        '''

        self.__name = input("Type the product name: ")
        self.__ingredients = input("Type the product's ingredients: ")
        self.__group = input("Type product group: ")
        self.__price = float(input("Type the product price: "))

        query = 'INSERT INTO products(name, ingredients, prodGroup, price) VALUES ("{}", "{}", "{}", {});'.format(
            self.__name, self.__ingredients, self.__group, self.__price)
        Connection().commitBD(query, "Product successfully saved!",
                           "Fail to insert product on database")


    def listProduct(self):
        '''Allow the user to see products already registered
        '''

        products = []
        query = 'SELECT * FROM products'
        registeredProducts = Connection().selectBD(
            query, 'Error connecting to database')

        for i in registeredProducts:
            products.append(i)
        if len(products) != 0:
            for i in range(0, len(products)):
                print("Product {}\n".format(round(i, 2)), products[i], "\n")
        else:
            print("No product registered!")


    def deleteProduct(self):
        '''Allow user to delete one of the products already registered
        '''

        deleteId = int(input("Type in the product id to be deleted: "))
        query = 'DELETE FROM products WHERE id = {}'.format(deleteId)
        Connection().commitBD(query, "Product successfully deleted!",
                           "Error deleting product")
