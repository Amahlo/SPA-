import csv 
from administrator import Administrator
from employee import Employee
from customer import Costumer


def get_administrator():
  name = input("Name: ")
  id = int(input("ID: "))
  email = input("e-mail: ").strip()
  password = input("Password: ").strip()
  administrator = Administrator(id, name, password, email)
  return administrator

def save_administrator(administrator):
   with open("db_administrator.csv", "a") as file:
      writer = csv.DictWriter(file, fieldnames=["name", "id", "password"])
      if file.tell() == 0:
         writer.writeheader()
      writer.writerow({"name": administrator.name, "id": administrator.id, "password": administrator.password})


def get_employee():
    name = input("Nombre: ")
    id = int(input("ID: "))
    email = input("e-mail: ").strip()
    password = input("Contraseña: ").strip()
    position = input("Posición: ")
    employee = Employee(id, name, password, position, email)
    return employee

def save_employee(employee):
    with open("db_employee.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "password", "position"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({"id": employee.id, "name": employee.name, "password": employee.password, "position": employee.position})

def get_customer():
    name = input("Nombre: ")
    id = int(input("ID: "))
    email = input("e-mail: ").strip()
    password = input("Password: ").strip()
    customer = Costumer(id, name, password, email)
    return customer

def save_cutomer(customer):
    with open("db_customer.csv", "a", newline= '') as file:
      writer = csv.DictWriter(file, fieldnames=["id", "name", "password", "email" ])
      if file.tell() == 0:
         writer.writeheader()
      writer.writerow({'id': customer.id, 'name': customer.name, 'password': customer.password, 'email': customer.email})


def main():
    administrator = get_administrator()
    save_administrator(administrator)
    employee = get_employee()
    save_employee(employee)
    customer = get_customer()
    save_cutomer(customer)

if __name__ == "__main__":
    main()