import json
import csv

from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'Nome das colunas com dados JSON:\n{dados_empresaA.nome_colunas}')
print(f'Qtde de linhas base JSON: {dados_empresaA.qtd_linhas}\n')

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'Nome das colunas com dados CSV:\n{dados_empresaB.nome_colunas}')
print(f'Qtde de linhas base CSV: {dados_empresaB.qtd_linhas}\n')

#Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f'Nome das colunas com dados CSV tranformados:\n{dados_empresaB.nome_colunas}')
print(f'Qtde de linhas base CSV: {dados_empresaB.qtd_linhas}\n')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'Nome das colunas com dados da fusão: \n{dados_fusao.nome_colunas}')
print(f'Qtde de linhas na base fusão: {dados_fusao.qtd_linhas}')

#Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)