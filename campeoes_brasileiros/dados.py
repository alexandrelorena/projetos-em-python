"""
Dados dos campeões Brasileiros
"""

import http.client
import json

# Configurações da solicitação
url = "www.sportsopendata.net"
endpoint = "/api/v1/soccer/championship/1/champions"

# Inicializa a conexão
conn = http.client.HTTPSConnection(url)

# Realiza a solicitação GET
conn.request("GET", endpoint)

# Obtém a resposta
response = conn.getresponse()

if response.status == 200:
    data = json.loads(response.read().decode('utf-8'))
    for champion in data:
        print(f"Ano: {champion['season']}, Campeão: {champion['champion']['name']}")
else:
    print("Erro ao acessar a API")

# Fecha a conexão
conn.close()

