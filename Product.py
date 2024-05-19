import datetime
class Product:
    def __init__(self, product_id, product_name, product_category, price, inventory, supplier, has_on_offer):

            self.product_id = product_id
            self.product_name = product_name
            self.product_category = product_category
            self.price = price
            self.inventory = inventory
            self.supplier = supplier
            self.has_on_offer = has_on_offer

###############################################################################################

    def __str__(self):
        return f"Product ID: {self.product_id}\n" \
               f"Product Name: {self.product_name}\n" \
               f"Product Category: {self.product_category}\n" \
               f"Price: {self.price}\n" \
               f"Inventory: {self.inventory} items\n" \
               f"Supplier: {self.supplier}\n"\
               f"Has an Offer?: {self.has_on_offer}"

    ###############################################################################################

    def place_An_Item_On_Sale(self):

        self.has_on_offer = 1
        offer_Price = input("Enter the offer price")
        self.offer_price = offer_Price

        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        Valid_until = datetime.datetime(year, month, day)  # Year, Month, Day
        self.valid_until = Valid_until

###############################################################################################

    def execute_order(self, num_of_items):

        self.inventory -= num_of_items

        # clear the pasket

###############################################################################################

    def update_product(self, product_ID):
        #  product_name, product_category, price, inventory, supplier, has_on_offer

        ''' This method is to update any product information, it's valid for all product fields other than the id, this
         done by displaying a menu to the user to choose the field she/he wanna modify
         '''


        while True:


            print("1. Product Name")
            print("2. Product Category")
            print("3. Product Price")
            print("4. Product Inventory")
            print("5. Product Supplier")
            print("6. Add an Offer")
            print("7. Finish updating product")

            choice = input("Select the field you wanna update: ")
            choice_int = int(choice)

            if choice_int == 1:
                name = input("Enter the new name for the product")
                self.product_name = name

            elif choice_int == 2:
                category = input("Enter the new category for the product")
                self.product_category = category

            elif choice_int == 3:
                price = input("Enter the new price for the product")
                price_int = int(price)
                self.price = price_int

            elif choice_int == 4:
                inventory = input("Enter the new inventory for the product")
                inventory_int =\
                    int(inventory)
                self.inventory = inventory_int

            elif choice_int == 5:
                supplier = input("Enter the new category for the product")
                self.supplier = supplier

            elif choice_int == 6:
                self.place_An_Item_On_Sale()

            elif choice_int == 7:
                break

            else:
                print("Invalid choice, try again.")

###############################################################################################
