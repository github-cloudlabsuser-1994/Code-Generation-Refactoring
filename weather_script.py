import requests

def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta tiene un error HTTP
        datos = respuesta.json()

        if datos.get("cod") != 200:
            print(f"Error al obtener datos: {datos.get('message')}")
            return

        print(f"Clima en {ciudad}:")
        print(f"Temperatura: {datos['main']['temp']}°C")
        print(f"Descripción: {datos['weather'][0]['description']}")
        print(f"Humedad: {datos['main']['humidity']}%")
        print(f"Velocidad del viento: {datos['wind']['speed']} m/s")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")

def main():
    print("Consulta del clima")
    ciudad = input("Ingresa el nombre de la ciudad: ")
    api_key = "200349a97dd27c8227d9a4a0669b4597"  # Reemplaza con tu clave de API
    obtener_clima(ciudad, api_key)

if __name__ == "__main__":
    main()