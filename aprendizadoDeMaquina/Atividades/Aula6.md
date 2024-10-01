# Tema: Regex "Expreções regulares".

A atividade anterior nos apresentou os principios de regex e esta nos deixa mais algumas atividades para por em prática o conceito. 

## Questões apresentadas:


1. Validação de Horário no formato 24 horas (HH)

- Descrição: Crie uma Regex para validar horários no formato 24 horas, onde:

    - As horas podem ir de 00 a 23.

    - Os minutos podem ir de 00 a 59.


**Exemplos**:


- Válidos:

    -   |Exemplos|
        |--------|
        |23:59 | 
        |00:00 |
        |15:30 |


- Inválidos:

    - |      Exemplos        | Motivo da invalidade    |
      |----------------------|-------------------------|
      |          24:00       |Hora inválida            |
      |          12:60       |Minuto inválido          |
      |          5:30        |falta o zero inicial nas horas|


Resposta: ^([0-1]\d|2[0-3]):[0-5]\d$
-----------------------------------------------------------------------------------------------


2. Validação de CEP (código postal brasileiro)

- Descrição: Crie uma Regex para validar um CEP no formato XXXXX-XXX, onde X é um dígito.

- Critérios:

    - Deve ter exatamente 5 dígitos, um hífen e mais 3 dígitos.


**Exemplos**:

- Válidos:

    -   |Exemplos|
        |--------|
        12345-678 | 
        98765-432|


- Inválidos:

    - |      Exemplos        | Motivo da Invalidade    |
      |----------------------|-------------------------|
      |         1234-567     |Faltando um Digito       |
      |         12345678     |Faltando o Hífen         |
      |          12-34567     |Esta fora do padrão      |


Resposta: ^\d{5}[-]\d{3}$
-----------------------------------------------------------------------------------------------


3. Validação de Número de Telefone celular

- Descrição: Crie uma Regex para validar Número de Telefone celular:

    - Ter DDD com 2 dígitos | Número telefone com 9 dígitos


**Exemplos**:

- Válidos:


    -   |   Exemplos    |
        |---------------|
        |11 95555 0000  |
        |(11) 95555-0000|
        | 09 91111-1556 |

- Inválidos:

      
    - |      Exemplos        | Motivo da Invalidade    |
      |----------------------|-------------------------|
      |   11 8888-888        | Está faltando um digito |      
      |   11 10000-00000     | Possui Digitos a mais   |
      |   9 10000-1000       |  Falta um número do dd  |


Resposta: ^[(]?\d{2}[)]?\s?[9]\d{4}[ -]?\d{4}$ ou ([(]\d{2}[)]|\d{2})\s?[9]\d{4}[ -]?\d{4}$
-----------------------------------------------------------------------------------------------

4. Validação de URL

- Descrição: Crie uma Regex para validar URLs que comecem com http:// ou https://, seguidas por um domínio, e opcionalmente uma barra e caminho adicional.

- Critérios:
    - |Exmeplos|
      |--------|
      |https://www.google.com|
      |http://meusite.net/contato|
      |https://dominio.org/|


**Exemplos**:

- Válidos:

    -   |Exemplos|
        |--------|
        |https://www.google.com |
         http://meusite.net/contato | 
         https://dominio.org/|

- Inválidos:

    - |      Exemplos        | Motivo da invalidade    |
      |----------------------|-------------------------|
      |  www.google.com      |     Sem protócolo       |
      |http://meusite.invalid|     Dominio inválido    |
      |  https://            |     Faltando Dominio    |


Resposta: http[s]?:\/{2}(www.)?\w{1,}.(org|net|com|com.br)(.br)?[\/]?(\w{1,})?
-----------------------------------------------------------------------------------------------
