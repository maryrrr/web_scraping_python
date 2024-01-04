
#  Araña rastreadora
Realiza la búsqueda de los productos de consum mediante web scraping:
1. Recuerda que en la url de consum, la búsqueda de productos se realiza 
mediante la url
"https://tienda.consum.es/es/s/'producto_a_buscar'" siendo 
'producto_a_buscar' lo que necesitas buscar en el supermercado.
2. En esta plataforma los espacios los tenemos que escapar por %20.
3. Recuerda ir a la web para encontrar las etiquetas, clases o id que 
podemos utilizar para realizar la lectura de los productos y su precio.
import requests
from bs4 import BeautifulSoup
busqueda = 'cerveza turia'
web = requests.get('https://tienda.consum.es/es/s/+busqueda.replace(" ","%
20"))
soup = BeautifulSoup(web.text,"lxml")
Ejercicio 1. Realiza un recorrido por todos los artículos de este supermercado.
PROGRAMACIÓN CON PYTHON
Existen plataformas que tienen una protección para que no podamos realizar 
web scraping, pero existe una alternativa para emular que somos un navegador.
# Ejecutar para poder acceder a webs que tienen protección y necesitan emular un navegador
# Cada 12 horas en colab se pierde la instalación de este driver
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
Realiza la búsqueda de los productos de Carrefour mediante web scraping:
1. Recuerda que en la url de Carrefour, la búsqueda de productos se realiza 
mediante la url por Get mediante la variable 
q,"https://www.carrefour.es/?q='producto_a_buscar'" siendo 
'producto_a_buscar' lo que necesitas buscar en el supermercado.
2. En esta plataforma los espacios los tenemos que escapar por +.
3. Recuerda ir a la web para encontrar las etiquetas, clases o id que 
podemos utilizar para realizar la lectura de los productos y su precio.
Como Carrefour tiene una protección debemos utilizar la emulación del 
navegador.
from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=options)
busqueda = 'cerveza turia'
wd.get("https://www.carrefour.es/?q="+busqueda.replace(" ","+"))
Ejercicio 2. Realiza un recorrido por todos los artículos de este supermercado, 
imprime el título de la página.
Estamos interesados en ver la relación de precios entre un supermercado y otro 
de este producto:
busqueda = 'chocolate milka'
Utilizaremos esta función para encontrar la similitud entre la descripción de un 
artículo y otro:
from difflib import SequenceMatcher
def similar(a, b):
 return SequenceMatcher(None, a, b).ratio()
Ejercicio 3. Utilizando los resultados de los ejercicios anteriores, compara los 
dos listados de artículos y almacena en un diccionario todos los productos 
referenciados a cada supermercado, almacenando en un mismo índice los 
PROGRAMACIÓN CON PYTHON
productos que sean similares en un 66%. Aunque no tengan similar en un 
supermercado agrégalos también al diccionario.
Es recomendable almacenar el porcentaje de la similitud en el diccionario.
Muestra el diccionario en pantalla.
Ejemplo de resultado del diccionario:
{'consum': {'Chocolate con Leche 270 Gr': '1,85 €'}, 'carrefour': {'Chocolate con 
leche Milka 270 g.': '2,10 €'}, 'porcentaje': 0.7931034482758621}
{'consum': {'-': '-'}, 'carrefour': {'Galletas con chocolate Choco Biscuits Milka 150 
g.': '1,91 €'}}
{'consum': {'Chocolate Triple 90 Gr': '1,29 €'}, 'carrefour': {'-': '-'}



## Authors

-[@sagader](https://github.com/maryrrr)


## Installation

download python

python3 -m venv 

!pip install selenium

!apt-get update # to update ubuntu to correctly run apt install

!apt install chromium-chromedriver



