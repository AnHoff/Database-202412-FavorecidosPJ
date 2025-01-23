# Database-202412-FavorecidosPJ

Base de dados MySQL criada com base nos dados de PJs Favorecidos (dez/2024) do Portal da Transparência. Esse repositório tem como objetivo montar um banco de dados didático que se enquadre nas exigências da disciplina Sistemas de Bancos de Dados 2 da Faculdade de Ciências e Tecnologias em Engenharias da Universidade de Brasília.

## Criação da Base de Dados

Para montar a base de dados **202412_FavorecidosPJ** em sua máquina, será necessário acessar o [Portal da Transparência](https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj) e realizar o download dos arquivos em formato `.csv` referentes a dezembro de 2024. É importante ressaltar que arquivos de outros meses ou anos podem ter formatação diferente e não serem compatíveis com o banco modelado nesse repositório.

A modelagem do banco foi elaborada a partir do cruzamento dos dados dos 3 arquivos `.csv` baixados e os diagramas DE-R (Diagrama Entidade-Relacionamento) e DLD (Diagrama Lógico de Dados) se encontram na pasta [Diagrams](./Diagrams). A modelagem atual é passível de evolução e serve como exercício para praticar a normalização de bases de dados. A pasta mencionada possui arquivos de modelagem editáveis por meio do brModelo3.

De modelagem simples, a base 202412_FavorecidosPJ se classifica como de fácil entendimento, mas possui complexidade suficiente para realizar consultas avançadas, criar de índices e praticar *tunning*, por exemplo.

### Scripts de Criação

A pasta [Scripts](./Scripts) possui arquivos .sql responsáveis pela criação do banco de dados. Para executá-los, é necessário ter instalado em sua máquina o MySQL Workbench ou similar. Execute primeiro o scriptFisico.sql, pois ele contém a estrutura do banco de dados. Em seguida, execute o arquivo popula.sql.

**Como criar o popula.sql?**

O arquivo CreateInserts.py atua na geração dos inserts necessários para popular o banco.

Para utilizá-lo, coloque os arquivos baixados do [Portal da Transparência](https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj) e coloque o caminho para cada um deles no script CreateInserts.py. Rode o script. Ao final, será gerado o script popula.sql, na pasta [Scripts](./Scripts/). Execute o arquivo gerado no MySQL Workbench ou similar.

O arquivo pode levar algum tempo para ser gerado. Os dados são analisados no CreateInserts.py, de forma a retirar tuplas incompletas. Isso servirá como prática para consultas e execução de scripts em SQL.