#every class  will have its own file "except in this lecture and in the assigment"

#attributes = characteristics
#name standard classes begin with uppercase letter
class Student:
    #a method is a function inside a class
    #Constructor - builds an instance of the class
    #constructor will always be defined this way with def __init__( self )
    #builds up the object (assembles the parts or characteristics of the object into an object)
    def __init__( self, first_name, last_name, age, instructor, course ):
        #Attributes/characteristics
        ############
        #first_name
        self.first_name = first_name
        #last_name
        self.last_name = last_name
        #age
        self.age = age
        #instructor
        self.instructor = instructor
        #course
        self.course = course
        
    #methods are the actionns of a class
    #generally uses self as the first parameter. it is a reference to the object created
    #self points to the instance of the student called
    def print_info( self ):
        print( f"Name: {self.first_name} {self.last_name}" )
        print( f"Age: {self.age}" )
        print( f"Instructor: {self.instructor}" )
        print( f"Course: {self.course}" )



#exectues the constructor method for this class 'Student'
#creating an object / making an instance of the student class
student_alex = Student( "Alex", "Miller", 20, "Nichole", "Web Fundamentals" )

# print(student_alex)

# print( student_alex.first_name)

# student_alex.print_info()


class Course:
    def __init__( self, data ):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["Program"]

    def print_insttructor_list( self ):
        for instructor in self.instructors:
            print( instructor )

    def update_instructor( self, new_name, index ):
        if index < len(self.instructors):
            self.instructors[index] = new_name

    def print_info(self):
        print( f"Program: {self.program}" )
        print( f"Name: {self.name}" )
        self.print_insttructor_list()


python = {
    "name" : "Python/Flask",
    "instructors" : ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
    "Program" : "Full stack"

}

course_python = Course( python )

course_python.print_info()
course_python.update_instructor("Ryan Mendez", 2)
course_python.print_info()
