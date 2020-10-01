

#Parent user class
class User:
    name = "Ryan"
    email = "pt@gmail.com"
    password = "1234pass"
    Address = ""

    def loginInfo(self):
        login_name = input("Enter name: ")
        login_email = input("Enter email: ")
        login_password = input("Enter password: ")
        if (login_email == self.email and login_password == self.password):
            print("Welcome back, {}!".format(login_name))
        else: 
            print("Password or email is incorrect")

#Child Class Employee
class Employee(User):
    base_pay: 12.00
    hours = 40
    department = "Physical Therapy"
    pin_number = 7890

    def loginInfo(self):
        login_name = input("Enter name: ")
        login_email = input("Enter email: ")
        login_pin = input("Enter pin: ")
        if (login_name == self.name and login_pin == self.pin_number):
            print("Access Granted")
        else:
            print("Access Denied")

#Child Class Patient
class Patient(User):
    co_pay = 15.00
    visits_left = ""
    access_code = 345

    def loginInfo(self):
        login_name = input("Enter name: ")
        login_email = input("Enter email: ")
        login_code = input("Enter access code: ")
        if (login_name == self.name and login_code == self.access_code):
            print("Access Granted")
        else:
            print("Access Denied")


employee = User()
employee.loginInfo()

patient = Patient()
patient.loginInfo()