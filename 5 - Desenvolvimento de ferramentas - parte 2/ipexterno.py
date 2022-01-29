import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cit = dados['city']
pais = dados['country']
regiao = dados['region']

print('-'*20)
print(f"""IP: {ip}\nORG: {org}\nCITY: {cit}\nPAIS: {pais}\nREGIÂO: {regiao}""")
print('-'*20)