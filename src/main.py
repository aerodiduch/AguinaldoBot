from datetime import datetime as dt, timedelta
import json
from dotenv import load_dotenv
import tweepy
import os

load_dotenv()

auth = tweepy.OAuthHandler(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET")
    )

auth.set_access_token(
    key=os.getenv("ACCESS_TOKEN"),
    secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

api = tweepy.API(auth)

fecha_de_hoy = dt.now()

def get_aguinaldos() -> list:
    fechas = []
    with open("aguinaldos.json", "r", encoding='utf8') as file:
        data = json.load(file)
    AGUINALDO_JUN = dt.fromisoformat(data["jun"])
    AGUINALDO_DIC = dt.fromisoformat(data["dic"])
    fechas.append(AGUINALDO_DIC)
    fechas.append(AGUINALDO_JUN)
    return fechas

def fecha_mas_cercana(fechas: list, pivot) -> dt:
    return min(fechas, key=lambda x: abs(x - pivot))


def dias_para_proximo_aguinaldo(fechas: list, fecha_hoy):
    proximo = fecha_mas_cercana(fechas, fecha_hoy)
    if proximo == fecha_de_hoy:
        api.update_status("🎉🎉🎉 HOY SE COBRA AGUINALDO CARAJO!! 🎉🎉🎉")
        actualizar_fecha(proximo)
    else:
        tiempo_restante = proximo - fecha_de_hoy
        api.update_status(f"Faltan {tiempo_restante.days} días para cobrar el aguinaldo 😎")
        pass
    
def actualizar_fecha(fecha):
    with open("aguinaldos.json", "r", encoding='utf8') as file:
        data = json.load(file)
    for key, value in data.items():
        if value == dt.isoformat(fecha):
            actualizado = fecha + timedelta(days=365)
            data[key] = dt.isoformat(actualizado)
    with open("aguinaldos.json", "w", encoding='utf8') as file:
        json.dump(data, file)


if __name__ == "__main__":
    fechas_de_aguinaldos = get_aguinaldos()
    dias_para_proximo_aguinaldo(fechas_de_aguinaldos, fecha_de_hoy)
