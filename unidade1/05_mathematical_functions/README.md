# Funções Matemáticas (Mathematical Functions) - Foco em Crescimento Exponencial

Este módulo aborda os fundamentos de funções matemáticas e sua aplicação prática no desenvolvimento de software, com ênfase especial no estudo de **Função Exponencial e Crescimento Exponencial**.

## Conceitos Teóricos Básicos
Uma função matemática é uma relação entre um conjunto de entradas (Domínio) e um conjunto de saídas potenciais (Contradomínio), de forma que cada entrada está associada a exatamente uma saída (Imagem).

* **Domínio (Domain):** O conjunto de todos os valores de entrada possíveis.
* **Contradomínio (Codomain):** O conjunto de todos os valores que podem potencialmente sair da função.
* **Imagem (Image):** O conjunto dos valores de saída que realmente ocorrem.

### Função Exponencial e Crescimento Exponencial
Uma função exponencial é uma função da forma:
$$f(x) = a \cdot b^x$$
Onde:
* $a$ é o valor inicial (para $x=0$).
* $b$ é a base de crescimento (taxa constante).
* $x$ é a variável independente (frequentemente representando tempo).

Se $b > 1$, a função representa um **Crescimento Exponencial**, onde o valor cresce cada vez mais rápido à medida que $x$ aumenta.

### Exemplo Prático: Crescimento Contínuo de Usuários
Um exemplo prático e recorrente em modelagem de crescimento populacional ou de usuários em sistemas é a função de crescimento exponencial contínuo:
$$U(t) = U_0 \cdot e^{k \cdot t}$$

Onde:
* $U(t)$ é o número de usuários no tempo $t$.
* $U_0$ é o número inicial de usuários.
* $k$ é a taxa de crescimento contínuo por período.
* $e$ é a base do logaritmo natural (Constante de Euler, $\approx 2,71828$).

**Estudo de Caso:**
Se uma plataforma inicia com $1.000$ usuários ($U_0 = 1000$) e cresce a uma taxa contínua de $k = 0,05$ ao mês ($5\%$), o número estimado de usuários após $12$ meses ($t = 12$) será:
$$U(12) = 1000 \cdot e^{0,05 \cdot 12} = 1000 \cdot e^{0,6} \approx 1000 \cdot 1,8221188 = 1.822 \text{ usuários}$$

---
### Representação Gráfica do Crescimento
A curva abaixo demonstra graficamente a aceleração do crescimento ao longo dos 12 meses, partindo do marco inicial de 1.000 usuários até o final de 1.822 usuários:

![Curva de Crescimento de Usuários](user_growth.png)

---

## Aplicação Real em Computação

1. **Complexidade de Algoritmos:** Algoritmos de força bruta ou recursão ineficiente (como a sequência de Fibonacci sem memorização) possuem complexidade de tempo exponencial $O(2^n)$.
2. **Criptografia:** A segurança de algoritmos como RSA e criptografia de curvas elípticas depende de funções matemáticas de sentido único (fáceis de calcular em uma direção, difíceis de reverter).
3. **Escalonamento de Infraestrutura (Growth Metrics):** Modelagem de tráfego de rede ou crescimento de base de usuários em escala viral segue padrões exponenciais.

## Como Executar o Código deste Módulo
Para rodar a simulação e gerar o gráfico deste estudo de caso utilizando o ambiente virtual (`.venv`), execute o seguinte comando na raiz do projeto:

```bash
.venv/bin/python unidade1/05_mathematical_functions/app.py
```
