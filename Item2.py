Vamos a subir otro Script Python

import requests

def obtener_distancia(ciudad_origen, ciudad_destino):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={ciudad_origen}&destinations={ciudad_destino}&language=es-ES"
    respuesta = requests.get(url)
    datos = respuesta.json()
    distancia = datos['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convertir la distancia de metros a kilómetros
    return distancia

def calcular_duracion(distancia):
    velocidad_promedio = 80  # km/h
    tiempo = distancia / velocidad_promedio
    horas = int(tiempo)
    minutos = int((tiempo * 60) % 60)
    segundos = int((tiempo * 3600) % 60)
    return horas, minutos, segundos

def calcular_combustible(distancia):
    rendimiento_vehiculo = 12  # km/l
    combustible = distancia / rendimiento_vehiculo
    return round(combustible, 1)

def main():
    ciudad_origen = input("Ciudad de Origen: ")
    ciudad_destino = input("Ciudad de Destino: ")

    distancia = obtener_distancia(ciudad_origen, ciudad_destino)
    duracion_horas, duracion_minutos, duracion_segundos = calcular_duracion(distancia)
    combustible_requerido = calcular_combustible(distancia)

    print("Duración del viaje:")
    print(f"Horas: {duracion_horas}")
    print(f"Minutos: {duracion_minutos}")
    print(f"Segundos: {duracion_segundos}")
    print(f"Combustible requerido: {combustible_requerido} lts")

    # Imprimir la narrativa del viaje
    print(f"Viaje desde {ciudad_origen} hacia {ciudad_destino}")

    # Agregar la letra 'S' como salida
    print("S")

if __name__ == '__main__':
    main()

Este texto se agregó originalmente en la rama de características
