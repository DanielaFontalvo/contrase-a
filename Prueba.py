from binascii import a2b_base64
from importlib.resources import path
from re import A
import pandas as pd
import os

path= r'C:\Users\equipo\OneDrive\Escritorio\contraseña\datos prueba 1.csv'
contraseña = input('nombre:')
df=pd.DataFrame([[contraseña]])
df.to_csv(r'C:\Users\equipo\OneDrive\Escritorio\contraseña\datos prueba 1.csv', index= False, mode= 'a', header= not os.path.isfile(path))