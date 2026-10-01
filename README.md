# Dashboard Executivo DATATRAN 2025

Dashboard executivo desenvolvido a partir dos dados públicos do **DATATRAN 2025**, com foco na análise de acidentes em rodovias federais brasileiras.

O projeto transforma mais de 72 mil registros em uma visão executiva e interativa, permitindo analisar volume de acidentes, gravidade, causas, localização, condições das ocorrências e impacto social estimado.

## Objetivo

O objetivo do projeto é facilitar a leitura dos dados de acidentes rodoviários e apoiar a identificação de pontos que merecem maior atenção.

O dashboard foi estruturado para responder perguntas como:

- Quantos acidentes ocorreram em 2025?
- Quantas pessoas morreram ou ficaram feridas?
- Quais estados concentram mais ocorrências?
- Onde a letalidade é maior?
- Quais causas aparecem com maior frequência?
- Quais tipos de acidente apresentam maior gravidade?
- Em quais períodos os acidentes se concentram?
- Quais fatores combinam maior frequência e maior impacto?
- Onde existem oportunidades prioritárias de atuação?

## Tecnologias utilizadas

- **HTML5** — estrutura da aplicação
- **CSS3** — identidade visual, responsividade e efeitos de interface
- **JavaScript** — filtros, cálculos, indicadores e interações
- **Chart.js** — visualizações gráficas
- **Python** — preparação e transformação da base antes da publicação
- **GitHub Pages** — publicação do dashboard

## Fonte dos dados

Os dados utilizados são provenientes do **DATATRAN**, base pública da Polícia Rodoviária Federal.

Período analisado:

**01/01/2025 a 31/12/2025**

A base utilizada no projeto contém:

- **72.529 acidentes**
- **188.346 pessoas envolvidas**
- **6.043 mortes**
- **83.550 feridos**
- **20.018 feridos graves**
- **144.922 veículos envolvidos**

## Principais indicadores

O dashboard apresenta, entre outros:

- Total de acidentes
- Total de mortes
- Total de feridos
- Total de feridos graves
- Acidentes com vítimas fatais
- Veículos envolvidos
- Mortes a cada 100 acidentes
- Percentual de acidentes fatais
- Percentual de feridos graves
- Feridos por acidente
- Veículos por acidente

## Principais análises

A página foi organizada em uma visão única e executiva, com:

- Evolução mensal dos acidentes
- Distribuição por gravidade
- Ranking de estados
- Relação entre volume de acidentes e letalidade
- Principais causas
- Tipos de acidente
- Distribuição por dia da semana
- Distribuição por horário/faixa do dia
- Condição meteorológica
- Tipo de pista
- Uso do solo
- Matriz de frequência x gravidade
- Ranking por município e rodovia
- Interpretações automáticas abaixo dos gráficos

## Filtros disponíveis

Os indicadores e gráficos podem ser filtrados por:

- Período
- UF
- Município
- BR
- Classificação do acidente
- Causa
- Tipo de acidente
- Condição meteorológica

Os filtros são combináveis e atualizam automaticamente os KPIs, gráficos, tabelas e textos interpretativos.

## Onde agir agora

O dashboard inclui um bloco executivo chamado **“Onde agir agora”**, que identifica automaticamente três focos prioritários a partir dos dados filtrados:

- causa com maior exposição econômica estimada;
- tipo de acidente com maior exposição;
- UF com maior exposição.

O objetivo desse bloco é transformar a análise em uma leitura orientada à decisão.

## Estimativa de impacto social

O DATATRAN não informa o custo financeiro individual de cada acidente.

Por isso, os valores financeiros exibidos no projeto são **estimativas de custo social**, calculadas a partir de custos médios por gravidade publicados pelo **Ipea** e atualizados monetariamente para valores de 2025.

A estimativa considera categorias como:

- acidente com vítima fatal;
- acidente com vítimas feridas;
- acidente sem vítimas.

Esses valores procuram representar impactos como perda de produção, atendimento às vítimas, danos materiais e custos institucionais.

### Importante

Os valores em reais apresentados no dashboard:

- não representam despesas efetivamente registradas no DATATRAN;
- não representam economia garantida;
- são estimativas analíticas para apoiar comparação e priorização.

O cenário de impacto potencial considera, quando indicado, uma **redução hipotética de 10% dos acidentes** no grupo analisado.

## Arquitetura do projeto

```text
datatran-dashboard-2025/
├── index.html
├── style.css
├── app.js
├── data.js
├── build_data.py
└── README.md
```

### Fluxo dos dados

```text
DATATRAN 2025
      ↓
Preparação em Python
      ↓
data.js
      ↓
JavaScript
      ↓
Filtros + KPIs + gráficos + tabelas
      ↓
Dashboard
```

A base é preparada previamente para reduzir o volume de processamento necessário durante a navegação.

Depois do carregamento, os cálculos e filtros são executados diretamente no navegador.

## Como executar localmente

1. Baixe ou clone o repositório.
2. Abra a pasta do projeto.
3. Abra o arquivo `index.html` no navegador.

Não é necessário instalar Python, banco de dados ou servidor para visualizar a versão publicada do dashboard.

> É necessária conexão com a internet caso as bibliotecas externas estejam sendo carregadas por CDN.

## Publicação

O projeto pode ser publicado gratuitamente pelo **GitHub Pages**.

Após ativar o Pages no repositório, o dashboard ficará disponível em um endereço semelhante a:

```text
https://seuusuario.github.io/datatran-dashboard-2025/
```

## Limitações da análise

Os dados permitem identificar padrões, concentrações e associações, mas não permitem concluir, por si só, relação direta de causa e efeito.

Por exemplo:

- uma causa aparecer com maior número de mortes não significa que uma única intervenção reduzirá automaticamente essas mortes;
- uma UF apresentar maior letalidade não significa que a condição das rodovias seja a única explicação;
- os dados não medem exposição ao tráfego, como quantidade de veículos circulando em cada rodovia;
- o impacto financeiro apresentado é estimado, e não observado diretamente;
- fatores externos não registrados na base podem influenciar os resultados.

Por isso, os indicadores devem ser usados como apoio para investigação e priorização, e não como prova isolada de causalidade.

## Autor

Projeto desenvolvido como parte de portfólio em **Data Analytics**, com foco em transformar dados públicos em análises visuais, indicadores executivos e informações úteis para tomada de decisão.
