# Design_Patterns

Gabriel Faria e Silva, Guilherme Canarini Kaneda

## RPG por turnos - Jogo
O jogo é uma simulação de RPG em que o jogador comanda um grupo de personagens enfrentando um inimigo poderoso, Smaug, o dragão. Abaixo está um resumo das principais mecânicas e funcionamento do jogo:

## 1. Inicialização
*Personagens do Jogador*:

O jogador controla uma party composta por três personagens:
- Knight (Cavaleiro): Alta vida, bom ataque e defesa.
- Cleric (Clérigo): Vida moderada, bom suporte com cura.
- Wizard (Mago): Ataques poderosos, mas baixa defesa.
  
Cada personagem é gerenciado por uma camada intermediária chamada UniversalCharacterBridge (*Bridge Pattern*), que fornece abstração sobre suas ações.

*Inimigo*:

O inimigo é um dragão com atributos de vida, mana, ataque e defesa.

*Histórico e Editor*:

O jogo utiliza um sistema de histórico (History) para armazenar as ações do jogador, permitindo repetir a última ação usada. (*Memento pattern*)

## 2. Fluxo de Jogo
*Objetivo*:

O jogador deve derrotar Smaug antes que todos os personagens da party sejam derrotados.

*Turnos*:

O jogo alterna entre turnos do jogador e do inimigo.
Ações do Jogador:

O jogador pode escolher entre as seguintes opções:
- Ataque: Causa dano ao inimigo.
- Cura: Restaura a vida de um ou mais personagens da party.
- Especial: Usa uma habilidade especial do personagem (gasta mana).
- Repetir Ação: Repete a última ação registrada no histórico (se válida).
  
As escolhas são armazenadas pelo sistema de histórico para permitir repetição no futuro.

*Turno do Inimigo*:

O dragão decide suas ações aleatoriamente:
- Ataque: Danifica os membros da party.
- Cura: Restaura sua própria vida.
- Especial: Usa um ataque poderoso se sua mana estiver cheia.

## 3. Condições de Vitória/Derrota
Vitória: O jogador vence se a vida do inimigo chegar a zero.

Derrota: O jogador perde se um membro da party for derrotado.

## 4. Mecânicas Especiais
*Histórico de Ações*:

Armazena as ações do jogador por meio do Editor e History, possibilitando repetir ações no futuro.

Se a última ação registrada não for válida (ex.: nenhuma ação foi registrada), o jogador é notificado.

*Mana e Habilidades Especiais*:

Tanto os personagens quanto o inimigo possuem habilidades especiais que dependem de mana acumulada.

*Sistema de Pontos de Vida e Mana*:

- Cada personagem (inclusive o inimigo) tem atributos de vida e mana que são afetados pelas ações de ataque, cura ou habilidades.

*Exemplo de Gameplay*

O jogador escolhe atacar, curar ou usar uma habilidade especial.

O inimigo responde com uma ação aleatória ou usa uma habilidade especial se tiver mana suficiente.

O ciclo continua até que uma das condições de vitória ou derrota seja atingida.

# Padrões utilizados

  - *Adapater*: na classe weapon, permitindo que todos os personagens ataquem idependentemente da implementação do ataque;
  - *Bridge*: Nas classes *CharacterBridge e UniversalCharacterBridge, a fim de separar a abstração da implementação;
  - *Composite*: a fim de representar hierarquias todo-parte;
  - *Facade*: a fim de fornecer uma interface acessiva ao usuário e à mudanças no futuro;
  - *Memento*: utilizado para guardar as ações do jogador durante a rodada.

# Como rodar
Execute a classe *main.py*.

Python 3.11 foi utilizado na produção e execução do código.
