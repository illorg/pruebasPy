tasa_interes_anual = int(input('ingrese interes anual: '))
tasa_penalizada_anual = tasa_interes_anual + 10
cert_fiscal = True
monto_prestamo = int(input('ingrese monto prestamo: '))
nombre = input('ingrese nombre: ')


def Evaluador(monto_prestamo, cert_fiscal):
    if cert_fiscal:
        evaluacion = monto_prestamo * (tasa_interes_anual / 100)\
             + monto_prestamo
    else:
        evaluacion = monto_prestamo * (tasa_penalizada_anual / 100)\
             + monto_prestamo
    return evaluacion


dato = Evaluador(monto_prestamo, cert_fiscal)
print('El monto a saldar por ' + nombre + ' seria de $' + str(dato))
