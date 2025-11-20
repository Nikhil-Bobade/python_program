


def get_marks():
    print("Enter the subject of all subject out of 100 ")
    s1=float(input("English :  "))
    s2=float(input("Science : "))
    s3=float(input("History: "))
    s4=float(input("Mathmatics: "))
    s5=float(input("Information tecnology : "))

    return s1,s2,s3,s4,s5



def calculatemark(marks):
    
    return sum(marks)





def calculatepercentage(Total_marks):
    
    percentage=(Total_marks/500)*100
    return percentage





def calculategrade(percentage):


    if percentage>=90:
        Grade ="A" 
    elif percentage>=80 :
         Grade="B" 
    elif percentage >=70 :
         Grade= "C" 
    elif percentage >=60 :
         Grade= "D" 
    else:
         Grade="E"  
    return Grade        







def main():
    
    marks=get_marks()
    Total_mark=calculatemark(marks)
    percentage=calculatepercentage(Total_mark)
    grade=calculategrade(percentage)

    print("Total marks: ",Total_mark)
    print("percentage : ",percentage)
    print("Grade : ",grade)
    

 

main()


