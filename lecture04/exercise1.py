first_name = input(("Enter your first name : "))
last_name = input(("Enter your last name : "))
student_id = input("Enter your study ID number : ")

system_first_name = first_name[-3::]
system_last_name = last_name[-3::]
system_study_id = student_id[-3::]

print(system_first_name + system_last_name + system_study_id)