import tkinter as tk
import re
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:Kaisa235*@localhost/formulariopa', echo=True)
Base = declarative_base()

class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    edad = Column(Integer)
    celular = Column(String(10))
    estatura = Column(Float)
    genero = Column(String(10))

Base.metadata.create_all(engine)

# Crear sesi�n
Session = sessionmaker(bind=engine)
session = Session()

# Funci�n para limpiar campos
def clear():
    tbName.delete(0, tk.END)
    tbLastName.delete(0, tk.END)
    tbHeight.delete(0, tk.END)
    tbPhone.delete(0, tk.END)
    tbAge.delete(0, tk.END)
    varGender.set(0)

# Validaciones
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
    age = tbAge.get()
    phone = tbPhone.get()
    height = tbHeight.get()
    gender = ""
    
    if varGender.get() == 1:
        gender = "Masculino"
    elif varGender.get() == 2:
        gender = "Femenino"
    
    if isValidInt(age) and isValidFloat(height) and isValidPhone(phone) and isValidText(names) and isValidText(lastN):
        try:
            nueva_persona = Persona(
                nombres=names,
                apellidos=lastN,
                edad=int(age),
                celular=phone,
                estatura=float(height),
                genero=gender
            )
            session.add(nueva_persona)
            session.commit()
            messagebox.showinfo("Info", "Registro Exitoso\n\n")
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"Error al guardar en la base de datos: {e}")
    else:
        messagebox.showerror("Error", "Error al guardar los datos\n\nFormato Incorrecto")
    
    clear()

# Crear la ventana
window = tk.Tk()
window.geometry("480x640")
window.title("Formulario")

varGender = tk.IntVar()

# Campos del formulario
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

rbMale = tk.Radiobutton(window, text="Masculino", variable=varGender, value=1)
rbMale.pack()
rbFemale = tk.Radiobutton(window, text="Femenino", variable=varGender, value=2)
rbFemale.pack()

# Botones
btnClear = tk.Button(window, text="Limpiar Campos", command=clear)
btnClear.pack()

btnSave = tk.Button(window, text="Enviar Formulario", command=save)
btnSave.pack()

window.mainloop()