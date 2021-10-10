class Employee:
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def email(self):
            return '{}.{}@email.com'.format(self.lastName, self.firstName)

    @property
    def fullName(self):
        return '{} {}'.format(self.lastName, self.firstName)

    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName


emp_1 = Employee("John", "berry")

emp_1.fullName = "Patil Pudhari"   # AttributeError: can't set attribute

print('First Name of Employee :: ' + emp_1.firstName)
print('Last Name of Employee :: ' + emp_1.lastName)
print('Full Name of Employee :: ' + emp_1.fullName)
print('Email Id of Employee :: ' +emp_1.email())
print('------------------------------------------------ \nModify LastName as :: '
      + emp_1.lastName + 'Result after Modification')
print('First Name of Employee :: ' + emp_1.firstName)
print('Last Name of Employee :: ' + emp_1.lastName)
print('Full Name of Employee :: ' + emp_1.fullName)
print('Email Id of Employee :: ' +emp_1.email())

