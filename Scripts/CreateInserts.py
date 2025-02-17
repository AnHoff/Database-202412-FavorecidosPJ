import pandas as pd
import unicodedata

file_paths = {
    'CNAE': r'202412_CNAE.csv',                           # Substitua pelo caminho real do arquivo CSV CNAE
    'NaturezaJuridica': r'202412_NaturezaJuridica.csv',   # Substitua pelo caminho real do arquivo CSV NaturezaJuridica
    'CNPJ': r'202412_CNPJ.csv'                            # Substitua pelo caminho real do arquivo CSV CNPJ
}

def remove_apostrophes(value):
    if isinstance(value, str):
        return value.replace("'", "")
    return value

def remove_diacritics(value):
    if isinstance(value, str):
        return ''.join(
            c for c in unicodedata.normalize('NFKD', value) if not unicodedata.combining(c)
        )
    return value

def contains_nan(row):
    return row.isnull().any() or (row.astype(str) == 'nan').any() or (row.astype(str) == '0').any()

sql_inserts = []

sql_inserts.append("-- Desabilitar a verificação de chaves estrangeiras")
sql_inserts.append("SET foreign_key_checks = 0;")

for table_name, file_path in file_paths.items():
    try:
        data = pd.read_csv(file_path, encoding='latin1', delimiter=';', quotechar='"')

        print(f"{table_name}: {len(data)} linhas lidas.")

        if data.empty:
            print(f"{table_name} não contém dados.")
            continue

        for _, row in data.iterrows():
            row = row.apply(remove_apostrophes).apply(remove_diacritics)

            if contains_nan(row):
                continue  # Pula essa linha se ela contiver NaN ou 'nan'

            values = "', '".join(map(str, row.values))
            sql = f"INSERT INTO {table_name} VALUES ('{values}');"
            sql_inserts.append(sql)
            print(f'INSERT INTO {table_name} VALUES ({values});')

    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")

with open('Scripts/populaFiltrado.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_inserts))

print("Arquivo SQL gerado com sucesso!")
