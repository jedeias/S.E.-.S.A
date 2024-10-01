# Tema: Regex "Expreções regulares".

Regex conhecido como "expresões regulares" é uma forma de tratar os elementos de um texto.

## Questões apresentadas:

1. Validação um endereço de e-mail.

    * ^\w{2,}[@]\w{2,}[.]\w{2,3}([.]?\w{2,3}?)?$

2. Validação de uma data.

    * ^(0?[1-9]|[12][0-9]|[3][01])[\/\.][0-1]?[0-9][\/\.]\d*$

3. Validação de cpf.

    * ^\d{3}[.]?\d{3}[.]?\d{3}[.\/]?\d{2}$

## Referências:

Site para teste [REGEX101](https://regex101.com/)

Tabela de símbulos mais usados eventulmente. 

|   Símbolo   |   Descrição    |
|-------------|----------------|
|**[Elementos]**|Filtra os elementos dentro do parenteses.|
|**^Caracteres**|Filtra as palavras que iniciam com caracteres.|
|**[a-z] [0-9]**|Filtra elementos entre o primeiro elemento e o segundo elemento, seja ele numeros ou caracteres de texto.|
|**.Caracter**|Filtra um caracter selecionado e mais um antecessor há ele, seja qual for.|
|**{Valor}**|Filtra uma quantiade de elementos, especificada pelo valor.|
|**Caracter$**|Filtra elementos que terminam com este determinado caracter.|
|__a*__|O '*' pode ser utilizado antes ou depois de um caracter, em ambos os casos ele apresenta o mesmo comportamento de buscar todos os elementos na direção em que esta posicionado.|
|**\s**|Filtra todos espaços.|
|**\S**|Filtra Elementos sem espaço.|
|**\d**|Filtra caracteres númericos.|
|**\D**|Filtra todos os caractres não númericos.|
|**\w**|Filtra todos os caracteres textuais.|
|**\W**|Filtra tudo que não é um conjunto de caracteres de texto.|
