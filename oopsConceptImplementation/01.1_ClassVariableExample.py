class Employee:

    number_of_employee = 0
    raise_amout = 1.05

    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        Employee.number_of_employee += 1

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)


print("Number of Employee :: ", Employee.number_of_employee)

emp_1 = Employee("John", "berry")
emp_2 = Employee("Pandhari", "Patil")
print('Created two employee Objects')
print("Number of Employee :: ", Employee.number_of_employee)

print("Here we can see that raise amount is part of employee instance", Employee.__dict__)
print(Employee.raise_amout)
print("Here we can see that raise amount is not part of employee instance", emp_2.__dict__)
print(emp_2.raise_amout)
emp_2.raise_amout = 2
print("Here we can see that raise amount is part of employee instance", emp_2.__dict__)
print(emp_2.raise_amout)
emp_1.raise_amout = 1.05
print("Here we can see that raise amount is part of employee instance though the value of class variable is same", emp_1.__dict__)
print(emp_1.raise_amout)
