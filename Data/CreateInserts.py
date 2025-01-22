import pandas as pd
# import csv

file_path = r'202412_CNPJ.csv'

# with open(file_path, 'r', encoding='latin1') as file:
#     reader = csv.reader(file)
#     for i, row in enumerate(reader, start=1):
#         if len(row) != 4:  # Substitua "4" pelo número esperado de colunas
#             print(f"Problema na linha {i}: {row}")

try:
    data = pd.read_csv(file_path, encoding='latin1', delimiter=';', quotechar='"')
    for _, row in data.iterrows():
        print(row)
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

# try:
#     data = pd.read_csv(file_path, encoding='latin1', delimiter=',')
# except Exception as e:
#     print(f"Erro ao ler o arquivo: {e}")


# Gerar os comandos INSERT
table_name = "CNPJ"
sql_inserts = []

for _, row in data.iterrows():
    values = "', '".join(map(str, row.values))
    sql = f"INSERT INTO {table_name} VALUES ('{values}');"
    sql_inserts.append(sql)

# Salvar os comandos em um arquivo
with open('inserts.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_inserts))
