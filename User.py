from abc import ABC, abstractmethod
from datetime import date

class Users(ABC):

    # 012903;omar Hussam;10/1/2022;admin;1;{010891:10,110212:3};3
    @abstractmethod

    def __init__(self, user_id, user_name, date_of_birth,role, active):
        self.user_id = user_id
        self.user_name = user_name
        self.date_of_birth = date_of_birth
        self.role = role
        self.active = active



    @abstractmethod

    def __str__(self):
        pass
        #return f"User ID: {self.user_id}\nRole: {self.role}\nUser Name: {self.user_name}\nDate of Birth: {self.date_of_birth}\nActive: {self.active}"

    #@abstractmethod
    #def update_user(self):
        #pass