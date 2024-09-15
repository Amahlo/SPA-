from person import Person

class Administrator(Person):
  def __init__(self, id, name, password, email):
        super().__init__(id, name, password, email,)
        #self.managment_appointment = managment_appointment
        #self.managment_employee = managment_employee 

  def __str__(self):
    return f"Id {self.id} Name {self.name} Password {self.password} Email {self.email}"
  
 