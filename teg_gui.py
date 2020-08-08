import tkinter as tk
import sys
import SimuladorTeg as tg
import threading


def on_double_click(event):
    print("posición del mouse :", event.x, event.y)


def increments():
    global counter
    counter += 1
    counter_lbl['text'] = str(counter)
    if ataque_entry.get() > "" and defensa_entry.get() > "":
        btnluzcargado['bg'] = 'Green'
        btnluzcargar['bg'] = 'Black'
        if btnluzsimular['bg'] == 'Black':
            btnluzsimular['bg'] = 'Blue'
            btnluzsimular['text'] = ">>>SIMULAR<<<"
        else:
            btnluzsimular['bg'] = 'Black'
            btnluzsimular['text'] = "SIMULAR"
    else:
        btnluzcargado['bg'] = 'Black'
        btnluzcargar['bg'] = 'Green'

    app.after(1000, increments)

def arrancadorTH2():
    global th2
    if not th2.is_alive():
        try:
            th2.start()
        except RuntimeError:
            th2 = threading.Thread(target=ejecutar_sim)
            th2.start() 
def ejecutar_sim():
    global resultado
    global variable_simulaciones
     
    fataque = ataque_entry.get()
    fdefensa = defensa_entry.get()
    sys.argv = ['', variable_simulaciones.get(), fataque, fdefensa]
    resultado_lbl['text'] = 'CALCULANDO..........'
    tg.run()  # ejecuto SimuladorTeg.py    
    resultado = float(tg.vict_ataque / tg.simulaciones)
    resultado_lbl['text'] = ("Probab. de victoria : " +
                             "{:.2%}".format(resultado))
    tg.vict_ataque = 0
    tg.vict_defensa = 0
    


   

sys.argv = ['', '', '', '']  # blanqueo sys.argv
counter = 0
opciones_simulaciones = ["10000", "100000", "500000", "1000000"]
resultado = ""
th = threading.Thread(target=counter)
th2 = threading.Thread(target=ejecutar_sim)
#th2.start()
###   Elementos Visuales
app = tk.Tk()
app.title('Simulador Probabilidades TEG Python')
app.geometry("400x250")
variable_simulaciones = tk.StringVar(app)
variable_simulaciones.set(opciones_simulaciones[0])
counter_lbl = tk.Label(app, text=str(counter), font=("Helvetica", 32))
counter_lbl.grid(padx=8, pady=8)
resultado_lbl = tk.Label(app, text=str(resultado), font=("", 16))
resultado_lbl.grid(row=5,columnspan=2, pady=5, padx=5, )
ataque_lbl = tk.Label(app, text='Fichas de ataque')
ataque_lbl.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W )
ataque_entry = tk.Entry()
ataque_entry.grid(row=1, column=1, pady=5, padx=5)
defensa_lbl = tk.Label(app, text='Fichas de defensa')
defensa_lbl.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W )
defensa_entry = tk.Entry()
defensa_entry.grid(row=2, column=1, pady=5, padx=5)
ejecutar_btn = tk.Button(app, text="simular", width=10,
                         pady=5, padx=5, command=arrancadorTH2)
ejecutar_btn.grid(row=4, column=0)
simulaciones_lbl = tk.Label(app, text='Nro de simulaciones')
simulaciones_lbl.grid(row=3, column=0, pady=5, padx=5)
simulaciones_opt = tk.OptionMenu(app, variable_simulaciones,
                                 *opciones_simulaciones)
simulaciones_opt.grid(row=3, column=1, pady=5, padx=5, sticky=tk.E + tk.W)
btnluzcargar =tk.Button(app, text="INGRESAR", fg="white", bg="Green", width=15)
btnluzcargar.grid(row=0, column=3)
btnluzcargado =tk.Button(app, text="CARGADO", fg="white", bg="Black", width=15)
btnluzcargado.grid(row=1, column=3)
btnluzsimular =tk.Button(app, text="SIMULAR", fg="white", bg="Black", width=15)
btnluzsimular.grid(row=2, column=3)
th.start()
app.bind("<Double-Button-1>", on_double_click)
app.after(1000, increments)
app.mainloop()
print("we leave the program")
