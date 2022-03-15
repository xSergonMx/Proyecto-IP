"""
Ejercicio nivel 2: Cupibook: La nueva red social
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""

def crear_amigo( nombre: str, fecha_de_nacimiento: int,
                 genero: str, genero_musical_favorito: str,
                 genero_literario_favorito: str,
                 numero_de_likes: int,
                 numero_de_publicaciones: int, cantidad_de_amigos: int,
                 bloqueado: bool) -> dict:
    """
    Función para crear un amigo en la plataforma. El signo zodiacal se asigna a partir
    de la fecha de nacimiento usando la función auxiliar asignar_signo_zodiacal.

    Parámetros
    ----------
    nombre : str
        Nombre del amigo.
    fecha_de_nacimiento : int
        Fecha de nacimiento del amigo representada como un entero de 8 dígitos
        en formato YYYYMMDD.
    genero : str
        Género del amigo.
    genero_musical_favorito : str
        Género musical favorito del amigo.
    genero_literario_favorito : str
        Género literario favorito del amigo.
    numero_de_likes : int
        Número de likes que tiene el amigo.
    numero_de_publicaciones : int
        Número de publicaciones que tiene el amigo.
    cantidad_de_amigos : int
        Número de amigos que se tienen
    bloqueado : bool
        Valor booleano que indica si un amigo está bloqueado o no.

    Retorno
    -------
    dict
        Diccionario del amigo con su información.

    """
    usuario = {"nombre":nombre,
               "fecha_nacimiento": fecha_de_nacimiento,
               "signo_zodiacal": asignar_signo_zodiacal(fecha_de_nacimiento),
               "genero": genero,
               "genero_musical_favorito": genero_musical_favorito,
               "genero_literario_favorito": genero_literario_favorito,
               "likes": numero_de_likes,
               "numero_de_publicaciones": numero_de_publicaciones,
               "bloqueado": bloqueado,
               "cantidad_de_amigos":cantidad_de_amigos,}

    return usuario


def buscar_amigo_por_nombre(nombre: str, a1: dict, a2: dict, a3: dict,
                            a4: dict) -> dict:
    """
    Busca el amigo con el nombre pasado por parámetro.
    En caso de no haber coincidencia se retorna None.

    Parámetros
    ----------
    nombre : str
        Nombre del amigo que se desea buscar.
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario del amigo con el nombre pasado por parámetro.
        Retorna None si no lo encuentra.

    """
    dicc_amigo = None
    if a1.get("nombre") == nombre:
        dicc_amigo = a1
    if a2.get("nombre") == nombre:
        dicc_amigo = a2
    if a3.get("nombre") == nombre:
        dicc_amigo = a3
    if a4.get("nombre") == nombre:
        dicc_amigo = a4

    return dicc_amigo


def buscar_amigo_con_mas_likes( a1: dict, a2: dict, a3: dict,
                               a4: dict ) -> dict:
    """
    Determina cuál es el amigo con más likes en la plataforma.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario que representa al amigo más famoso de la plataforma
    """
    likes = a1.get("likes")
    amigo_famoso = a1

    if likes < a2.get("likes"):
        likes = a2.get("likes")
        amigo_famoso = a2
    if likes < a3.get("likes"):
        amigo_famoso = a3

    return amigo_famoso


def buscar_amigo_con_menos_publicaciones( a1: dict, a2: dict, a3: dict,
                                         a4: dict ) -> dict:
    """
    Determina cuál es el amigo con menos publicaciones en la plataforma.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario que representa al amigo con menos publicaciones en la plataforma.
    """
    publicaciones = a1.get("numero_de_publicaciones")
    menos_publicaciones = a1

    if publicaciones > a2.get("numero_de_publicaciones"):
        publicaciones = a2.get("numero_de_publicaciones")
        menos_publicaciones = a2
    if publicaciones > a3.get("numero_de_publicaciones"):
        menos_publicaciones = a3

    return menos_publicaciones


def determinar_signo(dia:int, mes: int, fecha_signos:dict) -> str:
    
    capricornio = fecha_signos["capricornio"]
    acuario = fecha_signos["acuario"]
    piscis = fecha_signos["piscis"]
    aries = fecha_signos["aries"]
    tauro = fecha_signos["tauro"]
    geminis = fecha_signos["geminis"]
    cancer = fecha_signos["cancer"]
    leo = fecha_signos["leo"]
    virgo = fecha_signos["virgo"]
    libra = fecha_signos["libra"]
    escorpio = fecha_signos["escorpio"]
    sagitario = fecha_signos["sagitario"]

    if (mes == capricornio[0] and dia >= capricornio[1]) or (mes == capricornio[2] and dia <= capricornio[3]):
        resultado = "capricornio"
    elif (mes == acuario[0] and dia >= acuario[1]) or (mes == acuario[2] and dia <= acuario[3]):
        resultado = "acuario"
    elif (mes == piscis[0] and dia >= piscis[1]) or (mes == piscis[2] and dia <= piscis[3]):
        resultado = "piscis"
    elif (mes == aries[0] and dia >= aries[1]) or (mes == aries[2] and dia <= aries[3]):
        resultado = "aries"
    elif (mes == tauro[0] and dia >= tauro[1]) or (mes == tauro[2] and dia <= tauro[3]):
        resultado = "tauro"
    elif (mes == geminis[0] and dia >= geminis[1]) or (mes == geminis[2] and dia <= geminis[3]):
        resultado = "geminis"
    elif (mes == cancer[0] and dia >= cancer[1]) or (mes == cancer[2] and dia <= cancer[3]):
        resultado = "cancer"
    elif (mes == leo[0] and dia >= leo[1]) or (mes == leo[2] and dia <= leo[3]):
        resultado = "leo"
    elif (mes == virgo[0] and dia >= virgo[1]) or (mes == virgo[2] and dia <= virgo[3]):
        resultado = "virgo"
    elif (mes == libra[0] and dia >= libra[1]) or (mes == libra[2] and dia <= libra[3]):
        resultado = "libra"
    elif (mes == escorpio[0] and dia >= escorpio[1]) or (mes == escorpio[2] and dia <= escorpio[3]):
        resultado = "escorpio"
    elif (mes == sagitario[0] and dia >= sagitario[1]) or (mes == sagitario[2] and dia <= sagitario[3]):
        resultado = "sagitario"

    return resultado


def asignar_signo_zodiacal(fecha: int) -> str:
    """
    Función que determina de acuerdo a una fecha dada, el signo zodiacal
    correspondiente.

    Parámetros
    ----------
    fecha : int
        Fecha de nacimiento del amigo representada como un entero de 8 dígitos
        en formato YYYYMMDD.

    Retorno
    -------
    str
        Cadena con el signo zodiacal del amigo.

    """
    fecha_signos = {"capricornio": (12, 22, 1, 20),
                    "acuario": (1, 21, 2, 19),
                    "piscis": (2, 20, 3, 20),
                    "aries": (3,21, 4, 20),
                    "tauro": (4, 21, 5, 21),
                    "geminis": (5, 22, 6, 21),
                    "cancer": (6,22, 7, 22),
                    "leo": (7, 23, 8, 22),
                    "virgo": (8, 23, 9, 22),
                    "libra": (9, 23, 10, 22),
                    "escorpio": (10, 23, 11, 22),
                    "sagitario": (11, 23, 12, 21)}

    fecha = str(fecha)
    mes = int(fecha[4:6])
    dia = int(fecha[6:])
    signo = determinar_signo(dia, mes, fecha_signos)


    return signo

#print(asignar_signo_zodiacal(19771226))


def es_cupiamigo( amigo1: dict , amigo2: dict) -> bool:
    """
    Función que determina si dos amigos son Cupiamigos.

    Parámetros
    ----------
    amigo1 : dict
        Información del primer amigo.
    amigo2 : dict
        Información del segundo amigo.

    Retorno
    -------
    bool
        True si los dos amigos son Cupiamigos, False de lo contrario.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def es_cupienemigo( amigo:dict ) -> bool:
    """
    Función que determina si un amigo es Cupienemigo.

    Parámetros
    ----------
    amigo : dict
        Información del amigo.

    Retorno
    -------
    bool
        True si es Cupienemigo, False de lo contrario.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def signo_es_compatible( amigo1: dict, amigo2: dict ) -> bool:
    """
    Función que determina compatibilidad entre signos de dos amigos.

    Parámetros
    ----------
    amigo1 : dict
        Información el primer amigo.
    amigo2 : dict
        Información el segundo amigo.

    Retorno
    -------
    bool
        True si los dos amigos son compatibles según su signo, False de lo
        contrario.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def amigo_mas_compatibilidad( a1: dict, a2: dict,
                               a3: dict, a4: dict ) -> dict:
    """
    Función que determina el amigo con mayor puntaje de compatibilidad en la
    plataforma.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario con la infromación del amigo con mayor puntaje de
        compatibilidad.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def contar_amigos_con_generos(a1: dict, a2: dict,
                                a3: dict, a4: dict, genero_musical:str,
                                genero_literario: str) -> int:
    """
    Función que cuenta los amigos con un género musical y un género literario
    favorito determinado.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.
    genero_musical : str
        Género musical a buscar.
    genero_literario : str
        Género literario a buscar.

    Retorno
    -------
    int
        Número de amigos con el género musical y literario favorito pasados
        por parámetro.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None
