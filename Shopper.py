from User import Users
import datetime
class Shopper(Users):

    def __init__(self, user_id, user_name, date_of_birth,role, active, order=0):
        super().__init__( user_id, user_name, date_of_birth,role, active)

        self.basket = {}
        self.order = order

###############################################################################################

    def __str__(self):
        # Implement the __str__ method to return a string representation
        return f"Shopper ID: {self.user_id}\n" \
               f"Shopper Name: {self.user_name}\n" \
               f"Date of Birth: {self.date_of_birth}\n" \
               f"Active: {'Yes' if self.active == 1 else 'No'}\n" \
               f"Basket: {self.basket}\n" \
               f"Order: {'Yes' if self.order == 1 else 'No'}"

###############################################################################################

    def add_product_to_basket (self,product_id,num_of_items):
        if product_id in self.basket:
            self.basket[product_id] += num_of_items
        else:
            self.basket[product_id] = num_of_items

###############################################################################################

    def clear_basket(self):
        self.basket.clear()

###############################################################################################

    def remove_product_from_the_basket(self,product_id):

        if product_id in self.basket:
            del self.basket[product_id]
            print(f"The item with ID {product_id}has been removed")
        else:
            print(f"Product ID {product_id} not found in the dictionary")

###############################################################################################

    def update_basket(self,product_id, num_of_items):

        self.basket[product_id] =num_of_items


#########################################################################################
    def place_Order(self):#not was used to check if dectinary(basket) is empty or not
        if not bool(self.basket):
            print("The Basket is empty!!")
            self.order=0
        else:
            self.clear_basket()

            self.order = 1
            print(f"Order placed successfully: {self.order}")

###########################################################################################

    def update_shopper(self):
        while True:
            print("1. User Name")
            print("2. Date of Birth")
            print("3. Update Role")
            print("4. Active Status")
            print("5. Update Basket")
            print("6. Update the Order")
            print("7. Finish updating user")

            choice = input("Select the field you want to update: ")
            choice_int = int(choice)

            if choice_int == 1:
                name = input("Enter the new user name: ")
                self.user_name = name

            elif choice_int == 2:
                year = int(input("Enter year: "))
                month = int(input("Enter month: "))
                day = int(input("Enter day: "))
                date_of_birth = datetime.datetime(year, month, day)  # Year, Month, Day
                self.date_of_birth = date_of_birth

            elif choice_int == 3:
                role = input("Enter the new role for the user: ")
                self.role = role

            elif choice_int == 4:
                active = input("Enter the new active status (True/False): ")
                self.active = active

            elif choice_int == 5:
                print("Current Basket:", self.basket)
                item = input("Enter the item id to add to the basket: ")
                quantity = int(input("Enter the quantity: "))
                self.basket[item] = quantity
                print("Basket updated successfully.")

            elif choice_int == 6:
                order = input("Enter the new order status: ")
                self.order = order

            elif choice_int == 7:
                break

            else:
                print("Invalid choice, please try again.")
