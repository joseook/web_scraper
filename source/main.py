# main.py

import csv
import logging
from scraper import raspar_paginas
from logger import logging  # Importa a configuração de logging

def main(num_paginas=10, nome_arquivo='livros.csv'):
    dados_totais = raspar_paginas(num_paginas)
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        campos = ['Título', 'Preço', 'Disponibilidade', 'Classificação']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for livro in dados_totais:
            writer.writerow(livro)
    
    logging.info(f'{len(dados_totais)} livros foram raspados e salvos em "{nome_arquivo}".')

if __name__ == '__main__':
    num_paginas = int(input("Digite o número de páginas para raspar (padrão é 10): ") or "10")
    nome_arquivo = input("Digite o nome do arquivo de saída (padrão é 'livros.csv'): ") or "livros.csv"
    main(num_paginas, nome_arquivo)
