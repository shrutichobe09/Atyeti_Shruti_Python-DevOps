class employee:
    count=0    #class variable

    def __init__(self, emp_id):
        self.emp_id=emp_id
        employee.count+=1

employee1=employee("1")
employee2=employee("2")
employee3=employee("3")

print(employee.count)