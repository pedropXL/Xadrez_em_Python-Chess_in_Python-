# **Jogo de Xadrez em Python**
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Static Badge](https://img.shields.io/badge/LinkedIn-www.linkedin.com%2Fin%2Fpedropedrazzi-blue)
![Static Badge](https://img.shields.io/badge/License-MIT%20License-red)
![Static Badge](https://img.shields.io/badge/Portugu%C3%AAs%20-%20BR%20-%20green?style=plastic&labelColor=blue)

---
### **Clique no badger para acessar o texto em Inglês:** [![Static Badge](https://img.shields.io/badge/English%20-%20US%20-%20black?style=plastic&labelColor=yellow)](README.en.md)

---

## **Visão geral**

Este é um jogo de xadrez desenvolvido em Python usando a biblioteca Pygame. O jogo apresenta um tabuleiro de xadrez totalmente funcional com todas as peças de xadrez padrão, incluindo peões, torres, cavalos, bispos, rainhas e reis. Os jogadores podem mover as suas peças à vez, e o jogo inclui funcionalidades como capturar peças, verificar o rei e declarar um vencedor quando um rei é verificado. O jogador também pode jogar contra o computador.

---

## **Tabela de Conteúdos**

- [Caraterísticas](#caraterísticas)
- [Requisitos](#requisitos)
- [Como instalar as bibliotecas de requisitos](#como-instalar-as-bibliotecas-de-requisitos)
- [Recomendações](#recomendações)
- [Instalação](#instalação)
- [Como jogar](#comojogar)
- [Personalização](#personalização)
- [Áudio](#áudio)
- [Idioma](#idioma)
- [Estrutura do código](#estrutura-do-código)
- [Funções-chave](#funções-chave)
- [Imagem e Áudio](#imagem-e-audio)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contacto e feedback](#contacto-e-feedback)
---

## **Caraterísticas**
- Modo de um jogador**: Joga contra o computador.
- Modo de dois jogadores**: Joga contra um amigo na mesma máquina.
- Tabuleiro personalizável**: Escolha entre diferentes temas e cores de tabuleiro.
- Feedback de áudio**: Efeitos sonoros para movimentos de peças, capturas e fim de jogo.
- Desativar áudio**: É possível desativar o áudio se quiser.
- Suporte a idiomas**: Disponível em inglês, português e espanhol.
- Desfazer jogada**: Opção para desfazer o último movimento (limitado a um desfazer por turno).
- Deteção de Game Over**: Detecta automaticamente o xeque-mate e declara o vencedor.

---

## **Requisitos**
- Python 3.x
- Biblioteca Pygame: Para fornecer a estrutura para construir o jogo.
- Biblioteca PIL (Pillow): Para processamento e redimensionamento de imagens.
- biblioteca soundfile: Para lidar com ficheiros áudio.

---

## **Como instalar as bibliotecas de requisitos**

- Pygame: `pip install pygame`
- Pillow: `pip install pillow`
- Soudfile: `pip install soundfile`

- Ou simplesmente digite: `pip install pygame pillow soundfile`

---

## **Recomendações**

- Criar um Ambiente Virtual para baixar as bibliotecas.

---

## **Instalação**
1. **Clone o repositório**:
   
   Digite: `git clone https://github.com/pedropXL/Xadrez_em_Python-Chess_in_Python-.git`

2. **Acessar o repositório clonado**:
    Digite: `cd Xadrez_em_Python-Chess_in_Python-`

---

## **Como jogar**

- Controlos do rato: Use o mouse para clicar nos botões, selecionar e mover as peças.
- Baseado em turnos: Os jogadores movem as suas peças à vez. As brancas movem-se sempre primeiro.
- Capturar peças: Mova a sua peça para uma casa ocupada por uma peça do adversário para a capturar.
- Anular a jogada: Para anular a jogada, clique em Anular no lado esquerdo do ecrã do jogo principal.
- Desistir: Se quiseres desistir e(ou) recomeçar o jogo basta clicares em Desistir no lado esquerdo do ecrã no jogo principal.
- Xeque-mate: O jogo termina quando o rei de um jogador está em xeque-mate.
- Reiniciar o jogo: Para reiniciar o jogo após o xeque-mate basta digitar Enter.

### **Ecrã Inicial**

![Ecrã Inicial](/README_images/Initial%20screen.png)

### **Jogo Principal**
![Jogo Principal](/README_images/Main%20game.png)
---

## **Personalização**

- Temas do tabuleiro: Personaliza o aspeto do tabuleiro selecionando diferentes temas na área Personalizar.

---

## **Audio**

- Áudio: Ativar ou desativar efeitos sonoros no menu de definições.

---

## **Língua**

- Idioma: Altera o idioma do jogo no menu de definições, podes escolher entre inglês, português e espanhol.

---

## **Estrutura do código**

O código está dividido em várias secções:

- Inicialização: Configura o ambiente do Pygame, carrega os assets e inicializa as variáveis do jogo.
- Lógica do jogo: Lida com movimentos de peças, capturas e estado do jogo (xeque, xeque-mate, etc.).
- Renderização da interface do usuário: Desenha o tabuleiro, as peças e os elementos da interface do usuário, como o menu e as configurações.
- Tratamento de eventos: Processa as entradas do utilizador (cliques do rato, premir teclas) para controlar o jogo.

---

## **Funções chave**

- draw_board(): Renderiza o tabuleiro de xadrez e as peças.
- check_options(): Determina os movimentos válidos para cada peça.
- draw_valid(): Destaca os movimentos válidos para a peça selecionada.
- draw_captured(): Mostra as peças capturadas no lado do tabuleiro.
- draw_game_over(): Mostra o ecrã de fim de jogo quando um jogador ganha.

---

## **Imagem e Áudio**

- Imagens: Todas as imagens das peças de xadrez são guardadas no diretório assets/images.
- Áudio: Os efeitos sonoros são armazenados no diretório audio.

---

## **Contribuição**

As contribuições são bem-vindas! Se quiseres contribuir, por favor bifurca o repositório e submete um pull request com as tuas alterações. Sinta-se livre para melhorar o projeto, tornar o código mais eficiente, corrigir possíveis bugs e adicionar mais funcionalidades.

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Veja o ficheiro LICENSE para mais detalhes.

---

## **Links**

- [Linkedin](www.linkedin.com/in/pedropedrazzi)
- [Github](https://github.com/pedropXL)

## **Contacto e Feedback**

Para quaisquer questões ou feedback, por favor abra um problema no GitHub ou contacte o responsável pelo projeto.

Email para contacto: pedroppedrazzi@gmail.com

---