from bs4 import BeautifulSoup
import requests

url = input("Escribe el sitio web: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
