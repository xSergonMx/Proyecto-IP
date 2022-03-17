"""
Ejercicio nivel 2: Cupibook: La nueva red social
Modulo de interacción por consola.

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

import cupibook as cb

def mostrar_amigo( amigo:dict ) -> None:
    nombre = amigo["nombre"]
    fecha_de_nacimiento = amigo["fecha_de_nacimiento"]
    signo_zodiacal = amigo["signo_zodiacal"]
    genero = amigo["genero"]
    genero_musical_favorito = amigo["genero_musical_favorito"]
    genero_literario_favorito = amigo["genero_literario_favorito"]
    numero_de_likes = amigo["likes"]
    numero_de_publicaciones = amigo["numero_de_publicaciones"]
    cantidad_de_amigos = amigo["cantidad_de_amigos"]
    bloqueado = amigo["bloqueado"]

    print("Nombre: " + nombre +
          "\n\nFecha de nacimiento: " + str(fecha_de_nacimiento) +
          "\n\nSigno zodiacal: " + signo_zodiacal +
          "\n\nGénero: " + genero +
          "\n\nGénero musical favorito: " + genero_musical_favorito +
          "\n\nGénero literario favorito: " + genero_literario_favorito +
          "\n\nNúmero de likes: " + str(numero_de_likes) +
          "\n\nNúmero de publicaciones: " + str(numero_de_publicaciones) +
          "\n\nNúmero de amigos: " + str(cantidad_de_amigos) +
          "\n\nBloqueado: " + str(bloqueado)
    )


def ejecutar_encontar_amigo_por_su_nombre(a1:dict, a2:dict, 
                                           a3:dict, a4:dict) -> None:
    """
    Función que ejecuta la opción de encontar al amigo por nombre.

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
    
    El programa debe mostrar al amigo el diccionario del amigo con el
    nombre buscado
    """
    nombre = input("Ingrese el nombre del primer amigo que desea buscar: ")
    amigo = cb.buscar_amigo_por_nombre(nombre, a1, a2, a3, a4)
    if amigo != None:
        mostrar_amigo(amigo)
    else:
        print(f"El amigo {nombre} no existe en CupiBook")

def ejecutar_buscar_amigo_con_mas_likes( a1:dict, a2:dict, 
                                           a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción de buscar al amigo con más likes.

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
    
    El programa debe mostrar al amigo: "El amigo X es el amigo más
    famoso con Y likes." En el cual X es el nombre del amigo y Y su número
    de likes.
    """
    amigo_con_mas_likes = cb.buscar_amigo_con_mas_likes(a1, a2, a3, a4)
    plantilla = "El amigo {0} es el amigo más famoso con {1} likes"
    print(plantilla.format(amigo_con_mas_likes["nombre"], amigo_con_mas_likes["likes"]))

def ejecutar_buscar_amigo_con_menos_publicaciones( a1:dict, a2:dict, 
                                                    a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción de buscar al amigo con menos publicaciones.

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
    
    El programa debe mostrar al amigo: "El amigo X es el amigo con el
    menor número de publicaciones." En el cual X es el nombre del amigo.
    """
    usuario_con_menos_publicaciones = cb.buscar_amigo_con_menos_publicaciones(a1, a2, a3, a4)
    plantilla = "El amigo {0} es el amigo con el menor número de publicaciones"
    print(plantilla.format(usuario_con_menos_publicaciones["nombre"]))

def ejecutar_compatibilidad_segun_signo( a1:dict, a2:dict, 
                                         a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción de encontrar la compatibilidad de dos amigos
    según su signo.

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
    
    En caso de que los signos de los amigos sean compatiles el programa debe
    mostrar al amigo: "El amigo X y el amigo Y son compatibles según su
    signo." En el que X es el nombre del primer amigo y Y es el nombre del
    segundo amigo.
    
    En caso de que los signos de los amigos no sean compatiles el programa 
    debe mostrar al amigo: "El amigo X y el amigo Y no son compatibles 
    según su signo." En el que X es el nombre del primer amigo y Y es el 
    nombre del segundo amigo.

    En caso de que el nombre de alguno de los amigos no se encuentre, debe
    mostrar el mensaje "El amigo X no existe en CupiBook", donde X es el
    nombre que no se encontró
    """
    nombre_amigo1 = input("Ingrese el nombre del primer amigo que desea buscar: ")
    nombre_amigo2 = input("Ingrese el nombre del segundo amigo que desea buscar: ")
    
    amigo1 = cb.buscar_amigo_por_nombre(nombre_amigo1, a1, a2, a3, a4)
    amigo2 = cb.buscar_amigo_por_nombre(nombre_amigo2, a1, a2, a3, a4)
    
    if amigo1 == None:
        print(f"El amigo {nombre_amigo1} no existe en CupiBook")
    elif amigo2 == None:
        print(f"El amigo {nombre_amigo2} no existe en CupiBook")
    else:
        compatibilidad = cb.signo_es_compatible(amigo1, amigo2)
        if compatibilidad:
            print(f"El amigo {nombre_amigo1} y el amigo {nombre_amigo2} son compatibles según su signo.")
        elif not compatibilidad:
            print(f"El amigo {nombre_amigo1} y el amigo {nombre_amigo2} no son compatibles según su signo.")
            

def ejecutar_determinar_cupiamigo( a1:dict, a2:dict, 
                                  a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción de encontrar si dos amigos son Cupiamigos.

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
    
    En caso de que los amigos sean cupiamigos el programa debe
    mostrar al amigo: "El amigo X y el amigo Y son Cupiamigos."
    En el que X es el nombre del primer amigo y Y es el nombre del
    segundo amigo.
    
    En caso de que los amigos no sean cupiamigos el programa debe
    mostrar al amigo: "El amigo X y el amigo Y no son Cupiamigos."
    En el que X es el nombre del primer amigo y Y es el nombre del
    segundo amigo.

    En caso de que el nombre de alguno de los amigos no se encuentre, debe
    mostrar el mensaje "El amigo X no existe en CupiBook", donde X es el
    nombre que no se encontró
    """
    nombre_amigo1 = input("Ingrese el nombre del primer amigo que \
desea buscar: ")
    nombre_amigo2 = input("Ingrese el nombre del segundo amigo que \
desea buscar: ")
    
    amigo1 = cb.buscar_amigo_por_nombre(nombre_amigo1, a1, a2, a3, a4)
    amigo2 = cb.buscar_amigo_por_nombre(nombre_amigo2, a1, a2, a3, a4)
    
    if amigo1 == None:
        print(f"El amigo {nombre_amigo1} no existe en CupiBook")
    elif amigo2 == None:
        print(f"El amigo {nombre_amigo2} no existe en CupiBook")
    else:
        cupiamigos = cb.es_cupiamigo(amigo1, amigo2) 
        if cupiamigos:
            print(f"El amigo {nombre_amigo1} y el amigo {nombre_amigo2} son Cupiamigos.")
        elif not cupiamigos:
            print(f"El amigo {nombre_amigo1} y el amigo {nombre_amigo2} no son Cupiamigos.")
            

def ejecutar_determinar_cupienemigo( a1:dict, a2:dict, 
                                     a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción de encontrar si un amigo es un Cupienemigo.

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
    
    En caso de que el amigo sea Cupienemigo el programa debe mostrar al
    amigo: "El amigo X es un Cupienemigo." En el que X es el nombre del 
    amigo buscado.
    
    En caso de que el amigo no sea Cupienemigo el programa debe mostrar al
    amigo: "El amigo X no es un Cupienemigo." En el que X es el nombre del 
    amigo buscado.

    En caso de que el nombre no se encuentre, debe
    mostrar el mensaje "El amigo X no existe en CupiBook", donde X es el
    nombre que no se encontró
    """
    
    nombre = input("Ingrese el nombre del amigo que desea buscar: ")
    usuario = cb.buscar_amigo_por_nombre(nombre, a1, a2, a3, a4)
    
    if usuario == None:
        print(f"El amigo {nombre} no existe en CupiBook")
    else:
        cupienemigo = cb.es_cupienemigo(usuario)
        if cupienemigo:
            print(f"El amigo {nombre} es un Cupienemigo.")
        elif not cupienemigo:
            print(f"El amigo {nombre} no es un Cupienemigo.")
        

def ejecutar_amigo_mayor_compatibilidad( a1:dict, a2:dict, 
                                           a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción de encontrar el amigo con mayor
    compatibilidad en la plataforma.

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
        
    El programa debe mostrar al amigo: "El amigo X es el amigo con mejor
    puntaje de compatibilidad." En el cual X ese el nombre del amigo con
    mayor puntaje.
    """
    amigo_mas_compatible = cb.amigo_mas_compatibilidad(a1, a2, a3, a4).get("nombre")
    print(f"El amigo {amigo_mas_compatible} es el amigo con mejor puntaje de compatibilidad.")

def ejecutar_amigos_genero_musical_y_literario( a1:dict, a2:dict, 
                                                  a3:dict, a4:dict ) -> None:
    """
    Función que ejecuta la opción contar los amigos con un género musical
    y un género literario determinado.

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
        
    El programa debe mostrar al amigo: "El número de amigos que tienen
    como género musical y como género literario favoritos XXX y YYY son ZZZ."
    En el que XXX es el nombre del género musical buscado, YYY el género 
    literario buscado y ZZZ el número de amigos que tienen los géneros
    buscados como favoritos.
    """
    genero_musical = input("Ingrese el género musical que desea consultar: ")
    genero_literario = input("Ingrese el género literario que desea \
consultar: ")
    numero = cb.contar_amigos_con_generos(a1, a2, a3, a4, genero_musical, genero_literario)
    print(f"""El número de amigos que tienen como
género musical y como género literario 
favoritos {genero_musical} y {genero_literario} son {numero}.""")

def iniciar_aplicacion() -> None:
    fecha_nacimiento_a1 = 19960117
    fecha_nacimiento_a2 = 20030510 #taruo
    fecha_nacimiento_a3 = 20011108
    fecha_nacimiento_a4 = 19990327 #aries
    amigo1 = cb.crear_amigo("Pedro Sánchez", fecha_nacimiento_a1, "M", "pop", "drama", 100,
    20, 5, False) 
    amigo2 = cb.crear_amigo("Luna Ariza", fecha_nacimiento_a2, "O", "pop",
    "drama", 80, 10, 3, False)
    amigo3 = cb.crear_amigo("Paula Hernández", fecha_nacimiento_a3, "F", "salsa",
    "ciencia ficción", 107, 50, 2, False) 
    amigo4 = cb.crear_amigo("Tobías Fuentes", fecha_nacimiento_a4, "M", "rap", "lírico", 20, 1,
    0, True) 

    ejecutando = True
    while ejecutando:
        print("\nAmigos de Cupibook" + ("-"*50))
        print("Amigo 1\n")
        mostrar_amigo(amigo1)
        print("-"*50)

        print("Amigo 2\n")
        mostrar_amigo(amigo2)
        print("-"*50)

        print("Amigo 3\n")
        mostrar_amigo(amigo3)
        print("-"*50)

        print("Amigo 4\n")
        mostrar_amigo(amigo4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            amigo1, amigo2, amigo3, amigo4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion( a1: dict, a2: dict, a3: dict, a4: dict ) -> bool:
    print("Menu de opciones")
    print(" 1 - Buscar amigo con más likes")
    print(" 2 - Buscar amigo con menos publicaciones")
    print(" 3 - Calcular la compatibilidad de dos amigos según signo \
zodiacal")
    print(" 4 - Determinar amigo Cupiamigo")
    print(" 5 - Determinar amigo Cupienemigo")
    print(" 6 - Recomendar amigo con mayor compatibilidad")
    print(" 7 - Contar amigos con género musical y literario favorito")
    print(" 8 - Encontrar amigo por su nombre")
    print(" 9 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_amigo_con_mas_likes(a1, a2, a3, a4)
    elif opcion_elegida == "2":
        ejecutar_buscar_amigo_con_menos_publicaciones(a1, a2, a3, a4)
    elif opcion_elegida == "3":
        ejecutar_compatibilidad_segun_signo(a1, a2, a3, a4)
    elif opcion_elegida == "4":
        ejecutar_determinar_cupiamigo(a1, a2, a3, a4)
    elif opcion_elegida == "5":
        ejecutar_determinar_cupienemigo(a1, a2, a3, a4)
    elif opcion_elegida == "6":
        ejecutar_amigo_mayor_compatibilidad(a1, a2, a3, a4)
    elif opcion_elegida == "7":
        ejecutar_amigos_genero_musical_y_literario(a1, a2, a3, a4)
    elif opcion_elegida == "8":
        ejecutar_encontar_amigo_por_su_nombre(a1, a2, a3, a4)
    elif opcion_elegida == "9":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")
    return continuar_ejecutando

iniciar_aplicacion()
