fechas_signos = {"capricornio": (22, 12, 20, 1)}
fecha = 20050109
fecha = str(fecha)
mes = int(fecha[4:6])
dia = int(fecha[6:])

plantilla = "Hola {0} esta {1}"
print(plantilla.format("como", "?"))

