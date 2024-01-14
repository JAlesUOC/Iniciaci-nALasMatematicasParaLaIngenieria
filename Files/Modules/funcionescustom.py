# Numeros Naturales
def esdivisible (dividendo, divisor):
    """
    :param dividendo:
    :param divisor:
    :return: Cadena que expresa si el dividendo es divisible o no por el divisor
    """

    if dividendo % divisor == 0:
        resultado= f'El {dividendo} es divisible por {divisor}'
    else:
        resultado= f'El {dividendo} no es divisible por {divisor}'

    return resultado

def numeroprimo(numero):
    '''
    Funcion que comprueba si el numero es primo, devolviendo un booleano como respuesta
    :param numero: Numero que se desea comprobar
    :return: True si el Numero es primo, False si no es primo
    '''

    for divisor in range(2,numero):
        if numero % divisor == 0:
            return False
    return True

def factorizar(numero):
    '''
    Funcion que devuelve una lista con los factores del numero que se le pasa por parametro
    :param numero: Numero que se desea factorizar
    :return: Lista con los factores del número, el 1 devuelve una lista vacia
    '''
    factores=[]
    divisor = 2
    while numero >=2:
        if numero % divisor == 0:
            factores.append(divisor)
            numero=numero/divisor # Actualizamos el nuevo numero
            divisor=2 # Reiniciamos el divisor
        else:
            divisor=divisor+1

    return factores

def factorizaciondict(numero):
    '''
    Funcion que devuelve un diccionario con los factores y las veces que aparece
    :param numero: Numero que se desea factorizar
    :return: Diccionario con los factores y las veces que aparece
    '''

    factores=[]
    factores_dict={}
    divisor = 2
    # Creamos la lista de los factores
    while numero >=2:
        if numero % divisor == 0:
            factores.append(divisor)
            numero=numero/divisor # Actualizamos el nuevo numero
            divisor=2 # Reiniciamos el divisor
        else:
            divisor=divisor+1

    # Creamos el diccionario con los factores (factor:veces que aparece)
    for factor in factores:
        if factor in factores_dict:
            factores_dict[factor]=factores_dict[factor]+1
        else:
            factores_dict[factor]=1

    return factores_dict

def mcd(fact_num1,fact_num2):
    """
     Función que calcula el Máximo Común Divisor de los dos números que se les pase por parámetro
    :param fact_num1: Diccionario con los factores del primer número
    :param fact_num2: Diccionario con los factores del segundo número
    :return: El resultado del Máximo Común Divisor de ambos números
    """
    res_mcd=1

    # Valores comunes, elegimos el de menor exponente
    for valor in set(fact_num1).intersection(set(fact_num2)):
        if fact_num1[valor]<=fact_num2[valor]:
            res_mcd*= valor**fact_num1[valor]
        else:
            res_mcd*= valor**fact_num2[valor]

    return res_mcd

def mcm(fact_num1,fact_num2):
    """
     Función que calcula el Mínimo Común Múltiplo de los dos números que se les pase por parámetro
    :param fact_num1: Diccionario con los factores del primer número
    :param fact_num2: Diccionario con los factores del segundo número
    :return: El resultado del Mínimo Común Múltiplo de ambos números
    """
    res_mcm=1
    # Valores comunes, elegimos el mayor
    for valor in set(fact_num1).intersection(set(fact_num2)):
        if fact_num1[valor]<=fact_num2[valor]:
            res_mcm*= valor**fact_num2[valor]
        else:
            res_mcm*= valor**fact_num2[valor]
    # Valores diferentes, lo multiplicamos al resultado con su exponente correspondiente
    # La resta de conjuntos NO ES COMUNMUTATIVA
    for valor in set(fact_num1).difference(fact_num2):
        res_mcm*= valor**fact_num1[valor]

    for valor in set(fact_num2).difference(fact_num1):
        res_mcm*= valor**fact_num2[valor]

    return res_mcm

# Numeros Enteros
def valorabsoluto(numero):
    if numero >= 0:
        num_abs = numero
    else:
        num_abs = numero*-1 #Le cambiamos el signo

    return num_abs

def tipodeentero(numero):
    """
    Función que nos dirá si un número es un entero positivo, negativo o 0
    :param numero: El número a analizar
    :return: cadena que expresa el tipo de entero pasado por parámetro
    """
    if numero > 0:
        resultado = f'El numero {numero} es un entero positivo'
    elif numero < 0:
        resultado = f'El numero {numero} es un entero negativo'
    else:
        resultado = f'El 0 tambien es un entero, ni positivo ni negativo'

    return resultado

# Numeros Racionales
def fraccionirreducible(num,dem):
    """
    Dados el numerador y el denominador de una fracción, devuelve el numerador y el denominador de la fracción irreducible equivalente a ellos
    :param num: Número en el denominador
    :param dem: Número en el denominador
    :return: numerador y denominadador de la fracción irreducible
    """
    factores1=factorizaciondict(num)
    factores2=factorizaciondict(dem)
    resultado_mcd = mcd(factores1,factores2)
    if resultado_mcd  != 1:
        num,dem = num/resultado_mcd ,dem/resultado_mcd
    return num,dem