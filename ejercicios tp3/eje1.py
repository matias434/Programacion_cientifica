def correo_electronico(correo):
   return "@" in correo
correo=input("ingrese su correo electrónico: ")
if correo_electronico(correo):
 print("la direccion de correo es valida")
else:
 print("la direccion de correo no es valida")
