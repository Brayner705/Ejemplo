from tkinter import *
from tkinter import messagebox, ttk
import pymysql


def menu_pantalla(ventana_cerrada= Tk()): 
    ventana_cerrada.destroy()
    global pantalla
    pantalla = Tk()
    pantalla.geometry("400x250")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("icono.ico")

    Label(text="Acceso al sistema", bg="darkmagenta", fg="white", width="300", height="3", font=("sans serif", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3", width="30", command=inicia_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar", height="3", width="30", command= registrar ).pack()

    pantalla.mainloop()

def inicia_sesion():
    pantalla.destroy()

    global pantalla1
    pantalla1 = Tk()
    pantalla1.geometry("400x330")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("icono.ico")


    Label(pantalla1, text="Por favor ingrese su usuario y \n contraseña: ", bg="darkmagenta", fg="white", width="300", height="3", font=("sans serif", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombre_usuario_verify
    global contrasena_verify

    nombre_usuario_verify = StringVar()
    contrasena_verify = StringVar()

    global nombre_usuario_entry
    global contrasena_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombre_usuario_verify)
    nombre_usuario_entry.pack()
    nombre_usuario_entry.focus()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_entry = Entry(pantalla1, show="*", textvariable=contrasena_verify)
    contrasena_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Mostrar contraseña", command=toggle_password_visibility).pack()
    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()
    Button(pantalla1,text='Volver',command=lambda: menu_pantalla(pantalla1)).pack()
   


    pantalla1.mainloop()

def registrar(): 
    pantalla.destroy()
    global pantalla2
    pantalla2 = Tk()
    pantalla2.geometry("400x300")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("icono.ico")

    global nombre_usuario_entry
    global contrasena_entry
    
    nombre_usuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label (pantalla2, text="Por favor ingrese un usuario y contraseña \n para el sistema" , bg="darkmagenta", fg="white", width="300", height="3", font=("sans serif", 15)).pack()
    Label (pantalla2, text="").pack()

    Label (pantalla2, text="Usuario").pack()
    nombre_usuario_entry= Entry(pantalla2)
    nombre_usuario_entry.pack()
    Label (pantalla2).pack()

    Label (pantalla2, text="Contraseña").pack()
    contrasena_entry= Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label (pantalla2).pack()
    Button(pantalla2, text="Mostrar contraseña", command=toggle_password_visibility).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()
    Button(pantalla2, text='Volver', command=lambda: menu_pantalla(pantalla2)).pack()

    pantalla2.mainloop()

def inserta_datos():

    bd = pymysql.connect(
        host = "localhost",
        user="root",
        passwd="",
        db="bd"
    )

    if len(contrasena_entry.get()) <= 8:
        caracter = any(CHAR in ".,*+%$" for CHAR in contrasena_entry.get())

        if caracter:

            fcursor=bd.cursor()

            sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombre_usuario_entry.get(), contrasena_entry.get())

            try:
                fcursor.execute(sql)
                bd.commit()
                messagebox.showinfo(message="Registro Exitoso", title="Aviso")
            except:
                bd.rollback()
                messagebox.showinfo(message="No registrado", title="Aviso")

            bd.close()

        else: 
            messagebox.showinfo(title="Caracteres", message="La contraseña debe contener al menos uno de los siguientes carácteres especiales .,*+%$")

    else: 
        messagebox.showinfo(title="Caracteres", message="La contraseña puede contener hasta 8 caracteres")

def validacion_datos():
    bd = pymysql.connect(
        host = "localhost",
        user="root",
        passwd="",
        db="bd"
    )

    if len(contrasena_entry.get()) <= 8:
        caracter = any(CHAR in ".,*+%$" for CHAR in contrasena_entry.get())

        if caracter:

            fcursor=bd.cursor()

            sql="SELECT * FROM login WHERE usuario='"+nombre_usuario_entry.get()+"' and contrasena='"+contrasena_entry.get()+"'"

            fcursor.execute(sql)

            resultado= fcursor.fetchall()

            if resultado:
                listar_datos()
            else:
                messagebox.showinfo(title="Usuario no registrado", message="Usuario y contraseña incorrecta")

            bd.close()

        else: 
            messagebox.showinfo(title="Caracteres", message="La contraseña debe contener al menos uno de los siguientes carácteres especiales .,*+%$")

    else: 
        messagebox.showinfo(title="Caracteres", message="La contraseña puede contener hasta 8 caracteres")

def listar_datos():
    pantalla1.destroy()
    global pantalla3
    pantalla3 = Tk()
    pantalla3.geometry("400x250")
    pantalla3.title("Facturación")
    pantalla3.iconbitmap("icono.ico")

    bd = pymysql.connect(
        host = "localhost",
        user="root",
        passwd="",
        db="bd"
    )

    boton1 = Button(pantalla3, text="Registrar producto", command= registrar_p)
    boton1.grid(row=0,column=0)
    boton2= Button(pantalla3, text="Facturas realizadas", command= facturas_realizadas)
    boton2.grid(row=0,column=1)

    c1 = Label (pantalla3, text="Por favor ingrese los datos solicitados", fg="black", height="3", font=("sans serif", 15))
    c1.grid(row=2,column=0, columnspan=5)

    c2 = Label (pantalla3, text="RIF")
    c2.grid(row=4,column=0)
    nombre_usuario_entry= Entry(pantalla3)
    nombre_usuario_entry.grid(row=4,column=1)

    c3 = Label (pantalla3, text="Nombre")
    c3.grid(row=5,column=0)
    contrasena_entry= Entry(pantalla3)
    contrasena_entry.grid(row=5,column=1)

    boton3 = Button(pantalla3, text="Generar factura")
    boton3.grid(row=7,column=1)

    pantalla3.mainloop()

def registrar_p():
    global pantalla4
    pantalla4 = Toplevel(pantalla3)
    pantalla4.geometry("400x250")
    pantalla4.title("Registrar Productos")
    pantalla4.iconbitmap("icono.ico")

    Label (pantalla4, text="Por favor ingrese los datos del producto" , fg="black", width="300", height="3", font=("sans serif", 15)).pack()
    Label (pantalla4, text="").pack()

    global nombre_p
    global desc

    Label (pantalla4, text="Nombre del producto").pack()
    nombre_p= Entry(pantalla4)
    nombre_p.pack()
    Label (pantalla4).pack()

    Label (pantalla4, text="Descripción").pack()
    desc= Entry(pantalla4)
    desc.pack()
    Label (pantalla4).pack()

    Button(pantalla4, text="Registrar", command= registro_pdb).pack()

    pantalla4.mainloop()


def registro_pdb():
    bd = pymysql.connect(
        host = "localhost",
        user="root",
        passwd="",
        db="bd"
    )

    if len(nombre_p.get()) != 0 and len(desc.get()) != 0:

            fcursor=bd.cursor()

            sql="INSERT INTO producto (prod, descr) VALUES ('{0}', '{1}')".format(nombre_p.get(), desc.get())

            try:
                fcursor.execute(sql)
                bd.commit()
                messagebox.showinfo(message="Registro Exitoso", title="Aviso")
            except:
                bd.rollback()
                messagebox.showinfo(message="No registrado", title="Aviso")

            bd.close()

    else: 
        messagebox.showinfo(title="Caracteres", message="Los campos son obligatorios")

def toggle_password_visibility():

    if contrasena_entry.cget('show') == '':
        contrasena_entry.config(show='*')

    else:
        contrasena_entry.config(show='')

def facturas_realizadas():
    pantalla_facturas = Toplevel(pantalla3)
    pantalla_facturas.title('Facturas Realizadas')
    pantalla_facturas.iconbitmap('icono.ico')
    pantalla_facturas.geometry('400x400')

    titulo =Label(pantalla_facturas, text='Todas las facturas')
    titulo.pack(padx='100px',pady='10px')


menu_pantalla()