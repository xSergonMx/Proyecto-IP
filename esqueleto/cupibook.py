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
    fechas_signos = {"capricornio": (22, 12, 20, 1)}

    fecha = str(fecha)
    mes = int(fecha[4:6])
    dia = int(fecha[6:])


    return f"El dia es {dia} y el mes {mes}"

def determinar_signo(dia:int, mes: int, fecha_signos:dict) -> str:

    for
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):



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
