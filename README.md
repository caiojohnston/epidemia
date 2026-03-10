# Epidemia - Multi-Agent Epidemiological Intelligence Platform

> Sistema multiagente autônomo para vigilância epidemiológica do Brasil, integrando dados públicos do SUS, DATASUS e SINAN com Agentic RAG, Deep Learning e orquestração distribuída de agentes.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-0.3-green?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## O que é?

É uma plataforma de inteligência epidemiológica que transforma dados públicos em vigilância ativa de saúde. Um pesquisador ou gestor faz uma pergunta como *"qual a tendência de dengue no Pará nos últimos 3 meses e quais municípios têm risco de surto nas próximas semanas?"* e o sistema responde com análise, previsão e fontes rastreáveis, de forma completamente autônoma.

Internamente, um agente orquestrador recebe a pergunta, planeja a estratégia, aciona agentes especializados em coleta de dados epidemiológicos, análise de séries temporais, recuperação de literatura científica e geração de relatórios. O resultado é consolidado com raciocínio auditável e visualizações prontas para uso.

O projeto foi desenhado intencionalmente para cobrir o que há de mais relevante no mercado de dados em 2025-2026: agentes autônomos com MCP, Agentic RAG multimodal, deep learning para séries temporais epidemiológicas e infraestrutura containerizada pronta para produção, tudo aplicado a um problema real e com dados públicos brasileiros.

---

## Por que este projeto é diferente?

**No mercado de dados:**
- Agentic AI cresceu 1.445% em consultas de mercado entre Q1 2024 e Q2 2025 (Gartner)
- Sistemas de vigilância epidemiológica com IA são uma das fronteiras mais abertas em saúde pública digital
- DATASUS e SINAN possuem décadas de dados históricos praticamente inexplorados com arquiteturas modernas de agentes

**No contexto brasileiro:**
- O Brasil enfrenta ciclos anuais de dengue, leptospirose e outras arboviroses com impacto em milhões de pessoas
- ? Não existe publicamente um sistema de vigilância epidemiológica baseado em agentes LLM com RAG sobre literatura científica brasileira
- Projetos com dados do SUS e machine learning têm altíssima visibilidade em processos seletivos de empresas de saúde, fintechs de seguro e consultorias de dados no Brasil

**Na empregabilidade:**
- Portfólios com domínio aplicado concreto se destacam sobre projetos genéricos
- A combinação de NLP + séries temporais + dados públicos + infraestrutura é o que empresas como iFood Health, Hapvida, Dasa, Fleury e startups de healthtech buscam
- Docker + Kubernetes + CI/CD é o padrão de entrevistas para posições plenas e sênior em dado

---

## Arquitetura Geral

```
                        +----------------------------+
                        |   React Frontend             |
                        |   Dashboard Epidemiologico   |
                        |   Mapa + Chat + Alertas      |
                        +-----------+----------------+
                                    |
                        +-----------v----------------+
                        |   FastAPI Gateway            |
                        |   REST + WebSocket           |
                        +-----------+----------------+
                                    |
               +--------------------v-----------------------+
               |           Orchestrator Agent               |
               |           (LangGraph + Claude)             |
               |   Planeja estrategia, delega, consolida    |
               +---+----------+----------+----------+-------+
                   |          |          |          |
         +---------v-+ +------v--+ +-----v--+ +----v-------+
         |  DataSUS   | |  RAG    | |Forecast| |  Report    |
         |  Agent     | |  Agent  | |  Agent | |  Agent     |
         +---------+--+ +----+----+ +----+---+ +-----+------+
                   |         |           |           |
           +-------v---------v-----------v-----------v------+
           |                   MCP Servers                   |
           |  DATASUS | SINAN | PubMed | Geocoding | Files   |
           +-------------------------------------------------+
```

### Estrutura do Repositório

```
epidemia/
├── agents/
│   ├── orchestrator.py          # Agente central com LangGraph StateGraph
│   ├── datasus_agent.py         # Coleta e normaliza dados do DATASUS/SINAN
│   ├── rag_agent.py             # Recupera literatura epidemiologica relevante
│   ├── forecast_agent.py        # Aciona modelos de previsao de surtos
│   └── report_agent.py          # Gera relatorios e alertas automatizados
│
├── mcp_servers/
│   ├── datasus_server.py        # Servidor MCP para DATASUS e SINAN
│   ├── pubmed_server.py         # Servidor MCP para PubMed e SciELO
│   ├── filesystem_server.py     # Acesso a dados e relatorios locais
│   └── geocoding_server.py      # Resolucao geografica de municipios brasileiros
│
├── rag/
│   ├── ingestion/
│   │   ├── loaders.py           # PDF de boletins epidemiologicos, artigos
│   │   ├── chunker.py           # Chunking semantico adaptativo
│   │   └── embedder.py          # Modelo de embedding fine-tunado em pt-BR
│   ├── retrieval/
│   │   ├── hybrid_search.py     # BM25 + Dense Retrieval
│   │   ├── reranker.py          # Cross-encoder reranking
│   │   └── hyde.py              # Hypothetical Document Embeddings
│   └── vector_store/
│       └── qdrant_client.py
│
├── deep_learning/
│   ├── forecasting/
│   │   ├── tft_model.py         # Temporal Fusion Transformer para surtos
│   │   ├── dataset.py           # Pipeline de series temporais epidemiologicas
│   │   ├── train.py
│   │   └── evaluate.py          # MAE, RMSE, WIS por doenca e municipio
│   ├── embedding_finetuning/
│   │   ├── train.py             # Fine-tuning em corpus biomedico pt-BR
│   │   └── dataset.py
│   └── anomaly_detection/
│       ├── model.py             # Deteccao de anomalias em series epidemiologicas
│       └── train.py
│
├── data/
│   ├── raw/                     # Dados brutos do DATASUS e SINAN
│   ├── processed/               # Series temporais normalizadas por municipio
│   ├── embeddings/              # Corpus de literatura epidemiologica indexado
│   └── training/                # Dados de treinamento dos modelos DL
│
├── api/
│   ├── routes/
│   │   ├── chat.py              # Endpoint de interacao com agentes
│   │   ├── alerts.py            # Alertas de surto em tempo real
│   │   └── reports.py           # Geracao e download de relatorios
│   ├── schemas/
│   └── websocket.py             # Streaming de respostas e alertas
│
├── infra/
│   ├── docker/
│   │   ├── Dockerfile.api
│   │   ├── Dockerfile.worker
│   │   └── docker-compose.yml
│   ├── k8s/
│   │   ├── deployments/
│   │   ├── services/
│   │   ├── cronjobs/            # Ingestao automatica semanal do DATASUS
│   │   └── hpa.yaml
│   └── monitoring/
│       ├── prometheus.yml
│       └── grafana/
│           └── dashboards/
│
├── frontend/
│   ├── components/
│   │   ├── ChatInterface.tsx
│   │   ├── EpidemiologicalMap.tsx   # Mapa de calor por municipio (Leaflet)
│   │   ├── AgentTraceViewer.tsx     # Visualiza raciocinio dos agentes
│   │   ├── ForecastChart.tsx        # Previsao de casos por doenca
│   │   └── AlertBanner.tsx          # Alertas de risco de surto
│   └── hooks/
│
├── notebooks/
│   ├── 01_datasus_exploration.ipynb
│   ├── 02_sinan_dengue_analysis.ipynb
│   ├── 03_tft_experiments.ipynb
│   ├── 04_embedding_finetuning.ipynb
│   ├── 05_anomaly_detection.ipynb
│   └── 06_rag_evaluation.ipynb
│
├── tests/
├── .github/workflows/
│   ├── ci.yml
│   └── data_ingestion.yml       # Workflow de ingestao de dados DATASUS
└── mlflow/
```

---

## Stack Tecnológico

### Agentes e Orquestração
| Tecnologia | Uso |
|---|---|
| **LangGraph** | Orquestração de agentes com StateGraph e ciclos de raciocínio |
| **OpenAI** | LLM base para raciocínio dos agentes |
| **MCP (Model Context Protocol)** | Protocolo padrão para integração com DATASUS, PubMed e APIs externas |

### RAG e Recuperação
| Tecnologia | Uso |
|---|---|
| **AI Foundry** | Linkando Agentes com AI Search |


### Deep Learning
| Tecnologia | Uso |
|---|---|
| **Keras** | Framework principal |

### Dados Públicos Brasileiros
| Fonte | Conteúdo |
|---|---|
| **DATASUS (TabNet/API)** | Dados históricos de morbidade e mortalidade por município |
| **SINAN** | Sistema de Informação de Agravos de Notificação |
| **PubMed / SciELO** | Literatura científica para o pipeline RAG |
| **Boletins Epidemiológicos** | PDFs do Ministério da Saúde indexados no RAG |
| **OpenDengue** | Dataset global de dengue com dados brasileiros |

### Infraestrutura
| Tecnologia | Uso |
|---|---|
| **Docker + Docker Compose** | Ambiente de desenvolvimento |
| **Kubernetes + HPA** | Orquestração em produção com autoscaling |
| **FastAPI** | API REST + WebSocket para streaming |
| **Redis** | Cache de resultados e filas |
| **PostgreSQL + PostGIS** | Persistência com suporte a dados geoespaciais |
| **Prometheus + Grafana** | Observabilidade do sistema e dashboards epidemiológicos |
| **GitHub Actions** | CI/CD com ingestão automática semanal do DATASUS |

---

## Funcionalidades

### Agente Orquestrador
- Interpretação de perguntas em linguagem natural sobre saúde pública brasileira
- Planejamento dinâmico de tarefas com raciocínio Chain-of-Thought
- Delegação inteligente para os agentes especializados
- Consolidação de dados quantitativos e qualitativos em resposta única com fontes
- Raciocínio auditável na interface

### Agente DATASUS
- Coleta automática de dados do TabNet e da API DATASUS
- Normalização e alinhamento temporal de séries por município e CID
- Cálculo de indicadores epidemiológicos: incidência, mortalidade, taxa de hospitalização
- Cache inteligente para evitar requisições redundantes à API

### Agentic RAG Epidemiológico
- Corpus indexado: artigos PubMed, SciELO e boletins do Ministério da Saúde em PDF
- Recuperação em português e inglês com embeddings fine-tunados no domínio biomédico
- Busca híbrida (BM25 + dense) com reranqueamento por relevância
- Self-RAG: o agente decide dinamicamente quando buscar na literatura

### Agente de Forecasting
- Modelo Temporal Fusion Transformer treinado em séries históricas brasileiras
- Previsão de curto prazo (1 a 4 semanas) para dengue, leptospirose e outras notificações
- Detecção de anomalias para identificação precoce de surtos
- Intervalos de confiança calibrados por município e época do ano

### Agente de Relatórios e Alertas
- Geração automática de boletins epidemiológicos em PDF e Markdown
- Alertas de risco classificados por nível: atenção, alerta e emergência
- Dashboard interativo com mapa de calor por município
- Exportação em formatos compatíveis com gestão municipal de saúde

---

## Exemplos de Perguntas que o Sistema Responde

```
"Qual a situação atual de dengue no Pará e quais municípios têm maior risco
 de surto nas próximas 4 semanas?"

"Compare a mortalidade infantil entre Norte e Sudeste entre 2018 e 2024
 com contexto da literatura científica."

"Gere um boletim epidemiológico de leptospirose para São Paulo referente
 ao último trimestre."

"Quais municípios do Nordeste apresentaram anomalia estatística em notificações
 de arboviroses nos últimos 60 dias?"

"Com base nos dados históricos do SINAN, qual o perfil demográfico mais
 afetado por chikungunya no Brasil?"
```

---

## Doenças e Agravos Cobertos (v1)

- Dengue
- Chikungunya
- Zika
- Leptospirose
- Leishmaniose visceral e tegumentar
- Doença de Chagas
- Sarampo e Rubéola

O sistema é extensível: adicionar uma nova doença significa adicionar sua CID ao pipeline de coleta do SINAN.

---

## Primeiros Passos

### Pré-requisitos

```bash
-
```

### Instalação local

```bash
-
```

### Executando

```bash
-
```
---

## Treinando os Modelos

```bash
-
```

---

## Métricas de Avaliação

### Pipeline RAG
```
-
```

### Modelos de Forecasting
```
-
```

---

## Deploy com Kubernetes

```bash
-
```

---

## Roadmap

- [x] Definição de arquitetura e estrutura do projeto
- [ ] **Fase 1** - Infraestrutura base: Docker Compose + FastAPI + Qdrant + PostGIS
- [ ] **Fase 2** - Ingestão e normalização de dados DATASUS e SINAN
- [ ] **Fase 3** - Pipeline RAG com literatura epidemiológica em pt-BR
- [ ] **Fase 4** - Agentes especializados com LangGraph
- [ ] **Fase 5** - MCP Servers para DATASUS, PubMed e geocodificação
- [ ] **Fase 6** - Modelo TFT de forecasting de surtos
- [ ] **Fase 7** - Dashboard com mapa de calor e sistema de alertas
- [ ] **Fase 8** - Deploy Kubernetes + cronjob de ingestão semanal
- [ ] **Fase 9** - Avaliação end-to-end e documentação final

---

## Testes

```bash
-
```

---

## O que este projeto cobre

```
Agentes Autônomos      LangGraph, ReAct, CoT, planejamento multi-step
MCP                    Servidores customizados para DATASUS, PubMed e geocodificacao
Agentic RAG            Busca hibrida, reranking, HyDE, Self-RAG, corpus em pt-BR
Deep Learning          Temporal Fusion Transformer, fine-tuning de embeddings, anomaly detection
MLOps                  MLflow, versionamento de modelos, avaliacao epidemiologica
Infraestrutura         Docker, Kubernetes, cronjobs, CI/CD, Prometheus, Grafana
Dados Publicos BR      DATASUS, SINAN, PubMed, SciELO, boletins do Ministerio da Saude
Dados Geoespaciais     PostGIS, Leaflet, mapa de calor por municipio brasileiro
Backend                FastAPI, WebSockets, Redis, PostgreSQL
Frontend               React, dashboard epidemiologico interativo
```

---

## Referências de Dados

- [DATASUS TabNet](http://tabnet.datasus.gov.br)
- [SINAN Online](https://sinan.saude.gov.br)
- [Boletins Epidemiológicos - Ministério da Saúde](https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/boletins/epidemiologicos)
- [OpenDengue Dataset](https://opendengue.org)
- [SciELO Brasil](https://scielo.br)

---

## Licença

MIT License. Veja o arquivo [LICENSE](LICENSE) para detalhes.