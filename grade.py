class student:

    def __init__(self):
        self.marks=[]





    def get_marks(self):
        num=int(input("How many subject do you have ? "))

        print(f"Enter the marks of {num} subject (each out of 100): ")

        for i in range(1,num+1):
            mark=float(input(f"Enter marks of subject {i}: "))
            self.marks.append(mark)


    def total_marks(self):
        return sum(self.marks)
            

    def percentage(self):
        if len(self.marks)==0:
            return 0
        return (sum(self.marks)/(len(self.marks)*100))*100




student=student()

student.get_marks()

print("marks : ",student.total_marks())
print("Percentage ; ",student.percentage())


