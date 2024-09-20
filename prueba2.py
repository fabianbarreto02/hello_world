def suma_dos_valores(sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    
    return resultado

#suma_dos_valores(4,5)
#print("primera suma")
#print(resultado)
#suma_dos_valores(1,2)
#print("segunda suma")
#print(resultado)

def calculadora_dos_valores(numero1,numero2,operador):
    global resultado
    if operador ==1: #si el operador es 1 es suma
        resultado = numero1 + numero2
        return resultado    
    elif operador ==2:# si el operador es 2 es resta
        resultado = numero1 - numero2
        return resultado
    elif operador ==3:# si el operador es 3 es mult
        resultado = numero1 * numero2
        return resultado
    elif operador ==4:# si el operador es 4 es divisin
        resultado = numero1 / numero2
        return resultado
    else: # si el operador es otro numero
        print("el numero ingresado no es valido")
    return resultado


#calculadora_dos_valores(1,2,1)
#print("suma",resultado)
#calculadora_dos_valores(1,2,2)
#print("resta",resultado)
#calculadora_dos_valores(1,2,3)
#print("multiplicacio",resultado)
#calculadora_dos_valores(1,2,4)
#print("division",resultado)
    
def pitagoras(a,b):
    global c
    c=(a**2+b**2)**0.5
    return c

#pitagoras(3,4) 
#print("pitagoras",c)

def despeje_x():
    global x 
    b=int(input("Ingrese el valor de B= "))
    c=int(input("Ingrese el valor de C= "))
    x= (c-b)/2
    print("EL valor de x es: ",x)
    return x

#despeje_x()

def pitagoras_funcion_sumar():
    global resul_pitagoras
    a=int(input("Ingresar el valor de a= "))
    b=int(input("Ingresar el valor de b= "))
    a2= a**2
    b2= b**2
    suma= suma_dos_valores(a2,b2)
    resul_pitagoras= suma**0.5
    print("El valor de pitagoras es:", resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()

def separador_contador():
    global resultado_contador
    palabra = str(input("Ingrese la palabra a contar letras:"))
    letra = str(input("Ingrese la letra a contar: "))
    resultado_contador = palabra.count(letra)
    print ("La cantidad de letra",letra, "es= ",resultado_contador)
    print ("La cantidad de letras de la palabra es=", len(palabra))
    print("Palabra separada por letras= ",list(palabra))
    return resultado_contador
#separador_contador()

def eleccion():
    import random
    usuario1= random.choice(["piedra", "papel", "tijera"])
    print(usuario1)
    usuario2=random.choice(["piedra", "papel", "tijera"])
    print(usuario2)
    if usuario1==usuario2:
        print("empate")
    elif (usuario1 == "piedra" and usuario2 == "tijera"):
        print("usuario1 gana")
    elif (usuario1 == "tijera" and usuario2 == "papel"):
        print("usuario1 gana")
    elif (usuario1 == "papel" and usuario2 == "piedra"):
        print("usuario1 gana")
    else:
        print("usuario2 gana")
    return   
#eleccion()
import random
def piedra_papel_tijera():
    
    opciones = ["piedra", "papel", "tijera"]
    jugador2 = random.choice(opciones)
    jugador = random.choice(opciones)
    if jugador == jugador2:
        resultado = "empate"
    elif (jugador == "piedra" and jugador2 == "tijera") or (jugador == "papel" and jugador2 == "piedra") or (jugador == "tijera" and jugador2 == "papel"):
        resultado = "gana jugador 1"
    else:
        resultado = "gana jugador 2"
    print("el jugador 1:", jugador)
    print("el jugador 2:", jugador2)
    print("El resultado :", resultado)
    return resultado

#piedra_papel_tijera()