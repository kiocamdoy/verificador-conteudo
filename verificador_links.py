
import requests
from urllib.parse import urlparse
import streamlit as st

def verificar_link(link):
    resultado = {}

    if not urlparse(link).scheme:
        link = "https://" + link

    resultado["link_formatado"] = link

    try:
        response = requests.get(link, timeout=5)
        resultado["status_code"] = response.status_code
        resultado["acessivel"] = response.ok
    except requests.RequestException as e:
        resultado["erro"] = str(e)
        resultado["acessivel"] = False

    return resultado
