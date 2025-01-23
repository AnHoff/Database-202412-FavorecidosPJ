import pandas as pd

file_paths = {
    'CNAE': r'202412_CNAE.csv',                           # Substitua pelo caminho real do arquivo CSV CNAE
    'NaturezaJuridica': r'202412_NaturezaJuridica.csv',   # Substitua pelo caminho real do arquivo CSV NaturezaJuridica
    'CNPJ': r'202412_CNPJ.csv'                            # Substitua pelo caminho real do arquivo CSV CNPJ
}

def remove_apostrophes(value):
    if isinstance(value, str):
        return value.replace("'", "")                       # Remove o apóstrofo
    return value

sql_inserts = []

for table_name, file_path in file_paths.items():
    try:
        data = pd.read_csv(file_path, encoding='latin1', delimiter=';', quotechar='"')
        
        for _, row in data.iterrows():
            # Remover apóstrofos de todos os valores da linha
            row = row.apply(remove_apostrophes)
            values = "', '".join(map(str, row.values))
            sql = f"INSERT INTO {table_name} VALUES ('{values}');"
            sql_inserts.append(sql)
            print(f'INSERT INTO {table_name} VALUES ({values});')

    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")

with open('Scripts/popula.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_inserts))

print("Arquivo SQL gerado com sucesso!")
