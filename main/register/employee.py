from person import Person

class Employee(Person):
  def __init__(self, id, name, password, position, email):
        super().__init__(id, name, password, email)
        self.position = position

  def __str__(self):
      return super().__str__() + f", Position: {self.position}, Email {self.email}"
  

    
