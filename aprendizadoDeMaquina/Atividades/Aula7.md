# Tema: PNL "Programação de linguagem natural"

PNL "Programação de linguagem natural" é ultilizada para intrepretação de linguagens convencionais "Humanas" como ingles, espanhol e portugues para linguagem intrepretavel para maquinas, a PNL apresenta 5 principais pilares sendo eles;

1. Pré-processamento de texto: O texto é normalmente pré-processado para remover ruídos, como pontuação, stopwords (palavras comuns que não contribuem muito para o significado do texto), e realizar tokenização (dividir o texto em palavras ou unidades significativas).

2. Extração de características: As características relevantes do texto são extraídas. Isso pode incluir identificação de palavras-chave, entidades nomeadas, análise gramatical e semântica.

3. Modelagem de Linguagem: São usados modelos estatísticos ou de aprendizado de máquina para entender e gerar texto. Algoritmos como redes neurais recorrentes (RNNs), redes neurais convolucionais (CNNs) e transformers são comumente empregados.

4. Treinamento do Modelo: Os modelos de PNL são treinados com grandes conjuntos de dados de texto para aprender padrões e relações entre palavras e frases.

5. Avaliação e Ajuste: Os modelos são avaliados quanto à sua precisão e eficácia em tarefas específicas de PNL e, se necessário, são ajustados e refinados.

## Questões apresentadas: Faça o algoritmo de analise de sentimento de um arquivo tweets_test.txt, para treino e depois faça o arquivo tweets_treino.txt funcionar.

### Conclusão da atividade:

1. Criar um arquivo ".py" neste caso foi utilizado "main.py".

2. Logo após inciaremos o chamado da biblioteca chama "re", esta biblioteca ficara responsavel pelo regex.

3. Após este processo criamos uma função para o tratamento de dados ela ficara responsavel por remover elementos desnecessarios para o processamento do texto como caracteres especias [ @, !, %, $ ] e retornar uma lista contendo os valores tratados.

4. Dando seguimento no código criamos mais uma função para receber a lista tratada, esta segunda função tem como responsabilidade varrer duas outras lista que contém palavras negativas e positivas, e com base nos elementos dessas lista apontar se a sentença possui sentimentos positivos ou negativos.

5. Por fim fazemos uma função destinada a leitura dos elementos.

**main.py**
```
    import re

    def filtragemDeCaracteres(texto): # função responsavel pelo tratamento do texto

        texto = re.sub('[^\w\s]', '' ,texto) #filtra "[$,#,@,%,¨,&]" e similares

        # Em ambientes não controlados "cenarios comuns", usa-se uma filtragem de palavras que não afetariam o contexto do texto como Artigo 
        # No momento o foco é entender como o processo ocorre não em execultar todas as boas praticas. 
        
        #criando um lista com cada palavra do texto

        words =  texto.split()

        return words

    def validaSentimento(palavras: list): # esta função recebe um lista de palavras e verifica quais são as emoções correspondentes
        
        palavras_positivas = ["feliz","adorei" , "alegre", "ótimo", "bom","excelente","gostei","legal","amei"] 
        palavras_negativas = ["triste", "chateado", "ruim","horrível", "péssimo","odiei"]
        
        

        statusDoSentimento = 0 # Os status começam em zero para cada palavra negativa ele regride 1 e para cada palavra positiva é agregado 1

        for palavra in palavras:
            
            if palavra in palavras_positivas:
                statusDoSentimento  += 1
            
            elif palavra in palavras_negativas:
                statusDoSentimento -= 1

        if statusDoSentimento > 0:
            return "Positivo"
        else:
            return "Negativo"


    def starTraining():
        with open("tweets_test.txt", "r") as f:
        
            for linha in f:
                texto = linha.strip()
                textoFiltrado = filtragemDeCaracteres(texto)
                classificacao = validaSentimento(textoFiltrado)
                print(f"{texto}: {classificacao}")

    starTraining()

```

### Arquivo usado na leitura dos dados.

**tweets_test.txt**
```
    O atendimento ao cliente é excelente!
    Esse produto é terrível.
    Não recomendo.
    Café é bom.
    O filme é legal mas, com pipoca é melhor ainda.
```

Com isso terminamos a primeira requisição da atividade, e podemos dar seguimento a segunda etapa "para treino e depois faça o arquivo tweets_treino.txt funciona"


1. Começamos esta etapa criando outro arquivo para manter a organização do projeto, arquivo chamado de "treino.py"

2. Novamente importamos a biblioteca "re"

3. Criamos uma função de pré-processamento para filtrar caracteres indesejáveis

4. Nesta etapa utilizamos uma função de extrair recursos que recebe uma palavra, vasculha em duas listas de palavras positivas e negativas caso seja, encontrada altera uma variavel responsavel pela positividade subtraindo ou adicionando pontos conforme os pontos podemos definir se uma frase é positiva ou não por meio do limiar.

5. Por fim fazemos a chamada do texto que vai ser usado como material de treino e submentemos aos processos descritos acima.


**treino.py**
```
    import re

    def pre_processamento(texto):
        texto = texto.lower()
        texto = re.sub(r'[^\w\s]', '', texto)  # Remover caracteres especiais
        palavras = texto.split()
        palavras = [palavra for palavra in palavras if palavra not in stop_words]  # Remover stop words (opcional)
        return palavras

    def extrair_recursos(palavras):
        palavras_positivas = ["feliz","adorei" , "alegre", "ótimo", "bom","excelente","gostei","legal","amei"] 
        palavras_negativas = ["triste", "chateado", "ruim","horrível", "péssimo","odiei"]

        pontuacao = 0
        for palavra in palavras:
            if palavra in palavras_positivas:
                pontuacao += 1
            elif palavra in palavras_negativas:
                pontuacao -= 1
        return pontuacao

    def classificar(texto):
        palavras = pre_processamento(texto)
        pontuacao = extrair_recursos(palavras)
        if pontuacao > limiar:
            return "Positivo"
        else:
            return "Negativo"

    stop_words = ["a", "o", "e", "que", "de", "em", "para", "um", "uma", "dos", "das", "com", "se", "me", "te", "se", "na", "no", "pelo", "pela", "dos", "das", "até", "mais", "muito", "bem", "pois", "quando", "onde"]

    frequencias = {}  # Dicionário para armazenar a frequência de cada palavra

    with open("tweets_treino.txt", "r") as f:
        for linha in f:
            texto, sentimento = linha.strip().split(",")
            palavras = pre_processamento(texto)
            for palavra in palavras:
                if palavra not in frequencias:
                    frequencias[palavra] = 0
                frequencias[palavra] += 1

    limiar = 0  # Ajuste conforme necessário

    with open("tweets_test.txt", "r") as f:
        for linha in f:
            texto = linha.strip()
            classificacao = classificar(texto)
            print(f"{texto}: {classificacao}")
```


### Arquivo usado na leitura dos dados.

**tweets_treino.txt**
```
    Este é um ótimo produto.,Positivo
    Não gostei do serviço.,Negativo
    Eu amo esse filme!,Positivo
```

#### Observações.

- O sistema foi realizado na versão 3.12.1
- Os arquivos foram postos todos na mesma pasta como no exemplo abaixo:
    - raiz_do_codigo
        - main.py
        - treino.py
        - tweets_test.txt
        - tweets_treino.txt
