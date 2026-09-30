## Como usar este guia

- Use os capítulos 1 a 11 para revisão de conteúdo. Eles seguem os cinco domínios do exame: fundamentos de IA e ML (capítulos 1 a 3), fundamentos de IA generativa (4 a 6), aplicações de foundation models (7 a 9), IA responsável (10) e segurança e governança (11).
- Use a tabela **Decisão rápida** ao final de cada capítulo (1 a 11) como cheat sheet de véspera de prova: cada uma reúne cenários típicos, a resposta correta e os distratores clássicos daquele tema.
- Use os **Padrões recorrentes e palavras-chave** (seção 12) para treinar a leitura do enunciado. No AI Practitioner, uma expressão como "sem treinar modelo", "dados privados atualizados", "menor custo de customização" ou "filtrar conteúdo nocivo" costuma decidir a questão.
- Use o **Mapa de Domínios** (seção 13) para priorizar a revisão conforme o peso de cada domínio na nota final.
- Use o **Autoteste** (seção 14) para revisão ativa: cada flashcard esconde a resposta até você clicar, forçando recall em vez de releitura passiva.
- Use o **Mapa de cobertura e questões de múltipla resposta** (seção 15) para conferir as 14 tarefas oficiais e praticar os formatos de questão do exame, inclusive **ordenação** e **correspondência**.
- O AI Practitioner cobra **conceitos e escolha de serviço**, não programação nem matemática. Para cada tema, saiba responder: **o que é**, **quando usar**, **quanto custa em relação às alternativas** e **qual risco traz**.

### Números, preços e atualizações

Os números, nomes de serviços e datas deste guia foram conferidos na documentação oficial da AWS (docs.aws.amazon.com e aws.amazon.com) em **setembro de 2026**. São uma referência datada: confirme disponibilidade e preços antes de depender de um valor exato.

*O ecossistema de IA da AWS mudou muito em 2026, e a maior parte dos cursos e simulados ainda não reflete isso:*

- *O **guia do exame foi revisado para a versão 1.1** (30/abr/2026). Entraram IA agêntica, **Model Context Protocol (MCP)**, engenharia de contexto, preço por tokens, detecção de alucinação e os serviços **Kiro**, **Strands Agents**, **Amazon Bedrock AgentCore**, **Amazon Quick**, **SageMaker JumpStart** e **AWS Transform**.*
- *Em **30/jul/2026**, vários serviços e recursos passaram a **modo de manutenção** (não aceitam novos clientes; quem já usa continua): **Amazon Bedrock Agents** (agora "Agents Classic", substituído pelo AgentCore), **Amazon Kendra**, **Amazon Q Business** e os recursos do SageMaker AI **Clarify, Model Monitor, Ground Truth, Augmented AI (A2I)**, Debugger e Role Manager.*
- *O **Amazon Q Developer** deixou de aceitar novas assinaturas em 15/mai/2026 e será substituído pelo **Kiro**.*

Esses serviços ainda aparecem em simulados e explicam conceitos cobrados na prova, como detecção de viés, monitoramento de drift e revisão humana. Por isso o guia os ensina, sempre indicando a situação atual.

### Método para questões do AI Practitioner

1. **Classifique o problema**: é previsão com dados estruturados (ML tradicional), tarefa pronta de percepção (serviço de IA gerenciado), geração de conteúdo (IA generativa) ou execução de tarefas em várias etapas (agente)?
2. **Prefira o caminho de menor esforço que atende**: serviço de IA pronto → Bedrock com prompt → RAG → fine-tuning → treinar do zero. Só suba um degrau quando o enunciado exigir.
3. **Leia a restrição decisiva**: "dados privados e atualizados" leva a RAG; "tom e formato específicos do domínio" leva a fine-tuning; "sem acesso à internet pública" leva a PrivateLink; "bloquear tópicos" leva a Guardrails; "explicar a decisão ao regulador" leva a modelo interpretável.
4. **Desconfie das alternativas que exageram**: treinar um modelo do zero quase nunca é a resposta de menor custo, e mais dados de treino não resolvem uma pergunta sobre fatos de ontem.
5. **Questões de ordenação e correspondência**: não há crédito parcial. Revise a ordem das etapas do pipeline de ML, do RAG e do ciclo de vida de FMs.

### Formato do exame AIF-C01

| Item | Valor |
|---|---|
| Código | AIF-C01 (guia versão 1.1, vigente em setembro de 2026) |
| Questões | 65 no total: **50 pontuadas** e **15 não pontuadas** (não identificadas) |
| Duração | 90 minutos |
| Tipos de questão | **Múltipla escolha** (1 correta entre 4), **múltipla resposta** (2 ou mais corretas entre 5 ou mais), **ordenação** (colocar 3 a 5 itens na ordem certa) e **correspondência** (associar respostas a 3 a 7 enunciados) |
| Pontuação | Escala de 100 a 1.000; **mínimo de 700** para aprovação |
| Modelo de pontuação | **Compensatório**: não é preciso passar em cada domínio, só na prova como um todo |
| Chute | Questão em branco conta como errada e **não há penalidade** por errar |
| Público-alvo | Até 6 meses de exposição a IA/ML na AWS; **usa**, mas não necessariamente **constrói**, soluções de IA |
| Fora do escopo | Programar modelos, engenharia de dados e de features, tuning de hiperparâmetros, construir pipelines, análise matemática, implementar protocolos de segurança e frameworks de governança |
| Valor | US$ 100 (confira o preço vigente no site de certificação) |

### Domínios do exame AIF-C01 (pesos oficiais)

| Domínio | Peso |
|---|---|
| Fundamentals of AI and ML (Fundamentos de IA e ML) | 20% |
| Fundamentals of GenAI (Fundamentos de IA generativa) | 24% |
| Applications of Foundation Models (Aplicações de foundation models) | 28% |
| Guidelines for Responsible AI (Diretrizes de IA responsável) | 14% |
| Security, Compliance, and Governance for AI Solutions (Segurança, conformidade e governança) | 14% |

---

## 1. Fundamentos de IA e ML

> **Regra de ouro da prova**: pense em círculos concêntricos. **IA** é o campo amplo; **machine learning** é a parte da IA que aprende padrões com dados; **deep learning** é a parte do ML que usa redes neurais com muitas camadas; **IA generativa** usa deep learning para **criar conteúdo novo**; **IA agêntica** usa modelos generativos para **planejar e executar tarefas** com ferramentas.

### Conceitos e terminologia

#### Termos básicos

| Termo | Definição para a prova |
|---|---|
| **Inteligência artificial (IA)** | Campo que busca fazer máquinas executarem tarefas que exigiriam inteligência humana: perceber, raciocinar, aprender e decidir |
| **Machine learning (ML)** | Subconjunto da IA em que o sistema **aprende padrões a partir de dados**, sem regras programadas explicitamente |
| **Deep learning** | Subconjunto do ML que usa **redes neurais com muitas camadas**; é bom com dados não estruturados (imagem, áudio, texto) |
| **Rede neural** | Estrutura de nós (neurônios) organizados em camadas que ajustam **pesos** durante o treinamento |
| **Visão computacional** | IA que interpreta imagens e vídeos (detectar objetos, rostos, defeitos) |
| **Processamento de linguagem natural (NLP)** | IA que entende e gera linguagem humana (sentimento, tradução, resumo) |
| **Algoritmo** | O **método** de aprendizado (ex.: regressão linear, árvore de decisão, XGBoost) |
| **Modelo** | O **resultado do treinamento**: o algoritmo com os parâmetros aprendidos, pronto para fazer previsões |
| **Treinamento** | Processo de ajustar os parâmetros do modelo com dados |
| **Inferência** | Usar o modelo treinado para fazer **previsões ou gerar saídas** com dados novos |
| **Viés (bias)** | Erro sistemático que favorece ou prejudica resultados ou grupos. Em ML também significa suposições simplificadoras demais do modelo |
| **Justiça (fairness)** | Resultados que não discriminam indevidamente grupos de pessoas |
| **Ajuste (fit)** | Quão bem o modelo captura o padrão. **Overfitting**: ótimo no treino, ruim em dados novos. **Underfitting**: ruim até no treino |
| **Large language model (LLM)** | Modelo de linguagem muito grande, baseado em **transformers**, treinado em enormes volumes de texto |
| **IA generativa (GenAI)** | IA que **cria conteúdo novo** (texto, imagem, áudio, vídeo, código) a partir de um prompt |
| **IA agêntica (agentic AI)** | Sistemas em que modelos **planejam, decidem e agem** em várias etapas, usando ferramentas e memória, com autonomia (veja a seção 5) |

#### Semelhanças e diferenças entre IA, ML, deep learning, GenAI e IA agêntica
- Todos são **IA**. ML, deep learning e GenAI aprendem com dados; sistemas de regras também são IA, mas não são ML.
- **ML tradicional** costuma trabalhar com **dados estruturados** e produzir uma **previsão** (um número, uma classe).
- **Deep learning** lida bem com **dados não estruturados** e exige mais dados e computação.
- **GenAI** produz **conteúdo novo** e costuma usar **foundation models** pré-treinados, reaproveitáveis para muitas tarefas sem treinar de novo.
- **IA agêntica** não é um tipo novo de modelo: é uma **arquitetura** em que um modelo generativo decide os próximos passos, chama ferramentas e usa memória para cumprir um objetivo.

### Tipos de dados e de aprendizado

#### Tipos de dados em modelos de IA

| Tipo | Exemplo |
|---|---|
| **Rotulado** (labeled) | Imagens marcadas como "gato" ou "cachorro"; transações marcadas como "fraude" |
| **Não rotulado** (unlabeled) | Textos, cliques ou fotos sem marcação |
| **Tabular** | Linhas e colunas (planilha, tabela de banco) |
| **Série temporal** | Valores ordenados no tempo (vendas por dia, leituras de sensor) |
| **Imagem** | Fotos, raios X, imagens de satélite |
| **Texto** | E-mails, avaliações, documentos |
| **Estruturado** | Formato fixo e previsível (tabelas) |
| **Não estruturado** | Sem esquema fixo (texto livre, áudio, vídeo, imagem). A maior parte dos dados das empresas |

#### Tipos de aprendizado

| Tipo | Como aprende | Técnicas e exemplos |
|---|---|---|
| **Supervisionado** | Com **dados rotulados** (entrada → resposta correta conhecida) | **Classificação** (spam ou não, fraude ou não); **regressão** (prever preço, demanda) |
| **Não supervisionado** | Com **dados não rotulados**, encontrando estrutura por conta própria | **Clustering** (segmentar clientes), redução de dimensionalidade, **detecção de anomalias** |
| **Por reforço** (reinforcement learning) | Um **agente** age em um **ambiente** e aprende por **recompensas e penalidades** | Robótica, jogos, otimização de rotas, AWS DeepRacer; **RLHF** usa feedback humano como recompensa |
| **Autossupervisionado** | Cria os próprios rótulos a partir dos dados (ex.: prever a próxima palavra) | Pré-treinamento de LLMs e foundation models |
| **Semissupervisionado** | Poucos dados rotulados + muitos não rotulados | Quando rotular tudo é caro |

### Tipos de inferência

#### Como o modelo atende às requisições

| Tipo | Como funciona | Quando usar | Na AWS |
|---|---|---|---|
| **Tempo real** (real-time) | Endpoint sempre ativo responde a cada requisição com **baixa latência** | Recomendações no site, detecção de fraude no pagamento, chatbots | SageMaker AI real-time endpoints; Bedrock on-demand |
| **Serverless** | Endpoint sem gerenciar instâncias, que escala até zero; pode ter **cold start** | Tráfego **intermitente ou imprevisível**, com tolerância a alguma latência inicial | SageMaker AI Serverless Inference |
| **Assíncrona** (asynchronous) | Requisição entra em **fila**; o resultado é gravado no S3 e notificado depois | **Payloads grandes** (até 1 GB) e processamento **longo** (até cerca de 1 hora) | SageMaker AI Asynchronous Inference |
| **Em lote** (batch) | Processa um **conjunto grande de dados de uma vez**, sem endpoint persistente | Pontuar milhões de registros por noite; quando **não** é preciso resposta imediata | SageMaker AI Batch Transform; **Bedrock batch inference** (preço menor que on-demand) |

### Decisão rápida — Fundamentos de IA e ML

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Prever o preço de um imóvel | Aprendizado supervisionado — regressão | Classificação, clustering |
| Classificar e-mails como spam | Aprendizado supervisionado — classificação | Regressão, clustering |
| Segmentar clientes sem rótulos | Não supervisionado — clustering | Classificação |
| Robô que aprende por tentativa e erro com recompensas | Aprendizado por reforço | Supervisionado |
| Ajustar um LLM com preferências humanas | RLHF | Clustering, pré-treinamento |
| Modelo ótimo no treino e ruim em dados novos | Overfitting | Underfitting |
| Modelo ruim até nos dados de treino | Underfitting | Overfitting |
| Resposta imediata a cada transação | Inferência em tempo real | Batch |
| Pontuar milhões de registros uma vez por noite | Inferência em lote | Tempo real |
| Tráfego intermitente sem gerenciar instâncias | Inferência serverless | Endpoint real-time sempre ativo |
| Payload de 500 MB e processamento de 20 minutos | Inferência assíncrona | Tempo real, serverless |
| Sistema que planeja e usa ferramentas em várias etapas | IA agêntica | ML tradicional |

---

## 2. Casos de Uso e Serviços de IA

> **Regra de ouro da prova**: antes de escolher o modelo, pergunte se **IA é mesmo necessária**. Se o resultado precisa ser **exato e determinístico** (calcular imposto, aplicar uma regra fixa), use regras ou código. Se é uma tarefa comum de percepção ou linguagem, use um **serviço de IA pronto** antes de treinar qualquer coisa.

### Quando a IA agrega valor

#### Onde IA/ML ajuda
- **Apoiar decisões humanas**: priorizar leads, sugerir diagnóstico para revisão médica, sinalizar transações suspeitas.
- **Escalar soluções**: analisar milhões de documentos, imagens ou chamadas que humanos não conseguiriam revisar.
- **Automatizar** tarefas repetitivas: extrair dados de formulários, transcrever, traduzir, classificar tickets.
- **Encontrar padrões** complexos demais para regras escritas à mão.

#### Quando IA/ML não é apropriada
- **O custo supera o benefício**: pouco volume, ganho pequeno ou custo alto de dados, treinamento e operação.
- **É preciso um resultado específico, não uma previsão**: regras de negócio fixas, cálculos exatos, conformidade que exige a mesma saída sempre.
- **Faltam dados** suficientes, representativos ou de qualidade.
- **Explicabilidade total é exigida** e o modelo disponível é uma "caixa-preta".
- O **erro é inaceitável** e não há revisão humana.

#### Escolhendo a técnica de ML

| Técnica | Saída | Exemplos |
|---|---|---|
| **Regressão** | Um **número contínuo** | Prever vendas, preço, tempo de entrega, consumo de energia |
| **Classificação** | Uma **categoria** (binária ou múltipla) | Fraude sim/não, sentimento positivo/negativo, tipo de defeito |
| **Clustering** | **Grupos** de itens parecidos, sem rótulos | Segmentação de clientes, agrupar documentos |
| **Detecção de anomalias** | Itens **fora do padrão** | Fraude, falha de equipamento, intrusão |
| **Previsão de séries temporais** (forecasting) | Valores futuros ao longo do tempo | Demanda do próximo mês, capacidade |
| **Recomendação** | Itens relevantes para cada usuário | "Quem comprou isto também comprou" |

### Aplicações reais e serviços gerenciados

#### Exemplos de aplicações de IA

| Aplicação | Exemplo | Serviço AWS típico |
|---|---|---|
| **Visão computacional** | Moderar imagens, reconhecer rostos, contar pessoas | Amazon Rekognition |
| **Extração de documentos** | Ler notas fiscais, formulários, tabelas | Amazon Textract, Bedrock Data Automation |
| **NLP** | Sentimento de avaliações, entidades, PII em texto | Amazon Comprehend |
| **Reconhecimento de fala** | Transcrever chamadas e reuniões | Amazon Transcribe |
| **Síntese de fala** | Ler textos em voz alta | Amazon Polly |
| **Tradução** | Traduzir conteúdo | Amazon Translate |
| **Chatbots** | Atendimento por voz e texto | Amazon Lex, Amazon Bedrock |
| **Sistemas de recomendação** | Recomendações personalizadas | Amazon Personalize |
| **Detecção de fraude** | Transações suspeitas | Modelos no SageMaker AI |
| **Previsão** (forecasting) | Demanda e estoque | SageMaker AI (Canvas, algoritmos de séries temporais) |
| **Bases de conhecimento** | Responder perguntas com documentos da empresa | Amazon Bedrock Knowledge Bases |
| **IA agêntica** | Assistente que consulta sistemas e executa tarefas | Amazon Bedrock AgentCore, Amazon Quick |

#### Serviços de IA gerenciados (sem treinar modelo)

| Serviço | O que faz | Palavra-chave |
|---|---|---|
| **Amazon Rekognition** | Análise de imagens e vídeos: objetos, cenas, texto, **rostos** (comparação e busca), **moderação de conteúdo**, rótulos personalizados | "Detectar rostos", "conteúdo impróprio em imagens" |
| **Amazon Textract** | Extrai **texto, formulários (pares chave-valor) e tabelas** de documentos digitalizados; vai além do OCR simples | "Extrair dados de formulários escaneados" |
| **Amazon Comprehend** | **NLP**: sentimento, entidades, frases-chave, idioma, tópicos, **detecção de PII**, classificação personalizada. **Comprehend Medical** para textos clínicos | "Sentimento de avaliações", "entidades em documentos" |
| **Amazon Transcribe** | **Fala para texto**, com identificação de locutores, vocabulário personalizado e redação de PII. **Call Analytics** e **Transcribe Medical** | "Transcrever chamadas", "legendas" |
| **Amazon Polly** | **Texto para fala** com vozes naturais (neurais) e SSML | "Converter texto em áudio" |
| **Amazon Translate** | **Tradução automática neural**, com terminologia personalizada | "Traduzir conteúdo em tempo real" |
| **Amazon Lex** | **Chatbots** de voz e texto com reconhecimento de intenção (mesma tecnologia da Alexa); integra-se ao Amazon Connect | "Criar bot conversacional para atendimento" |
| **Amazon Personalize** | **Recomendações personalizadas** em tempo real, com a tecnologia usada na Amazon.com | "Recomendar produtos a cada usuário" |
| **Amazon SageMaker AI** | Plataforma para **construir, treinar e implantar modelos próprios** (seção 3) | "Modelo personalizado com dados próprios" |

- *Material antigo cita **Amazon Kendra** (busca corporativa inteligente), **Amazon Forecast**, **Amazon Fraud Detector** e a família **Amazon Lookout**. O Kendra entrou em modo de manutenção em 30/jul/2026, e a recomendação atual para busca e perguntas sobre documentos é **Amazon Bedrock Knowledge Bases**. Os demais também deixaram de aceitar novos clientes ou tiveram o suporte encerrado; confira a disponibilidade antes de escolher.*

### ML tradicional ou foundation model

#### Como decidir

| Critério | ML tradicional tende a ser melhor | Foundation model tende a ser melhor |
|---|---|---|
| **Tipo de tarefa** | Previsão específica com dados estruturados (churn, preço, fraude) | Linguagem, conteúdo, conversas, tarefas abertas e variadas |
| **Regulação e explicabilidade** | Exigência de **explicar cada decisão** (crédito, seguros): modelos interpretáveis | Quando a explicação detalhada de cada saída não é exigida |
| **Restrições operacionais** | Latência muito baixa, custo por previsão mínimo, execução em dispositivo | Quando é aceitável custo por token e latência maiores |
| **Dados** | Muitos dados rotulados do próprio negócio | Poucos dados rotulados; o FM já traz conhecimento geral |
| **Determinismo** | Mesma entrada, mesma saída | Saídas variáveis (não determinísticas) são aceitáveis |
| **Tempo de entrega** | Projeto de ML com treinamento | Protótipo rápido com prompt, sem treinar |

### Decisão rápida — Casos de uso e serviços

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Cálculo que precisa dar sempre o mesmo resultado exato | Regras/código, não ML | Modelo de ML, LLM |
| Prever a demanda do próximo mês | Regressão / forecasting | Clustering |
| Agrupar clientes por comportamento | Clustering | Classificação |
| Detectar rostos e conteúdo impróprio em fotos | Amazon Rekognition | Textract, Comprehend |
| Extrair tabelas de PDFs digitalizados | Amazon Textract | Rekognition, Comprehend |
| Sentimento e PII em avaliações | Amazon Comprehend | Translate, Textract |
| Transcrever chamadas do call center | Amazon Transcribe | Polly |
| Gerar áudio a partir de texto | Amazon Polly | Transcribe |
| Traduzir o site | Amazon Translate | Comprehend |
| Chatbot com intenções para atendimento | Amazon Lex | Polly, Rekognition |
| Recomendações personalizadas | Amazon Personalize | Comprehend |
| Modelo próprio com dados da empresa | Amazon SageMaker AI | Serviços de IA prontos |
| Decisão de crédito que precisa ser explicada ao regulador | Modelo de ML tradicional interpretável | LLM de propósito geral |
| Perguntas sobre documentos internos (busca atual) | Bedrock Knowledge Bases | Kendra para novos clientes |

---

## 3. Ciclo de Vida de IA/ML e MLOps

> **Regra de ouro da prova**: a ordem do pipeline cai em questões de **ordenação**. Decore: **objetivo de negócio → enquadrar o problema de ML → coletar dados → explorar (EDA) → pré-processar → engenharia de features → treinar → ajustar hiperparâmetros → avaliar → implantar → monitorar** (e retreinar).

### Pipeline de IA/ML

#### Etapas e o que acontece em cada uma

| Etapa | O que acontece | Serviços AWS |
|---|---|---|
| **1. Objetivo de negócio** | Definir o problema, a métrica de sucesso e o valor esperado | — |
| **2. Enquadrar o problema de ML** | Traduzir em tarefa de ML (classificação, regressão…) e verificar se ML é adequado | — |
| **3. Coleta de dados** | Reunir dados de várias fontes e rotulá-los quando preciso | S3, AWS Glue, AWS Data Exchange, SageMaker Ground Truth (rotulagem) |
| **4. Análise exploratória (EDA)** | Entender distribuições, correlações, valores faltantes e desbalanceamento | SageMaker Data Wrangler, SageMaker Canvas, Athena, Amazon Quick |
| **5. Pré-processamento** | Limpar, tratar faltantes, remover duplicatas, normalizar, dividir em treino/validação/teste | AWS Glue, Glue DataBrew, Data Wrangler |
| **6. Engenharia de features** | Criar e selecionar as variáveis que o modelo usa | Data Wrangler, **SageMaker Feature Store** (guarda e compartilha features) |
| **7. Treinamento** | Ajustar os parâmetros do modelo com os dados de treino | SageMaker AI Training, JumpStart, Autopilot/Canvas |
| **8. Ajuste de hiperparâmetros** | Buscar a melhor configuração (taxa de aprendizado, profundidade…) | SageMaker Automatic Model Tuning |
| **9. Avaliação** | Medir desempenho em dados que o modelo não viu (métricas da seção 3) | SageMaker AI, SageMaker Clarify (viés), Bedrock Model Evaluation |
| **10. Implantação** | Colocar o modelo em produção (endpoint, batch) | SageMaker AI endpoints, SageMaker Model Registry |
| **11. Monitoramento** | Acompanhar qualidade, **drift** de dados e de conceito, viés e custo; retreinar quando necessário | SageMaker Model Monitor, CloudWatch |

- **Hiperparâmetro vs. parâmetro**: **parâmetros** (pesos) são aprendidos no treinamento; **hiperparâmetros** são escolhidos **antes** do treinamento (ex.: número de épocas, taxa de aprendizado).
- **Divisão dos dados**: **treino** ensina o modelo, **validação** ajusta hiperparâmetros e **teste** mede o desempenho final em dados nunca vistos.

#### Serviços e recursos por etapa

| Serviço ou recurso | Papel no ciclo de vida |
|---|---|
| **Amazon SageMaker AI** | Plataforma completa para construir, treinar, implantar e gerenciar modelos (antigo Amazon SageMaker) |
| **SageMaker Studio** | Ambiente de desenvolvimento web para todo o ciclo de ML |
| **SageMaker Canvas** | ML **sem código** para analistas de negócio (previsões por interface visual) |
| **SageMaker JumpStart** | **Hub de modelos pré-treinados** e foundation models para implantar e ajustar com poucos cliques |
| **SageMaker Data Wrangler** | Preparação visual de dados e engenharia de features |
| **SageMaker Feature Store** | Repositório central de features para treino e inferência |
| **SageMaker Pipelines** | Automatiza fluxos de ML (CI/CD de ML) |
| **SageMaker Model Registry** | Catálogo de versões de modelos com aprovação para produção |
| **SageMaker Model Cards** | **Documentação** do modelo: uso pretendido, dados, métricas, riscos (governança) |
| **SageMaker Clarify** | Detecção de **viés** e **explicabilidade** (importância das features). *Em manutenção desde 30/jul/2026* |
| **SageMaker Model Monitor** | Monitoramento de **drift** e qualidade em produção. *Em manutenção desde 30/jul/2026* |
| **SageMaker Ground Truth** | **Rotulagem** de dados com humanos e automação. *Em manutenção desde 30/jul/2026* |
| **Amazon Augmented AI (A2I)** | **Revisão humana** de previsões de baixa confiança. *Em manutenção desde 30/jul/2026* |
| **Amazon Bedrock** | Foundation models por API, com customização, avaliação e guardrails (seção 6) |
| **Amazon Quick** | Espaço de trabalho de IA para usuários de negócio: BI (Quick Sight), pesquisa, fluxos e agentes |
| **Kiro** | Ambiente de desenvolvimento agêntico para criar aplicações de IA (seção 5) |
| **AWS Glue, Glue DataBrew, Lake Formation, Data Exchange** | Preparar, catalogar, governar e obter dados |

### Fontes de modelos e uso em produção

#### De onde vêm os modelos
- **Modelos pré-treinados de código aberto** (open-weight): Llama, Mistral e outros, disponíveis no Bedrock, no SageMaker JumpStart ou em repositórios públicos. Você pode usá-los como estão ou ajustá-los.
- **Modelos proprietários via API**: Amazon Nova, Anthropic Claude e outros, acessados pelo Amazon Bedrock.
- **Treinar um modelo próprio**: com seus dados no SageMaker AI. Dá controle total, mas exige dados, tempo e custo. Treinar um foundation model do zero é o caminho mais caro de todos.

#### Formas de usar um modelo em produção
- **Serviço de API gerenciado** (ex.: **Amazon Bedrock**): sem infraestrutura para gerenciar, cobrança por uso (tokens), escala automática. Menor esforço operacional.
- **API auto-hospedada** (ex.: modelo em **endpoint do SageMaker AI**, EC2, ECS ou EKS): mais controle sobre o modelo, a versão e a infraestrutura, mas o cliente gerencia capacidade, escala e custo das instâncias.

### MLOps

#### Conceitos fundamentais
- **MLOps** aplica práticas de DevOps ao ciclo de vida de ML para colocar e manter modelos em produção de forma confiável.
- **Experimentação**: registrar experimentos, parâmetros e resultados para comparar versões.
- **Processos repetíveis**: pipelines automatizados de dados, treino e implantação (SageMaker Pipelines).
- **Sistemas escaláveis**: treino e inferência que crescem com a demanda.
- **Gerenciar dívida técnica**: evitar código e dados ad hoc que tornam o sistema frágil.
- **Prontidão para produção**: versionamento (Model Registry), testes, aprovação, rollback.
- **Monitoramento do modelo**: o desempenho **degrada com o tempo**. **Data drift** é a mudança na distribuição dos dados de entrada; **concept drift** é a mudança na relação entre entrada e resultado.
- **Retreinamento**: agendado ou disparado quando o monitoramento detecta queda de qualidade.

### Métricas de avaliação

#### Métricas de desempenho de classificação
Base: a **matriz de confusão**, com verdadeiros positivos (VP), falsos positivos (FP), verdadeiros negativos (VN) e falsos negativos (FN).

| Métrica | O que mede | Quando priorizar |
|---|---|---|
| **Acurácia** (accuracy) | Proporção de acertos no total | Classes **balanceadas**. Engana com dados desbalanceados (99% de "não fraude" dá 99% de acurácia a um modelo inútil) |
| **Precisão** (precision) | Dos que o modelo disse "positivo", quantos eram mesmo: VP / (VP + FP) | Quando **falso positivo é caro** (bloquear um cliente bom, marcar e-mail legítimo como spam) |
| **Recall** (sensibilidade) | Dos positivos reais, quantos o modelo encontrou: VP / (VP + FN) | Quando **falso negativo é caro** (não detectar fraude ou doença) |
| **F1 score** | Média harmônica de precisão e recall | Equilibrar as duas, especialmente com classes desbalanceadas |
| **AUC-ROC** | Capacidade de separar as classes em todos os limiares (0,5 = aleatório; 1 = perfeito) | Comparar classificadores binários |

- **Regressão** usa métricas de erro: **MAE** (erro absoluto médio), **RMSE** (raiz do erro quadrático médio) e **R²** (quanto da variação o modelo explica).

#### Métricas de negócio
- **Custo por usuário** ou por previsão, **custos de desenvolvimento**, **feedback dos clientes**, **retorno sobre o investimento (ROI)**.
- Um modelo tecnicamente ótimo que não melhora a métrica de negócio não entrega valor. As métricas de negócio são definidas na **primeira etapa** do pipeline.

### Decisão rápida — Ciclo de vida e MLOps

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Primeira etapa do pipeline de ML | Definir o objetivo de negócio | Coletar dados, treinar |
| Entender distribuições e valores faltantes | Análise exploratória (EDA) | Treinamento |
| Criar variáveis a partir dos dados | Engenharia de features | Ajuste de hiperparâmetros |
| Escolher a melhor taxa de aprendizado | Ajuste de hiperparâmetros | Engenharia de features |
| Dados de produção mudaram e o modelo piorou | Data drift → monitorar e retreinar | Aumentar a instância |
| Rotular milhares de imagens | Ground Truth (em manutenção) ou rotulagem própria | Rekognition, Comprehend |
| ML sem código para analistas | SageMaker Canvas | SageMaker Studio, EMR |
| Implantar modelo pré-treinado com poucos cliques | SageMaker JumpStart | Treinar do zero |
| Documentar uso pretendido e riscos do modelo | SageMaker Model Cards | CloudTrail, Model Registry |
| Versionar e aprovar modelos para produção | SageMaker Model Registry | Feature Store |
| Automatizar o fluxo de treino e implantação | SageMaker Pipelines | Step Functions genérico |
| Falso negativo é o erro mais caro (fraude, doença) | Priorizar recall | Acurácia, precisão |
| Falso positivo é o erro mais caro | Priorizar precisão | Recall |
| Equilibrar precisão e recall com classes desbalanceadas | F1 score | Acurácia |
| Menor esforço operacional para usar um modelo | API gerenciada (Bedrock) | Endpoint auto-hospedado |

---

## 4. Fundamentos de IA Generativa

> **Regra de ouro da prova**: um **foundation model (FM)** é um modelo grande, pré-treinado em dados amplos e **reaproveitável** para muitas tarefas. Você o adapta com **prompt**, **contexto (RAG)** ou **fine-tuning**, e paga por **tokens**. Suas fraquezas clássicas são **alucinação**, **não determinismo** e **baixa interpretabilidade**.

### Conceitos básicos de IA generativa

#### Termos fundamentais

| Termo | Definição para a prova |
|---|---|
| **Token** | Unidade de texto processada pelo modelo (uma palavra, parte de palavra ou pontuação). Limites de contexto e preço são medidos em tokens |
| **Chunking** | Dividir documentos em **pedaços** menores antes de gerar embeddings, para caber no contexto e melhorar a busca (RAG) |
| **Embedding** | Representação **numérica (vetor)** do significado de um texto, imagem ou áudio. Conteúdos parecidos geram vetores próximos |
| **Vetor** | Lista de números que representa o embedding; bancos vetoriais fazem **busca por similaridade** entre vetores |
| **Engenharia de prompt** | Projetar as instruções e o contexto enviados ao modelo para obter a melhor resposta (seção 8) |
| **Transformer** | Arquitetura de rede neural com **mecanismo de atenção** (self-attention), base dos LLMs modernos; processa sequências em paralelo |
| **Large language model (LLM)** | FM de linguagem baseado em transformers, treinado para prever o próximo token |
| **Foundation model (FM)** | Modelo grande pré-treinado em dados amplos, adaptável a muitas tarefas sem treinar do zero |
| **Modelo multimodal** | Aceita e/ou gera **mais de um tipo de dado** (texto, imagem, áudio, vídeo) |
| **Modelo de difusão** | Gera imagens (ou vídeo e áudio) partindo de **ruído** e removendo-o passo a passo até formar o conteúdo pedido |
| **Janela de contexto** | Quantidade máxima de tokens (entrada + saída) que o modelo considera de uma vez |
| **Alucinação** | Resposta **plausível, mas falsa** ou sem base nos dados |

#### Casos de uso de IA generativa
- **Geração de imagem, vídeo e áudio**: marketing, protótipos visuais, narração.
- **Resumo** de documentos, reuniões e chamadas.
- **Assistentes de IA** e **agentes de atendimento ao cliente**.
- **Tradução** e adaptação de conteúdo.
- **Geração de código** e documentação.
- **Busca** semântica e perguntas e respostas sobre documentos.
- **Mecanismos de recomendação** e personalização de conteúdo.

#### Ciclo de vida de um foundation model
1. **Seleção de dados**: reunir e curar dados amplos e de qualidade.
2. **Seleção do modelo**: arquitetura e tamanho (ou escolher um FM pronto).
3. **Pré-treinamento**: treinamento autossupervisionado em grande escala.
4. **Fine-tuning**: especializar para tarefas ou domínios.
5. **Avaliação**: benchmarks, métricas e avaliação humana.
6. **Implantação**: disponibilizar para inferência.
7. **Feedback**: coletar retorno de uso para melhorar o modelo (inclusive RLHF).

### Tokens, custo e contexto

#### Preço baseado em tokens
- A maioria dos FMs no Amazon Bedrock é cobrada **por token de entrada e por token de saída**, com preços diferentes para cada um. Tokens de **saída** costumam ser **mais caros** que os de entrada.
- **Efeito no custo**: prompts longos, muitos documentos no contexto, históricos de conversa extensos e respostas longas aumentam a conta. Um modelo maior custa mais por token.
- **Efeito no desempenho**: mais tokens significam **mais latência**, porque o modelo processa a entrada e gera a saída token a token.
- **Como reduzir**: escolher o **menor modelo que atende**, limitar o tamanho máximo de saída, enviar só o contexto relevante (bom chunking e recuperação), usar **cache de prompt** (prompt caching) para prefixos repetidos e **inferência em lote** quando não há urgência.

#### Engenharia de contexto
- É a disciplina de **decidir e montar o que entra na janela de contexto** do modelo a cada chamada: instruções do sistema, histórico relevante, documentos recuperados, resultados de ferramentas, memória e exemplos.
- Vai além da engenharia de prompt: trata o contexto como um **recurso limitado e caro**. Contexto demais aumenta custo e latência e pode "diluir" a informação importante; contexto de menos causa alucinação.
- **Técnicas**: recuperar só os trechos relevantes (RAG), resumir históricos longos, guardar fatos em **memória** de longo prazo e trazê-los quando necessário, estruturar a saída de ferramentas e remover informação obsoleta.
- É central em **agentes**, que acumulam muitas interações e resultados de ferramentas ao longo de uma tarefa.

### Capacidades e limitações

#### Vantagens da IA generativa
- **Adaptabilidade**: um mesmo modelo resolve muitas tarefas diferentes.
- **Responsividade**: respostas rápidas em linguagem natural.
- **Capacidade conversacional**: interações de várias rodadas.
- **Capacidade de gerar conteúdo** novo (texto, imagem, código, áudio).
- **Simplicidade**: menos necessidade de dados rotulados e de treinamento específico.

#### Desvantagens e limitações

| Limitação | O que é | Mitigação |
|---|---|---|
| **Alucinação** | Inventa fatos com confiança | RAG com citações, contextual grounding check, validação da saída |
| **Interpretabilidade** | Difícil explicar por que o modelo respondeu algo | Modelos mais simples quando a explicação é exigida; documentação; avaliação |
| **Imprecisão** | Erros factuais, cálculos errados, conhecimento desatualizado (data de corte) | RAG com dados atuais, ferramentas (agentes) para cálculos e consultas |
| **Não determinismo** | A mesma entrada pode gerar respostas diferentes | Temperatura baixa, prompts e formatos de saída estruturados |
| **Viés e toxicidade** | Reproduz vieses dos dados de treino | Guardrails, avaliação, dados diversos |
| **Custo e latência** | Tokens e modelos grandes custam e demoram | Modelo menor, cache, batch, destilação |

#### Seleção de modelos de IA generativa
Fatores do guia do exame: **tipo de modelo** (texto, imagem, multimodal, embeddings), **requisitos de desempenho**, **capacidades**, **restrições**, **conformidade**, **custo**, **latência** e **complexidade do modelo**. O capítulo 7 detalha os critérios de seleção.

#### Valor de negócio e métricas
- **Desempenho entre domínios** (cross-domain performance), **ROI**, **eficiência** (tempo economizado, tarefas automatizadas), **taxa de conversão**, **receita média por usuário (ARPU)**, **precisão** e **valor do tempo de vida do cliente (CLV)**.
- Métricas de alinhamento com o negócio em aplicações de IA: **taxa de conclusão de tarefas**, **satisfação do usuário** e **custo por interação** (seção 9).

### Decisão rápida — Fundamentos de IA generativa

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Unidade usada para medir contexto e preço | Token | Caractere, palavra |
| Representação numérica do significado de um texto | Embedding | Token, chunk |
| Dividir documentos antes de indexar | Chunking | Tokenização, fine-tuning |
| Arquitetura base dos LLMs | Transformer | Modelo de difusão |
| Gerar imagens partindo de ruído | Modelo de difusão | Transformer de texto |
| Modelo que entende texto e imagem | Multimodal | Embeddings de texto |
| Resposta plausível mas falsa | Alucinação | Overfitting |
| Mesma pergunta, respostas diferentes | Não determinismo | Alucinação |
| Reduzir custo de prompts que repetem o mesmo prefixo | Prompt caching | Modelo maior |
| Decidir o que entra na janela de contexto a cada chamada | Engenharia de contexto | Fine-tuning |
| Etapa do ciclo do FM que especializa o modelo | Fine-tuning | Pré-treinamento |

---

## 5. IA Agêntica e Agentes

> **Regra de ouro da prova**: um **agente** combina um **modelo** (raciocínio), **ferramentas** (agir no mundo), **memória** (lembrar) e um **loop de orquestração** (planejar → agir → observar → repetir) para cumprir um objetivo com autonomia. **MCP** padroniza como agentes se conectam a ferramentas e dados. Na AWS, o SDK é o **Strands Agents** e a plataforma de execução é o **Amazon Bedrock AgentCore**.

### Conceitos fundamentais de IA agêntica

#### O que compõe um agente

| Componente | Papel |
|---|---|
| **Modelo (FM)** | Raciocina, planeja e decide o próximo passo |
| **Instruções** | Objetivo, papel e limites do agente (system prompt) |
| **Ferramentas** (tool use / function calling) | Funções que o agente pode chamar: APIs, bancos de dados, busca, execução de código, navegador |
| **Memória** | **Curto prazo**: contexto da conversa ou tarefa atual. **Longo prazo**: fatos e preferências que persistem entre sessões |
| **Orquestração do fluxo** | O loop que decide a ordem das ações, trata erros, pede confirmação e sabe quando parar |

- **Diferença para um chatbot**: o chatbot responde; o agente **executa** tarefas de várias etapas (consultar um pedido, abrir um chamado, reagendar uma entrega), decidindo quais ferramentas usar.
- **Humano no loop**: agentes que executam ações sensíveis devem pedir **aprovação humana** antes de agir (ex.: estornar um pagamento).

#### Model Context Protocol (MCP)
- **Protocolo aberto** que padroniza como aplicações de IA e agentes se conectam a **ferramentas, dados e sistemas externos**.
- Arquitetura **cliente-servidor**: o agente (cliente MCP) descobre e chama as ferramentas expostas por um **servidor MCP** (ex.: um servidor que expõe o sistema de tickets, o banco de dados ou uma API interna).
- **Benefício**: escrever a integração **uma vez** e reutilizá-la em vários agentes e modelos, em vez de criar um conector próprio para cada combinação. Costuma ser comparado a uma "porta USB-C" para IA.
- Na AWS, o **AgentCore Gateway** transforma APIs, funções Lambda e serviços existentes em **ferramentas compatíveis com MCP**.
- **Agent-to-Agent (A2A)** é outro protocolo aberto, voltado à **comunicação entre agentes**; MCP conecta agente a ferramenta.

#### Padrões de sistemas multiagente

| Padrão | Como funciona | Quando usar |
|---|---|---|
| **Supervisor / orquestrador** | Um agente central divide a tarefa e delega a agentes especialistas, depois consolida | Tarefas complexas com partes bem definidas |
| **Agentes como ferramentas** (agents-as-tools) | Um agente chama outros agentes como se fossem ferramentas | Reaproveitar especialistas de forma simples |
| **Swarm (enxame)** | Agentes colaboram de forma autônoma, passando o controle entre si | Problemas exploratórios que se beneficiam de várias perspectivas |
| **Grafo / workflow** | Agentes em um fluxo com ordem e condições definidas | Processos previsíveis e auditáveis |

- **Padrões de comunicação**: hierárquica (supervisor), ponto a ponto, memória ou estado compartilhado e troca de mensagens (A2A).
- **Riscos**: mais agentes significam mais custo (tokens), mais latência e mais pontos de falha. Use multiagente só quando um agente não resolve bem.

#### Aplicações de negócio de agentes
- **Atendimento ao cliente** que consulta pedidos, altera cadastros e abre chamados.
- **Operações de TI**: investigar incidentes, consultar logs e sugerir correções.
- **Assistentes de pesquisa** que buscam, leem e sintetizam várias fontes.
- **Automação de processos**: aprovações, conciliações e preenchimento de sistemas.
- **Desenvolvimento de software**: planejar, escrever, testar e revisar código (Kiro).
- **Modernização e migração** de aplicações legadas (AWS Transform).

### Serviços AWS para agentes

#### Amazon Bedrock AgentCore
Plataforma agêntica para **construir, implantar e operar agentes com segurança e em escala**, com **qualquer framework** (Strands Agents, LangGraph, CrewAI, LlamaIndex e outros) e **qualquer modelo**, dentro ou fora do Bedrock, **sem gerenciar infraestrutura**. Os serviços funcionam juntos ou separados:

| Componente | Função |
|---|---|
| **Runtime** | Ambiente **serverless** e seguro para executar agentes e ferramentas, com isolamento de sessão e suporte a tarefas longas |
| **Harness** | Loop de agente **gerenciado**: declare modelo, prompt e ferramentas e invoque com uma chamada de API. É o substituto recomendado do Bedrock Agents Classic |
| **Memory** | Memória de **curto prazo** (conversa) e **longo prazo** (persistente entre sessões) |
| **Gateway** | Converte APIs, funções Lambda e serviços em **ferramentas MCP** e conecta servidores MCP existentes |
| **Identity** | Identidade, acesso e autenticação **do agente**, compatível com provedores existentes (Cognito, Okta, Entra ID) |
| **Policy** | Regras **determinísticas** que limitam quais ferramentas e ações o agente pode usar e em quais condições; intercepta cada chamada de ferramenta no Gateway |
| **Code Interpreter** | Sandbox isolado para o agente **executar código** |
| **Browser** | Navegador na nuvem para o agente **interagir com sites** |
| **Observability** | Rastreamento e depuração de cada passo do agente (compatível com OpenTelemetry, integrado ao CloudWatch) |
| **Evaluations** | Avaliação automatizada da qualidade do agente e das ferramentas |

- **Cobrança por consumo**, sem compromisso inicial.

#### Strands Agents, Kiro e outros serviços agênticos

| Serviço | O que é | Quando é a resposta |
|---|---|---|
| **Strands Agents** | **SDK open source** (Apache 2.0) da AWS, em **Python e TypeScript**, para construir agentes com abordagem **orientada ao modelo**: você define um prompt e uma lista de ferramentas, e o modelo planeja e chama as ferramentas. Suporta MCP, A2A, padrões multiagente, memória e qualquer provedor de modelo | "Framework/SDK para escrever agentes em código" |
| **Kiro** | **Plataforma de desenvolvimento agêntico** da AWS (IDE, CLI e outras interfaces) com **desenvolvimento orientado a especificações** (spec-driven): transforma o pedido em requisitos, design e tarefas antes de gerar código. Tem *steering files*, *agent hooks* e suporte a MCP. **Substitui o Amazon Q Developer** | "Assistente de IA para desenvolver software", "IDE agêntica" |
| **Amazon Quick** | **Espaço de trabalho de IA agêntica** para usuários de negócio: chat, pesquisa, **Quick Sight** (BI), fluxos (Quick Flows), automação e agentes conectados a dados e aplicações da empresa. Sucessor do Amazon Q Business e do QuickSight | "Funcionários perguntando e automatizando tarefas com dados da empresa", "dashboards com IA" |
| **AWS Transform** | Serviço de **IA agêntica para migração e modernização**: VMware, mainframe, .NET/Windows, upgrades de Java e redução de dívida técnica | "Modernizar aplicações legadas com agentes de IA" |
| **Amazon Nova Act** | Serviço para criar **agentes que automatizam fluxos em interfaces web** (navegador) | "Agente que opera um site como um usuário" |
| **Amazon Bedrock Agents (Classic)** | Agentes gerenciados do Bedrock com action groups e Knowledge Bases. **Em manutenção desde 30/jul/2026**; novas contas devem usar o **AgentCore** | Aparece em simulados antigos como resposta para "agentes que executam tarefas em várias etapas" |

### Decisão rápida — IA agêntica

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Assistente que consulta sistemas e executa tarefas em várias etapas | Agente de IA | Chatbot simples, modelo de classificação |
| Padrão aberto para conectar agentes a ferramentas e dados | Model Context Protocol (MCP) | A2A, REST genérico |
| Padrão aberto de comunicação entre agentes | Agent-to-Agent (A2A) | MCP |
| Executar agentes em produção sem gerenciar infraestrutura | Amazon Bedrock AgentCore (Runtime) | EC2, Bedrock Agents Classic para novos clientes |
| Transformar APIs e funções Lambda em ferramentas MCP | AgentCore Gateway | API Gateway sozinho |
| Memória do agente entre sessões | AgentCore Memory | S3 genérico, cache |
| Limitar deterministicamente as ações do agente | Policy in AgentCore | Prompt pedindo para não fazer |
| Identidade e autenticação do agente | AgentCore Identity | Chave fixa no código |
| Agente que executa código com segurança | AgentCore Code Interpreter | Lambda sem isolamento |
| Rastrear cada passo do agente | AgentCore Observability | CloudTrail sozinho |
| SDK open source para escrever agentes em Python/TypeScript | Strands Agents | SageMaker Pipelines |
| IDE agêntica com desenvolvimento orientado a especificações | Kiro | Amazon Q Business, CodeBuild |
| Agentes e BI para usuários de negócio | Amazon Quick | SageMaker Canvas |
| Modernizar mainframe e .NET com agentes | AWS Transform | Application Migration Service |
| Supervisor que delega a especialistas | Padrão multiagente supervisor | Swarm |

---

## 6. Serviços AWS para IA Generativa

> **Regra de ouro da prova**: **Amazon Bedrock** é a resposta para "usar foundation models de vários provedores **por API, sem gerenciar infraestrutura**", com Knowledge Bases (RAG), Guardrails, avaliação e customização. **SageMaker AI / JumpStart** é a resposta quando se quer **mais controle** para implantar, ajustar ou treinar modelos na própria infraestrutura gerenciada.

### Amazon Bedrock

#### O que é e o que oferece
- Serviço **totalmente gerenciado e serverless** que dá acesso, por **uma única API**, a foundation models de vários provedores: **Amazon Nova**, Anthropic (Claude), Meta (Llama), Mistral, Cohere, AI21, Stability AI, DeepSeek, OpenAI (modelos open-weight) e outros.
- **Privacidade**: seus prompts e dados **não são usados para treinar os modelos base** nem compartilhados com os provedores dos modelos. Os dados ficam na Região escolhida, criptografados em trânsito e em repouso (com chaves do KMS), e o acesso pode ser privado via **AWS PrivateLink**.

| Recurso do Bedrock | Para que serve |
|---|---|
| **Playgrounds** | Testar modelos e prompts no console |
| **Knowledge Bases** | **RAG gerenciado**: ingere documentos (S3 e outras fontes), faz chunking, gera embeddings, guarda em banco vetorial e recupera trechos com citações |
| **Guardrails** | Filtros de conteúdo, tópicos negados, filtros de palavras, **PII**, verificação de fundamentação (grounding) e verificações de raciocínio automatizado (seção 10) |
| **Model Evaluation** | Avaliar e comparar modelos e aplicações RAG com métricas automáticas, **LLM como juiz** ou **avaliadores humanos** |
| **Prompt Management** | Criar, **versionar**, testar e reutilizar prompts (seção 8) |
| **Flows** | Encadear prompts, modelos, Knowledge Bases e funções em fluxos visuais |
| **Data Automation** | Extrair insights de documentos, imagens, áudio e vídeo não estruturados com IA generativa |
| **Customização de modelos** | **Fine-tuning**, **continued pre-training**, **destilação** e importação de modelos customizados |
| **Batch inference** | Processar grandes volumes de forma assíncrona com **preço menor** que o on-demand |
| **Cross-Region inference** | Distribuir requisições entre Regiões para mais capacidade e resiliência |
| **Prompt caching** e **Intelligent Prompt Routing** | Reduzir custo e latência com cache de prefixos e roteamento entre modelos de uma família conforme a complexidade |
| **Bedrock Marketplace** | Descobrir e implantar modelos adicionais especializados |

#### Família Amazon Nova

| Modelo | Tipo | Uso |
|---|---|---|
| **Nova Micro** | Compreensão, **só texto** | Menor latência e custo |
| **Nova Lite** | Compreensão multimodal (texto, imagem, vídeo) | Muito baixo custo e rápido |
| **Nova Pro** | Compreensão multimodal | Melhor equilíbrio entre precisão, velocidade e custo |
| **Nova Premier** | Compreensão multimodal | Mais capaz, tarefas complexas; também serve de "professor" na destilação |
| **Nova Canvas** | Criativo | **Geração e edição de imagens** |
| **Nova Reel** | Criativo | **Geração de vídeos** |
| **Nova Sonic** | Fala | Conversa **fala para fala** em tempo real |
| **Nova 2** (Lite, Sonic e outros) | Nova geração | Raciocínio e fala com melhor custo-benefício |

- Também existem **Amazon Nova Act** (agentes de navegador) e **Amazon Nova Forge** (criar modelos próprios a partir do Nova). **Amazon Titan Embeddings** e **Nova Multimodal Embeddings** geram embeddings para RAG.

### SageMaker AI, JumpStart e outros serviços

#### Amazon SageMaker AI e SageMaker JumpStart
- **SageMaker JumpStart**: hub de **centenas de modelos pré-treinados e FMs** (inclusive open-weight) para **implantar em endpoints do SageMaker AI** e **ajustar** com seus dados, com poucos cliques. Você escolhe a instância e controla a infraestrutura do endpoint.
- **SageMaker AI**: para **treinar modelos próprios**, fazer fine-tuning avançado, pré-treinar e hospedar com controle total. Chips **AWS Trainium** (treino) e **AWS Inferentia** (inferência) reduzem custo e consumo de energia.
- **Bedrock vs. JumpStart**: Bedrock = API serverless, paga por token, sem gerenciar instâncias. JumpStart = modelo em **endpoint dedicado**, paga pela instância, mais controle.

#### Amazon Q e a transição para Kiro e Amazon Quick
- **Amazon Q Developer**: assistente de IA generativa para desenvolvedores (código, testes, transformação, operações na AWS). Novas assinaturas bloqueadas desde **15/mai/2026**; suporte até **30/abr/2027**. O sucessor é o **Kiro**.
- **Amazon Q Business**: assistente para funcionários com base nos dados da empresa. **Em manutenção desde 30/jul/2026**; o sucessor é o **Amazon Quick**.
- Em simulados, "Amazon Q" ainda aparece como resposta para "assistente de IA generativa pronto para desenvolvedores ou funcionários". Reconheça o conceito e saiba os sucessores.

#### Vantagens dos serviços de IA generativa da AWS
- **Acessibilidade e menor barreira de entrada**: usar FMs sem especialistas em ML nem treinamento.
- **Eficiência e custo-benefício**: pagar pelo uso, sem infraestrutura ociosa.
- **Velocidade de lançamento** (speed to market): protótipos em dias.
- **Capacidade de atender aos objetivos de negócio** com escolha de modelos e customização.
- **Benefícios da infraestrutura AWS**: **segurança** (IAM, KMS, PrivateLink, isolamento de dados), **conformidade** (programas e certificações, inclusive **ISO/IEC 42001** para gestão de IA), **responsabilidade compartilhada** clara e **segurança do conteúdo** (Guardrails).

### Custos e trade-offs

#### Opções de preço e fatores de custo

| Opção | Como cobra | Quando usar |
|---|---|---|
| **On-demand** (Bedrock) | Por **token** de entrada e saída, sem compromisso | Uso variável, protótipos, maioria das aplicações |
| **Batch inference** (Bedrock) | Por token, com **desconto** em relação ao on-demand | Grandes volumes sem necessidade de resposta imediata |
| **Provisioned Throughput** (Bedrock) | Por **unidade de modelo por hora**, com ou sem compromisso de prazo | **Throughput garantido** para cargas altas e previsíveis; em geral necessário para **modelos customizados** |
| **Modelos customizados** | Custo do **treinamento** (tokens processados) + **armazenamento** mensal do modelo + inferência | Quando prompt e RAG não bastam |
| **Endpoints do SageMaker AI** | Por **hora de instância**, usada ou não (exceto serverless) | Controle total e modelos auto-hospedados |

- **Trade-offs cobrados**: **responsividade** (latência) vs. custo; **disponibilidade e redundância** (cross-Region inference, várias Regiões) vs. custo; **desempenho** (modelo maior) vs. custo por token; **cobertura regional** (nem todo modelo existe em toda Região); **token-based** vs. **throughput provisionado**; custo extra de **modelos customizados**.

### Decisão rápida — Serviços de IA generativa

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Usar FMs de vários provedores por API sem gerenciar servidores | Amazon Bedrock | SageMaker AI, EC2 com GPU |
| Implantar um modelo open-weight em endpoint próprio com poucos cliques | SageMaker JumpStart | Bedrock on-demand |
| Treinar um modelo do zero com controle total | SageMaker AI | Bedrock Playground |
| RAG gerenciado com citações | Bedrock Knowledge Bases | Fine-tuning |
| Bloquear tópicos e filtrar PII nas respostas | Bedrock Guardrails | IAM, Macie |
| Comparar modelos com métricas e avaliadores humanos | Bedrock Model Evaluation | CloudWatch |
| Versionar prompts | Bedrock Prompt Management | CodeCommit, S3 |
| Gerar imagens com modelo da Amazon | Amazon Nova Canvas | Nova Reel, Rekognition |
| Gerar vídeos com modelo da Amazon | Amazon Nova Reel | Nova Canvas |
| Menor latência e custo para texto simples | Amazon Nova Micro | Nova Premier |
| Processar milhões de prompts sem urgência, mais barato | Bedrock batch inference | Provisioned Throughput |
| Throughput garantido para carga alta e previsível | Provisioned Throughput | On-demand |
| Assistente de código (novo cliente em 2026) | Kiro | Amazon Q Developer |
| Assistente para funcionários com dados da empresa (novo cliente em 2026) | Amazon Quick | Amazon Q Business |
| Dados do prompt usados para treinar o modelo base? | Não, no Bedrock | Sim |

---

## 7. Aplicações com Foundation Models: Design, RAG e Customização

> **Regra de ouro da prova**: a escada de customização, da mais barata à mais cara: **engenharia de prompt / in-context learning → RAG → fine-tuning → continued pre-training → pré-treinamento do zero**. **RAG** traz **conhecimento** novo e atualizado sem retreinar; **fine-tuning** muda o **comportamento** (tom, formato, tarefa específica). **Destilação** cria um modelo menor e mais barato a partir de um maior.

### Critérios de seleção e parâmetros de inferência

#### Critérios para escolher um FM

| Critério | Pergunta que ele responde |
|---|---|
| **Custo** | Quanto custa por token ou por hora, no volume esperado? |
| **Modalidade** | Precisa de texto, imagem, vídeo, áudio ou embeddings? |
| **Latência** | A aplicação é interativa (chat) ou pode esperar (lote)? |
| **Multilíngue** | Precisa atender em português e em outros idiomas? |
| **Tamanho do modelo** | Um modelo menor atende? Modelos menores são mais rápidos e baratos |
| **Complexidade do modelo** | A tarefa exige raciocínio avançado ou é simples (classificar, extrair)? |
| **Customização** | O modelo suporta fine-tuning ou destilação no Bedrock? |
| **Tamanho de entrada e saída** | A janela de contexto comporta os documentos? Qual o máximo de tokens de saída? |
| **Prompt caching** | O modelo suporta cache de prompt para reduzir custo e latência? |
| **Conformidade e licença** | Termos de uso, disponibilidade na Região exigida, origem dos dados de treino |

#### Parâmetros de inferência

| Parâmetro | Efeito | Na prática |
|---|---|---|
| **Temperatura** | Controla a **aleatoriedade**. Baixa (perto de 0) = respostas mais **previsíveis e focadas**; alta = mais **criativas e variadas** | Baixa para respostas factuais, extração e código; alta para brainstorming e textos criativos |
| **Top P** (nucleus sampling) | Considera só os tokens cuja probabilidade acumulada chega a P | Valor menor = respostas mais conservadoras |
| **Top K** | Considera só os K tokens mais prováveis | K menor = menos variedade |
| **Comprimento máximo** (max tokens) | Limita o tamanho da **resposta** | Controla custo e latência; resposta pode ser cortada |
| **Sequências de parada** (stop sequences) | Texto que faz o modelo parar de gerar | Delimitar formatos |
| **Tamanho da entrada** | Mais contexto = mais custo e latência, e o limite é a janela de contexto | Envie só o necessário |

### Retrieval Augmented Generation (RAG)

#### Como o RAG funciona
**RAG** busca informações relevantes em uma fonte de conhecimento externa **no momento da pergunta** e as inclui no prompt, para que o modelo responda **com base nesses dados**. Etapas (cobradas em questões de ordenação):

1. **Ingestão**: coletar os documentos da empresa (S3, sites, Confluence, SharePoint…).
2. **Chunking**: dividir os documentos em pedaços.
3. **Embeddings**: converter cada pedaço em vetor com um modelo de embeddings.
4. **Armazenamento**: gravar os vetores em um **banco vetorial**.
5. **Consulta**: converter a pergunta do usuário em embedding.
6. **Recuperação**: buscar os pedaços mais **semelhantes** à pergunta.
7. **Aumento**: inserir os trechos recuperados no prompt.
8. **Geração**: o FM responde usando o contexto, idealmente **com citações**.

#### Benefícios e aplicações de negócio
- Responde com **dados privados e atualizados** sem retreinar o modelo; basta atualizar a base.
- **Reduz alucinações** e permite **citar as fontes** (transparência e auditoria).
- **Mais barato e rápido** que fine-tuning para injetar conhecimento.
- Respeita permissões quando a recuperação filtra por metadados e perfil do usuário.
- **Aplicações**: assistentes de RH e políticas internas, suporte técnico sobre manuais, atendimento com base em catálogos, pesquisa jurídica, análise de contratos.
- **Na AWS**: **Amazon Bedrock Knowledge Bases** faz o RAG de ponta a ponta (ingestão, chunking, embeddings, armazenamento, recuperação e geração com citações).

#### Bancos vetoriais na AWS

| Serviço | Como guarda embeddings |
|---|---|
| **Amazon OpenSearch Service** (e OpenSearch Serverless) | Mecanismo vetorial (k-NN) com busca híbrida (palavra-chave + semântica). Opção padrão de Knowledge Bases |
| **Amazon Aurora PostgreSQL** | Extensão **pgvector**; bom quando a aplicação já usa PostgreSQL |
| **Amazon RDS for PostgreSQL** | Extensão **pgvector** |
| **Amazon Neptune** (Neptune Analytics) | Busca vetorial combinada com **grafos** (GraphRAG) |
| **Amazon DocumentDB** | Busca vetorial em documentos JSON |
| **Amazon S3 Vectors** | Armazenamento vetorial de baixo custo no S3 para grandes volumes |

### Abordagens de customização

#### Comparação de custo e esforço

| Abordagem | O que muda | Custo e esforço | Quando usar |
|---|---|---|---|
| **Engenharia de prompt / in-context learning** | Só o prompt (instruções e exemplos) | **Menor**: nenhum treinamento | Sempre o primeiro passo |
| **RAG** | O **contexto** enviado ao modelo | Baixo a médio: banco vetorial, embeddings, tokens de contexto | Conhecimento **privado ou que muda** com frequência |
| **Fine-tuning** | Os **pesos** do modelo, com dados **rotulados** (pares prompt-resposta) | Médio a alto: dados, treinamento, hospedagem do modelo customizado | Estilo, tom, formato ou tarefa específica que o prompt não resolve |
| **Continued pre-training** | Os pesos, com grandes volumes de dados **não rotulados** do domínio | Alto | Vocabulário e conhecimento de um domínio (jurídico, médico, financeiro) |
| **Destilação** (distillation) | Um modelo **aluno** menor aprende com as respostas de um modelo **professor** maior | Médio (treinamento), mas **reduz o custo e a latência de inferência** | Precisa da qualidade do modelo grande com custo de um pequeno |
| **Pré-treinamento do zero** | Cria um FM novo | **Maior** de todos: dados massivos, meses, muita computação | Raramente; organizações com necessidades e recursos excepcionais |

- **Armadilha**: fine-tuning **não** é a melhor forma de ensinar fatos que mudam toda semana. O modelo "congela" o conhecimento no treino; use **RAG**.
- **Armadilha**: RAG não muda o **estilo** do modelo; se o problema é tom ou formato, tente prompt e, depois, fine-tuning.

### Agentes em aplicações

#### O papel dos agentes no design
- Use um agente quando a aplicação precisa **executar ações** ou **combinar várias fontes e ferramentas** em várias etapas, não só responder.
- Um agente pode usar **RAG como uma de suas ferramentas** (consultar a base de conhecimento) ao lado de APIs e bancos de dados.
- Mais autonomia = mais risco: combine com **Guardrails**, **Policy in AgentCore**, permissões mínimas e **aprovação humana** para ações sensíveis. Veja a seção 5.

### Decisão rápida — Design, RAG e customização

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Respostas factuais e consistentes | Temperatura baixa | Temperatura alta |
| Textos criativos e variados | Temperatura alta | Temperatura 0 |
| Limitar custo e tamanho das respostas | Max tokens menor | Temperatura |
| Responder com políticas internas que mudam toda semana | RAG (Bedrock Knowledge Bases) | Fine-tuning, pré-treinamento |
| Citar a fonte da resposta | RAG com citações | Temperatura baixa |
| Modelo deve responder sempre no tom e formato da marca | Fine-tuning (após tentar prompt) | RAG |
| Ensinar vocabulário de um domínio com dados não rotulados | Continued pre-training | Fine-tuning com poucos exemplos |
| Qualidade de modelo grande com custo de modelo pequeno | Destilação | Pré-treinamento |
| Opção de customização de menor custo | Engenharia de prompt / in-context learning | Fine-tuning |
| Opção de customização mais cara | Pré-treinar do zero | RAG |
| Guardar embeddings junto de um banco PostgreSQL existente | Aurora/RDS PostgreSQL com pgvector | DynamoDB |
| Busca vetorial gerenciada padrão para RAG | Amazon OpenSearch Service | Redshift |
| Combinar grafos e vetores | Amazon Neptune | RDS |
| Primeira etapa do RAG | Ingestão e chunking dos documentos | Geração |

---

## 8. Engenharia de Prompts

> **Regra de ouro da prova**: um bom prompt é **específico, conciso e estruturado**: diz **o que fazer** (instrução), **com quais informações** (contexto e dados de entrada), **em que formato** (saída) e, quando útil, **com exemplos** (few-shot). **Prompt injection** e **jailbreaking** são os riscos mais cobrados; **Guardrails** e validação de entrada e saída são a defesa.

### Construção de prompts

#### Elementos de um prompt

| Elemento | Exemplo |
|---|---|
| **Instrução** | "Resuma o texto abaixo em três tópicos." |
| **Contexto** | "Você é um analista financeiro escrevendo para a diretoria." |
| **Dados de entrada** | O texto, o documento ou a pergunta do usuário |
| **Indicador de saída** (formato) | "Responda em JSON com os campos titulo e resumo." |
| **Exemplos** | Pares de entrada e saída esperada (few-shot) |
| **Prompt negativo** | O que o modelo **não** deve fazer ou incluir: "Não cite concorrentes." Em geração de imagens, elementos a evitar ("sem texto, sem pessoas") |
| **System prompt** | Instruções persistentes que definem papel, tom e limites da aplicação |

### Técnicas de prompt

#### Técnicas cobradas

| Técnica | Como funciona | Quando usar |
|---|---|---|
| **Zero-shot** | Só a instrução, **sem exemplos** | Tarefas simples e comuns |
| **Single-shot / one-shot** | **Um** exemplo de entrada e saída | Mostrar o formato esperado |
| **Few-shot** | **Alguns** exemplos | Tarefas com padrão específico (classificar tickets nas categorias da empresa) |
| **Chain-of-thought (CoT)** | Pedir que o modelo **raciocine passo a passo** antes de responder | Problemas de lógica, matemática e várias etapas |
| **Templates de prompt** | Estruturas reutilizáveis com **variáveis** preenchidas em tempo de execução | Padronizar e escalar prompts na aplicação |

- **In-context learning** é o nome geral para o modelo "aprender" a tarefa pelos exemplos no próprio prompt, **sem alterar os pesos**. Zero-shot, one-shot e few-shot são formas de in-context learning.

#### Benefícios e boas práticas
- **Melhora a qualidade da resposta** sem custo de treinamento.
- **Experimentação**: teste variações e compare resultados (Bedrock Playground, Prompt Management, Model Evaluation).
- **Guardrails**: combine prompts com controles de segurança.
- **Descoberta**: explorar o que o modelo sabe fazer.
- **Especificidade e concisão**: instruções claras, sem ambiguidade; peça o formato exato.
- **Divida em várias instruções**: separe tarefas complexas em passos ou em prompts encadeados.
- Coloque as instruções em posição clara, delimite os dados de entrada (tags, aspas) e peça que o modelo diga "não sei" quando a resposta não estiver no contexto.

### Riscos e gerenciamento de prompts

#### Riscos e limitações

| Risco | O que é | Defesa |
|---|---|---|
| **Prompt injection** | Texto malicioso (do usuário ou de um documento recuperado) tenta **sobrescrever as instruções** do sistema | Guardrails (filtro de ataque de prompt), separar instruções de dados, validar entradas e saídas, menor privilégio para ferramentas |
| **Hijacking** (sequestro) | Desviar o modelo para outra tarefa ou objetivo | Instruções firmes no system prompt, tópicos negados |
| **Jailbreaking** | Contornar as proteções de segurança do modelo com truques (encenação, cenários hipotéticos) | Guardrails, avaliação adversarial (red teaming) |
| **Exposição / vazamento** (exposure, leaking) | Fazer o modelo revelar o **system prompt**, dados sensíveis ou informações de outros usuários | Não colocar segredos no prompt, filtros de PII, controle de acesso na recuperação |
| **Envenenamento** (poisoning) | Inserir dados maliciosos nos **dados de treino** ou na **base de conhecimento** para manipular respostas | Curadoria e validação das fontes, controle de quem escreve na base |

#### Amazon Bedrock Prompt Management
- Cria, testa, **versiona** e compartilha prompts reutilizáveis com **variáveis**, modelo e parâmetros de inferência associados.
- **Versões imutáveis** permitem comparar, voltar a uma versão anterior e promover um prompt aprovado para produção sem mudar o código da aplicação.
- Integra-se ao **Bedrock Flows** e aos testes comparativos entre variantes de prompt.
- **Estratégia recomendada**: tratar prompts como código: versionar, revisar, testar com um conjunto de avaliação e registrar qual versão está em produção.

### Decisão rápida — Engenharia de prompts

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Pedir a tarefa sem exemplos | Zero-shot | Few-shot |
| Fornecer vários exemplos no prompt | Few-shot | Fine-tuning |
| Fazer o modelo raciocinar passo a passo | Chain-of-thought | Zero-shot |
| Reutilizar prompts com variáveis | Templates de prompt | Fine-tuning |
| Aprender a tarefa pelo prompt sem mudar pesos | In-context learning | Fine-tuning |
| Dizer o que o modelo não deve incluir | Prompt negativo | Temperatura |
| Usuário tenta "ignore as instruções anteriores" | Prompt injection | Alucinação |
| Truque para contornar as proteções do modelo | Jailbreaking | Poisoning |
| Documentos maliciosos inseridos na base de conhecimento | Poisoning | Jailbreaking |
| Modelo revela o system prompt | Exposição / vazamento | Hijacking |
| Versionar e gerenciar prompts no Bedrock | Bedrock Prompt Management | S3, Git sozinho |
| Bloquear ataques de prompt | Bedrock Guardrails | IAM, KMS |

---

## 9. Treinamento, Fine-tuning e Avaliação de FMs

> **Regra de ouro da prova**: **pré-treinamento** usa dados enormes **não rotulados** (autossupervisionado); **fine-tuning** usa dados **rotulados** menores para uma tarefa; **continued pre-training** usa dados **não rotulados do domínio**; **destilação** transfere conhecimento de um modelo grande para um pequeno. Na avaliação: **ROUGE** para **resumo**, **BLEU** para **tradução**, **BERTScore** para **similaridade semântica**, **LLM como juiz** para critérios subjetivos em escala.

### Treinamento e fine-tuning

#### Elementos do treinamento de um FM

| Elemento | Dados | Objetivo |
|---|---|---|
| **Pré-treinamento** | Volumes massivos e amplos, **não rotulados** | Aprender linguagem e conhecimento geral (autossupervisionado) |
| **Fine-tuning** | Conjunto menor e **rotulado** (pares prompt-resposta) | Adaptar a uma tarefa, estilo ou formato |
| **Continued pre-training** (pré-treinamento contínuo) | Grandes volumes **não rotulados** de um domínio | Adaptar o modelo ao vocabulário e ao conhecimento do domínio |
| **Destilação** | Respostas geradas por um modelo **professor** | Criar um modelo **aluno** menor, mais rápido e mais barato |

#### Métodos de fine-tuning
- **Instruction tuning**: treinar com exemplos de **instruções e respostas**, para o modelo seguir melhor pedidos.
- **Adaptação de domínio**: especializar em uma área (jurídica, médica, atendimento de uma empresa).
- **Transfer learning**: reaproveitar o conhecimento de um modelo pré-treinado e ajustá-lo a uma tarefa nova com poucos dados. É o princípio por trás de todo fine-tuning de FMs.
- **Continued pre-training**: continuar o pré-treinamento com dados do domínio.
- **Técnicas eficientes** (PEFT, como LoRA): ajustam só uma pequena parte dos parâmetros, reduzindo custo.

#### Preparação de dados para fine-tuning
- **Curadoria**: selecionar exemplos corretos, relevantes e sem duplicatas.
- **Governança**: origem conhecida, direitos de uso, privacidade (remover ou mascarar PII) e conformidade.
- **Tamanho**: dados suficientes para a tarefa; qualidade vale mais que quantidade.
- **Rotulagem**: rótulos consistentes e revisados.
- **Representatividade**: cobrir os casos, idiomas e grupos que o modelo vai atender, evitando viés.
- **RLHF (reinforcement learning from human feedback)**: humanos **classificam ou comparam** respostas; um modelo de recompensa aprende essas preferências e orienta o ajuste. Alinha o modelo a respostas **úteis, honestas e seguras**.

### Avaliação de foundation models

#### Abordagens de avaliação

| Abordagem | Como funciona | Pontos fortes |
|---|---|---|
| **Avaliação com humano no loop** | Pessoas avaliam respostas por critérios (utilidade, correção, tom) | Captura nuances e qualidade percebida; mais cara e lenta |
| **Conjuntos de dados de benchmark** | Conjuntos padronizados de perguntas e respostas esperadas | Comparação objetiva e repetível entre modelos |
| **Amazon Bedrock Model Evaluation** | Avaliação **automática** (métricas e conjuntos prontos ou próprios), **LLM como juiz** e **com equipes humanas** (suas ou gerenciadas); também avalia aplicações RAG | Comparar modelos e configurações na AWS |

#### Métricas de avaliação de FMs

| Métrica | O que mede | Tarefa típica |
|---|---|---|
| **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) | Sobreposição de palavras e sequências entre o texto gerado e uma referência, com foco em **recall** | **Resumo** |
| **BLEU** (Bilingual Evaluation Understudy) | Sobreposição de n-gramas com foco em **precisão** em relação a traduções de referência | **Tradução** |
| **BERTScore** | **Similaridade semântica** usando embeddings; reconhece paráfrases com palavras diferentes | Qualidade de texto quando o significado importa mais que as palavras exatas |
| **LLM como juiz** (LLM-as-a-judge) | Um modelo avalia as respostas de outro segundo critérios definidos (correção, relevância, completude, nocividade) | Avaliação em escala de critérios subjetivos |
| **Perplexidade** | Quão "surpreso" o modelo fica com um texto (menor é melhor) | Qualidade de modelos de linguagem |
| **Acurácia / F1** | Acertos em tarefas com resposta fechada | Classificação, extração, perguntas objetivas |

#### Avaliar aplicações e alinhamento com o negócio
- **Aplicações RAG**: avalie a **recuperação** (os trechos certos foram encontrados?) e a **geração** (a resposta é **fiel ao contexto** — faithfulness/groundedness — e relevante?). O Bedrock avalia Knowledge Bases.
- **Agentes**: taxa de conclusão de tarefas, uso correto de ferramentas, número de passos, custo por tarefa. **AgentCore Evaluations** automatiza essas medições.
- **Fluxos (workflows)**: sucesso de ponta a ponta, latência e custo de cada etapa.
- **O FM atende ao objetivo de negócio?** Meça **produtividade**, **engajamento do usuário** e a execução correta das tarefas.
- **Métricas de alinhamento com o negócio**: **taxa de conclusão de tarefas**, **satisfação do usuário** (CSAT, avaliações) e **custo por interação**.

### Decisão rápida — Treinamento e avaliação

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Aprender linguagem geral com dados massivos não rotulados | Pré-treinamento | Fine-tuning |
| Adaptar com pares de instrução e resposta rotulados | Fine-tuning (instruction tuning) | Continued pre-training |
| Adaptar ao domínio com muitos documentos não rotulados | Continued pre-training | Fine-tuning supervisionado |
| Reaproveitar um modelo pré-treinado para nova tarefa | Transfer learning | Treinar do zero |
| Alinhar respostas a preferências humanas | RLHF | Clustering |
| Modelo menor que imita um maior | Destilação | Pré-treinamento |
| Avaliar qualidade de resumos | ROUGE | BLEU |
| Avaliar qualidade de traduções | BLEU | ROUGE |
| Comparar significado mesmo com palavras diferentes | BERTScore | BLEU |
| Avaliar critérios subjetivos em escala com um modelo | LLM como juiz | ROUGE |
| Avaliação padronizada e repetível entre modelos | Benchmark datasets | Avaliação ad hoc |
| Avaliar tom e utilidade percebida | Avaliação humana | Métricas automáticas |
| Avaliar modelos e RAG na AWS | Bedrock Model Evaluation | CloudWatch, Config |
| Métrica de negócio para um assistente de atendimento | Taxa de conclusão de tarefas / custo por interação | Perplexidade |

---

## 10. IA Responsável

> **Regra de ouro da prova**: IA responsável é garantir que o sistema seja **justo, explicável, seguro, robusto, privado, controlável, transparente e bem governado**. Para **filtrar conteúdo nocivo e bloquear tópicos** em IA generativa, a resposta é **Amazon Bedrock Guardrails**. Para **detectar viés e explicar previsões** de modelos de ML, a resposta clássica é **SageMaker Clarify**. Para **documentar** o modelo, **SageMaker Model Cards**.

### Características da IA responsável

#### Dimensões da IA responsável
O guia do exame cita **viés, justiça, inclusão, robustez, segurança e veracidade**. A AWS organiza a IA responsável em oito dimensões:

| Dimensão | Significado |
|---|---|
| **Justiça** (fairness) | Considerar o impacto em diferentes grupos de pessoas e evitar discriminação |
| **Explicabilidade** (explainability) | Entender e avaliar as saídas do sistema |
| **Privacidade e segurança** | Obter, usar e proteger dados e modelos adequadamente |
| **Segurança** (safety) | Prevenir saídas nocivas e uso indevido |
| **Controlabilidade** | Ter mecanismos para monitorar e dirigir o comportamento do sistema |
| **Veracidade e robustez** | Obter saídas corretas, mesmo com entradas inesperadas ou adversariais |
| **Governança** | Incorporar boas práticas à cadeia de fornecimento de IA, incluindo fornecedores e implantadores |
| **Transparência** | Permitir que as partes interessadas façam escolhas informadas sobre o uso do sistema |

- **Inclusão**: o sistema deve funcionar bem para pessoas de diferentes idiomas, regiões, idades e capacidades.

#### Ferramentas para IA responsável na AWS

| Ferramenta | O que faz |
|---|---|
| **Amazon Bedrock Guardrails** | Salvaguardas configuráveis aplicadas a entradas e saídas de qualquer FM (inclusive fora do Bedrock, via API ApplyGuardrail) |
| **SageMaker Clarify** | Detecta **viés** nos dados (antes do treino) e no modelo (depois do treino) e **explica previsões** mostrando a importância de cada feature. *Em manutenção desde 30/jul/2026* |
| **SageMaker Model Monitor** | Monitora **drift** de dados, de qualidade e de viés em produção. *Em manutenção desde 30/jul/2026* |
| **Amazon Augmented AI (A2I)** | Envia previsões de baixa confiança para **revisão humana**. *Em manutenção desde 30/jul/2026* |
| **SageMaker Model Cards** | Documentação padronizada do modelo: uso pretendido, dados, métricas, riscos, avaliação |
| **Bedrock Model Evaluation** | Avalia modelos inclusive em **robustez** e **toxicidade**, com métricas automáticas, LLM como juiz ou humanos |
| **AWS AI Service Cards** | Documentos da AWS sobre uso pretendido, limitações e boas práticas dos serviços de IA dela |

#### Filtros do Amazon Bedrock Guardrails

| Política | O que faz | Exemplo |
|---|---|---|
| **Filtros de conteúdo** | Detectam e bloqueiam categorias nocivas (ódio, insultos, sexual, violência, má conduta) em texto e imagem, com intensidade ajustável; inclui filtro de **ataques de prompt** | Bloquear linguagem ofensiva e tentativas de jailbreak |
| **Tópicos negados** | Bloqueiam assuntos definidos em linguagem natural | Um banco proíbe o assistente de dar "recomendações de investimento" |
| **Filtros de palavras** | Bloqueiam palavras e expressões específicas, incluindo palavrões | Nomes de concorrentes |
| **Filtros de informações sensíveis** | Detectam **PII** e padrões personalizados (regex) para **bloquear ou mascarar** | Mascarar CPF, e-mail e telefone nas respostas |
| **Verificação de fundamentação contextual** (contextual grounding check) | Detecta respostas **não fundamentadas** na fonte ou irrelevantes para a pergunta | Reduzir **alucinações** em RAG |
| **Verificações de raciocínio automatizado** (automated reasoning checks) | Validam matematicamente a resposta contra regras e políticas formalizadas | Conferir se a resposta respeita uma política de RH |

### Dados, viés e riscos

#### Características de bons conjuntos de dados
- **Inclusivos e diversos**: representam os grupos, idiomas e situações do mundo real.
- **Fontes curadas**: origem conhecida, qualidade verificada, direitos de uso claros.
- **Balanceados**: sem uma classe ou grupo dominando os demais. Dados desbalanceados produzem modelos enviesados e métricas enganosas.

#### Viés e variância
- **Viés alto** (high bias): o modelo é **simples demais** e erra sistematicamente, até nos dados de treino → **underfitting**.
- **Variância alta** (high variance): o modelo **decora** os dados de treino e falha com dados novos → **overfitting**.
- **Efeitos**: resultados **injustos para grupos demográficos** (ex.: aprovar menos crédito para um grupo sub-representado nos dados), **imprecisão** e perda de confiança.
- **Como corrigir overfitting**: mais dados, regularização, modelo mais simples, parar o treino antes (early stopping). **Underfitting**: modelo mais complexo, mais features, treinar por mais tempo.

#### Como detectar e monitorar viés, confiabilidade e veracidade
- **Analisar a qualidade dos rótulos**: rótulos errados ou inconsistentes transmitem viés.
- **Auditorias humanas**: revisores avaliam amostras de saídas.
- **Análise por subgrupos**: medir o desempenho **separadamente para cada grupo** demográfico; um modelo com boa média pode falhar com um grupo específico.
- **Monitoramento contínuo** em produção (drift de viés) e avaliação periódica.

#### Riscos legais da IA generativa
- **Violação de propriedade intelectual**: conteúdo gerado parecido com obras protegidas ou modelos treinados com dados sem direito de uso.
- **Saídas enviesadas** que geram discriminação e responsabilização.
- **Perda da confiança do cliente** após respostas erradas, ofensivas ou vazamentos.
- **Risco ao usuário final**: decisões ou orientações erradas em saúde, finanças ou segurança.
- **Alucinações** apresentadas como fatos.

#### Seleção responsável de modelos
- **Considerações ambientais e de sustentabilidade**: escolher o **menor modelo que atende** à tarefa, reaproveitar modelos pré-treinados em vez de treinar do zero, usar hardware eficiente (**AWS Trainium**, **AWS Inferentia**, Graviton) e Regiões com energia mais limpa.
- Avaliar também licença, documentação (model cards), origem dos dados e resultados de avaliação de segurança do modelo.

### Transparência e explicabilidade

#### Modelos transparentes vs. caixa-preta
- **Transparentes e explicáveis**: é possível entender **como** chegam a uma decisão. Exemplos: regressão linear, árvores de decisão, modelos baseados em regras.
- **Não transparentes** (caixa-preta): redes neurais profundas e LLMs com bilhões de parâmetros; difícil saber por que produziram uma saída.
- **Transparência** refere-se a informar como o sistema foi construído, com quais dados e para qual uso. **Explicabilidade** refere-se a explicar **uma saída específica** (ex.: quais features pesaram na negativa de crédito).

#### Ferramentas de transparência e explicabilidade
- **SageMaker Model Cards**: documentam o modelo para auditoria e governança.
- **SageMaker Clarify**: explicabilidade com importância de features (SHAP).
- **Bedrock Model Evaluations**: resultados comparáveis de qualidade e segurança.
- **Modelos, dados e licenças open source**: permitem inspecionar pesos, dados de treino e termos de uso.
- **AWS AI Service Cards**: transparência sobre os serviços de IA da AWS.

#### Trade-offs entre segurança, transparência e desempenho
- Modelos mais **interpretáveis** costumam ter **desempenho menor** em tarefas complexas; modelos mais poderosos são menos interpretáveis. É preciso **medir interpretabilidade e desempenho** e escolher conforme o risco do caso de uso.
- Expor detalhes demais (dados de treino, prompts, regras) pode facilitar ataques, e esconder demais reduz a confiança. O equilíbrio depende do público e da regulação.

#### Design centrado no humano para IA explicável
- **Mecanismos de feedback do usuário**: botões de avaliação, correções e canais para contestar decisões.
- **Transparência das decisões de IA**: informar quando o usuário está interagindo com IA, mostrar as fontes e o nível de confiança e explicar em linguagem simples.
- **Supervisão humana** para decisões de alto impacto e possibilidade de revisão.
- Interfaces que ajudam o usuário a **calibrar a confiança** (nem confiar cegamente, nem descartar).

### Decisão rápida — IA responsável

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Bloquear conteúdo ofensivo nas respostas do FM | Bedrock Guardrails (filtros de conteúdo) | IAM, Macie |
| Impedir que o assistente fale de um assunto | Guardrails — tópicos negados | Prompt negativo sozinho |
| Mascarar dados pessoais nas respostas | Guardrails — filtro de informações sensíveis | KMS |
| Detectar respostas não fundamentadas na fonte | Guardrails — contextual grounding check | Temperatura alta |
| Detectar viés nos dados e explicar previsões de ML | SageMaker Clarify | Model Cards, CloudTrail |
| Documentar uso pretendido e limitações do modelo | SageMaker Model Cards | Model Registry |
| Revisão humana de previsões de baixa confiança | Amazon A2I (em manutenção) / revisão humana | Rekognition |
| Modelo decora o treino e falha em produção | Variância alta (overfitting) | Viés alto |
| Modelo simples demais, erra sempre | Viés alto (underfitting) | Variância alta |
| Descobrir se o modelo falha com um grupo específico | Análise por subgrupos | Acurácia geral |
| Dados com um grupo sub-representado | Conjunto desbalanceado → coletar/balancear dados | Aumentar a temperatura |
| Escolha de modelo com menor impacto ambiental | Menor modelo que atende, hardware eficiente | Maior modelo disponível |
| Decisão que precisa ser explicada ao cliente | Modelo interpretável + explicabilidade | LLM caixa-preta |
| Conteúdo gerado parecido com obra protegida | Risco de propriedade intelectual | Alucinação |

---

## 11. Segurança, Conformidade e Governança para IA

> **Regra de ouro da prova**: a segurança de IA usa os **mesmos blocos da AWS** — **IAM** com menor privilégio, **KMS** para criptografia, **PrivateLink** para tráfego privado, **Macie** para PII no S3, **CloudTrail** para auditoria, **Config** para conformidade, **Inspector** para vulnerabilidades, **Artifact** para relatórios — mais os controles específicos de IA: **Guardrails**, **AgentCore Identity** e **Policy in AgentCore**.

### Proteger sistemas de IA

#### Serviços e recursos de segurança

| Serviço ou recurso | Papel na segurança de IA |
|---|---|
| **IAM** (roles, políticas, permissões) | Controlar quem pode invocar quais modelos, acessar Knowledge Bases e dados de treino; roles com **menor privilégio** para aplicações e agentes |
| **Criptografia** (AWS KMS, TLS) | Dados de treino, modelos customizados, Knowledge Bases e logs criptografados em repouso com chaves do KMS; TLS em trânsito |
| **Amazon Macie** | Descobrir **PII e dados sensíveis** em buckets S3 **antes** de usá-los em treino ou RAG |
| **AWS PrivateLink** (VPC endpoints) | Acessar o Bedrock e o SageMaker AI **sem passar pela internet pública** |
| **Modelo de responsabilidade compartilhada** | A AWS protege a infraestrutura e os serviços gerenciados; o cliente protege seus dados, prompts, acessos, configurações e aplicações |
| **Amazon Bedrock AgentCore Identity** | Identidade e credenciais **dos agentes**, com acesso delegado a ferramentas e integração a provedores de identidade |
| **Policy in AgentCore** | Regras **determinísticas** (linguagem compatível com **Cedar**) que definem quais ferramentas e ações o agente pode executar e sob quais condições |
| **Amazon Bedrock Guardrails** | Filtrar entradas e saídas, bloquear ataques de prompt e PII |
| **AWS Secrets Manager** | Guardar chaves de API e credenciais usadas por aplicações e agentes |

- **Responsabilidade compartilhada na IA generativa**: ao usar o Bedrock, a AWS cuida da infraestrutura, da hospedagem dos modelos e do isolamento dos dados; o cliente é responsável por **quem acessa**, **quais dados envia**, **quais guardrails configura**, **como a aplicação usa as respostas** e pela conformidade do seu caso de uso.

#### Considerações de segurança e privacidade

| Consideração | Como tratar |
|---|---|
| **Segurança da aplicação** | Validar entradas, autenticar usuários, limitar taxas, seguir boas práticas de desenvolvimento |
| **Detecção de ameaças** | Amazon GuardDuty (inclusive proteção para cargas de IA) e monitoramento de uso anômalo |
| **Gestão de vulnerabilidades** | Amazon Inspector em instâncias, contêineres e Lambda que hospedam a aplicação |
| **Proteção da infraestrutura** | VPC, security groups, PrivateLink, menor privilégio |
| **Prompt injection** | Guardrails, separar instruções de dados, limitar permissões de ferramentas |
| **Criptografia em repouso e em trânsito** | KMS e TLS |
| **Prevenção de vazamento de dados** | Não enviar dados desnecessários ao modelo, mascarar PII, filtrar a recuperação pelas permissões do usuário |
| **Filtragem e validação da saída** | Guardrails, validar formato e conteúdo antes de exibir ou executar |
| **Trilha de auditoria e logs das interações** | **CloudTrail** registra as chamadas de API; o **model invocation logging** do Bedrock grava prompts e respostas no CloudWatch Logs ou no S3 |
| **Toxicidade** | Filtros de conteúdo e avaliação de toxicidade |

#### Detecção de alucinação e grounding
- **Fundamentação com RAG** (RAG grounding): responder a partir de documentos confiáveis, **com citações**, e instruir o modelo a dizer "não sei" quando a resposta não estiver no contexto.
- **Validação da saída**: verificar a resposta contra fontes, regras ou outro modelo; **contextual grounding check** e **automated reasoning checks** do Guardrails.
- **Pontuação de confiança** (confidence scoring): atribuir um nível de confiança e encaminhar respostas de baixa confiança a um humano ou pedir mais informações.
- Também ajudam: **temperatura baixa**, prompts específicos e ferramentas para cálculos e consultas em vez de "memória" do modelo.

#### Origem dos dados e engenharia de dados segura
- **Citação de fontes** e **documentação da origem dos dados**: saber de onde veio cada dado de treino e cada trecho usado na resposta.
- **Linhagem de dados** (data lineage): rastrear a origem e as transformações dos dados até o modelo.
- **Catalogação de dados**: AWS Glue Data Catalog e Lake Formation mantêm metadados e permissões.
- **SageMaker Model Cards**: registram dados usados, finalidade e avaliação.
- **Boas práticas de engenharia de dados segura**: **avaliar a qualidade** dos dados; aplicar **tecnologias de preservação de privacidade** (anonimização, mascaramento, tokenização, privacidade diferencial, dados sintéticos); **controlar o acesso** (Lake Formation, IAM); garantir a **integridade** (versionamento, checksums, controle de quem altera).

### Governança e conformidade

#### Serviços de governança e conformidade

| Serviço | Papel |
|---|---|
| **AWS Config** | Registrar configurações e avaliar conformidade dos recursos (ex.: endpoints e buckets criptografados) |
| **Amazon Inspector** | Encontrar vulnerabilidades nas cargas que hospedam IA |
| **AWS Artifact** | Relatórios de conformidade da AWS (SOC, ISO, incluindo **ISO/IEC 42001** de sistema de gestão de IA) |
| **AWS CloudTrail** | Auditoria de quem chamou quais APIs (invocações de modelos, alterações em guardrails) |
| **AWS Trusted Advisor** | Recomendações de segurança, custo e limites |
| **AWS Audit Manager** | Coletar evidências para auditorias, com frameworks prontos (inclusive para IA generativa) |
| **Amazon CloudWatch** | Métricas, logs e alarmes de uso e desempenho |

#### Estratégias de governança de dados
- **Ciclo de vida dos dados**: coleta, uso, arquivamento e exclusão definidos.
- **Logs**: registrar acessos, invocações e alterações.
- **Residência**: manter dados na Região exigida por lei ou contrato.
- **Monitoramento e observação**: acompanhar uso, qualidade e desvios continuamente.
- **Retenção**: guardar dados e logs pelo tempo exigido e não mais que isso.

#### Processos e frameworks de governança
- **Políticas** de uso aceitável de IA, aprovação de casos de uso e classificação de risco.
- **Cadência de revisão** e **estratégias de revisão** (revisões periódicas de modelos, dados, prompts e incidentes).
- **Padrões de transparência**: informar usuários sobre o uso de IA e documentar modelos.
- **Requisitos de treinamento das equipes** em uso seguro e responsável de IA.
- **Regulações e padrões externos**: **ISO/IEC 42001** (gestão de IA), **NIST AI Risk Management Framework**, **EU AI Act** (classificação por nível de risco) e leis de proteção de dados como **LGPD** e **GDPR**.

#### Generative AI Security Scoping Matrix
Framework da AWS que classifica o uso de IA generativa em **cinco escopos**, do menor ao maior controle (e responsabilidade) do cliente:

| Escopo | Tipo | Exemplo |
|---|---|---|
| **1** | **Aplicação para consumidor** | Funcionários usando um chatbot público de IA |
| **2** | **Aplicação corporativa** (SaaS com IA) | Software empresarial com recursos de IA generativa embutidos |
| **3** | **Modelos pré-treinados** | Construir a aplicação sobre um FM via API (ex.: Amazon Bedrock) |
| **4** | **Modelos ajustados** (fine-tuned) | Ajustar um FM com os próprios dados |
| **5** | **Modelos treinados pela própria empresa** | Treinar um modelo do zero |

- Quanto **maior o escopo**, mais responsabilidades de segurança, privacidade, governança e conformidade ficam com o cliente (dados de treino, pesos do modelo, avaliação).

### Decisão rápida — Segurança e governança

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Invocar o Bedrock sem passar pela internet | AWS PrivateLink (VPC endpoint) | NAT Gateway, Direct Connect sozinho |
| Encontrar PII em dados de treino no S3 | Amazon Macie | Comprehend, Inspector |
| Criptografar dados de treino e modelos customizados | AWS KMS | ACM, Secrets Manager |
| Controlar quem pode invocar cada modelo | IAM (políticas com menor privilégio) | Guardrails |
| Auditar quem chamou o modelo e quando | AWS CloudTrail | CloudWatch métricas |
| Registrar prompts e respostas | Bedrock model invocation logging | Config |
| Identidade e credenciais de agentes | AgentCore Identity | Access keys fixas |
| Limitar ações de agentes com regras determinísticas | Policy in AgentCore | Prompt de sistema |
| Relatórios de conformidade da AWS (ex.: ISO 42001) | AWS Artifact | Audit Manager |
| Coletar evidências para auditoria | AWS Audit Manager | Artifact |
| Verificar conformidade de configurações | AWS Config | CloudTrail |
| Vulnerabilidades nas instâncias que hospedam o modelo | Amazon Inspector | GuardDuty |
| Reduzir alucinações com fontes confiáveis | RAG com citações + grounding check | Temperatura alta |
| Rastrear origem e transformações dos dados | Linhagem de dados (data lineage) | Fine-tuning |
| Empresa usando um FM via Bedrock: qual escopo? | Escopo 3 — modelos pré-treinados | Escopo 1, escopo 5 |
| Empresa treinando o próprio FM | Escopo 5 | Escopo 3 |

---

## 12. Padrões recorrentes e palavras-chave

As questões do AI Practitioner giram em torno de poucas decisões: qual técnica, qual nível de customização, qual serviço e qual controle de risco. Esta seção reúne as palavras do enunciado que apontam para cada resposta e os pares que mais se confundem.

### Palavras-chave do enunciado

| Se o enunciado diz… | Pense em… |
|---|---|
| "Número contínuo", "prever valor" | Regressão |
| "Categoria", "sim ou não" | Classificação |
| "Sem rótulos", "agrupar", "segmentar" | Clustering (não supervisionado) |
| "Recompensa", "tentativa e erro" | Aprendizado por reforço |
| "Resultado exato sempre", "regra fixa" | Não usar ML |
| "Sem treinar modelo", "serviço pronto" | Serviço de IA gerenciado (Rekognition, Textract, Comprehend…) |
| "Vários FMs por API", "serverless" | Amazon Bedrock |
| "Modelo pré-treinado em endpoint próprio" | SageMaker JumpStart |
| "Dados privados", "atualizados", "citar fontes" | RAG (Bedrock Knowledge Bases) |
| "Tom", "estilo", "formato específico" | Fine-tuning |
| "Menor custo de customização" | Engenharia de prompt / in-context learning |
| "Modelo menor com qualidade do maior" | Destilação |
| "Respostas consistentes e factuais" | Temperatura baixa |
| "Raciocinar passo a passo" | Chain-of-thought |
| "Exemplos no prompt" | Few-shot |
| "Ignore as instruções anteriores" | Prompt injection |
| "Bloquear tópicos", "filtrar conteúdo", "mascarar PII na resposta" | Bedrock Guardrails |
| "Resposta inventada" | Alucinação → RAG, grounding check |
| "Executa tarefas em várias etapas com ferramentas" | Agente (AgentCore, Strands Agents) |
| "Conectar agentes a ferramentas de forma padronizada" | MCP |
| "Viés e explicabilidade de modelo de ML" | SageMaker Clarify |
| "Documentar o modelo" | SageMaker Model Cards |
| "Sem internet pública" | AWS PrivateLink |
| "PII em buckets S3" | Amazon Macie |
| "Quem chamou o modelo" | AWS CloudTrail |
| "Relatório de conformidade da AWS" | AWS Artifact |
| "Resumo" (avaliação) | ROUGE |
| "Tradução" (avaliação) | BLEU |

### Pares que mais se confundem

| Par | Como separar |
|---|---|
| **IA vs. ML vs. deep learning vs. GenAI** | Círculos concêntricos: IA ⊃ ML ⊃ deep learning ⊃ GenAI; IA agêntica é uma arquitetura que usa GenAI |
| **Algoritmo vs. modelo** | Algoritmo é o método; modelo é o resultado treinado |
| **Treinamento vs. inferência** | Treinar ajusta parâmetros; inferir usa o modelo para prever |
| **Parâmetro vs. hiperparâmetro** | Parâmetro é aprendido; hiperparâmetro é escolhido antes do treino |
| **Overfitting vs. underfitting** | Overfitting = variância alta, decora o treino; underfitting = viés alto, simples demais |
| **Precisão vs. recall** | Precisão evita falsos positivos; recall evita falsos negativos |
| **Inferência em tempo real vs. assíncrona vs. batch vs. serverless** | Imediata; fila com payload grande; lote offline; intermitente sem instância |
| **RAG vs. fine-tuning** | RAG muda o **contexto** (conhecimento atual); fine-tuning muda os **pesos** (comportamento) |
| **Fine-tuning vs. continued pre-training** | Fine-tuning usa dados **rotulados**; continued pre-training usa dados **não rotulados** do domínio |
| **Bedrock vs. SageMaker AI** | Bedrock = FMs por API serverless; SageMaker AI = construir, treinar e hospedar com controle |
| **Bedrock vs. SageMaker JumpStart** | Pagar por token sem instância vs. modelo em endpoint dedicado pago por hora |
| **Comprehend vs. Textract** | Comprehend entende texto (sentimento, entidades); Textract extrai texto e tabelas de documentos |
| **Transcribe vs. Polly** | Transcribe: fala → texto; Polly: texto → fala |
| **Rekognition vs. Textract** | Rekognition analisa imagens (rostos, objetos); Textract lê documentos |
| **Lex vs. Bedrock** | Lex: bot baseado em intenções; Bedrock: FMs para conversas abertas e geração |
| **Guardrails vs. IAM** | Guardrails controla o **conteúdo**; IAM controla **quem acessa** |
| **Guardrails vs. Clarify** | Guardrails protege aplicações de GenAI em tempo real; Clarify analisa viés e explicabilidade de modelos de ML |
| **Model Cards vs. AI Service Cards** | Model Cards documentam **seus** modelos; AI Service Cards documentam os serviços de IA **da AWS** |
| **MCP vs. A2A** | MCP conecta agente a ferramentas e dados; A2A conecta agente a agente |
| **Strands Agents vs. AgentCore** | Strands é o **SDK** para escrever o agente; AgentCore é a **plataforma** para executar e operar |
| **Kiro vs. Amazon Quick** | Kiro é para **desenvolvedores**; Amazon Quick é para **usuários de negócio** |
| **ROUGE vs. BLEU vs. BERTScore** | Resumo (recall) vs. tradução (precisão) vs. similaridade semântica |
| **Prompt injection vs. jailbreaking vs. poisoning** | Sobrescrever instruções vs. contornar proteções vs. contaminar dados de treino ou da base |
| **CloudTrail vs. model invocation logging** | CloudTrail: quem chamou a API; invocation logging: conteúdo dos prompts e respostas |

### Afirmações falsas que aparecem como alternativa
- "Fine-tuning é a melhor forma de manter o modelo atualizado com dados que mudam diariamente" — **falso**, use RAG.
- "Aumentar a temperatura reduz alucinações" — **falso**, temperatura alta aumenta a variação.
- "O Amazon Bedrock usa os prompts dos clientes para treinar os modelos base" — **falso**.
- "Acurácia é sempre a melhor métrica" — **falso** com classes desbalanceadas.
- "Treinar um FM do zero é a opção de menor custo" — **falso**, é a mais cara.
- "Guardrails substituem o controle de acesso do IAM" — **falso**, são complementares.
- "IA é sempre a melhor solução para automatizar decisões" — **falso** quando o resultado precisa ser exato ou o custo supera o benefício.
- "Modelos maiores são sempre a melhor escolha" — **falso**: custam mais, têm mais latência e maior impacto ambiental.
- "RAG altera os pesos do modelo" — **falso**, só adiciona contexto.
- "Um agente deve ter acesso amplo a todas as ferramentas para ser útil" — **falso**, aplique menor privilégio e Policy.

---

## 13. Mapa de Domínios do Exame

Cada domínio oficial tem um peso diferente na nota final (20/24/28/14/14%). Esta seção cruza os tópicos das seções 1 a 11 com o domínio que eles testam, para priorizar a revisão pelo que realmente pesa na prova.

### Domínio 1 — Fundamentals of AI and ML (20%)

| Tópico | Onde revisar |
|---|---|
| Termos básicos, IA vs. ML vs. deep learning vs. GenAI vs. IA agêntica | Seção 1 |
| Tipos de inferência, de dados e de aprendizado | Seção 1 |
| Quando usar e quando não usar IA; regressão, classificação, clustering | Seção 2 |
| Aplicações reais e serviços de IA gerenciados | Seção 2 |
| ML tradicional vs. foundation models | Seção 2 |
| Pipeline de IA/ML, fontes de modelos, uso em produção, serviços por etapa | Seção 3 |
| MLOps e métricas de modelo e de negócio | Seção 3 |

### Domínio 2 — Fundamentals of GenAI (24%)

| Tópico | Onde revisar |
|---|---|
| Tokens, chunking, embeddings, vetores, transformers, FMs, multimodal, difusão | Seção 4 |
| Casos de uso e ciclo de vida de FMs | Seção 4 |
| Preço por tokens e engenharia de contexto | Seção 4 |
| Conceitos de IA agêntica, MCP, padrões multiagente, memória, ferramentas | Seção 5 |
| Vantagens, limitações, seleção de modelos e métricas de negócio | Seção 4 |
| Bedrock, SageMaker AI, JumpStart, Amazon Quick, Kiro, Strands Agents, AgentCore | Seções 5 e 6 |
| Vantagens, benefícios de infraestrutura e trade-offs de custo | Seção 6 |

### Domínio 3 — Applications of Foundation Models (28%)

| Tópico | Onde revisar |
|---|---|
| Critérios de seleção de FMs e parâmetros de inferência | Seção 7 |
| RAG, Bedrock Knowledge Bases e bancos vetoriais | Seção 7 |
| Custos de customização (pré-treino, fine-tuning, in-context, RAG, destilação) | Seção 7 |
| Papel dos agentes e aplicações de negócio | Seções 5 e 7 |
| Elementos, técnicas, boas práticas e riscos de prompts; Prompt Management | Seção 8 |
| Pré-treinamento, fine-tuning, continued pre-training, destilação, preparação de dados, RLHF | Seção 9 |
| Avaliação de FMs e aplicações; ROUGE, BLEU, BERTScore, LLM como juiz; métricas de negócio | Seção 9 |

### Domínio 4 — Guidelines for Responsible AI (14%)

| Tópico | Onde revisar |
|---|---|
| Dimensões da IA responsável e Bedrock Guardrails | Seção 10 |
| Seleção responsável de modelos e sustentabilidade | Seção 10 |
| Riscos legais da IA generativa | Seção 10 |
| Conjuntos de dados, viés e variância, detecção de viés | Seção 10 |
| Transparência, explicabilidade, Model Cards, trade-offs, design centrado no humano | Seção 10 |

### Domínio 5 — Security, Compliance, and Governance for AI Solutions (14%)

| Tópico | Onde revisar |
|---|---|
| IAM, KMS, Macie, PrivateLink, responsabilidade compartilhada, AgentCore Identity, Policy, Guardrails | Seção 11 |
| Citação de fontes, linhagem, catalogação, Model Cards | Seção 11 |
| Engenharia de dados segura e considerações de segurança e privacidade | Seção 11 |
| Detecção de alucinação e grounding | Seções 10 e 11 |
| Config, Inspector, Artifact, CloudTrail, Trusted Advisor | Seção 11 |
| Governança de dados, processos, Generative AI Security Scoping Matrix | Seção 11 |

### Observação sobre o modelo de pontuação

O AIF-C01 usa pontuação **compensatória**: não é preciso atingir a nota mínima em cada domínio separadamente, só na prova como um todo. **Aplicações de foundation models (28%)** e **fundamentos de IA generativa (24%)** somam 52% da nota: as seções 4 a 9 deste guia têm o maior retorno por hora de estudo. Os domínios 4 e 5 (28% juntos) são curtos e muito "decoráveis": revise as seções 10 e 11 na véspera.

---

## 14. Autoteste — Flashcards de Revisão Rápida

Cada card abaixo esconde a resposta: clique para expandir só depois de tentar responder mentalmente. O objetivo é forçar recall ativo, não releitura passiva. Uma rodada de 15 a 20 cards por dia nos dias antes da prova cobre todo o banco.

### Fundamentos de IA e ML

> [!question]- Qual é a relação entre IA, machine learning, deep learning e IA generativa?
> São círculos concêntricos: **IA** é o campo amplo; **ML** aprende com dados; **deep learning** é ML com redes neurais profundas; **IA generativa** usa deep learning para criar conteúdo novo. **IA agêntica** é uma arquitetura que usa modelos generativos para planejar e agir.

> [!question]- Qual é a diferença entre algoritmo e modelo?
> O **algoritmo** é o método de aprendizado; o **modelo** é o resultado do treinamento, com os parâmetros aprendidos, usado para inferência.

> [!question]- O que é inferência?
> Usar um modelo treinado para fazer previsões ou gerar saídas a partir de dados novos.

> [!question]- Um modelo acerta 99% nos dados de treino e 60% em dados novos. Qual é o problema?
> **Overfitting** (variância alta): o modelo decorou o treino e não generaliza.

> [!question]- Um modelo erra muito até nos dados de treino. Qual é o problema?
> **Underfitting** (viés alto): o modelo é simples demais para o padrão.

> [!question]- Qual tipo de aprendizado usa dados rotulados?
> **Supervisionado** (classificação e regressão).

> [!question]- Qual tipo de aprendizado encontra grupos em dados sem rótulos?
> **Não supervisionado**, por exemplo com **clustering**.

> [!question]- Um sistema aprende a jogar recebendo pontos por boas jogadas e penalidades por más. Qual tipo de aprendizado?
> **Aprendizado por reforço**.

> [!question]- Cite quatro tipos de dados usados em modelos de IA.
> Rotulados e não rotulados, tabulares, séries temporais, imagens, texto, estruturados e não estruturados.

> [!question]- Qual tipo de inferência usar para pontuar milhões de registros uma vez por noite?
> **Inferência em lote** (batch), como o SageMaker Batch Transform ou a batch inference do Bedrock.

> [!question]- Qual tipo de inferência do SageMaker AI atende a payloads grandes e processamento longo, com resultado entregue no S3?
> **Inferência assíncrona**.

> [!question]- Qual tipo de inferência atende a tráfego intermitente sem gerenciar instâncias, aceitando cold start?
> **Inferência serverless**.

### Casos de uso e serviços de IA

> [!question]- Quando a IA/ML não é a solução adequada?
> Quando o **custo supera o benefício**, quando é preciso um **resultado exato e determinístico** em vez de uma previsão, quando faltam dados de qualidade ou quando a explicabilidade total é obrigatória e o modelo não a oferece.

> [!question]- Prever o valor de venda de um imóvel é classificação ou regressão?
> **Regressão**, porque a saída é um número contínuo.

> [!question]- Identificar se uma transação é fraudulenta é classificação ou regressão?
> **Classificação** (binária).

> [!question]- Qual serviço detecta rostos e conteúdo impróprio em imagens?
> **Amazon Rekognition**.

> [!question]- Qual serviço extrai formulários e tabelas de documentos digitalizados?
> **Amazon Textract**.

> [!question]- Qual serviço identifica sentimento, entidades e PII em textos?
> **Amazon Comprehend**.

> [!question]- Transcribe ou Polly: qual converte áudio de chamadas em texto?
> **Amazon Transcribe**. O Polly faz o contrário (texto para fala).

> [!question]- Qual serviço cria chatbots baseados em intenções, com a tecnologia da Alexa?
> **Amazon Lex**.

> [!question]- Qual serviço gera recomendações personalizadas de produtos?
> **Amazon Personalize**.

> [!question]- Quando um modelo de ML tradicional é preferível a um foundation model?
> Quando a tarefa é uma **previsão específica com dados estruturados**, quando a **regulação exige explicar cada decisão**, ou quando há restrições operacionais de **latência, custo por previsão ou determinismo**.

> [!question]- Qual é a recomendação atual da AWS para busca e perguntas sobre documentos internos, já que o Kendra entrou em manutenção?
> **Amazon Bedrock Knowledge Bases** (RAG gerenciado).

### Ciclo de vida e MLOps

> [!question]- Coloque em ordem: avaliação, coleta de dados, implantação, engenharia de features, treinamento, objetivo de negócio, monitoramento.
> Objetivo de negócio → coleta de dados → engenharia de features → treinamento → avaliação → implantação → monitoramento.

> [!question]- O que é análise exploratória de dados (EDA)?
> Examinar os dados para entender distribuições, correlações, valores faltantes, outliers e desbalanceamento antes de preparar e treinar.

> [!question]- Qual é a diferença entre parâmetro e hiperparâmetro?
> **Parâmetros** (pesos) são aprendidos no treino. **Hiperparâmetros** (taxa de aprendizado, épocas) são definidos antes e ajustados em busca da melhor configuração.

> [!question]- Qual recurso do SageMaker oferece ML sem código para analistas de negócio?
> **SageMaker Canvas**.

> [!question]- Qual recurso do SageMaker armazena e compartilha features para treino e inferência?
> **SageMaker Feature Store**.

> [!question]- Qual recurso do SageMaker é um hub de modelos pré-treinados para implantar com poucos cliques?
> **SageMaker JumpStart**.

> [!question]- Quais são as duas formas principais de usar um modelo em produção?
> **API gerenciada** (ex.: Amazon Bedrock, menor esforço operacional) ou **API auto-hospedada** (ex.: endpoint do SageMaker AI, EC2 ou EKS, mais controle).

> [!question]- O que é data drift e como tratar?
> Mudança na distribuição dos dados de entrada em produção, que degrada o modelo. Trata-se com **monitoramento contínuo** e **retreinamento**.

> [!question]- Cite quatro conceitos de MLOps.
> Experimentação, processos repetíveis, sistemas escaláveis, gestão de dívida técnica, prontidão para produção, monitoramento e retreinamento de modelos.

> [!question]- Por que a acurácia pode enganar em detecção de fraude?
> Porque as classes são **desbalanceadas**: um modelo que diz "não fraude" sempre teria acurácia altíssima sem detectar nada. Use recall, precisão, F1 ou AUC.

> [!question]- Em diagnóstico de doenças, qual métrica priorizar?
> **Recall**, porque não detectar um doente (falso negativo) é o erro mais caro.

> [!question]- Em um filtro que bloqueia e-mails, qual métrica priorizar para não bloquear mensagens legítimas?
> **Precisão**, porque o falso positivo é o erro mais caro.

> [!question]- O que é o F1 score?
> A média harmônica entre precisão e recall; equilibra as duas, útil com classes desbalanceadas.

> [!question]- Cite três métricas de negócio para avaliar um modelo de ML.
> Custo por usuário, custos de desenvolvimento, feedback dos clientes e ROI.

### Fundamentos de IA generativa

> [!question]- O que é um token?
> A unidade de texto processada pelo modelo (palavra, parte de palavra ou pontuação). Contexto e preço são medidos em tokens.

> [!question]- O que são embeddings?
> Vetores numéricos que representam o **significado** de textos, imagens ou áudio; conteúdos semelhantes ficam próximos no espaço vetorial.

> [!question]- Para que serve o chunking?
> Dividir documentos em pedaços menores antes de gerar embeddings, para melhorar a recuperação e caber na janela de contexto.

> [!question]- Qual arquitetura é a base dos LLMs modernos?
> **Transformer**, com mecanismo de atenção.

> [!question]- Como funciona um modelo de difusão?
> Parte de ruído aleatório e o remove passo a passo até gerar a imagem (ou vídeo) descrita.

> [!question]- O que é um foundation model?
> Um modelo grande pré-treinado em dados amplos, reaproveitável e adaptável a muitas tarefas.

> [!question]- Cite as etapas do ciclo de vida de um FM.
> Seleção de dados, seleção do modelo, pré-treinamento, fine-tuning, avaliação, implantação e feedback.

> [!question]- Como o preço por tokens afeta custo e desempenho?
> Mais tokens de entrada e saída aumentam o **custo** e a **latência**. Tokens de saída costumam ser mais caros. Reduz-se com modelos menores, prompts enxutos, limite de saída, prompt caching e batch.

> [!question]- O que é engenharia de contexto?
> Decidir e montar o que entra na janela de contexto a cada chamada (instruções, histórico, documentos, resultados de ferramentas, memória), tratando o contexto como um recurso limitado e caro.

> [!question]- Cite quatro desvantagens da IA generativa.
> Alucinações, baixa interpretabilidade, imprecisão e não determinismo (além de viés, custo e latência).

> [!question]- Cite quatro vantagens da IA generativa.
> Adaptabilidade, responsividade, capacidade conversacional e capacidade de gerar conteúdo.

> [!question]- Cite fatores para escolher um modelo de IA generativa.
> Tipo de modelo, desempenho, capacidades, restrições, conformidade, custo, latência e complexidade.

### IA agêntica

> [!question]- Quais são os componentes de um agente de IA?
> Um **modelo** que raciocina, **instruções**, **ferramentas** para agir, **memória** (curto e longo prazo) e um **loop de orquestração** (planejar, agir, observar).

> [!question]- O que é o Model Context Protocol (MCP)?
> Um protocolo aberto que padroniza como agentes e aplicações de IA se conectam a ferramentas, dados e sistemas externos, em arquitetura cliente-servidor.

> [!question]- Qual é a diferença entre MCP e A2A?
> **MCP** conecta agentes a **ferramentas e dados**; **A2A** padroniza a comunicação **entre agentes**.

> [!question]- Cite três padrões de sistemas multiagente.
> Supervisor/orquestrador, agentes como ferramentas, swarm e grafo/workflow.

> [!question]- Qual é a diferença entre memória de curto e de longo prazo em agentes?
> **Curto prazo**: contexto da conversa ou tarefa atual. **Longo prazo**: fatos e preferências que persistem entre sessões.

> [!question]- O que é o Amazon Bedrock AgentCore?
> Plataforma para construir, implantar e operar agentes com segurança e em escala, com qualquer framework e modelo, sem gerenciar infraestrutura (Runtime, Harness, Memory, Gateway, Identity, Policy, Code Interpreter, Browser, Observability, Evaluations).

> [!question]- Qual componente do AgentCore transforma APIs e funções Lambda em ferramentas MCP?
> **AgentCore Gateway**.

> [!question]- O que é o Strands Agents?
> **SDK open source** da AWS, em Python e TypeScript, para construir agentes com abordagem orientada ao modelo: você define prompt e ferramentas, e o modelo planeja e chama as ferramentas.

> [!question]- O que é o Kiro?
> A plataforma de **desenvolvimento agêntico** da AWS (IDE, CLI), com desenvolvimento orientado a especificações. Substitui o Amazon Q Developer.

> [!question]- O que aconteceu com o Amazon Bedrock Agents em julho de 2026?
> Virou **Bedrock Agents Classic** e entrou em **modo de manutenção** (sem novos clientes desde 30/jul/2026). A recomendação é usar o **Bedrock AgentCore** (harness gerenciado ou agentes em código).

> [!question]- Qual serviço usa agentes de IA para modernizar mainframe, .NET e VMware?
> **AWS Transform**.

### Serviços de IA generativa

> [!question]- O que é o Amazon Bedrock?
> Serviço serverless que dá acesso por API a foundation models de vários provedores, com Knowledge Bases, Guardrails, avaliação, gerenciamento de prompts e customização.

> [!question]- O Amazon Bedrock usa os prompts e dados dos clientes para treinar os modelos base?
> **Não**. Os dados não são usados para treinar os modelos base nem compartilhados com os provedores.

> [!question]- Bedrock ou SageMaker JumpStart: qual implanta o modelo em um endpoint dedicado cobrado por hora de instância?
> **SageMaker JumpStart**. O Bedrock on-demand cobra por token, sem instância.

> [!question]- Qual opção de preço do Bedrock dá throughput garantido para carga alta e previsível?
> **Provisioned Throughput**.

> [!question]- Qual opção do Bedrock processa grandes volumes sem urgência com preço menor?
> **Batch inference**.

> [!question]- Qual modelo Amazon Nova gera imagens? E vídeos?
> **Nova Canvas** gera imagens; **Nova Reel** gera vídeos.

> [!question]- Qual modelo Amazon Nova é só texto e tem a menor latência?
> **Nova Micro**.

> [!question]- Qual é o sucessor do Amazon Q Business para novos clientes?
> **Amazon Quick**, espaço de trabalho de IA agêntica que inclui chat, pesquisa, fluxos, automação e o Quick Sight.

> [!question]- Cite três benefícios da infraestrutura AWS para IA generativa.
> Segurança (IAM, KMS, PrivateLink, isolamento de dados), conformidade (certificações como ISO/IEC 42001), responsabilidade compartilhada clara e segurança do conteúdo (Guardrails).

### Design, RAG e customização

> [!question]- Qual efeito tem uma temperatura baixa?
> Respostas mais **previsíveis, focadas e consistentes**. Temperatura alta gera respostas mais criativas e variadas.

> [!question]- O que é RAG?
> **Retrieval Augmented Generation**: recuperar trechos relevantes de uma base de conhecimento no momento da pergunta e incluí-los no prompt para o modelo responder com base neles.

> [!question]- Coloque em ordem as etapas do RAG: geração, embeddings dos documentos, recuperação, chunking, armazenamento no banco vetorial.
> Chunking → embeddings dos documentos → armazenamento no banco vetorial → recuperação → geração.

> [!question]- Qual recurso do Bedrock implementa RAG gerenciado?
> **Amazon Bedrock Knowledge Bases**.

> [!question]- Cite quatro serviços AWS que armazenam embeddings em banco vetorial.
> Amazon OpenSearch Service, Amazon Aurora PostgreSQL (pgvector), Amazon RDS for PostgreSQL (pgvector) e Amazon Neptune (também DocumentDB e S3 Vectors).

> [!question]- Ordene do menor para o maior custo: fine-tuning, pré-treinamento do zero, engenharia de prompt, RAG.
> Engenharia de prompt → RAG → fine-tuning → pré-treinamento do zero.

> [!question]- Um assistente precisa responder com base em políticas internas que mudam toda semana. RAG ou fine-tuning?
> **RAG**: basta atualizar a base de conhecimento, sem retreinar.

> [!question]- O modelo precisa sempre responder no formato e tom da marca, e o prompt não resolveu. Qual abordagem?
> **Fine-tuning** com exemplos rotulados.

> [!question]- O que é destilação de modelos?
> Treinar um modelo **aluno** menor para imitar as respostas de um modelo **professor** maior, reduzindo custo e latência de inferência.

### Engenharia de prompts

> [!question]- Quais são os elementos de um bom prompt?
> Instrução, contexto, dados de entrada, formato de saída e, quando útil, exemplos e prompts negativos.

> [!question]- Qual é a diferença entre zero-shot, one-shot e few-shot?
> Zero-shot: sem exemplos. One-shot: um exemplo. Few-shot: alguns exemplos no prompt.

> [!question]- O que é chain-of-thought?
> Pedir ao modelo que raciocine passo a passo antes de responder, melhorando tarefas de lógica e várias etapas.

> [!question]- O que é um prompt negativo?
> Instrução sobre o que o modelo **não** deve fazer ou incluir (ou elementos a evitar em uma imagem gerada).

> [!question]- O que é prompt injection?
> Texto malicioso que tenta sobrescrever as instruções do sistema, vindo do usuário ou de um documento recuperado.

> [!question]- Qual é a diferença entre jailbreaking e poisoning?
> **Jailbreaking** contorna as proteções do modelo com truques no prompt. **Poisoning** contamina os dados de treino ou a base de conhecimento.

> [!question]- Para que serve o Amazon Bedrock Prompt Management?
> Criar, testar, **versionar** e reutilizar prompts com variáveis e configurações, promovendo versões aprovadas sem mudar o código.

### Treinamento e avaliação

> [!question]- Qual é a diferença entre fine-tuning e continued pre-training?
> **Fine-tuning** usa dados **rotulados** (prompt-resposta) para uma tarefa. **Continued pre-training** usa grandes volumes **não rotulados** do domínio.

> [!question]- O que é instruction tuning?
> Fine-tuning com pares de instrução e resposta para o modelo seguir melhor os pedidos.

> [!question]- O que é RLHF?
> Reinforcement learning from human feedback: humanos avaliam respostas, um modelo de recompensa aprende as preferências e orienta o ajuste do modelo.

> [!question]- Cite cinco cuidados na preparação de dados para fine-tuning.
> Curadoria, governança, tamanho adequado, rotulagem consistente e representatividade.

> [!question]- Qual métrica avalia a qualidade de resumos?
> **ROUGE**.

> [!question]- Qual métrica avalia a qualidade de traduções?
> **BLEU**.

> [!question]- Qual métrica compara o significado mesmo com palavras diferentes?
> **BERTScore**.

> [!question]- O que é LLM como juiz?
> Usar um modelo para avaliar as respostas de outro segundo critérios definidos, em escala.

> [!question]- Como avaliar uma aplicação RAG?
> Avaliar a **recuperação** (trechos corretos?) e a **geração** (resposta fiel ao contexto e relevante?), por exemplo com o Bedrock Model Evaluation.

> [!question]- Cite três métricas de alinhamento com o negócio para aplicações de IA.
> Taxa de conclusão de tarefas, satisfação do usuário e custo por interação.

### IA responsável

> [!question]- Cite seis características da IA responsável citadas no guia.
> Viés, justiça, inclusão, robustez, segurança e veracidade.

> [!question]- Quais políticas o Amazon Bedrock Guardrails oferece?
> Filtros de conteúdo (incluindo ataques de prompt), tópicos negados, filtros de palavras, filtros de informações sensíveis (PII), verificação de fundamentação contextual e verificações de raciocínio automatizado.

> [!question]- Qual ferramenta detecta viés e explica previsões de modelos de ML?
> **SageMaker Clarify** (em manutenção desde 30/jul/2026).

> [!question]- O que são SageMaker Model Cards?
> Documentação padronizada do modelo: uso pretendido, dados, métricas, avaliação e riscos, para transparência e governança.

> [!question]- O que é análise por subgrupos?
> Medir o desempenho do modelo separadamente para cada grupo demográfico, revelando falhas escondidas na média.

> [!question]- Cite três riscos legais da IA generativa.
> Violação de propriedade intelectual, saídas enviesadas, perda da confiança do cliente, risco ao usuário final e alucinações.

> [!question]- Cite características de um bom conjunto de dados.
> Inclusivo, diverso, de fontes curadas e balanceado.

> [!question]- Qual é o trade-off entre interpretabilidade e desempenho?
> Modelos mais interpretáveis (árvores, regressão) costumam ter desempenho menor em tarefas complexas; modelos mais poderosos são menos interpretáveis.

> [!question]- Cite dois princípios de design centrado no humano para IA explicável.
> Mecanismos de feedback do usuário e transparência das decisões de IA (inclusive supervisão humana em decisões de alto impacto).

> [!question]- Como escolher um modelo de forma sustentável?
> Usar o menor modelo que atende, reaproveitar modelos pré-treinados e usar hardware eficiente como Trainium e Inferentia.

### Segurança, conformidade e governança

> [!question]- Como acessar o Amazon Bedrock sem passar pela internet pública?
> Com **AWS PrivateLink** (interface VPC endpoint).

> [!question]- Qual serviço descobre PII em dados de treino armazenados no S3?
> **Amazon Macie**.

> [!question]- Qual é a responsabilidade do cliente ao usar o Bedrock?
> Controlar o acesso (IAM), os dados que envia, os guardrails, a criptografia com suas chaves, como a aplicação usa as respostas e a conformidade do caso de uso. A AWS protege a infraestrutura e o serviço.

> [!question]- Para que serve o Policy in AgentCore?
> Definir regras determinísticas sobre quais ferramentas e ações um agente pode usar e em quais condições, interceptando cada chamada de ferramenta.

> [!question]- Como registrar os prompts e respostas de um modelo no Bedrock?
> Com o **model invocation logging**, que envia os registros ao CloudWatch Logs ou ao S3. O CloudTrail registra as chamadas de API.

> [!question]- Cite três técnicas para detectar alucinações ou fundamentar respostas.
> Grounding com RAG e citações, validação da saída (inclusive contextual grounding check) e pontuação de confiança.

> [!question]- O que é linhagem de dados?
> O rastreamento da origem e das transformações dos dados até o modelo, essencial para auditoria.

> [!question]- Cite tecnologias de preservação de privacidade.
> Anonimização, mascaramento, tokenização, privacidade diferencial e dados sintéticos.

> [!question]- Onde obter o relatório ISO/IEC 42001 da AWS?
> No **AWS Artifact**.

> [!question]- Cite cinco estratégias de governança de dados do guia.
> Ciclo de vida dos dados, logs, residência, monitoramento/observação e retenção.

> [!question]- Quais são os cinco escopos da Generative AI Security Scoping Matrix?
> 1 — aplicação para consumidor; 2 — aplicação corporativa; 3 — modelos pré-treinados; 4 — modelos ajustados (fine-tuned); 5 — modelos treinados pela própria empresa.

### Pegadinhas Duplas (confusões mais recorrentes)

> [!question]- RAG, fine-tuning ou prompt: qual responde "dados de ontem", "tom da marca" e "menor custo para começar"?
> Dados de ontem → **RAG**. Tom da marca → **fine-tuning**. Menor custo para começar → **engenharia de prompt**.

> [!question]- Guardrails, IAM ou Macie: qual responde "bloquear um tópico", "quem pode invocar o modelo" e "PII nos dados de treino do S3"?
> Bloquear tópico → **Guardrails**. Quem pode invocar → **IAM**. PII no S3 → **Macie**.

> [!question]- ROUGE, BLEU ou BERTScore: qual responde "resumo", "tradução" e "mesmo significado com outras palavras"?
> Resumo → **ROUGE**. Tradução → **BLEU**. Mesmo significado → **BERTScore**.

> [!question]- Precisão ou recall: qual priorizar para "não deixar fraude passar" e "não bloquear cliente bom"?
> Não deixar fraude passar → **recall**. Não bloquear cliente bom → **precisão**.

> [!question]- Strands Agents, AgentCore ou Kiro: qual responde "escrever o agente em Python", "executar o agente em produção" e "IDE com IA para desenvolver"?
> Escrever o agente → **Strands Agents**. Executar em produção → **AgentCore**. IDE com IA → **Kiro**.

---

## 15. Mapa de cobertura do guia oficial e questões de múltipla resposta

O [guia oficial do AIF-C01](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html) divide a prova em **14 tarefas**. A tabela localiza a revisão de cada tarefa neste material. Cobrir as tarefas publicadas **não garante** conhecer todas as questões: o guia não é uma lista exaustiva, e a [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-in-scope-services.html) está sujeita a alterações. O [histórico de revisões](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-revisions.html) mostra o que mudou na versão 1.1.

| Tarefa oficial | Decisões e conceitos a dominar | Onde revisar |
|---|---|---|
| **1.1 Conceitos e terminologia de IA** | Termos básicos, IA vs. ML vs. GenAI vs. agêntica, tipos de inferência, dados e aprendizado | Seção 1 |
| **1.2 Casos de uso práticos** | Quando usar ou não IA, regressão/classificação/clustering, aplicações, serviços gerenciados, ML tradicional vs. FM | Seção 2 |
| **1.3 Ciclo de vida de IA/ML** | Pipeline, fontes de modelos, uso em produção, serviços por etapa, MLOps, métricas | Seção 3 |
| **2.1 Conceitos de GenAI** | Tokens, chunking, embeddings, transformers, difusão, casos de uso, ciclo do FM, preço por tokens, engenharia de contexto, IA agêntica e MCP | Seções 4 e 5 |
| **2.2 Capacidades e limitações** | Vantagens, desvantagens, seleção de modelos, valor e métricas de negócio | Seção 4 |
| **2.3 Infraestrutura e tecnologias AWS** | Bedrock, SageMaker AI, JumpStart, Quick, Kiro, Strands Agents, AgentCore; vantagens, benefícios e trade-offs de custo | Seções 5 e 6 |
| **3.1 Design de aplicações com FMs** | Critérios de seleção, parâmetros de inferência, RAG, bancos vetoriais, custos de customização, agentes | Seções 5 e 7 |
| **3.2 Engenharia de prompts** | Elementos, técnicas, boas práticas, riscos, Prompt Management | Seção 8 |
| **3.3 Treinamento e fine-tuning** | Pré-treinamento, fine-tuning, continued pre-training, destilação, preparação de dados, RLHF | Seção 9 |
| **3.4 Avaliação de FMs** | Humano no loop, benchmarks, Bedrock Model Evaluation, ROUGE/BLEU/BERTScore/LLM como juiz, avaliação de RAG e agentes, métricas de negócio | Seção 9 |
| **4.1 Sistemas de IA responsáveis** | Dimensões, Guardrails, seleção sustentável, riscos legais, datasets, viés e variância, detecção de viés | Seção 10 |
| **4.2 Transparência e explicabilidade** | Modelos transparentes vs. caixa-preta, Model Cards, trade-offs, design centrado no humano | Seção 10 |
| **5.1 Proteger sistemas de IA** | IAM, KMS, Macie, PrivateLink, responsabilidade compartilhada, AgentCore Identity e Policy, Guardrails, linhagem, dados seguros, alucinação e grounding | Seção 11 |
| **5.2 Governança e conformidade** | Config, Inspector, Artifact, CloudTrail, Trusted Advisor, governança de dados, processos, Scoping Matrix | Seção 11 |

### Como resolver múltipla resposta, ordenação e correspondência

O AIF-C01 tem quatro formatos: **múltipla escolha**, **múltipla resposta** (marque exatamente a quantidade pedida), **ordenação** (3 a 5 itens na sequência correta) e **correspondência** (associar 3 a 7 pares). Nenhum formato dá crédito parcial. Nas questões abaixo, responda antes de abrir a solução.

> [!question]- 1. Uma empresa quer que o assistente responda com base em manuais internos atualizados diariamente e cite as fontes. Escolha DUAS: (A) usar Bedrock Knowledge Bases; (B) fazer fine-tuning diário do modelo; (C) armazenar embeddings em um banco vetorial como OpenSearch Service; (D) aumentar a temperatura; (E) pré-treinar um modelo do zero.
> **A e C.** RAG com Knowledge Bases e um banco vetorial traz dados atuais com citações. Fine-tuning diário e pré-treino são caros e lentos; temperatura alta aumenta a variação. Revise a seção 7.

> [!question]- 2. Quais medidas reduzem alucinações? Escolha DUAS: (A) fundamentar respostas com RAG e citações; (B) usar a verificação de fundamentação contextual do Guardrails; (C) aumentar a temperatura para 1; (D) remover o system prompt; (E) aumentar o tamanho máximo da resposta.
> **A e B.** Grounding e validação da saída reduzem respostas inventadas. As outras opções não ajudam ou pioram. Revise as seções 10 e 11.

> [!question]- 3. Um banco usa um FM no Bedrock e precisa impedir conselhos de investimento e mascarar CPFs nas respostas. Escolha DUAS configurações do Guardrails: (A) tópicos negados; (B) filtro de informações sensíveis; (C) política do IAM; (D) chave do KMS; (E) Amazon Macie.
> **A e B.** Tópicos negados bloqueiam o assunto e o filtro de informações sensíveis mascara PII. IAM, KMS e Macie têm outras funções. Revise a seção 10.

> [!question]- 4. Uma empresa precisa usar o Bedrock com dados confidenciais. Escolha DUAS medidas de segurança: (A) acessar via AWS PrivateLink; (B) aplicar políticas do IAM com menor privilégio; (C) tornar o bucket de dados público; (D) colocar credenciais no prompt; (E) desativar o CloudTrail.
> **A e B.** Tráfego privado e acesso mínimo. As demais aumentam o risco. Revise a seção 11.

> [!question]- 5. Quais são limitações da IA generativa? Escolha DUAS: (A) alucinações; (B) não determinismo; (C) incapacidade de processar linguagem natural; (D) exigência de dados rotulados para qualquer uso; (E) impossibilidade de gerar código.
> **A e B.** C, D e E são falsas: FMs processam linguagem, funcionam sem rótulos via prompt e geram código. Revise a seção 4.

> [!question]- 6. Um time quer construir e operar agentes em produção na AWS. Escolha DUAS: (A) escrever o agente com Strands Agents; (B) executá-lo no Amazon Bedrock AgentCore Runtime; (C) usar Amazon Polly para orquestrar ferramentas; (D) criar um novo agente no Bedrock Agents Classic em uma conta nova; (E) treinar um FM do zero para cada agente.
> **A e B.** Strands é o SDK e AgentCore a plataforma de execução. Polly é voz, Agents Classic não aceita contas novas desde 30/jul/2026, e treinar do zero é desnecessário. Revise a seção 5.

> [!question]- 7. Quais são características de um conjunto de dados que reduz viés? Escolha TRÊS: (A) inclusivo; (B) balanceado; (C) de fontes curadas; (D) com um único grupo demográfico; (E) sem revisão de rótulos; (F) o maior possível, sem curadoria.
> **A, B e C.** Diversidade, equilíbrio e curadoria reduzem viés. D, E e F o aumentam. Revise a seção 10.

> [!question]- 8. ORDENAÇÃO — Coloque as etapas do pipeline de ML na ordem: (1) implantação; (2) coleta de dados; (3) treinamento; (4) definição do objetivo de negócio; (5) avaliação.
> **4 → 2 → 3 → 5 → 1**: objetivo de negócio, coleta de dados, treinamento, avaliação e implantação. Revise a seção 3.

> [!question]- 9. ORDENAÇÃO — Ordene as abordagens de customização da mais barata para a mais cara: (1) fine-tuning; (2) engenharia de prompt; (3) pré-treinamento do zero; (4) RAG.
> **2 → 4 → 1 → 3**: prompt, RAG, fine-tuning e pré-treinamento do zero. Revise a seção 7.

> [!question]- 10. CORRESPONDÊNCIA — Associe cada tarefa ao serviço: (a) extrair tabelas de notas fiscais; (b) transcrever chamadas; (c) analisar sentimento de avaliações; (d) detectar rostos em fotos. Serviços: Rekognition, Comprehend, Textract, Transcribe.
> (a) **Textract**; (b) **Transcribe**; (c) **Comprehend**; (d) **Rekognition**. Revise a seção 2.

> [!question]- 11. CORRESPONDÊNCIA — Associe cada métrica à tarefa: (a) ROUGE; (b) BLEU; (c) recall; (d) BERTScore. Tarefas: tradução, resumo, similaridade semântica, não deixar passar casos positivos.
> (a) **Resumo**; (b) **tradução**; (c) **não deixar passar casos positivos**; (d) **similaridade semântica**. Revise as seções 3 e 9.

> [!question]- 12. CORRESPONDÊNCIA — Associe cada escopo da Generative AI Security Scoping Matrix ao exemplo: (a) escopo 1; (b) escopo 3; (c) escopo 4; (d) escopo 5. Exemplos: treinar um FM do zero; funcionário usando chatbot público; aplicação sobre FM via Bedrock; FM ajustado com dados da empresa.
> (a) **Chatbot público**; (b) **aplicação sobre FM via Bedrock**; (c) **FM ajustado com dados da empresa**; (d) **treinar um FM do zero**. Revise a seção 11.
