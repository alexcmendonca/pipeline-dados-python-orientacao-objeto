# Pipeline de dados: combinando Python e Orientação a Objeto

## 💡Objetivos
Repositório dedicado a contribuir para o desenvolvimento de um Pipeline de Dados abrangendo as fases de ETL (Extração, Transformação e Carregamento de Dados). Este pipeline é projetado para oferecer flexibilidade e facilidade de reutilização em diversas situações.

## 🖥️Desafios do Projeto
Duas empresas recentemente se uniram, cada uma com suas próprias bases de dados, apresentando origens e estruturas distintas. No âmbito do nosso time de engenharia de dados, a responsabilidade recai sobre a integração dessas duas fontes de dados, realizando as transformações necessárias e estabelecendo um pipeline robusto. Esse pipeline visa garantir a reprodução eficiente do processo nos meses subsequentes, quando a demanda por essa integração ressurgir.

O objetivo final é disponibilizar esses dados consolidados para a equipe de Business Intelligence (BI), capacitando-os a criar relatórios detalhados, extrair insights valiosos e compreender os resultados decorrentes dessa fusão empresarial. Essas análises buscará responder questões cruciais, se as vendas aumentaram, diminuíram ou se concentraram predominantemente na empresa A ou B.

## 📄Atividades Realizadas
|Atividades|Realizadas |
|----------|-----------|
|Estruturar um projeto de engenharia de dados|Mudar o comportamento do método get do tipo dicionário|
|Comandos Linux de criação de pastas|Utilizar o for e o get para construir uma nova estrutura de lista de listas|
|Baixar dados utilizando wget|Salvar os dados com writer do pacote csv|
|Leitura de dados com o comando open|Sair da etapa de exploração para a etapa de criação de um pipeline|
|Biblioteca csv e json para leitura eficiente dos dados|Refatorar código criando funções para a extração, transformação e carregamento|
|Escolher uma estrutura para armazenar seus dados|Gerar um relatório do pipeline informando os dados lidos e gerados|
|Utilizar as funções DictReader e readlines|Identificar as etapas do pipeline ETL no código|
|Utilizar o método keys, get e items do tipo dicionário|Identificar a necessidade de aplicar o paradigma orientação a objeto|
|Alinhar decisões com o cliente|Transformar um pipeline de dados de funções para uma classe|
|Combinar o for com as funções do dicionário renomear as colunas|Criar os atributos e métodos da classe Dados|
|Utilizando o método extend do tipo lista para juntar nossos dados|Refatorar código para novas necessidades|
|Salvando os dados com DictWriter|Utilizar um pipeline de Dados em script|

##  🗂️Estrutura de Pastas
- data_raw: Diretório que contém os dados no formato bruto, antes de qualquer processamento.
- data_processed: Armazenamento dedicado aos dados após passarem por transformações e análises, representando a versão trabalhada e refinada.
- notebook: Pasta destinada aos arquivos Jupyter Notebook, nos quais são realizadas análises e explorações aprofundadas dos dados.
- scripts: Espaço designado para os scripts em Python, encapsulando o código utilizado no processo de manipulação e transformação dos dados.

## 🔍Referências
- [Alura](https://www.alura.com.br/)