## Como usar este guia

- Use os capítulos 1 a 11 para revisão de conteúdo. Eles seguem as categorias de serviço da lista oficial do exame, não a ordem dos domínios, porque a prova mistura os temas.
- Use a tabela **Decisão rápida** ao final de cada capítulo (1 a 11) como cheat sheet de véspera de prova: cada uma reúne cenários típicos, a resposta correta e os distratores clássicos daquele tema.
- Use os **Padrões recorrentes e palavras-chave** (seção 12) para treinar a leitura do enunciado: no Cloud Practitioner, uma palavra do tipo "gerenciado", "auditar", "estimar" ou "sem servidor" costuma decidir a questão. A seção 12 também traz os **serviços que aparecem só como distrator**, os **nomes inventados** e a tabela de **divergências entre a documentação atual e os simulados** — consulte-a sempre que um gabarito contrariar o guia.
- Use o **Mapa de Domínios** (seção 13) para priorizar a revisão conforme o peso de cada domínio na nota final.
- Use o **Autoteste** (seção 14) para revisão ativa: cada flashcard esconde a resposta até você clicar, forçando recall em vez de releitura passiva.
- Use o **Mapa de cobertura e questões de múltipla resposta** (seção 15) para conferir as 19 tarefas oficiais e praticar a seleção da quantidade de alternativas pedida no enunciado.
- O Cloud Practitioner cobra **reconhecimento de serviços e conceitos**, não configuração. Para cada serviço, saiba responder três perguntas: **o que é**, **qual problema resolve** e **com qual serviço parecido ele é confundido**.

### Números, preços e atualizações

Os números, preços e datas deste guia foram conferidos na documentação oficial da AWS (docs.aws.amazon.com e aws.amazon.com) em **setembro de 2026**. São uma referência datada: confirme cotas, preços e disponibilidade antes de depender de um valor exato.

*Três mudanças recentes afetam diretamente o CLF-C02 e ainda não aparecem na maior parte dos cursos e simulados: (1) os **planos de suporte** foram reorganizados em **Basic, Business Support+, Enterprise e Unified Operations**, e o guia oficial do exame já usa esses nomes (veja a seção 11); (2) o **Free Tier** para contas criadas a partir de 15/jul/2025 funciona por **créditos e plano gratuito de 6 meses**, não mais pelo "12 meses grátis"; (3) a **família Snow** deixou de aceitar novos clientes em nov/2025. Quando um simulado usar o modelo antigo, o guia mostra os dois lados para explicar a divergência.*

*Todas as divergências desse tipo estão reunidas numa tabela única em **"Divergências conhecidas entre a documentação atual e os simulados"** (seção 12), com a resposta esperada em cada contexto — inclusive um caso de **erro de gabarito** identificado nos simulados.*

### Método para questões do Cloud Practitioner

1. **Ache a palavra decisiva**: "gerenciado", "sem servidor", "auditar chamadas de API", "estimar custo antes", "alertar quando passar do orçamento", "menor latência global", "conexão privada dedicada". Quase toda questão tem uma.
2. **Identifique a categoria antes do serviço**: é segurança, custo, rede, armazenamento, banco de dados, IA ou suporte? Elimine as alternativas de outra categoria.
3. **Desconfie de serviços reais que fazem outra coisa**: CloudTrail (quem fez) vs. CloudWatch (como está) vs. Config (como estava configurado); Cost Explorer (analisar o passado) vs. Pricing Calculator (estimar o futuro) vs. Budgets (alertar).
4. **Prefira o gerenciado quando o enunciado fala em reduzir esforço operacional**: RDS em vez de banco em EC2, Fargate em vez de cluster EC2, Lambda em vez de servidor ocioso.
5. **Questões com várias respostas**: confira quantas opções o enunciado pede ("Escolha DUAS") e avalie cada alternativa isoladamente.

### Formato do exame CLF-C02

| Item | Valor |
|---|---|
| Código | CLF-C02 (versão vigente em setembro de 2026) |
| Questões | 65 no total: **50 pontuadas** e **15 não pontuadas** (não identificadas) |
| Duração | 90 minutos |
| Tipos de questão | Múltipla escolha (1 correta entre 4) e múltipla resposta (2 ou mais corretas entre 5 ou mais) |
| Pontuação | Escala de 100 a 1.000; **mínimo de 700** para aprovação |
| Modelo de pontuação | **Compensatório**: não é preciso passar em cada domínio, só na prova como um todo |
| Chute | Questão em branco conta como errada e **não há penalidade** por errar. Nunca deixe em branco |
| Público-alvo | Até 6 meses de exposição à AWS; papéis técnicos e não técnicos |
| Fora do escopo | Programar, projetar arquitetura, troubleshooting, implementação, testes de carga |
| Valor | US$ 100 (confira o preço e os descontos vigentes no site de certificação) |

### Domínios do exame CLF-C02 (pesos oficiais)

| Domínio | Peso |
|---|---|
| Cloud Concepts (Conceitos de nuvem) | 24% |
| Security and Compliance (Segurança e conformidade) | 30% |
| Cloud Technology and Services (Tecnologia e serviços de nuvem) | 34% |
| Billing, Pricing, and Support (Faturamento, preços e suporte) | 12% |

---

## 1. Conceitos de Nuvem

> **Regra de ouro da prova**: computação em nuvem é a **entrega sob demanda** de recursos de TI pela internet com **preço pago conforme o uso**. Quando o enunciado pergunta "qual é o benefício da nuvem", a resposta quase sempre é uma das **seis vantagens** abaixo, escrita com outras palavras.

### Benefícios da nuvem AWS

#### As seis vantagens da computação em nuvem
A AWS descreve seis vantagens no whitepaper *Overview of Amazon Web Services*. Decore a ideia de cada uma, porque as alternativas costumam parafrasear o texto:

| Vantagem | O que significa | Como aparece no enunciado |
|---|---|---|
| **Trocar despesa fixa (CapEx) por despesa variável (OpEx)** | Em vez de comprar servidores e data centers antes de saber como vão ser usados, você paga só pelo que consome | "Evitar investimento inicial alto", "pagar somente pelo uso" |
| **Beneficiar-se de enormes economias de escala** | A AWS agrega o uso de centenas de milhares de clientes e repassa custos menores em preço por unidade | "Preços menores que o cliente conseguiria sozinho" |
| **Parar de adivinhar a capacidade** | Aumente ou reduza a capacidade conforme a demanda real, sem superdimensionar nem faltar recurso | "Evitar recursos ociosos ou falta de capacidade em picos" |
| **Aumentar velocidade e agilidade** | Novos recursos ficam disponíveis em minutos, e o custo de experimentar cai | "Reduzir o tempo para disponibilizar recursos de semanas para minutos" |
| **Parar de gastar com a operação de data centers** | Foque nos clientes e no produto, não em rack, energia e refrigeração | "Concentrar-se no negócio em vez da infraestrutura" |
| **Tornar-se global em minutos** | Implante em várias Regiões do mundo com poucos cliques | "Baixa latência para usuários em outros continentes" |

#### Conceitos que a prova diferencia
- **Elasticidade**: adquirir recursos quando precisa e liberá-los quando não precisa mais, **automaticamente**, acompanhando a demanda. Exemplo: Auto Scaling adicionando instâncias no pico e removendo à noite.
- **Escalabilidade**: capacidade de crescer para atender a uma carga maior. **Vertical** (scale up) aumenta o tamanho de um recurso; **horizontal** (scale out) adiciona mais recursos iguais.
- **Alta disponibilidade**: o sistema continua acessível com o mínimo de interrupção, em geral distribuindo recursos por várias **Availability Zones**.
- **Tolerância a falhas**: o sistema continua funcionando **sem degradação** mesmo quando um componente falha. É um nível acima de alta disponibilidade.
- **Agilidade**: rapidez para experimentar, inovar e entregar, porque o recurso chega em minutos e o custo do erro é baixo.
- **Alcance global e velocidade de implantação**: benefícios diretos da infraestrutura global (Regiões, AZs e edge locations; veja a seção 2).

#### Modelos de serviço
- **IaaS (Infrastructure as a Service)**: você recebe blocos básicos (servidores, rede, armazenamento) e controla o sistema operacional para cima. Exemplo: **Amazon EC2**.
- **PaaS (Platform as a Service)**: a AWS gerencia a infraestrutura e a plataforma; você cuida do código e dos dados. Exemplos: **AWS Elastic Beanstalk**, **Amazon RDS** (do ponto de vista do banco).
- **SaaS (Software as a Service)**: produto completo, operado pelo provedor; você só usa. Exemplos: **Amazon WorkSpaces**, **Amazon Connect**, softwares vendidos no **AWS Marketplace**.
- Quanto mais alto o modelo (IaaS → PaaS → SaaS), **menos responsabilidade** fica com o cliente. Isso conecta diretamente com o modelo de responsabilidade compartilhada (seção 3).

#### Modelos de implantação
- **Nuvem (cloud / all-in)**: toda a aplicação roda na nuvem, seja criada nela ou migrada.
- **Híbrido**: conecta recursos na nuvem à infraestrutura existente on-premises. Exemplos de serviços: **AWS Direct Connect**, **Site-to-Site VPN**, **AWS Storage Gateway**, **AWS Outposts**.
- **On-premises (nuvem privada)**: recursos em data center próprio, com virtualização e ferramentas de automação. A AWS oferece **Outposts** para levar serviços AWS para dentro do data center do cliente.

### Princípios de projeto: AWS Well-Architected Framework

> **Regra de ouro da prova**: o Well-Architected tem **seis pilares**. A prova dá uma prática ou um objetivo e pergunta a qual pilar ele pertence. Associe cada pilar a uma palavra: **operar**, **proteger**, **recuperar**, **usar bem**, **gastar bem**, **impactar menos**.

#### Os seis pilares

| Pilar | Foco em uma frase | Palavras-chave no enunciado | Princípios de design mais cobrados |
|---|---|---|---|
| **Excelência operacional** (Operational Excellence) | Executar e monitorar sistemas e melhorar processos continuamente | Operações como código, runbooks, pequenas mudanças reversíveis, aprender com falhas | Executar operações como código; fazer mudanças frequentes, pequenas e reversíveis; antecipar falhas; aprender com todos os eventos operacionais |
| **Segurança** (Security) | Proteger dados, sistemas e ativos | Identidade, rastreabilidade, criptografia, menor privilégio | Base de identidade forte; habilitar rastreabilidade; aplicar segurança em todas as camadas; automatizar boas práticas; proteger dados em trânsito e em repouso; manter pessoas longe dos dados; preparar-se para incidentes |
| **Confiabilidade** (Reliability) | Executar a função pretendida de forma correta e consistente e se recuperar de falhas | Recuperação automática, Multi-AZ, backup, testar recuperação | Recuperar automaticamente de falhas; testar procedimentos de recuperação; escalar horizontalmente; parar de adivinhar capacidade; gerenciar mudanças com automação |
| **Eficiência de desempenho** (Performance Efficiency) | Usar recursos computacionais de forma eficiente conforme a demanda muda | Escolher o tipo certo, serverless, global em minutos, experimentar | Democratizar tecnologias avançadas; tornar-se global em minutos; usar arquiteturas serverless; experimentar com mais frequência; considerar a "simpatia mecânica" |
| **Otimização de custos** (Cost Optimization) | Entregar valor de negócio pelo menor preço | Rightsizing, pagar pelo consumo, atribuir gastos, parar de pagar por ocioso | Implementar gestão financeira de nuvem; adotar modelo de consumo; medir a eficiência geral; parar de gastar com trabalho pesado indiferenciado; analisar e atribuir despesas |
| **Sustentabilidade** (Sustainability) | Minimizar o impacto ambiental da carga de trabalho | Maximizar utilização, hardware mais eficiente, serviços gerenciados, reduzir desperdício | Entender seu impacto; definir metas de sustentabilidade; maximizar a utilização; adotar hardware e software mais eficientes; usar serviços gerenciados; reduzir o impacto downstream |

#### Diferenças entre pilares que confundem
- **Confiabilidade vs. desempenho**: "recuperar-se de falha de uma AZ" é confiabilidade; "escolher instância otimizada para computação para reduzir o tempo de processamento" é desempenho.
- **Custo vs. sustentabilidade**: os dois gostam de "desligar recursos ociosos". Se o enunciado fala em **gasto**, é custo; se fala em **impacto ambiental, energia ou emissões**, é sustentabilidade.
- **Excelência operacional vs. confiabilidade**: "fazer mudanças pequenas e reversíveis" e "operações como código" são excelência operacional; "testar a recuperação" e "recuperar automaticamente" são confiabilidade.
- **Segurança**: "habilitar rastreabilidade" (logs, CloudTrail) e "aplicar segurança em todas as camadas" são princípios de segurança, não de operação.

#### Ferramentas do Well-Architected
- **AWS Well-Architected Tool**: serviço gratuito no console para revisar uma carga de trabalho contra as boas práticas dos seis pilares, registrar riscos (alto e médio) e acompanhar um plano de melhoria.
- **Lenses**: extensões com perguntas específicas de um domínio, como Serverless, SaaS, Machine Learning e IA generativa.
- **Well-Architected Reviews** também fazem parte do plano **Enterprise Support** (seção 11).

### Princípios de design de arquitetura em nuvem

> **Regra de ouro da prova**: além dos princípios *de cada pilar*, existem os **princípios gerais de design** do Well-Architected e um vocabulário de arquitetura que a prova cobra sem citar serviço nenhum. Quando a alternativa fala de **monolito, capacidade de pico fixa, servidor "especial", processo manual ou decisão única**, ela está errada por princípio.

#### Princípios gerais de design do Well-Architected

Cobrados quase literalmente em questões do tipo "qual é um princípio de design da AWS Cloud?":

| Princípio | O que significa | Como aparece no enunciado |
|---|---|---|
| **Pare de adivinhar a capacidade** | Meça a demanda real e escale, em vez de dimensionar para o pico | "Provisionar mais capacidade do que a carga precisa" é o **distrator** |
| **Teste sistemas em escala de produção** | Na nuvem é barato criar um ambiente igual ao de produção, testar e destruir | "Testar apenas com demanda moderada" é o distrator |
| **Automatize para facilitar a experimentação arquitetural** | IaC e automação deixam criar, testar e reverter arquiteturas a baixo custo | "Enfatizar processos manuais" é o distrator |
| **Permita arquiteturas evolutivas** | A arquitetura muda com o tempo; decisão arquitetural **não é evento único** | "Tornar as decisões estáticas e únicas" é o distrator |
| **Oriente arquiteturas usando dados** | Decida com base em métricas do comportamento real da carga, não em palpite | "Tomar decisões baseadas em dados para determinar o design" |
| **Melhore com dias de teste** (*game days*) | Simule falhas e picos em produção para treinar a equipe e validar procedimentos | "Simular falhas para testar os processos de recuperação" |

#### Conceitos de arquitetura que a prova cobra

| Conceito | O que é | Onde aparece |
|---|---|---|
| **Acoplamento fraco** (*loosely coupled*) | Componentes independentes que conversam por **fila, tópico ou API**. A falha ou a lentidão de um **não derruba** os outros, e cada um escala sozinho | Decompor **monolito em microsserviços** com ECS/EKS, SQS, SNS ou Lambda. "Arquitetura fortemente acoplada" é sempre o distrator |
| **Sem estado** (*stateless*) | O servidor **não guarda** dados de sessão; qualquer instância atende qualquer requisição. O estado vai para DynamoDB, ElastiCache ou S3 | Pré-requisito para escalar horizontalmente e para o Auto Scaling substituir instâncias livremente |
| **Com estado** (*stateful*) | O servidor guarda a sessão localmente, então o usuário precisa voltar sempre à mesma instância (*sticky sessions*) | Limita a escala; carga "com estado" de 3 anos leva a **Reserved Instances** |
| **Recursos descartáveis** (*disposable resources*) | Tratar servidor como peça substituível, não como bicho de estimação: em vez de consertar, **destrua e recrie** a partir de AMI, user data ou CloudFormation | "Considere servidores como recursos **não** descartáveis" é o distrator |
| **Paralelismo** | Em vez de uma instância enorme, use **muitas instâncias em paralelo** (ou muitas tarefas/funções) | Transcodificar milhares de vídeos, processar lotes de imagens: a resposta é **várias instâncias em paralelo**, não uma instância com GPU gigante |
| **Redundância** | Duplicar componentes para eliminar ponto único de falha | É o princípio que sustenta a **alta disponibilidade** (implantar em ≥ 2 AZs) |
| **Elasticidade** | Ajustar a quantidade de recursos automaticamente conforme a demanda | É o princípio que sustenta a **escalabilidade** e elimina **CPU ociosa** |
| **Projetar para a falha** | Assuma que tudo falha e planeje a recuperação automática | Auto Scaling repondo instâncias, Multi-AZ, health checks do ELB |

- **Par cobrado direto**: "qual princípio garante **alta disponibilidade**?" → **redundância**. "Qual princípio garante **escalabilidade**?" → **elasticidade**. São duas questões diferentes com respostas diferentes.
- **Monolito em contêiner**: é **possível** mover uma aplicação monolítica para ECS/EKS **sem refatorar**, e às vezes é o primeiro passo (rehost/replatform). Mas ela **não ganha os benefícios de microsserviços** (escala e implantação independentes, falha isolada). Cuidado com alternativas que afirmam que o monolito "fica mais rápido" ou que "o ECS não aceita monolito" — as duas são falsas.

### Adoção e migração para a nuvem

#### AWS Cloud Adoption Framework (AWS CAF)
- É um guia de boas práticas da AWS para **planejar e acelerar a transformação digital** com a nuvem. Organiza as capacidades necessárias em **seis perspectivas**:

| Perspectiva | Grupo | Foco | Quem costuma participar |
|---|---|---|---|
| **Business** (Negócio) | Negócio | Garantir que os investimentos em nuvem aceleram os resultados de negócio | CEO, CFO, COO, CIO, CTO |
| **People** (Pessoas) | Negócio | Cultura, estrutura organizacional, liderança, capacitação e gestão da mudança | RH, líderes de pessoas |
| **Governance** (Governança) | Negócio | Orquestrar iniciativas, maximizar benefícios e minimizar riscos; gestão de programas, benefícios e riscos, finanças da nuvem | CIO, CFO, PMO, arquitetos corporativos |
| **Platform** (Plataforma) | Técnico | Construir uma plataforma de nuvem híbrida escalável e segura; arquitetura e engenharia | CTO, arquitetos, engenheiros |
| **Security** (Segurança) | Técnico | Confidencialidade, integridade e disponibilidade de dados e cargas | CISO, CCO, equipes de segurança |
| **Operations** (Operações) | Técnico | Garantir que os serviços de nuvem são entregues no nível acordado com o negócio | Gerentes de infraestrutura e operações, SRE |

- **Resultados de negócio** que o CAF promete (cobrados literalmente no guia do exame): **redução do risco de negócio**, **melhora no desempenho ESG** (ambiental, social e governança), **aumento de receita** e **aumento da eficiência operacional**.
- **Domínios de transformação**: Tecnologia, Processo, Organização e Produto.
- **Fases da jornada**: **Envision** (visualizar oportunidades), **Align** (alinhar e identificar lacunas entre as perspectivas), **Launch** (entregar pilotos em produção) e **Scale** (expandir os pilotos para o negócio).

#### Capacidades do CAF por perspectiva

> **Regra de ouro da prova**: a questão dá o nome de uma **capacidade** e pergunta a qual **perspectiva** ela pertence. Os distratores são sempre capacidades de *outra* perspectiva, então não há como deduzir: é reconhecimento. Ancore cada perspectiva em uma palavra — **Business** = valor, **People** = gente, **Governance** = controle, **Platform** = construir, **Security** = proteger, **Operations** = manter no ar.

| Perspectiva | Capacidades (as mais cobradas em **negrito**) |
|---|---|
| **Business** | Gestão de estratégia, gestão de portfólio, gestão de inovação, gestão de produto, **parceria estratégica**, monetização de dados, insights de negócio, ciência de dados |
| **People** | Evolução cultural, liderança transformacional, **fluência em nuvem**, transformação da força de trabalho, aceleração da mudança, design organizacional, alinhamento organizacional |
| **Governance** | Gestão de programas e projetos, **gestão de benefícios**, gestão de riscos, gestão financeira na nuvem, gestão do portfólio de aplicações, governança de dados, curadoria de dados, **gestão de mudanças e lançamentos** |
| **Platform** | Arquitetura de plataforma, **arquitetura de dados**, engenharia de plataforma, **engenharia de dados**, provisionamento e orquestração, desenvolvimento moderno de aplicações, **CI/CD** |
| **Security** | Governança de segurança, garantia de segurança, gestão de identidade e acesso, detecção de ameaças, gestão de vulnerabilidades, **proteção de infraestrutura**, proteção de dados, segurança de aplicações, **resposta a incidentes** |
| **Operations** | **Observabilidade**, gestão de eventos (AIOps), **gestão de incidentes e problemas**, gestão de mudanças e lançamentos, **gestão de desempenho e capacidade**, gestão de configuração, gestão de patches, **disponibilidade e continuidade**, gestão de aplicações |

- **Pares que mais confundem**: "**resposta a incidentes**" é **Security** (reagir a um evento de segurança); "**gestão de incidentes e problemas**" é **Operations** (reagir a uma falha operacional). "**Proteção de infraestrutura**" é **Security**, não Platform nem Operations. "**Observabilidade**" é **Operations**, não Platform.
- **CAF vs. Well-Architected**: se as alternativas forem *Sustentabilidade, Confiabilidade, Eficiência de desempenho, Segurança*, a pergunta sobre "perspectiva do CAF" tem uma única resposta possível — **Segurança**, porque é o único nome que existe nos dois frameworks. As outras são pilares do Well-Architected.
- *Atenção a um erro de gabarito conhecido: alguns simulados marcam "gerenciamento de incidentes e problemas" como capacidade da perspectiva **Security**. Pela documentação da AWS, ela é de **Operations**, e a dupla correta de Security naquele tipo de questão é **resposta a incidentes + proteção de infraestrutura**.*

#### Estratégias de migração: os 7 Rs

| Estratégia | O que faz | Exemplo típico |
|---|---|---|
| **Retire** (aposentar) | Desliga aplicações que não são mais necessárias | Sistema duplicado descoberto no inventário |
| **Retain** (reter) | Mantém on-premises por enquanto (dependência, conformidade, migração recente) | Mainframe que será revisto depois |
| **Rehost** ("lift and shift") | Move para a nuvem **sem alterar** a aplicação | Servidores físicos → EC2 com **AWS Application Migration Service** |
| **Relocate** | Move para a nuvem no nível do hipervisor, sem comprar hardware nem alterar a aplicação | VMware on-premises → VMware Cloud on AWS |
| **Replatform** ("lift, tinker and shift") | Faz algumas otimizações de nuvem sem mudar a arquitetura central | Banco em servidor próprio → **Amazon RDS** |
| **Repurchase** ("drop and shop") | Troca o produto por outro, em geral SaaS | CRM próprio → CRM SaaS do **AWS Marketplace** |
| **Refactor / Re-architect** | Reescreve para usar recursos nativos de nuvem | Monolito → microsserviços com Lambda e DynamoDB |

- **Replicação de banco de dados** (citada no guia do exame como estratégia de migração): o **AWS DMS** copia os dados enquanto o banco de origem continua em produção e mantém as mudanças sincronizadas (CDC) até a virada, reduzindo o tempo de parada.

#### Recursos e serviços que apoiam a migração

| Serviço | Para que serve |
|---|---|
| **Migration Evaluator** | Montar o **caso de negócio** e estimar o custo de rodar na AWS a partir do inventário on-premises (antigo TSO Logic) |
| **AWS Application Discovery Service** | Descobrir servidores on-premises, uso de recursos e **dependências** entre aplicações |
| **AWS Migration Hub** | Painel central para **acompanhar o progresso** de migrações feitas com várias ferramentas |
| **AWS Application Migration Service (MGN)** | Migração **rehost** de servidores (físicos, virtuais ou de outra nuvem) para EC2, com replicação contínua e virada rápida |
| **AWS Database Migration Service (DMS)** | Migrar bancos de dados com a origem em operação, entre engines iguais ou diferentes |
| **AWS Schema Conversion Tool (SCT)** | Converter esquema e código de banco em migrações **heterogêneas** (ex.: Oracle → Aurora PostgreSQL). A conversão também existe no console como **DMS Schema Conversion** |
| **AWS DataSync** | Transferência online e agendada de arquivos (NFS, SMB, HDFS, outras nuvens) para S3, EFS e FSx |
| **AWS Transfer Family** | Endpoints gerenciados de **SFTP, FTPS, FTP e AS2** com armazenamento em S3 ou EFS |
| **Família AWS Snow (legado)** | Dispositivos físicos com **duas funções**: (1) **transferência offline** de grandes volumes e (2) **processamento de dados no local** (computação na borda). Fechada para novos clientes desde 7/nov/2025, com fim do suporte previsto para 31/dez/2026. Ainda aparece em simulados como resposta para "petabytes com rede lenta" |
| **AWS Managed Services (AMS)** | A AWS **opera sua infraestrutura no dia a dia**: operações contínuas, gestão de mudanças, monitoramento e segurança automatizada, para adotar a nuvem em escala com menos equipe própria |
| **AWS Professional Services e Parceiros AWS** | Consultoria e execução da migração (seção 11) |

- **As duas caras do Snowball Edge** (os simulados cobram as duas):
  - **Transferência**: mover dezenas de TB a PB para a AWS quando a rede é lenta ou caríssima.
  - **Computação na borda**: **processar dados localmente** onde a conexão é **intermitente ou inexistente** (área isolada, navio, mina, campo). Palavras-chave: "conectividade limitada/intermitente", "processar localmente antes de enviar", "operar sem conexão estável à internet".
- *Simulados antigos citam **Snowmobile** (caminhão para **exabytes**, já aposentado) e **Snowcone** (descontinuado em 2024). Reconheça os nomes: em questão de simulado, "exabytes" continua levando a **Snowmobile** e "petabytes/conectividade ruim" a **Snowball Edge**, mesmo que hoje a AWS direcione para DataSync, Direct Connect ou Transfer Family.*
- **AMS vs. os outros três** (confusão clássica): **CAF** ajuda a *planejar* a adoção; **Well-Architected** ajuda a *revisar* a arquitetura; **AWS Support** *atende* quando você abre um caso; **AMS** *opera* o ambiente para você.

### Economia da nuvem

#### Custos fixos vs. variáveis e custos on-premises
- **Custo fixo (CapEx)**: comprar servidores, storage, rede e data center antes de usar, com depreciação ao longo de anos. O risco é pagar por capacidade ociosa ou ficar sem capacidade no pico.
- **Custo variável (OpEx)**: pagar pelo que usa, quando usa. É o modelo da nuvem.
- **Custos do ambiente on-premises** que a prova espera que você reconheça no **TCO (Total Cost of Ownership)**: hardware (servidores, storage, rede), **espaço físico, energia e refrigeração**, **equipe** de operação e manutenção, licenças de software, **ciclos de renovação** de hardware, redundância e capacidade ociosa para picos. Custos "invisíveis" (tempo de provisionamento, oportunidade perdida) também contam.
- Mover para a nuvem **transfere** parte desses custos para a AWS, mas **não elimina** custos com licenças, pessoal de nuvem e transferência de dados. A comparação justa é TCO contra TCO.

#### Estratégias de licenciamento
- **License Included**: o preço da instância ou do banco já inclui a licença (ex.: Windows Server no EC2, SQL Server ou Oracle SE2 no RDS). Simples e sem gestão de licença.
- **BYOL (Bring Your Own License)**: você reaproveita licenças que já possui. Licenças vinculadas a **socket ou núcleo físico** exigem **EC2 Dedicated Hosts**. O **AWS License Manager** controla o uso e evita violações de licença.
- A escolha depende do contrato existente: BYOL faz sentido quando a empresa já pagou por licenças com mobilidade; License Included faz sentido para quem não tem licença ou quer flexibilidade.

#### Rightsizing, automação e economias de escala
- **Rightsizing**: ajustar tipo e tamanho dos recursos ao uso real medido (CPU, memória, rede). É o primeiro passo de otimização de custos, **antes** de assumir compromissos como Savings Plans. Ferramentas: **AWS Compute Optimizer**, recomendações do **Cost Explorer** e **Trusted Advisor**.
- **Benefícios da automação**: menos erro humano, ambientes reproduzíveis, provisionamento rápido, escala automática e desligamento de recursos ociosos. Ferramentas: **CloudFormation** (infraestrutura como código), **Auto Scaling**, **Systems Manager**.
- **Economias de escala**: por comprar e operar em volume gigantesco, a AWS tem custo unitário menor e historicamente **reduz preços** ao longo do tempo. Além disso, alguns serviços têm **preço por faixa de volume** (quanto mais usa, menor o preço por GB), como o S3.

### Decisão rápida — Conceitos de Nuvem

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Evitar grande investimento inicial em hardware | Trocar despesa fixa por variável (pay-as-you-go) | Economias de escala, alcance global |
| Recursos que acompanham a demanda automaticamente | Elasticidade | Alta disponibilidade, agilidade |
| Provisionar em minutos e experimentar barato | Agilidade / velocidade | Economias de escala |
| Pilar que trata de recuperar-se de falhas | Confiabilidade | Excelência operacional, desempenho |
| Pilar que trata de operações como código e mudanças pequenas | Excelência operacional | Confiabilidade |
| Pilar que trata de reduzir impacto ambiental | Sustentabilidade | Otimização de custos |
| Medir e relatar o impacto ambiental do seu uso da AWS | AWS Customer Carbon Footprint Tool (no console de Billing) | Pilar de Sustentabilidade, Compute Optimizer |
| Revisar a carga contra as boas práticas | AWS Well-Architected Tool | Trusted Advisor, Config |
| Princípio que garante alta disponibilidade | Redundância | Elasticidade, segurança |
| Princípio que garante escalabilidade | Elasticidade | Redundância |
| Decompor monolito em microsserviços | Acoplamento fraco (loosely coupled) | Acoplamento forte, sem estado |
| Processar milhares de arquivos de mídia | Várias instâncias em paralelo | Uma instância com GPU, hardware dedicado |
| Criar ambiente igual ao de produção para validar | Testar sistemas em escala de produção | Testar com demanda moderada |
| Framework para planejar a transformação da organização | AWS Cloud Adoption Framework (CAF) | Well-Architected Framework |
| Perspectiva do CAF sobre capacitação e cultura | People (fluência em nuvem) | Governance, Business |
| Capacidade do CAF para definir e acompanhar resultados de negócio | Governance (gestão de benefícios) | Business, Operations |
| Capacidade do CAF para CI/CD e engenharia de dados | Platform | Operations, Governance |
| Capacidade do CAF para resposta a incidentes e proteção de infraestrutura | Security | Operations |
| Capacidade do CAF para observabilidade e gestão de incidentes | Operations | Security, Platform |
| AWS operar sua infraestrutura no dia a dia | AWS Managed Services (AMS) | CAF, Well-Architected, AWS Support |
| Mover servidores sem alterar nada | Rehost (MGN) | Refactor, Replatform |
| Migrar banco para RDS sem mudar a aplicação | Replatform | Rehost, Refactor |
| Trocar software próprio por SaaS | Repurchase | Rehost, Retain |
| Descobrir servidores e dependências on-premises | Application Discovery Service | Migration Hub, MGN |
| Montar o caso de negócio da migração | Migration Evaluator | Pricing Calculator, Cost Explorer |
| Migrar banco mantendo a origem em operação | AWS DMS | SCT sozinho, Snowball |
| Converter esquema Oracle para PostgreSQL | AWS SCT / DMS Schema Conversion | DMS sozinho |
| Reaproveitar licença por núcleo físico | BYOL em Dedicated Hosts | Dedicated Instances, Spot |

---

## 2. Infraestrutura Global

> **Regra de ouro da prova**: **Região** contém **Availability Zones**; AZ contém **um ou mais data centers**; **edge locations** ficam fora das Regiões, perto dos usuários. Alta disponibilidade usa **várias AZs**; recuperação de desastres regional, soberania de dados e latência global usam **várias Regiões**.

### Regiões, Availability Zones e edge locations

#### Componentes da infraestrutura global

| Componente | O que é | Para que serve |
|---|---|---|
| **Região (Region)** | Área geográfica isolada com várias AZs (em geral **três ou mais**). Hoje são mais de 30 Regiões no mundo | Escolher onde os dados e recursos ficam; isolamento de falhas e de conformidade |
| **Availability Zone (AZ)** | Um ou mais data centers discretos com **energia, rede e conectividade redundantes**, separados de outras AZs por distância significativa (até cerca de 100 km) e ligados por rede de baixa latência | Alta disponibilidade e tolerância a falhas dentro de uma Região |
| **Edge location** | Ponto de presença (PoP) em centenas de cidades, fora das Regiões | Cache e entrega de conteúdo (**CloudFront**), DNS (**Route 53**), aceleração de rede (**Global Accelerator**), proteção DDoS (**Shield**) |
| **Regional edge cache** | Cache intermediário maior, entre as edge locations e a origem | Manter conteúdo menos acessado mais perto dos usuários |
| **Local Zone** | Extensão de uma Região em uma área metropolitana, com computação e storage | Latência de um dígito de milissegundo para usuários de uma cidade (ex.: edição de vídeo, jogos) |
| **Wavelength Zone** | Infraestrutura AWS dentro da rede **5G** de operadoras de telecom | Aplicações móveis de ultrabaixa latência |
| **AWS Outposts** | Racks e servidores da AWS instalados **no data center do cliente** | Serviços AWS on-premises para latência local, processamento local ou residência de dados |

- **AZs não compartilham ponto único de falha**: cada AZ tem energia, refrigeração e rede independentes. Por isso distribuir recursos em **pelo menos duas AZs** protege contra a falha de um data center inteiro.
- **Duas perguntas parecidas com respostas diferentes** — leia com atenção qual está sendo feita:
  - "**Em quantas AZs implantar** para ter alta disponibilidade?" → **no mínimo duas**. Vale em qualquer versão do material e é a resposta certa sempre.
  - "**Quantas AZs uma Região tem?**" → a AWS hoje projeta Regiões com **no mínimo três** AZs, e a documentação atual usa esse número. *Porém muitos simulados e cursos antigos ainda afirmam "pelo menos duas". Se a alternativa "pelo menos três" existir e a questão for sobre a doc atual, ela é a correta; em simulado antigo, espere **duas** como gabarito.*
- **Serviços globais vs. regionais**: a maioria dos serviços é **regional** (EC2, RDS, VPC, Lambda). Alguns são **globais**: **IAM**, **Route 53**, **CloudFront**, **AWS Organizations** e **WAF** associado ao CloudFront. O S3 tem namespace global de nomes de bucket, mas **cada bucket fica em uma Região**.

#### Como escolher uma Região
Quatro critérios, nesta ordem de prioridade típica:
1. **Conformidade e soberania de dados**: leis e contratos podem exigir que os dados fiquem em um país. É o critério que decide sozinho quando existe. Os dados **não saem da Região** escolhida a menos que o cliente os mova.
2. **Proximidade dos usuários (latência)**: quanto mais perto, menor a latência.
3. **Serviços e recursos disponíveis**: nem todo serviço ou tipo de instância existe em todas as Regiões.
4. **Preço**: o mesmo serviço pode custar diferente entre Regiões.

### Alta disponibilidade e múltiplas Regiões

#### Várias AZs: alta disponibilidade
- Distribua instâncias em **várias AZs** atrás de um **Elastic Load Balancer** e use **Auto Scaling** para repor capacidade. Se uma AZ falhar, as outras continuam atendendo.
- Serviços gerenciados já fazem isso por você: **S3** (Standard) guarda dados em no mínimo três AZs, **DynamoDB** replica entre AZs automaticamente, **RDS Multi-AZ** mantém um standby em outra AZ, **Aurora** guarda seis cópias em três AZs, **EFS** (Regional) é multi-AZ.

#### Várias Regiões: quando usar
O guia do exame lista quatro motivos:
- **Recuperação de desastres (DR)**: sobreviver à perda de uma Região inteira.
- **Continuidade de negócios**: manter a operação em outra Região durante incidentes graves.
- **Baixa latência para usuários finais** espalhados pelo mundo.
- **Soberania de dados**: manter dados de clientes de um país dentro dele.
- Usar várias Regiões **aumenta custo e complexidade** (replicação, transferência de dados entre Regiões). Para alta disponibilidade comum, várias AZs bastam.
- Serviços que ajudam: **Route 53** (failover e roteamento por latência), **CloudFront**, **Global Accelerator**, **S3 Cross-Region Replication**, **DynamoDB Global Tables**, **Aurora Global Database**, **AWS Elastic Disaster Recovery**.

#### Benefícios das edge locations
- Aproximam o conteúdo e a entrada da rede AWS do usuário, reduzindo **latência**.
- Absorvem ataques na borda (**Shield** e **WAF** no CloudFront).
- Reduzem a carga na origem, porque o conteúdo em cache não volta ao servidor.

### Decisão rápida — Infraestrutura Global

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Continuar funcionando se um data center falhar | Implantar em várias AZs | Várias edge locations, instância maior |
| Sobreviver à falha de uma Região inteira | Várias Regiões (DR) | Várias AZs |
| Dados devem ficar em um país por lei | Escolher a Região nesse país | Edge location, Local Zone por padrão |
| Entregar conteúdo estático com baixa latência global | CloudFront (edge locations) | Mais instâncias EC2 em uma Região |
| Latência de um dígito de ms em uma cidade sem Região | Local Zone | Outposts, Wavelength |
| Aplicação móvel 5G de ultrabaixa latência | Wavelength Zone | Local Zone |
| Serviços AWS dentro do data center do cliente | AWS Outposts | Local Zone, Storage Gateway |
| Primeiro critério ao escolher uma Região com exigência legal | Conformidade / soberania de dados | Preço, latência |
| Serviço global (não regional) | IAM, Route 53, CloudFront, Organizations | EC2, RDS, VPC |

---

## 3. Segurança e Conformidade

> **Regra de ouro da prova**: a AWS é responsável pela segurança **DA** nuvem; o cliente é responsável pela segurança **NA** nuvem. Diante de qualquer tarefa, pergunte: "isso é hardware, instalação física ou software do serviço gerenciado?" (AWS) ou "isso é dado, identidade, configuração ou código meu?" (cliente).

### Fundamentos: o que a segurança protege

Parte das questões cobra o **conceito**, sem citar serviço nenhum: "qual é o objetivo da criptografia?", "qual é o objetivo do controle de acesso?". Cada mecanismo defende uma propriedade diferente:

| Propriedade | O que garante | Mecanismo que a defende |
|---|---|---|
| **Confidencialidade** | Só quem tem autorização **consegue ler** o dado | **Criptografia** (em repouso e em trânsito), KMS, TLS |
| **Integridade** | O dado **não foi alterado** indevidamente | Hashes e checksums, versionamento, Object Lock, assinatura |
| **Disponibilidade** | O dado e o sistema **continuam acessíveis** | Multi-AZ, backups, Auto Scaling, Shield contra DDoS |
| **Autenticidade** | O usuário **é quem diz ser** | Senha + **MFA / autenticação de dois fatores** |
| **Autorização (controle de acesso)** | **Apenas usuários autorizados** acessam cada recurso | **IAM**: políticas, roles, menor privilégio |

- **Pares que a prova separa**:
  - "Objetivo da **criptografia**" → **confidencialidade** (não integridade, não disponibilidade).
  - "Objetivo do **controle de acesso**" → garantir que **apenas usuários autorizados** tenham acesso.
  - "Vantagem da **autenticação de dois fatores**" → **garantir a autenticidade do usuário** (não "aumentar a complexidade da senha" nem "reduzir o número de senhas").
- **Criptografia em trânsito** é a resposta para "melhorar a segurança dos dados que trafegam": use **HTTPS ou SSL/TLS**. RDP e FTP não são resposta.

### Modelo de responsabilidade compartilhada

#### Quem cuida de quê

| Responsabilidade da AWS (segurança **da** nuvem) | Responsabilidade do cliente (segurança **na** nuvem) |
|---|---|
| Segurança física dos data centers (acesso, guardas, energia, refrigeração) | **Dados** do cliente e sua classificação |
| Hardware, rede global, Regiões, AZs e edge locations | **IAM**: usuários, grupos, roles, políticas, MFA |
| Camada de virtualização (hipervisor) | **Sistema operacional convidado** no EC2 (patches e atualizações) |
| Software dos serviços gerenciados (ex.: patch do engine no RDS, runtime do Lambda) | Aplicações e código |
| Descarte seguro de mídias de armazenamento | Configuração de **security groups**, network ACLs e firewall do SO |
| | **Criptografia**: escolher e habilitar (lado cliente e lado servidor) e proteger o tráfego |

#### Controles compartilhados, herdados e específicos
- **Controles herdados**: o cliente herda integralmente da AWS. Exemplo: controles **físicos e ambientais** dos data centers.
- **Controles compartilhados**: cada lado faz a sua parte em uma camada diferente:
  - **Gestão de patches**: a AWS corrige a infraestrutura; o cliente corrige o SO convidado e as aplicações.
  - **Gestão de configuração**: a AWS configura seus dispositivos; o cliente configura SO, bancos e aplicações.
  - **Conscientização e treinamento**: a AWS treina seus funcionários; o cliente treina os seus.
- **Controles específicos do cliente**: responsabilidade só do cliente, como proteção de dados e roteamento em zonas de segurança.

#### Como a responsabilidade muda conforme o serviço

| Serviço | AWS cuida de | Cliente cuida de |
|---|---|---|
| **Amazon EC2** (IaaS) | Hardware, rede, hipervisor | SO convidado e patches, aplicações, security groups, dados, IAM |
| **Amazon RDS** (gerenciado) | Hardware, SO do servidor, **instalação e patch do engine**, backups automáticos | Usuários do banco, security groups, habilitar criptografia, janela de manutenção, dados, estrutura das tabelas |
| **AWS Lambda** (serverless) | Servidores, SO, runtime, escala e disponibilidade | Código da função, permissões IAM (execution role), dados e configuração |
| **Amazon S3** | Infraestrutura, durabilidade, disponibilidade | Políticas de bucket e acesso, criptografia escolhida, versionamento, dados |
| **Amazon DynamoDB** | Tudo abaixo da tabela, incluindo patch e escala | Controle de acesso, dados, criptografia com chave própria se exigido |

- Quanto **mais gerenciado** o serviço, **mais responsabilidade** passa para a AWS. Mas **dados e controle de acesso** são sempre do cliente, em qualquer serviço.

### AWS IAM e gestão de acesso

> **Regra de ouro da prova**: **usuário** é uma pessoa ou aplicação com credencial de longo prazo; **grupo** reúne usuários para aplicar permissões; **role** é uma identidade **assumida temporariamente** por serviços, aplicações, outras contas ou usuários federados; **política** é o documento JSON que concede ou nega permissões.

#### Identidades do IAM
- **IAM** é um serviço **global** e **gratuito** que controla **quem** (autenticação) pode fazer **o quê** (autorização) em quais recursos.
- **Usuário do IAM**: identidade com credenciais permanentes (senha para o console e/ou **access keys** para acesso programático). Nova identidade começa **sem nenhuma permissão**.
- **Grupo do IAM**: coleção de usuários. Permissões atribuídas ao grupo valem para todos os membros. Grupos **não** podem conter outros grupos e **não** são identidades que fazem login.
- **Role do IAM**: identidade sem credencial permanente. Quem a assume recebe **credenciais temporárias** do **AWS STS**. Usos clássicos: instância EC2 acessando S3 (instance profile), função Lambda acessando DynamoDB, **acesso entre contas** (cross-account role) e usuários federados.
- **Boa prática**: prefira **roles com credenciais temporárias** a access keys de longo prazo. Nunca coloque access keys em código, AMIs ou repositórios.

#### Políticas e menor privilégio
- **Política do IAM**: documento JSON com `Effect` (Allow/Deny), `Action`, `Resource` e, opcionalmente, `Condition`.
- **Tipos**:
  - **AWS managed**: criadas e mantidas pela AWS (ex.: `ReadOnlyAccess`). Práticas para começar, mas costumam ser amplas.
  - **Customer managed**: criadas por você, reutilizáveis e versionadas. Melhores para aplicar **menor privilégio**.
  - **Inline**: embutidas em uma única identidade, relação 1:1.
  - **Baseadas em recurso**: anexadas ao recurso, como **bucket policy** do S3.
- **Avaliação**: por padrão tudo é negado (**deny implícito**). Um `Allow` concede. Um **`Deny` explícito sempre vence**.
- **Princípio do menor privilégio**: conceda só as permissões necessárias para a tarefa, e nada mais. Comece restrito e amplie conforme a necessidade.
- **Ferramentas para ajustar permissões**: **IAM Access Analyzer** (acessos externos e políticas amplas; gera políticas a partir da atividade), **último acesso** (access advisor) e **credential report** (relatório de todos os usuários da conta e do estado de senha, access keys e MFA). Os dois últimos são os "relatórios de acesso" citados no guia do exame.

#### Autenticação, senhas e credenciais
- **MFA (autenticação multifator)**: algo que você sabe (senha) + algo que você tem (app autenticador, chave de segurança FIDO/passkey, token de hardware). Habilite para o root e para todos os usuários.
- **Política de senhas**: define tamanho mínimo, complexidade, expiração e reutilização para usuários do IAM.
- **Access keys**: par access key ID + secret access key para CLI, SDK e API. Faça **rotação** periódica, remova as que não usa e prefira roles.
- **Onde guardar segredos**:
  - **AWS Secrets Manager**: senhas de banco, chaves de API e tokens com **rotação automática** (integrada ao RDS, Aurora, Redshift e DocumentDB). Cobrado por segredo e por chamada de API.
  - **AWS Systems Manager Parameter Store**: parâmetros de configuração e segredos (`SecureString`, criptografados pelo KMS). A camada padrão é gratuita, mas **não tem rotação automática nativa**.
- **Métodos de autenticação na AWS** listados no guia: **MFA**, **IAM Identity Center** (login único) e **cross-account roles**.

#### Usuário raiz (root user)
- É a identidade criada com a conta, com **acesso total e irrestrito**. Não pode ser limitada por políticas do IAM na própria conta.
- **Como proteger o root**:
  - Habilitar **MFA** (hoje exigido por padrão para o root) e usar senha forte.
  - **Não criar access keys** para o root (e apagar as existentes).
  - Usar o root **somente** para tarefas que o exigem; no dia a dia, usar usuário administrativo no **IAM Identity Center** ou no IAM.
  - Monitorar o uso do root (alarme no CloudTrail/EventBridge).
  - Em **AWS Organizations**, habilitar o **gerenciamento centralizado de acesso root** e **remover as credenciais root das contas-membro**.
- **Tarefas que só o root pode fazer** (as mais cobradas):
  - Alterar configurações da conta, como **e-mail do root, senha do root e access keys do root** (conta avulsa).
  - **Fechar a conta** AWS (conta avulsa, fora de Organizations).
  - **Restaurar permissões do IAM** quando o único administrador revogou as próprias permissões.
  - **Ativar o acesso do IAM ao console de Billing and Cost Management**.
  - Visualizar certas notas fiscais de impostos.
  - **Registrar-se como vendedor no Reserved Instance Marketplace**.
  - **Configurar MFA Delete** em um bucket S3.
  - Editar ou excluir uma **bucket policy do S3** ou **política de fila SQS** que nega acesso a todos os principals.
  - Inscrever-se no **AWS GovCloud (US)**.
- *Simulados antigos incluem "alterar ou cancelar o plano de suporte" entre as tarefas exclusivas do root. A lista atual da documentação do IAM não traz mais esse item. Se ele aparecer como alternativa, prefira os itens acima.*

#### Tipos de gestão de identidade
- **IAM Identity Center** (sucessor do AWS SSO): **login único para a força de trabalho** em várias contas da Organization e em aplicações. Integra-se a provedores externos (Microsoft Entra ID, Okta) via SAML 2.0 e SCIM, ou usa diretório próprio. É a recomendação atual para acesso humano.
- **Federação**: usuários autenticam em um provedor de identidade externo (IdP corporativo via **SAML 2.0**, ou OIDC) e recebem credenciais temporárias na AWS, sem precisar de usuário do IAM.
- **Amazon Cognito**: identidade para **usuários finais de aplicações** web e mobile (cadastro, login, login social com Google/Apple/Facebook, MFA). Não é para funcionários acessarem o console.
- **AWS Directory Service**: Microsoft Active Directory gerenciado (**AWS Managed Microsoft AD**), **AD Connector** (proxy para o AD on-premises) ou **Simple AD**.
- **AWS Resource Access Manager (RAM)**: compartilhar recursos (sub-redes, Transit Gateway, regras do Route 53 Resolver, configurações do License Manager) entre contas, sem duplicá-los.

### Governança multi-conta

#### AWS Organizations
- Gerencia várias contas AWS de forma centralizada. A **conta de gerenciamento** (management account) cria a organização; as demais são **contas-membro**, agrupadas em **unidades organizacionais (OUs)**.
- **Faturamento consolidado** (consolidated billing): **uma fatura** para todas as contas, **somatório do uso** para alcançar descontos por volume (ex.: faixas do S3) e **compartilhamento de descontos** de Reserved Instances e Savings Plans entre as contas (o compartilhamento pode ser desativado por conta). Não tem custo adicional.
- **Service Control Policies (SCPs)**: definem o **máximo de permissões** disponíveis nas contas-membro de uma OU ou conta. **SCP não concede permissão**: ela só limita. Valem inclusive para o **root das contas-membro**, mas **não afetam a conta de gerenciamento**.
- Usos típicos de SCP: bloquear Regiões não aprovadas, impedir que alguém desative o CloudTrail, proibir serviços não autorizados.

#### AWS Control Tower
- Configura e governa um **ambiente multi-conta seguro** seguindo boas práticas, criando uma **landing zone** sobre o Organizations.
- **Controls (guardrails)**: **preventivos** (implementados com SCPs), **detectivos** (com AWS Config) e **proativos** (verificam recursos antes do provisionamento, com hooks do CloudFormation).
- **Account Factory**: cria novas contas já em conformidade, publicado como produto do **AWS Service Catalog**.
- **Como ele cria os recursos**: o Control Tower provisiona a landing zone e os recursos das contas usando **AWS CloudFormation** (StackSets) nos bastidores. A prova pergunta isso direto: *"qual serviço o Control Tower usa para criar recursos?"* → **CloudFormation**.
- **Palavra-chave**: "configurar rapidamente um ambiente multi-conta com boas práticas e guardrails" leva a **Control Tower**. "Aplicar políticas a contas" sozinho leva a **Organizations/SCP**.

### Proteção de dados e criptografia

#### Criptografia em repouso e em trânsito
- **Em repouso** (at rest): dados armazenados em disco. Exemplos: criptografia de volumes **EBS**, buckets **S3** (criptografados por padrão com SSE-S3 desde 2023), bancos **RDS**, tabelas **DynamoDB** (criptografadas por padrão). A maioria usa chaves do **AWS KMS**.
- **Em trânsito** (in transit): dados trafegando pela rede, protegidos com **TLS/HTTPS** ou VPN (IPsec). Certificados TLS vêm do **AWS Certificate Manager (ACM)**.
- **Benefícios da criptografia na nuvem**: integração nativa com os serviços, gerenciamento centralizado de chaves, auditoria de uso de chaves pelo CloudTrail e conformidade com normas que exigem criptografia.
- **Lado servidor vs. lado cliente**: no lado servidor, o serviço AWS criptografa ao gravar; no lado cliente, a aplicação criptografa **antes** de enviar à AWS.

#### Serviços de chaves, certificados e dados sensíveis

| Serviço | O que é | Quando é a resposta |
|---|---|---|
| **AWS KMS (Key Management Service)** | Serviço gerenciado para criar e controlar chaves de criptografia, com HSMs gerenciados pela AWS e integração a mais de 100 serviços | "Criar e gerenciar chaves de criptografia", "controlar quem usa as chaves", "auditar uso das chaves" |
| **AWS CloudHSM** | **HSM dedicado** (single-tenant) na nuvem, em que **só o cliente** controla as chaves | "Hardware dedicado", "controle exclusivo das chaves", requisitos regulatórios estritos |
| **AWS Certificate Manager (ACM)** | Provisiona, gerencia e **renova automaticamente** certificados SSL/TLS. Certificados públicos para ELB, CloudFront e API Gateway não têm custo | "Certificado HTTPS", "renovação automática de certificado" |
| **AWS Secrets Manager** | Armazena e **rotaciona** segredos | "Rotacionar senha do banco automaticamente" |
| **Amazon Macie** | Usa machine learning para **descobrir e proteger dados sensíveis (PII)** no **S3** | "Encontrar dados pessoais/sensíveis em buckets S3" |

### Segurança de rede e de aplicações

#### Security groups vs. network ACLs

| Característica | Security group | Network ACL (NACL) |
|---|---|---|
| Nível | **Instância** (interface de rede / ENI) | **Sub-rede** |
| Estado | **Stateful**: a resposta de uma conexão permitida volta automaticamente | **Stateless**: regras de entrada e saída avaliadas separadamente |
| Regras | Somente **permitir** (allow) | **Permitir e negar** (allow e deny) |
| Avaliação | Todas as regras são avaliadas | Em **ordem numérica**; a primeira que casa decide |
| Padrão | Nega toda entrada e permite toda saída | A NACL padrão permite tudo |
| Bloquear um IP específico | Não é possível (não há deny) | **Sim** |

#### Proteção de borda e firewall

| Serviço | O que faz | Palavra-chave |
|---|---|---|
| **AWS Shield Standard** | Proteção **automática e gratuita** contra os ataques DDoS mais comuns nas camadas 3 e 4, para todos os clientes | "Proteção DDoS sem custo adicional" |
| **AWS Shield Advanced** | Proteção DDoS **paga** e avançada (inclusive camada 7 com WAF), acesso 24/7 ao **Shield Response Team (SRT)**, **proteção de custos** contra picos de cobrança causados pelo ataque e relatórios detalhados. Cobrança mensal por organização com compromisso de 1 ano | "Equipe especializada em DDoS", "reembolso de custos de escala durante ataque" |
| **AWS WAF** | Firewall de **aplicação web** (camada 7) que filtra requisições HTTP/HTTPS: SQL injection, cross-site scripting (XSS), IPs, países e limite de taxa (rate-based). Usado com CloudFront, ALB, API Gateway, AppSync e Cognito | "Bloquear SQL injection/XSS", "bloquear requisições de um país", "limitar requisições por IP" |
| **AWS Firewall Manager** | Gerencia **centralmente** regras de WAF, Shield Advanced, security groups, Network Firewall e DNS Firewall em **todas as contas** da Organization | "Aplicar regras de firewall de forma consistente em várias contas" |
| **AWS Network Firewall** | Firewall gerenciado e stateful no nível da **VPC** (filtragem e inspeção de tráfego) | "Inspecionar e filtrar o tráfego da VPC" |

### Detecção, auditoria e conformidade

#### Serviços de detecção e avaliação

| Serviço | O que faz | Não confundir com |
|---|---|---|
| **Amazon GuardDuty** | **Detecção de ameaças** contínua com machine learning, analisando CloudTrail, VPC Flow Logs e logs de DNS (e, opcionalmente, S3, EKS, RDS, malware em EBS) | Inspector (vulnerabilidades), Macie (dados sensíveis) |
| **Amazon Inspector** | **Varredura automatizada de vulnerabilidades** (CVEs) e exposição de rede em instâncias **EC2**, imagens de contêiner no **ECR** e funções **Lambda** | GuardDuty (ameaças ativas) |
| **Amazon Detective** | **Investiga a causa raiz** de achados de segurança, montando um grafo de relações a partir de logs | GuardDuty (detecta; Detective investiga) |
| **AWS Security Hub** | Painel central que **agrega achados** de GuardDuty, Inspector, Macie e parceiros e verifica conformidade com padrões (CIS, PCI DSS, AWS Foundational Security Best Practices) | Trusted Advisor (recomendações gerais) |
| **Amazon Macie** | Descoberta de **dados sensíveis** no S3 | GuardDuty |
| **AWS Trusted Advisor** | Recomendações de boas práticas, incluindo **verificações de segurança** (MFA no root, security groups com portas abertas, permissões de bucket S3, access keys expostas) | Inspector, Security Hub |

#### Logs e auditoria: onde encontrar cada informação
- **AWS CloudTrail**: registra **chamadas de API e ações** na conta: **quem** fez, **o quê**, **quando** e **de onde** (IP). O **Event history** guarda 90 dias de eventos de gerenciamento sem custo; para retenção longa, crie um **trail** que entrega ao S3 (ou use CloudTrail Lake). É a resposta para "auditar quem apagou o recurso".
- **AWS Config**: registra a **configuração dos recursos** e o **histórico de mudanças**, e avalia a conformidade com **Config rules** (ex.: "todo volume EBS deve estar criptografado"). É a resposta para "como o recurso estava configurado na semana passada" e "detectar recursos fora do padrão".
- **Amazon CloudWatch**: **métricas, logs e alarmes** de desempenho e operação (CPU, latência, erros). CloudWatch Logs centraliza logs de aplicações e sistemas.
- **VPC Flow Logs**: metadados do tráfego IP de VPC, sub-redes ou interfaces (origem, destino, porta, aceito/rejeitado).
- **Relatórios de acesso**: **credential report** e **último acesso** do IAM (veja "Políticas e menor privilégio").
- **Resumo para a prova**: CloudTrail = **quem fez**; Config = **como está e como estava configurado**; CloudWatch = **como está o desempenho**.

#### Conformidade: onde encontrar e o que varia
- **AWS Artifact**: portal **self-service e gratuito** com acesso sob demanda aos **relatórios de conformidade da AWS** (SOC 1/2/3, PCI DSS, ISO 27001 e outros emitidos por auditores terceiros) e aos **acordos** (como o BAA para HIPAA). É a resposta para "auditor pede comprovação de conformidade da AWS".
- **AWS Compliance Programs** (página de conformidade): lista os programas que a AWS atende por país e setor, como **LGPD**, **GDPR**, **HIPAA**, **PCI DSS** e **FedRAMP**.
- **A conformidade varia por serviço e por Região**: nem todo serviço está no escopo de todo programa (ex.: a lista de serviços **HIPAA eligible**), e exigências legais podem variar por localização. Consulte a página *AWS Services in Scope by Compliance Program*.
- **A AWS ser certificada não torna a aplicação do cliente conforme**: o cliente herda os controles físicos, mas precisa configurar os seus (responsabilidade compartilhada).
- **Testes de intrusão (pentest)**: permitidos sem aprovação prévia em uma lista de serviços (como EC2, RDS, Aurora, CloudFront, API Gateway, Lambda, Lightsail e Elastic Beanstalk). Testes de **DoS/DDoS** e ataques como *DNS zone walking* seguem política própria ou são proibidos.

#### Fontes de informação de segurança
- **AWS Security Center** (aws.amazon.com/security): visão geral de segurança, conformidade, boletins e recursos.
- **AWS Security Blog**: artigos e anúncios de segurança.
- **AWS Knowledge Center** e **AWS re:Post**: respostas a dúvidas frequentes e comunidade.
- **AWS Marketplace**: produtos de segurança de **terceiros** (firewalls, antivírus, SIEM) prontos para usar na AWS.
- **AWS Trust & Safety**: equipe que recebe **denúncias de abuso** vindas de recursos AWS (spam, phishing, malware, ataques DDoS partindo da AWS, conteúdo ilegal). Denuncie pelo formulário de abuso ou por abuse@amazonaws.com. Não é o suporte técnico.

### Decisão rápida — Segurança e Conformidade

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Objetivo da criptografia de dados | Confidencialidade | Integridade, disponibilidade |
| Objetivo do controle de acesso | Só usuários autorizados acessam | Proteger contra ameaças externas |
| Vantagem da autenticação de dois fatores | Garantir a autenticidade do usuário | Senha mais complexa, menos senhas |
| Proteger dados em trânsito | HTTPS / SSL/TLS | RDP, KMS sozinho |
| Aplicar patches no SO de uma instância EC2 | Cliente | AWS |
| Aplicar patches no engine de banco do RDS | AWS | Cliente |
| Segurança física dos data centers | AWS | Cliente, compartilhada |
| Dar permissão temporária a uma instância EC2 para ler S3 | IAM role | Access keys no código, usuário IAM |
| Conceder o mínimo necessário | Princípio do menor privilégio | Política `AdministratorAccess` |
| Login único da equipe em várias contas | IAM Identity Center | Cognito, usuários IAM por conta |
| Login de clientes em app mobile com Google | Amazon Cognito | IAM Identity Center, IAM |
| Rotacionar senha de banco automaticamente | Secrets Manager | Parameter Store, KMS |
| Limitar o que contas-membro podem fazer | SCP no AWS Organizations | Política do IAM, Control Tower sozinho |
| Configurar multi-conta com boas práticas e guardrails | AWS Control Tower | Organizations sozinho, Config |
| Serviço que o Control Tower usa para criar recursos | AWS CloudFormation | Trusted Advisor, Directory Service |
| Automatizar a coleta de evidências para auditoria da **sua** carga | AWS Audit Manager | AWS Artifact (relatórios da AWS) |
| Uma fatura e descontos por volume entre contas | Faturamento consolidado (Organizations) | Cost Explorer, Budgets |
| Criar e controlar chaves de criptografia | AWS KMS | CloudHSM, ACM |
| HSM dedicado com controle exclusivo das chaves | AWS CloudHSM | KMS |
| Certificado TLS com renovação automática | AWS Certificate Manager | KMS, Secrets Manager |
| Encontrar PII em buckets S3 | Amazon Macie | GuardDuty, Inspector |
| Detectar atividade maliciosa na conta | Amazon GuardDuty | Inspector, Detective |
| Encontrar vulnerabilidades em EC2 e imagens | Amazon Inspector | GuardDuty, Trusted Advisor |
| Investigar a causa raiz de um achado | Amazon Detective | GuardDuty, CloudTrail |
| Painel único de achados e padrões de conformidade | AWS Security Hub | Trusted Advisor, Config |
| Bloquear SQL injection e XSS | AWS WAF | Shield, security group |
| Proteção DDoS gratuita e automática | Shield Standard | Shield Advanced, WAF |
| Equipe de resposta a DDoS e proteção de custos | Shield Advanced | Shield Standard |
| Regras de firewall centralizadas em várias contas | AWS Firewall Manager | WAF isolado, SCP |
| Bloquear um IP específico na sub-rede | Network ACL | Security group |
| Saber quem apagou um recurso | AWS CloudTrail | CloudWatch, Config |
| Histórico de configuração e conformidade de recursos | AWS Config | CloudTrail, CloudWatch |
| Relatórios SOC/PCI/ISO da AWS | AWS Artifact | Security Hub, Trusted Advisor |
| Denunciar abuso vindo de recursos AWS | AWS Trust & Safety | AWS Support, re:Post |
| Produtos de segurança de terceiros | AWS Marketplace | AWS Artifact |

---

## 4. Computação

> **Regra de ouro da prova**: quanto de controle o cliente quer? **Controle total do servidor** leva a **EC2**. **Contêineres** levam a **ECS/EKS** (com **Fargate** para não gerenciar servidores). **Código que roda por evento sem servidor** leva a **Lambda**. **Subir código e deixar a AWS provisionar tudo** leva a **Elastic Beanstalk**. **Servidor virtual simples com preço fixo mensal** leva a **Lightsail**.

### Amazon EC2

#### Fundamentos do EC2
- **Amazon EC2 (Elastic Compute Cloud)**: servidores virtuais (instâncias) redimensionáveis, cobrados pelo uso. É **IaaS**: o cliente escolhe e gerencia o SO, faz patches e instala aplicações.
- **AMI (Amazon Machine Image)**: modelo com SO e software para lançar instâncias. Pode ser da AWS, do **AWS Marketplace**, da comunidade ou criada por você.
- **User data**: script executado na inicialização para instalar e configurar a instância automaticamente.
- **Key pair**: par de chaves para acesso SSH/RDP. **Session Manager** do Systems Manager permite acesso sem abrir portas nem gerenciar chaves.
- **Armazenamento**: volumes **EBS** (persistentes, na rede) ou **instance store** (temporário, no host físico). Veja a seção 5.

#### Tipos de instância

| Família | Otimizada para | Casos de uso típicos | Exemplos |
|---|---|---|---|
| **Uso geral** (general purpose) | Equilíbrio entre CPU, memória e rede | Servidores web, repositórios de código, ambientes de desenvolvimento | M, T (burstable) |
| **Otimizada para computação** (compute optimized) | CPU de alto desempenho | Processamento em lote, servidores de jogos, HPC, transcodificação de mídia, inferência de ML, servidores web de alto desempenho | C |
| **Otimizada para memória** (memory optimized) | Grandes conjuntos de dados em memória | Bancos em memória, análise em tempo real de big data, caches | R, X, z |
| **Otimizada para armazenamento** (storage optimized) | Alto I/O sequencial em armazenamento **local** | Data warehouses, bancos OLTP/NoSQL de alto I/O, sistemas de arquivos distribuídos | I, D, H |
| **Computação acelerada** (accelerated computing) | GPUs e aceleradores de hardware | Treinamento e inferência de ML, renderização gráfica, cálculos científicos | P, G, Inf, Trn |
| **Otimizada para HPC** | Computação de alto desempenho em larga escala | Simulações complexas, modelagem científica | Hpc |

#### Modelos de compra do EC2

| Modelo | Desconto aproximado vs. On-Demand | Compromisso | Quando usar |
|---|---|---|---|
| **On-Demand** | — | Nenhum; cobrança por segundo (mínimo de 60 s em Linux e Windows) ou por hora. É o **modelo de preço padrão** do EC2 | Cargas curtas, imprevisíveis, testes, aplicações novas sem histórico, que não podem ser interrompidas. Também é a resposta para uso **periódico/esporádico** (ex.: algumas horas por dia, uma semana por mês) |
| **Reserved Instances (RI)** | Até ~72% (Standard) e ~66% (Convertible) | 1 ou 3 anos, com atributos da instância | Carga estável e previsível (ex.: banco 24/7) |
| **Savings Plans** | Até ~72% (EC2 Instance) e ~66% (Compute) | Gasto em US$/hora por 1 ou 3 anos | Carga estável com flexibilidade de família, Região ou uso em Fargate e Lambda |
| **Spot Instances** | Até ~90% | Nenhum; a AWS pode **interromper com aviso de 2 minutos** | Cargas **tolerantes a interrupção**: lote, CI/CD, análise de dados, renderização |
| **Dedicated Hosts** | Opções On-Demand, reserva ou Savings Plans | Opcional | **Servidor físico inteiro** dedicado; **BYOL** de licenças por socket/núcleo; conformidade |
| **Dedicated Instances** | Custo maior que o compartilhado | Opcional | Hardware não compartilhado com outros clientes, **sem** visibilidade nem controle do host |
| **On-Demand Capacity Reservations** | Nenhum sozinho | Nenhum; paga enquanto a reserva existe | **Garantir capacidade** em uma AZ por qualquer duração |

- **Reserved Instances**:
  - **Pagamento**: All Upfront (maior desconto), Partial Upfront ou No Upfront.
  - **Standard vs. Convertible**: Standard dá mais desconto e pode ser **vendida no Reserved Instance Marketplace**; Convertible permite **trocar** de família, SO ou tenancy.
  - **Flexibilidade**: uma RI **regional** aplica o desconto em qualquer AZ da Região e, para Linux com tenancy padrão, em **qualquer tamanho da mesma família** (flexibilidade de tamanho). Uma RI **zonal** reserva capacidade em uma AZ específica.
  - **Comportamento em AWS Organizations**: com faturamento consolidado, o desconto de uma RI comprada em uma conta **pode ser aplicado automaticamente ao uso correspondente de outras contas** da organização. O compartilhamento pode ser desativado.
  - **Como contar RIs em faturamento consolidado** (questão recorrente de "quantas instâncias serão cobradas como RI?"). A regra tem três passos:
    1. As RIs cobrem **primeiro** as instâncias correspondentes da **conta que comprou**.
    2. As RIs **que sobrarem** cobrem instâncias correspondentes **de qualquer outra conta** da organização.
    3. As instâncias sem RI disponível são cobradas como **On-Demand** (regulares). RI ociosa **é paga de qualquer forma** — não há reembolso.
    - *Exemplo:* Conta X com **7 RIs** e 5 instâncias; Conta Y com 2 instâncias; Conta Z com 4 instâncias. → as 5 de X usam 5 RIs; sobram 2 RIs, que cobrem as 2 de Y; as 4 de Z ficam regulares. Resultado: **7 como RI e 4 regulares**.
    - *Outro exemplo:* Conta A com **5 RIs** e 4 instâncias; Conta B com 4 instâncias. → 4 RIs em A, 1 RI sobrando cobre 1 de B, restam 3 regulares. Resultado: **5 como RI e 3 regulares**.
- **Savings Plans**: compromisso de **gasto por hora**, não de uma instância. **Compute Savings Plans** valem para EC2 em qualquer família e Região, **Fargate e Lambda**. **EC2 Instance Savings Plans** dão mais desconto, mas ficam presos a uma família em uma Região. Existe também o **SageMaker AI Savings Plans**.
- **Combinação clássica de menor custo**: RI/Savings Plans para a **carga base** + Spot para **picos tolerantes a interrupção** + On-Demand para o restante imprevisível.

### Escalabilidade e balanceamento de carga

#### Auto Scaling
- **Amazon EC2 Auto Scaling** ajusta automaticamente o número de instâncias em um **Auto Scaling group** entre um **mínimo**, uma **capacidade desejada** e um **máximo**. Ele também **substitui instâncias com falha** (autorrecuperação).
- **Elasticidade**: o Auto Scaling é o exemplo clássico. Adiciona capacidade quando a demanda sobe (**scale out**) e remove quando cai (**scale in**), então você paga só pelo necessário.
- **Tipos de scaling**: **dinâmico** (target tracking, como "manter CPU em 50%", step ou simple), **agendado** (horário conhecido), **preditivo** (usa machine learning para prever padrões recorrentes).
- **AWS Auto Scaling** (o serviço com esse nome) cria planos de escala para vários recursos ao mesmo tempo: grupos EC2, tarefas ECS, tabelas DynamoDB e réplicas Aurora.

#### Elastic Load Balancing (ELB)
- Distribui o tráfego de entrada entre vários destinos (EC2, contêineres, IPs, Lambda) em **várias AZs**, faz **health checks** e envia tráfego só para destinos saudáveis. Pode fazer terminação TLS (**SSL offload**) com certificados do ACM.

| Tipo | Camada | Quando usar |
|---|---|---|
| **Application Load Balancer (ALB)** | 7 (HTTP/HTTPS) | Aplicações web e microsserviços; roteamento por caminho (`/api`) ou host |
| **Network Load Balancer (NLB)** | 4 (TCP/UDP/TLS) | Altíssimo desempenho, milhões de requisições por segundo, latência ultrabaixa, IP estático |
| **Gateway Load Balancer (GWLB)** | 3 | Implantar e escalar appliances virtuais de terceiros (firewalls, IDS/IPS) |
| **Classic Load Balancer** | 4 e 7 | Legado; não é resposta para novos projetos |

- **Auto Scaling + ELB**: o par clássico para **alta disponibilidade e elasticidade**. O ELB espalha a carga; o Auto Scaling ajusta a quantidade de instâncias.

### Contêineres e serverless

#### Opções de contêiner

| Serviço | O que é | Palavra-chave |
|---|---|---|
| **Amazon ECS** (Elastic Container Service) | Orquestrador de contêineres **nativo da AWS**, simples e integrado aos serviços AWS | "Rodar contêineres Docker na AWS com orquestração gerenciada" |
| **Amazon EKS** (Elastic Kubernetes Service) | **Kubernetes gerenciado**: a AWS opera o control plane | "Já usamos Kubernetes", "portabilidade entre nuvens e on-premises" |
| **AWS Fargate** | Motor de computação **serverless para contêineres**, usado com ECS ou EKS. Sem servidores para provisionar ou corrigir; paga por vCPU e memória da tarefa | "Rodar contêineres sem gerenciar instâncias EC2" |
| **Amazon ECR** (Elastic Container Registry) | **Registro** gerenciado de imagens de contêiner | "Armazenar imagens Docker" |

- **ECS e EKS podem rodar em EC2 ou em Fargate**. EC2 dá controle sobre as instâncias (e permite usar Spot e RI); Fargate elimina a gestão de servidores.

#### Serverless: AWS Lambda e AWS Fargate
- **Serverless** significa que você **não provisiona nem gerencia servidores**, a escala é automática e você paga pelo uso real (sem pagar por ocioso).
- **AWS Lambda**: executa **código em resposta a eventos** (upload no S3, mensagem no SQS, requisição do API Gateway, agendamento do EventBridge).
  - Cobrança por **número de requisições** e **duração** (em milissegundos) conforme a memória configurada.
  - Execução máxima de **15 minutos** por invocação; memória de 128 MB a 10.240 MB.
  - Ideal para tarefas curtas e orientadas a eventos. **Não** é a resposta para processos longos (use Fargate, ECS, Batch ou EC2).
- **AWS Fargate**: serverless para **contêineres**, sem o limite de 15 minutos do Lambda.

### Outras opções de computação

#### Serviços de computação que a prova diferencia

| Serviço | O que é | Quando é a resposta |
|---|---|---|
| **Amazon Lightsail** | Servidores virtuais (VPS), bancos e contêineres com **preço mensal fixo e previsível**, incluindo armazenamento, transferência de dados, DNS e IP estático | Sites simples, WordPress, pequenas empresas, "quem não tem experiência com nuvem" |
| **AWS Elastic Beanstalk** | **PaaS**: você envia o código (Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker) e ele provisiona EC2, Auto Scaling, ELB e monitoramento. **Sem custo adicional**: paga só os recursos criados | "Implantar aplicação web rapidamente sem gerenciar infraestrutura", "desenvolvedor foca no código" |
| **AWS Batch** | Executa **jobs em lote** em qualquer escala, provisionando EC2 (inclusive Spot) ou Fargate conforme a fila | "Milhares de jobs de processamento em lote" |
| **AWS Outposts** | Infraestrutura e serviços AWS **no data center do cliente** | "Latência local on-premises", "dados que precisam ficar on-premises com as APIs da AWS" |

#### Gerenciar o próprio servidor ou usar serviço gerenciado
- **EC2**: controle total, mas o cliente gerencia SO, patches, escala e disponibilidade.
- **Serviços gerenciados** (Lambda, Fargate, Elastic Beanstalk, RDS): a AWS assume parte da operação e o cliente ganha agilidade. Quando o enunciado fala em **"reduzir esforço operacional"** ou **"sem gerenciar servidores"**, descarte o EC2.

### Decisão rápida — Computação

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Servidor virtual com controle do SO | Amazon EC2 | Lambda, Lightsail |
| Processamento em lote de alto desempenho de CPU | Instância otimizada para computação | Otimizada para memória |
| Banco em memória de grande porte | Instância otimizada para memória | Otimizada para armazenamento |
| Alto I/O em disco local | Instância otimizada para armazenamento | Uso geral |
| Treinamento de ML com GPU | Computação acelerada | Otimizada para computação |
| Carga curta e imprevisível, sem interrupção | On-Demand | Spot, Reserved |
| Carga 24/7 estável por 3 anos | Reserved Instances ou Savings Plans (3 anos) | On-Demand, Spot |
| Carga tolerante a interrupção com menor custo | Spot Instances | On-Demand, Dedicated Hosts |
| Licença de software vinculada a núcleos físicos | Dedicated Hosts | Dedicated Instances |
| Desconto flexível que vale para EC2, Fargate e Lambda | Compute Savings Plans | Standard RI |
| Garantir capacidade em uma AZ para um evento | On-Demand Capacity Reservation | Savings Plans, RI regional |
| Adicionar e remover instâncias conforme a demanda | EC2 Auto Scaling | ELB, CloudWatch sozinho |
| Distribuir tráfego HTTP entre instâncias em várias AZs | Application Load Balancer | NLB, Route 53 |
| Tráfego TCP/UDP de latência ultrabaixa | Network Load Balancer | ALB |
| Kubernetes gerenciado | Amazon EKS | ECS, Fargate |
| Contêineres sem gerenciar servidores | AWS Fargate | EC2, EKS em EC2 |
| Armazenar imagens de contêiner | Amazon ECR | S3, ECS |
| Código que roda por evento sem servidor | AWS Lambda | EC2, Elastic Beanstalk |
| Processo que dura mais de 15 minutos sem servidor | Fargate / Batch | Lambda |
| Enviar código e a AWS provisiona tudo | Elastic Beanstalk | CloudFormation, EC2 |
| VPS com preço fixo mensal e simples | Amazon Lightsail | EC2, Elastic Beanstalk |

---

## 5. Armazenamento

> **Regra de ouro da prova**: identifique o **tipo de acesso**. **Objeto** via API/HTTP, backup, data lake e site estático levam a **S3**. **Bloco** para uma instância EC2 leva a **EBS** (ou **instance store** se temporário). **Arquivos compartilhados** entre várias instâncias levam a **EFS** (Linux/NFS) ou **FSx** (Windows/SMB, Lustre, NetApp, OpenZFS). **On-premises acessando a nuvem** leva a **Storage Gateway**.

### Amazon S3

#### Fundamentos do S3
- **Armazenamento de objetos**: cada objeto (arquivo + metadados) fica em um **bucket** e é acessado por uma chave via API/HTTP. Objetos de até **5 TB**; capacidade total praticamente ilimitada.
- **Durabilidade de 99,999999999% (11 noves)**: os dados são replicados em várias AZs (exceto classes One Zone).
- **Usos**: backup e restauração, arquivamento, **data lakes** e analytics, mídia, conteúdo para aplicações e **hospedagem de sites estáticos**.
- **Segurança**: buckets privados por padrão, **Block Public Access** ligado por padrão, bucket policies, criptografia padrão (SSE-S3), **presigned URLs** para acesso temporário.
- **Recursos de proteção**: **versionamento** (guarda versões anteriores e protege contra sobrescrita e exclusão acidental), **MFA Delete**, **Object Lock** (WORM, retenção imutável) e **replicação** entre Regiões (CRR) ou na mesma Região (SRR).
- **S3 Transfer Acceleration**: acelera uploads de longa distância usando edge locations.

#### Classes de armazenamento

| Classe | Padrão de acesso | Recuperação | Duração mínima cobrada | Observação |
|---|---|---|---|---|
| **S3 Standard** | Acesso frequente | Milissegundos | — | Padrão; ≥ 3 AZs |
| **S3 Intelligent-Tiering** | **Padrão desconhecido ou variável** | Milissegundos (camadas de arquivo opcionais) | — | Move objetos entre camadas automaticamente; pequena taxa de monitoramento, **sem taxa de recuperação** |
| **S3 Express One Zone** | Acesso muito frequente e sensível a latência | Um dígito de milissegundo | — | Uma única AZ; máximo desempenho |
| **S3 Standard-IA** | Pouco frequente, mas precisa de acesso rápido | Milissegundos | 30 dias | Taxa por GB recuperado |
| **S3 One Zone-IA** | Pouco frequente, **dados recriáveis** | Milissegundos | 30 dias | Uma AZ só: perde os dados se a AZ for destruída |
| **S3 Glacier Instant Retrieval** | Arquivo acessado cerca de uma vez por trimestre | **Milissegundos** | 90 dias | Arquivamento com acesso imediato |
| **S3 Glacier Flexible Retrieval** | Arquivo acessado 1 a 2 vezes por ano | Minutos a horas (expedited 1–5 min, standard 3–5 h, bulk 5–12 h) | 90 dias | Antigo "S3 Glacier" |
| **S3 Glacier Deep Archive** | Retenção de longo prazo (7 a 10 anos ou mais) | Até 12 h (standard) ou até 48 h (bulk) | 180 dias | **Menor custo** de armazenamento da AWS |

- **Na prova**: "acesso imprevisível" leva a **Intelligent-Tiering**; "arquivamento de longo prazo pelo menor custo, recuperação em horas é aceitável" leva a **Glacier Deep Archive**; "arquivamento com recuperação em milissegundos" leva a **Glacier Instant Retrieval**; "dados que podem ser recriados, acesso pouco frequente, menor custo" leva a **One Zone-IA**.

#### Políticas de ciclo de vida (lifecycle)
- Regras automáticas que **movem objetos para classes mais baratas** conforme a idade (**transition**) ou os **excluem** (**expiration**).
- Exemplo típico: Standard → Standard-IA após 30 dias → Glacier Flexible Retrieval após 90 dias → excluir após 7 anos.
- Também limpam versões antigas (versionamento) e uploads multipart incompletos.
- **Lifecycle vs. Intelligent-Tiering**: lifecycle segue regras de **tempo que você define** (padrão conhecido); Intelligent-Tiering reage ao **acesso real** (padrão desconhecido).

### Armazenamento em bloco e de arquivos

#### Amazon EBS e instance store

| Característica | Amazon EBS | Instance store |
|---|---|---|
| Tipo | Bloco, conectado **pela rede** | Bloco, **fisicamente conectado** ao host |
| Persistência | **Persistente**, independente da vida da instância | **Temporário**: perde os dados ao parar, hibernar ou encerrar (sobrevive a reboot) |
| Escopo | **Uma AZ**; normalmente ligado a uma instância por vez | O host da instância |
| Backup | **Snapshots** incrementais armazenados no S3 (copiáveis para outra AZ ou Região) | Não tem snapshot; copie os dados antes |
| Uso típico | Volume de boot, bancos de dados, aplicações | Cache, buffers, dados temporários, alto I/O |

- **Tipos de volume EBS**: SSD de uso geral (**gp3**), SSD de IOPS provisionado (**io2**, para bancos críticos), HDD otimizado para throughput (**st1**, big data e logs) e HDD frio (**sc1**, menor custo). Todos podem ser criptografados com KMS.
- Para usar um volume em outra AZ: crie um **snapshot** e restaure na AZ de destino.

#### Amazon EFS e Amazon FSx

| Serviço | Protocolo e sistema | Quando usar |
|---|---|---|
| **Amazon EFS** | NFS, **Linux** | Sistema de arquivos **compartilhado e elástico** (cresce e encolhe sozinho) para milhares de instâncias em várias AZs e on-premises. Classes Standard, Infrequent Access e Archive, com lifecycle |
| **FSx for Windows File Server** | SMB, **Windows**, integração com Active Directory | Compartilhamentos de arquivos Windows |
| **FSx for Lustre** | Lustre | **HPC**, machine learning, processamento de mídia; integra-se ao S3 |
| **FSx for NetApp ONTAP** | NFS, SMB, iSCSI | Migrar cargas NetApp; multiprotocolo |
| **FSx for OpenZFS** | NFS | Migrar cargas ZFS com baixa latência |

### Híbrido, backup e recuperação

#### AWS Storage Gateway
- Serviço de **armazenamento híbrido** que dá a aplicações on-premises acesso a armazenamento praticamente ilimitado na nuvem, com **cache local** para baixa latência. É o "sistema de arquivos com cache" citado no guia do exame.
- **Tipos**:
  - **S3 File Gateway**: compartilhamento NFS/SMB on-premises gravando objetos no **S3**.
  - **Volume Gateway**: volumes iSCSI com cópia no S3 e snapshots EBS (modos cached e stored).
  - **Tape Gateway**: **biblioteca de fitas virtual (VTL)** que substitui fitas físicas por armazenamento no S3/Glacier, sem mudar o software de backup.
  - **FSx File Gateway**: acesso local a um FSx for Windows (confira a disponibilidade para novos clientes).

#### AWS Backup e AWS Elastic Disaster Recovery
- **AWS Backup**: serviço **centralizado e gerenciado** para automatizar backups com **planos e políticas** (frequência, retenção, cópia entre Regiões e contas) de EC2, EBS, EFS, FSx, RDS, Aurora, DynamoDB, S3, Storage Gateway e outros. **Backup Vault Lock** torna os backups imutáveis. Em Organizations, aplica políticas de backup a várias contas.
- **Quando usar AWS Backup**: "centralizar e automatizar backups de vários serviços", "comprovar retenção para auditoria", "proteger backups contra exclusão".
- **AWS Elastic Disaster Recovery (DRS)**: replicação contínua de servidores (on-premises ou na nuvem) para a AWS, com **RPO de segundos e RTO de minutos**. É a resposta para "recuperar servidores rapidamente na AWS em caso de desastre".

### Decisão rápida — Armazenamento

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Armazenar objetos, backups e site estático | Amazon S3 | EBS, EFS |
| Padrão de acesso desconhecido | S3 Intelligent-Tiering | Standard-IA, lifecycle |
| Arquivamento de longo prazo pelo menor custo | S3 Glacier Deep Archive | Glacier Instant Retrieval |
| Arquivo raro que precisa de acesso em milissegundos | S3 Glacier Instant Retrieval | Deep Archive |
| Dados recriáveis, acesso pouco frequente, menor custo | S3 One Zone-IA | Standard-IA |
| Mover objetos para classes baratas conforme a idade | Lifecycle policy | Versionamento, replicação |
| Recuperar objeto sobrescrito ou apagado por engano | Versionamento do S3 | Lifecycle |
| Volume de disco persistente para uma instância | Amazon EBS | Instance store, S3 |
| Disco temporário de altíssimo I/O | Instance store | EBS |
| Arquivos compartilhados entre instâncias Linux | Amazon EFS | EBS, FSx for Windows |
| Compartilhamento Windows com Active Directory | FSx for Windows File Server | EFS |
| Sistema de arquivos para HPC | FSx for Lustre | EFS |
| On-premises usando armazenamento da nuvem com cache local | AWS Storage Gateway | DataSync, Direct Connect |
| Substituir fitas de backup físicas | Tape Gateway | Glacier direto, Snowball |
| Backup centralizado de vários serviços | AWS Backup | Snapshots manuais, Storage Gateway |
| Replicar servidores para recuperação rápida na AWS | Elastic Disaster Recovery | AWS Backup |

---

## 6. Banco de Dados

> **Regra de ouro da prova**: **relacional** (SQL, tabelas, transações) leva a **RDS/Aurora**. **NoSQL chave-valor** de escala massiva e latência de milissegundos leva a **DynamoDB**. **Cache em memória** leva a **ElastiCache**. **Data warehouse** e análise de grandes volumes leva a **Redshift**. **Grafos** leva a **Neptune**; **documentos compatíveis com MongoDB** leva a **DocumentDB**.

### Banco em EC2 ou banco gerenciado

#### Quando cada um é a resposta
- **Banco em EC2**: você instala e opera o banco em uma instância. Faz sentido quando é preciso **acesso ao SO**, um **engine ou versão que o serviço gerenciado não oferece** ou configurações muito específicas. O cliente cuida de patches, backups, alta disponibilidade e escala.
- **Banco gerenciado (RDS, Aurora, DynamoDB)**: a AWS cuida de provisionamento, **patches**, **backups automáticos**, **alta disponibilidade** e escala. É a resposta quando o enunciado fala em **reduzir esforço operacional**.
- **RDS Custom** (Oracle e SQL Server) é o meio-termo: banco gerenciado com acesso ao SO.

### Bancos relacionais

#### Amazon RDS
- Banco relacional **gerenciado** com engines **MySQL, PostgreSQL, MariaDB, Oracle, SQL Server e Db2**, além do Aurora.
- **Backups automáticos** com restauração point-in-time (retenção de até 35 dias) e **snapshots manuais**.
- **Multi-AZ**: réplica **standby síncrona** em outra AZ **da mesma Região**, com **failover automático**. Serve para **alta disponibilidade e tolerância a falhas**, não para escalar leituras — e **não protege contra a perda de uma Região inteira**, porque o standby está na mesma Região.
- **Multi-AZ DB Cluster**: variante com **duas réplicas standby legíveis** em duas outras AZs, com failover mais rápido. Também fica **na mesma Região**, então também não serve de DR regional.
- **Read Replicas**: cópias **assíncronas** para **escalar leituras** (relatórios, consultas). Podem ficar na mesma Região **ou em outra Região**.
- **Os três casos de uso que a prova separa** (mesma pergunta, três respostas):

| Requisito | Resposta |
|---|---|
| **Alta disponibilidade** com failover automático dentro da Região | **Multi-AZ** |
| **Escalar leituras** (relatórios, consultas pesadas) | **Read Replica** |
| **Recuperação de desastres** contra a perda de uma **Região inteira** | **Read Replica em outra Região** (promovida a primária no desastre) |
- **Criptografia** em repouso com KMS, habilitada na criação.

#### Amazon Aurora
- Banco relacional da AWS **compatível com MySQL e PostgreSQL**, com desempenho de até 5x o MySQL padrão e 3x o PostgreSQL padrão.
- Armazenamento distribuído que guarda **6 cópias dos dados em 3 AZs** e cresce automaticamente.
- **Aurora Serverless v2**: capacidade que escala automaticamente conforme a demanda.
- **Aurora Global Database**: replicação entre Regiões com baixa latência, para DR e leitura global.
- Custa mais que o RDS equivalente, mas entrega mais desempenho e disponibilidade.

### Bancos NoSQL, em memória e especializados

#### Amazon DynamoDB
- Banco **NoSQL chave-valor e de documentos**, **serverless** e totalmente gerenciado, com desempenho de **milissegundos de um dígito em qualquer escala**.
- Modos de capacidade **on-demand** (paga por requisição) ou **provisionado** (com Auto Scaling).
- **Global Tables** (multi-Região, multi-ativo), **DAX** (cache em memória com latência de microssegundos), **backup point-in-time**, **Streams** (captura de mudanças).
- Casos de uso: carrinho de compras, perfis de usuário, jogos, IoT, sessões e aplicações serverless.

#### Amazon ElastiCache e Amazon MemoryDB
- **Amazon ElastiCache**: **cache em memória** gerenciado com engines **Valkey, Redis OSS e Memcached**. Latência de **microssegundos**; reduz a carga do banco principal e acelera leituras repetidas. Também guarda **sessões** de usuário e rankings.
- **Amazon MemoryDB**: banco **em memória durável** compatível com Valkey e Redis OSS. Diferente do cache, ele é o banco principal.

#### Outros bancos especializados

| Serviço | Tipo | Quando usar |
|---|---|---|
| **Amazon Redshift** | **Data warehouse** colunar, escala de petabytes | Análises (OLAP) e relatórios de BI sobre grandes volumes; Redshift Spectrum consulta dados no S3 |
| **Amazon DocumentDB** | Documentos (JSON), **compatível com MongoDB** | Migrar cargas MongoDB, catálogos, perfis |
| **Amazon Neptune** | **Grafos** | Redes sociais, recomendações, **detecção de fraude**, grafos de conhecimento |
| **Amazon Keyspaces** | Colunar largo, compatível com Apache Cassandra | Migrar cargas Cassandra |
| **Amazon Timestream** | Séries temporais | Telemetria de IoT, métricas operacionais |

- *Simulados antigos citam o **Amazon QLDB** (ledger) como resposta para "registro imutável e verificável". O suporte ao QLDB terminou em julho de 2025; reconheça o nome, mas não o trate como opção atual.*

### Migração de bancos de dados

#### AWS DMS e AWS SCT
- **AWS Database Migration Service (DMS)**: migra bancos para a AWS de forma rápida e segura. O **banco de origem continua operando** durante a migração, e a **replicação contínua (CDC)** mantém os dados sincronizados até a virada.
- **Migração homogênea** (mesmo engine, ex.: MySQL → RDS MySQL): só o DMS resolve.
- **Migração heterogênea** (engines diferentes, ex.: Oracle → Aurora PostgreSQL ou SQL Server → MySQL): primeiro converta o **esquema e o código** com o **AWS SCT** (ou DMS Schema Conversion) e depois migre os dados com o **DMS**.
- O DMS também replica continuamente para data warehouses (Redshift) e data lakes (S3).

### Decisão rápida — Banco de Dados

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Banco relacional gerenciado | Amazon RDS | DynamoDB, banco em EC2 |
| Banco que exige acesso ao SO ou engine não suportado | Banco em EC2 (ou RDS Custom) | RDS padrão |
| Relacional compatível com MySQL/PostgreSQL de alto desempenho | Amazon Aurora | RDS MySQL, Redshift |
| Alta disponibilidade do RDS com failover automático | RDS Multi-AZ | Read Replica |
| Escalar leituras de um banco relacional | Read Replicas | Multi-AZ |
| DR do RDS contra a perda de uma Região inteira | Read Replica em **outra Região** | Multi-AZ, Multi-AZ DB Cluster |
| Banco de dados totalmente gerenciado e serverless | Amazon DynamoDB | MySQL, PostgreSQL, Oracle (são engines, não serviços) |
| NoSQL serverless com milissegundos em qualquer escala | Amazon DynamoDB | RDS, Redshift |
| Cache em memória para reduzir carga do banco | Amazon ElastiCache | DynamoDB, CloudFront |
| Latência de microssegundos para DynamoDB | DynamoDB Accelerator (DAX) | ElastiCache genérico |
| Data warehouse para relatórios analíticos | Amazon Redshift | RDS, DynamoDB |
| Workload compatível com MongoDB | Amazon DocumentDB | DynamoDB, Neptune |
| Relacionamentos complexos, detecção de fraude, redes sociais | Amazon Neptune | RDS, DynamoDB |
| Migrar banco com mínima parada | AWS DMS | Snowball, backup e restore |
| Converter esquema entre engines diferentes | AWS SCT / DMS Schema Conversion | DMS sozinho |

---

## 7. Redes e Entrega de Conteúdo

> **Regra de ouro da prova**: **VPC** é a sua rede isolada; **sub-rede pública** tem rota para o **Internet Gateway**; **sub-rede privada** sai para a internet pelo **NAT Gateway**. Para chegar à AWS a partir do data center: **VPN** é rápida e passa pela internet criptografada; **Direct Connect** é **privada, dedicada e consistente**, mas leva semanas. Para usuários globais: **CloudFront** faz cache de conteúdo; **Global Accelerator** acelera tráfego sem cache; **Route 53** resolve nomes.

### Amazon VPC

#### Componentes da VPC

| Componente | O que é |
|---|---|
| **VPC** | Rede virtual **logicamente isolada** em uma Região, com faixa de IPs (CIDR) definida pelo cliente |
| **Sub-rede (subnet)** | Faixa de IPs dentro da VPC, sempre em **uma AZ**. **Pública** se a tabela de rotas aponta para um Internet Gateway; **privada** se não aponta |
| **Tabela de rotas (route table)** | Define para onde o tráfego de cada sub-rede é encaminhado |
| **Internet Gateway (IGW)** | Permite comunicação entre a VPC e a **internet** (entrada e saída) |
| **NAT Gateway** | Permite que instâncias em sub-redes **privadas** **iniciem** conexões para a internet (ex.: baixar atualizações) sem receber conexões de entrada. Gerenciado e cobrado por hora e por GB |
| **Virtual private gateway / Customer gateway** | Pontas AWS e on-premises de uma conexão Site-to-Site VPN |
| **Security group e network ACL** | Firewall da instância (stateful) e da sub-rede (stateless). Veja a seção 3 |
| **VPC endpoints** | Acesso **privado** a serviços AWS sem passar pela internet. **Gateway endpoint** (S3 e DynamoDB, sem custo) e **interface endpoint** (**AWS PrivateLink**, para a maioria dos serviços e serviços de terceiros) |
| **VPC Peering** | Conexão privada **um a um** entre duas VPCs. **Não é transitiva** |
| **AWS Transit Gateway** | **Hub central** que conecta **muitas VPCs e redes on-premises**, simplificando topologias com dezenas ou centenas de conexões |
| **VPC Flow Logs** | Registram metadados do tráfego IP para auditoria e troubleshooting |

- **Segurança na VPC** segundo o guia do exame: **network ACLs**, **security groups** e **Amazon Inspector** (que também avalia a **alcançabilidade de rede** das instâncias).

#### Quais serviços ficam dentro de uma VPC

A prova pergunta direto: *"qual destes serviços exige uma VPC?"*. A divisão é por onde o recurso **vive**:

| Ficam **dentro** da VPC (têm IP na sua rede) | Ficam **fora** da VPC (acesso por endpoint) |
|---|---|
| **EC2**, **RDS** e Aurora, **EFS** (mount targets), **ElastiCache**, **Redshift**, ELB, NAT Gateway, Fargate/ECS/EKS (modo VPC) | **S3**, **DynamoDB**, **Cognito**, **SQS**, **SNS**, Lambda (por padrão), IAM, Route 53, CloudFront |

- Serviços "de fora" são acessados pela **internet** ou, de forma privada, por um **VPC endpoint** (gateway endpoint para S3 e DynamoDB; interface endpoint / PrivateLink para os demais).
- **Lambda** é o caso especial: roda fora da sua VPC por padrão, mas **pode ser anexada** a uma VPC quando precisa alcançar recursos privados (RDS, ElastiCache).

### Conectividade com a AWS

#### VPN e Direct Connect

| Opção | Como funciona | Quando usar |
|---|---|---|
| **AWS Site-to-Site VPN** | Túnel **IPsec criptografado** pela **internet pública** entre o data center e a VPC | Conexão rápida de configurar e barata; backup do Direct Connect |
| **AWS Client VPN** | VPN gerenciada para **usuários individuais** (notebooks, trabalho remoto) acessarem a AWS e a rede on-premises | "Funcionários remotos acessando recursos privados" |
| **AWS Direct Connect** | **Conexão de rede física, privada e dedicada** entre o data center (ou colocation) e a AWS, **sem passar pela internet** | Banda alta e **consistente**, latência previsível, grandes volumes de dados, custo menor de transferência em volume. Leva semanas para provisionar e **não é criptografada por padrão** (combine com VPN ou MACsec) |

- **Palavra-chave**: "conexão privada dedicada", "desempenho consistente", "não passar pela internet" leva a **Direct Connect**. "Criptografada, rápida de configurar, pela internet" leva a **Site-to-Site VPN**.

### DNS, CDN e APIs

#### Amazon Route 53
- Serviço de **DNS** gerenciado, altamente disponível e escalável. Também **registra domínios** e faz **health checks**.
- **Políticas de roteamento**:
  - **Simple**: um recurso.
  - **Weighted** (ponderado): divide o tráfego por pesos (ex.: 90/10 em testes A/B).
  - **Latency-based**: envia para a Região de **menor latência** para o usuário.
  - **Failover**: ativo/passivo, com health check (DR).
  - **Geolocation**: roteia pela **localização do usuário** (país/continente), útil para conteúdo localizado ou restrição.
  - **Geoproximity**: roteia pela distância geográfica, com ajuste de viés.
  - **Multivalue answer**: devolve vários registros saudáveis.
  - **IP-based**: roteia pela faixa de IP de origem.

#### Amazon CloudFront, Global Accelerator e API Gateway

| Serviço | O que faz | Quando é a resposta |
|---|---|---|
| **Amazon CloudFront** | **CDN**: faz **cache** de conteúdo estático e dinâmico nas **edge locations**, com HTTPS, integração com WAF e Shield, e origens como S3, ALB e EC2 | "Entregar conteúdo (vídeos, imagens, site) com baixa latência para usuários no mundo todo" |
| **AWS Global Accelerator** | Usa a **rede global da AWS** para melhorar desempenho e disponibilidade de aplicações TCP/UDP, com **dois IPs anycast estáticos** e failover rápido entre Regiões. **Não faz cache** | Jogos, IoT, VoIP e aplicações não HTTP; "IP estático global"; failover regional rápido |
| **Amazon API Gateway** | Cria, publica, protege e monitora **APIs** (REST, HTTP e WebSocket) em qualquer escala, com autenticação, throttling e cache. Porta de entrada comum para o Lambda | "Expor funções Lambda como API", "API serverless" |

### Decisão rápida — Redes

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Rede isolada logicamente na AWS | Amazon VPC | Sub-rede, security group |
| Serviço que exige uma VPC | EFS, EC2, RDS, ElastiCache, Redshift | S3, DynamoDB, Cognito |
| Dar acesso à internet para sub-rede pública | Internet Gateway | NAT Gateway |
| Instâncias privadas baixarem atualizações da internet | NAT Gateway | Internet Gateway direto |
| Acessar S3 da VPC sem passar pela internet | Gateway VPC endpoint | NAT Gateway, Direct Connect |
| Expor um serviço de forma privada para outras VPCs | AWS PrivateLink | VPC Peering, Internet Gateway |
| Conectar duas VPCs de forma privada | VPC Peering | Transit Gateway (para muitas) |
| Conectar muitas VPCs e redes on-premises em um hub | AWS Transit Gateway | VPC Peering em malha |
| Conexão criptografada rápida pela internet | Site-to-Site VPN | Direct Connect |
| Conexão privada dedicada e consistente | AWS Direct Connect | Site-to-Site VPN |
| Funcionários remotos acessando a VPC | AWS Client VPN | Site-to-Site VPN |
| DNS, registro de domínio e health checks | Amazon Route 53 | CloudFront |
| Enviar usuários à Região de menor latência | Route 53 latency-based routing | Geolocation |
| Conteúdo por país do usuário | Route 53 geolocation routing | Latency-based |
| Cache de conteúdo global com baixa latência | Amazon CloudFront | Global Accelerator, S3 Transfer Acceleration |
| IPs estáticos globais e aceleração TCP/UDP sem cache | AWS Global Accelerator | CloudFront |
| Publicar API para funções Lambda | Amazon API Gateway | ALB, CloudFront |

---

## 8. Analytics, IA e Machine Learning

> **Regra de ouro da prova**: em analytics, pense no pipeline **coletar → armazenar → catalogar/transformar → consultar → visualizar**. Em IA/ML, pense em **"qual tarefa"**: falar (**Polly**), ouvir (**Transcribe**), traduzir (**Translate**), entender texto (**Comprehend**), ver imagens (**Rekognition**), ler documentos (**Textract**), conversar (**Lex**), construir modelos próprios (**SageMaker AI**), IA generativa (**Amazon Q**, **Amazon Bedrock**).

### Serviços de analytics

#### O que cada serviço de analytics faz

| Serviço | O que faz | Palavra-chave |
|---|---|---|
| **Amazon Athena** | Consultas **SQL interativas e serverless** diretamente sobre dados no **S3**. Paga por dados escaneados | "Consultar dados no S3 com SQL sem servidor", "análise ad hoc de logs" |
| **AWS Glue** | **ETL serverless** (extrair, transformar e carregar) e **Glue Data Catalog** (catálogo de metadados), com **crawlers** que descobrem esquemas | "Preparar e transformar dados", "catalogar dados do data lake" |
| **Amazon Kinesis** | **Dados em streaming em tempo real**: **Kinesis Data Streams** (coleta e processa fluxos), **Amazon Data Firehose** (entrega fluxos ao S3, Redshift e OpenSearch sem código; antigo Kinesis Data Firehose) e **Kinesis Video Streams** | "Clickstream, telemetria e logs em tempo real" |
| **Amazon EMR** | Clusters gerenciados de **big data** com Apache **Spark, Hadoop**, Hive e Presto | "Processamento distribuído de big data com Hadoop/Spark" |
| **Amazon Redshift** | **Data warehouse** para análises em escala de petabytes | "Relatórios analíticos sobre dados históricos estruturados" |
| **Amazon OpenSearch Service** | Busca, **análise de logs** e observabilidade (sucessor do Amazon Elasticsearch Service), com dashboards | "Pesquisa de texto completo", "análise de logs quase em tempo real" |
| **Amazon Quick Sight** | Serviço de **BI** serverless para **dashboards e visualizações** interativas, com insights de ML. Grafado "QuickSight" em materiais antigos | "Criar dashboards e relatórios visuais", "visualizar o Cost and Usage Report" |
| **Amazon QuickSight Q** | Recurso do Quick Sight que aceita **perguntas em linguagem natural (NLP)** e responde com **gráficos e visualizações** | "Fazer perguntas sobre os dados e receber respostas com visualizações", "NLP em painéis de BI" |
| **AWS Data Exchange** | **Assinar, comprar e usar conjuntos de dados de terceiros** já integrados à AWS, para enriquecer as próprias análises | "Comprar dados de provedores", "assinar conjuntos de dados confiáveis de terceiros" |
| **AWS Lake Formation** | Criar e **governar data lakes** no S3 com permissões centralizadas | "Controlar acesso ao data lake" |
| **Amazon MSK** | Apache Kafka gerenciado | "Já usamos Kafka" |

- **Pipeline serverless clássico**: dados no **S3** → **Glue** cataloga e transforma → **Athena** consulta → **Quick Sight** visualiza.
- **Quick Sight vs. QuickSight Q**: se o enunciado só pede **dashboards e gráficos**, a resposta é **Quick Sight**. Se pede **fazer perguntas em linguagem natural** e receber visualizações, a resposta é **QuickSight Q** — e ele costuma aparecer junto de Kendra, Comprehend, Lex e Bedrock como distratores.
- **Data Exchange vs. Marketplace**: **Data Exchange** vende **dados**; **Marketplace** vende **software e serviços**. Redshift, Athena e DynamoDB *armazenam ou consultam* dados, mas não os **fornecem**.
- **Athena vs. S3 Select**: **Athena** consulta **vários objetos** de um bucket com SQL padrão e gera relatórios; **S3 Select** apenas **filtra dentro de um único objeto**, com SQL limitado. "Ler todos esses arquivos e gerar um relatório resumido" leva a **Athena**.

### Serviços de IA e machine learning

#### Serviços de IA prontos (sem treinar modelo)

| Serviço | Tarefa | Exemplo de enunciado |
|---|---|---|
| **Amazon Rekognition** | **Análise de imagens e vídeos**: objetos, pessoas, texto, **rostos**, conteúdo impróprio | "Identificar rostos em fotos", "moderar imagens enviadas" |
| **Amazon Textract** | **Extrair texto, formulários e tabelas** de documentos digitalizados (vai além de OCR simples) | "Extrair dados de notas fiscais e formulários escaneados" |
| **Amazon Comprehend** | **Processamento de linguagem natural (NLP)**: sentimento, entidades, frases-chave, idioma, PII em texto | "Analisar o sentimento de avaliações de clientes" |
| **Amazon Transcribe** | **Fala para texto** (speech-to-text) | "Legendar vídeos", "transcrever chamadas" |
| **Amazon Polly** | **Texto para fala** (text-to-speech) com vozes realistas | "Converter artigos em áudio" |
| **Amazon Translate** | **Tradução** automática de idiomas | "Traduzir conteúdo do site" |
| **Amazon Lex** | **Chatbots e interfaces conversacionais** de voz e texto (mesma tecnologia da Alexa) | "Criar um chatbot de atendimento" |
| **Amazon Q** | **Assistente de IA generativa**: **Amazon Q Business** responde perguntas e resume com base nos dados da empresa; **Amazon Q Developer** ajuda a escrever, explicar e transformar código e a operar recursos AWS | "Assistente de IA generativa para funcionários", "assistente de código" |

- **Fora da lista oficial, mas frequentes em simulados**: **Amazon Bedrock** (acesso via API a **modelos de fundação** de vários provedores para criar aplicações de IA generativa), **Amazon Kendra** (busca corporativa inteligente), **Amazon Personalize** (recomendações personalizadas).

#### Amazon SageMaker AI
- Plataforma totalmente gerenciada para **construir, treinar e implantar modelos de machine learning próprios** em escala (antigo Amazon SageMaker).
- Inclui notebooks e ambiente de desenvolvimento, rotulagem de dados (**Ground Truth**), treinamento gerenciado, implantação de endpoints e ML sem código (**SageMaker Canvas**).
- **Palavra-chave**: "cientistas de dados precisam criar, treinar e implantar modelos personalizados" leva a **SageMaker AI**. Se a tarefa já é resolvida por um serviço pronto (tradução, transcrição, imagem), a resposta é o serviço pronto.

### Decisão rápida — Analytics e IA

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| SQL sobre dados no S3 sem servidor | Amazon Athena | Redshift, RDS |
| ETL serverless e catálogo de dados | AWS Glue | EMR, Athena |
| Ingestão de dados em streaming em tempo real | Amazon Kinesis | SQS, Glue |
| Big data com Hadoop/Spark | Amazon EMR | Glue, Athena |
| Data warehouse para BI | Amazon Redshift | DynamoDB, Athena |
| Dashboards e visualizações de BI | Amazon Quick Sight | CloudWatch dashboards, Athena |
| Perguntas em linguagem natural sobre os dados, com gráficos | Amazon QuickSight Q | Kendra, Comprehend, Lex, Bedrock |
| Comprar/assinar conjuntos de dados de terceiros | AWS Data Exchange | Redshift, DynamoDB, Marketplace |
| Filtrar dados dentro de um único objeto do S3 | Amazon S3 Select | Athena (vários objetos) |
| Busca de texto e análise de logs | Amazon OpenSearch Service | Athena, Kendra |
| Reconhecer rostos e objetos em imagens | Amazon Rekognition | Textract, SageMaker AI |
| Extrair tabelas e formulários de documentos | Amazon Textract | Rekognition, Comprehend |
| Sentimento e entidades em texto | Amazon Comprehend | Translate, Lex |
| Áudio para texto | Amazon Transcribe | Polly |
| Texto para áudio | Amazon Polly | Transcribe |
| Traduzir textos | Amazon Translate | Comprehend |
| Chatbot conversacional | Amazon Lex | Polly, Connect sozinho |
| Assistente de IA generativa com dados da empresa | Amazon Q Business | Lex, SageMaker AI |
| Assistente de código com IA | Amazon Q Developer | CodeBuild, X-Ray |
| Modelos de fundação via API | Amazon Bedrock | SageMaker AI (modelo próprio) |
| Construir, treinar e implantar modelo próprio | Amazon SageMaker AI | Rekognition, Comprehend |

---

## 9. Integração, Aplicações e Demais Categorias

> **Regra de ouro da prova**: para **desacoplar** componentes com uma **fila**, use **SQS**. Para **notificar** muitos assinantes ao mesmo tempo (push), use **SNS**. Para **rotear eventos** entre serviços AWS, aplicações e SaaS, use **EventBridge**. Para **orquestrar** passos de um fluxo, use **Step Functions**. **E-mail em massa ou transacional** é **SES**, não SNS.

### Integração de aplicações

#### SQS, SNS, EventBridge e Step Functions

| Serviço | Modelo | Quando é a resposta |
|---|---|---|
| **Amazon SQS** | **Fila** de mensagens: o produtor envia, o consumidor **puxa** (pull) quando puder. Filas **Standard** (throughput quase ilimitado, entrega ao menos uma vez) e **FIFO** (ordem garantida, processamento exatamente uma vez). Retém mensagens por até 14 dias | "**Desacoplar** componentes", "absorver picos sem perder pedidos", "processamento assíncrono" |
| **Amazon SNS** | **Publish/subscribe**: um tópico **empurra** (push) a mensagem para vários assinantes (e-mail, SMS, push mobile, HTTP, Lambda, SQS) | "**Enviar alertas e notificações**", "fan-out para vários sistemas" |
| **Amazon EventBridge** | **Barramento de eventos** serverless: regras filtram eventos de serviços AWS, aplicações próprias e **SaaS** e os enviam a destinos. Inclui **EventBridge Scheduler** | "Reagir a eventos de serviços AWS ou SaaS", "arquitetura orientada a eventos", "agendar tarefas" |
| **AWS Step Functions** | **Orquestração visual de fluxos** (máquinas de estado) com vários passos, desvios, novas tentativas e espera | "Coordenar várias funções Lambda em sequência", "workflow com etapas e tratamento de erro" |

- **Alertas de monitoramento**: um **alarme do CloudWatch** normalmente notifica por um **tópico SNS**.
- **Amazon MQ** (ActiveMQ/RabbitMQ gerenciado) aparece em simulados para "migrar aplicações que já usam um broker de mensagens padrão sem reescrever".

### Aplicações de negócio e computação para usuário final

#### Aplicações de negócio
- **Amazon Connect**: **central de atendimento (contact center)** omnichannel na nuvem, com voz, chat e tarefas, pago pelo uso. Integra-se a Lex (bots) e Transcribe/Contact Lens (análise).
- **Amazon SES (Simple Email Service)**: envio de **e-mails** transacionais, de marketing e em massa, com alta entregabilidade. Também recebe e-mails.
- **Diferença clássica**: SNS envia notificações (inclusive por e-mail) a assinantes de um tópico; **SES** é o serviço de **e-mail** para aplicações e campanhas.

#### Computação para o usuário final

| Serviço | O que entrega | Quando usar |
|---|---|---|
| **Amazon WorkSpaces** | **Desktops virtuais persistentes** (DaaS) Windows ou Linux | "Funcionários precisam de um desktop completo acessível de qualquer dispositivo" |
| **Amazon AppStream 2.0** | **Streaming de aplicações** individuais para o navegador, sem instalar localmente | "Entregar uma aplicação desktop específica pelo navegador" |
| **Amazon WorkSpaces Secure Browser** | **Navegador seguro** gerenciado para acessar sites internos e SaaS sem deixar dados no dispositivo (antigo WorkSpaces Web) | "Acesso seguro a aplicações web internas a partir de dispositivos não gerenciados" |

- O guia do exame pergunta quais serviços **apresentam a saída de VMs na máquina do usuário final**: **WorkSpaces** (desktop inteiro) e **AppStream 2.0** (aplicação).

### Frontend, IoT e ferramentas de desenvolvimento

#### Frontend web e mobile
- **AWS Amplify**: ferramentas e serviços para **criar, implantar e hospedar aplicações full-stack web e mobile** rapidamente, com autenticação, dados, armazenamento e **Amplify Hosting** (CI/CD a partir do Git).
- Serviços relacionados que aparecem em simulados: **AWS AppSync** (APIs GraphQL gerenciadas) e **AWS Device Farm** (testar apps em dispositivos reais na nuvem).

#### Internet das Coisas (IoT)
- **AWS IoT Core**: conecta **bilhões de dispositivos** à nuvem com segurança (protocolos MQTT, HTTPS), recebe e roteia mensagens para outros serviços AWS. É a resposta para "gerenciar e conectar dispositivos IoT".
- **AWS IoT Greengrass**: runtime para executar processamento, Lambda e ML **nos próprios dispositivos** na borda.

#### Ferramentas de desenvolvimento

| Ferramenta | O que faz |
|---|---|
| **AWS CLI** | Linha de comando para gerenciar serviços AWS e automatizar com scripts |
| **AWS SDKs** | Bibliotecas para usar serviços AWS a partir de linguagens de programação |
| **AWS CloudShell** | Terminal no navegador, já autenticado, com CLI pré-instalada |
| **AWS Cloud9** | **IDE (ambiente de desenvolvimento integrado) na nuvem**: escrever, executar e depurar código pelo navegador, com colaboração em tempo real entre a equipe |
| **AWS CodeCommit** | **Repositório Git** gerenciado — a etapa de **origem** do pipeline |
| **AWS CodeBuild** | **Compila o código, executa testes** e gera artefatos, sem servidores de build |
| **AWS CodePipeline** | **Orquestra o pipeline de CI/CD** (código → build → teste → deploy) |
| **AWS CodeDeploy** | Automatiza **implantações** em EC2, servidores on-premises, Lambda e ECS |
| **AWS CodeArtifact** | Repositório gerenciado de pacotes de software (npm, Maven, PyPI) |
| **AWS X-Ray** | **Rastreamento distribuído**: mostra o caminho de uma requisição entre microsserviços e ajuda a **encontrar gargalos e erros** |
| **AWS Application Composer** | **Projetar e construir visualmente** aplicações serverless, arrastando componentes numa tela e gerando o template de IaC. Renomeado **AWS Infrastructure Composer** |
| **AWS CodeStar** *(legado)* | Criava **rapidamente um projeto com pipeline CI/CD pronto**, integrando CodeCommit, CodeBuild, CodePipeline e CodeDeploy. **Descontinuado em jul/2024**, mas ainda aparece em simulados como resposta para "implementar um pipeline CI/CD rapidamente" |

- **Palavra-chave**: "desenvolver, implantar e **solucionar problemas** de aplicações" junta **CodeBuild + CodePipeline + X-Ray**.
- **Pares que confundem nas ferramentas de desenvolvimento**:
  - **Cloud9** = IDE para *escrever* código. **CodeBuild** = *compilar e testar*. **CloudShell** = terminal com a CLI, não um IDE.
  - **Application Composer** = *desenhar* a aplicação serverless visualmente. **App Runner** = *rodar* um contêiner ou app web gerenciado a partir do repositório. **Lambda** = executar a função.
  - **CodeStar** = projeto e pipeline prontos de uma vez. **CodePipeline** = só a orquestração do pipeline.
  - **CloudFormation/CDK** = infraestrutura como código de qualquer recurso. **Application Composer** = interface visual que gera esse código para serverless.

### Decisão rápida — Integração e demais categorias

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Desacoplar componentes com fila | Amazon SQS | SNS, EventBridge |
| Mensagens processadas na ordem exata | SQS FIFO | SQS Standard, SNS |
| Enviar alerta para vários assinantes (e-mail, SMS) | Amazon SNS | SQS, SES |
| Rotear eventos de serviços AWS e SaaS por regras | Amazon EventBridge | SNS, SQS |
| Orquestrar fluxo com vários passos | AWS Step Functions | SQS, EventBridge |
| Central de atendimento na nuvem | Amazon Connect | Amazon Lex, SES |
| E-mails de marketing ou transacionais | Amazon SES | Amazon SNS |
| Desktop virtual completo para funcionários | Amazon WorkSpaces | AppStream 2.0 |
| Transmitir uma aplicação para o navegador | Amazon AppStream 2.0 | WorkSpaces |
| Navegador seguro para apps internos | WorkSpaces Secure Browser | Client VPN |
| Criar e hospedar app web/mobile full-stack | AWS Amplify | Elastic Beanstalk, Lightsail |
| Conectar e gerenciar dispositivos IoT | AWS IoT Core | IoT Greengrass, Kinesis |
| Compilar e testar código | AWS CodeBuild | CodePipeline, CodeDeploy |
| Automatizar o pipeline de CI/CD | AWS CodePipeline | CodeBuild |
| IDE na nuvem para a equipe escrever e depurar código | AWS Cloud9 | CodeBuild, CloudShell, OpsWorks |
| Implementar um pipeline CI/CD completo rapidamente | AWS CodeStar (legado) | Config, Cognito, DataSync |
| Projetar visualmente uma aplicação serverless | AWS Application Composer | Lambda, Batch, App Runner |
| Repositório Git gerenciado | AWS CodeCommit | CodeArtifact, CodeBuild |
| Rastrear requisições entre microsserviços | AWS X-Ray | CloudTrail, CloudWatch Logs |

---

## 10. Gerenciamento, Operação e Governança

> **Regra de ouro da prova**: **CloudWatch** observa (métricas, logs, alarmes). **CloudTrail** audita (quem chamou qual API). **Config** registra configurações e conformidade. **Trusted Advisor** recomenda (custo, desempenho, segurança, tolerância a falhas, limites, excelência operacional). **CloudFormation** cria infraestrutura a partir de código. **Systems Manager** opera frotas de servidores.

### Formas de acessar e provisionar

#### Console, acesso programático e infraestrutura como código

| Forma | O que é | Quando é a melhor escolha |
|---|---|---|
| **AWS Management Console** | Interface **web gráfica** | Tarefas pontuais, exploração, aprendizado, visualização |
| **AWS CLI** | Linha de comando | Automação com scripts, tarefas repetitivas |
| **SDKs e APIs** | Acesso **programático** a partir de código | Aplicações que usam serviços AWS |
| **Infraestrutura como código (IaC)** | Descrever a infraestrutura em arquivos versionados: **AWS CloudFormation** (templates JSON/YAML) e **AWS CDK** (linguagens de programação que geram CloudFormation) | Ambientes **repetíveis e consistentes**, várias contas e Regiões, auditoria de mudanças |

- **Operação única vs. processo repetível** (cobrado no guia do exame): para uma tarefa **pontual**, o console basta; para algo que se **repete** ou precisa ser **igual em vários ambientes**, use **IaC ou scripts**. Automação reduz erro humano e acelera o provisionamento.
- **AWS CloudFormation**: cria, atualiza e exclui conjuntos de recursos (**stacks**) de forma previsível. **Sem custo adicional**: paga só pelos recursos criados.

#### Serviços de operação e governança

| Serviço | O que faz | Palavra-chave |
|---|---|---|
| **AWS Systems Manager** | Central de operações para EC2 e servidores on-premises: **Session Manager** (acesso sem SSH/bastion), **Patch Manager** (patches), **Run Command** (comandos em lote), **Parameter Store**, inventário e automação | "Aplicar patches em uma frota", "acesso seguro sem abrir portas", "comandos em várias instâncias" |
| **AWS Service Catalog** | **Catálogo de produtos aprovados** (templates) que usuários provisionam em modo **self-service**, respeitando padrões | "Usuários só podem lançar configurações aprovadas" |
| **AWS License Manager** | Gerencia e controla o uso de **licenças de software** (Microsoft, Oracle, SAP), evitando excesso | "Controlar licenças BYOL" |
| **AWS Compute Optimizer** | Recomendações de **rightsizing** com machine learning para EC2, Auto Scaling, EBS, Lambda, ECS no Fargate e RDS | "Identificar instâncias superdimensionadas" |
| **Service Quotas** | Visualizar e **solicitar aumento de cotas** (limites) dos serviços | "Aumentar o limite de instâncias" |
| **AWS Well-Architected Tool** | Revisar cargas contra os seis pilares | Seção 1 |
| **AWS Organizations e Control Tower** | Governança multi-conta | Seção 3 |

### Monitoramento e recomendações

#### Amazon CloudWatch
- **Métricas** de recursos e aplicações (CPU, latência, erros, métricas personalizadas), **alarmes** que disparam ações (notificar via SNS, acionar Auto Scaling, parar instância), **CloudWatch Logs** (centralizar e pesquisar logs) e **dashboards**.
- Exemplo clássico: "notificar quando a CPU passar de 80%" leva a **alarme do CloudWatch + SNS**. "Alertar quando a fatura passar de US$ 1.000" pode ser **AWS Budgets** ou um **alarme de faturamento** do CloudWatch.
- **Monitoramento para governança e conformidade**: o guia do exame associa **monitoramento** ao CloudWatch e **auditoria** ao CloudTrail e ao Config.

#### AWS Trusted Advisor
- Inspeciona a conta e dá **recomendações de boas práticas** em seis categorias:
  1. **Otimização de custos** (instâncias ociosas, volumes EBS não anexados, IPs elásticos sem uso).
  2. **Desempenho**.
  3. **Segurança** (MFA no root, security groups abertos, permissões de buckets S3).
  4. **Tolerância a falhas** (backups, Multi-AZ).
  5. **Limites de serviço** (cotas próximas do máximo).
  6. **Excelência operacional**.
- **Basic Support** dá acesso às **verificações principais** (core checks: segurança essencial e limites de serviço). **Business Support+ ou superior** libera **todas as verificações** e o acesso por API.

#### AWS Health Dashboard e AWS Health API
- **AWS Health Dashboard**: mostra a **saúde dos serviços AWS** em todas as Regiões e, na visão da conta, **eventos que afetam os seus recursos** (manutenções programadas, problemas, avisos de fim de suporte de versões), com orientações de correção.
- **AWS Health API**: acesso programático aos mesmos eventos para integrar com ferramentas de operação, disponível a partir do **Business Support+**.
- **Diferença**: Health Dashboard informa **problemas do lado da AWS** que afetam você; CloudWatch monitora **os seus recursos e aplicações**.

### Decisão rápida — Gerenciamento e Governança

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Tarefa pontual e exploratória | AWS Management Console | CloudFormation |
| Ambientes repetíveis e versionados | CloudFormation / CDK (IaC) | Console, CLI manual |
| Criar infraestrutura usando uma linguagem de programação | AWS CDK | SDK, Elastic Beanstalk |
| Terminal no navegador já autenticado | AWS CloudShell | CLI local, Session Manager |
| Aplicar patches em várias instâncias | Systems Manager Patch Manager | Inspector, Config |
| Acessar instância sem abrir a porta SSH | Systems Manager Session Manager | Bastion host |
| Catálogo self-service de recursos aprovados | AWS Service Catalog | Marketplace, CloudFormation sozinho |
| Controlar uso de licenças | AWS License Manager | Artifact, Trusted Advisor |
| Recomendações de rightsizing com ML | AWS Compute Optimizer | Cost Explorer, Budgets |
| Solicitar aumento de limite | Service Quotas | Trusted Advisor, Support Center |
| Métricas, alarmes e logs | Amazon CloudWatch | CloudTrail, Config |
| Recomendações de custo, segurança e limites | AWS Trusted Advisor | Inspector, Config |
| Eventos da AWS que afetam os seus recursos | AWS Health Dashboard | CloudWatch, CloudTrail |

---

## 11. Faturamento, Preços e Suporte

> **Regra de ouro da prova**: **Pricing Calculator** estima **antes** de usar. **Cost Explorer** analisa o que **já foi gasto** (e prevê a tendência). **Budgets** **alerta** quando o gasto real ou previsto passa de um limite. **Cost and Usage Report** é o dado **mais detalhado**. **Tags de alocação de custos** atribuem gasto a projetos. **Organizations** consolida a fatura.

### Modelos de preço

#### Princípios de preço da AWS
- **Pague conforme o uso** (pay-as-you-go): sem contratos de longo prazo nem licenças complexas.
- **Economize ao se comprometer** (save when you commit): Reserved Instances e Savings Plans dão descontos em troca de 1 ou 3 anos.
- **Pague menos por unidade ao usar mais**: preço por faixa de volume (ex.: S3 e transferência de dados) e descontos agregados pelo faturamento consolidado.
- Os fatores que mais pesam no custo são **computação, armazenamento e transferência de dados de saída**.
- **Como a AWS calcula o preço**, de forma geral: **com base no uso dos serviços e nos recursos consumidos** — não pelo número de contas, de usuários ou de instâncias criadas.

#### Unidade de cobrança de cada serviço

A prova pergunta direto "como a AWS cobra pelo *X*?". Decore a unidade:

| Serviço | Unidade de cobrança |
|---|---|
| **Amazon EC2** | Por **hora ou segundo** em que a instância está **em execução** (mínimo de 60 s). Instância parada não é cobrada, mas o **volume EBS anexado é** |
| **Amazon RDS** | Por **hora de instância de banco em execução**, mais armazenamento, backup além do provisionado e I/O |
| **Amazon S3** | Por **GB armazenado por mês**, mais requisições, recuperação (classes IA/Glacier) e transferência de saída |
| **Amazon EBS** | Por **GB provisionado por mês** (usado ou não), mais IOPS/throughput provisionados em alguns tipos |
| **Amazon EFS** | Por **GB efetivamente usado**, por classe de armazenamento |
| **AWS Lambda** | Por **número de requisições** e **duração em milissegundos** conforme a memória configurada |
| **Amazon DynamoDB** | Por requisição (on-demand) ou por capacidade provisionada, mais armazenamento |
| **NAT Gateway** | Por **hora** de existência mais **GB processado** |
| **Elastic IP** | Gratuito enquanto **associado** a uma instância em execução; cobrado quando **ocioso** |

- **Serviços sempre gratuitos** (aparecem como "qual serviço é sempre fornecido sem custo?"): **IAM**, **AWS Organizations** e faturamento consolidado, **CloudFormation** (paga só os recursos criados), **Auto Scaling**, **Elastic Beanstalk** (idem), **VPC** (a rede em si), **AWS Artifact**, **Well-Architected Tool**, **Shield Standard**. Cuidado: **S3, ELB e WAF são cobrados**.

#### Custos de transferência de dados

| Tráfego | Custo |
|---|---|
| **Entrada** da internet para a AWS | **Gratuito** |
| **Saída** da AWS para a internet | **Cobrado** por GB, com preço por faixa (os primeiros 100 GB por mês são gratuitos, somados entre os serviços) |
| Entre **AZs** na mesma Região | Cobrado por GB (nos dois sentidos, para a maioria dos serviços) |
| Na **mesma AZ** usando IP privado | Gratuito |
| Entre **Regiões** | Cobrado por GB na Região de origem |
| Da origem AWS para o **CloudFront** | Gratuito (o CloudFront cobra a entrega aos usuários) |

- **Direct Connect** reduz o custo de saída em grandes volumes; **VPC endpoints do tipo gateway** evitam cobrança de NAT Gateway para S3 e DynamoDB.

#### Opções e camadas de armazenamento
- **S3**: cobra por **GB armazenado por mês** (varia pela classe), **requisições**, **recuperação** (classes IA e Glacier) e **transferência de saída**. Classes mais baratas para armazenar costumam ser **mais caras para recuperar** e têm **duração mínima cobrada** (30, 90 ou 180 dias).
- **EBS**: cobra pelo volume **provisionado** (GB/mês), usado ou não, e por IOPS/throughput provisionados em alguns tipos; snapshots cobram pelo armazenamento incremental.
- **EFS**: cobra pelo armazenamento **efetivamente usado**, por classe.
- Os modelos de compra de computação estão na seção 4.

#### AWS Free Tier

| Modelo | Como funciona |
|---|---|
| **Contas criadas a partir de 15/jul/2025** | **US$ 100 em créditos** no cadastro e **até US$ 100 a mais** ao concluir atividades com serviços básicos. Escolha entre **plano gratuito** (sem cobrança, acesso limitado, dura **6 meses ou até acabar os créditos**; depois a conta é fechada se não houver upgrade, com os dados retidos por 90 dias) e **plano pago** (acesso completo; uso acima dos créditos é cobrado) |
| **Sempre gratuito** (always free) | Mais de 30 serviços com cota mensal gratuita sem prazo (ex.: AWS Lambda com 1 milhão de requisições por mês; Amazon DynamoDB com 25 GB) |
| **Contas antigas (antes de 15/jul/2025)** | Modelo anterior de **12 meses gratuitos** em cotas específicas (ex.: 750 horas/mês de instância t2/t3.micro), que ainda aparece em muitos simulados |
| **Testes gratuitos** (trials) | Período de teste de alguns serviços a partir da ativação |

### Ferramentas de faturamento, orçamento e custo

#### Ferramentas de gestão de custos

| Ferramenta | O que faz | Quando é a resposta |
|---|---|---|
| **AWS Pricing Calculator** | **Estima o custo** de uma arquitetura **antes** de implantar, com estimativas exportáveis e compartilháveis | "Estimar o custo mensal de uma nova carga", "comparar cenários antes de migrar" |
| **AWS Billing and Cost Management console** | Faturas, formas de pagamento, histórico de pagamentos, créditos e alertas do Free Tier | "Ver e pagar a fatura", "baixar notas" |
| **AWS Cost Explorer** | **Visualiza e analisa** custos e uso **históricos** com filtros (serviço, conta, tag, Região), **prevê** gastos futuros e dá **recomendações de RI, Savings Plans e rightsizing** | "Quais serviços mais custaram nos últimos meses", "tendência de gastos" |
| **AWS Budgets** | Define **orçamentos** de custo, uso, utilização e cobertura de RI/Savings Plans e **envia alertas** (e-mail ou SNS) quando o valor **real ou previsto** ultrapassa o limite. **Budget actions** podem aplicar políticas do IAM, SCPs ou parar instâncias EC2/RDS | "Ser avisado antes de estourar o orçamento" |
| **AWS Cost and Usage Report (CUR)** | Relatório **mais completo e granular** (itens por hora, recurso e tag) entregue no **S3**, para análise com Athena, Redshift ou Quick Sight. Hoje é gerado pelo **AWS Data Exports** (CUR 2.0) | "Dados de faturamento mais detalhados possíveis" |
| **AWS Cost Anomaly Detection** | Usa machine learning para **detectar gastos anormais** e alertar | "Detectar picos de custo inesperados" |
| **Tags de alocação de custos** | Rótulos chave-valor que organizam o custo por projeto, equipe ou centro de custo | "Atribuir gastos por departamento" |
| **AWS Organizations (faturamento consolidado)** | Uma fatura para várias contas, desconto por volume agregado e compartilhamento de RI/Savings Plans | "Uma fatura única para todas as contas" |
| **AWS Billing Conductor** | Faturas personalizadas para **showback/chargeback** entre unidades ou clientes | "Refaturar para clientes internos" |
| **AWS Customer Carbon Footprint Tool** | Relatório do **impacto ambiental (emissões de carbono)** do seu uso da AWS, disponível **dentro do console de Billing and Cost Management** | "Medir o impacto ambiental do uso da AWS", "relatório de pegada de carbono" |
| **AWS Purchase Order Management** | Gerenciar **ordens de compra (POs)** e vinculá-las às faturas da AWS | "Controlar ordens de compra" — **não** serve para consultar preços |

- **Carbon Footprint Tool vs. pilar de Sustentabilidade vs. Compute Optimizer**: a **ferramenta** *mede e relata* as emissões; o **pilar** do Well-Architected dá *boas práticas* para reduzi-las; o **Compute Optimizer** recomenda *rightsizing* (que reduz custo e, de tabela, consumo). Quando o enunciado pede **relatório ou medição do impacto ambiental**, a resposta é a **ferramenta**, e o caminho de acesso é o **console de Billing**.

#### Tags de alocação de custos e relatórios
- **Dois tipos**:
  - **Geradas pela AWS** (prefixo `aws:`, como `aws:createdBy`).
  - **Definidas pelo usuário** (prefixo `user:` nos relatórios, como `user:Projeto`).
- As tags precisam ser **ativadas** no console de Billing para aparecer no **Cost Explorer** e no **Cost and Usage Report** (como colunas). Só valem **a partir da ativação**, não retroativamente.
- Em **Organizations**, a ativação é feita na **conta de gerenciamento**.
- **Cost Categories** agrupam custos por regras (ex.: "Marketing" = contas A e B + tag X).

#### Faturamento consolidado e alocação de custos em Organizations
- **Uma fatura** paga pela conta de gerenciamento, com o custo de cada conta-membro visível separadamente.
- **Uso combinado** para atingir faixas de volume mais baratas.
- **Compartilhamento de descontos** de Reserved Instances e Savings Plans entre as contas (pode ser desativado).
- **Sem custo adicional**.

### Suporte e recursos técnicos

#### Planos do AWS Support
Em dezembro de 2025, a AWS reorganizou os planos. O guia oficial do CLF-C02 já cita **Basic Support, AWS Business Support+, AWS Enterprise Support e AWS Unified Operations**.

| Plano | Preço inicial | Destaques | Resposta mais rápida |
|---|---|---|---|
| **Basic** | Gratuito, incluído em toda conta | Atendimento ao cliente **24/7 para conta e faturamento**, documentação, whitepapers, **re:Post**, **Health Dashboard** e **verificações principais do Trusted Advisor**. **Não inclui casos de suporte técnico** | — |
| **Business Support+** | A partir de **US$ 29/mês** por conta | Assistência com IA contextual e **acesso 24/7 a engenheiros** por telefone, chat e e-mail, **todas as verificações do Trusted Advisor**, **AWS Support API**, suporte a software de terceiros. Plano mínimo recomendado para **produção** | < 1 h para sistema de produção fora do ar; < 30 min para sistema crítico de negócio fora do ar |
| **Enterprise Support** | A partir de **US$ 5.000/mês** | **Technical Account Manager (TAM) designado**, especialista sênior de faturamento e conta, revisões Well-Architected, orientação proativa, **AWS Countdown Premium** (apoio a eventos planejados), AWS Security Incident Response incluído | **< 15 min** para sistema crítico de negócio fora do ar |
| **Unified Operations** | Mais alto, sob consulta | Tudo do Enterprise + **engenheiros especialistas de domínio designados**, **engenheiros de gestão de incidentes 24/7**, monitoramento de cargas, AWS Incident Detection and Response incluído | **< 5 min** para incidentes críticos |

- **Planos antigos (legado)**, ainda presentes em simulados e em contas existentes:
  - **Developer**: e-mail em horário comercial, orientação geral em < 24 h úteis e sistema prejudicado em < 12 h úteis. Encerra em **1º/jan/2027**; já não aceita novas assinaturas.
  - **Business**: 24/7 por telefone, chat e e-mail, produção fora do ar em < 1 h e todas as verificações do Trusted Advisor. Encerra em 1º/jan/2027 e foi substituído pelo **Business Support+**.
  - **Enterprise On-Ramp**: sistema crítico fora do ar em < 30 min, **pool de TAMs** e Concierge de faturamento. Encerra em 1º/jan/2027; os clientes são migrados automaticamente para o **Enterprise Support** ao longo de 2026.

##### Equivalência entre nomes antigos e novos

**Praticamente todos os simulados usam os nomes antigos.** Use esta tabela para traduzir o enunciado antes de responder:

| Nome no simulado (antigo) | Nome atual | O que continua valendo como resposta |
|---|---|---|
| **Basic** | **Basic** (não mudou) | Gratuito; **só conta e faturamento**, sem casos técnicos; core checks do Trusted Advisor; re:Post; Health Dashboard |
| **Developer** | *(encerrado — sem equivalente)* | E-mail em **horário comercial**, 1 contato, orientação geral < 24 h úteis. Em simulado, é o plano "mais barato **com** suporte técnico" |
| **Business** | **Business Support+** | **24/7 por telefone, chat e e-mail**; **todas** as verificações do Trusted Advisor; Support API; produção fora do ar **< 1 h**; **plano mínimo recomendado para produção** |
| **Enterprise On-Ramp** | *(migrado para Enterprise)* | **Pool** de TAMs; crítico fora do ar **< 30 min** |
| **Enterprise** | **Enterprise Support** | **TAM designado**, **Concierge**, revisões Well-Architected, crítico fora do ar **< 15 min** |
| *(não existia)* | **Unified Operations** | Engenheiros de incidentes 24/7; resposta **< 5 min** |

- **Palavras-chave** (funcionam nos dois esquemas de nomes):
  - "**TAM designado**" leva a **Enterprise** (ou Unified Operations).
  - "**Agente Concierge**" leva a **Enterprise** — o Concierge Support Team ajuda com faturamento e gestão de várias contas vinculadas. É exclusivo do Enterprise (o On-Ramp tinha uma versão reduzida).
  - "**Resposta em 15 minutos**" leva a **Enterprise**; em **5 minutos**, a **Unified Operations**; em **30 minutos**, a **Enterprise On-Ramp** (legado).
  - "**Resposta em 1 hora**" ou "**menor custo com suporte técnico 24/7 para produção**" leva a **Business / Business Support+**.
  - "**Plano mínimo recomendado para produção**" leva a **Business / Business Support+**.
  - "**Plano mais barato com todas as verificações do Trusted Advisor**" leva a **Business / Business Support+** (o Basic só tem as core checks).
  - "**Só dúvidas de conta e faturamento**" leva a **Basic**.
  - **Nunca é resposta**: suporte **no local** (*on-site*) de engenheiros da AWS e "APN sem custo adicional" não fazem parte de nenhum plano.
- **AWS Support Center**: onde se **abrem e acompanham casos** de suporte técnico, de conta e faturamento e de aumento de cotas.
- ***Advisor* não é um plano de suporte**: em questões do tipo "qual destes **não** é um plano de suporte?", a resposta é **Advisor** (é o *Trusted Advisor*, uma ferramenta).

#### Recursos técnicos e documentação

| Recurso | O que oferece |
|---|---|
| **Documentação da AWS** (docs.aws.amazon.com) | Guias de usuário, referências de API e tutoriais de cada serviço |
| **Whitepapers e guias** | Documentos técnicos oficiais (ex.: *Overview of AWS*, Well-Architected) |
| **AWS Blogs** | Anúncios, arquiteturas e boas práticas |
| **AWS Prescriptive Guidance** | **Estratégias, guias e padrões** testados para migração, modernização e operação |
| **AWS Knowledge Center** | Respostas às **perguntas mais frequentes** recebidas pelo suporte |
| **AWS re:Post** | **Comunidade de perguntas e respostas** moderada pela AWS, com respostas revisadas por especialistas (substituiu os AWS Forums) |
| **AWS Architecture Center e Solutions Library** | Arquiteturas de referência e soluções prontas |
| **AWS Online Tech Talks** | Apresentações **ao vivo e sessões gravadas** sobre como implementar serviços da AWS, com **oportunidade de perguntar diretamente a especialistas da AWS** durante a transmissão |
| **AWS Skill Builder e AWS Training and Certification** | Cursos e preparação para certificações |

- **Qual recurso para qual necessidade** (os quatro mais confundidos):
  - "Quero **exemplos de outros clientes** e **perguntar a especialistas da AWS**" → **AWS Online Tech Talks**.
  - "Quero a **referência técnica** de um serviço" → **Documentação da AWS**.
  - "Quero a **resposta a uma dúvida frequente** já respondida pelo suporte" → **AWS Knowledge Center**.
  - "Quero **perguntar à comunidade**" → **AWS re:Post**.

#### Assistência técnica, parceiros e AWS Marketplace
- **AWS Professional Services**: equipe global de consultores da própria AWS que ajuda empresas a alcançar resultados com a nuvem (migrações, modernização), em geral junto de parceiros.
- **AWS Managed Services (AMS)**: a AWS **assume a operação do dia a dia** do seu ambiente — operações contínuas, monitoramento, gestão de mudanças, aplicação de patches e segurança automatizada. É a resposta para "adotar a AWS em escala e **operar** de forma mais eficiente e segura", quando os distratores são CAF, Well-Architected e AWS Support. Regra curta: **CAF planeja, Well-Architected revisa, Support atende, AMS opera**.
- **Arquitetos de soluções da AWS** (solutions architects): orientam clientes sobre arquitetura e melhores práticas.
- **AWS Partner Network (APN)**: programa global de parceiros. Tipos principais:
  - **Integradores de sistemas e consultorias** (system integrators, SIs): projetam, migram e gerenciam cargas para os clientes.
  - **Fornecedores independentes de software** (ISVs): vendem softwares que rodam ou se integram à AWS, muitas vezes pelo Marketplace.
- **AWS Partner Solutions Finder**: catálogo para **encontrar um parceiro** AWS (consultoria ou ISV). Não é onde se **compra** software — isso é o Marketplace.
- **Benefícios de ser parceiro AWS**: treinamento e certificação para parceiros, eventos de parceiros, descontos por volume para parceiros, apoio de marketing e financiamento e visibilidade para clientes.
- **AWS Marketplace**: **catálogo digital** de softwares, dados e serviços de terceiros que rodam na AWS, com cobrança **na fatura da AWS**. Oferece opções de preço flexíveis (por hora, anual, BYOL, teste gratuito) e **ofertas privadas**.
  - **Gestão de custos**: gastos visíveis no Cost Explorer.
  - **Governança**: Private Marketplace com catálogo aprovado.
  - **Gestão de direitos de uso** (entitlement): controle das licenças adquiridas.
  - **Benefícios cobrados na prova** (questão do tipo "quais benefícios o cliente obtém ao usar o Marketplace? Escolha DUAS"):
    - **Velocidade nos negócios**: soluções prontas para usar, com implantação em minutos em vez de um ciclo de compra e instalação.
    - **Menos objeções legais**: **licenças e termos padronizados** pela AWS, o que encurta a revisão jurídica e de compras.
    - **Cobrança unificada** na própria fatura da AWS e opções de preço flexíveis.
    - *Alternativas falsas típicas*: "só produtos open source", "nenhum produto precisa de licença", "uso gratuito de todos os serviços na primeira hora".
- **AWS Trust & Safety**: canal para **denunciar abuso** de recursos AWS (seção 3).

### Decisão rápida — Faturamento, Preços e Suporte

| Cenário / requisito | Resposta correta | Distratores clássicos |
|---|---|---|
| Estimar o custo antes de implantar | AWS Pricing Calculator | Cost Explorer, Budgets |
| Analisar gastos históricos e tendências | AWS Cost Explorer | Pricing Calculator, CUR |
| Alertar quando o gasto real ou previsto passar do limite | AWS Budgets | Cost Explorer, Trusted Advisor |
| Dados de custo mais granulares, por hora e por recurso | AWS Cost and Usage Report | Cost Explorer |
| Atribuir custos por projeto ou equipe | Tags de alocação de custos | Organizations sozinho, IAM |
| Uma fatura para várias contas com desconto por volume | Faturamento consolidado (Organizations) | Budgets, Control Tower |
| Detectar gasto anormal automaticamente | Cost Anomaly Detection | Budgets, CloudTrail |
| Tráfego de entrada da internet | Gratuito | Cobrado por GB |
| Tráfego de saída para a internet | Cobrado por GB | Gratuito |
| Só suporte de conta e faturamento, sem custo | Basic Support | Business Support+ |
| Menor custo com acesso 24/7 a engenheiros | Business Support+ (antigo Business) | Enterprise, Basic |
| Plano mínimo recomendado para produção | Business Support+ (antigo Business) | Developer, Enterprise |
| Todas as verificações do Trusted Advisor pelo menor preço | Business Support+ (antigo Business) | Basic, Developer |
| Resposta em 1 hora para produção fora do ar | Business Support+ (antigo Business) | Developer |
| TAM designado e resposta em 15 minutos | Enterprise Support | Business Support+ |
| Agente **Concierge** para faturamento e contas vinculadas | Enterprise Support | Business, Developer, Basic |
| Engenheiros de incidentes 24/7 e resposta em 5 minutos | Unified Operations | Enterprise Support |
| Item que **não** é um plano de suporte | Advisor (é o Trusted Advisor) | Basic, Developer, Enterprise |
| Medir o impacto ambiental do uso da AWS | AWS Customer Carbon Footprint Tool | Pilar de Sustentabilidade, Compute Optimizer |
| Como a AWS calcula o preço | Pelo uso dos serviços e recursos consumidos | Nº de contas, de usuários ou de instâncias |
| Serviço sempre gratuito | IAM (também Organizations, CloudFormation, VPC, Auto Scaling) | S3, ELB, WAF |
| Cobrança do EC2 | Por hora/segundo de instância **em execução** | Por instância criada |
| Cobrança do RDS | Por hora de banco **em execução** | Por requisição |
| Cobrança do S3 | Por GB armazenado por mês | Por hora, por requisição de download |
| Aprender com exemplos e perguntar a especialistas da AWS | AWS Online Tech Talks | Documentação, re:Post, Health Dashboard |
| AWS operar o ambiente no dia a dia | AWS Managed Services (AMS) | CAF, Well-Architected, AWS Support |
| Encontrar um parceiro AWS | AWS Partner Solutions Finder | AWS Marketplace, Support Center |
| Abrir caso técnico ou pedir aumento de cota | AWS Support Center / Service Quotas | re:Post |
| Guias e padrões de migração testados | AWS Prescriptive Guidance | Knowledge Center |
| Perguntas frequentes respondidas pelo suporte | AWS Knowledge Center | Prescriptive Guidance |
| Comunidade de perguntas e respostas | AWS re:Post | AWS Support Center |
| Consultoria da própria AWS para migração | AWS Professional Services | AWS Marketplace |
| Empresa parceira para implementar a migração | Parceiro AWS (integrador de sistemas) | Trust & Safety |
| Comprar software de terceiros na fatura AWS | AWS Marketplace | AWS Artifact |

---

## 12. Padrões recorrentes e palavras-chave

As questões do Cloud Practitioner costumam girar em torno de poucas confusões. Esta seção reúne as palavras do enunciado que apontam para cada resposta e os pares de serviços que mais se confundem.

### Palavras-chave do enunciado

| Se o enunciado diz… | Pense em… |
|---|---|
| "Pagar só pelo que usa", "sem investimento inicial" | Despesa variável, pay-as-you-go |
| "Ajustar automaticamente à demanda" | Elasticidade, Auto Scaling |
| "Gerenciado", "reduzir esforço operacional" | Serviço gerenciado (RDS, Fargate, Lambda, Elastic Beanstalk) |
| "Sem servidor", "sem provisionar servidores" | Lambda, Fargate, DynamoDB, Athena, S3 |
| "Quem fez", "chamadas de API", "auditoria de ações" | CloudTrail |
| "Histórico de configuração", "recurso em conformidade com regra" | Config |
| "Métrica", "alarme", "logs da aplicação" | CloudWatch |
| "Recomendações de boas práticas", "verificações" | Trusted Advisor |
| "Relatórios de conformidade da AWS", "SOC", "PCI", "ISO" | AWS Artifact |
| "Estimar custo antes" | Pricing Calculator |
| "Analisar gastos passados" | Cost Explorer |
| "Alertar ao passar do orçamento" | Budgets |
| "Mais detalhado", "por hora", "por recurso" | Cost and Usage Report |
| "Conexão privada dedicada", "não passar pela internet" | Direct Connect |
| "Criptografada pela internet", "rápida de configurar" | Site-to-Site VPN |
| "Baixa latência global para conteúdo" | CloudFront |
| "Desacoplar", "fila" | SQS |
| "Notificar", "fan-out", "pub/sub" | SNS |
| "Credenciais temporárias" | IAM role / STS |
| "Uma fatura para várias contas" | Organizations (faturamento consolidado) |
| "Limitar permissões máximas das contas" | SCP |
| "Interrupção aceitável", "menor custo possível" | Spot Instances |
| "Licença por núcleo/socket" | Dedicated Hosts |
| "TAM designado" | Enterprise Support ou Unified Operations |
| "Agente Concierge" | Enterprise Support |
| "Isolamento físico da carga" | Dedicated Hosts / Servidores dedicados |
| "Monolito em microsserviços", "falha de um componente não derruba o resto" | Acoplamento fraco (SQS, Lambda, ECS) |
| "Milhares de arquivos para processar" | Várias instâncias/tarefas em paralelo (Batch) |
| "Conectividade intermitente", "processar localmente sem internet" | Snowball Edge (computação na borda) |
| "Comprar/assinar dados de terceiros" | AWS Data Exchange |
| "Perguntas em linguagem natural com gráficos" | Amazon QuickSight Q |
| "Pegada de carbono", "impacto ambiental do meu uso" | AWS Customer Carbon Footprint Tool |
| "IDE na nuvem", "escrever e depurar pelo navegador" | AWS Cloud9 |
| "Projetar visualmente app serverless" | AWS Application Composer |
| "AWS operar meu ambiente no dia a dia" | AWS Managed Services (AMS) |
| "Perguntar a especialistas da AWS em apresentações" | AWS Online Tech Talks |
| "Coletar evidências para auditoria da minha carga" | AWS Audit Manager |
| "Capacidade do CAF", "perspectiva do CAF" | Tabela de capacidades na seção 1 |

### Pares que mais se confundem

| Par | Como separar |
|---|---|
| **CloudTrail vs. CloudWatch vs. Config** | CloudTrail = quem fez qual ação (API); CloudWatch = desempenho e logs; Config = configuração e conformidade ao longo do tempo |
| **Security group vs. network ACL** | SG = instância, stateful, só allow; NACL = sub-rede, stateless, allow e deny |
| **Shield vs. WAF** | Shield = DDoS (camadas 3/4; Advanced também 7); WAF = regras de requisição HTTP (SQL injection, XSS) |
| **GuardDuty vs. Inspector vs. Macie** | GuardDuty = ameaças e comportamento malicioso; Inspector = vulnerabilidades de software; Macie = dados sensíveis no S3 |
| **KMS vs. CloudHSM** | KMS = chaves gerenciadas em HSM multi-tenant da AWS; CloudHSM = HSM dedicado e controle exclusivo do cliente |
| **IAM Identity Center vs. Cognito** | Identity Center = funcionários acessando contas e apps; Cognito = clientes finais acessando o seu aplicativo |
| **Organizations vs. Control Tower** | Organizations = estrutura de contas, SCPs e faturamento; Control Tower = landing zone pronta com guardrails sobre o Organizations |
| **Multi-AZ vs. Read Replica** | Multi-AZ = alta disponibilidade (failover); Read Replica = escalar leituras |
| **Várias AZs vs. várias Regiões** | AZs = alta disponibilidade; Regiões = DR regional, latência global, soberania de dados |
| **EBS vs. instance store vs. EFS** | EBS = bloco persistente de uma instância; instance store = bloco temporário; EFS = arquivos compartilhados por várias instâncias |
| **S3 lifecycle vs. Intelligent-Tiering** | Lifecycle = regra por idade que você define; Intelligent-Tiering = movimento automático pelo acesso real |
| **RDS vs. DynamoDB vs. Redshift** | RDS = relacional transacional; DynamoDB = NoSQL em escala; Redshift = data warehouse analítico |
| **CloudFront vs. Global Accelerator** | CloudFront = cache de conteúdo HTTP; Global Accelerator = rede AWS e IPs estáticos para TCP/UDP, sem cache |
| **SQS vs. SNS vs. EventBridge** | SQS = fila (pull); SNS = notificação (push); EventBridge = roteamento de eventos com regras, inclusive SaaS |
| **SNS vs. SES** | SNS = notificações para assinantes de tópicos; SES = serviço de e-mail |
| **WorkSpaces vs. AppStream 2.0** | WorkSpaces = desktop completo; AppStream 2.0 = uma aplicação transmitida |
| **Elastic Beanstalk vs. CloudFormation** | Beanstalk = envia o código e ele cuida do ambiente; CloudFormation = você descreve cada recurso em um template |
| **Lightsail vs. EC2** | Lightsail = simples, preço fixo mensal; EC2 = controle e flexibilidade totais |
| **Reserved Instances vs. Savings Plans** | RI = desconto atrelado a atributos da instância; Savings Plans = compromisso de gasto por hora, mais flexível |
| **Dedicated Hosts vs. Dedicated Instances** | Hosts = servidor inteiro com visibilidade de sockets/núcleos (BYOL); Instances = hardware isolado sem essa visibilidade |
| **Cost Explorer vs. Budgets vs. Pricing Calculator** | Passado vs. alerta vs. estimativa futura |
| **Trusted Advisor vs. Compute Optimizer** | Trusted Advisor = verificações amplas em seis categorias; Compute Optimizer = rightsizing detalhado com ML |
| **Knowledge Center vs. re:Post vs. Prescriptive Guidance** | Knowledge Center = perguntas frequentes; re:Post = comunidade; Prescriptive Guidance = estratégias e padrões |
| **AWS Artifact vs. AWS Marketplace** | Artifact = relatórios de conformidade da AWS; Marketplace = compra de software de terceiros |
| **AWS Artifact vs. AWS Audit Manager** | Artifact = relatórios de conformidade **da AWS**; Audit Manager = automatiza a coleta de evidências **da sua** carga |
| **AWS Marketplace vs. Data Exchange vs. Partner Solutions Finder** | Marketplace = comprar **software**; Data Exchange = comprar **dados**; Solutions Finder = encontrar **parceiros** |
| **Athena vs. S3 Select** | Athena = SQL padrão sobre **vários objetos**, gera relatórios; S3 Select = filtra dentro de **um objeto** |
| **Quick Sight vs. QuickSight Q** | Quick Sight = dashboards; QuickSight Q = **perguntas em linguagem natural** com visualizações |
| **Cloud9 vs. CloudShell vs. CodeBuild** | Cloud9 = IDE completa no navegador; CloudShell = terminal com a CLI; CodeBuild = compila e testa |
| **Application Composer vs. App Runner** | Composer = **desenhar** a app serverless; App Runner = **rodar** contêiner/app web gerenciado |
| **AMS vs. CAF vs. Well-Architected vs. Support** | AMS opera; CAF planeja; Well-Architected revisa; Support atende |
| **Multi-AZ vs. Read Replica vs. Read Replica cross-Region** | HA na Região; escalar leitura; **DR contra perda da Região** |
| **Redundância vs. elasticidade** | Redundância → alta **disponibilidade**; elasticidade → **escalabilidade** |
| **Health Dashboard vs. Service Health Dashboard** | Mesmo serviço: "Service Health Dashboard" é o **nome antigo** da visão pública |
| **Snowball Edge: transferência vs. computação** | Rede lenta e petabytes → transferência; conectividade intermitente e processar no local → computação na borda |
| **Online Tech Talks vs. Knowledge Center vs. re:Post vs. Prescriptive Guidance** | Apresentações com especialistas; FAQ do suporte; comunidade; estratégias e padrões |

### Afirmações falsas que aparecem como alternativa
- "A AWS é responsável por aplicar patches no sistema operacional das instâncias EC2" — **falso**, é o cliente.
- "Security groups podem negar um IP específico" — **falso**, só permitem.
- "SCPs concedem permissões" — **falso**, só limitam.
- "Direct Connect é criptografado por padrão" — **falso**.
- "Savings Plans garantem capacidade" — **falso**; use Capacity Reservations.
- "Multi-AZ do RDS serve para escalar leituras" — **falso**; use Read Replicas.
- "Tráfego de entrada na AWS é cobrado" — **falso**, é gratuito.
- "O plano Basic inclui casos de suporte técnico" — **falso**, cobre conta e faturamento.
- "A certificação da AWS torna a aplicação do cliente automaticamente conforme" — **falso**.
- "Lambda executa processos de várias horas" — **falso**, o limite é 15 minutos.
- "Construir arquiteturas com componentes **fortemente** acoplados" — **falso**, o princípio é o acoplamento **fraco**.
- "Considerar servidores como recursos **não** descartáveis" — **falso**, o princípio é tratá-los como **descartáveis**.
- "Provisionar **mais** capacidade do que a carga precisa" — **falso**, o princípio é **parar de adivinhar** a capacidade.
- "Tornar as decisões arquiteturais eventos **únicos e estáticos**" — **falso**, o princípio é **arquitetura evolutiva**.
- "Enfatizar processos **manuais** para permitir alterações" — **falso**, o princípio é **automatizar**.
- "RDS Multi-AZ protege contra a perda de uma **Região** inteira" — **falso**, o standby fica na mesma Região; use **Read Replica cross-Region**.
- "O Marketplace só oferece produtos **open source**" ou "nenhum produto precisa de licença" — **falso**.
- "Existem **vários usuários raiz**, um por ambiente" — **falso**, há **um só** root por conta.
- "Suporte **no local** (*on-site*) de engenheiros da AWS" — **falso**, nenhum plano inclui isso.
- "Uma instância EC2 **parada** não gera nenhum custo" — **falso**: a instância não é cobrada, mas o **volume EBS anexado é**.

### Serviços que aparecem quase só como distrator

São serviços **reais**, mas que raramente são a resposta. Reconhecer o que cada um faz elimina a alternativa em segundos.

| Serviço | O que realmente faz | Confundido com |
|---|---|---|
| **AWS Audit Manager** | Automatiza a **coleta de evidências** para auditorias da **sua** carga | AWS Artifact |
| **Amazon Pinpoint** | Engajamento de cliente: campanhas por e-mail, SMS e push | SES, SNS, Personalize |
| **AWS Data Pipeline** | Orquestração de movimentação e transformação de dados (legado) | Glue, Step Functions |
| **AWS OpsWorks** | Gestão de configuração com **Chef e Puppet** gerenciados | Systems Manager, Elastic Beanstalk |
| **AWS App Runner** | Rodar **contêiner ou app web** direto do repositório, gerenciado | Fargate, Elastic Beanstalk, Application Composer |
| **Amazon Elastic Transcoder** | **Transcodificação de vídeo** (legado; hoje AWS Elemental MediaConvert) | CloudFront |
| **Amazon WorkLink** | Acesso seguro a sites internos de **dispositivos móveis** (descontinuado) | WorkSpaces Secure Browser, AppStream 2.0 |
| **AWS Server Migration Service (SMS)** | Migração de **VMs** on-premises (substituído pelo **MGN**) | Application Migration Service |
| **AWS Purchase Order Management** | Gerenciar **ordens de compra** na fatura | Pricing Calculator, Cost Explorer |
| **AWS Partner Solutions Finder** | **Encontrar parceiros** AWS | AWS Marketplace |
| **Amazon S3 Select** | **Filtrar** dados dentro de **um único objeto** do S3 | Athena |
| **Amazon MemoryDB** (for Valkey/Redis) | Banco **em memória durável** (é o banco principal, não cache) | ElastiCache, DynamoDB |
| **AWS CodeCommit** | **Repositório Git** gerenciado | CodeArtifact, CodeBuild |
| **AWS Service Health Dashboard** | Nome **antigo** do AWS Health Dashboard | AWS Health Dashboard, Inspector |
| **AWS AppSync** | APIs **GraphQL** gerenciadas | API Gateway, Amplify |
| **AWS Device Farm** | Testar apps em **dispositivos reais** na nuvem | Amplify |
| **Placement group** | Controle do **posicionamento físico** de instâncias EC2 (cluster, spread, partition) | Multi-AZ, Auto Scaling |
| **EC2 Auto Recovery** | Recupera a instância após falha de hardware, **na mesma AZ** | Auto Scaling, Multi-AZ |
| **AWS Resource Access Manager (RAM)** | **Compartilhar recursos** entre contas | Organizations, IAM |

### Nomes que não existem (distratores inventados)

Reconhecer que o serviço **não existe** elimina a alternativa na hora. Os simulados usam com frequência:

`AWS Protector` · `AWS Firewall Security` · `Amazon Monitor` / `AWS Monitor` · `AWS Audit` · `Amazon Desktop` · `AWS Network` · `Amazon Analytics` · `IAM Access Pool` · `Multi-Instances` · `AWS ETL` · `Amazon Elastic Block Storage` (o correto é Elastic Block **Store**) · `AWS Simple Token Service` (o correto é **Security** Token Service — STS)

- Cuidado também com **prefixo trocado**: a prova às vezes escreve "AWS S3", "AWS RDS", "AWS Lambda", "Amazon CloudFront". O prefixo correto (*Amazon* para serviços de infraestrutura nomeados, *AWS* para os demais) **não** é critério de resposta — não elimine uma alternativa só pelo prefixo.

### Divergências conhecidas entre a documentação atual e os simulados

Onde estudar pela AWS e responder pelo simulado dão resultados diferentes. Em cada caso, saiba **as duas respostas** e escolha pela origem da questão.

| Tema | Simulado antigo espera | Documentação atual da AWS | Como decidir |
|---|---|---|---|
| **Nº de AZs por Região** | "Pelo menos **duas**" | Regiões novas são projetadas com **no mínimo três** | Se a pergunta é "em quantas AZs implantar para HA?", a resposta é **duas** em qualquer caso |
| **Planos de suporte** | Basic, Developer, Business, Enterprise On-Ramp, Enterprise | Basic, **Business Support+**, Enterprise, **Unified Operations** | Traduza pela tabela de equivalência da seção 11 |
| **Família Snow** | Snowball / Snowball Edge / Snowmobile como resposta correta | Fechada para novos clientes desde nov/2025 | Em simulado, continue respondendo Snowball/Snowmobile |
| **Free Tier** | "12 meses grátis", 750 h de t2.micro | Créditos + plano gratuito de 6 meses (contas desde 15/jul/2025) | Veja a data no enunciado; sem data, o simulado quer o modelo antigo |
| **Tarefas exclusivas do root** | Inclui "**alterar ou cancelar o plano de suporte**" | A lista atual do IAM **não** traz mais esse item | Se a alternativa aparecer entre ações banais (ver relatórios, mudar recurso, conceder acesso), **ela é o gabarito esperado** |
| **Amazon QLDB** | Resposta para "registro imutável e verificável" | Suporte encerrado em jul/2025 | Reconheça o nome; em simulado, ainda é a resposta |
| **AWS CodeStar** | Resposta para "pipeline CI/CD rápido" | Descontinuado em jul/2024 | Idem |
| **Capacidades do CAF – Security** | Alguns gabaritos marcam "gestão de incidentes e problemas" | Essa capacidade é de **Operations**; as de Security são **resposta a incidentes** e **proteção de infraestrutura** | **Erro de gabarito.** Estude pela documentação |

---

## 13. Mapa de Domínios do Exame

Cada domínio oficial tem um peso diferente na nota final (24/30/34/12%). Esta seção cruza os tópicos das seções 1 a 11 com o domínio que eles testam, para priorizar a revisão pelo que realmente pesa na prova.

### Domínio 1 — Cloud Concepts (24%)

| Tópico | Onde revisar |
|---|---|
| Seis vantagens da nuvem, elasticidade, agilidade, alta disponibilidade | Seção 1 |
| Benefícios da infraestrutura global (velocidade, alcance) | Seções 1 e 2 |
| Seis pilares do Well-Architected e diferenças entre eles | Seção 1 |
| **Princípios gerais de design** e conceitos de arquitetura (acoplamento fraco, stateless, descartável, paralelismo, redundância vs. elasticidade) | Seção 1 |
| AWS CAF: perspectivas, **capacidades de cada perspectiva** e resultados de negócio | Seção 1 |
| 7 Rs e ferramentas de migração (MGN, DMS, SCT, Discovery, Migration Hub, Migration Evaluator, Snowball Edge, AMS) | Seções 1 e 6 |
| Custos fixos vs. variáveis, TCO, BYOL vs. License Included, rightsizing, automação, economias de escala | Seção 1 |

### Domínio 2 — Security and Compliance (30%)

| Tópico | Onde revisar |
|---|---|
| Fundamentos: confidencialidade, integridade, disponibilidade, autenticidade, controle de acesso | Seção 3 |
| Modelo de responsabilidade compartilhada (EC2, RDS, Lambda) | Seção 3 |
| IAM: usuários, grupos, roles, políticas, menor privilégio, MFA | Seção 3 |
| Tarefas exclusivas e proteção do usuário root | Seção 3 |
| IAM Identity Center, federação, Cognito, cross-account roles | Seção 3 |
| Secrets Manager e Parameter Store | Seção 3 |
| Organizations, SCPs, Control Tower | Seção 3 |
| Criptografia em repouso e em trânsito, KMS, CloudHSM, ACM, Macie | Seção 3 |
| WAF, Shield, Firewall Manager, security groups e NACLs | Seções 3 e 7 |
| GuardDuty, Inspector, Detective, Security Hub, Trusted Advisor | Seções 3 e 10 |
| CloudTrail, Config, CloudWatch, relatórios de acesso | Seções 3 e 10 |
| AWS Artifact, programas de conformidade, fontes de informação, Marketplace | Seção 3 |

### Domínio 3 — Cloud Technology and Services (34%)

| Tópico | Onde revisar |
|---|---|
| Console, CLI, SDK, API, IaC; operação única vs. repetível; modelos de implantação | Seções 1 e 10 |
| Regiões, AZs, edge locations, múltiplas Regiões | Seção 2 |
| Tipos de instância EC2, contêineres, serverless, Auto Scaling, ELB | Seção 4 |
| RDS (Multi-AZ, Read Replica, DR cross-Region), Aurora, DynamoDB, ElastiCache, bancos especializados, DMS/SCT | Seção 6 |
| Componentes e segurança da VPC, **quais serviços exigem VPC**, Route 53, VPN, Direct Connect, CloudFront | Seção 7 |
| S3 e classes, lifecycle, EBS, instance store, EFS, FSx, Storage Gateway, AWS Backup | Seção 5 |
| Serviços de IA/ML e de analytics, **QuickSight Q**, **Data Exchange** | Seção 8 |
| Integração, aplicações de negócio, usuário final, Amplify, IoT, ferramentas de desenvolvimento (**Cloud9**, **Application Composer**, **CodeStar**) | Seção 9 |

### Domínio 4 — Billing, Pricing, and Support (12%)

| Tópico | Onde revisar |
|---|---|
| Modelos de compra de computação, flexibilidade de RI, **como contar RI em Organizations** | Seções 4 e 11 |
| Custos de transferência de dados e de armazenamento; **unidade de cobrança de cada serviço**; serviços sempre gratuitos | Seção 11 |
| Pricing Calculator, Cost Explorer, Budgets, CUR, tags de alocação, **Carbon Footprint Tool** | Seção 11 |
| Faturamento consolidado | Seções 3 e 11 |
| Planos de suporte (**nomes antigos e novos**, Concierge), Support Center, Trusted Advisor, Health Dashboard e Health API | Seções 10 e 11 |
| Recursos técnicos (**Online Tech Talks**), Professional Services, **AMS**, APN, Marketplace e seus benefícios, Trust & Safety | Seções 3 e 11 |

### Observação sobre o modelo de pontuação

O CLF-C02 usa pontuação **compensatória**: não é preciso atingir a nota mínima em cada domínio separadamente, só na prova como um todo. Como **Tecnologia e serviços (34%)** e **Segurança e conformidade (30%)** somam 64% da nota, as seções 3 a 10 deste guia têm o maior retorno por hora de estudo. O Domínio 4 pesa só 12%, mas é o mais "decorável": vale revisar a seção 11 na véspera.

---

## 14. Autoteste — Flashcards de Revisão Rápida

Cada card abaixo esconde a resposta: clique para expandir só depois de tentar responder mentalmente. O objetivo é forçar recall ativo, não releitura passiva. Uma rodada de 15 a 20 cards por dia nos dias antes da prova cobre todo o banco.

### Conceitos de Nuvem

> [!question]- Uma startup quer evitar a compra de servidores antes de saber quantos clientes terá. Qual vantagem da nuvem atende a esse objetivo?
> **Trocar despesa fixa (CapEx) por despesa variável (OpEx)**: paga-se apenas pelo que é consumido, sem investimento inicial em hardware. "Parar de adivinhar a capacidade" também ajuda, mas o foco no investimento inicial aponta para a despesa variável.

> [!question]- Qual é a diferença entre elasticidade e escalabilidade?
> **Escalabilidade** é a capacidade de crescer para atender a uma carga maior (vertical ou horizontal). **Elasticidade** é ajustar os recursos **automaticamente** para cima e para baixo conforme a demanda, liberando o que não é mais necessário.

> [!question]- Por que a AWS consegue oferecer preços por unidade menores do que uma empresa conseguiria no próprio data center?
> Por **economias de escala**: a AWS agrega o uso de centenas de milhares de clientes, compra e opera em volume e repassa custos menores.

> [!question]- Quais são os seis pilares do AWS Well-Architected Framework?
> Excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade.

> [!question]- "Executar operações como código" e "fazer mudanças pequenas, frequentes e reversíveis" pertencem a qual pilar do Well-Architected?
> **Excelência operacional**.

> [!question]- "Recuperar-se automaticamente de falhas" e "testar os procedimentos de recuperação" pertencem a qual pilar?
> **Confiabilidade**.

> [!question]- Uma empresa quer medir e reduzir o impacto ambiental de suas cargas de trabalho. Qual pilar trata disso?
> **Sustentabilidade**. Se o foco fosse o gasto, seria otimização de custos.

> [!question]- Quais são as seis perspectivas do AWS Cloud Adoption Framework (CAF)?
> **Business, People e Governance** (capacidades de negócio) e **Platform, Security e Operations** (capacidades técnicas).

> [!question]- Quais resultados de negócio o AWS CAF destaca?
> Redução do risco de negócio, melhora no desempenho ESG, aumento de receita e aumento da eficiência operacional.

> [!question]- Uma empresa move servidores on-premises para EC2 sem alterar as aplicações. Qual estratégia de migração é essa e qual serviço a apoia?
> **Rehost** ("lift and shift"), com o **AWS Application Migration Service (MGN)**.

> [!question]- Uma empresa migra seu banco MySQL de um servidor próprio para o Amazon RDS, sem mudar a aplicação. Qual dos 7 Rs é esse?
> **Replatform** ("lift, tinker and shift"): uma otimização de nuvem (banco gerenciado) sem mudar a arquitetura central.

> [!question]- Qual é a diferença entre Retire e Retain?
> **Retire** desliga aplicações que não são mais necessárias. **Retain** mantém a aplicação on-premises por enquanto, para rever depois.

> [!question]- Qual ferramenta ajuda a montar o caso de negócio e estimar o custo de migrar o ambiente on-premises para a AWS?
> **Migration Evaluator**. O Pricing Calculator estima uma arquitetura específica; o Migration Evaluator parte do inventário real on-premises.

> [!question]- Uma empresa já tem licenças de software vinculadas a núcleos físicos e quer reaproveitá-las na AWS. Qual modelo de licenciamento e qual opção de EC2?
> **BYOL (Bring Your Own License)** em **EC2 Dedicated Hosts**, com controle pelo **AWS License Manager**.

> [!question]- O que é rightsizing e quando ele deve ser feito?
> Ajustar tipo e tamanho dos recursos ao uso real medido. Deve vir **antes** de assumir compromissos como Savings Plans ou Reserved Instances, para não congelar desperdício.

> [!question]- A qual perspectiva do CAF pertencem "resposta a incidentes" e "proteção de infraestrutura"? E "observabilidade" e "gestão de incidentes e problemas"?
> As duas primeiras são de **Security**; as duas últimas são de **Operations**. É a confusão mais explorada: *resposta a incidentes* = segurança, *gestão de incidentes e problemas* = operações.

> [!question]- A qual perspectiva do CAF pertence "fluência em nuvem"? E "gestão de benefícios"? E "engenharia de dados" e "CI/CD"?
> **People** (fluência em nuvem), **Governance** (gestão de benefícios, para definir e acompanhar resultados de negócio) e **Platform** (engenharia de dados e CI/CD).

> [!question]- Cite três princípios gerais de design do Well-Architected.
> Entre os seis: **parar de adivinhar a capacidade**, **testar sistemas em escala de produção**, **automatizar para facilitar a experimentação**, **permitir arquiteturas evolutivas**, **orientar arquiteturas usando dados** e **melhorar com dias de teste (game days)**.

> [!question]- O que é uma arquitetura fracamente acoplada e por que a AWS a recomenda?
> Componentes independentes que se comunicam por **fila, tópico ou API** (SQS, SNS, EventBridge). A falha ou lentidão de um **não derruba os outros**, e cada componente escala sozinho. É o princípio por trás de decompor um monolito em microsserviços.

> [!question]- Qual princípio de arquitetura sustenta a **alta disponibilidade** e qual sustenta a **escalabilidade**?
> **Redundância** → alta disponibilidade (duplicar para eliminar ponto único de falha). **Elasticidade** → escalabilidade (ajustar a quantidade de recursos conforme a demanda).

> [!question]- Para processar milhares de vídeos ou imagens, o que a arquitetura AWS recomenda?
> **Várias instâncias (ou tarefas/funções) em paralelo** — princípio do paralelismo. Não é "uma instância enorme com GPU" nem "hardware dedicado".

> [!question]- É possível migrar um monolito para o ECS sem refatorar?
> **Sim**, e às vezes é o primeiro passo. Mas ele **não ganha os benefícios de microsserviços** (escala e implantação independentes, falha isolada). "O ECS não aceita monolito" e "a aplicação fica mais rápida" são as duas afirmações falsas.

> [!question]- Quais são as duas funções do AWS Snowball Edge?
> **Transferência offline** de grandes volumes quando a rede é lenta, e **processamento de dados no local** (computação na borda) onde a conectividade é **intermitente ou inexistente**.

> [!question]- Qual a diferença entre AWS CAF, Well-Architected, AWS Support e AWS Managed Services (AMS)?
> **CAF planeja** a adoção, **Well-Architected revisa** a arquitetura, **Support atende** quando você abre um caso e **AMS opera** o ambiente para você no dia a dia.

> [!question]- Qual ferramenta mede o impacto ambiental do seu uso da AWS, e onde ela fica?
> **AWS Customer Carbon Footprint Tool**, dentro do **console de Billing and Cost Management**. O *pilar de Sustentabilidade* dá boas práticas, não mede; o *Compute Optimizer* recomenda rightsizing.

### Infraestrutura Global

> [!question]- Qual é a relação entre Regiões, Availability Zones e edge locations?
> Uma **Região** contém várias **AZs** (em geral três ou mais); cada AZ tem um ou mais data centers com energia e rede independentes. As **edge locations** ficam fora das Regiões, perto dos usuários, e atendem CloudFront, Route 53, Global Accelerator e Shield.

> [!question]- Como alcançar alta disponibilidade dentro de uma Região?
> Distribuindo os recursos em **várias Availability Zones**, por exemplo com um ELB e um Auto Scaling group em duas ou mais AZs. As AZs não compartilham ponto único de falha.

> [!question]- Cite quatro motivos para usar várias Regiões.
> Recuperação de desastres, continuidade de negócios, baixa latência para usuários em outras partes do mundo e soberania de dados.

> [!question]- Uma lei exige que os dados de clientes fiquem no Brasil. Qual é o critério decisivo na escolha da Região?
> **Conformidade e soberania de dados**: escolher a Região no Brasil (São Paulo). Latência, serviços disponíveis e preço só são comparados entre Regiões que atendem à lei.

> [!question]- Qual opção leva infraestrutura e serviços da AWS para dentro do data center do cliente?
> **AWS Outposts**.

> [!question]- Local Zones ou Wavelength Zones: qual atende a aplicações móveis 5G de ultrabaixa latência?
> **Wavelength Zones**, que ficam dentro das redes 5G das operadoras. Local Zones aproximam recursos de uma área metropolitana.

> [!question]- Cite três serviços globais da AWS.
> **IAM**, **Route 53** e **CloudFront** (também AWS Organizations). A maioria dos outros serviços, como EC2 e RDS, é regional.

> [!question]- Quantas AZs uma Região da AWS tem, e em quantas você deve implantar para ter alta disponibilidade?
> **Implantar para HA: no mínimo duas** — essa resposta vale sempre. **Quantas a Região tem**: a AWS hoje projeta Regiões com **no mínimo três**, mas muitos simulados antigos ainda respondem "pelo menos duas". Leia qual das duas perguntas está sendo feita.

### Segurança e Conformidade

> [!question]- No modelo de responsabilidade compartilhada, quem aplica patches no sistema operacional de uma instância EC2? E no engine de banco do Amazon RDS?
> No EC2, o **cliente** aplica patches no SO convidado. No RDS, a **AWS** aplica patches no SO e no engine do banco.

> [!question]- Cite três controles compartilhados entre AWS e cliente.
> **Gestão de patches**, **gestão de configuração** e **conscientização e treinamento**. Cada lado executa a sua parte em camadas diferentes.

> [!question]- Qual responsabilidade é sempre do cliente, em qualquer serviço?
> Os **dados** e o **controle de acesso** a eles (IAM, políticas, escolha de criptografia).

> [!question]- Com quais permissões um novo usuário do IAM começa?
> **Nenhuma**. Todas as permissões precisam ser concedidas explicitamente.

> [!question]- Uma aplicação em EC2 precisa ler objetos no S3. Qual é a forma recomendada de dar acesso?
> Uma **IAM role** anexada à instância (instance profile), que fornece **credenciais temporárias**. Nunca guardar access keys na instância ou no código.

> [!question]- O que acontece quando uma política do IAM concede `Allow` e outra aplicável tem `Deny` explícito para a mesma ação?
> O **Deny explícito sempre vence**.

> [!question]- Cite três boas práticas para proteger o usuário root.
> Habilitar **MFA**, **não criar access keys** para o root e usá-lo **somente** para tarefas que o exigem (no dia a dia, usar um usuário administrativo). Em Organizations, remover as credenciais root das contas-membro.

> [!question]- Cite quatro tarefas que só o usuário root pode fazer.
> Alterar e-mail, senha ou access keys do root (conta avulsa); fechar a conta (conta avulsa); restaurar permissões do IAM quando o único administrador as perdeu; ativar o acesso do IAM ao console de faturamento; registrar-se como vendedor no Reserved Instance Marketplace; configurar MFA Delete no S3.

> [!question]- Funcionários precisam de login único em várias contas AWS e aplicações SaaS usando o diretório corporativo. Qual serviço?
> **AWS IAM Identity Center**, integrado ao provedor de identidade corporativo (SAML 2.0/SCIM).

> [!question]- Um aplicativo mobile precisa de cadastro e login de clientes com Google e Apple. Qual serviço?
> **Amazon Cognito**.

> [!question]- Secrets Manager ou Parameter Store: qual rotaciona automaticamente a senha de um banco RDS?
> **AWS Secrets Manager**. O Parameter Store guarda segredos criptografados, mas não tem rotação automática nativa.

> [!question]- Uma SCP concede permissões às contas-membro?
> **Não**. A SCP define o **máximo** de permissões disponíveis; as permissões efetivas ainda precisam ser concedidas por políticas do IAM. SCPs não afetam a conta de gerenciamento.

> [!question]- Qual serviço configura rapidamente um ambiente multi-conta seguro, com landing zone e guardrails?
> **AWS Control Tower**.

> [!question]- KMS ou CloudHSM: qual oferece um HSM dedicado em que só o cliente controla as chaves?
> **AWS CloudHSM**. O KMS é gerenciado pela AWS em HSMs compartilhados e é a escolha padrão para a maioria dos casos.

> [!question]- Qual serviço provisiona e renova automaticamente certificados SSL/TLS para ELB e CloudFront?
> **AWS Certificate Manager (ACM)**.

> [!question]- Qual serviço usa machine learning para encontrar dados pessoais sensíveis em buckets S3?
> **Amazon Macie**.

> [!question]- Security group ou network ACL: qual é stateless e permite regras de negação?
> **Network ACL**, no nível da sub-rede. O security group é stateful, fica na instância e só tem regras de permissão.

> [!question]- Qual é a diferença entre AWS Shield Standard e Shield Advanced?
> **Standard**: gratuito e automático, contra os ataques DDoS mais comuns (camadas 3/4). **Advanced**: pago, com proteção avançada (inclusive camada 7 com WAF), **Shield Response Team 24/7** e **proteção de custos** durante ataques.

> [!question]- Qual serviço bloqueia SQL injection e cross-site scripting?
> **AWS WAF**.

> [!question]- Qual serviço gerencia regras de WAF, Shield Advanced e security groups de forma centralizada em todas as contas da organização?
> **AWS Firewall Manager**.

> [!question]- GuardDuty, Inspector ou Detective: qual varre instâncias EC2 e imagens de contêiner em busca de vulnerabilidades de software?
> **Amazon Inspector**. GuardDuty detecta ameaças; Detective investiga a causa raiz.

> [!question]- Qual serviço detecta ameaças analisando CloudTrail, VPC Flow Logs e logs de DNS com machine learning?
> **Amazon GuardDuty**.

> [!question]- Qual serviço agrega achados de segurança de vários serviços e verifica conformidade com padrões como CIS e PCI DSS?
> **AWS Security Hub**.

> [!question]- Um auditor pede o relatório SOC 2 da AWS. Onde obtê-lo?
> No **AWS Artifact**, portal self-service e gratuito de relatórios e acordos de conformidade.

> [!question]- Um administrador precisa descobrir quem excluiu um bucket S3 ontem. Qual serviço?
> **AWS CloudTrail**, que registra as chamadas de API com identidade, horário e origem.

> [!question]- Como verificar continuamente se todos os volumes EBS estão criptografados e ver o histórico de configuração?
> **AWS Config** com uma Config rule.

> [!question]- A quem denunciar uma instância AWS que está enviando spam ou atacando o seu site?
> À equipe **AWS Trust & Safety**, pelo formulário de abuso (ou abuse@amazonaws.com).

> [!question]- Onde encontrar produtos de segurança de terceiros prontos para usar na AWS?
> No **AWS Marketplace**.

> [!question]- Qual propriedade da segurança a criptografia garante? E a autenticação de dois fatores?
> **Criptografia → confidencialidade** (só quem tem autorização lê). **MFA/2FA → autenticidade do usuário** (ele é quem diz ser). Integridade = o dado não foi alterado; disponibilidade = continua acessível.

> [!question]- Qual é o objetivo do controle de acesso na nuvem?
> Garantir que **apenas usuários autorizados** tenham acesso às informações e recursos. É o papel do IAM, aplicando menor privilégio.

> [!question]- Qual é a melhor prática para proteger dados **em trânsito**?
> Usar **HTTPS ou SSL/TLS**. Certificados vêm do **ACM**. RDP e FTP não são resposta.

### Computação

> [!question]- Qual família de instâncias EC2 atende a servidores de jogos, processamento em lote e transcodificação de mídia?
> **Otimizada para computação** (família C).

> [!question]- Qual família de instâncias atende a bancos de dados em memória e análises de big data em tempo real?
> **Otimizada para memória** (famílias R e X).

> [!question]- Qual família de instâncias atende a cargas com alto I/O sequencial em armazenamento local, como data warehouses?
> **Otimizada para armazenamento** (famílias I, D e H).

> [!question]- Uma carga de processamento em lote pode ser interrompida e retomada. Qual modelo de compra minimiza o custo?
> **Spot Instances**, com até ~90% de desconto e aviso de interrupção de 2 minutos.

> [!question]- Um banco de dados roda 24/7 e continuará assim por 3 anos. Qual modelo de compra reduz o custo?
> **Reserved Instances ou Savings Plans de 3 anos** (maior desconto com pagamento All Upfront).

> [!question]- Qual é a diferença entre Compute Savings Plans e EC2 Instance Savings Plans?
> **Compute Savings Plans** valem para qualquer família, Região, SO, **Fargate e Lambda** (até ~66%). **EC2 Instance Savings Plans** dão mais desconto (até ~72%), mas ficam presos a uma família em uma Região.

> [!question]- O desconto de uma Reserved Instance comprada em uma conta pode beneficiar outra conta?
> **Sim**, com faturamento consolidado do AWS Organizations: o desconto se aplica automaticamente ao uso correspondente de outras contas da organização (o compartilhamento pode ser desativado).

> [!question]- Dedicated Hosts ou Dedicated Instances: qual oferece visibilidade de sockets e núcleos físicos?
> **Dedicated Hosts**, necessários para BYOL por socket ou núcleo.

> [!question]- Como garantir capacidade EC2 em uma AZ para um evento de duas semanas, sem compromisso de longo prazo?
> **On-Demand Capacity Reservation**. Savings Plans e RIs regionais não reservam capacidade.

> [!question]- Qual recurso da AWS demonstra elasticidade ao adicionar e remover instâncias conforme a demanda?
> **EC2 Auto Scaling**.

> [!question]- Qual é o papel de um load balancer?
> Distribuir o tráfego entre vários destinos em várias AZs, verificar a saúde (health checks) e enviar tráfego só para destinos saudáveis, aumentando disponibilidade e tolerância a falhas.

> [!question]- ALB ou NLB: qual roteia requisições HTTP pelo caminho da URL?
> **Application Load Balancer** (camada 7). O NLB atua na camada 4, com latência ultrabaixa.

> [!question]- ECS, EKS ou Fargate: qual é Kubernetes gerenciado?
> **Amazon EKS**. O ECS é o orquestrador nativo da AWS; o Fargate é o motor serverless que roda contêineres para ECS ou EKS.

> [!question]- Qual é o tempo máximo de execução de uma função Lambda?
> **15 minutos**. Para processos mais longos sem servidor, use Fargate ou AWS Batch.

> [!question]- Um desenvolvedor quer enviar o código de uma aplicação web e deixar a AWS provisionar EC2, balanceador e Auto Scaling. Qual serviço?
> **AWS Elastic Beanstalk** (PaaS, sem custo adicional além dos recursos).

> [!question]- Uma pequena empresa quer um servidor para WordPress com preço mensal fixo e configuração simples. Qual serviço?
> **Amazon Lightsail**.

### Armazenamento

> [!question]- Qual classe do S3 é indicada quando o padrão de acesso é desconhecido ou muda com o tempo?
> **S3 Intelligent-Tiering**, que move os objetos automaticamente entre camadas conforme o acesso, sem taxa de recuperação.

> [!question]- Qual classe do S3 tem o menor custo de armazenamento para retenção de longo prazo com recuperação em até 12 horas?
> **S3 Glacier Deep Archive**.

> [!question]- Dados de arquivo acessados uma vez por trimestre precisam ser recuperados em milissegundos. Qual classe?
> **S3 Glacier Instant Retrieval**.

> [!question]- Quando usar S3 One Zone-IA?
> Para dados acessados com pouca frequência **que podem ser recriados**, porque ficam em uma única AZ.

> [!question]- Para que serve uma política de ciclo de vida (lifecycle) do S3?
> Para **mover objetos para classes mais baratas** conforme a idade e **excluí-los** ao fim da retenção, automaticamente.

> [!question]- Qual recurso do S3 permite recuperar um objeto sobrescrito ou excluído por engano?
> **Versionamento**.

> [!question]- Qual é a diferença entre EBS e instance store?
> **EBS** é bloco persistente conectado pela rede, independente da vida da instância, com snapshots. **Instance store** é bloco temporário no host físico: os dados se perdem ao parar ou encerrar a instância.

> [!question]- Um volume EBS pode ser usado diretamente em outra AZ?
> **Não**. O volume fica em uma AZ; é preciso criar um **snapshot** e restaurá-lo na AZ de destino.

> [!question]- Várias instâncias Linux em AZs diferentes precisam do mesmo sistema de arquivos. Qual serviço?
> **Amazon EFS**.

> [!question]- Qual serviço oferece compartilhamentos de arquivos Windows (SMB) integrados ao Active Directory?
> **Amazon FSx for Windows File Server**.

> [!question]- Servidores on-premises precisam acessar armazenamento na nuvem com cache local de baixa latência. Qual serviço?
> **AWS Storage Gateway**.

> [!question]- Qual tipo de Storage Gateway substitui fitas físicas de backup sem mudar o software de backup?
> **Tape Gateway** (biblioteca de fitas virtual).

> [!question]- Qual serviço centraliza e automatiza backups de EC2, EBS, RDS, DynamoDB, EFS e S3 com políticas?
> **AWS Backup**.

### Banco de Dados

> [!question]- Quando faz sentido hospedar o banco em EC2 em vez de usar o RDS?
> Quando é preciso **acesso ao SO**, um **engine ou versão não suportado** pelo serviço gerenciado ou configurações muito específicas. O custo é assumir patches, backups e alta disponibilidade.

> [!question]- RDS Multi-AZ serve para escalar leituras?
> **Não**. Multi-AZ mantém um standby síncrono para **alta disponibilidade e failover automático**. Para escalar leituras, use **Read Replicas**.

> [!question]- Quais engines relacionais o Amazon Aurora é compatível?
> **MySQL e PostgreSQL**.

> [!question]- Qual banco NoSQL serverless oferece latência de milissegundos de um dígito em qualquer escala?
> **Amazon DynamoDB**.

> [!question]- Qual serviço reduz a carga do banco guardando resultados de consultas frequentes em memória?
> **Amazon ElastiCache** (Valkey, Redis OSS ou Memcached).

> [!question]- Qual serviço é um data warehouse para análises e BI em escala de petabytes?
> **Amazon Redshift**.

> [!question]- Uma aplicação de detecção de fraude precisa analisar relações entre contas, dispositivos e transações. Qual banco?
> **Amazon Neptune** (banco de grafos).

> [!question]- Qual banco é compatível com MongoDB?
> **Amazon DocumentDB**.

> [!question]- Uma migração de Oracle para Aurora PostgreSQL precisa de quais serviços?
> **AWS SCT** (ou DMS Schema Conversion) para converter o esquema e o código, e **AWS DMS** para migrar os dados.

> [!question]- O banco de origem precisa continuar em uso durante a migração. Qual serviço?
> **AWS DMS**, com replicação contínua (CDC) até a virada.

> [!question]- Multi-AZ, Read Replica ou Read Replica em outra Região: qual resolve HA, qual escala leitura e qual é DR contra a perda de uma Região?
> **Multi-AZ** = alta disponibilidade com failover dentro da Região. **Read Replica** = escalar leituras. **Read Replica em outra Região** = **DR regional** (promovida a primária no desastre). Multi-AZ e Multi-AZ DB Cluster ficam na **mesma Região**, então não servem de DR regional.

### Redes

> [!question]- O que torna uma sub-rede pública?
> A tabela de rotas da sub-rede ter uma rota para um **Internet Gateway**.

> [!question]- Instâncias em uma sub-rede privada precisam baixar atualizações da internet sem receber conexões de entrada. O que usar?
> Um **NAT Gateway** em uma sub-rede pública.

> [!question]- Como acessar o S3 a partir de uma VPC sem passar pela internet?
> Com um **gateway VPC endpoint** (sem custo) para o S3.

> [!question]- VPC Peering ou Transit Gateway para conectar 50 VPCs e a rede on-premises?
> **AWS Transit Gateway**, que funciona como hub central. VPC Peering é um a um e não é transitivo.

> [!question]- Qual é a diferença entre Site-to-Site VPN e Direct Connect?
> **Site-to-Site VPN**: túnel IPsec criptografado pela internet, rápido e barato de configurar. **Direct Connect**: conexão física privada e dedicada, com banda consistente, que não passa pela internet e leva semanas para provisionar.

> [!question]- Funcionários remotos precisam acessar recursos privados na VPC a partir dos notebooks. Qual serviço?
> **AWS Client VPN**.

> [!question]- Qual serviço oferece DNS, registro de domínios e health checks?
> **Amazon Route 53**.

> [!question]- Qual política de roteamento do Route 53 envia o usuário para a Região com menor latência?
> **Latency-based routing**.

> [!question]- Qual política de roteamento do Route 53 serve conteúdo diferente conforme o país do usuário?
> **Geolocation routing**.

> [!question]- CloudFront ou Global Accelerator: qual faz cache de conteúdo nas edge locations?
> **Amazon CloudFront**. O Global Accelerator usa a rede global da AWS e IPs estáticos, sem cache.

> [!question]- Qual serviço cria e publica APIs REST que acionam funções Lambda?
> **Amazon API Gateway**.

> [!question]- Quais serviços ficam **dentro** de uma VPC e quais ficam fora?
> **Dentro**: EC2, RDS/Aurora, **EFS**, ElastiCache, Redshift, ELB, NAT Gateway. **Fora**: S3, DynamoDB, Cognito, SQS, SNS, IAM, Route 53 — acessados pela internet ou por **VPC endpoint**. Lambda fica fora por padrão, mas pode ser anexada a uma VPC.

### Analytics e IA

> [!question]- Qual serviço consulta dados no S3 com SQL sem gerenciar servidores?
> **Amazon Athena**.

> [!question]- Qual serviço faz ETL serverless e mantém um catálogo de metadados do data lake?
> **AWS Glue** (com o Glue Data Catalog).

> [!question]- Qual serviço coleta e processa dados em streaming em tempo real, como cliques e telemetria?
> **Amazon Kinesis**.

> [!question]- Qual serviço cria dashboards de BI interativos?
> **Amazon Quick Sight**.

> [!question]- Qual serviço processa big data com Apache Spark e Hadoop em clusters gerenciados?
> **Amazon EMR**.

> [!question]- Qual serviço identifica rostos e objetos em imagens e vídeos?
> **Amazon Rekognition**.

> [!question]- Qual serviço extrai texto, formulários e tabelas de documentos digitalizados?
> **Amazon Textract**.

> [!question]- Qual serviço analisa o sentimento de avaliações de clientes?
> **Amazon Comprehend**.

> [!question]- Transcribe ou Polly: qual converte texto em fala?
> **Amazon Polly**. O Transcribe converte fala em texto.

> [!question]- Qual serviço cria chatbots de voz e texto?
> **Amazon Lex**.

> [!question]- Qual serviço permite construir, treinar e implantar modelos de ML personalizados?
> **Amazon SageMaker AI**.

> [!question]- Qual serviço é um assistente de IA generativa que responde perguntas com base nos dados da empresa?
> **Amazon Q Business**. Para código, **Amazon Q Developer**.

> [!question]- Qual serviço permite fazer perguntas em linguagem natural e receber gráficos e visualizações?
> **Amazon QuickSight Q**. O Quick Sight comum faz os dashboards; o **Q** acrescenta a camada de NLP. Kendra (busca corporativa), Comprehend (NLP em texto) e Bedrock (modelos de fundação) são os distratores.

> [!question]- Onde comprar ou assinar conjuntos de dados de terceiros para enriquecer suas análises?
> **AWS Data Exchange**. O Marketplace vende **software**; Redshift, Athena e DynamoDB apenas armazenam ou consultam dados — não os fornecem.

> [!question]- Athena ou S3 Select para ler vários arquivos .csv de um bucket e gerar um relatório resumido?
> **Athena**: SQL padrão sobre **vários objetos**. O **S3 Select** só filtra dentro de **um único objeto**, com SQL limitado.

### Integração e demais categorias

> [!question]- Qual serviço desacopla componentes de uma aplicação usando filas?
> **Amazon SQS**.

> [!question]- Qual serviço envia notificações por e-mail, SMS e push para vários assinantes ao mesmo tempo?
> **Amazon SNS**.

> [!question]- Qual serviço roteia eventos de serviços AWS e aplicações SaaS para destinos com base em regras?
> **Amazon EventBridge**.

> [!question]- Qual serviço orquestra um fluxo de trabalho com várias etapas, desvios e novas tentativas?
> **AWS Step Functions**.

> [!question]- Uma empresa quer um contact center na nuvem com pagamento por uso. Qual serviço?
> **Amazon Connect**.

> [!question]- Qual serviço envia e-mails transacionais e de marketing em massa?
> **Amazon SES**.

> [!question]- WorkSpaces ou AppStream 2.0: qual entrega um desktop virtual completo e persistente?
> **Amazon WorkSpaces**. O AppStream 2.0 transmite aplicações individuais.

> [!question]- Qual serviço cria, implanta e hospeda aplicações web e mobile full-stack?
> **AWS Amplify**.

> [!question]- Qual serviço conecta e gerencia bilhões de dispositivos IoT?
> **AWS IoT Core**.

> [!question]- Qual serviço compila código e executa testes sem servidores de build?
> **AWS CodeBuild**.

> [!question]- Qual serviço orquestra o pipeline de CI/CD?
> **AWS CodePipeline**.

> [!question]- Qual serviço rastreia requisições entre microsserviços para encontrar gargalos?
> **AWS X-Ray**.

> [!question]- Qual serviço é um IDE na nuvem para a equipe escrever e depurar código pelo navegador?
> **AWS Cloud9**. Não confunda com **CloudShell** (terminal com a CLI, não IDE) nem com **CodeBuild** (compila e testa).

> [!question]- Qual serviço permite projetar visualmente uma aplicação serverless? E qual criava um projeto com pipeline CI/CD pronto?
> **AWS Application Composer** (hoje Infrastructure Composer) para desenhar a aplicação serverless; **AWS CodeStar** para o projeto com pipeline pronto — descontinuado em jul/2024, mas ainda usado como resposta em simulados.

### Gerenciamento e Governança

> [!question]- Console ou CloudFormation para criar o mesmo ambiente em cinco contas de forma consistente?
> **CloudFormation** (infraestrutura como código). O console serve para tarefas pontuais.

> [!question]- Qual serviço aplica patches e executa comandos em uma frota de instâncias EC2 e servidores on-premises?
> **AWS Systems Manager** (Patch Manager e Run Command).

> [!question]- Qual serviço permite acesso ao shell de uma instância sem abrir a porta SSH nem usar bastion host?
> **Systems Manager Session Manager**.

> [!question]- Usuários só podem provisionar configurações de recursos aprovadas pela TI. Qual serviço?
> **AWS Service Catalog**.

> [!question]- Quais são as seis categorias do AWS Trusted Advisor?
> Otimização de custos, desempenho, segurança, tolerância a falhas, limites de serviço e excelência operacional.

> [!question]- Qual plano de suporte libera todas as verificações do Trusted Advisor?
> **Business Support+** ou superior (Enterprise e Unified Operations). O Basic tem só as verificações principais.

> [!question]- Qual é a diferença entre o AWS Health Dashboard e o Amazon CloudWatch?
> O **Health Dashboard** mostra eventos **do lado da AWS** que afetam os seus recursos (manutenções, incidentes). O **CloudWatch** monitora métricas e logs **dos seus recursos e aplicações**.

> [!question]- Qual serviço dá recomendações de rightsizing com machine learning para EC2, EBS e Lambda?
> **AWS Compute Optimizer**.

> [!question]- Como solicitar aumento do limite de instâncias EC2 em uma Região?
> Pelo **Service Quotas** (ou abrindo um caso no Support Center).

### Faturamento, Preços e Suporte

> [!question]- Qual ferramenta estima o custo de uma arquitetura antes de ela ser implantada?
> **AWS Pricing Calculator**.

> [!question]- Qual ferramenta mostra quais serviços mais custaram nos últimos seis meses e prevê o gasto futuro?
> **AWS Cost Explorer**.

> [!question]- Qual ferramenta envia alerta quando o gasto previsto do mês vai ultrapassar US$ 500?
> **AWS Budgets**.

> [!question]- Qual é o relatório de faturamento mais detalhado da AWS e onde ele é entregue?
> O **AWS Cost and Usage Report (CUR)**, entregue em um bucket **S3** e analisável com Athena ou Quick Sight.

> [!question]- O que é preciso fazer para uma tag aparecer como dimensão de custo no Cost Explorer?
> **Ativá-la como tag de alocação de custos** no console de Billing (na conta de gerenciamento, se houver Organizations). Ela só vale a partir da ativação.

> [!question]- Quais são os dois tipos de tags de alocação de custos?
> **Geradas pela AWS** (prefixo `aws:`) e **definidas pelo usuário** (prefixo `user:`).

> [!question]- Quais são os benefícios do faturamento consolidado?
> Uma fatura única, visão do custo por conta, uso agregado para descontos por volume e compartilhamento de descontos de RI e Savings Plans. Sem custo adicional.

> [!question]- A transferência de dados da internet para a AWS é cobrada?
> **Não**. A entrada é gratuita; a saída para a internet é cobrada por GB.

> [!question]- A transferência de dados entre AZs da mesma Região é gratuita?
> **Não**. É cobrada por GB. É gratuita dentro da mesma AZ usando IPs privados.

> [!question]- Como funciona o Free Tier para contas criadas a partir de 15/jul/2025?
> US$ 100 em créditos no cadastro e até US$ 100 a mais com atividades; plano gratuito por até 6 meses (ou até acabar os créditos) ou plano pago. Os serviços "sempre gratuitos" continuam com cotas mensais.

> [!question]- Qual plano de suporte é gratuito e o que ele inclui?
> **Basic**: atendimento 24/7 para conta e faturamento, documentação, whitepapers, re:Post, Health Dashboard e verificações principais do Trusted Advisor. Não inclui casos técnicos.

> [!question]- Qual plano é o mínimo recomendado para cargas em produção, com acesso 24/7 a engenheiros?
> **Business Support+** (a partir de US$ 29/mês por conta), que substitui os planos Developer e Business.

> [!question]- Qual plano oferece um Technical Account Manager (TAM) designado e resposta em 15 minutos para sistemas críticos?
> **Enterprise Support**. O **Unified Operations** também tem TAM e responde em 5 minutos a incidentes críticos.

> [!question]- Onde encontrar estratégias, guias e padrões testados para migração e modernização?
> **AWS Prescriptive Guidance**.

> [!question]- Qual é a diferença entre AWS Knowledge Center e AWS re:Post?
> O **Knowledge Center** reúne respostas às perguntas mais frequentes do suporte. O **re:Post** é a comunidade de perguntas e respostas moderada pela AWS.

> [!question]- Qual é a diferença entre um integrador de sistemas (SI) e um ISV na AWS Partner Network?
> O **SI** presta serviços de consultoria, migração e gestão. O **ISV** desenvolve e vende software que roda ou se integra à AWS.

> [!question]- Cite três benefícios de ser parceiro AWS.
> Treinamento e certificação para parceiros, eventos de parceiros e descontos por volume para parceiros (além de apoio de marketing e visibilidade).

> [!question]- Quais funções de gestão o AWS Marketplace oferece além da compra de software?
> **Gestão de custos** (cobrança na fatura AWS), **governança** (Private Marketplace com catálogo aprovado) e **gestão de direitos de uso** (entitlement) das licenças.

> [!question]- Uma empresa precisa de consultores da própria AWS para planejar uma migração grande. Qual opção?
> **AWS Professional Services**.

> [!question]- Como a AWS cobra pelo EC2, pelo RDS e pelo S3?
> **EC2**: por **hora ou segundo de instância em execução** (instância parada não é cobrada, mas o volume EBS anexado é). **RDS**: por **hora de banco em execução**. **S3**: por **GB armazenado por mês**. E o preço geral da AWS é calculado **pelo uso dos serviços e recursos consumidos** — não pelo número de contas, usuários ou instâncias criadas.

> [!question]- Cite quatro serviços da AWS que são sempre gratuitos.
> **IAM**, **AWS Organizations** (e o faturamento consolidado), **CloudFormation** e **Auto Scaling** — também VPC, Elastic Beanstalk, AWS Artifact, Well-Architected Tool e Shield Standard. Você paga apenas os recursos que eles criam. Cuidado: **S3, ELB e WAF são cobrados**.

> [!question]- Qual plano de suporte oferece um agente **Concierge**?
> **Enterprise Support**. O Concierge Support Team ajuda com faturamento e gestão de várias contas vinculadas. Basic, Developer e Business não têm.

> [!question]- Traduza os nomes antigos dos planos de suporte para os atuais.
> **Business → Business Support+**; **Enterprise → Enterprise Support**; **Enterprise On-Ramp → migrado para Enterprise**; **Developer → encerrado sem equivalente**; **Basic** não mudou; **Unified Operations** é novo. Os simulados usam quase sempre os nomes antigos.

> [!question]- Em faturamento consolidado, a conta X tem 7 RIs e 5 instâncias, a Y tem 2 e a Z tem 4. Quantas são cobradas como RI?
> **7 como RI e 4 regulares.** As RIs cobrem primeiro a conta que comprou (5 em X), as 2 que sobram cobrem instâncias de outras contas (as 2 de Y) e o restante vira On-Demand (as 4 de Z).

> [!question]- Onde aprender com exemplos de outros clientes e perguntar diretamente a especialistas da AWS?
> **AWS Online Tech Talks** (apresentações ao vivo e gravadas). Documentação = referência técnica; **Knowledge Center** = FAQ do suporte; **re:Post** = comunidade.

> [!question]- Quais são dois benefícios do AWS Marketplace cobrados na prova?
> **Velocidade nos negócios** (soluções prontas, implantação em minutos) e **menos objeções legais** (licenças e termos **padronizados**, o que encurta a revisão jurídica). Também: cobrança na própria fatura da AWS.

### Pegadinhas Duplas (confusões mais recorrentes)

> [!question]- CloudTrail, CloudWatch ou Config: qual responde "a CPU passou de 90%", "quem desligou a instância" e "o security group estava aberto ontem"?
> CPU passou de 90% → **CloudWatch**. Quem desligou a instância → **CloudTrail**. Configuração do security group ontem → **Config**.

> [!question]- Cost Explorer, Budgets ou Pricing Calculator: qual responde "quanto gastei", "me avise se passar" e "quanto vai custar"?
> Quanto gastei → **Cost Explorer**. Me avise se passar → **Budgets**. Quanto vai custar → **Pricing Calculator**.

> [!question]- SQS, SNS ou SES: qual responde "fila para processar pedidos", "alerta para a equipe" e "newsletter para clientes"?
> Fila → **SQS**. Alerta → **SNS**. Newsletter → **SES**.

> [!question]- Artifact, Trusted Advisor ou Security Hub: qual responde "relatório PCI da AWS", "security group com porta aberta" e "achados de várias ferramentas em um painel"?
> Relatório PCI → **Artifact**. Porta aberta → **Trusted Advisor** (ou Security Hub). Painel de achados → **Security Hub**.

> [!question]- Várias AZs ou várias Regiões: qual responde "falha de um data center" e "desastre que derruba uma Região"?
> Falha de um data center → **várias AZs**. Desastre regional → **várias Regiões**.

---

## 15. Mapa de cobertura do guia oficial e questões de múltipla resposta

O [guia oficial do CLF-C02](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) divide a prova em **19 tarefas**. A tabela localiza a revisão de cada tarefa neste material. Cobrir as tarefas publicadas **não garante** conhecer todas as questões: o guia não é uma lista exaustiva, e a [lista de serviços no escopo](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html) também declara que está sujeita a alterações.

| Tarefa oficial | Decisões e conceitos a dominar | Onde revisar |
|---|---|---|
| **1.1 Benefícios da nuvem AWS** | Proposta de valor, infraestrutura global, alta disponibilidade, elasticidade, agilidade | Seções 1 e 2 |
| **1.2 Princípios de projeto** | Seis pilares do Well-Architected e diferenças entre eles; **princípios gerais de design**; acoplamento fraco, stateless, descartável, paralelismo, redundância vs. elasticidade | Seção 1 |
| **1.3 Migração para a nuvem** | AWS CAF (perspectivas **e capacidades**), estratégias de migração, replicação de banco, recursos de migração, Snowball Edge, AMS | Seções 1 e 6 |
| **1.4 Economia da nuvem** | Fixo vs. variável, custos on-premises, BYOL, rightsizing, automação, economias de escala | Seção 1 |
| **2.1 Responsabilidade compartilhada** | O que é da AWS, do cliente e compartilhado; mudança por serviço (EC2, RDS, Lambda) | Seção 3 |
| **2.2 Segurança, governança e conformidade** | Artifact, conformidade por região e setor, Inspector, Security Hub, GuardDuty, Shield, criptografia, CloudWatch, CloudTrail, Config, relatórios de acesso | Seções 3 e 10 |
| **2.3 Gestão de acesso** | IAM, root, menor privilégio, Identity Center, access keys, senhas, Secrets Manager, MFA, cross-account roles, federação | Seção 3 |
| **2.4 Componentes e recursos de segurança** | WAF, Firewall Manager, Shield, GuardDuty, Marketplace, Knowledge Center, Security Center, Security Blog, Trusted Advisor | Seções 3 e 10 |
| **3.1 Implantar e operar** | Console, API, SDK, CLI, IaC; operação única vs. repetível; nuvem, híbrido e on-premises | Seções 1 e 10 |
| **3.2 Infraestrutura global** | Regiões, AZs, edge locations, alta disponibilidade, várias Regiões | Seção 2 |
| **3.3 Computação** | Tipos de instância, ECS/EKS, Fargate/Lambda, Auto Scaling, load balancers | Seção 4 |
| **3.4 Banco de dados** | EC2 vs. gerenciado, RDS, Aurora, DynamoDB, ElastiCache, DMS, SCT | Seção 6 |
| **3.5 Rede** | Componentes e segurança da VPC, Route 53, VPN, Direct Connect | Seção 7 |
| **3.6 Armazenamento** | Objeto, classes do S3, EBS, instance store, EFS, FSx, Storage Gateway, lifecycle, AWS Backup | Seção 5 |
| **3.7 IA/ML e analytics** | SageMaker AI, Lex e serviços de IA; Athena, Kinesis, Glue, Quick Sight, **QuickSight Q**, **Data Exchange** | Seção 8 |
| **3.8 Outras categorias** | EventBridge, SNS, SQS, Connect, SES, AWS Support, CodeBuild, CodePipeline, X-Ray, AppStream 2.0, WorkSpaces, Secure Browser, Amplify, IoT Core, **Cloud9**, **Application Composer**, **CodeStar**, **CodeCommit** | Seções 9 e 11 |
| **4.1 Modelos de preço** | Opções de compra de computação, flexibilidade de RI, RI em Organizations, transferência de dados, preços de armazenamento | Seções 4 e 11 |
| **4.2 Faturamento, orçamento e custos** | Budgets, Cost Explorer, Pricing Calculator, faturamento consolidado, tags de alocação, CUR | Seção 11 |
| **4.3 Recursos técnicos e suporte** | Documentação, Prescriptive Guidance, Knowledge Center, re:Post, **Online Tech Talks**, planos de suporte (**nomes antigos e novos**, Concierge), Trusted Advisor, Health, Trust & Safety, parceiros, **Partner Solutions Finder**, Marketplace **e seus benefícios**, Professional Services, **AMS** | Seções 3, 10 e 11 |

### Como resolver múltipla resposta

O exame inclui questões de **múltiplas respostas**, com duas ou mais opções corretas entre cinco ou mais alternativas. Não há crédito parcial: é preciso marcar **todas** as corretas. Nas questões abaixo, marque a **quantidade pedida no enunciado** antes de abrir a solução e avalie cada alternativa isoladamente.

> [!question]- 1. Quais são responsabilidades do cliente no modelo de responsabilidade compartilhada? Escolha DUAS: (A) segurança física dos data centers; (B) configurar security groups; (C) aplicar patches no hipervisor; (D) gerenciar usuários e permissões do IAM; (E) manter o hardware de rede global.
> **B e D.** Configuração de rede do cliente e gestão de identidade são segurança **na** nuvem. A, C e E são responsabilidades da AWS. Revise a seção 3.

> [!question]- 2. Quais são boas práticas para proteger o usuário root? Escolha DUAS: (A) habilitar MFA; (B) usar o root nas tarefas diárias de administração; (C) não criar access keys para o root; (D) compartilhar a senha do root com a equipe de operações; (E) anexar a política AdministratorAccess ao root.
> **A e C.** O root deve ter MFA e nenhuma access key, e ser usado só para tarefas exclusivas. B e D aumentam o risco; E não faz sentido, porque políticas do IAM não se aplicam ao root da própria conta. Revise a seção 3.

> [!question]- 3. Quais são vantagens da computação em nuvem? Escolha DUAS: (A) trocar despesa variável por despesa fixa; (B) parar de adivinhar a capacidade; (C) aumentar a velocidade e a agilidade; (D) eliminar toda a responsabilidade de segurança do cliente; (E) exigir contratos de longo prazo para todos os serviços.
> **B e C.** A inverte a vantagem (é trocar fixa por variável). D é falso pela responsabilidade compartilhada. E contradiz o pay-as-you-go. Revise a seção 1.

> [!question]- 4. Uma empresa quer alta disponibilidade para uma aplicação web em EC2. Escolha DUAS ações: (A) distribuir as instâncias em várias Availability Zones; (B) usar um Elastic Load Balancer com health checks; (C) usar uma única instância maior; (D) armazenar o estado apenas no instance store; (E) usar várias edge locations para rodar as instâncias.
> **A e B.** Várias AZs removem o ponto único de falha e o ELB envia tráfego só para instâncias saudáveis. C mantém um ponto único de falha, D perde dados, E não é onde instâncias EC2 rodam. Revise as seções 2 e 4.

> [!question]- 5. Quais serviços ajudam a auditar e manter a conformidade de uma conta? Escolha DUAS: (A) AWS CloudTrail; (B) Amazon Polly; (C) AWS Config; (D) Amazon Lightsail; (E) AWS Amplify.
> **A e C.** CloudTrail registra as ações; Config registra configurações e avalia regras. Os outros são serviços de fala, computação simples e frontend. Revise a seção 3.

> [!question]- 6. Uma empresa quer controlar gastos em várias contas. Escolha DUAS ações: (A) ativar tags de alocação de custos e padronizar seu uso; (B) configurar AWS Budgets com alertas; (C) usar o AWS Artifact para acompanhar custos; (D) usar o Amazon Inspector para prever gastos; (E) desativar o faturamento consolidado.
> **A e B.** Tags atribuem gastos por projeto e Budgets alerta antes de estourar. Artifact é conformidade, Inspector é vulnerabilidade, e desativar o faturamento consolidado perde descontos. Revise a seção 11.

> [!question]- 7. Quais são serviços de banco de dados gerenciados que reduzem o esforço operacional em relação a um banco em EC2? Escolha DUAS: (A) Amazon RDS; (B) Amazon EBS; (C) Amazon DynamoDB; (D) AWS Storage Gateway; (E) Amazon EFS.
> **A e C.** RDS e DynamoDB são bancos gerenciados. EBS, Storage Gateway e EFS são serviços de armazenamento. Revise a seção 6.

> [!question]- 8. Quais serviços protegem aplicações web contra ataques? Escolha DUAS: (A) AWS WAF; (B) AWS Shield; (C) Amazon Macie; (D) AWS Artifact; (E) Amazon Quick Sight.
> **A e B.** WAF filtra requisições maliciosas e Shield protege contra DDoS. Macie descobre dados sensíveis, Artifact entrega relatórios e Quick Sight é BI. Revise a seção 3.

> [!question]- 9. Uma carga de trabalho tem uma base estável 24/7 e picos de processamento em lote que podem ser interrompidos. Escolha DUAS opções para reduzir o custo: (A) Savings Plans ou Reserved Instances para a base; (B) Spot Instances para os picos; (C) Dedicated Hosts para toda a carga; (D) On-Demand para a base estável de 3 anos; (E) Capacity Reservations como forma de desconto.
> **A e B.** Compromisso para a base previsível e Spot para o que tolera interrupção. C é caro sem requisito de licença; D desperdiça o desconto; E reserva capacidade, mas não dá desconto sozinha. Revise a seção 4.

> [!question]- 10. Quais recursos oferecem ajuda técnica da própria AWS ou de sua comunidade? Escolha TRÊS: (A) AWS re:Post; (B) AWS Knowledge Center; (C) AWS Prescriptive Guidance; (D) AWS Artifact; (E) AWS Trust & Safety; (F) AWS Cost Explorer.
> **A, B e C.** re:Post é a comunidade, Knowledge Center responde perguntas frequentes e Prescriptive Guidance traz estratégias e padrões. Artifact entrega relatórios de conformidade, Trust & Safety recebe denúncias de abuso e Cost Explorer analisa custos. Revise a seção 11.

> [!question]- 11. Uma empresa precisa conectar o data center à AWS. Escolha DUAS afirmações corretas: (A) Site-to-Site VPN usa um túnel IPsec criptografado pela internet; (B) Direct Connect é uma conexão privada dedicada que não passa pela internet; (C) Direct Connect é criptografado por padrão; (D) VPN oferece desempenho sempre mais consistente que Direct Connect; (E) Direct Connect fica pronto em minutos.
> **A e B.** C é falso (combine com VPN ou MACsec), D inverte a comparação e E é falso (leva semanas). Revise a seção 7.

> [!question]- 12. Quais são tarefas que exigem o usuário root? Escolha DUAS: (A) fechar uma conta AWS avulsa; (B) criar um bucket S3; (C) restaurar permissões quando o único administrador do IAM perdeu o acesso; (D) lançar uma instância EC2; (E) criar um usuário do IAM.
> **A e C.** Criar buckets, instâncias e usuários pode ser feito por identidades do IAM com as permissões corretas. Revise a seção 3.
