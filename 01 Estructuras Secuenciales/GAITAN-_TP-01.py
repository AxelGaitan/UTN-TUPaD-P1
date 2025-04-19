# 1
men="Hola mundo!"
print(men)
#2
nombre=input("por favor ingrese su nombre: ")
saludo=f"bienvenido {nombre} a mi programa"
print(saludo) 
#3
dato_A=input("por favor ingrese su Nombre y Apellido: ")
dato_B=input("Ahora necesita ingresar su edad: ")
dato_C=input("Donde vive actualmente(ciudad): ")
dato_D=input("Ingrese la provincia a la que pertenece: ")
print(f"""soy {dato_A} y tengo {dato_B}años,
además vivo en la ciudad de {dato_C}, de la provincia de {dato_D}""")
#4
dato_a=float(input("Ingrese el radio del circulo: "))
pi=3.14
area= pi*(dato_a**2)
perimetro=2*pi*dato_a
print(f"el area del circulo es:{area} mientras que su perimetro es:{perimetro}")
#5
seg=int(input( "por favor ingrese los segundos: "))
ope=seg/3600
print(f"""la cantidad de segundos que ingreso,
equivale a : {ope}hs""")
#6
num_f=int(input("Por favor ingrese el numero: "))
multi=num_f*1
multi2=num_f*2
multi3=num_f*3
multi4=num_f*4
multi5=num_f*5
multi6=num_f*6
multi7=num_f*7
multi8=num_f*8
multi9=num_f*9
multi10=num_f*10
print(f"""La tabla de multplicar del numero {num_f}: 
{num_f} X 1 = {multi}
{num_f} X 2 = {multi2}
{num_f} X 3 = {multi3}
{num_f} X 4 = {multi4}
{num_f} X 5 = {multi5}
{num_f} X 6 = {multi6}
{num_f} X 7 = {multi7}
{num_f} X 8 = {multi8}
{num_f} X 9 = {multi9}
{num_f} X 10 = {multi10}
""")
#7
num_1=int(input("Por favor ingrese un numero diferente de 0:  "))
num_2=int(input("Por favor ingrese el segundo numero distinto de 0: "))

suma= num_1+num_2
resta=num_1-num_2
multi=num_1*num_2
div=num_1/num_2

print(f"""La suma del {num_1} y el numero {num_2} es: {suma}.
La resta del {num_1} y el numero {num_2} da como resultado: {resta}.
La multiplicacion del {num_1} por el numero {num_2} es: {multi}. """)

#8
saludo="Bienvenidos a mi programa! para calcular el indice de masa corporal"
pedi=float(input("Ingrese su altura por favor: "))
pedi2=float(input("Ingrese su peso por favor: "))
imc= pedi2/(pedi ** 2)


print(saludo)
print(f"su indice corporal es: {imc}")

#9
grados=int(input("Por favor ingrese la temperatura en grados: "))
calc=(9/5)*grados + 32
print(f"La temperatura ingresada equivale a: {calc} Fahrenheit" )

#10
n1=int(input("ingrese su primer nota: "))
n2=int(input("ingrese su segunda nota: "))
n3=int(input("ingrese su tercer nota: "))
pro=(n1+n2+n3)/3
print(f"el promedio de sus notas es: {pro}")


