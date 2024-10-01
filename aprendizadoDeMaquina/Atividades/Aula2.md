# Tema: Tabela verdade

Esta atividade de apredizado de maquina foi nossa introdução pratica a tabela verdade.

## Questões apresentadas:

1. Em uma festa, se Ana está dançando, então João está sorrindo. Construa a tabela verdade para esta afirmação e classifique-a como tautologia, contingência ou contradição.

| P | Q | P → Q  |
|---|---|--------|
| V | V | V      |
| V | F | F      |
| F | V | V      |
| F | F | V      |

**Contigência**: pois apresenta valores verdadeiro e valores falsos.

2. Se estiver chovendo e eu não trouxer um guarda-chuva, então vou ficar molhado. Construa a tabela verdade para esta afirmação e classifique-a como tautologia, contingência ou contradição.

| P | Q | R | ¬Q | P ∧ ¬Q | () → R|
|---|---|---|----|--------|-------|
| V | V | V | F  | F      | V     |
| V | V | F | F  | F      | V     |
| V | F | V | F  | V      | V     |
| V | F | F | F  | V      | F     |
| F | V | V | V  | F      | V     |
| F | V | F | V  | F      | V     |
| F | F | V | V  | F      | V     |
| F | F | F | V  | F      | V     |

**Contigência**: pois apresenta valores verdadeiro e valores falsos.

3. Em um jogo de cartas, se Maria vencer, então ou João perde ou Carlos empata. Construa a tabela verdade para esta afirmação e classifique-a como tautologia, contingência ou contradição.

| P   | Q   | R   | (Q ∨ R) | P → ()    |
| --- | --- | --- | ------- | --------- |
| V   | V   | V   | V       | V         |
| V   | V   | F   | V       | V         |
| V   | F   | V   | V       | V         |
| V   | F   | F   | F       | F         |
| F   | V   | V   | V       | V         |
| F   | V   | F   | V       | V         |
| F   | F   | V   | V       | V         |
| F   | F   | F   | F       | V         |

**Contigência**: pois apresenta valores verdadeiro e valores falsos.

### Tabela usa como referencia:

| Conector    | Símbolo | Descrição                                                           | Exemplo            | Resultado                                                        |
|-------------|---------|---------------------------------------------------------------------|--------------------|------------------------------------------------------------------|
| Negação     | ¬       | Inverte o valor de verdade da proposição.                           | ¬P (não P)         | Se P for V, então ¬P será F.                                     |
| Conjunção   | ∧       | Verdadeira se ambas as proposições forem verdadeiras.               | P ∧ Q (P e Q)      | Se P e Q forem V, então P ∧ Q será V.                            |
| Disjunção   | ∨       | Verdadeira se pelo menos uma das proposições for verdadeira.        | P ∨ Q (P ou Q)     | Se P ou Q forem V, então P ∨ Q será V.                           |
| Implicação  | →       | Verdadeira se a primeira proposição for falsa ou se ambas forem V.  | P → Q (se P então Q)| Se P for F ou se P e Q forem V, então P → Q será V.             |
| Equivalência| ↔       | Verdadeira se ambas as proposições forem verdadeiras ou falsas.     | P ↔ Q (P sse Q)    | Se P e Q forem V ou se P e Q forem F, então P ↔ Q será V.        |

### Referencias

1. [Tabela de referencias](https://sponge-dryosaurus-50f.notion.site/Aula-1-Introdu-o-Intelig-ncia-Artificial-e-Tabela-Verdade-07-08-2024-eb9d71bfdbc14aec92c47637dd2bf72a)
