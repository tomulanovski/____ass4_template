from persistence import *

def main():
    print(repo.activitys._table_name.capitalize())
    activities = repo.activitys.find_all()
    activities.sort(key=lambda i: i.date)
    for activity in activities:
        print(activity.__str__())
    print()
    print(repo.branches._table_name.capitalize())
    branches = repo.branches.find_all()
    branches.sort(key=lambda i: i.id)
    for branch in branches:
        print((branch.id, str(branch.location), branch.number_of_employees))
    print()
    print(repo.employees._table_name.capitalize())
    employees = repo.employees.find_all()
    employees.sort(key=lambda i: i.id)
    for employee in employees:
        print((employee.id, str(employee.name), employee.salary, employee.branche))
    print()
    print(repo.products._table_name.capitalize())
    products = repo.products.find_all()
    products.sort(key=lambda i: i.id)
    for product in products:
        print((product.id, str(product.description), product.price, product.quantity))
    print()
    print(repo.suppliers._table_name.capitalize())
    suppliers = repo.suppliers.find_all()
    suppliers.sort(key=lambda i: i.id)
    for supplier in suppliers:
        print((supplier.id, str(supplier.name),str(supplier.contact_information))) 
    print()
    print("Employees report")
    report = repo.execute_command('''SELECT employees.name , employees.salary , branches.location ,
    IFNULL(SUM((activitys.quantity * (-1)) * products.price), 0)
    FROM employees 
    LEFT JOIN activitys ON activitys.activator_id=employees.id 
    LEFT JOIN products ON products.id=activitys.product_id 
    LEFT JOIN branches ON branches.id=employees.branche
    GROUP BY Name
    ORDER BY Name''')
    for item in report:
        print(*item)          
    print()
    report = repo.execute_command( '''SELECT activitys.date , products.description , 
    activitys.quantity, employees.name, suppliers.name
    FROM activitys 
    LEFT JOIN products ON activitys.product_id = products.id
    LEFT JOIN employees ON activitys.activator_id = employees.id
    LEFT JOIN suppliers ON activitys.activator_id = suppliers.id
    ORDER BY date''')
    print("Activities report")
    for item in report:
        print(item)

if __name__ == '__main__':
    main()
