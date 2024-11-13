# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")

# Abrir o Navegador
navegador = webdriver.Firefox()

# Acessar o site desejado
navegador.get('http://127.0.0.1:8000/admin')

# Maximar janela do navegador
navegador.maximize_window()

# Login
navegador.find_element("id", "id_username").send_keys(admin_username)
navegador.find_element("id", "id_password").send_keys(admin_password)
botao_login = navegador.find_element("class name", "submit-row")
botao_login.click()

# Selecionar respondente e enviar email
respondent_email = navegador.find_element("id", "respondent")
respondent_email.click()
dropdown = Select(respondent_email)
dropdown.select_by_value("2")

botao_enviar = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Enviar Formulário']"))
)
botao_enviar.click()

time.sleep(10)