
name=input("What is your name?\n")
print(f"Hello {name}")
student_id = input("What is your Student ID?\n")
print("Your ID is {student_id}\n")


var1= float(input("Enter var1\n"))
var2= float(input("Enter var2\n"))
var_sum= var1 + var2
var_diff= var1 - var2
var_prod= var1 * var2
print(
    f"var1 = {var1}\n"
    f"var2 = {var2}\n"
    f"var_sum = {var_sum}\n"
    f"var_diff = {var_diff}\n"
    f"var_prod = {var_prod}\n"
)


name=input("What is your name?\n")
lab_grade=float(input("What is your lab grade?\n"))
midterm_grade=float(input("What is your midterm grade?\n"))
final_grade=float(input("What is your final grade?\n"))
print(
    f"Name: {name}\n"
    f"Lab Grade: {lab_grade}\n"
    f"Midterm Grade: {midterm_grade}\n"
    f"Final Grade: {final_grade}\n"
    f"Last Score: {lab_grade*0.25 + midterm_grade*0.35 + final_grade*0.40}\n"
)


print ("*\n**\n***\n**\n*\n")