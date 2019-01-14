class Product:
	"""Defininf class for the product price,id and quantity"""

    def __init__(self,price,id,quantity):
    	"""Initializing values"""

        self.price = price
        self.id = id
        self.quantity = quantity

class Inventory:
	"""Class defined to access the product information"""

    def __init__(self):
    	"""list for product information is initialized"""

        self.inventoryObjects = []

    def addProduct(self):
    	"""For adding the products into the inventory"""

        print("Enter the Product ID: ")
        p_id = input()
        print("Enter the price: ")
        price = int(input())
        print("Enter the quantity in hand: ")
        quantity = int(input())

        self.inventoryObjects.append(Product(price,p_id,quantity))

    def searchProduct(self):
    	"""Searching the product by its id"""

        print("\nEnter the product ID of the product to be searched: ",end='')
        p_id = input()

        flag = True
        
        for product in self.inventoryObjects:
            if(product.id == p_id):
                print("\nProduct ID: ",end='')
                print(product.id)
                print("Product Price: ",end='')
                print(product.price)
                print("Product Quantity: ",end='')
                print(product.quantity)
                flag = False

        if(flag):
            print("\nProduct with Product ID ",end='')
            print(p_id,end='')
            print(" was not found. Try a different search.\n")

    def totalPrice(self):
    	"""Total price of all products in the inventory is calculated"""

        totalInvPrice = 0

        if(len(self.inventoryObjects) <= 0):
            print("\nNothing's there in your inventory right now. Try adding some products first and then check back!\n")
            return;

        for products in self.inventoryObjects:
            totalInvPrice += (products.price * products.quantity)

        print("\nTotal Inventory Value stands at: ",end='')
        print(totalInvPrice,end='\n\n')

def main():
	"""Calling the inventory class by taking varius options"""

    myInventory = Inventory()

    while(True):

        print("======================================")
        print("Menu: ")
        print("1. Add a product to the Inventory.")
        print("2. Find the value of the Inventory.")
        print("3. Search for a product.")
        print("4. Quit.")
        print("Enter your choice (1,2 or 3): ",end='')

        choice = int(input())
        print("======================================")

        if(choice == 1):
            myInventory.addProduct()
            print("Product Added.")

        elif(choice == 2):
            myInventory.totalPrice()

        elif(choice == 3):
            myInventory.searchProduct()

        else:
            break

if __name__ == "__main__":
    main()
