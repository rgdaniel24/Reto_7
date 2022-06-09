import pandas as pd

e = ['Enero', 30500, 22000]
f = ['Febrero', 35600, 23400]
m = ['Marzo', 28300, 18100]
a = ['Abril', 33900, 20700]

ventas = [e, f, m, a]

def creardataframe():
  ventas1 =pd.DataFrame(ventas, 
            columns = ['Mes', 'Ventas', 'Gastos'])
  print(ventas1)
  return ventas1

def creardataframeb():
  balance = ventas1['Gastos']
