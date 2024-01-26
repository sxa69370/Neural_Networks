# Question: Create a class Employee and then do the following 
# • Create a data member to count the number of Employees 
# • Create a constructor to initialize name, family, salary, department 
# • Create a function to average salary 
# • Create a Fulltime Employee class and it should inherit the properties of Employee class 
# • Create the instances of Fulltime Employee class and Employee class and call their member functions. 


class Employee:
    employee_count = 0
    benefits = None
    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count+=1

    def avg_salary(employees):
        total_salary = sum(emp.salary for emp in employees)
        return total_salary/len(employees)

class Fulltime_Employee(Employee):
    def __init__(self, name, family, salary, department, benefits):
        super().__init__(name, family, salary, department)
        self.benefits = benefits


if __name__=='__main__':
    emp1 = Employee('Dinesh','Mekala',25000,'IT')
    emp2 = Employee('Raju','Karne',40000,'Pharmaceuticals')
    emp3 = Fulltime_Employee('Rakesh','Pusa',60000,'Finance',True)

    employees = [emp1,emp2,emp3]
    print("Employee Details: ")
    for emp in employees:
        print(emp.name,emp.family, emp.salary, emp.department, emp.benefits)
    
    print("\nTotal Employees:", Employee.employee_count)
    print("Average Salary:", Employee.avg_salary(employees))