
emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_con_no = int(input("Enter Employee Contact No: "))
emp_skills = input("Enter Employee Skills: ").split(',')
emp_salary = float(input("Enter Employee Salary: "))
no_of_work_days = int(input("Enter No of Working Days(per month): "))
no_of_weekoff = int(input("Enter No of WeekOffs(per month): "))
work_schedule = (no_of_work_days, no_of_weekoff)
emp_department = input("Enter Employee Working Department: ")
emp_work_loc = input("Enter Employee Work Location: ")



print('\nEmployee Info:\n')
print("Employee ID, Employee Name, Salary: "+ str(emp_id), emp_name, emp_salary, sep=',')
print(f"Employee Name: {emp_name} \nEmployee Contact No: {emp_con_no} \nEmployee Salary: ₹{emp_salary} \n")
print(f'Employee position: Employee Department - {emp_department}, Employee Work_Location - {emp_work_loc}')
