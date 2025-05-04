class Student:
    def __init__(self,name):
        self.name=name
        self.grade=[]
    def addGrades(self,grade):
        self.grade.append(grade)
        print(f"Added Grade {grade} for {self.name}")
    def averageGrade(self):
        if not self.grade:
            print(f"{self.name} has no grades")
            return
        total= sum(self.grade)
        average = total/len(self.grade)
        return average
    def displayGrades(self):
        print(f"Grades for {self.name}")
        if not self.grade:
            print("No grade received")
        else: 
            for grade in self.grade:
                print(f"{grade}")
        
student1 = Student("Alice")
student1.addGrades(85)
student1.addGrades(55)
student1.addGrades(80)

student1.displayGrades()

avg=student1.averageGrade()
print(f"THe average grade of {student1.name} is {avg:.2f}")