# Importamos el ModuMódulo
import pywhatkit
# Usamos Un try-except
try:
  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+54_3835520577","Mensaje De Prueba",10,50)
  print("Mensaje Enviado")
  
except:
  print("Ocurrio Un Error")
