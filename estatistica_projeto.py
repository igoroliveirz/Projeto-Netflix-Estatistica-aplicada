# -*- coding: utf-8 -*-
"""Estatistica Projeto

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BuCANfJOuUqOPCw5aoHDBInl68CE1MIJ
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_csv('netflix_titles.csv')
df.head()

print(f"Número de linhas (registros): {df.shape[0]}")
print(f"Número de colunas (variáveis): {df.shape[1]}")

print(df.columns.tolist())

variaveis_quantitativas = ['release_year']
print("Variáveis Quantitativas:", variaveis_quantitativas)

variaveis_qualitativas = ['show_id', 'type', 'title', 'director', 'cast',
                          'country', 'date_added', 'rating', 'duration',
                          'listed_in', 'description']
print("Variáveis Qualitativas:", variaveis_qualitativas)

tabela_resumo = pd.DataFrame({
    "Variável": variaveis_quantitativas + variaveis_qualitativas,
    "Tipo": ['Quantitativa'] * len(variaveis_quantitativas) +
            ['Qualitativa'] * len(variaveis_qualitativas)
})

print(tabela_resumo)