import tkinter as tk
import sys
import time
import SimuladorTeg as tg
import threading

def on_double_click(event):
    print("posición del mouse :", event.x, event.y)


def increments():
    global counter
    counter += 1
    counter_lbl['text'] = str(counter)
    app.after(1000, increments)


def ejecutar_sim():
    global resultado
    global variable_simulaciones
    fataque = ataque_entry.get()
    fdefensa = defensa_entry.get()
    sys.argv = ['', variable_simulaciones.get(), fataque, fdefensa]
    resultado_lbl['text'] = 'CALCULANDO..........'

    tg.run() # ejecuto SimuladorTeg.py
    resultado =  float(tg.vict_ataque / tg.simulaciones)
    resultado_lbl['text'] = ("Probab. de victoria : " + 
                             "{:.2%}".format(resultado))
    tg.vict_ataque = 0
    tg.vict_defensa = 0


sys.argv = ['', '', '', '']# blanqueo sys.argv
app = tk.Tk()
counter = 0
opciones_simulaciones = ["10000", "100000", "500000", "1000000"]
resultado = ""
th = threading.Thread(target=ejecutar_sim)
app.geometry("300x300")
variable_simulaciones = tk.StringVar(app)
variable_simulaciones.set(opciones_simulaciones[0])
counter_lbl = tk.Label(app, text=str(counter), font=("", 32))
counter_lbl.grid(padx=8, pady=8)
resultado_lbl = tk.Label(app, text=str(resultado), font=("", 16))
resultado_lbl.grid(row=5,columnspan=2, pady=5, padx=5, )
ataque_lbl = tk.Label(app, text='Fichas de ataque')
ataque_lbl.grid(row=1, column=0, pady=5, padx=5, )
ataque_entry = tk.Entry()
ataque_entry.grid(row=1, column=1, pady=5, padx=5)
defensa_lbl = tk.Label(app, text='Fichas de defensa')
defensa_lbl.grid(row=2, column=0, pady=5, padx=5, )
defensa_entry = tk.Entry()
defensa_entry.grid(row=2, column=1, pady=5, padx=5)
ejecutar_btn = tk.Button(app, text="simular", width=10,
                         pady=5, padx=5, command=th.start)
ejecutar_btn.grid(row=4, column=0)
simulaciones_lbl = tk.Label(app, text='Nro de simulaciones')
simulaciones_lbl.grid(row=3, column=0, pady=5, padx=5)
simulaciones_opt = tk.OptionMenu(app, variable_simulaciones,
                                 *opciones_simulaciones)
simulaciones_opt.grid(row=3, column=1, pady=5, padx=5)

app.bind("<Double-Button-1>", on_double_click)
app.after(1000, increments)
app.mainloop()
print("we leave the program")
