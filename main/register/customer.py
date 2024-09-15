from person import Person

class Costumer(Person):
  def __init__(self, id, name, password, email):
        super().__init__(id, name, password, email)
        #self.checking_appoinment = checking_appoinment
        #self.edit_appoinment = edit_appoinment
        #self.view_catalog = view_catalog

  def __str__(self):
    return f"Id {self.id} Name {self.name} Password {self.password} Email {self.email}"