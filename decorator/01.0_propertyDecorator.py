class Employee:
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    # Here the emil is the function
    def email(self):
        return '{}.{}@email.com'.format(self.lastName, self.firstName)

    # here the fullName is property Object
    @property
    def fullName(self):
        return '{} {}'.format(self.lastName, self.firstName)

emp_1 = Employee("John", "berry")

emp_1.lastName = "Robert"

print('First Name of Employee :: ' + emp_1.firstName)
print('Last Name of Employee :: ' + emp_1.lastName)
print('Full Name of Employee :: ' + emp_1.fullName)
print('Email Id of Employee :: ' +emp_1.email())
print('------------------------------------------------ \nModify LastName as :: '
      + emp_1.lastName + 'Result after Modification')
print('First Name of Employee :: ' + emp_1.firstName)
print('Last Name of Employee :: ' + emp_1.lastName)
print('Full Name of Employee :: ' + emp_1.fullName)
''' 
Note fullName is implemented with property decorator hence () is not required 

'''
print('Email Id of Employee :: ' +emp_1.email())

