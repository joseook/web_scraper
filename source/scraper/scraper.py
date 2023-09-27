# scraper.py

import requests
from bs4 import BeautifulSoup
import time
import logging
import random
from config import BASE_URL, USER_AGENTS

def extrair_dados_da_pagina(soup):
    livros = soup.find_all('article', class_='product_pod')
    dados = []
    
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        disponibilidade = livro.find('p', class_='availability').text.strip()
        categoria = livro.find('p', class_='star-rating')['class'][1]
        
        dados.append({
            'Título': titulo,
            'Preço': preco,
            'Disponibilidade': disponibilidade,
            'Classificação': categoria
        })
    
    return dados

def raspar_paginas(num_paginas=10):
    dados_totais = []
    
    for i in range(1, num_paginas + 1):
        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }
        
        url = BASE_URL.format(i)
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            dados_pagina = extrair_dados_da_pagina(soup)
            dados_totais.extend(dados_pagina)
            
            logging.info(f"Página {i} raspada com sucesso!")
            time.sleep(random.uniform(1, 3))  # Espera entre 1 a 3 segundos antes da próxima requisição
        except requests.RequestException as e:
            logging.error(f"Erro ao raspar a página {i}: {e}")
    
    return dados_totais
