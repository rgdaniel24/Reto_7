import pandas as pd

def creardataframe():
  ventas = {'Mes': ['Enero', 'febrero', 'Marzo', 'Abril'], 'Ventas': [30500, 35600, 28300, 33900],'Gastos': [22000, 23400, 18100, 20700]}
  df = pd.DataFrame(ventas)
  print(df)
  return df

def dataframeb():
  balance = 'Ventas'-'Gastos'
