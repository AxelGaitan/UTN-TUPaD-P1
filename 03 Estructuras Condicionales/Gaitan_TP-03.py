#1
saludo=int(input("Bienvenido a mi programa, por favor ingrese su edad: "))

if saludo >= 18 :
    print("eres mayor de edad")
else:
    print("eres menor de edad")
#2
nota_del_usuario=int(input("Bienvenido, por favor ingrese su nota: "))

if nota_del_usuario >= 6:
    print("aprobado")
else:
    print("desaprobado")
#3
numero_del_usuario=int(input("Bienvenido, por favor ingrese un numero par: "))
verifico= numero_del_usuario %2

if verifico == 0:
    print("ah ingresado un numero par, bien hecho!")
else:
    print("Por favor, ingrese un numero par") 
#4
ingrese_edad=int(input("Ingrese su edad y le diremos a que categoria pertenece: "))
if ingrese_edad < 12:
    print(" Niño ")
elif ingrese_edad >= 12 and ingrese_edad < 18:
    print(" Adolescente ")
elif ingrese_edad >= 18 and ingrese_edad < 30:
    print (" Adulto Joven ")
else:
    print(" Adulto ")

#5
ingrese_contra=input("""por favor ingrese una contraseña
esta debe tener entre 8 y 14 caracteres: """)
control= len(ingrese_contra)
if control >= 8 and control <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de 8 a 14 caracteres")

#6
import random
from statistics import mode, median, mean
lista_aleatoria= [random.randint(1, 100) for i in range(50)]

media= mean(lista_aleatoria)
mediana=median(lista_aleatoria)
moda=mode(lista_aleatoria)


if media> mediana and mediana > moda:
    sesgo="positivo"
elif media < mediana and mediana < moda:
    sesgo= 'negativo'
elif media== mediana and mediana==moda:
    sesgo = "sin sesgo"
else:
    sesgo= 'no se puede determinar un sesgo claro'
    
print('lista de numeros: ', lista_aleatoria)
print('media: ', media)
print('mediana', mediana)
print('moda', moda)
print('sesgo:',sesgo)


#7
frase_de_usuario=str(input("por favor ingrese una frase o una palabra: "))

if frase_de_usuario.lower().endswith(('a','e','i','o','u')):
    print(f"la frase o palabra {frase_de_usuario}! termina con vocal!")
else:
    print(frase_de_usuario)
    
##puede haber otra solucion tambien que no implique usar estos metodos:

frase_de_usuario=str(input("por favor ingrese una frase o una palabra: "))
controlo_la_letra=frase_de_usuario[-1].lower()
if controlo_la_letra in ("a","e","i","o","u"):
    print(f"la frase o palabra {frase_de_usuario}! termina con vocal!")
else:
    print(frase_de_usuario)

#8
ingreso=input("Bienvenido al programa! para empzar necesito su nombre: ")
seleccion=int(input("""Menu del usuario:
                    
                    1) Imprimir mi nombre en mayuscula.Por ejemplo: PEDRO.
                    2) Imprimir mi nombre en minuscula.Por ejemplo: pedro.
                    3) Escribir mi nombre con la primera letra mayuscula. Por ejemplo: Pedro.
                    
                    
                    seleccione el numero de la accion que desea realizar: 
                    """))
if seleccion==1:
    print(ingreso.upper())
elif seleccion==2:
    print(ingreso.lower())
elif seleccion==3:
    print(ingreso.title())
else:
    print('usted ah ingresado una opcion que no exíste!')
    
    
#9
magnitud= float(input("ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve(imperceptible)")
elif 3<= magnitud <4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5<= magnitud <6:
    print("Fuerte(puede causar daños en estructuras debiles)")
elif 6<= magnitud <7:
    print("Muy Fuerte(puede causar daños significativos)")
else:
    print("Extremo!(puede causar daños a gran escala)")
    
    
#10
hemisferio= input("ingrese su hemisferio (N/S): ").upper()
mes= int(input("en que mes estamos? (1 a 12): "))
dia=int(input("ingrese en que dia estamos(solo el numero): "))

def obtener_estacion(mes, dia):
    if(mes==12 and dia >=21) or (mes in [1,2]) or (mes==3 and dia <=20):
        return "invierno"
    elif (mes ==3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <=20):
        return "primavera"
    elif (mes == 6 and dia>=21) or (mes in[7,8]) or (mes == 9 and dia<=20):
        return "verano"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        return "otoño"
    



estacion_norte=obtener_estacion(mes, dia)
if hemisferio == "N":
    estacion = estacion_norte
elif hemisferio=="S":
    if estacion_norte== "verano":
        estacion= "invierno"
    elif estacion_norte=="invierno":
        estacion="verano"
    elif estacion_norte== "primavera":
        estacion="otoño"
    elif estacion_norte=="otoño":
        estacion="primavera"
else:
    estacion="hemisferio no valido"
        
print("Estacion del año:", estacion) 