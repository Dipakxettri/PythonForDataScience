class Student:
    def findPercantage(self,tOM):
        self.percentage = (tOM / 600) * 100
        return self.percentage
    
    def findGpa(self,percent):
        self.gpa = (percent / 100) * 4
        return self.gpa
    
    def checksMarks(self):
        self.c = int(input("Enter the marks of C Programming:"))
        self.dsa = int(input("Enter the marks of DSA:"))
        self.physics = int(input("Enter the marks of physics:"))
        self.ai = int(input("Enter the marks of AI:"))
        self.opps = int(input("Enter the marks of OPPS:"))
        self.dl = int(input("Enter the marks of Digital Logic:"))

        totalObtained = self.c + self.dsa + self.physics + self.ai + self.opps + self.dl

        self.percentage = self.findPercantage(totalObtained)
        print(f"The Percentage is : {self.percentage}")

        self.gpa = self.findGpa(self.percentage)
        print(f"The GPA is : {self.gpa}")
    
student = Student()
student.checksMarks()
