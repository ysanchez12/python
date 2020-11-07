print("Ejercicio de Amortización")
deudaInicial = float(input("Ingrese el monto a prestar: "))
periodos = int(input("Digite el tiempo del crédito: "))
interes =0.1
amortizacion = deudaInicial / periodos

for i in range(periodos):
    pago = 0
    intereses = interes * 0.1
    pago = intereses + amortizacion

    