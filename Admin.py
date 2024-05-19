from User import Users
import datetime
class Admin(Users):


    def __init__(self, user_id, user_name, date_of_birth,role, active):
        super().__init__(user_id, user_name, date_of_birth, role, active)

    def __str__(self):
        # Override the __str__ method to return a customized string representation
        return f"Admin ID: {self.user_id}\n" \
               f"Admin Name: {self.user_name}\n" \
               f"Date of Birth: {self.date_of_birth}\n" \
               f"Active: {'Yes' if self.active == 1 else 'No'}"

    #############################################################################3

    def update_admin(self):
        while True:
            print("1. User Name")
            print("2. Date of Birth")
            print("3. Role")
            print("4. Active Status")
            print("5. Finish updating user")

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
                self.active = bool(active)

            elif choice_int == 5:
                break

            else:
                print("Invalid choice, please try again.")
#############################################################################3

