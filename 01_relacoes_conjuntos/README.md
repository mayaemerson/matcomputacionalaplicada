# Teoria dos Conjuntos (Set Theory) - Relações entre Conjuntos

Este módulo aborda os fundamentos da Teoria dos Conjuntos e as relações entre eles, conceitos matemáticos essenciais que estruturam a lógica digital, bancos de dados e coleções na programação.

## Conceitos Teóricos Básicos

Um conjunto é uma coleção de elementos distintos. As relações e operações fundamentais entre conjuntos são:

* **Pertinência ($\in$):** Relação entre um elemento e um conjunto. Ex: $x \in A$ ($x$ pertence a $A$).
* **Subconjunto / Inclusão ($\subseteq$):** Relação entre dois conjuntos. $A \subseteq B$ se todo elemento de $A$ também é elemento de $B$.
* **União ($A \cup B$):** Conjunto contendo todos os elementos que estão em $A$ ou em $B$.
* **Interseção ($A \cap B$):** Conjunto contendo apenas os elementos que pertencem simultaneamente a $A$ e $B$.
* **Diferença ($A \setminus B$ ou $A - B$):** Conjunto de elementos que pertencem a $A$, mas não pertencem a $B$.
* **Conjunto das Partes ($\mathcal{P}(A)$):** O conjunto de todos os subconjuntos possíveis de $A$.

## Estudo de Caso: Modelagem de Permissões de Acesso em Sistemas Computacionais

### Contextualização do Problema
Em sistemas computacionais, a segurança e o controle de acesso são gerenciados por meio da atribuição de permissões específicas a usuários. Suponha um sistema que possui um conjunto finito $U$ de usuários e um conjunto $R$ de recursos digitais (como arquivos, serviços ou dispositivos). O objetivo é modelar as permissões de acesso de forma rigorosa utilizando Teoria dos Conjuntos e Funções.

* **Conjunto U:** $U = \{u_1, u_2, u_3, \dots, u_n\}$ representa os usuários cadastrados.
* **Conjunto R:** $R = \{r_1, r_2, r_3, \dots, r_m\}$ representa os recursos disponíveis.
* **Conjunto P:** Conjunto das permissões, que relaciona usuários a recursos.

---

### Análise Matemática Formal

#### 1. Relação de Permissões ($P$)
Matematicamente, as permissões de acesso no sistema representam uma **relação binária** de $U$ para $R$. Essa relação é um subconjunto do produto cartesiano de usuários por recursos:
$$P \subseteq U \times R$$

Se um par ordenado $(u_i, r_j) \in P$, dizemos que o usuário $u_i$ possui permissão ativa para acessar o recurso $r_j$. Se $(u_i, r_j) \notin P$, o acesso é bloqueado.

#### 2. Função de Mapeamento de Recursos Autorizados ($f$)
Podemos descrever o acesso aos recursos através de uma função matemática $f$ que mapeia cada usuário para o conjunto de seus recursos autorizados. O contradomínio desta função é o **Conjunto das Partes** de $R$ (indicado por $\mathcal{P}(R)$), que engloba todas as combinações possíveis de recursos do sistema:
$$f: U \rightarrow \mathcal{P}(R)$$

Onde para cada usuário $u \in U$, a função é definida como:
$$f(u) = \{r \in R \mid (u, r) \in P\}$$

#### 3. Relações Dinâmicas (Mutabilidade de Estado)
Em um sistema de produção, as permissões variam ao longo do tempo. Matematicamente, a concessão e revogação de acessos são operações de conjuntos sobre a relação $P$:
* **Conceder acesso** de $u_i$ a $r_j$ é uma operação de união:
  $$P_{\text{novo}} = P \cup \{(u_i, r_j)\}$$
* **Revogar acesso** de $u_i$ a $r_j$ é uma operação de diferença:
  $$P_{\text{novo}} = P \setminus \{(u_i, r_j)\}$$

---

## Como Executar o Código deste Módulo

Para rodar a simulação e testar as relações dinâmicas de permissão utilizando o ambiente virtual (`.venv`), execute o seguinte comando na raiz do projeto:

```bash
.venv/bin/python 01_relacoes_conjuntos/app.py
```
