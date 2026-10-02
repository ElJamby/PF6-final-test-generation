import json
import requests

URL = "https://api-colombia.com/api/v1/"


def obtener_datos(endpoint):
    response = requests.get(URL + endpoint)
    return json.loads(response.content)


def dish_fetch(num):
    data = obtener_datos("TypicalDish")
    return data[num - 1]


def main():
    numero = int(input("Elige el número del plato: "))
    plato = dish_fetch(numero)
    print(f"Plato: {plato['name']}")
    print(f"Descripción: {plato['description']}")
    print(f"Ingredientes: {plato['ingredients']}")
