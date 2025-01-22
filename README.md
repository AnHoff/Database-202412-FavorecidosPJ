# Database-202412-FavorecidosPJ
Base de dados MySQL criada com base nos dados de PJs Favorecidos (dez/2024) do Portal da Transparência.

## Criação dos Inserts

O arquivo CreateInserts.py atua na geração dos inserts necessários para popular o banco.

Para utilizá-lo, faça o download dos dados de presentes no Portal da Transparência (acesse [aqui](https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj)) e os coloque na pasta Data, onde o arquivo CreatInserts.py está localizado. Os dados utilizados para a criação desse repositório são de dezembro/2024. No script Python, deve-se alterar o nome do arquivo .csv lido para gerar os inserts correspondentes. Renomeie o arquivo gerado ("inserts.sql") para corresponder à tabela lida.