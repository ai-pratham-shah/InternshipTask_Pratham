#In one company there are few employees (Prepare dictionary from below details):
#- Robert Downey and Anne Hathaway are Project Managers. Robert has 4 TL: Mark,
#Samuel, Paul, and Tom, all have 8 Years of experience. Anne has 5 TLs, all have 5
#Years of Experience: Chris, Pratt, Emma, Will, and Smith. James is TL and has 3 senior
#developers Jennifer, Scott, and Sophie, they have 3.8 years of experience and his
#manager is Chris, Fergal is a senior developer and has 4.5 years of experience and his
#mentor is Paul. Edge has 3 years of experience and Ryan has 3.5 years of experience.
#Their designation is senior developer and his manager is Will. Jerry and John are junior
#developers and their mentor is Tom, their experience is 1.5 and 1.6 years of experience.
#Leonardo and Alexandra are junior developers and their mentor is Mark who has 1 year
#of experience in each. Walker and Diana are senior developers and they have 2.7 years
#of experience and their reporting manager is Smith.
#a. Display all employees' names for the given project manager name.
#b. Display names of only those employees whose experience is more than 4 years.
#c. Update years of experience with 4.6 whose experience is greater than 3.5 and
#less than 4.5 years.
#d. Display TL with their year of experience, if has no experience then display N/A.
#e. Smith left the company and all his members were assigned to Ryan.
#f. Check company has any employee who has less than 2 years of experience.
#g. Check whether Edge is TL or not if not make him TL.

class Employee:
    def __init__(self, name, designation, experience, manager=None, mentor=None):
        self.name = name
        self.designation = designation
        self.experience = experience
        self.manager = manager
        self.mentor = mentor

def validate_string(prompt):
    """Validates input to ensure it is a non-empty string containing only alphabetic characters."""
    while True:
        value = input(prompt).strip()
        if value.replace(" ", "").isalpha():
            return value
        print("Invalid input. Please enter a valid string containing only alphabets.")

def validate_experience():
    """Validates input to ensure experience is a valid number or 'None'."""
    while True:
        try:
            experience = input("Enter years of experience (or 'None' if not applicable): ").strip()
            if experience.lower() == 'none' or experience == '':
                return None
            exp_value = float(experience)
            if exp_value < 0:
                print("Experience cannot be negative. Try again.")
                continue
            return exp_value
        except ValueError:
            print("Invalid input. Please enter a valid number or 'None'.")

def validate_float(prompt):
    """Validates input to ensure it is a valid positive floating-point number."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("Experience cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_employees_by_manager(manager_name, employees):
    """Displays a list of employees under a given manager."""
    if not employees:
        print("No employees in the system.")
        return
    result = [emp.name for emp in employees if emp.manager == manager_name]
    print(f"Employees under {manager_name}: {', '.join(result) if result else 'None'}")

def display_employees_with_experience(employees, min_experience):
    """Displays a list of employees with more than the given minimum years of experience."""
    if not employees:
        print("No employees in the system.")
        return
    result = [emp.name for emp in employees if emp.experience and emp.experience > min_experience]
    print(f"Employees with more than {min_experience} years of experience: {', '.join(result) if result else 'None'}")

def update_experience(employees):
    """Updates the experience of employees whose experience is between 3.5 and 4.5 years."""
    if not employees:
        print("No employees in the system.")
        return
    
    # Get the new experience value from user input
    new_experience = float(input("Enter the new experience value to update: "))

    for emp in employees:
        if emp.experience and 3.5 < emp.experience < 4.5:
            emp.experience = new_experience
    
    print(f"Experience updated for employees between 3.5 and 4.5 years to {new_experience}.")

def display_tl_with_experience(tls):
    """Displays the list of team leads and their experience."""
    if not tls:
        print("No team leads in the system.")
        return
    for tl in tls:
        print(f"{tl.name}: {tl.experience if tl.experience else 'N/A'} years")

def reassign_manager(old_manager, new_manager, employees):
    """Reassigns the manager of employees from the old manager to the new manager."""
    if not employees:
        print("No employees in the system.")
        return
    for emp in employees:
        if emp.manager == old_manager:
            emp.manager = new_manager
    print(f"Employees under {old_manager} reassigned to {new_manager}.")

def check_low_experience(employees, threshold=2):
    """Checks if any employee has less than the specified threshold years of experience."""
    if not employees:
        print("No employees in the system.")
        return
    result = any(emp.experience and emp.experience < threshold for emp in employees)
    print(f"Company has employee with less than {threshold} years of experience: {'Yes' if result else 'No'}")

def promote_to_tl(name, employees):
    """Promotes an employee to the role of Team Lead."""
    if not employees:
        print("No employees in the system.")
        return
    for emp in employees:
        if emp.name.lower() == name.lower():
            if emp.designation.lower() == "team lead":
                print(f"{name} is already a Team Lead.")
            else:
                emp.designation = "Team Lead"
                print(f"{name} promoted to Team Lead.")
            return
    print(f"Employee {name} not found.")

def menu():
    """Displays the main menu and handles user input for various operations."""
    while True:
        print("\nMenu:")
        print("1. Display employees by manager")
        print("2. Display employees with experience greater than given years")
        print("3. Update experience for employees")
        print("4. Display TLs with their experience")
        print("5. Reassign manager")
        print("6. Check for employees with experience less than 2 years")
        print("7. Promote an employee to TL")
        print("8. Exit")
        choice = input("Enter your choice: ")
       
        if choice == "1":
            manager_name = validate_string("Enter manager name: ")
            display_employees_by_manager(manager_name, employees)
        elif choice == "2":
            min_experience = validate_float("Enter minimum experience: ")
            display_employees_with_experience(employees, min_experience)
        elif choice == "3":
            update_experience(employees)
        elif choice == "4":
            display_tl_with_experience([emp for emp in employees if emp.designation.lower() == "team lead"])
        elif choice == "5":
            old_manager = validate_string("Enter old manager name: ")
            new_manager = validate_string("Enter new manager name: ")
            reassign_manager(old_manager, new_manager, employees)
        elif choice == "6":
            check_low_experience(employees)
        elif choice == "7":
            name = validate_string("Enter employee name to promote to TL: ")
            promote_to_tl(name, employees)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

# User Input for Employee Data
employees = []
n = int(input("Enter the number of employees: "))
for _ in range(n):
    name = validate_string("Enter employee name: ")
    designation = validate_string("Enter designation: ")
    experience = validate_experience()
    manager = input("Enter manager's name (or 'None' if not applicable): ").strip()
    manager = None if manager.lower() == 'none' else manager
    mentor = input("Enter mentor's name (or 'None' if not applicable): ").strip()
    mentor = None if mentor.lower() == 'none' else mentor
    employees.append(Employee(name, designation, experience, manager, mentor))
menu()

# ------------------------------STEPS/PSUEDOCODE------------------------------

# Step 1: Define the Employee Class
# 	Create a class Employee with attributes:
# 						name
# 						designation
# 						experience
# 						manager
# 						mentor
#
# Step 2: Define validation Functions
# 	Function: validate_string(prompt)
# 		Ask the user for input.
# 			Check if the input contains only alphabets (allowing spaces).
# 			If valid, return the input.
# 			Else, prompt again.
# 	Function: validate_experience()
# 		Ask the user to enter years of experience.
# 			If input is 'None' or empty, return None.
# 			Convert input to a float.
# 			If experience is negative, ask again.
# 		Return valid experience.
# 	Function: validate_float(prompt)
# 		Ask the user for a float input.
# 			If negative, ask again.
# 		Return valid float.
#
# Step 3: Define Employee Operations
# 	Function: display_employees_by_manager(manager_name, employees)
# 		Print employees managed by the given manager.

# 	Function: display_employees_with_experience(employees, min_experience)
# 		Print employees having more experience than the given value.

# 	Function: update_experience(employees)
# 		Update experience to 4.6 for employees with experience between 3.5 and 4.5 years.

# 	Function: display_tl_with_experience(tls)
# 		Display team leads (TLs) along with their experience.

# 	Function: reassign_manager(old_manager, new_manager, employees)
# 		Change manager of all employees under old_manager to new_manager.

# 	Function: check_low_experience(employees, threshold=2)
# 		Check if any employee has experience less than 2 years.

# 	Function: promote_to_tl(name, employees)
# 		Promote an employee to Team Lead (TL) if they are not already one.
#
# Step 4: Main User Input for Employees
# 	Ask the user how many employees to enter.
# 	Loop n times:
# 	Get employee details: name, designation, experience, manager, mentor
# 	Create an Employee object.
# 	Store it in a list.
#
# Step 5: Display Menu and Perform Actions

# 	Loop indefinitely:
# 	Display menu options.
# 	Get user choice:
# 		1: Show employees under a manager.
# 		2: Show employees with experience greater than input.
# 		3: Update experience for specific employees.
# 		4: Show team leads and their experience.
# 		5: Reassign manager for employees.
# 		6: Check if any employee has less than 2 years of experience.
# 		7: Promote an employee to Team Lead.
# 		8: Exit.
# 	Perform the selected action.
# 	Repeat until the user chooses Exit.
#
# End of Program
# The program ends when the user selects Exit.



