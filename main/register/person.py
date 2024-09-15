import re
import csv

class Person:
  def __init__(self, id, name, password, email):
    self.id = id
    self.name = name
    self.password = password
    self.email = email

  def __str__(self):
    return f"Id {self.id} Name {self.name} Password {self.password} Email {self.email}"
  
  @property
  def password(self):
     return self._password
  
  @password.setter
  def password(self, password):
    if len(password) < 6:
       raise ValueError("almenos 6 caracteres")
    elif re.search(r'[a-zA-Z0-9]', password):
       print("valid")
    else:
       raise ValueError("invalid")  
    self._password = password

  @property
  def email(self):
     return self._email
  
  @email.setter
  def email(self, email):
    if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email):
      print("valid")
    else:
      raise ValueError("invalid")
    self._email = email
