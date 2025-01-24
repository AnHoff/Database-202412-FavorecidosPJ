# Database-202412-FavorecidosPJ

Base de dados MySQL criada com base nos dados de PJs Favorecidos (dez/2024) do Portal da Transparência. Esse repositório tem como objetivo montar um banco de dados didático que se enquadre nas exigências da disciplina Sistemas de Bancos de Dados 2 da Faculdade de Ciências e Tecnologias em Engenharias da Universidade de Brasília.

## Criação da Base de Dados

Para montar a base de dados **202412_FavorecidosPJ** em sua máquina, será necessário acessar o [Portal da Transparência](https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj) e realizar o download dos arquivos em formato `.csv` referentes a dezembro de 2024. É importante ressaltar que arquivos de outros meses ou anos podem ter formatação diferente e não serem compatíveis com o banco modelado nesse repositório.

A modelagem do banco foi elaborada a partir do cruzamento dos dados dos 3 arquivos `.csv` baixados e os diagramas DE-R (Diagrama Entidade-Relacionamento) e DLD (Diagrama Lógico de Dados) se encontram na pasta [Diagrams](./Diagrams). A modelagem atual é passível de evolução e serve como exercício para praticar a normalização de bases de dados. A pasta mencionada possui arquivos de modelagem editáveis por meio do brModelo3.

### Importante!

Caso opte por utilizar os dados do modo que vem por default pelo download dos arquivos `.csv`, encontrará uma base de dados com 3 tabelas, CNAE, NaturezaJuridica e CNPJ. Cada tabela contém, respectivamente, 1.109, 72 e 1.595.263 tuplas. O script de processamento dessas planilhas, o CreateInserts.py, formará os inserts e irá filtrar dados inválidos, reduzindo significativamente o consumo de recursos da máquina para criar e acessar o banco de dados.

De modelagem simples, a base 202412_FavorecidosPJ se classifica como de fácil entendimento, mas possui complexidade suficiente para realizar consultas avançadas, criar de índices e praticar *tunning*, por exemplo.

### Scripts de Criação

A pasta [Scripts](./Scripts) possui arquivos .sql responsáveis pela criação do banco de dados. Para executá-los, é necessário ter instalado em sua máquina o MySQL Workbench ou similar. Execute primeiro o scriptFisico.sql, pois ele contém a estrutura do banco de dados. Em seguida, execute o arquivo popula.sql.

**Como criar o popula.sql?**

O arquivo CreateInserts.py atua na geração dos inserts necessários para popular o banco.

Para utilizá-lo, coloque os arquivos baixados do [Portal da Transparência](https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj) e coloque o caminho para cada um deles no script CreateInserts.py. Rode o script. Ao final, será gerado o script popula.sql, na pasta [Scripts](./Scripts/). Execute o arquivo gerado no MySQL Workbench ou similar. Caso queira retirar os filtros e gerar o popula.sql completo, faça os ajustes necessários no código. Basta comentar as linhas referentes aos filtros.

O arquivo pode levar algum tempo para ser gerado. Os dados são analisados no CreateInserts.py, portanto, caso queira customizar a criação do popula, realize os ajustes no script Python. Tenha em mente que tais ajustes podem fazer com que o banco de dados populado não corresponda ao modelado neste repositório. Isso servirá como prática para consultas e execução de scripts em SQL.

Os inserts gerados correspondem às tuplas com dados válidos, deixando de lado tuplas com dados em branco ou inválidos. Isso foi necessário para facilitar a montagem da base de dados e otimizar a preparação e execução do arquivo popula.sql, que era extremamente custoso para a máquina.

Recomendamos o uso do script com dados filtrados para executar a base em máquinas pessoais ou de laboratórios da Universidade de Brasília, visto que seu poder de processamento costuma ser baixo e não suficiente para executar os scripts de forma fluida. Se ainda assim apresentar travamentos, recomendamos abrir o popula.sql com o Bloco de Notas ou com o Notepad++, copiar o conteúdo e colar no workbench.

Na pasta [Scripts](./Scripts/) você encontra o populaFiltrado.sql, arquivo otimizado mencionado acima. Verifique na Tabela 1 abaixo a diferença entre o script com os dados completos do Portal da Transparência e o script com dados filtrados.

<center>Tabela 1. Quantidade de Tuplas por Tabela</center>

| Tipo Popula.sql | CNAE | NaturezaJuridica | CNPJ | Tamanho popula.sql |
| --------------- | ---- | ---------------- | ---- | ------------------ |
| Dados completos | 1.109 | 72 | 1.595.263 | Aproximadamente 360mb |
| Dados filtrados | 1.109 | 72 | 296.030 | Aproximadamente 75mb |

### Dump

O dump da base de dados **filtrada** pode ser encontrado na pasta [Scripts/Dump](./Scripts/Dump).