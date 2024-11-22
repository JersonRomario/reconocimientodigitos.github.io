import os

# Verificar si el archivo existe en la ruta relativa
if os.path.exists('modelo/modelo_mnist.h5'):
    print("El archivo está en la carpeta correcta.")
else:
    print("El archivo no se encuentra en la carpeta.")