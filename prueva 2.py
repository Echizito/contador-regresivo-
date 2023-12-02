# @echizito
from tkinter import Label, Entry, StringVar, Tk, Button
from datetime import datetime, timedelta
from tkinter import END

ventana = Tk()
ventana.title('Contador Regresivo')
ventana.config(bg='white')
ventana.geometry('350x250+10+10')
ventana.minsize(width=250, height=200)
ventana.columnconfigure(0, weight=15)
ventana.rowconfigure(0, weight=15)
ventana.columnconfigure([1,2], weight=1)
ventana.rowconfigure([1,2], weight=1)

# Declaramos fecha_final como variable global
fecha_final = datetime.now() + timedelta(days=7)

# Crear variables de cadena para almacenar la fecha actual y la fecha de actualización
fecha_actual_str = StringVar()
fecha_actual_str.set(datetime.now().strftime("%d-%m-%Y"))
fecha_actualizacion_str = StringVar()
fecha_actualizacion_str.set(fecha_final.strftime("%d-%m-%Y"))

def actualizar_contador():
    global fecha_final # Ahora podemos acceder a fecha_final sin problemas
    fecha_actual = datetime.now()
    diferencia = fecha_final - fecha_actual
    dias = diferencia.days
    horas = diferencia.seconds // 3600
    minutos = (diferencia.seconds // 60) % 60
    
    texto_dias.config(text=f'{dias} días')
    texto_horas.config(text=f'{horas} horas')
    texto_minutos.config(text=f'{minutos} minutos')
    
    if diferencia.total_seconds() > 0:
        ventana.after(1000, actualizar_contador)
    else:
        fecha_final = datetime.now() + timedelta(days=7)
        fecha_actualizacion_str.set(fecha_final.strftime("%d-%m-%Y"))
        texto_minutos.config(text=f'El contador se reinició en {datetime.now().strftime("%d-%m-%Y")}')

def iniciar_contador():
    global fecha_final
    fecha_final = datetime.now() + timedelta(days=7)
    fecha_actualizacion_str.set(fecha_final.strftime("%d-%m-%Y"))
    actualizar_contador()

def detener_contador():
    ventana.after_cancel(actualizar_contador)

texto_dias = Label(ventana, text='Días', fg='red', bg='black', font=('Radioland', 10))
texto_dias.grid(row=0, column=0, sticky="nsew", ipadx=5, ipady=20)
texto_horas = Label(ventana, text='Horas', fg='green2', bg='gray3', font=('Comic Sans MS', 10, 'bold'))
texto_horas.grid(row=0, column=1, sticky="nsew", ipadx=5, ipady=20)
texto_minutos = Label(ventana, text='Minutos', fg='blue', bg='gray2', font=('Lucida Calligraphy', 10))
texto_minutos.grid(row=0, column=2, sticky="nsew", ipadx=5, ipady=20)

# Agregar los Entry para mostrar la fecha actual y la fecha de actualización
entry_fecha_actual = Entry(ventana, textvariable=fecha_actual_str, bd=1, bg='yellow', fg='black', state='readonly')
entry_fecha_actual.grid(row=1, column=0, sticky="nsew", ipadx=5, ipady=20)
entry_fecha_actualizacion = Entry(ventana, textvariable=fecha_actualizacion_str, bd=1, bg='white', fg='black', state='readonly')
entry_fecha_actualizacion.grid(row=1, column=1, sticky="nsew", ipadx=5, ipady=20)

# Botón que inicia el contador  
boton_iniciar = Button(ventana, text='Iniciar', command=iniciar_contador)
boton_iniciar.grid(row=1, column=2, sticky="nsew", ipadx=5, ipady=20)

# Botón que detiene o reanuda el contador
boton_detener = Button(ventana, text='Detener', command=detener_contador)
boton_detener.grid(row=2, column=2, sticky="nsew", ipadx=5, ipady=20)

# Mostramos las fechas en los entrys
entry_fecha_actual.insert(END, fecha_actual_str.get())
entry_fecha_actualizacion.insert(END, fecha_actualizacion_str.get())

# Iniciamos el contador
ventana.after(1000, actualizar_contador)
ventana.mainloop()
