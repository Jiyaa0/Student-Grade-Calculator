print("STUDENT GRADE CALCULATOR")
name = input("Enter Student Name: ")
sub1 = float(input("Enter English Marks: "))
sub2 = float(input("Enter Physics Marks: "))
sub3 = float(input("Enter Math Marks: "))
total = sub1+sub2+sub3
per = (total/300)*100
print("Student Name: ",name)
print("Total Marks: ",total,"/300")
print("Percentage: ",per,"%")
if per>=80:
    print("Grade: A")
elif per >= 70:
    print("Grade: B")
elif per >= 60:
    print("Grade: C")
elif per >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
