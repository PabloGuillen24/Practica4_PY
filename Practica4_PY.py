import tkinter as tk
import re
from tkinter import messagebox

def clear():
  tbName.delete(0,tk.END)
  tbLastName.delete(0,tk.END)
  tbHeight.delete(0,tk.END)
  tbPhone.delete(0,tk.END)
  tbAge.delete(0,tk.END)
  varGender.set(0)
  	
#Validations
def isValidInt(val):
    try:
      int(val)
      return True
    except ValueError:
      return False

def isValidFloat(val):
    try:
      float(val)
      return True
    except ValueError:
      return False
  
def isValidPhone(val):
     return val.isdigit() and len(val) == 10

def isValidText(val):
   return bool(re.match("^[a-zA-Z\s]+$", val))


def save():
  names = tbName.get()
  lastN = tbLastName.get()
  age   = tbAge.get()
  phone = tbPhone.get()
  height= tbHeight.get()
  gender= ""
  if varGender.get() == 1:
    gender = "Masculino"
  elif varGender.get() == 2:
    gender = "Femenino"
  #validate data
  
  if(isValidInt(age) and isValidFloat(height) and isValidPhone(phone) and isValidText(names) and isValidText(lastN)):
     
      data = "Nombre(s): " + names + "\nApellidos: " + lastN + "\nEdad: " + age + "\nCelular: " + phone + "\nEstatura: " + height + "\nGener0: " + gender
      with open("3O2024Data.txt", "a") as file:
        file.write(data + "\n\n")
      messagebox.showinfo("Info" + "Registro Exitoso\n\n", data)
  else:
     messagebox.showerror("Error", "Error al guardar los datos\n\nFormato Incorrecot")
     
  clear();  


window = tk.Tk()
window.geometry("480x640")
window.title("Form")

varGender = tk.IntVar()

lbName = tk.Label(window, text="Nombre(s): ")
lbName.pack()
tbName = tk.Entry()
tbName.pack()
lbLastName = tk.Label(window, text="Apellidos:")
lbLastName.pack()
tbLastName = tk.Entry()
tbLastName.pack()
lbAge = tk.Label(window, text="Edad:")
lbAge.pack()
tbAge = tk.Entry()
tbAge.pack()
lbPhone = tk.Label(window, text="Celular:")
lbPhone.pack()
tbPhone = tk.Entry()
tbPhone.pack()
lbHeight = tk.Label(window, text="Estatura:")
lbHeight.pack()
tbHeight = tk.Entry()
tbHeight.pack()
lbGender = tk.Label(window, text="Genero:")
lbGender.pack()
rbMale = tk.Radiobutton(window, text = "Masculino", variable=varGender, value=1)
rbMale.pack()
rbFemale = tk.Radiobutton(window, text = "Femenino", variable=varGender, value=2)
rbFemale.pack()

btnClear = tk.Button(window, text = "Limpiar Campos", command=clear)
btnClear.pack()
btnSave  = tk.Button(window, text = "Enviar Formulario", command=save)
btnSave.pack()


window.mainloop()
