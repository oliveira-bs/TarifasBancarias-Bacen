### Pipeline de Tarifas bancárias

Esse projeto visa criar um *database* de tarifas bancárias de todas as instituições financeiras vigentes no país. Os dados são extraídos diretamente via API do [Banco Central do Brasil](https://dadosabertos.bcb.gov.br/dataset/tarifas-bancarias-por-segmento-e-por-instituicao)(BCB). Além disso, o **database** final conta com as informações da ouvidoria específica de cada Instituição Financeira.

O nosso pipeline é orquestrado pelo **Apache Airflow** em conjunto com o sistema gerenciador de banco de dados objeto relacional **Postgresql**. A dag presente nesse projeto aprtesenta operadores tanto na linguagem **python** quanto na linguagem **sql** para executar as suas operações.

O pipeline consiste em extrair os dados presentes nas APIs do Banco Central do Brasil, realizar as transformações necessárias nas informações fornecidas, realizar a correlação entre os campos devidos nos dados extraídos e armazenar esses dados tanto no **datalake** no formato json *(diretório local ./raw/tales)* quanto em tables via **Postgresql**.

![Screenshot from 2023-04-12 00-39-27](https://user-images.githubusercontent.com/68130436/231344724-5424cd80-fff9-46f7-8313-d32241311774.png)


Posteriormente, esses dados finais podem contribuir para analisar as taxas cobradas pelas Instituições Bancárias no país atualmente e verificar qual instituição é mais indicada para um determinado perfil de cliente.
