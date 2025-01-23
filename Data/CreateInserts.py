import pandas as pd

file_paths = {
    'CNAE': r'202412_CNAE.csv',                           # Substitua pelo caminho real do arquivo CSV CNAE
    'NaturezaJuridica': r'202412_NaturezaJuridica.csv',   # Substitua pelo caminho real do arquivo CSV NaturezaJuridica
    'CNPJ': r'202412_CNPJ.csv'                            # Substitua pelo caminho real do arquivo CSV CNPJ
}

# Remover apóstrofos
def remove_apostrophes(value):
    if isinstance(value, str):
        return value.replace("'", "")
    return value

# Verificar se há valores 'nan' ou NaN
def contains_nan(row):
    return row.isnull().any() or (row == 'nan').any() or (row == '0').any() or (row == 0).any()

sql_inserts = []

# Adicionando a linha para desabilitar a verificação de chaves estrangeiras no início do script
sql_inserts.append("-- Desabilitar a verificação de chaves estrangeiras")
sql_inserts.append("SET foreign_key_checks = 0;")

for table_name, file_path in file_paths.items():
    try:
        # Definir o encoding de acordo com o arquivo
        # if table_name in ['CNAE', 'NaturezaJuridica']:
        #     encoding = 'latin1'
        # else:
        #     encoding = 'utf-8'  # Para CNPJ

        # print(f"Lendo dados da tabela {table_name} a partir de {file_path} com encoding {encoding}...")

        # data = pd.read_csv(file_path, encoding=encoding, delimiter=';', quotechar='"')
        data = pd.read_csv(file_path, encoding='latin1', delimiter=';', quotechar='"')


        print(f"{table_name}: {len(data)} linhas lidas.")
        
        if len(data) == 0:
            print(f"{table_name} não contém dados.")
            continue

        for _, row in data.iterrows():
            # Remover apóstrofos de todos os valores da linha
            row = row.apply(remove_apostrophes)
            
            # Verificar se a linha contém NaN (valores ausentes) ou 'nan'
            if contains_nan(row):
                continue  # Pula essa linha se ela contiver NaN ou 'nan'
            
            values = "', '".join(map(str, row.values))
            sql = f"INSERT INTO {table_name} VALUES ('{values}');"
            sql_inserts.append(sql)
            print(f'INSERT INTO {table_name} VALUES ({values});')

    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")

with open('Scripts/popula.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_inserts))

print("Arquivo SQL gerado com sucesso!")
