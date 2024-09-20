import time

def ejercicio1 ():
    palabra= str(input("Por favor ingresar palabra"))
    cantidad= int(input("Por favor ingresar cantidad de veces: "))
    for i in range(cantidad):
        print ("valor de la variable i: ", i+1)
        time.sleep(2)
        print(palabra)
    return palabra 
#ejercicio1()

def ejercicio2():
    edad= int(input("Por favor ingresar los años:"))
    for i in range(edad):
        print("Edad i:",i+1)
        time.sleep(1)
    
#ejercicio2()

def calcular_edad():
    año = int(input("ingresar el año actual: "))
    añon = int(input("ingresar el año de nacimiento:"))
    edad = año- añon
    for i in range(edad):
        print("Año: ",añon + i +1)
        print(i+1)
        time.sleep(1)
    return edad

#calcular_edad()
def numeros_impares():
    numero= int(input("Ingrese el numero: "))

    for i in range(1,numero+1,1):
        time.sleep(1)
        print(i, end=", \n")
        if i==15:
            break;
        

#
def reloj():
    
    numero = int(input("ingrese el limite de segundos"))
    for i in range(60,0,-1):
        print(i, "segundos")
        time.sleep(1)
        if i==numero:
            print("\33[103m"+"tiempo maximo"+"\33[0m")
            break; 
            
#reloj()

def interes_compuesto():
    cantidad_invertida= float(input("ingrese la cantidad a invertir: "))
    interes_inversion= float(input("ingrese el interes de la inversion: "))
    años_inversion= int(input("ingrese la cantidad de años de inversion: "))
    dinero_ganado=cantidad_invertida
    for i in range(1,años_inversion+1):
        inversion= dinero_ganado*(interes_inversion/100)
        time.sleep(1)
        inversion_año= dinero_ganado+inversion
        dinero_ganado= inversion_año
        print(inversion)
        print(inversion_año)
        print("Dinero ganado al año es: ",dinero_ganado)
        
#interes_compuesto()

def triangulo_de_numeros ():
    numero = int(input("Por favor ingrese un número"))
    for i in range(1,numero+1):
        print("*"*i)


#triangulo_de_numeros()     

def descubrir_contraseña ():
    contraseña ="123456789"
    contraseña_ingresada =""
    intento_ingresado = int(input("Por favor ingrese un numero de intentos"))
    intento= 1
    while contraseña_ingresada != contraseña:
        contraseña_ingresada = str(input("Ingrese una contraseña: "))
        if contraseña_ingresada != contraseña:
            print("La contraseña no coinciden")
        if contraseña_ingresada== contraseña:
            print("Contraseña correcta")
            break 
        if intento == intento_ingresado:
            print("Se llego al limete de los intentos")
            break    
        intento= intento + 1

#descubrir_contraseña()

def buscador_de_letras ():
    frase=str(input("ingresar la frace que quieras= "))
    letra=str(input("ingrese la letra que quieras buscar= "))
    contador=0
    for i in frase:
        if i==letra:
            contador=contador+1
    print("la letra ",letra,"se repite ",contador," veces")
buscador_de_letras()