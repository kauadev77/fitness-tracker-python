# Rastreador de Exercícios em Python

Um programa de linha de comando desenvolvido em Python para rastrear exercícios físicos, gerenciar calorias queimadas, calcular IMC e fornecer relatórios e motivação. Ideal para quem deseja monitorar sua rotina de treinos.

## Sobre o Projeto

Este projeto foi desenvolvido como parte do 1º semestre do curso de Ciência da Computação da Universidade Presbiteriana Mackenzie (Mackenzie). Foi criado em colaboração com o colega Luiz Augusto.

1. **Uso**:

   - Escolha uma opção no menu para:
     - **1**: Cadastrar um novo exercício.
     - **2**: Gerar um relatório diário.
     - **3**: Verificar a meta semanal de calorias.
     - **4**: Calcular o IMC.
     - **5**: Receber uma frase motivacional.
     - **6**: Ver a média de calorias queimadas.
     - **7**: Visualizar um gráfico de calorias queimadas.
     - **8**: Sair do programa.

## Funcionalidades

- **Cadastro de Exercícios**: Registre exercícios com nome, tempo gasto, calorias queimadas e dia da semana.
- **Relatório Diário**: Liste exercícios realizados em um dia específico, com total de tempo e calorias.
- **Meta Semanal**: Defina e verifique se a meta de calorias queimadas na semana foi atingida.
- **Cálculo de IMC**: Calcule o Índice de Massa Corporal e receba uma classificação (ex.: normal, sobrepeso).
- **Frase Motivacional**: Exiba frases aleatórias para incentivar o usuário.
- **Média de Calorias**: Calcule a média de calorias queimadas por exercício.
- **Gráfico de Calorias**: Visualize um gráfico simples de barras representando calorias queimadas por exercício.
- **Validação de Entrada**: Trata entradas inválidas para evitar erros.

## Exemplo de Uso

Ao executar o programa, você verá o menu:

```
Menu:
1 - Cadastrar exercício
2 - Relatório diário
3 - Meta semanal
4 - Cálculo de imc
5 - Frase motivacional
6 - Média de calorias queimadas
7 - Gráfico de calorias queimadas
8 - Sair
```

**Exemplo de interação**:

1. Digite `1` para cadastrar um exercício:
   - Nome: "Corrida"
   - Tempo: 30 minutos
   - Calorias: 300 kcal
   - Dia: "Segunda"
2. Digite `2` e escolha "Segunda" para o relatório:

   ```
   Exercícios realizados na Segunda:
   - Corrida | 30 min | 300 kcal
   Total de tempo gasto: 30 minutos
   Total de calorias queimadas: 300 kcal
   ```
3. Digite `7` para ver o gráfico:

   ```
   Gráfico de calorias queimadas:
   |||||||||||||||||||||||||||||| Corrida: 300 cal
   ```

## Tecnologias

- **Linguagem**: Python
- **Estruturas de Dados**: Listas para armazenar dados de exercícios
- **Bibliotecas**: `random` para frases motivacionais
- **Funcionalidades**: Manipulação de entrada/saída e cálculos matemáticos

## Status do Projeto

Concluído, com funcionalidades robustas e validação de entradas. Futuras melhorias podem incluir:

- Persistência de dados em arquivo (ex.: JSON ou CSV).
- Interface gráfica com `tkinter` ou `PyQt`.
- Validações adicionais para entradas numéricas (ex.: impedir calorias negativas).

## Contribuidores

- [@kauadev77](https://github.com/kauadev77)
- [@Karrarass](https://github.com/Karrarass)
