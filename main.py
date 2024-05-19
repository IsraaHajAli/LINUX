# Israa Haj Ali 1201506 //// Lana Hamayel 1200209
import datetime
from Product import Product
from Shopper import Shopper
from Admin import Admin

##########################################################################  PRODUCTS LIST GENERATION  ############################################################################
##########################################################################  PRODUCTS LIST GENERATION  ############################################################################
##########################################################################  PRODUCTS LIST GENERATION  ############################################################################
##########################################################################  PRODUCTS LIST GENERATION  ############################################################################
##########################################################################  PRODUCTS LIST GENERATION  ############################################################################

products = []  # to store the product objects
print("Welcome to Our Online Shopping System")
myfile = input('Please enter the file name which includes the products information: ')


try:
    with open(myfile, 'r') as file:
        line_number = 0
        for line in file:  # This for loop is to read a line py line from the file
            line_number += 1
            # Products [] productInformation; in case the code was in java (to make the code more understadable for us)
            productInformation = line.strip().split(';')  # productInformation is a list which contains the product information
            # strip is to remove leading and trailing whitespace from the string

            if len(productInformation) == 7:  # to check if the provided line is valid or not (is the number of product valid or not)
                product = Product(*productInformation)#creating an instances from the class named Product


                products.append(product)# append the instances to the list called products
                #print()
                print(product.__str__())
                #print()

            elif len(productInformation) == 9:
                product = Product(productInformation[0],productInformation[1],productInformation[2],productInformation[3],productInformation[4],productInformation[5],productInformation[6])
                product.offer_price = productInformation[7]
                product.valid_until = productInformation[8]
                products.append(product)# append the instances to the list called products


            else:
                print(f"There is a loss  in the provided information for product in line '{line_number}' !!")
                continue


            # print(len(productInformation))


    '''for element in products:
        print()
        print()
        print(element.__str__())
        print(f"On Offer: { element.offer_price}")
        print(f"Valid until: { product.valid_until}")
        print()'''

    #################################################################################  USERS LIST GENERATION  #####################################################################
    #################################################################################  USERS LIST GENERATION  #####################################################################
    #################################################################################  USERS LIST GENERATION  #####################################################################
    #################################################################################  USERS LIST GENERATION  #####################################################################
    #################################################################################  USERS LIST GENERATION  #####################################################################

    print()
    print("_______________________________________________________________________________________________________")
    print("_______________________________________________________________________________________________________")
    print()



    users = []  # to store the product objects

    myfile2 = input('Please enter the file name which includes the users information: ')

    try:
        with open(myfile2, 'r') as file2:
            line_number2 = 0
            for line2 in file2:  # This for loop is to read a line py line from the file
                line_number2 += 1
                # Products [] productInformation; in case the code was in java (to make the code more understadable for us)
                userInformation = line2.strip().split(';')  # productInformation is a list which contains the product information
                # strip is to remove leading and trailing whitespace from the string
                print(userInformation.__len__())
                print(userInformation)
                if len(userInformation) == 7:  # to check if the provided line is valid or not (is the number of product valid or not)

                #if userInformation[3].lower() == "shopper":

                    shopper = Shopper(userInformation[0],userInformation[1],userInformation[2],userInformation[3],userInformation[4],userInformation[6])
                    a = userInformation[5]

                    b = a.strip('{}').split(',')

                    for element in b:

                        c = element.split(':')
                        shopper.basket[str(c[0])] = str(c[1])

                    users.append(shopper)

                elif len(userInformation) == 5:
                    print("achieved the admin ")
                    admin = Admin(*userInformation)
                    users.append(admin)

                else:
                    print(f"There is a loss  in the provided information for product in line '{line_number2}' !!")
                    continue


                # print(len(productInformation))

        for user in users:
            print("user type: ",type(user))
        #####################################3 SAVING FUNCTIONS ##############################################################

        def save_products_on_a_file(products):
            try:
                file_name = input("Enter the file name you want to save the products' information on: ")

                with open(file_name, 'w') as file:
                    for productt in products:
                        file.write(productt.__str__() + '\n')  # Add a newline character to separate product information
                        if productt.has_on_offer == "1":
                            file.write("Offer Price: " + productt.offer_price + '\n')
                            file.write("Valid Until: " + productt.valid_until + '\n')
                        file.write('\n\n')

                print(f"Product information saved to '{file_name}'")

            except FileNotFoundError:
                print(f"The file '{file_name}' was not found.")


        #################################################################################################################3

        def save_users_on_a_file(users):
            try:
                file_name = input("Enter the file name you want to save the users' information on: ")

                with open(file_name, 'w') as file:
                    for user in users:

                        file.write(user.__str__() + '\n')  # Add a newline character to separate user information
                        if user.role.lower() == "sopper":
                            file.write(user.basket+'\n')
                            file.write(user.order+'\n')
                        file.write('\n\n')

                print(f"User information saved to '{file_name}'")

            except FileNotFoundError:
                print(f"The file '{file_name}' was not found.")


        ######################################################## MENU ########################################################
        ######################################################## MENU ########################################################
        ######################################################## MENU ########################################################
        ######################################################## MENU ########################################################
        ######################################################## MENU ########################################################
        ######################################################## MENU ########################################################

        while True:
            print("1. Add product.")
            print("2. Place an item on sale.")
            print("3. Update product.")
            print("4. Add a new user.")
            print("5. Update user.")
            print("6. Display all users.")
            print("7. List products.")
            print("8. List shoppers.")
            print("9. Add product to the basket.")
            print("10. Display basket.")
            print("11. Update basket.")
            print("12. Place order.")
            print("13. Execute order.")
            print("14. Save products to a file.")
            print("15. Save users to a text file.")
            print("16. Exit")
            print("ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
            print()
            choice = int(input("Choose from the choices above\n"))
            if choice == 1:

                user_ID = input("Enter Ur ID\n")
                print(user_ID)
                flag = 0
                for user in users:
                    if user.user_id == user_ID:

                        flag = 1
                        #
                        if flag == 1 and user.role == "admin":
                            print("You as an admin are allowed to add product ")

                            ######################## write the code
                            Product_id = int(input("Enter the product ID: "))
                            Product_name = input("Enter the product name: ")
                            Product_category = input("Enter the product category: ")
                            Product_price = int(input("Enter the product price: "))
                            Product_inventory = int(input("Enter the product inventory: "))
                            Product_supplier = input("Enter the product supplier: ")
                            Has_on_offer = int(input("Has the product on offer? "))
                            product = Product(Product_id, Product_name, Product_category, Product_price, Product_inventory,Product_supplier, Has_on_offer)
                            if Has_on_offer == 1:
                                Offer_price = int(input("Enter the offer price: "))
                                print("valid until: ")
                                year = int(input("Enter the year:\n"))
                                month = int(input("Enter the month\n"))
                                day = int(input("Enter the day\n"))
                                Valid_until = datetime.datetime(year, month, day)

                                product.offer_price = Offer_price
                                product.valid_until = Valid_until

                            products.append(product)
                            print("The product has been added successfully !!")


                            break
                        else:
                            print("You as a shopper are not allowed to add product")

                if flag == 0:
                    print("The user is noy found, try again.")
        #################################################################################################################3

            elif choice == 2:

                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if flag == 1 and user.role == "admin":
                            print("You as an admin are allowed to place an item on sale ")
                            item_id = input("Enter the item ID you wanna place on sale:  ")
                            flag1 = 0
                            for item in products:
                                if item_id == item.product_id:
                                    flag1 = 1
                                    item.place_An_Item_On_Sale()
                                    break

                            if flag1 == 0:
                                print("The item you are trying to put on sale is not found.")

                                print("The product has been put on sale successfully !!")

                                ######################## write the code
                                break

                        else:
                            print("You as a shopper are not allowed to place an item on sale")

                if flag == 0:
                    print("The user is not found, try again.")

        #################################################################################################################3

            elif choice == 3:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to update some product ")

                            update_id = input("Enter the product ID you wanna update: ")
                            flag2 = 0
                            for item in products:
                                if update_id == item.product_id:
                                    flag2 = 1
                                    item.update_product(update_id)
                                    print("The product has been updated successfully !!")

                                    break

                            if flag2 == 0:
                                print("The item you are trying to update is not found.")


                            ######################## write the code


                            break
                        else:
                            print("You as a shopper are not allowed to update some product")

                if flag == 0:
                    print("The user is noy found, try again.")


            #################################################################################################################3
            elif choice == 4:
                user_ID = input("Enter Ur ID\n")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to add a new user ")

                            user_id = int(input("Enter the user ID: "))
                            user_name = input("Enter the user name: ")
                            year = int(input("Enter year: "))
                            month = int(input("Enter month: "))
                            day = int(input("Enter day: "))
                            date_of_birth = datetime.datetime(year, month, day)  # Year, Month, Day
                            role = input("Enter the role for the user: ")
                            active = int(input("Enter which the user is active or not: "))

                            if role.lower() == "shopper":

                                #user_id, user_name, date_of_birth,role, active, order=0
                                order = int(input("Enter the order status for this user\n"))
                                shopper = Shopper(user_id,user_name,date_of_birth, role, active, order)
                                print("The shopped has been added successfully !!")

                                while True:
                                    print("Add item to the shopper basket:\n")
                                    item_id = input("Enter the item id:\n")
                                    num_of_items = input("Enter the number of items:\n")
                                    shopper.add_product_to_basket(item_id,num_of_items)
                                    ans = int(input("If you want to add another items press 1, if not press 0."))
                                    if ans == 0:
                                        break
                                    elif ans == 1:
                                        continue
                                    else:
                                        print("Invalid input")

                                users.append(shopper)
                            else:
                                users.append(Admin(user_id, user_name, date_of_birth, role, active))
                                print("The admin has been added successfully !!")

                            ######################## write the code

                            break
                        else:
                            print("You as a shopper are not allowed to add a new user")

                if flag == 0:
                    print("The user is noy found, try again.")


            #################################################################################################################3

            elif choice == 5:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1
                        if user.role == "admin":
                            print("You as an admin are allowed to update some user ")
                            update_id = input("Enter the user ID you wanna update ")
                            flag2 = 0
                            for user in users:
                                if update_id == user.user_id:
                                    flag2 = 1
                                    if user.role.lower() == "shopper":
                                        user.update_shopper()
                                        print("The user has been updated successfully !!")

                                    else:
                                        user.update_admin()
                                        print("The user has been updated successfully !!")
                                    break
                            if flag2 == 0:
                                print("The user you are trying to update is not found.")
                            ######################## write the code
                            break
                        else:
                            print("You as a shopper are not allowed to update some user")
                if flag == 0:
                    print("The user is noy found, try again.")
        #################################################################################################################3

            elif choice == 6:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to display all users. ")
                            for user in users:
                                print()
                                print(user.__str__())
                                print()


                            break
                        else:
                            print("You as a shopper are not allowed to display all users.")

                if flag == 0:
                    print("The user is noy found, try again.")
        #################################################################################################################3

            elif choice == 7:
                while True:
                    print("You are allowed to list the products.")
                    print("1. List all Products.")
                    print("2. List products with offers.")
                    print("3. List product according its category.")
                    print("4. List products according some name.")
                    print("5. Finish viewing products.")
                    choice = int(input("Choose from the above choices:"))
                    if choice == 1:
                        for product in products:
                            print()
                            print(product.__str__())
                            print()
                    elif choice == 2:
                        for product in products:
                            if  product.has_on_offer == "1":
                                print(product.__str__())
                    elif choice == 3:
                        cat = input("Enter some category: ")
                        for product in products:
                            if cat == product.product_category:
                                print(product.__str__())

                    elif choice == 4:

                        name = input("Enter some name: ")
                        for product in products:
                            if name == product.product_name:
                                print(product.__str__())

                    elif choice == 5:
                        break

                    else:
                        print("Invalid choice, try again.")
        #################################################################################################################3
            elif choice == 8:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to list shoppers ")

                            while True:
                                print("1. List all shoppers: ")
                                print("2. List shoppers with items in the basket: ")
                                print("3. List shoppers which have unprocessed orders: ")
                                print("4. Finish viewing the shoppers.")
                                print()

                                choice = int(input("enter your choice number"))

                                if choice == 1:
                                    for user in users:
                                        if user.role.lower() == "shopper":
                                            print(user.__str__())
                                        else:
                                            continue
                                elif choice == 2:
                                    for user in users:
                                        if user.role.lower() == "shopper":
                                            print(user.__str__())

                                        else:
                                            continue
                                elif choice == 3:
                                    for user in users:
                                        if user.role.lower() == "shopper":
                                            print(user.__str__())

                                        else:
                                            continue
                                elif choice == 4:
                                    break
                                else:
                                    print("This choice is invalid d !!")


                            ######################## write the code

                            break
                        else:
                            print("You as a shopper are not allowed to list shoppers")

                if flag == 0:
                    print("The user is noy found, try again.")
        #################################################################################################################3
            elif choice == 9:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "shopper":
                            print("You as a shopper are allowed to add a product to the basket. ")

                            id = int(input("Enter the product id to add to the basket:"))
                            num_of_items = int(input("Enter the number of items from this product:"))
                            user.add_product_to_basket(id, num_of_items)
                            print("The product has been added to the basket successfully !!")


                            ######################## write the code

                            break
                        else:
                            print("You as an admin are not allowed to add a product to the basket.")

                if flag == 0:
                    print("The user is noy found, try again.")
        #################################################################################################################3

            elif choice == 10:
                user_ID = input("Enter Ur ID\n")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role.lower() == "shopper":
                            print("You as a shopper are allowed to display the basket. ")

                            for user in users:
                                #print(user.__str__())
                                if user.role == "shopper":
                                    '''print()
                                    print()
        
                                    print(user.__str__())
                                    print()'''

                                    if user.basket.__len__() > 0 :

                                        for key in user.basket:

                                            for product in products:

                                                if str(key) == str(product.product_id):

                                                    print()
                                                    print()
                                                    print(product.__str__())
                                                    if product.has_on_offer == 1:
                                                        print("Offer price: ",product.offer_price)
                                                        print("Valid until: ",product.valid_until)
                                                    print()
                                                    print()


                                else:
                                    continue

                            ######################## write the code

                            break
                        else:
                            print("You as an admin are not allowed to  display the basket.")

                if flag == 0:
                    print("The user is noy found, try again.")



            #################################################################################################################3

            elif choice == 11:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "shopper":
                            print("You as a shopper are allowed to update the basket. ")

                            ######################## write the code
                            while True:
                                print("1. Remove all products from the basket.")
                                print("2. Remove a specific product from the basket based on product id.")
                                print("3. Change the number of items of a particular product in the basket based on product id.")
                                print("4. Finish updating the basket.")
                                choice = int(input("enter your choice number"))
                                if choice == 1:
                                    id = int(input("Enter the shopper id to remove the products from his basket. "))
                                    for user in users:
                                        if user.user_id == id:
                                            user.clear_basket()
                                            print("The basket has been cleared successfully !!")

                                elif choice == 2:
                                    r_id = input("Enter the user id to remove a product from his basket.")
                                    for user in users:
                                        if user.user_id == r_id:
                                            p_id = input("enter the product id to remove. ")
                                            for key in user.basket:
                                                if key == p_id:
                                                    user.remove_product_from_the_basket(p_id)
                                                    print("The product has been removed from the basket successfully !!")



                                elif choice == 3:
                                    u_id = input("Enter the user id to update his basket. ")
                                    for user in users:
                                        if user.user_id == u_id:
                                            pro_id = input("Enter the product id to be updated.")
                                            for key in user.basket:
                                                if key == pro_id:
                                                    items = int(input("Enter the number of items to be updated"))
                                                    user.update_basket(pro_id, items)
                                                    print("The product has been updated successfully !!")

                                elif choice == 4:
                                    break
                                else:
                                    print("This choice is invalid !!")

                            break
                        else:
                            print("You as an admin are not allowed to update the basket. 0")

                if flag == 0:
                    print("The user is noy found, try again.")





            #################################################################################################################3

            elif choice == 12:
                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "shopper":
                            print("You as a shopper are allowed to place an order. ")

                            id = int(input("Enter the shopper id to place his order."))
                            for user in users:
                                if user.user_id == id:
                                    user.place_Order()
                                    print("The ordder has been placed successfully !!")

                            ######################## write the code

                            break
                        else:
                            print("You as an admin are not allowed to place an order.")

                if flag == 0:
                    print("The user is noy found, try again.")




            #################################################################################################################3

            elif choice == 13:

                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to execute an order. ")

                            id = int(input("Enter the user id to execute his order. "))
                            for user in users:
                                if user.role == 0 and user.user_id == id:

                                    user.place_Order()
                                    for key in user.basket:
                                        for product in products:
                                            if key == product.product_id:
                                                product.inventory -= user.basket[key]
                                                print("The order has been executed successfully !!")

                            ######################## write the code

                            break
                        else:
                            print("You as a shopper are not allowed to execute an order.")

                if flag == 0:
                    print("The user is noy found, try again.")


        #################################################################################################################3



             # basket printing

            elif choice == 14:

                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to save products to a file. ")
                            save_products_on_a_file(products)

                            ######################## write the code

                            break
                        else:
                            print("You as a shopper are not allowed to save products to a file.")

                if flag == 0:
                    print("The user is noy found, try again.")



        #################################################################################################################3
            elif choice == 15:

                user_ID = input("Enter Ur ID")
                flag = 0
                for user in users:
                    if user.user_id == user_ID:
                        flag = 1

                        if user.role == "admin":
                            print("You as an admin are allowed to save users to a file. ")
                            save_users_on_a_file(users)

                            ######################## write the code

                            break
                        else:
                            print("You as a shopper are not allowed to save users to a file.")

                if flag == 0:
                    print("The user is noy found, try again.")

        #################################################################################################################3


            elif choice == 16:
                print("Exit the system.")
                ans = input("Do you want to save your the product ans users information? ")
                answer = ans.lower()
                if answer == "yes":
                    save_products_on_a_file(products)
                    save_users_on_a_file(users)
                    exit(0)

                else:
                    exit(0)

        #################################################################################################################3



        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################

        ########################################### CHECKING THE ACCESSIBILITY ###########################################
    except FileNotFoundError:
        print(f"The file {myfile2} is not found ")

except FileNotFoundError:
    print(f"The file {myfile} is not found ")