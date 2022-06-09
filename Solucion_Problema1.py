import pandas as pd

def creardataframe():
  ventas = {'Mes': ['Enero', 'febrero', 'Marzo', 'Abril'], 'Ventas': [30500, 35600, 28300, 33900],'Gastos': [22000, 23400, 18100, 20700]}
  df = pd.DataFrame(ventas)
  return df

# NOTE: Estás intentando restar un string, por eso te sale error. Te lo dejo comentado por si lo quieres quitar
"""
def dataframeb():
  balance = 'Ventas'-'Gastos'
"""

# TODO: Ten cuidado! te mostré una pequeña solución, más no la completa. Lee bien lo que te piden y mira como puedes hacerlo. Necesitas recibir en esta función un DataFrame, y los meses que quiere obtener el balance.
# Debería de ser así la función balance(DataFrame, Meses)
def balance(df):
    ventas= df['Ventas']
    gastos= df['Gastos']
    return ventas.subtract(gastos)

# Esta variable almacena un DataFrame
df= creardataframe()
# Imprimo el balance
print(balance(df))
