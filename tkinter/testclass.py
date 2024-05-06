"""
Create a class that encalpsulates a person

"""

class Student:

    """
    The __init__ function is a 'built in' function that must be defined at the top of every new class.
    It initializes the instance of the class.

    """ 
    def __init__(self, student_name, reg_no, no_of_subjects, sex, scorestotal):
        self.name = student_name
        self.reg_no = reg_no
        self.no_of_subjects = no_of_subjects
        self.sex = sex
        self.scorestotal = scorestotal # out of 1000

    def compute_grade(self):
        self.grade = (self.scorestotal / 10)
        return self.grade
    
    def get_no_of_subjects(self):
        return self.no_of_subjects
    
    def get_reg_no(self):
        return self.reg_no
    





# make use of the class to create instances
student1 = Student("Daniel", 1111, 10, "M", 645.0) # instance 1 of student class

student2 = Student("Abdullah", 1110, 10, "M", 750.0) # instance 2 of student class

daniels_grade = student1.compute_grade()
abdullahs_grade = student2.compute_grade()

print("Daniel's grade is ", daniels_grade, "/100")
print("Abdullah's grade is ", abdullahs_grade, "/100")



