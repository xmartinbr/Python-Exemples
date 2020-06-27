from bs4 import BeautifulSoup
import requests

url = input("Escribe el sitio web: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('img',class_="attachment-home-post wp-post-image"):
    print(link.get('width'))
