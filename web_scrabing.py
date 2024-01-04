from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from difflib import SequenceMatcher
import time

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def obtener_productos_carrefour(busqueda):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome()

    wd.get(f"https://www.carrefour.es/?q={busqueda.replace(' ', '+')}")

    WebDriverWait(wd, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    titulo_pagina = wd.title
    print("Titulo de la pagina:", titulo_pagina)
    time.sleep(10)

    buscador = wd.find_element(By.ID, 'search-input')
    buscador.send_keys(busqueda)
    buscador.send_keys(Keys.ENTER)

    try:
        WebDriverWait(wd, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'ebx-result--normal')))
        print("¡Resultados de busqueda encontrados en Carrefour!")

        productos_carrefour = {}
        carrefour_elements = wd.find_elements(By.CLASS_NAME, 'ebx-result--normal')
        for producto in carrefour_elements:
            titulo_producto = producto.find_element(By.CLASS_NAME, 'ebx-result-title').text
            precio_producto = producto.find_element(By.CLASS_NAME, 'ebx-result-price').text
            productos_carrefour[titulo_producto] = precio_producto

        return productos_carrefour

    except Exception as e:
        print(f"Error al obtener resultados de Carrefour: {e}")
    finally:
        wd.quit()

def obtener_productos_consum(busqueda):
    chrome_path = './chromedriver.exe'
    driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver.get(f"https://tienda.consum.es/es/s/{busqueda.replace(' ', '%20')}")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'widget-prod__info')))
        print("¡Resultados de busqueda en Consum encontrados!")

        productos_consum = {}
        consum_elements = driver.find_elements(By.CLASS_NAME, 'widget-prod__info')
        for producto in consum_elements:
            try:
                titulo_producto = producto.find_element(By.CLASS_NAME, 'widget-prod__info-description').text
                precio_producto = producto.find_element(By.CLASS_NAME, 'widget-prod__info-unitprice').text
                productos_consum[titulo_producto] = precio_producto
            except (NoSuchElementException, StaleElementReferenceException) as ex:
                print(f"No se pudo encontrar el titulo del producto en Consum: {ex}")

        return productos_consum

    except Exception as e:
        print(f"Error al obtener resultados de Consum: {e}")
    finally:
        driver.quit()

def comparar_productos(supermercado1, supermercado2):
    diccionario_resultados = {'consum': {}, 'carrefour': {}, 'porcentaje': {}}

    for producto1, precio1 in supermercado1.items():
        for producto2, precio2 in supermercado2.items():
            porcentaje_similitud = similar(producto1, producto2)
            if porcentaje_similitud > 0.66:
                diccionario_resultados['consum'][producto1] = precio1
                diccionario_resultados['carrefour'][producto2] = precio2
                diccionario_resultados['porcentaje'][producto1] = porcentaje_similitud

    return diccionario_resultados

if __name__ == "__main__":
    busqueda = 'chocolate milka'

    productos_carrefour = obtener_productos_carrefour(busqueda)
    productos_consum = obtener_productos_consum(busqueda)

    diccionario_resultados = comparar_productos(productos_carrefour, productos_consum)

    print(diccionario_resultados)