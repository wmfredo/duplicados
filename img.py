import os
from datetime import datetime

ruta_app = os.getcwd() + "img\\" # obtiene ruta del script
print(ruta_app)

contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir

num_archivos = 0
formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora

archivos =[]

for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    num_archivos += 1
        
    estado = os.stat(archivo)           # obtiene estado del archivo
    size = estado.st_size               
    ult_acceso = estado.st_atime        
    modificado = estado.st_mtime

    archivos.append([elemento, size, modificado])
    #print ([elemento, size, modificado])
    
    # Obtiene del estado fechas de último acceso/modificación
    # Como los valores de las fechas-horas vienen expresados
    # en segundos se convierten a tipo datetime. 
        
    #ult_acceso = datetime.fromtimestamp(estado.st_atime)
    #modificado = datetime.fromtimestamp(estado.st_mtime)
        
    # Se aplica el formato establecido de fecha y hora
        
    #ult_acceso = ult_acceso.strftime(formato)
    #modificado = modificado.strftime(formato)
        
    # Se muestra info de cada archivo

    #info = 'archivo: ' + elemento + ' modificado: ' + modificado + ' último acceso: ' + ult_acceso + ' tamaño: ' + str(round(size/1024, 1))
    #print (info)

for img in archivos:    
    print(img)
    
print('Núm. archivos:', num_archivos)
