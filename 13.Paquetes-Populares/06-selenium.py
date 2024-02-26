from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)

# Abrir GitHub y buscar el boton Sing in y dar clic
browser.get("https://github.com")
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

# Buscar los campos para el usuario y el password
user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

# Enviar el usuario y la contraseña a github y dar enter
user_input.send_keys(os.environ.get("gh_user"))
pass_input.send_keys(os.environ.get("gh_password"))
pass_input.send_keys(Keys.RETURN)
