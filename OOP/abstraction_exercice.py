'''
Exercice: try to abstract an Academic Management System with:
Students, teachers, course and assignatures
'''
class Student:
    def __init__(self, name, id_student, course,assignatures): # Defining atributes
        self.name = name
        self.id_student = id_student
        self.course = course
        self.assignatures = assignatures

    # Creating methods
    def enroll(self):
        pass
    def see_enrolled_assignatures(self):
        pass

class Teacher:
    def __init__(self, name, id_teacher, admin, assignatures):
        self.name = name
        self.id_teacher = id_teacher
        self.admin = admin
        self.assignatures = assignatures
    
    def register_student(self):
        if self.admin == True: # You can register students
            pass
        else: # You can't register students
            pass

    def register_assignature(self):
        if self.admin == True: # You can register assignatures
            pass
        else: # You can't register assignatures
            pass
        
class Course:
    def __init__(self, name, assignatures):
        self.name = name
        self.assignatures = assignatures

class Assignature:
    def __init__(self, name, course, workload):
        self.name = name
        self.course = course
        self.workload = workload
