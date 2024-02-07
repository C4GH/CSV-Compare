import pandas as pd

def comparar(archivo1, archivo2):
    df1 = pd.read_csv(archivo1, header=None)
    df2 = pd.read_csv(archivo2, header=None)
    resultado = df2.iloc[:, 1:] - df1.iloc[:, 1:]
    resultado.to_csv('resultado.csv', index=False)
    print("Resultado de la resta guardado en resultado.csv")

if __name__ == "__main__":
    archivo1 = 'limpio400.csv'
    archivo2 = 'limpio800.csv'
    comparar(archivo1, archivo2)

