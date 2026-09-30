# AWS Well-Architected Framework — Guia de revisão

Guia de estudo · Atualizado em setembro de 2026

Baseado no treinamento AWS Well-Architected — princípios de design, pilares e práticas recomendadas para arquitetar na nuvem.

**Erik Nathan** · [eriknathan.me](https://eriknathan.me/)

**Seis pilares do framework:** Excelência operacional; Segurança; Confiabilidade; Eficiência de desempenho; Otimização de custos; Sustentabilidade.

## Sumário

1. [Módulo 1 — Visão geral do AWS Well-Architected Framework](#modulo-1)
2. [Módulo 2 — Como executar uma análise do Well-Architected Framework](#modulo-2)
3. [Módulo 3 — Análise detalhada da ferramenta do AWS Well-Architected](#modulo-3)
4. [Módulo 4 — Análise detalhada do pilar de excelência operacional](#modulo-4)
5. [Módulo 5 — Análise detalhada do pilar de segurança](#modulo-5)
6. [Módulo 6 — Análise detalhada do pilar de confiabilidade](#modulo-6)
7. [Módulo 7 — Análise detalhada do pilar de eficiência de desempenho](#modulo-7)
8. [Módulo 8 — Análise detalhada do pilar de otimização de custos](#modulo-8)
9. [Módulo 9 — Análise detalhada do pilar de sustentabilidade](#modulo-9)
10. [Módulo 10 — Questionário](#modulo-10)
11. [Resumo final](#resumo-final)

<a id="modulo-1"></a>

## Módulo 1 — Visão geral do AWS Well-Architected Framework

### 1.1 Boas-vindas!

Boas-vindas ao módulo um do AWS Well-Architected - Análise do AWS Well-Architected Framework. Neste módulo, você aprenderá sobre o Well-Architected Framework e sua definição, pilares, histórico e propostas de valor.

### 1.2 Objetivos de aprendizado

Neste módulo, você aprenderá sobre o AWS Well-Architected Framework, os componentes do Well-Architected Framework e os pilares e princípios de design do Well-Architected Framework.

Neste módulo, você:

- Terá uma visão geral do AWS Well-Architected (AWS WA) Framework
- Aprenderá sobre os componentes do framework
- Conhecerá os pilares e os princípios gerais de design do framework

### 1.3 O que é o Well-Architected Framework?

Para começar, você aprenderá informações gerais sobre o framework, seus benefícios e seu histórico.

### 1.4 Você tem uma boa arquitetura?

Ao analisar as cargas de trabalho que sua equipe está criando, você consegue responder à pergunta: **"Você tem uma boa arquitetura?"**

Ao analisar as cargas de trabalho que sua equipe está criando, qual é o seu grau de confiança de que seus sistemas foram criados seguindo as práticas recomendadas para a nuvem?

> O framework é um conjunto de princípios de design e práticas recomendadas que ajudam você a entender as decisões tomadas ao criar sistemas na AWS. Ele fornece uma maneira de medir sua arquitetura em relação às práticas recomendadas da AWS e identificar como abordar deficiências.

### 1.5 O que é o Well-Architected Framework?

Os arquitetos de soluções da AWS têm anos de experiência em uma ampla variedade de verticais de negócios e casos de uso. Os arquitetos de soluções ajudaram a projetar e revisar milhares de arquiteturas de clientes na AWS. Com essa experiência, identificamos as práticas recomendadas e as principais estratégias para a arquitetura de sistemas na nuvem.

O uso do framework pode ajudar você a aprender as práticas recomendadas de arquitetura para projetar e operar cargas de trabalho seguras, confiáveis, eficientes, econômicas e sustentáveis na nuvem AWS. Ele oferece uma maneira de aprender de forma consistente as práticas recomendadas, avaliar suas arquiteturas em relação a essas práticas recomendadas e identificar áreas de melhoria. A repetição periódica desse processo cria um ciclo de vida de melhoria contínua. Ao prosseguir com este treinamento, você aprenderá mais sobre esses princípios de design e práticas recomendadas e como integrá-los à sua carga de trabalho.

> Ao usar o framework, você aprenderá as práticas recomendadas de arquitetura para projetar e operar sistemas de forma segura, confiável, eficiente e econômica, e sustentável na nuvem.

O framework é aplicado como um ciclo de melhoria contínua, composto por três etapas que se repetem para cada carga de trabalho:

1. **Aprender:** as práticas recomendadas de arquitetura
2. **Medir:** sua carga de trabalho em relação a essas práticas
3. **Aprimorar:** sua carga de trabalho com base no que foi medido

Esse ciclo se repete e se estende também a outras cargas de trabalho, criando um processo contínuo de melhoria arquitetural.

### 1.6 Por que usar o Well-Architected Framework?

Há muitos motivos para aplicar o Well-Architected Framework. Primeiro, o uso do framework pode ajudar você a criar e implantar com mais rapidez. E isso é possível reduzindo as ações não planejadas, aumentando o gerenciamento da capacidade e usando a automação, o que permitirá que você faça experiências e libere valor com mais frequência. Também é possível reduzir ou mitigar os riscos. Se você entender onde há riscos em sua arquitetura, poderá resolvê-los antes que afetem seus negócios e distraiam sua equipe. Quanto mais informações você tiver, melhores serão suas decisões. Ao garantir a tomada de decisões ativas de arquitetura, você pode controlar o impacto sobre os resultados dos negócios. Você pode tomar decisões informadas sobre o futuro de sua arquitetura com base na sua situação atual. E, por fim, você aprenderá as práticas recomendadas que a AWS desenvolveu ao analisar as arquiteturas de milhares de clientes.

Principais motivos para usar o framework:

- **Crie e implante com mais rapidez.**
- **Diminua ou mitigue os riscos.**
- **Tome decisões informadas.**
- **Conheça as práticas recomendadas da AWS.**

### 1.7 Um breve histórico do Well-Architected Framework

Antes de nos aprofundarmos nos componentes do framework, vamos dar uma olhada em como ele começou e como evoluiu ao longo do tempo. Na nuvem, as restrições do ambiente tradicional foram removidas — o framework nasceu para orientar essa nova forma de arquitetar.

- **2012:** O AWS Well-Architected iniciou.
- **2013:** Os arquitetos de soluções da AWS começaram a analisar as cargas de trabalho dos clientes.
- **2014:** A AWS padronizou as perguntas em quatro pilares.
- **2015:** A AWS publicou um framework formal baseado nos quatro pilares.
- **2016:** Foi acrescentado o pilar de excelência operacional ao Well-Architected Framework.
- **2017:** Para expandir para mais clientes, a AWS treinou os parceiros da AWS selecionados para analisar as cargas de trabalho dos clientes.
- **2018:** A ferramenta do AWS Well-Architected foi lançada no console AWS, disponibilizando-a para todos os clientes.
- **2019:** A AWS lançou a ferramenta do AWS Well-Architected e o Programa de Parceiros do Well-Architected em várias Regiões.
- **2020:** A AWS atualizou o framework, acrescentou mais lentes e lançou o acesso à API para a ferramenta do AWS Well-Architected.
- **2021:** O framework adicionou o pilar de sustentabilidade e mais lentes.
- **2022:** A ferramenta do AWS Well-Architected foi lançada nas Regiões do AWS GovCloud e integrada com o AWS Trusted Advisor.
- **2023:** O Well-Architected continua a adicionar mais recursos, lentes e integrações com outros serviços da AWS.

### 1.8 Componentes do Well-Architected Framework

Agora você aprenderá sobre os três componentes do framework.

### 1.9 Componentes do Well-Architected Framework

O Well-Architected Framework é composto de conteúdo, ferramenta e dados. O framework inclui conteúdo que pode usar para aprender as diretrizes da AWS, como pilares, princípios de design e práticas recomendadas. O framework também inclui a ferramenta do AWS Well-Architected, que você pode usar para medir sua carga de trabalho e suas equipes em relação a essas práticas recomendadas. Outro componente do framework são os dados que você adquire durante a análise do Well-Architected Framework de suas cargas de trabalho. Você pode usar esses dados para melhoria de suas cargas de trabalho e operações. Neste módulo, você se aprofundará no conteúdo. Você vai saber mais sobre a ferramenta do AWS Well-Architected e sobre a análise do Well-Architected Framework em módulos futuros.

Os três componentes do framework se sobrepõem e se relacionam entre si:

- **Conteúdo**
  - Framework: pilares (áreas), princípios de design, perguntas, práticas recomendadas
  - Whitepapers (PDF, Kindle) do treinamento, site
  - Recursos úteis, resumos de conteúdo, glossário interativo
- **Ferramenta**
  - Cargas de trabalho, revisão (perguntas e respostas), painel relatório (PDF)
  - Abordagem da revisão: autoatendimento, parceiro, conduzido pela AWS
  - Recursos de parceiros: APN, Marketplace
- **Dados**
  - Documentar cargas de trabalho: descrição, regiões, prioridade do pilar
  - Análise: classificação, respostas, observações, marcos
  - Planos de melhoria

### 1.10 Conteúdo do Well-Architected Framework

O Well-Architected Framework é um conjunto de perguntas e princípios de design em seis pilares. Junto com os pilares do framework estão as lentes, que fornecem orientação com foco em domínios específicos do setor ou da tecnologia.

Para avaliar a integridade de suas cargas de trabalho, você responde a um conjunto de perguntas fundamentais, com base no framework, nos pilares e nas lentes. Essas perguntas validarão se uma determinada prática recomendada está em vigor na carga de trabalho ou não.

O conteúdo do framework é composto por:

- Pilares e lentes
- Princípios de design
- Perguntas
- Práticas recomendadas

### 1.11 Pilares do AWS Well-Architected

Atualmente, há seis pilares do Well-Architected Framework: excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. Esses pilares são os fundamentos da arquitetura de suas soluções de tecnologia na nuvem.

- **01 Excelência operacional**
- **02 Segurança**
- **03 Confiabilidade**
- **04 Eficiência de desempenho**
- **05 Otimização de custos**
- **06 Sustentabilidade**

### 1.12 Lentes do AWS Well-Architected

As lentes do Well-Architected se estendem à orientação oferecida pelo AWS Well-Architected a domínios específicos do setor e da tecnologia. Exemplos desses domínios são Machine Learning, data analytics, aplicações sem servidor, computação de alto desempenho e Internet das Coisas, SAP, mídia de streaming, setor de jogos, redes híbridas, e serviços financeiros.

Para avaliar totalmente as cargas de trabalho, você usa as lentes aplicáveis juntamente com a estrutura e seus seis pilares. Também é possível criar lentes personalizadas definidas pelo usuário e gerenciadas para melhor se alinhar ao setor, aos planos operacionais e aos processos internos da sua organização. Você pode criar seus conjuntos de perguntas e adicionar contexto e práticas recomendadas conforme se relacionam com sua própria organização e processos. Nem todas as lentes estão presentes na ferramenta no momento, mas todas estão disponíveis como parte do framework.

Lentes disponíveis:

- Data Analytics
- Setor de jogos
- Machine Learning
- Serviços financeiros
- Aplicação sem servidor
- Redes híbridas
- IoT
- SAP
- Mídia de streaming
- SaaS
- HPC
- Lentes personalizadas

### 1.13 Princípios gerais de design

Os princípios gerais de design são aplicados a todas as cargas de trabalho e a todos os pilares. Há também princípios de design específicos para cada pilar, sobre os quais você aprenderá mais a seguir.

A computação em nuvem abriu espaço tecnológico para um mundo totalmente novo na forma de pensar onde as restrições que tínhamos no ambiente tradicional não existem mais. Ao pensar nos princípios gerais de design, é interessante contrastar com a forma como você pensaria sobre isso em um ambiente tradicional. Você precisaria adivinhar o tamanho da infraestrutura que seria necessária, o que se baseia em demanda e requisitos de negócio de alto nível e, muitas vezes, antes que uma linha de código fosse escrita. Você não poderia se dar ao luxo de testar e dimensionar porque uma duplicação completa dos custos de produção é difícil de justificar, especialmente com baixa utilização. Então, quando você entrava em produção, normalmente encontrava uma nova classe de problemas em alta escala.

Qualquer prova de conceito ou experimento de arquitetura teria sido feito manualmente e geralmente apenas no início do projeto. Você tinha arquiteturas estáticas e seria difícil até mesmo pensar em fazer mudanças. Geralmente, não era possível gerar conjuntos de dados que possibilitassem a tomada de decisões informadas, portanto, você provavelmente usava modelos e suposições para dimensionar sua arquitetura. Por fim, em um ambiente tradicional, você apenas usaria o runbook quando algo ruim ocorresse na produção.

Na nuvem, as restrições foram removidas. Você pode usar esses princípios para tirar proveito disso.

Os princípios gerais de design do Well-Architected Framework são:

1. 1Parar de adivinhar as necessidades de capacidade.
2. 2Testar os sistemas em escala de produção.
3. 3Automatizar para facilitar experimentos de arquitetura.
4. 4Permitir que as arquiteturas evoluam.
5. 5Impulsionar arquiteturas usando dados.
6. 6Aprimorar por meio de dias de teste.

### 1.14 Princípios de design

Cada pilar do framework também tem seus próprios princípios de design. Eles são chamados de princípios de design específicos de cada pilar e se aplicam somente a pilares específicos do framework.

Como você aprendeu anteriormente, um dos princípios gerais do design é aprimorar por meio de dias de teste. Dias de teste é um termo que significa testar sua arquitetura e seus processos, simulando regularmente eventos em produção. Isso o ajudará a entender onde é possível fazer melhorias e a desenvolver a experiência organizacional para lidar com eventos.

> **EX:** **Princípio geral → princípio específico do pilar:** "Aprimorar por meio de dias de teste" (geral) leva à "preparação para eventos de segurança" (específico do pilar de segurança). Prepare-se para um incidente tendo processos e uma política de investigação e gerenciamento de incidentes que estejam alinhados aos requisitos da organização. Execute simulações de resposta a incidentes e use ferramentas com automação para aumentar sua velocidade de detecção, investigação e recuperação.

### 1.15 Perguntas e práticas recomendadas

Os dois últimos componentes do framework são perguntas e práticas recomendadas. Você pode usar perguntas para validar se uma prática específica está em vigor ou não. Cada pilar tem um conjunto de perguntas e práticas para responder a essas perguntas. Essas são as práticas recomendadas, ou respostas, com as quais os clientes obtiveram sucesso. As respostas não são diretas. A resposta pode ser válida devido ao seu contexto da carga de trabalho. Você ainda precisará aplicar seus conhecimentos de arquitetura.

Uma pergunta do framework é composta por três partes: texto da pergunta, contexto da pergunta e práticas recomendadas. Por exemplo:

> SEG 8 — Como você protege os dados ociosos?

> **CTX:** Proteja seus dados em repouso implementando vários controles para reduzir o risco de acesso não autorizado ou manuseio incorreto.

- ****Implemente o gerenciamento seguro de chaves**:** As chaves de criptografia devem ser armazenadas de forma segura, com controle de acesso rigoroso, por exemplo, usando um serviço de gerenciamento de chaves, como o AWS KMS. Considere o uso de chaves diferentes e o controle de acesso às chaves, combinado com o IAM e as políticas de recursos, para alinhar-se aos níveis de classificação de dados e aos requisitos de segregação.
- ****Aplique a criptografia em repouso**:** Aplique seus requisitos de criptografia com base nos padrões e recomendações mais recentes para ajudar a proteger seus dados em repouso.
- ****Automatize a proteção dos dados em repouso**:** Use ferramentas automatizadas para validar e aplicar a proteção de dados em repouso continuamente, por exemplo, verifique se há apenas recursos de armazenamento criptografados.

### 1.16 Pergunta 1

Com que finalidade a ferramenta do AWS Well-Architected foi criada?

- A Identificar as ameaças associadas ao modelo de negócios do cliente.
- B Analisar a configuração do cluster do Amazon Elastic Kubernetes Service (Amazon EKS) de um cliente.
- C Determinar se a fatura de um cliente está correta.
- D Medir as cargas de trabalho e as equipes de um cliente em relação às práticas recomendadas do AWS Well-Architected.

**Resposta: D.** Medir as cargas de trabalho e as equipes de um cliente em relação às práticas recomendadas do AWS Well-Architected — esse é o propósito central da ferramenta.

### 1.17 Pergunta 2

Quais são algumas partes do conteúdo do AWS Well-Architected Framework? (Selecione TRÊS.)

- A Pilares
- B Perguntas
- C Listas de verificação
- D Princípios de design
- E Framework de software
- F Métricas

**Resposta: A, B, D.** Pilares, Perguntas e Princípios de design são partes do conteúdo do framework — as demais opções não fazem parte da estrutura oficial.

### 1.18 Resumo do Módulo 1

Neste módulo, você aprendeu o valor e os benefícios do Well-Architected Framework. Você também aprendeu sobre o processo, o objetivo e as informações obtidas por meio da análise do Well-Architected Framework.

- O valor do Well-Architected Framework
- Os benefícios do Well-Architected Framework
- O processo, o objetivo e as informações obtidas por meio da análise do Well-Architected Framework

<a id="modulo-2"></a>

## Módulo 2 — Como executar uma análise do Well-Architected Framework

### 2.1 AWS Well-Architected

Boas-vindas ao módulo dois do AWS Well-Architected: Como executar uma análise do Well-Architected Framework.

### 2.2 Objetivos de aprendizado

Neste módulo, você aprenderá a concluir uma análise do Well-Architected Framework, a compreender o impacto das decisões de design sobre sua arquitetura e a avaliar os riscos em sua arquitetura e como mitigá-los.

Neste módulo, você aprenderá a:

- Concluir uma análise do Well-Architected Framework
- Compreender o impacto das decisões de design sobre sua arquitetura
- Avaliar os riscos em sua arquitetura e como mitigá-los

### 2.3 O que é a análise do Well-Architected Framework?

A análise do Well-Architected Framework é um mecanismo de aprimoramento contínuo que ajuda os clientes a avaliar consistentemente as cargas de trabalho em relação às práticas recomendadas da Amazon Web Services, ou AWS. Por meio dessa análise, é possível identificar as correções recomendadas para tratar de problemas de alto e médio risco.

O objetivo da análise de uma arquitetura é ajudar a identificar quaisquer problemas críticos que podem precisar ser resolvidos ou áreas que possam ser aprimoradas. O resultado da análise é um conjunto de ações criadas para aprimorar a arquitetura da carga de trabalho com base nos seis pilares do framework.

### 2.4 Um mecanismo

Para atingir o objetivo desejado com uma análise do framework, é importante considerá-la como uma etapa de um plano de aprimoramento contínuo que se integre ao ciclo de vida da carga de trabalho. Esse mecanismo tem três etapas: aprender, medir e aprimorar.

Primeiro, comece aprendendo as estratégias e as práticas recomendadas para a arquitetura na nuvem. Em seguida, você pode avaliar sua arquitetura usando o framework; as lentes do Well-Architected, como a lente de data analytics e as práticas recomendadas de sua organização com as lentes personalizadas na ferramenta do AWS Well-Architected ou AWS WA Tool.

Por fim, você pode usar o resultado para aprimorar sua arquitetura de nuvem, abordando quaisquer problemas de alto risco. Você pode identificar problemas usando planos de aprimoramento, laboratórios do Well-Architected, a Rede de Parceiros da AWS (APN), equipes de arquitetura de soluções da AWS e muito mais.

Você precisa aplicar esse mecanismo de três etapas em todas as cargas de trabalho da sua organização. Uma carga de trabalho identifica um conjunto de componentes que, juntos, proporcionam valor comercial. Você saberá mais sobre os detalhes da carga de trabalho em um módulo posterior.

O mecanismo para aprimoramento contínuo é um ciclo aplicado às cargas de trabalho, com três etapas:

1. **Aprender:** as estratégias e práticas recomendadas para arquitetura na nuvem
2. **Medir:** sua arquitetura usando o framework, as lentes e as práticas recomendadas da organização
3. **Aprimorar:** sua arquitetura de nuvem, abordando os problemas de alto risco identificados

### 2.5 Intenção da análise

O objetivo da análise de uma arquitetura é ajudar a identificar quaisquer problemas críticos que precisam ser resolvidos ou áreas que possam ser aprimoradas. O resultado da análise é um conjunto de ações que devem aprimorar a experiência de uso da carga de trabalho.

Para atingir esse objetivo, a análise da arquitetura precisa ser feita de forma consistente e com uma abordagem sem acusações que incentive a equipe a se aprofundar. Deve ser um processo leve que seja concluído em horas, não em dias. Trata-se de uma conversa, não de uma auditoria.

Os membros da equipe que criam uma arquitetura usando esse framework devem analisar continuamente a arquitetura, em vez de realizar uma reunião formal de análise. Uma abordagem contínua ajuda os membros da sua equipe a atualizar as respostas à medida que a arquitetura evolui, aprimorando-a à medida que você fornece recursos.

| A análise... | Como aplicar |
| --- | --- |
| **Não é uma auditoria** | Trabalhamos juntos para aprimorar |
| **Não é teórica** | Conselhos pragmáticos comprovados |
| **Não é uma verificação única** | Durante todo o ciclo de vida |

### 2.6 Aprendizados

Algumas das lições que aprendemos ao fazer as análises incluem o seguinte.

Primeiro, faça a análise no início do ciclo de vida, pois é mais rápido e mais fácil corrigir problemas e influenciar o design.

Segundo, os problemas às vezes não são causados por decisões ruins, mas sim por não perceber que há uma decisão que precisa ser tomada. Por exemplo, os membros da equipe normalmente não decidem não fazer backup dos dados; eles simplesmente se esquecem de falar sobre isso.

E terceiro, a maioria das cargas de trabalho tem itens de alto risco que precisam ser resolvidos. Descobrir tais itens não é uma coisa ruim, eles sempre estiveram ali. Se você resolvê-los, será uma coisa a menos que pode prejudicar ou atrasar seus negócios.

| Pergunta | Aprendizado |
| --- | --- |
| **Apenas pré-lançamento?** | Mais cedo é melhor |
| **Tomada de más decisões?** | Decisões não consideradas |
| **Descobertas?** | A maioria das cargas de trabalho pode ser aprimorada |

### 2.7 Casos de uso

Agora, você conhecerá alguns dos casos de uso mais comuns das análises da ferramenta do AWS Well-Architected.

O primeiro caso de uso é **aprender as práticas recomendadas para a nuvem**. Isso se aplica à maioria dos clientes e suas equipes que desejam aprender a arquitetar para a nuvem. Ao conhecer as práticas recomendadas da AWS, as empresas podem identificar riscos e oportunidades de aprimoramento para sua arquitetura.

A **governança tecnológica** é outra consideração. Antes de iniciar a produção, você quer saber se você e sua carga de trabalho estão prontos. Com muitas equipes, pode ser difícil saber se todas elas estão fazendo as coisas certas. Quando se trata de iniciar qualquer processo ou análise, como é possível obter consistência? Como os problemas são priorizados ao longo do tempo? A ferramenta do AWS Well-Architected fornece um processo consistente para medir sua arquitetura usando as práticas recomendadas da AWS.

Para o **gerenciamento de portfólio**, a maioria das organizações depende de seu portfólio de tecnologia para operar. As organizações geralmente não têm um registro central do que está nesse portfólio e quais são os riscos. Isso significa que pode ser difícil tomar decisões informadas sobre onde investir. As organizações que têm um processo de análise provavelmente não têm um processo consistente e abrangente, e os resultados não podem ser descobertos.

Ao usar a ferramenta do AWS Well-Architected, você terá um portfólio de cargas de trabalho em sua organização. Você tem um local para registrar metadados sobre as cargas de trabalho, como produção, conta ou Regiões. Os clientes costumam usar a ferramenta para documentar as decisões de arquitetura que tomaram. Isso cria uma visão central de todos os seis pilares e de todos os riscos existentes. A gerência sênior pode então verificar as tendências em todo o portfólio e qualquer treinamento que possa ser necessário.

Casos de uso comuns:

- Aprender práticas recomendadas para a nuvem
- Governança tecnológica
- Gerenciamento de portfólio

### 2.8 As três fases da análise

Há três fases na execução de uma análise do Well-Architected Framework: preparação, análise e aprimoramento.

Na fase de **preparação**, você define uma carga de trabalho para a análise em sua organização e identifica as pessoas que podem responder às perguntas durante a análise de cada pilar. Você também precisa identificar alguém para ser o responsável pelo plano de aprimoramento e, eventualmente, pela implantação do aprimoramento como resultado da análise. Esses indivíduos são chamados de responsáveis.

Durante a fase de **análise**, você executa a análise real usando o AWS WA Tool. Em seguida, você publica o relatório que contém detalhes sobre o estado atual da carga de trabalho, incluindo notas e ações de aprimoramento recomendadas. Durante essa fase, você identifica problemas de alto risco e problemas de médio risco para correção.

Na fase de **aprimoramento**, você começa a analisar os problemas de risco identificados como parte da análise, prioriza-os e cria um plano de tratamento detalhado para resolvê-los.

Você se aprofundará em cada fase e nas práticas recomendadas.

| Fase | Foco |
| --- | --- |
| **Preparação** | Identificar responsáveis, escopo da carga de trabalho |
| **Análise** | Analisar a carga de trabalho, criar o relatório |
| **Aprimoramento** | Priorizar problemas, plano de tratamento |

### 2.9 Preparação

Primeiro, você aprenderá mais sobre a fase de preparação da análise.

### 2.10 Práticas recomendadas para a preparação de análises

Que medidas você pode tomar para ajudar a se preparar para a análise?

Primeiro, **defina a carga de trabalho** que será analisada. Uma carga de trabalho pode ser um processo, uma tecnologia, uma infraestrutura, uma equipe ou uma combinação de todos eles, que agrega valor comercial à sua organização. Por exemplo, um site em que você recebe pedidos de compra de seus clientes pode ser uma carga de trabalho.

Em seguida, **identifique a equipe principal** para a carga de trabalho analisada. Essa equipe é responsável pelo sucesso dessa carga de trabalho e contém especialistas no assunto para cada pilar. Os especialistas dessa equipe devem ser capazes de responder às perguntas de cada pilar e devem ser responsáveis pelo plano de aprimoramento futuro que pode resultar da identificação de riscos na arquitetura.

Em seguida, você precisa **realizar uma sessão de escopo**. É aqui que você decide sobre a carga de trabalho e os pilares a serem revisados.

- Defina a carga de trabalho
- Identifique a equipe principal
- Realize sessão de escopo

### 2.11 Práticas recomendadas para a preparação de análises (cont.)

Outros aspectos da preparação incluem a decisão sobre o tipo de análise. Por exemplo, trata-se de uma sessão de um dia para analisar os seis pilares ou de várias sessões para analisar os pilares separadamente?

Os participantes também precisam se preparar e reunir os dados necessários para responder às perguntas da análise. Finalmente, você está pronto para agendar a análise.

- Determinar o tipo de análise
- Coletar dados
- Agendar sessão

### 2.12 Etapas de preparação da análise

A seguir, um exemplo de cronograma que pode ajudar você a planejar a análise.

Aproximadamente três semanas antes de uma análise planejada, selecione uma carga de trabalho e uma equipe principal de análise. Convide os participantes para a reunião de definição do escopo.

Cerca de 14 dias antes da análise, realize a sessão de definição do escopo. Nessa reunião, confirme e registre a definição da carga de trabalho. Selecione as perguntas apropriadas da ferramenta do AWS Well-Architected, incluindo as lentes relevantes, quando aplicável. Identifique especialistas no assunto para todas as questões relevantes e defina o tipo e a abordagem da análise. Solicite que os participantes coletem dados relevantes que sejam acessíveis, em vez de criar novos dados para a análise.

Então, cinco dias antes da análise, o escopo deve ser confirmado por todos os participantes. Envie um lembrete para que eles tragam todas as informações relevantes que estejam prontamente disponíveis.

No dia anterior à análise, envie um lembrete final a todos os participantes.

- **~ 3 semanas antes:** Seleção de carga de trabalho, seleção da equipe principal, convite para reunião de escopo.
- **~ 14 dias antes:** Reunião de escopo, relevância das perguntas, identificação de quem pode responder às perguntas, participantes da análise, cronograma da análise.
- **~ 5 dias antes:** Verificar com os participantes se a agenda ou o escopo precisa de alguma alteração, lembrete para ter todas as informações relevantes disponíveis durante a análise.
- **1 dia antes:** Lembrete final para a participação na análise de todos os participantes.

### 2.13 Análise

A segunda fase é a fase de análise para conduzir a análise real.

### 2.14 Práticas recomendadas para a execução de análises

Ao realizar uma análise, recomendam-se algumas práticas recomendadas.

A partir da equipe principal de análise, o **moderador** administra a reunião e se atém ao escopo definido durante a preparação. Convém que a equipe de análise nomeie uma pessoa para fazer anotações sobre a discussão e inseri-las na ferramenta. É possível fazer rodízio dessa função na equipe para distribuir a carga e o esforço. É importante que o moderador não seja também o tomador de notas, pois isso pode levar a análises menos produtivas.

Somente **uma pessoa atualiza a ferramenta** por vez. Os campos não são alterados dinamicamente conforme modificados em vários clientes. Os registros atualizados são substituídos. Use a ferramenta do AWS Well-Architected para monitorar os resultados. Uma dica é configurar um bucket do Amazon Simple Storage, ou Amazon S3, para armazenar análises ou outros diagramas ou documentação relacionados a essa carga de trabalho. Você pode usar uma convenção de nomenclatura simples, como o nome da conta e da carga de trabalho.

Mantenha o **foco nos problemas e riscos de maior prioridade**.

- Uma pessoa faz anotações
- Apenas UMA pessoa atualiza a ferramenta
- Simplifique, mantenha-se no escopo

### 2.15 Aprimoramento

A terceira fase é a fase de aprimoramento. Essa fase consiste em elaborar um plano de aprimoramento para mitigar alguns dos riscos identificados como resultado da realização da análise.

### 2.16 Metodologia de priorização de riscos e considerações

A primeira etapa da fase de aprimoramento da análise é a priorização dos riscos. Antes de começar a priorização de riscos, é uma boa ideia definir brevemente o termo.

> A priorização de riscos é o processo de identificação dos riscos mais críticos para que eles possam ser tratados primeiro.

As prioridades devem ser definidas com base na probabilidade de um risco e no impacto potencial que ele representa para a organização ou para os negócios. O objetivo é determinar uma ordem de classificação dos riscos identificados do mais crítico para o menos crítico.

Exemplos de impactos de risco incluem perda de vendas, responsabilidade corporativa, danos à reputação da marca, perda de participação no mercado, maior tempo de colocação no mercado, questões legais, regulatórias e assim por diante. Os riscos são identificados com base nas metas, necessidades e prioridades da empresa. Os exemplos incluem tempo de colocação no mercado, segurança, confiabilidade, desempenho e custo.

No Well-Architected Framework, os níveis de risco são categorizados como alto ou médio. Como o nome sugere, os problemas de alto risco são escolhas arquitetônicas e operacionais que a AWS descobriu que podem resultar em um impacto negativo significativo para uma empresa. Embora os problemas de risco médio também possam afetar negativamente os negócios, eles geralmente o fazem em menor escala.

- **HRI**
  Problemas de alto risco (High Risk Issue)
- **MRI**
  Problemas de risco médio (Medium Risk Issue)

### 2.17 Fluxo de trabalho de aprimoramento do Well-Architected

Agora que você conhece os níveis de risco, é útil revisar o fluxo de trabalho de aprimoramento para identificar, priorizar e, posteriormente, abordar esses riscos.

Comece **identificando riscos e as oportunidades de aprimoramento**. Isso é obtido com a execução de uma análise do Well-Architected Framework em relação a uma carga de trabalho para entender onde a carga de trabalho é medida em relação às práticas recomendadas de nuvem no framework.

À medida que você coleta dados sobre a carga de trabalho, geramos informações para **entender onde estão os riscos e as oportunidades de aprimoramento**.

Em seguida, você aproveitará as oportunidades de aprimoramento e **determinará soluções prescritivas**. Elas abordam os problemas que têm maior prioridade com base no impacto potencial e no nível de esforço necessário para implementá-las e eliminar o maior número possível de riscos ao mesmo tempo.

Depois que as soluções forem determinadas, é importante identificar quais são as mais prioritárias do ponto de vista comercial — **priorizar aprimoramentos**.

Então, é possível começar a **implementar as soluções de aprimoramento** por ordem de prioridade e **acompanhar** o progresso. O progresso de aprimoramento deve ser acompanhado, monitorando os resultados para garantir que os benefícios desejados sejam alcançados.

As práticas recomendadas no framework incluem orientações sobre pessoas, processos e tecnologia. A implantação de uma prática recomendada ausente requer uma combinação de colaboração entre a equipe da sua conta AWS e ações da sua parte para aplicá-las. Essas fases serão explicadas em mais detalhes nos próximos módulos.

O fluxo de trabalho de aprimoramento é um ciclo contínuo:

1. 1Identificar riscos e oportunidades de aprimoramento
2. 2Entender riscos e oportunidades de aprimoramento
3. 3Determinar soluções prescritivas
4. 4Priorizar aprimoramentos
5. 5Implementar e acompanhar os aprimoramentos

### 2.18 Pergunta 1

Quais são as três fases da análise do AWS Well-Architected Framework?

- A Preparação, análise e auditoria
- B Preparação, análise e aprimoramento
- C Preparação, condução e identificação de riscos
- D Preparação, análise e priorização

**Resposta: B.** Preparação, análise e aprimoramento.

### 2.19 Pergunta 2

Uma análise do AWS Well-Architected Framework de uma carga de trabalho maior pode ser dividida em várias análises.

- A Verdadeiro
- B Falso

**Resposta: A.** Verdadeiro.

### 2.20 Resumo do Módulo 2

Neste módulo, você aprendeu a concluir uma análise do Well-Architected Framework e os impactos das decisões de design na sua arquitetura. Você também aprendeu a identificar e avaliar os riscos em sua arquitetura e como mitigá-los.

Neste módulo, você aprendeu a:

- Concluir uma análise do Well-Architected Framework
- Compreender os impactos das decisões de design sobre sua arquitetura
- Avaliar os riscos em sua arquitetura e como mitigá-los

<a id="modulo-3"></a>

## Módulo 3 — Análise detalhada da ferramenta do AWS Well-Architected

### 3.1 Boas-vindas!

Boas-vindas ao módulo 3 do AWS Well-Architected: Análise detalhada da ferramenta do AWS Well-Architected.

### 3.2 Objetivos de aprendizado

Neste módulo, você aprenderá sobre os componentes e recursos da ferramenta do AWS Well-Architected ou AWS WA Tool. Você também vai descobrir como usar a ferramenta para executar uma análise do Well-Architected Framework e saber mais sobre a ferramenta.

Neste módulo, você aprenderá sobre:

- Os componentes e os recursos da ferramenta do AWS Well-Architected
- Como usar a ferramenta para executar uma análise do Well-Architected Framework
- Onde saber mais sobre a ferramenta

### 3.3 Um mecanismo para aprimoramento contínuo

Para atingir o objetivo desejado com uma análise do framework, é importante considerá-la como uma etapa de um plano de melhoria contínua que se integre ao ciclo de vida da carga de trabalho.

Esse mecanismo começa primeiro com o aprendizado das estratégias e práticas recomendadas para a arquitetura na nuvem. Depois, você pode avaliar sua arquitetura usando o AWS Well-Architected framework e as lentes do Well-Architected e as práticas recomendadas de sua organização com as lentes personalizadas na ferramenta do AWS Well-Architected.

Por fim, você pode usar o resultado para aprimorar sua arquitetura de nuvem, abordando quaisquer problemas de alto risco. Esses problemas podem ser identificados usando planos de melhoria, laboratórios do Well-Architected, a Rede de Parceiros da AWS (APN), equipes de arquitetura de soluções da AWS e muito mais.

Esse mecanismo de três etapas deve ser aplicado de forma consistente em todas as cargas de trabalho de sua organização. Uma carga de trabalho identifica um conjunto de componentes que, juntos, proporcionam valor comercial.

O mecanismo de aprimoramento contínuo é um ciclo aplicado às cargas de trabalho, com três etapas:

1. **Aprender:** 
2. **Medir:** 
3. **Aprimorar:** 

### 3.4 Componentes do Well-Architected Framework

Você viu uma versão desse diagrama dos componentes do framework em um módulo anterior. Para revisar, o framework inclui conteúdo que você pode usar para aprender as práticas recomendadas da AWS. Ele também tem uma ferramenta que pode ajudar a medir sua carga de trabalho e suas equipes em relação às práticas recomendadas.

Além disso, a ferramenta contém dados que você adquire durante a revisão de suas cargas de trabalho. Isso pode ser usado para melhorar continuamente suas cargas de trabalho e operações. Neste módulo, você se aprofundará em como o AWS Well-Architected pode ser usado pelos clientes para medir e melhorar ao longo do tempo.

Os três componentes do framework:

- **Conteúdo**
  - Framework: pilares (áreas), princípios de design, perguntas, práticas recomendadas
  - Whitepapers (PDF, Kindle) do treinamento, site
  - Recursos úteis, resumos de conteúdo, glossário interativo
- **Ferramenta**
  - Cargas de trabalho, revisão (perguntas e respostas), painel relatório (PDF)
  - Abordagem da revisão: autoatendimento, parceiro, conduzido pela AWS
  - Recursos do Marketplace da Rede de Parceiros da AWS (APN)
  - Planos de melhoria
- **Dados**
  - Documentar cargas de trabalho: descrição, regiões, prioridade do pilar
  - Análise: classificação, respostas, observações, marcos

### 3.5 Ferramenta do AWS Well-Architected

A ferramenta do AWS Well-Architected foi desenvolvida para ajudar você a analisar o estado das suas aplicações e cargas de trabalho, fornecendo um local central para as práticas recomendadas e orientações de arquitetura. Além da orientação padrão fornecida pelo framework e pelas lentes da AWS, a ferramenta ajuda você a adicionar orientações de práticas recomendadas usando lentes personalizadas.

A maneira mais rápida de iniciar é realizar uma análise do Well-Architected Framework, usando a ferramenta no console ou com as APIs. Você pode criar a carga de trabalho da ferramenta do AWS Well-Architected na conta AWS do cliente para armazená-la com segurança. Isso segue o acesso com privilégio mínimo, em que somente as pessoas têm acesso aos detalhes da carga de trabalho.

As cargas de trabalho podem ser compartilhadas com seu arquiteto de soluções e equipe de contas ou recurso de parceiro para colaboração nas etapas de revisão ou correção. As lentes personalizadas também podem ser compartilhadas com o arquiteto de soluções ou com o recurso do parceiro para colaboração.

O fluxo básico da ferramenta:

1. 1**Identifique a carga de trabalho a ser revisada** — em seguida, responda a uma série de perguntas sobre sua arquitetura.
2. 2**Ferramenta do AWS Well-Architected** — revise suas respostas com base nos seis pilares estabelecidos pelo Well-Architected Framework.
3. 3**Obtenha vídeos e documentos** relacionados às melhores práticas da AWS.
4. 4**Gere o relatório** que resume a revisão das cargas de trabalho.
5. 5**Visualize os resultados** das revisões de cargas de trabalho em toda a organização em um único painel.

Recursos:

- Página do produto Ferramenta do AWS Well-Architected
- Laboratório da ferramenta do AWS Well-Architected

### 3.6 Visão geral da ferramenta do AWS Well-Architected

Quando você navega até a ferramenta do AWS Well-Architected no console de gerenciamento da AWS, o painel mostra os recursos da Região que você selecionou. Conforme mencionado no histórico do Well-Architected, atualizações e melhorias contínuas no framework e na ferramenta são feitas com base no feedback dos clientes. Se houver cargas de trabalho que não estejam usando a versão mais recente de uma lente ou do framework, você terá a opção de atualizar essas cargas de trabalho usando a opção Exibir atualizações disponíveis no console.

Você pode acessar uma lista de todas as cargas de trabalho atuais disponíveis em uma determinada conta e Região na lista Cargas de trabalho no console. Você também pode visualizar os detalhes da carga de trabalho, como nome, proprietário, número de perguntas respondidas e número de riscos identificados. No console de cargas de trabalho, você também pode definir uma nova carga de trabalho para iniciar uma nova análise para essa carga de trabalho.

Principais áreas do painel:

- ****Opções da ferramenta do AWS Well-Architected**:** menu com Dashboard, Custom lenses, Share invitations, Workloads e Settings.
- ****Detalhes da carga de trabalho**:** lista com nome, proprietário, status geral, riscos altos, riscos médios e status de melhoria.
- ****Atualizações disponíveis**:** aviso quando uma carga de trabalho usa uma versão desatualizada de uma lente ou do framework.
- ****Definir nova carga de trabalho**:** botão *Define workload* para iniciar uma nova análise.

### 3.7 Nova carga de trabalho da ferramenta do AWS Well-Architected

Ao criar uma nova carga de trabalho na ferramenta, a primeira coisa que você precisa é de um nome exclusivo e descritivo para identificá-la. Você também precisa especificar uma descrição da carga de trabalho para documentar seu escopo e finalidade pretendida.

Outro campo obrigatório é o campo do proprietário da análise, que foi adicionado em 2020. O proprietário da análise é a pessoa que, em última instância, tem a responsabilidade de concluir a análise, relatar o status dos riscos e acompanhar as melhorias ao longo do tempo.

Em seguida, está o ambiente para a carga de trabalho. As duas opções, produção e pré-produção, ajudam a identificar em que ponto do ciclo de vida está a carga de trabalho.

Campos da tela "Specify properties":

- ****Nome da carga de trabalho (Name)**:** um identificador exclusivo para a carga de trabalho.
- ****Descrição da carga de trabalho (Description)**:** uma breve descrição para documentar o escopo e a finalidade pretendida.
- ****Proprietário da análise (Review owner)**:** nome, e-mail ou identificador do responsável pelo processo de análise.
- ****Ambiente da carga de trabalho (Environment)**:** Production ou Pre-production.

### 3.8 Nova carga de trabalho da ferramenta do AWS Well-Architected (cont.)

Os últimos campos obrigatórios, ao configurar uma nova carga de trabalho, são as Regiões em que ela é executada. Ao criar uma nova carga de trabalho na ferramenta, lembre-se de que o conceito de carga de trabalho é algo que você elege como cliente. Isso significa que é um conceito sintético, portanto, as Regiões em que a carga de trabalho é executada são usadas principalmente para ajudar a pesquisar, classificar e filtrar. Observe também que as práticas recomendadas no framework podem ser estendidas para além do seu ambiente AWS. Você pode usar a ferramenta para analisar os recursos que estão sendo executados no local ou em outros ambientes de provedores de nuvem.

A próxima seção é para o ID da conta, ou IDs, se a sua carga de trabalho abranger várias contas. Observe que, por padrão, você não precisará conceder à ferramenta nenhuma permissão do AWS Identity and Access Management (IAM) ou o acesso aos IDs de conta especificados aqui. Se estiver usando uma Well-Architected API ou serviços fornecidos por parceiros de software da AWS que funcionam entre contas, talvez seja necessário alterar as permissões nos IDs de conta listados para que o acesso programático funcione corretamente. Consulte a referência da API na documentação da ferramenta ou na documentação do produto de terceiro ou do parceiro do AWS Marketplace.

Há também um local opcional para especificar o URL de um design arquitetônico para a carga de trabalho na qual você fará a análise. Isso pode ser usado como recurso de referência ao executar uma análise para garantir que todos tenham as mesmas informações de configuração sobre a carga de trabalho. Isso é especialmente útil se a sua análise estiver recebendo suporte de funcionários da AWS ou por um Parceiro do AWS Well-Architected.

O último conjunto de opções ao criar uma nova carga de trabalho é estabelecer o tipo de setor e o setor de sua organização ou carga de trabalho. Mais uma vez, isso é fornecido principalmente para ajudar a classificar, filtrar e pesquisar quando você cria várias cargas de trabalho.

Campos adicionais da tela "Specify properties":

- ****Regiões das cargas de trabalho (Regions)**:** Regiões da AWS ou fora da AWS em que a carga de trabalho é executada.
- ****IDs de contas de carga de trabalho (Account IDs)**:** opcional; IDs das contas AWS que a carga de trabalho abrange.
- ****Design arquitetônico (Architectural design)**:** opcional; um link para o design arquitetônico da carga de trabalho.
- ****Setor e tipo (Industry type)**:** opcional; o setor associado à carga de trabalho.

### 3.9 Detalhes da carga de trabalho da ferramenta do AWS Well-Architected

Depois que uma nova carga de trabalho tiver sido criada ou selecionada em uma lista de cargas de trabalho existentes, você encontrará uma visão geral da carga de trabalho. Na visão geral, é possível editar os detalhes da carga de trabalho depois de ela ter sido criada. Você também pode excluir uma carga de trabalho dessa visualização.

A visão geral da carga de trabalho inclui o número de perguntas que seriam respondidas em relação ao total disponível. Ela também contém os riscos que foram identificados durante o processo de análise.

É importante observar na página de detalhes da carga de trabalho que você tem a opção de salvar um marco para acompanhar o progresso ao fazer uma análise do framework.

Elementos da tela "Workload overview":

- ****Editar detalhes da carga de trabalho**:** botão *Edit*.
- ****Excluir carga de trabalho**:** botão *Delete workload*.
- ****Perguntas respondidas e riscos**:** número de perguntas respondidas (ex: 57/58) e riscos identificados (High risk, Medium risk).
- ****Salvar marco**:** botão *Save milestone*, para acompanhar o progresso da análise.

### 3.10 Detalhes da carga de trabalho da ferramenta do AWS Well-Architected (cont.)

Abaixo dos detalhes da carga de trabalho, você também verá as observações que foram inseridas sobre a carga de trabalho em geral. Essas observações são abertas e podem ser usadas para acompanhar o progresso, mudanças importantes ou informações sobre lançamentos futuros.

Abaixo das observações da carga de trabalho, você verá uma lista das lentes aplicadas a essa carga de trabalho. As lentes fora do framework padrão são abordadas em outra sessão da série. Isso inclui as lentes criadas e suportadas pela AWS e também a criação de lentes personalizadas. Para obter mais informações, consulte as outras sessões.

Na parte inferior dos detalhes da carga de trabalho, você verá a prioridade do pilar que escolheu para essa carga de trabalho. Aqui está listada a prioridade padrão do pilar. Isso não quer dizer que um pilar seja mais importante do que outro. Em vez disso, essa é a ordem em que a maioria dos clientes tende a abordar os conceitos no framework. Se suas prioridades para a carga de trabalho forem diferentes da ordem padrão, você poderá usar o botão de edição para alterar a prioridade do pilar. A alteração da prioridade do pilar reorganizará a ordem das perguntas na ferramenta. Ele também alterará a ordem das recomendações de melhoria com base em suas prioridades.

Elementos adicionais da página de detalhes da carga de trabalho:

- ****Observações sobre a carga de trabalho (Workload notes)**:** campo aberto para anotações gerais.
- ****Detalhes da lente de carga de trabalho (Lenses)**:** lista das lentes aplicadas, autor, perguntas respondidas e riscos.
- ****Prioridade do pilar (Pillar priority)**:** ordem padrão: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.
- ****Editar prioridade do pilar**:** botão *Edit*, para reordenar os pilares conforme as prioridades da carga de trabalho.

### 3.11 Ferramenta do AWS Well-Architected (marcos)

Os marcos são um mecanismo que você pode usar para rastrear as alterações que ocorrem em uma carga de trabalho ao longo do tempo. Normalmente, um marco é criado após a conclusão da análise inicial. À medida que você faz melhorias ou alterações em sua carga de trabalho, pode atualizar suas respostas, observações e práticas recomendadas para denotar essas alterações. Depois que essas atualizações forem feitas, você poderá criar um novo marco para ajudar a acompanhar o progresso e as melhorias ao longo do tempo.

Selecione qualquer um dos marcos que você criou pelo nome e, em seguida, selecione Gerar relatório. O relatório será baseado no status da análise no momento em que o marco foi salvo. Você também pode visualizar todos os marcos, inclusive o atual, usando Exibir marcos.

Elementos da aba "Milestones":

- ****Nomes dos marcos**:** ex: *Pre-Production*, *First-Remediation-date*.
- ****Detalhes dos marcos**:** perguntas respondidas, riscos altos, riscos médios e data em que o marco foi salvo.
- ****Gerar relatório (Generate report)**:** cria um relatório baseado no status do marco selecionado.
- ****Visualizar marco (View milestone)**:** exibe os detalhes completos de um marco específico.

### 3.12 Compartilhamento da ferramenta do AWS Well-Architected

Um outro recurso importante da ferramenta é a capacidade de compartilhar cargas de trabalho com outros usuários, contas ou até mesmo por meio de organizações da AWS. Se você compartilha uma carga de trabalho com várias entidades principais, há uma opção de pesquisa ou filtro para ajudar a encontrar os compartilhamentos de carga de trabalho atuais.

Por meio dos detalhes do compartilhamento, você pode ver qual é a entidade principal atual e se é um usuário do IAM, outra conta AWS ou uma organização AWS. Você também pode revisar o status atual de um compartilhamento, se ele está pendente ou aceito, e quais permissões ele concede a outras entidades principais.

Elementos da aba "Shares":

- ****Buscar e filtrar**:** campo de busca por Principal e filtro por status.
- ****Entidade principal compartilhada com**:** coluna Principal, indicando o usuário IAM, conta ou organização.
- ****Compartilhar status**:** Status (ex: *Accepted*, *Pending*) e Permission (ex: *Read-Only*).
- ****Novas opções de compartilhamento**:** botão *Create*, com opções *Create shares to IAM users or accounts* e *Create shares to Organizations*.

### 3.13 Conteúdo da ferramenta do AWS Well-Architected

Agora, reserve um momento para se aprofundar e considerar como uma pergunta na ferramenta é exibida. Na parte superior, você encontrará o pilar e o número da pergunta, incluindo a pergunta que é o tópico da discussão. Cada pergunta tem um conceito-chave com o qual se relaciona. Nesse caso, a pergunta do Custo 6 está focada no dimensionamento correto.

Cada conceito em uma pergunta do framework foi criado para ajudar você a entender como implantar o princípio de projeto desse pilar. Por exemplo, nesse caso, o conceito de dimensionamento correto é usado para ajudar você a implantar o princípio de projeto de adoção de um modelo de consumo.

Abaixo da pergunta e de sua explicação, também é possível encontrar uma lista de caixas de seleção que representam as práticas recomendadas de como atingir esse conceito-chave. Na barra de detalhes à esquerda da tela, você pode explorar explicações adicionais sobre cada prática recomendada. Você também pode acessar recursos úteis para saber mais sobre possíveis métodos de implantação de práticas recomendadas nessa questão.

Elementos da tela de pergunta:

- ****Pergunta**:** ex: *COST 6. How do you meet cost targets when you select resource type, size and number?*
- ****Conceito-chave**:** ex: *Dimensionamento correto*.
- ****Princípio de projeto**:** ex: *Adotar um modelo de consumo*.
- ****Práticas recomendadas**:** lista de caixas de seleção com as práticas para atingir o conceito-chave (ex: *Perform cost modeling*, *Select resource type, size, and number based on data*).
- ****Recursos úteis (Helpful resources)**:** links e explicações adicionais sobre cada prática recomendada.

### 3.14 Lentes personalizadas da ferramenta do AWS Well-Architected

Além de medir suas cargas de trabalho em relação ao framework e às lentes da AWS, agora você pode criar suas próprias lentes personalizadas. As lentes personalizadas podem incluir pilares, perguntas, opções de resposta, recursos úteis e planos de melhoria. Você pode especificar regras para determinar quais opções, quando não seguidas, resultariam em um risco alto ou médio. Em seguida, você pode fornecer sua própria orientação para resolver o risco. Isso ajuda a compartilhar essas lentes entre suas contas e a medir consistentemente as cargas de trabalho em sua organização.

Você pode criar sua própria lente personalizada usando a Ferramenta do AWS Well-Architected. Baixe o modelo JSON e, em seguida, faça o upload da sua lente e aplique-a à análise da carga de trabalho da mesma forma que você aplica as lentes da AWS hoje. Isso ajuda os clientes a analisar sua carga de trabalho usando seu conjunto personalizado de perguntas, da mesma forma que você analisa as cargas de trabalho em relação ao framework ou ao conteúdo da AWS. Você também pode compartilhar a lente personalizada com outra conta, arquiteto de soluções ou parceiro da AWS.

Fluxo para criar uma lente personalizada:

- ****Disponível no console**:** em *Custom lenses*, no console da ferramenta do AWS Well-Architected.
- ****Modelo básico disponível para baixar**:** botão *Download file* para obter o modelo JSON base.
- ****Fazer upload da lente**:** arquivo formatado em JSON, com dados definidos pelo usuário.
- ****Documentação da lente personalizada**:** link para a documentação com o formato esperado do arquivo JSON.

Recurso: [Lentes personalizadas — AWS Well-Architected Tool User Guide](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html)

### 3.15 Quais são as novidades do AWS WA?

A AWS apresentou o **pilar de sustentabilidade** durante a re:Invent 2021 para ajudar os clientes a minimizar os impactos ambientais da execução de cargas de trabalho na nuvem. Em março de 2022, esse pilar ficou disponível para os clientes usarem durante as análises de carga de trabalho na ferramenta do AWS Well-Architected. O pilar de sustentabilidade foi criado para ajudar chief technology officers, arquitetos, desenvolvedores e membros da equipe de operações a contribuir para um número cada vez maior de metas de sustentabilidade definidas por suas organizações.

A ferramenta agora apresenta acesso direto ao **AWS re:Post**, um serviço de perguntas e respostas orientado pela comunidade para ajudar os clientes da AWS a remover obstáculos técnicos, acelerar a inovação e melhorar a operação. O AWS re:Post inclui mais de 40 tópicos, com uma comunidade específica para o AWS Well-Architected.

A ferramenta do AWS Well-Architected lançou a **integração com o AWS Organizations** em junho de 2022. Essa integração ajudou os arquitetos de nuvem a compartilhar cargas de trabalho e lentes personalizadas de forma mais ampla em toda a organização. O AWS Organizations é um serviço de gerenciamento de contas que os clientes usam para consolidar várias contas AWS em uma única organização gerenciada de forma centralizada. Essa atualização aumenta a eficiência e simplifica o compartilhamento de lentes e cargas de trabalho em várias contas.

A ferramenta foi iniciada nas **Regiões do AWS GovCloud (EUA)** em agosto de 2022 para clientes com requisitos regulatórios e de conformidade específicos e parceiros da AWS. Tanto o setor público quanto o comercial podem usá-la para realizar análises do Well-Architected com autoatendimento. O AWS GovCloud (EUA) é uma Região isolada projetada para hospedar dados sigilosos e cargas de trabalho regulamentadas na nuvem.

Com a **integração do AWS Trusted Advisor**, a ferramenta do AWS Well-Architected agora apresenta descobertas com base em verificações automatizadas de recursos do Trusted Advisor. Isso fornece mais informações contextuais durante as análises, melhorando a precisão das respostas e a velocidade da análise. Anteriormente, os clientes que realizavam análises do framework tinham que gastar tempo verificando as respostas, checando novamente as cargas de trabalho para verificar se estavam seguindo as práticas recomendadas. Não havia uma ligação clara entre a carga de trabalho que estava sendo analisada e os recursos associados.

A ferramenta do AWS Well-Architected também está agora **integrada ao AppRegistry do AWS Service Catalog**. Você pode usar o AppRegistry para armazenar suas aplicações AWS, coleções de recursos associados e grupos de atributos de aplicações. A integração com o AppRegistry oferece melhor visibilidade de quais aplicações estão associadas a quais cargas de trabalho durante o processo de análise. Isso pode economizar seu tempo ao rastrear e organizar os recursos associados às suas cargas de trabalho.

Você pode verificar o link do feed de novidades para obter mais recursos atualizados à medida que eles são adicionados à ferramenta do AWS Well-Architected.

Principais novidades:

- Pilar de sustentabilidade adicionado à ferramenta do AWS Well-Architected
- AWS re:Post a partir da ferramenta do AWS Well-Architected
- Integração da ferramenta do AWS Well-Architected com o AWS Organizations
- Ferramenta do AWS Well-Architected disponível nas Regiões do AWS GovCloud (EUA)
- Integração da ferramenta do AWS Well-Architected com o AWS Trusted Advisor
- Integração da ferramenta do AWS Well-Architected com o AppRegistry do AWS Service Catalog

Recurso: [Novidades do AWS Well-Architected — feed de novidades da AWS](https://aws.amazon.com/pt/new/?whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&awsf.whats-new-networking-content-delivery=*all&awsf.whats-new-quantum-tech=*all&awsf.whats-new-robotics=*all&awsf.whats-new-satellite=*all&awsf.whats-new-security-id-compliance=*all&awsf.whats-new-serverless=*all&awsf.whats-new-storage=*all&awsf.whats-new-analytics=*all&awsf.whats-new-app-integration=*all&awsf.whats-new-arvr=*all&awsf.whats-new-blockchain=*all&awsf.whats-new-business-applications=*all&awsf.whats-new-cloud-financial-management=*all&awsf.whats-new-compute=*all&awsf.whats-new-containers=*all&awsf.whats-new-customer-enablement=*all&awsf.whats-new-customer%20engagement=*all&awsf.whats-new-database=*all&awsf.whats-new-developer-tools=*all&awsf.whats-new-end-user-computing=*all&awsf.whats-new-mobile=*all&awsf.whats-new-gametech=*all&awsf.whats-new-iot=*all&awsf.whats-new-machine-learning=*all&awsf.whats-new-management-governance=*all&awsf.whats-new-media-services=*all&awsf.whats-new-migration-transfer=*all&whats-new-content-all.q=AWS%2BWell-Architected&whats-new-content-all.q_operator=AND#feed)

### 3.16 Pergunta 1

Qual desses é um componente do AWS Well-Architected Framework?

- A Conteúdo
- B Pilares
- C Lista de verificação
- D Diagramas de arquitetura

**Resposta: A.** Conteúdo.

### 3.17 Pergunta 2

Qual item é obrigatório definir ao adicionar uma carga de trabalho para análise usando a ferramenta do AWS Well-Architected?

- A Região
- B Tipo de setor
- C ID da conta
- D Design de arquitetura

**Resposta: A.** Região.

### 3.18 Pergunta 3

Qual mecanismo da ferramenta do AWS Well-Architected pode ser usado para rastrear as melhorias na arquitetura da carga de trabalho?

- A Lentes personalizadas
- B Marcos
- C Práticas recomendadas no Well-Architected Framework
- D Observações sobre a carga de trabalho

**Resposta: B.** Marcos.

### 3.19 Pergunta 4

Qual é a maneira recomendada de compartilhar uma carga de trabalho?

- A Usar o recurso de compartilhamento na ferramenta do AWS Well-Architected.
- B Não é recomendado compartilhar uma análise de carga de trabalho com clientes ou com a equipe de contas da AWS.
- C Fazer upload do relatório em um bucket do Amazon S3 e compartilhar o link público.
- D Baixar o relatório, criptografá-lo e enviá-lo por e-mail aos clientes.

**Resposta: A.** Usar o recurso de compartilhamento na ferramenta do AWS Well-Architected.

### 3.20 Resumo do Módulo 3

Neste módulo, você aprendeu sobre a ferramenta do AWS Well-Architected. Mais especificamente, você aprendeu sobre os componentes e recursos da ferramenta e como usá-la para fazer uma análise do Well-Architected Framework. Por fim, você também descobriu onde pode obter mais informações sobre a ferramenta do AWS Well-Architected.

Neste módulo, você aprendeu sobre:

- Os componentes e os recursos da ferramenta do AWS Well-Architected
- Como usar a ferramenta do AWS Well-Architected para executar uma análise do Well-Architected Framework
- Onde saber ainda mais sobre a ferramenta do AWS Well-Architected

<a id="modulo-4"></a>

## Módulo 4 — Análise detalhada do pilar de excelência operacional

### 4.1 Boas-vindas!

Boas-vindas ao módulo quatro do AWS Well-Architected: Análise detalhada do pilar de excelência operacional.

### 4.2 Objetivos de aprendizado

Neste módulo, você terá uma visão geral do pilar de excelência operacional do AWS Well-Architected Framework. Você também aprenderá os princípios de design e as práticas recomendadas do pilar de excelência operacional.

Neste módulo, você:

- Terá uma visão geral do pilar de excelência operacional do AWS Well-Architected Framework
- Aprenderá sobre os princípios de design e as práticas recomendadas do pilar de excelência operacional

### 4.3 Visão geral do pilar de excelência operacional

Para começar, você terá uma visão geral do pilar de excelência operacional.

### 4.4 Pilares do Well-Architected

Atualmente, há seis pilares do Well-Architected Framework: excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. Esses pilares são os fundamentos da arquitetura de suas soluções de tecnologia na nuvem. O foco deste módulo será o pilar de excelência operacional.

- **01 Excelência operacional**
- **02 Segurança**
- **03 Confiabilidade**
- **04 Eficiência de desempenho**
- **05 Otimização de custos**
- **06 Sustentabilidade**

### 4.5 O que é o pilar de excelência operacional?

O que é o pilar de excelência operacional? Alguns dos fundamentos da excelência operacional são garantir que suas cargas de trabalho, seus processos e procedimentos forneçam valor comercial para sua organização. Suas cargas de trabalho precisam fornecer valor comercial efetivo, e todas as funções de suporte em torno dessa carga de trabalho precisam reforçar isso.

Excelência operacional é a execução de suas cargas de trabalho de forma eficiente. Ter uma carga de trabalho segura, com custo otimizado, confiável e de alto desempenho é fantástico, mas se suas equipes não conseguirem executá-la e operá-la com eficiência, ela se torna uma despesa para o negócio.

> A excelência operacional é a capacidade de oferecer suporte ao desenvolvimento e executar cargas de trabalho de forma eficaz, obter informações sobre as operações e melhorar continuamente os processos e procedimentos de suporte para fornecer valor comercial.

**Por que a excelência operacional é importante para melhorar sua arquitetura?**

### 4.6 Excelência operacional

Agora que já sabe o que é o pilar de excelência operacional, você se aprofundará nos princípios de design do pilar da excelência operacional.

### 4.7 Excelência operacional

Existem cinco princípios de design para a excelência operacional na nuvem.

O primeiro é **realizar operações como código**. Na nuvem, é possível aplicar a mesma disciplina de engenharia utilizada no código da aplicação a todo o ambiente. Você pode definir toda a sua carga de trabalho, como aplicações, infraestrutura e assim por diante, como código e atualizá-la com código. Você pode criar scripts para seus procedimentos de operações e automatizar a inicialização deles, invocando-os em resposta a eventos. Isso pode limitar o erro humano e gerar respostas consistentes aos eventos.

O segundo princípio é **fazer mudanças frequentes, pequenas e reversíveis**. Projete cargas de trabalho de modo que você possa atualizar os componentes regularmente para aumentar o fluxo de alterações benéficas em sua carga de trabalho. Faça alterações em pequenos incrementos para possibilitar a reversão em caso de falha, a fim de ajudar a identificar e resolver problemas introduzidos em seu ambiente, sem afetar os clientes, quando possível.

O terceiro princípio é **refinar os procedimentos operacionais com frequência**. Conforme você usa os procedimentos operacionais, procure oportunidades para melhorá-los. À medida que sua carga de trabalho evolui, aprimore seus procedimentos adequadamente. Defina dias de teste regulares para revisar e validar que todos os procedimentos são eficazes e que as equipes estão familiarizadas com eles.

O quarto princípio é **prever falhas**. Execute exercícios pre-mortem para identificar possíveis fontes de falha para que você possa removê-las ou atenuá-las. Teste os cenários de falha e valide a compreensão do seu impacto. Teste seus procedimentos de resposta para garantir que eles sejam eficazes e que as equipes estejam familiarizadas com a forma de iniciá-los. Defina dias de teste regulares para testar a carga de trabalho e as respostas da equipe a eventos simulados.

O último princípio de design é **aprender com todas as falhas operacionais**. Promova melhorias por meio das lições aprendidas com todos os eventos e falhas operacionais. Compartilhe o que aprendeu com as equipes e com toda a organização.

Os cinco princípios de design de excelência operacional:

1. 1Executar operações como código
2. 2Fazer alterações frequentes, pequenas e reversíveis
3. 3Refinar os procedimentos de operações com frequência
4. 4Prever falhas
5. 5Aprender com todas as falhas operacionais

### 4.8 Práticas recomendadas de excelência operacional

Agora que você já entendeu os princípios de design da excelência operacional, aprenderá sobre as práticas recomendadas de excelência operacional.

### 4.9 Excelência operacional

Para ajudar você a navegar pelas práticas recomendadas de excelência operacional, o pilar analisa quatro áreas de foco diferentes.

A primeira área de foco é a **organização**. Você precisa entender as prioridades da sua organização, sua estrutura organizacional e como ela dá suporte aos membros da sua equipe, para que eles possam dar suporte aos seus resultados comerciais.

Outra área de foco é **se preparar**. Para se preparar para a excelência operacional, você precisa entender suas cargas de trabalho e os comportamentos esperados. Em seguida, você pode projetá-los para fornecer informações sobre seu status e criar os procedimentos para apoiá-los.

A terceira área de foco é **operar**. Sucesso é a obtenção de resultados comerciais medidos pelas métricas que você define. Ao compreender a integridade de sua carga de trabalho e de suas operações, você pode identificar quando os resultados organizacionais e comerciais podem estar em risco, ou estão em risco, e responder adequadamente.

A última área de foco de práticas recomendadas é **evoluir**. A evolução é o ciclo contínuo de aprimoramento ao longo do tempo. Implemente pequenas e frequentes mudanças incrementais com base nas lições aprendidas em suas atividades operacionais e avalie o sucesso dessas mudanças para obter melhorias.

As quatro áreas de práticas recomendadas de excelência operacional:

- **01 Organização**
- **02 Preparar**
- **03 Operar**
- **04 Evoluir**

### 4.10 Organização

A organização é a primeira área de práticas recomendadas de excelência operacional.

### 4.11 Prioridades da organização

Suas equipes precisam entender toda a carga de trabalho, a função que desempenham nela e as metas comerciais compartilhadas para definir as prioridades que impulsionarão o sucesso dos negócios. Prioridades bem definidas maximizarão os benefícios de seus esforços. Revise suas prioridades regularmente para que possa atualizá-las à medida que as necessidades da sua organização mudarem. Você pode considerar algumas práticas recomendadas para isso.

**Avalie as necessidades dos clientes externos.** Envolva stakeholders importantes, incluindo equipes de negócios, desenvolvimento e operações, para determinar onde concentrar esforços nas necessidades dos clientes externos. Isso garantirá que você tenha um entendimento completo do suporte operacional necessário para alcançar os resultados comerciais desejados.

**Avalie as necessidades dos clientes internos.** Envolva os principais stakeholders ao determinar onde concentrar esforços nas necessidades dos clientes internos, para garantir que você entenda o suporte operacional necessário para alcançar os resultados comerciais. Use suas prioridades estabelecidas para concentrar seus esforços de aprimoramento onde eles terão o maior impacto. Isso pode significar, por exemplo, desenvolver habilidades de equipe, melhorar o desempenho da carga de trabalho, reduzir custos, automatizar runbooks ou aprimorar o monitoramento. Atualize suas prioridades conforme as necessidades mudarem.

**Avalie os requisitos de governança.** Governança é o conjunto de políticas, regras ou estruturas que uma empresa usa para atingir as metas comerciais. Os requisitos de governança são gerados dentro de sua organização. Eles podem afetar os tipos de tecnologias que você escolhe ou influenciar a maneira como você opera sua carga de trabalho. Incorpore os requisitos de governança organizacional em sua carga de trabalho. Conformidade é a capacidade de demonstrar que você implementou os requisitos de governança.

**Avalie os requisitos de conformidade.** Os requisitos de conformidade regulatória, do setor e internos são um importante fator para definir as prioridades de sua organização. Seu framework de conformidade pode impedi-lo de usar tecnologias ou localizações geográficas específicas. Aplique a devida diligência se nenhuma estrutura de conformidade externa for identificada. Gere auditorias ou relatórios que validem a conformidade. Se você anuncia que seu produto atende a padrões de conformidade específicos, deve ter um processo interno para garantir a conformidade contínua. Exemplos de padrões de conformidade incluem PCI DSS, FedRAMP e HIPAA. Os padrões de conformidade aplicáveis são determinados por vários fatores, como os tipos de dados que a solução armazena ou transmite e as Regiões geográficas às quais a solução oferece suporte.

**Avalie o cenário de ameaças.** Avalie as ameaças aos negócios, como concorrência, riscos e responsabilidades comerciais, riscos operacionais e ameaças à segurança das informações. Mantenha informações atualizadas em um registro de riscos. Inclua o impacto dos riscos ao determinar onde concentrar os esforços.

**Avalie as compensações.** Avalie o impacto das compensações entre interesses conflitantes ou abordagens alternativas, para ajudar a tomar decisões informadas ao determinar onde concentrar esforços ou escolher um curso de ação. Por exemplo, você pode enfatizar a aceleração da velocidade de lançamento de novos recursos no mercado em detrimento da otimização de custos. Ou você pode escolher um banco de dados relacional para dados não relacionais para simplificar o esforço de migração de um sistema, em vez de migrar para um banco de dados otimizado para o seu tipo de dados e atualizar a aplicação.

**Gerencie os benefícios e os riscos.** Isso ajudará você a tomar decisões informadas ao determinar onde concentrar seus esforços. Por exemplo, pode ser vantajoso implantar uma carga de trabalho com problemas não resolvidos para disponibilizar novos recursos significativos aos clientes. Pode ser possível mitigar os riscos associados ou pode se tornar inaceitável que um risco permaneça e, nesse caso, você tomará ações para lidar com o risco. Talvez você queira enfatizar um pequeno subconjunto de suas prioridades em algum momento. Use uma abordagem equilibrada de longo prazo para garantir o desenvolvimento das capacidades necessárias e o gerenciamento de riscos. Atualize suas prioridades conforme as necessidades mudarem.

Práticas recomendadas para prioridades da organização:

- Avaliar as necessidades dos clientes externos
- Avaliar as necessidades dos clientes internos
- Avaliar os requisitos de governança
- Avaliar os requisitos de conformidade
- Avaliar o cenário de ameaças
- Avaliar as compensações
- Gerenciar os benefícios e os riscos

### 4.12 Modelos de operação

Neste diagrama, o eixo vertical mostra aplicações e plataformas. Aplicações referem-se à carga de trabalho que atende a um resultado comercial e podem ser softwares desenvolvidos sob medida ou adquiridos. A plataforma refere-se à infraestrutura física e virtual e a outros softwares que dão suporte a essa carga de trabalho.

No eixo horizontal, temos engenharia e operações. Engenharia refere-se ao desenvolvimento, à criação e ao teste de aplicações e infraestrutura. Operações é a implantação, atualização e suporte contínuo de aplicações e infraestrutura.

Há outras versões desse modelo que representam como essas responsabilidades tendem a ser distribuídas entre as equipes. Para mais detalhes, consulte a documentação desse pilar.

A matriz do modelo de operação:

|  | Engenharia | Operações |
| --- | --- | --- |
| **Aplicações** | Engenharia de aplicações — *Software comercial*: desenvolvido sob medida ou comercial de pronta entrega | Operações de aplicações |
| **Plataforma** | Engenharia da plataforma — *Infraestrutura*: computação, rede, armazenamento, middleware, runtime, operações de dados, segurança | Operações de plataforma |

- ****Desenvolver, criar e testar**:** todas as atividades necessárias para definir e validar a plataforma, a infraestrutura ou as aplicações comerciais.
- ****Implantar, operar e gerenciar**:** todas as atividades necessárias para implantar e dar suporte à plataforma, à infraestrutura e às aplicações em produção.

### 4.13 Cultura organizacional

Ofereça suporte aos membros da sua equipe para que eles possam ser mais eficazes na tomada de ações e no suporte aos resultados do seu negócio.

Uma maneira de fazer isso é por meio do **patrocínio executivo**. A liderança sênior define claramente as expectativas para a organização e avalia o sucesso. A liderança sênior é a patrocinadora, defensora e impulsionadora da adoção de práticas recomendadas e da evolução da organização.

Outra forma é **capacitar os membros da equipe**. O proprietário da carga de trabalho definiu a orientação e o escopo, capacitando os membros da equipe a responder quando os resultados estiverem em risco. Os mecanismos de encaminhamento são usados para obter orientação quando os eventos estão fora do escopo definido. Os membros da equipe também têm mecanismos e são incentivados a levar suas preocupações aos tomadores de decisão e stakeholders se acreditarem que os resultados estão em risco. O encaminhamento deve ser realizado antecipadamente e com frequência para que os riscos possam ser identificados e impedidos de causar incidentes.

**As comunicações são oportunas, claras e acionáveis.** Mecanismos existem e são usados para avisar em tempo hábil os membros da equipe sobre riscos conhecidos e eventos planejados. O contexto, os detalhes e o tempo necessários são fornecidos, quando possível, para ajudar a determinar se a ação é necessária, qual ação é exigida e para agir em tempo hábil. Por exemplo, avisar sobre vulnerabilidades de software para agilizar a aplicação de patches ou avisar sobre promoções de vendas planejadas para que um congelamento de mudanças possa ser implementado para evitar o risco de interrupção do serviço. Os eventos planejados podem ser registrados em um calendário de mudanças ou cronograma de manutenção para que os membros da equipe possam identificar as atividades pendentes.

**A experimentação é incentivada**, pois pode ser um catalisador para transformar novas ideias em produtos e recursos. Ela acelera o aprendizado e mantém os membros da equipe interessados e engajados. Os membros da equipe são incentivados a experimentar com frequência para impulsionar a inovação. Mesmo quando ocorre um resultado indesejado, é importante saber o que não fazer. Os membros da equipe não são punidos por experiências bem-sucedidas com resultados indesejados.

**Os membros da equipe são capacitados e incentivados a manter e aumentar os conjuntos de habilidades.** As equipes precisam desenvolver os conjuntos de habilidades para adotar novas tecnologias e dar suporte às mudanças na demanda e nas responsabilidades em apoio às suas cargas de trabalho. O desenvolvimento de habilidades em novas tecnologias é frequentemente uma fonte de satisfação para os membros da equipe e apoia a inovação. Apoie os membros da sua equipe na busca e manutenção de certificações do setor que validem e reconheçam as habilidades que eles estão desenvolvendo. Promova capacitação cruzada para promover a transferência de conhecimento e reduzir o risco de impacto significativo ao perder membros da equipe qualificados e experientes com conhecimento institucional. Proporcione tempo estruturado dedicado ao aprendizado.

**Forneça recursos adequados às equipes.** Garanta a capacidade dos membros da equipe e forneça ferramentas e recursos para atender às suas necessidades de carga de trabalho. A sobrecarga de tarefas dos membros da equipe aumenta o risco de incidentes resultantes de erro humano. Os investimentos em ferramentas e recursos, por exemplo, fornecendo automação para atividades realizadas com frequência, podem dimensionar a eficácia da sua equipe. Isso pode fazer com que eles auxiliem em atividades adicionais.

**Opiniões diversas são incentivadas e buscadas dentro e entre as equipes.** Aproveite a diversidade interorganizacional para buscar várias perspectivas únicas. Use essa perspectiva para aumentar a inovação, desafiar suas suposições e reduzir o risco dos vieses de confirmação. Aumente a inclusão, a diversidade e a acessibilidade em suas equipes para obter perspectivas benéficas.

Práticas recomendadas para cultura organizacional:

- Patrocínio executivo
- Os membros da equipe têm autonomia para agir quando os resultados estão em risco
- Incentiva-se o encaminhamento
- As comunicações são oportunas, claras e acionáveis
- Incentiva-se a experimentação
- Os membros da equipe são capacitados e incentivados a manter e aumentar o conjunto de habilidades
- Forneça recursos adequados às equipes
- Opiniões diversas são incentivadas e buscadas dentro e entre as equipes

### 4.14 Preparar

Para se preparar para a excelência operacional, você precisa entender suas cargas de trabalho e os comportamentos esperados. Em seguida, você pode projetá-los para fornecer informações sobre o status e criar procedimentos para apoiá-los.

### 4.15 Projetar Telemetria

Projete sua carga de trabalho de modo que ela forneça as informações necessárias para que você entenda o estado interno. Os exemplos incluem métricas, logs, eventos e rastreamentos. Isso deve ser feito em todos os componentes para apoiar a observabilidade e a investigação de problemas. Faça iterações para desenvolver a telemetria necessária para monitorar a integridade de sua carga de trabalho, identificar quando os resultados estão em risco e gerar respostas eficazes.

**Implemente a telemetria de aplicações**, que é a base para a observabilidade de sua carga de trabalho. Sua aplicação deve emitir telemetria que forneça informações sobre o estado da aplicação e a obtenção de resultados comerciais. Desde a solução de problemas até a medição do impacto de um novo recurso, a telemetria de aplicações informa a maneira como você cria, opera e desenvolve sua carga de trabalho. A telemetria de aplicações consiste em métricas e logs. As métricas são informações de diagnóstico, como seu pulso ou temperatura; são usadas coletivamente para descrever o estado da sua aplicação. A coleta de métricas ao longo do tempo pode ser usada para desenvolver linhas de base e detectar anomalias. Os logs são mensagens que a aplicação envia sobre seu estado interno ou eventos que ocorrem. Exemplos de eventos que são registrados incluem códigos de erro, identificadores de transação e ações do usuário.

**Implemente e configure a telemetria de carga de trabalho.** Projete e configure sua carga de trabalho para emitir informações sobre seu estado interno e status atual, por exemplo, volume de chamadas de API, códigos de status HTTP e eventos de scaling. Use essas informações para ajudar a determinar quando uma resposta é necessária.

**Implemente a telemetria de atividade do usuário.** Instrumente o código da aplicação para emitir informações sobre a atividade do usuário. Exemplos de atividade do usuário incluem transmissões de cliques ou transações iniciadas, abandonadas e concluídas. Use essas informações para ajudar a entender como a aplicação é usada, os padrões de uso e para determinar quando uma resposta é necessária. Ao capturar a atividade real do usuário, é possível criar uma atividade sintética que pode ser usada para monitorar e testar a carga de trabalho na produção.

**Implemente a telemetria de dependência.** Projete e configure sua carga de trabalho para emitir informações sobre o status dos recursos dos quais ela depende. Esses são recursos externos à sua carga de trabalho. Exemplos de dependências externas incluem bancos de dados externos, DNS e conectividade de rede. Use essas informações para determinar quando uma resposta é necessária e fornecer contexto adicional sobre o estado da carga de trabalho.

**Implemente a rastreabilidade das transações.** Implemente o código da sua aplicação e configure os componentes da sua carga de trabalho para emitir eventos, que são acionados como resultado de operações lógicas únicas e consolidados em vários limites da sua carga de trabalho. Gere mapas para ver como os registros trafegam em sua carga de trabalho e serviços. Obtenha informações sobre as relações entre os componentes e identifique e analise problemas. Em seguida, use as informações coletadas para determinar quando uma resposta é necessária e para ajudá-lo a identificar os fatores que contribuem para um problema.

Práticas recomendadas para projetar telemetria:

- Implementar a telemetria da aplicação
- Implementar e configurar a telemetria de carga de trabalho
- Implementar a telemetria de atividade do usuário
- Implementar a telemetria de dependência
- Implementar a rastreabilidade das transações

### 4.16 Projetar para operações

Adote abordagens que melhorem o fluxo de mudanças na produção e que possibilitem a refatoração, o feedback rápido sobre a qualidade e a correção de bugs. Isso acelera a entrada de mudanças benéficas na produção, limita os problemas implantados e promove a rápida identificação e correção dos problemas introduzidos pelas atividades de implantação.

Com a AWS, você pode visualizar toda a sua carga de trabalho, incluindo aplicações, infraestrutura, política, governança e operações, como código. Tudo pode ser definido e atualizado usando código. Isso significa que você pode aplicar a mesma disciplina de engenharia usada para código de aplicação a cada elemento de sua pilha.

**Use o controle de versão** para iniciar o rastreamento de alterações e versões.

**Teste e valide as alterações.** Você precisa testar cada alteração implantada para evitar erros na produção. Essa prática recomendada se concentra em testar as alterações do controle de versão para a compilação de artefatos. Além das alterações no código da aplicação, os testes devem incluir infraestrutura, configuração, controles de segurança e procedimentos operacionais. Os testes assumem várias formas, desde testes unitários até análise de componentes de software (SCA). Mover os testes mais para a esquerda no processo de integração e entrega de software resulta em maior certeza da qualidade do artefato. Sua organização deve desenvolver padrões de teste para todos os artefatos de software. Os testes automatizados reduzem o trabalho e evitam erros nos testes manuais. Em alguns casos, podem ser necessários testes manuais. Os desenvolvedores devem ter acesso aos resultados dos testes automatizados para criar circuitos de feedback que melhorem a qualidade do software.

**Use sistemas de gerenciamento de configuração** para fazer e rastrear alterações de configuração. Esses sistemas reduzem os erros causados por processos manuais e reduzem o nível de esforço para implantar alterações.

**Use sistemas de gerenciamento de compilação e implantação**, que reduzem os erros causados por processos manuais e o nível de esforço para implantar alterações.

**Execute o gerenciamento de patches** para obter recursos, resolver problemas e manter a conformidade com a governança. Automatize o gerenciamento de patches para reduzir os erros causados por processos manuais e reduzir o nível de esforço para aplicar patches. O gerenciamento de patches e vulnerabilidades faz parte de suas atividades de gerenciamento de riscos e benefícios. É preferível ter infraestruturas imutáveis e implantar cargas de trabalho em estados bons conhecidos e verificados. Quando isso não for viável, você pode aplicar um patch no local.

**Compartilhe padrões de design** e práticas recomendadas entre as equipes para aumentar a conscientização e maximizar os benefícios dos esforços de desenvolvimento. Documente-os e mantenha-os atualizados à medida que sua arquitetura evolui. Se os padrões compartilhados forem aplicados em sua organização, é fundamental que existam mecanismos para solicitar adições, alterações e exceções aos padrões. Sem essa opção, os padrões se tornam uma restrição à inovação.

**Implemente práticas para melhorar a qualidade do código** e minimizar os defeitos. Alguns exemplos incluem desenvolvimento orientado por testes, revisões de código, adoção de padrões e programação em pares. Incorpore essas práticas em seu processo de integração contínua e entrega.

**Use vários ambientes** para experimentar, desenvolver e testar sua carga de trabalho. Use níveis crescentes de controles à medida que os ambientes se aproximam da produção para ganhar confiança de que a sua carga de trabalho funcionará como pretendido quando implantada.

**Faça alterações frequentes, pequenas e reversíveis.** Isso pode reduzir o escopo e o impacto de uma mudança. Isso facilita a solução de problemas, possibilita a correção mais rápida e oferece a opção de reverter uma mudança.

Por fim, você deve **automatizar totalmente a integração e a implantação.** Automatize a criação, a implantação e o teste da carga de trabalho. Isso reduz os erros causados por processos manuais e reduz o esforço para implantar alterações.

Práticas recomendadas para projetar para operações:

- Usar controle de versão
- Testar e validar as alterações
- Usar sistemas de gerenciamento de configuração
- Usar sistemas de gerenciamento de compilação e implantação
- Executar o gerenciamento de patches
- Compartilhar padrões de design
- Implementar práticas para melhorar a qualidade do código
- Usar vários ambientes
- Fazer alterações frequentes, pequenas e reversíveis
- Automatizar totalmente a integração e a implantação

### 4.17 Mitigar os riscos de implantação

Há também maneiras de reduzir os riscos de implantação.

**Planeje-se para mudanças malsucedidas.** Planeje reverter para um estado bom conhecido ou corrigir no ambiente de produção se uma alteração não tiver o resultado desejado. Essa preparação reduz o tempo de recuperação por meio de respostas mais rápidas.

**Teste e valide as alterações** em todos os estágios do ciclo de vida para confirmar os novos recursos e minimizar o risco e o impacto de implantações malsucedidas.

**Use sistemas de gerenciamento de implantação** para rastrear e implementar alterações. Isso reduz os erros causados por processos manuais e reduz o esforço para implantar alterações.

**Teste usando implantações limitadas** junto com os sistemas existentes para confirmar os resultados desejados antes da implantação em escala total. Por exemplo, use testes de canary de implantação ou implantações de caixa única.

**Implante usando ambientes paralelos.** Implemente as alterações em ambientes paralelos e depois faça a transição para o novo ambiente. Mantenha o ambiente anterior até que haja confirmação de que a implantação foi bem-sucedida. Isso minimiza o tempo de recuperação, possibilitando a reversão para o ambiente anterior.

**Implante alterações frequentes, pequenas e reversíveis** para reduzir o escopo de uma alteração. Isso resulta em uma solução de problemas mais fácil e uma correção mais rápida com a opção de reverter uma alteração.

**Automatize totalmente a integração e a implantação.** Automatize a criação, a implantação e o teste da carga de trabalho. Isso reduz os erros causados por processos manuais e reduz o esforço para implantar alterações.

Por fim, **automatize testes e reversão.** Automatize os testes de ambientes implantados para confirmar os resultados desejados. Automatize a reversão para um bom estado anterior conhecido quando os resultados não forem alcançados para minimizar o tempo de recuperação e reduzir os erros causados por processos manuais.

Práticas recomendadas para mitigar os riscos de implantação:

- Planejar para alterações malsucedidas
- Testar e validar as alterações
- Usar sistemas de gerenciamento de implantação
- Testar usando implantações limitadas
- Implantar usando ambientes paralelos
- Implantar alterações frequentes, pequenas e reversíveis
- Automatizar totalmente a integração e a implantação
- Automatizar testes e reversão

### 4.18 Prontidão operacional e gerenciamento de alterações

Avalie a prontidão operacional de sua carga de trabalho, processos, procedimentos e pessoal para entender os riscos operacionais relacionados à sua carga de trabalho. Gerencie o fluxo de alterações em seus ambientes. Você deve usar um processo consistente, incluindo listas de verificação manuais ou automatizadas, para saber quando está pronto para colocar em prática sua carga de trabalho ou uma alteração. Isso também ajudará você a encontrar áreas que precisa planejar para resolver. Você terá runbooks que documentam suas atividades de rotina e playbooks que orientam seus processos de resolução de problemas. Use um mecanismo para gerenciar as alterações que suporte o fornecimento de valor comercial e ajude a reduzir os riscos associados à alteração.

**Garanta a capacidade da equipe** com um mecanismo para validar se você tem o número adequado de pessoal treinado para suportar a carga de trabalho. Eles devem ser treinados na plataforma e nos serviços que compõem sua carga de trabalho. Forneça a eles o conhecimento necessário para operar a carga de trabalho. Deve haver pessoal suficiente para dar suporte à operação normal da carga de trabalho e solucionar quaisquer incidentes que ocorram. Tenha pessoal suficiente para que você possa fazer trocas durante o plantão e as férias para evitar o esgotamento.

**Garanta uma revisão consistente da prontidão operacional.** Use as Revisões de Prontidão Operacional, ou ORRs, para validar que é possível operar sua carga de trabalho. ORR é um mecanismo desenvolvido na Amazon para validar se as equipes podem operar as cargas de trabalho com segurança. É um processo de análise e inspeção que utiliza uma lista de verificação de requisitos e uma experiência de autoatendimento que as equipes usam para certificar as cargas de trabalho. As ORRs incluem práticas recomendadas de lições aprendidas em nossos anos de desenvolvimento de software. A lista de verificação inclui recomendações de arquitetura, processos operacionais, gerenciamento de eventos e qualidade de lançamento. Nosso processo de Correção de Erros é um dos principais impulsionadores desses itens. Sua própria análise pós-incidente deve orientar a evolução de sua própria ORR. Uma ORR não trata apenas de seguir as práticas recomendadas, mas de evitar a recorrência de eventos que você já presenciou antes. Os requisitos de segurança, governança e conformidade também podem ser incluídos em uma ORR.

**Use runbooks** para executar procedimentos. Runbooks são processos documentados para alcançar resultados específicos e consistem em uma série de etapas que alguém segue para realizar algo. Os runbooks têm sido usados em operações desde os primórdios da aviação. Em operações na nuvem, usamos runbooks para reduzir os riscos e alcançar os resultados desejados. Em sua forma mais simples, um runbook é uma lista de verificação para concluir uma tarefa.

**Use playbooks para investigar problemas.** Playbooks são guias passo a passo usados para investigar um incidente. Quando ocorrem incidentes, você pode usar playbooks para investigar, avaliar o impacto e identificar a causa-raiz. Você pode usar os playbooks para uma variedade de cenários, desde implantações com falha até incidentes de segurança. Em muitos casos, os playbooks identificam a causa-raiz na qual se usa um runbook com objetivo de mitigação. Os playbooks são um componente essencial dos planos de resposta a incidentes de sua organização.

**Tome decisões informadas para implantar sistemas e alterações.** Tenha processos em vigor para alterações bem-sucedidas e malsucedidas em sua carga de trabalho. Um pre-mortem é um exercício em que uma equipe simula uma falha para desenvolver estratégias de mitigação. Use pre-mortem para prever falhas e criar procedimentos quando apropriado. Avalie os benefícios e os riscos da implantação de alterações em sua carga de trabalho. Verifique se todas as alterações estão em conformidade com a governança.

**Facilite planos de suporte para cargas de trabalho de produção.** Garanta o suporte a todos os softwares e serviços dos quais sua carga de trabalho de produção depende. Selecione um nível de suporte adequado para atender às suas necessidades de nível de serviço de produção. Os planos de suporte para essas dependências são necessários em caso de interrupções de serviço ou problemas de software. Documente os planos de suporte e o modo de solicitar suporte para todos os fornecedores de serviços e software. Implemente mecanismos que verifiquem se os pontos de contato de suporte são mantidos atualizados.

Práticas recomendadas para prontidão operacional e gerenciamento de alterações:

- Garantir a capacidade da equipe
- Garantir uma revisão consistente da prontidão operacional
- Usar runbooks para executar procedimentos
- Usar playbooks para investigar problemas
- Tomar decisões informadas para implantar sistemas e alterações
- Facilitar planos de suporte para cargas de trabalho de produção

### 4.19 Operar

Sucesso é a obtenção de resultados comerciais medidos pelas métricas que você define. Ao compreender a integridade de sua carga de trabalho e de suas operações, você pode identificar quando os resultados organizacionais e comerciais podem estar em risco, ou estão em risco, e responder adequadamente.

### 4.20 Compreender a integridade da carga de trabalho

Defina, capture e analise métricas de carga de trabalho para obter visibilidade dos eventos de carga de trabalho, de modo que você possa tomar as medidas adequadas. Sua equipe deve ser capaz de entender facilmente a integridade da sua carga de trabalho. Você deverá usar métricas com base nos resultados da carga de trabalho para obter informações úteis. Você deve usar essas métricas para implementar painéis com pontos de vista comerciais e técnicos que ajudarão os membros da equipe a tomar decisões informadas.

**Identifique os indicadores-chave de desempenho (KPIs)** com base nos resultados comerciais desejados e nos resultados dos clientes. Os resultados comerciais desejados podem incluir a taxa de pedidos, a taxa de retenção de clientes e o lucro em relação às despesas operacionais. A satisfação do cliente é um exemplo de resultados para o cliente. Avalie os KPIs para determinar o sucesso da carga de trabalho.

**Defina as métricas de carga de trabalho**, que medem a integridade da carga de trabalho. A integridade da carga de trabalho é medida pela obtenção de resultados comerciais ou KPIs e pelo estado dos componentes e aplicações da carga de trabalho. Exemplos de KPIs incluem carrinhos de compras abandonados, pedidos feitos, custo, preço e despesa de carga de trabalho alocada. Embora você possa coletar a telemetria de vários componentes, selecione um subconjunto que forneça informações sobre a integridade geral da carga de trabalho. Ajuste as métricas de carga de trabalho ao longo do tempo, conforme as necessidades comerciais mudam.

**Colete e analise as métricas de carga de trabalho.** Realize análises regulares e proativas dessas métricas para identificar tendências e determinar se é necessária uma resposta e validar a obtenção de resultados comerciais. Agregue métricas de suas aplicações e componentes de carga de trabalho em um local central. Use painéis e ferramentas de analytics para analisar a telemetria e determinar a integridade da carga de trabalho. Implemente um mecanismo para realizar análises periódicas da integridade da carga de trabalho com stakeholders em sua organização.

**Estabeleça linhas de base de métricas de carga de trabalho** para ajudar a entender a integridade e o desempenho da carga de trabalho. Usando linhas de base, você pode identificar aplicações e componentes com desempenho abaixo ou acima do esperado. Uma linha de base de carga de trabalho aumenta sua capacidade de atenuar os problemas antes que eles se tornem incidentes. As linhas de base são fundamentais para desenvolver padrões de atividade e implementação de detecção de anomalias quando as métricas se desviam dos valores esperados.

**Aprenda os padrões de atividade esperados para a carga de trabalho.** Estabeleça padrões de atividade de carga de trabalho para identificar atividades anômalas e, assim, poder responder adequadamente, se necessário.

**Alerte quando os resultados da carga de trabalho estiverem em risco**, para que possa reagir adequadamente, se necessário. O ideal é que você tenha identificado previamente um limite de métrica sobre o qual possa disparar um alarme ou um evento que possa usar para invocar uma resposta automatizada.

**Alerte quando forem detectadas anomalias na carga de trabalho** para que você possa responder adequadamente, se necessário. A análise das métricas da carga de trabalho ao longo do tempo pode estabelecer padrões de comportamento que podem ser quantificados o suficiente para definir um evento ou acionar um alarme em resposta.

**Valide a obtenção de resultados e a eficácia de KPIs e métricas.** Crie uma visão comercial das operações de sua carga de trabalho para ajudar você a determinar se está atendendo às necessidades e a identificar as áreas que precisam ser aprimoradas para atingir as metas de negócios.

Práticas recomendadas para compreender a integridade da carga de trabalho:

- Identificar principais indicadores de desempenho
- Definir métricas da carga de trabalho
- Coletar e analisar as métricas da carga de trabalho
- Estabelecer linhas de base de métricas de carga de trabalho
- Aprender os padrões de atividade esperados para a carga de trabalho
- Alertar quando os resultados da carga de trabalho estiverem em risco
- Alertar quando forem detectadas anomalias na carga de trabalho
- Validar a obtenção de resultados e a eficácia de KPIs e métricas

### 4.21 Compreensão da integridade operacional

Defina, capture e analise métricas de operações para obter visibilidade dos eventos de carga de trabalho, para que você possa tomar as medidas adequadas. Sua equipe deve ser capaz de entender facilmente a integridade das suas operações. Você deverá usar métricas baseadas nos resultados das operações para obter informações úteis. Você deve usar essas métricas para implementar painéis de controle com pontos de vista comerciais e técnicos que ajudarão os membros da equipe a tomar decisões informadas.

**Identifique os principais indicadores de desempenho** com base nos resultados comerciais desejados, como novos recursos entregues, e nos resultados dos clientes, como casos de suporte ao cliente. Avalie os KPIs para determinar o sucesso das operações.

**Defina métricas de operações** para medir as realizações dos KPIs, por exemplo, implantações bem-sucedidas e implantações com falha. Defina métricas de operações para medir a integridade das atividades operacionais, como o tempo médio para detectar um incidente (MTTD) e o tempo médio de recuperação (MTTR) de um incidente. Avalie as métricas para determinar se as operações estão alcançando os resultados desejados e para entender a integridade das atividades de suas operações.

**Colete e analise métricas de operações.** Realize análises proativas regulares das métricas para identificar tendências e determinar onde são necessárias respostas adequadas. Você deve agregar dados de log da execução de suas atividades de operações e chamadas de API de operações em um serviço como o CloudWatch Logs. Gere métricas a partir de observações do conteúdo de log necessário para obter informações sobre o desempenho das atividades de operações.

**Estabeleça linhas de base de métricas de operações** para que as métricas forneçam valores esperados como base para comparação e identificação de atividades operacionais com desempenho abaixo ou acima do esperado.

**Aprenda os padrões de atividade esperados para as operações.** Estabeleça padrões de atividade de operações para identificar comportamentos anômalos, de modo que possa responder adequadamente, se necessário.

**Alerte quando os resultados das operações estiverem em risco.** Sempre que estiverem em risco, um alerta deve ser emitido e acionado. Os resultados das operações são qualquer atividade que ofereça suporte a uma carga de trabalho na produção. Isso inclui tudo, desde a implantação de novas versões de aplicações até a recuperação de uma interrupção. Os resultados operacionais devem ser tratados com a mesma importância que os resultados comerciais. As equipes de software devem identificar as principais métricas e atividades de operações e criar alertas para elas. Os alertas devem ser oportunos e acionáveis. Se um alerta for gerado, deverá ser incluída uma referência a um runbook ou playbook correspondente. Os alertas sem uma ação correspondente podem levar à fadiga de alertas.

**Alerte quando forem detectadas anomalias** nas operações para que você possa responder adequadamente, se necessário. A análise das métricas das operações ao longo do tempo pode estabelecer padrões de comportamento que podem ser quantificados o suficiente para definir um evento ou acionar um alarme em resposta.

**Valide a obtenção de resultados e a eficácia dos KPIs e métricas.** Crie uma visão comercial das atividades de operações para ajudar a determinar se você está atendendo às necessidades e a identificar as áreas que precisam ser aprimoradas para atingir as metas de negócios. Valide a eficácia dos KPIs e métricas e revise-os, se necessário.

Práticas recomendadas para compreensão da integridade operacional:

- Identificar principais indicadores de desempenho
- Definir métricas de operações
- Coletar e analisar métricas de operações
- Estabelecer linhas de base de métricas de operações
- Aprender os padrões de atividade esperados para as operações
- Alertar quando os resultados das operações estiverem em risco
- Alertar quando forem detectadas anomalias
- Validar a obtenção de resultados, a eficácia de KPIs e métricas

### 4.22 Responder a eventos

Você deve se antecipar aos eventos operacionais. Isso pode incluir eventos planejados, como promoções de vendas, implantações e testes de falhas. Eles também podem incluir eventos não planejados, como picos de utilização e falhas de componentes. Você deve usar seus runbooks e playbooks existentes para fornecer resultados consistentes ao responder aos alertas. Uma função ou uma equipe responsável pela resposta e pelos encaminhamentos deve ser responsável pelos alertas definidos. Você também deve conhecer o impacto comercial dos componentes do seu sistema e usá-lo para direcionar esforços quando necessário. Você deve realizar uma análise da causa-raiz após os eventos e, em seguida, evitar a recorrência de falhas ou documentar as soluções alternativas.

**Use um processo para gerenciamento de eventos, incidentes e problemas.** Sua organização deve ter processos para lidar com eventos, incidentes e problemas. Eventos são coisas que ocorrem em sua carga de trabalho, mas que talvez não precisem de intervenção. Incidentes são eventos que exigem intervenção. Os problemas são eventos recorrentes que exigem intervenção ou não podem ser resolvidos. Você precisa de processos para reduzir o impacto desses eventos em sua empresa e garantir uma resposta adequada.

**Tenha um processo por alerta.** Tenha uma resposta bem definida (runbook ou playbook), com um proprietário especificamente identificado, para qualquer evento para o qual você emita um alerta. Isso garante respostas eficazes e imediatas aos eventos operacionais e evita que eventos acionáveis sejam obscurecidos por notificações menos valiosas.

**Priorize eventos operacionais com base no impacto nos negócios.** Quando vários eventos exigirem intervenção, assegure-se de que os mais significativos para a empresa sejam tratados primeiro. Os impactos podem incluir mortes ou ferimentos, perdas financeiras ou danos à reputação ou à confiança.

**Defina caminhos de encaminhamento** em seus runbooks e playbooks, incluindo o gatilho do encaminhamento e os procedimentos para encaminhar. Identifique especificamente os proprietários de cada ação para garantir respostas eficazes e imediatas aos eventos operacionais. Identifique quando uma decisão humana é necessária antes de uma ação ser tomada. Trabalhe com os tomadores de decisão para que essa decisão seja tomada com antecedência e a ação seja pré-aprovada, a fim de evitar um longo tempo médio para reparo (MTTR), à espera de uma resposta.

**Defina um plano de comunicação com o cliente para interrupções de serviço.** Defina e teste um plano de comunicação confiável para manter seus clientes e stakeholders informados sobre interrupções do sistema. Comunique-se diretamente com seus usuários quando os serviços que eles usam forem afetados e quando os serviços voltarem ao normal.

**Comunique o status por meio de painéis.** Forneça painéis adaptados aos seus públicos-alvo, como equipes técnicas internas, liderança e clientes, para comunicar o status operacional atual dos negócios e fornecer métricas de interesse.

Por fim, **automatize as respostas aos eventos** para reduzir os erros causados por processos manuais e para garantir respostas rápidas e consistentes.

Práticas recomendadas para responder a eventos:

- Usar um processo para gerenciamento de eventos, incidentes e problemas
- Ter um processo por alerta
- Priorizar eventos operacionais com base no impacto nos negócios
- Definir caminhos de encaminhamento
- Definir um plano de comunicação com o cliente para interrupções de serviço
- Comunicar o status por meio de painéis
- Automatizar as respostas aos eventos

### 4.23 Evoluir

A evolução é o ciclo contínuo de aprimoramento ao longo do tempo. Implemente pequenas e frequentes mudanças incrementais com base nas lições aprendidas em suas atividades operacionais e avalie o sucesso dessas mudanças para obter melhorias.

### 4.24 Aprender, compartilhar e melhorar

É fundamental que você reserve periodicamente tempo para fazer análises das atividades operacionais, analisar falhas, experimentar e fazer melhorias. Em caso de falha, você deve garantir que a sua equipe, bem como a comunidade de engenharia mais ampla, aprenda com essas falhas. Você deve analisar as falhas para identificar as lições aprendidas e planejar melhorias. Você deverá analisar regularmente as lições aprendidas com outras equipes para validar suas informações.

**Tenha um processo de melhoria contínua.** Avalie sua carga de trabalho em relação às práticas recomendadas de arquitetura interna e externa. Realize revisões da carga de trabalho pelo menos uma vez por ano. Priorize as oportunidades de melhoria em sua cadência de desenvolvimento de software.

**Realize análise pós-incidente.** Analise os eventos que afetam o cliente e identifique os fatores contribuintes e as ações preventivas. Use essas informações para desenvolver mitigações para limitar ou evitar a recorrência. Desenvolva procedimentos para respostas rápidas e eficazes. Comunique os fatores que contribuíram para isso e as ações corretivas conforme apropriado, adaptadas aos públicos-alvo.

**Implante circuitos de feedback**, que podem fornecer informações acionáveis que orientam a tomada de decisões. Crie circuitos de feedback em seus procedimentos e cargas de trabalho. Assim, você pode identificar problemas e áreas que precisam ser melhoradas. Eles também validam os investimentos feitos em melhorias. Esses circuitos de feedback são a base para melhorar continuamente sua carga de trabalho.

**Execute gerenciamento do conhecimento.** O gerenciamento do conhecimento ajuda os membros da equipe a encontrar as informações para realizar seu trabalho. Nas organizações de aprendizagem, as informações são compartilhadas livremente, o que capacita os indivíduos. As informações podem ser descobertas ou pesquisadas. As informações são precisas e atualizadas. Existem mecanismos para criar novas informações, atualizar informações existentes e arquivar informações desatualizadas. O exemplo mais comum de uma plataforma de gerenciamento de conhecimento é um sistema de gerenciamento de conteúdo, como um Wiki.

**Defina os motivadores da melhoria** para ajudar você a avaliar e priorizar as oportunidades.

**Valide informações.** Analise os resultados e as respostas da sua análise com equipes multifuncionais e proprietários de negócios. Use essas análises para estabelecer um entendimento comum, identificar impactos adicionais e determinar cursos de ação. Ajuste as respostas conforme apropriado.

**Realize análises de métricas de operações** regularmente, com participantes de várias equipes de diferentes áreas da empresa. Use essas análises para identificar oportunidades de melhoria, possíveis cursos de ação e para compartilhar as lições aprendidas. Procure oportunidades de melhoria em todos os seus ambientes, como desenvolvimento, teste e produção.

**Documente e compartilhe as lições aprendidas** com as atividades de operações para que possa usá-las internamente e entre as equipes. Compartilhar o que suas equipes aprendem pode aumentar os benefícios em toda a organização. Convém compartilhar informações e recursos para impedir erros evitáveis e facilitar os esforços de desenvolvimento. Isso ajudará você a se concentrar no fornecimento dos recursos desejados.

Por fim, **aloque tempo para fazer melhorias**, dedicando tempo e recursos em seus processos para possibilitar melhorias incrementais contínuas.

Práticas recomendadas para aprender, compartilhar e melhorar:

- Ter um processo de melhoria contínua
- Realizar análise pós-incidente
- Implantar circuitos de feedback
- Executar gerenciamento do conhecimento
- Definir os motivadores da melhoria
- Validar informações
- Realizar análises de métricas de operações
- Documentar e compartilhar as lições aprendidas
- Alocar tempo para fazer melhorias

### 4.25 Pergunta 1

Quais das seguintes áreas representam as melhores práticas para o pilar de excelência operacional? (Selecione TRÊS.)

- A Eficiência de desempenho
- B Preparar
- C Relação custo/benefício
- D Organização
- E Segurança
- F Evoluir

**Resposta: B, D, F.** Preparar, Organização e Evoluir.

### 4.26 Pergunta 2

Qual destes é um princípio de design de excelência operacional?

- A Implementar uma base de identidade sólida.
- B Recuperar-se automaticamente de falhas.
- C Avaliar a eficiência geral.
- D Executar operações como código.

**Resposta: D.** Executar operações como código.

### 4.27 Resumo do Módulo 4

Neste módulo, você aprendeu sobre o pilar da excelência operacional. Iniciamos com uma visão geral e incluímos uma discussão aprofundada sobre a proposta de valor, os princípios de design e as práticas recomendadas do pilar de excelência operacional.

Neste módulo, você:

- Teve uma visão geral do pilar de excelência operacional
- Aprendeu sobre a proposta de valor para a excelência operacional
- Conheceu os diferentes princípios de design do pilar de excelência operacional
- As práticas recomendadas do pilar de excelência operacional

<a id="modulo-5"></a>

## Módulo 5 — Análise detalhada do pilar de segurança

### 5.1 Boas-vindas!

Boas-vindas ao módulo cinco do AWS Well-Architected: Análise detalhada do pilar de segurança.

### 5.2 Objetivos de aprendizado

Neste módulo você terá uma visão geral do pilar de segurança do AWS Well-Architected Framework. Você também aprenderá os princípios de design e as práticas recomendadas do pilar de segurança.

Neste módulo, você aprenderá sobre:

- Uma visão geral do pilar de segurança do AWS Well-Architected Framework
- Os princípios de design e as práticas recomendadas do pilar de segurança

### 5.3 Visão geral do pilar de segurança

Para começar, você terá uma visão geral do pilar de segurança.

### 5.4 Pilares do Well-Architected

Atualmente, há seis pilares do Well-Architected Framework: excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. Esses pilares são os fundamentos da arquitetura de suas soluções de tecnologia na nuvem. Este módulo se concentrará no pilar de segurança.

- **01 Excelência operacional**
- **02 Segurança**
- **03 Confiabilidade**
- **04 Eficiência de desempenho**
- **05 Otimização de custos**
- **06 Sustentabilidade**

### 5.5 O que é o pilar de segurança?

O pilar de segurança abrange a capacidade de proteger dados, sistemas e ativos na nuvem. Para operar sua carga de trabalho com segurança, você deve aplicar as práticas recomendadas abrangentes a todas as áreas de segurança.

> O pilar de segurança envolve a habilidade de proteger dados, sistemas e ativos para aproveitar as tecnologias de nuvem para melhorar sua segurança.

**Por que a segurança é importante para melhorar sua arquitetura?**

### 5.6 Princípios de design de segurança

Agora que você já sabe o que é o pilar de segurança, vai se aprofundar nos princípios de design do pilar de segurança.

### 5.7 Segurança

Na nuvem, vários princípios podem ajudar você a fortalecer a segurança da carga de trabalho.

**Implemente uma base sólida de identidade.** Você pode implementar o princípio de menor privilégio e aplicar a separação de tarefas com a autorização apropriada para cada interação com os recursos da AWS. Centralize o gerenciamento de identidades e tenha como meta eliminar a dependência de credenciais estáticas de longo prazo.

**Ative a rastreabilidade.** Você pode monitorar, alertar e fazer auditoria de ações e alterações em seu ambiente em tempo real. Integre a coleta de log e métricas com sistemas para investigar e tomar medidas automaticamente.

**Aplique a segurança em todas as camadas.** Aplique uma abordagem de defesa em profundidade com vários controles de segurança. Aplique controles a todas as camadas, como rede de borda, nuvem privada virtual (VPC), balanceamento de carga, instâncias de computação, sistemas operacionais, aplicações e código.

**Automatize as práticas de segurança.** Os mecanismos automatizados de segurança baseados em software melhoram a capacidade de dimensionar com segurança de modo mais rápido e econômico. Crie arquiteturas seguras, incluindo a implantação de controles definidos e gerenciados como código em modelos com controle de versão.

**Proteja dados em trânsito e em repouso.** Classifique seus dados em níveis de confidencialidade e use mecanismos como criptografia, tokenização e controle de acesso, conforme apropriado.

**Não divulgue dados** (mantenha as pessoas longe dos dados). Use mecanismos e ferramentas para reduzir ou eliminar a necessidade de acesso direto ou processamento manual de dados. Isso diminui o risco de manuseio incorreto ou erro humano com dados sigilosos.

Por fim, **prepare-se para eventos de segurança.** Prepare-se para um incidente tendo processos e uma política de investigação e gerenciamento de incidentes que estejam alinhados aos requisitos da organização. Execute simulações de resposta a incidentes e use ferramentas automatizadas para acelerar sua detecção, investigação e recuperação.

Os sete princípios de design de segurança:

1. 1Implementar uma base de identidade sólida
2. 2Ativar a rastreabilidade
3. 3Aplicar a segurança em todas as camadas
4. 4Automatizar as práticas recomendadas de segurança
5. 5Proteger dados em trânsito e em repouso
6. 6Manter as pessoas longe dos dados
7. 7Preparar-se para eventos de segurança

### 5.8 Práticas recomendadas de segurança

Agora que você entende os princípios de design de segurança, aprenderá sobre as práticas recomendadas de segurança.

### 5.9 Segurança

O pilar de segurança está agrupado em sete áreas de práticas recomendadas. Isso inclui fundamentos de segurança, Identity and Access Management, detecção, proteção de infraestrutura, proteção de dados, resposta a incidentes e segurança de aplicações.

Áreas de práticas recomendadas de segurança:

- Fundamentos de segurança
- Identity and Access Management
- Detecção
- Proteção de infraestrutura
- Proteção de dados
- Resposta a incidentes
- Segurança de aplicações

### 5.10 Fundamentos de segurança

Os fundamentos de segurança são a primeira área de práticas recomendadas de segurança.

### 5.11 Responsabilidade compartilhada

Segurança e conformidade são responsabilidades compartilhadas entre a AWS e o cliente. Esse modelo compartilhado pode auxiliar a reduzir os encargos operacionais do cliente à medida que a AWS opera, gerencia e controla os componentes do sistema operacional do host e a camada de virtualização até a segurança física das instalações em que o serviço opera. O cliente assume a responsabilidade e o gerenciamento do sistema operacional convidado (incluindo atualizações e patches de segurança) e de outros softwares de aplicações associados. O cliente também é responsável pela configuração do firewall do grupo de segurança da AWS.

Os clientes devem considerar com cuidado os serviços que escolherem. As responsabilidades variam de acordo com os serviços usados, a integração desses serviços no ambiente de TI e as leis e normas aplicáveis. A natureza dessas responsabilidades compartilhadas também fornece a flexibilidade e o controle do cliente necessários para a implantação.

Essa distinção entre responsabilidades é normalmente chamada de segurança "da" nuvem, em vez de segurança "na" nuvem. A **AWS é responsável pela segurança da nuvem**, protegendo a infraestrutura que executa todos os serviços oferecidos na nuvem AWS. Essa infraestrutura é composta por hardware, software, redes e instalações que executam o AWS Cloud Services. O **cliente é responsável pela segurança na nuvem**. A responsabilidade dele é determinada pela seleção dos AWS Cloud Services. Isso determina a quantidade de operações de configuração que o cliente deverá executar como parte de suas responsabilidades de segurança.

Por exemplo, um serviço como o Amazon Elastic Compute Cloud (Amazon EC2) é classificado como infraestrutura como serviço. Dessa forma, exige que o cliente execute todas as tarefas necessárias de configuração e gerenciamento de segurança. Os clientes que implantam uma instância do EC2 são responsáveis por gerenciar o sistema operacional convidado (incluindo atualizações e patches de segurança) e qualquer software ou utilitário de aplicações que instalarem nas instâncias. Eles também seriam responsáveis pela configuração do firewall fornecido pela AWS, ou grupo de segurança, em cada instância.

Para serviços abstraídos, como o Amazon Simple Storage Service (Amazon S3) e o Amazon DynamoDB, a AWS opera a camada de infraestrutura, o sistema operacional e as plataformas. Os clientes acessam os endpoints para armazenar e recuperar dados. São responsáveis por gerenciar os dados (incluindo opções de criptografia), classificar os ativos e usar as ferramentas do AWS IAM para aplicar as permissões apropriadas.

Modelo de responsabilidade compartilhada:

| Camada | Responsável |
| --- | --- |
| Dados do cliente | **Cliente** |
| Plataforma, aplicações, Identity & Access Management | **Cliente** |
| Configuração de sistema operacional, rede e firewall | **Cliente** |
| Autenticação da integridade de dados e criptografia de dados do cliente / Criptografia do lado do servidor / Proteção do tráfego de rede | **Cliente** |
| Software | **AWS** |
| Computação, armazenamento, banco de dados, redes | **AWS** |
| Infraestrutura global de hardware/AWS | **AWS** |
| Regiões, Zonas de Disponibilidade, Locais de Borda | **AWS** |

- ****Cliente**:** responsabilidade pela segurança "na" nuvem.
- ****AWS**:** responsabilidade pela segurança "da" nuvem.

### 5.12 Separação e gerenciamento de contas da AWS

É uma prática recomendada organizar as cargas de trabalho em contas separadas e contas de grupo. Isso pode ser baseado na função, nos requisitos de conformidade ou em um conjunto comum de controles, em vez de espelhar a estrutura de relatórios da sua organização. Na AWS, as contas são um limite rígido. Por exemplo, a separação em nível de conta é altamente recomendada para isolar as cargas de trabalho de produção das cargas de trabalho de desenvolvimento e teste.

Você deve gerenciar contas, definir controles e configurar serviços e recursos de forma centralizada. Para separar as cargas de trabalho usando contas, você pode estabelecer proteções comuns e isolamento entre ambientes (como produção, desenvolvimento e teste) e cargas de trabalho por meio de uma estratégia de várias contas. A separação em nível de conta é altamente recomendada porque fornece um limite de isolamento forte para segurança, faturamento e acesso.

Você também deve **proteger o usuário-raiz e as propriedades da conta**. O usuário-raiz é o usuário mais privilegiado em uma conta AWS, com acesso administrativo total a todos os recursos da conta. Em alguns casos, ele não pode ser limitado por políticas de segurança. Você pode tomar as seguintes medidas para ajudar a reduzir o risco de exposição inadvertida de credenciais-raiz e o subsequente comprometimento do ambiente de nuvem: desative o acesso programático ao usuário-raiz, estabeleça controles apropriados para o usuário-raiz e evite o seu uso rotineiro.

Práticas recomendadas para separação e gerenciamento de contas da AWS:

- Separar cargas de trabalho usando contas
- Proteger usuário-raiz e propriedades de contas

### 5.13 Operar suas cargas de trabalho com segurança

Para operar sua carga de trabalho com segurança, você deve aplicar as práticas recomendadas abrangentes a todas as áreas de segurança. Utilize os requisitos e processos definidos na excelência operacional em nível organizacional e de carga de trabalho e aplique-os a todas as áreas. Manter-se atualizado com as recomendações da AWS e do setor e com a inteligência sobre ameaças ajuda a desenvolver o seu modelo de ameaças e os objetivos de controle. Automatizar processos de segurança, testes e validação ajuda a dimensionar suas operações de segurança.

**Identifique e valide os objetivos de controle.** Com base nos requisitos de conformidade e nos riscos identificados no modelo de ameaças, obtenha e valide os objetivos de controle e os controles que você precisa aplicar à sua carga de trabalho. A validação contínua de objetivos de controle e controles ajuda a medir a eficácia da mitigação de riscos.

**Mantenha-se atualizado sobre as ameaças de segurança.** Para ajudar você a definir e implementar controles adequados, reconheça os vetores de ataque mantendo-se atualizado com as ameaças de segurança mais recentes.

**Mantenha-se atualizado sobre as recomendações de segurança** da AWS e do setor para aprimorar o procedimento de segurança de sua carga de trabalho.

**Automatize testes e validação de controles de segurança em pipelines.** Estabeleça linhas de base e modelos seguros para mecanismos de segurança que são testados e validados como parte de sua construção, pipelines e processos. Use ferramentas e automação para testar e validar continuamente todos os controles de segurança.

**Identifique as ameaças e priorize as atenuações usando um modelo de ameaças.** Realize a modelagem de ameaças para identificar e manter um registro atualizado de possíveis ameaças e atenuações associadas à sua carga de trabalho. Priorize ameaças e adapte mitigações de controle de segurança para prevenir, detectar e responder. Revisite-as e mantenha-as no contexto de sua carga de trabalho e do cenário de segurança em evolução.

**Avalie e implemente novos serviços e recursos de segurança regularmente.** Avalie e implemente serviços e recursos de segurança da AWS e dos parceiros da AWS para ajudar você a aprimorar o procedimento de segurança de sua carga de trabalho.

Práticas recomendadas para operar suas cargas de trabalho com segurança:

- Identifique e valide os objetivos de controle
- Mantenha-se atualizado sobre as ameaças de segurança
- Mantenha-se atualizado sobre as recomendações de segurança
- Automatize testes e validação de controles de segurança em pipelines
- Identifique as ameaças e priorize as atenuações usando um modelo de ameaças
- Avalie e implemente novos serviços e recursos de segurança regularmente

### 5.14 Identity and Access Management

A próxima área de práticas recomendadas de segurança é o Identity and Access Management. Para usar os serviços da AWS, você deve conceder aos seus usuários e aplicações acesso aos recursos nas suas contas AWS. À medida que você executa mais cargas de trabalho na AWS, precisa de gerenciamento de identidade e permissões robustos para garantir que as pessoas certas tenham acesso aos recursos certos nas condições certas.

A AWS oferece uma grande variedade de recursos para ajudar você a gerenciar suas identidades humanas e de máquina e suas permissões. As práticas recomendadas para esses recursos se enquadram em duas áreas principais: gerenciamento de identidade e gerenciamento de permissões.

- Gerenciamento de identidade
- Gerenciamento de permissões

### 5.15 Gerenciamento de identidades

Há dois tipos de identidades que você precisa gerenciar ao abordar como operar cargas de trabalho seguras da AWS.

Primeiro, as **identidades humanas**: os administradores, desenvolvedores, operadores e consumidores das suas aplicações precisam de uma identidade para acessar seus ambientes e aplicações AWS. Elas podem ser membros da sua organização ou usuários externos com os quais você colabora. Elas interagem com seus recursos da AWS por meio de um navegador da web, uma aplicação cliente, um aplicativo móvel ou ferramentas interativas de linha de comando.

Segundo, as **identidades de máquina**: suas aplicações de carga de trabalho, ferramentas operacionais e componentes exigem uma identidade para fazer solicitações aos serviços da AWS, como ler dados. Essas identidades incluem máquinas em execução em seu ambiente AWS, como instâncias do EC2 ou funções do AWS Lambda. Você também pode gerenciar identidades de máquinas para partes externas que precisam de acesso. Além disso, você pode ter máquinas fora da AWS que precisam de acesso ao seu ambiente AWS.

**Use mecanismos de login fortes.** Autenticação com credenciais de login pode apresentar riscos quando não são usados mecanismos como a autenticação multifator (MFA). Isso é verdadeiro em situações em que as credenciais de login foram divulgadas inadvertidamente ou são facilmente adivinhadas. Os mecanismos de login podem ajudar a reduzir esses riscos, exigindo MFA e políticas de senhas fortes.

**Utilize credenciais temporárias** para autenticação em vez de credenciais de longo prazo. Isso ajuda a reduzir ou eliminar riscos, como a divulgação, o compartilhamento ou o roubo inadvertido de credenciais.

**Armazene e use segredos com segurança.** Uma carga de trabalho requer um recurso automatizado para comprovar a identidade em bancos de dados, recursos e serviços de terceiro. Isso é feito usando credenciais de acesso secretas, como chaves de acesso à API, senhas e tokens OAuth. O uso de um serviço criado para armazenar, gerenciar e trocar essas credenciais ajuda a reduzir a probabilidade de que elas sejam comprometidas.

**Conte com um provedor de identidade centralizado.** Para as identidades da força de trabalho, conte com um provedor de identidade que o ajude a gerenciar identidades em um local centralizado. Isso facilita o gerenciamento do acesso em várias aplicações e serviços porque você está criando, gerenciando e revogando o acesso a partir de um único local.

**Realize auditorias e troque as credenciais periodicamente** para limitar o tempo que as credenciais podem ser usadas para acessar seus recursos. As credenciais de longo prazo criam muitos riscos, e esses riscos podem ser reduzidos com a troca regular das credenciais de longo prazo.

**Configure grupos e atributos de usuários.** À medida que o número de usuários que você gerencia aumenta, será necessário determinar maneiras de organizá-los para que possa gerenciá-los de forma dimensionada. Coloque os usuários com requisitos de segurança comuns em grupos definidos pelo seu provedor de identidade. Implemente mecanismos para garantir que os atributos do usuário que podem ser usados para controle de acesso, como departamento ou local, estejam corretos e atualizados. Use esses grupos e atributos para controlar o acesso em vez de usuários individuais. Isso ajuda a gerenciar o acesso de forma centralizada, alterando a associação ao grupo ou os atributos de um usuário uma vez com um conjunto de permissões. Evita-se a necessidade de atualizar muitas políticas individuais quando o acesso de um usuário precisa ser alterado.

Práticas recomendadas para gerenciamento de identidades:

- Usar mecanismos de login fortes
- Utilizar credenciais temporárias
- Armazenar e usar segredos com segurança
- Contar com um provedor de identidade centralizado
- Realizar auditorias e trocar as credenciais periodicamente
- Configurar grupos e atributos de usuários

### 5.16 Gerenciamento de permissões

Gerencie as permissões para controlar o acesso a identidades humanas e de máquinas que exigem acesso à AWS e às suas cargas de trabalho. As permissões controlam quem pode acessar o que e em que condições. Defina permissões para identidades humanas e de máquina específicas para conceder acesso a ações de serviço específicas em recursos específicos. Além disso, especifique as condições que devem ser verdadeiras para que o acesso seja concedido. Por exemplo, você pode permitir que os desenvolvedores criem novas funções Lambda, mas somente em uma Região específica.

**Defina os requisitos de acesso.** Cada componente ou recurso de sua carga de trabalho precisa ser acessado por administradores, usuários finais ou outros componentes. Tenha uma definição clara de quem ou o que deve ter acesso a cada componente. Escolha o tipo de identidade adequado e o método de autenticação e autorização.

**Conceda acesso de menor privilégio.** Recomenda-se conceder apenas o acesso necessário para que as identidades realizem ações específicas em recursos específicos sob condições específicas. Use atributos de grupo e identidade para definir dinamicamente as permissões de acordo com suas dimensões, em vez de definir permissões para usuários individuais. Por exemplo, você pode permitir que um grupo de desenvolvedores tenha acesso para gerenciar apenas os recursos de seu projeto. Dessa forma, se um desenvolvedor deixar o projeto, o acesso dele será automaticamente revogado sem alterar as políticas de acesso subjacentes.

**Estabeleça um processo de acesso de emergência** para o caso improvável de um processo automatizado ou problema no pipeline. Isso ajudará você a contar com o acesso de menor privilégio, mas garantirá que os usuários possam obter o nível certo de acesso quando necessário.

**Reduza as permissões continuamente.** À medida que as equipes e as cargas de trabalho determinam o acesso de que precisam, remova as permissões que não são mais usadas e estabeleça processos de revisão para obter permissões de privilégio mínimo. Reduza e monitore as identidades e permissões não utilizadas.

**Defina barreiras de proteção de permissões para sua organização** e estabeleça controles comuns que restrinjam o acesso a todas as identidades da sua organização.

**Gerencie o acesso com base no ciclo de vida.** Integre os controles de acesso ao ciclo de vida do operador e da aplicação e ao seu provedor de federação centralizado.

**Analise o acesso público e entre contas.** Monitore continuamente as descobertas que destacam o acesso público e entre contas. Reduza o acesso público e o acesso entre contas a apenas recursos que exigem esse tipo de acesso.

**Compartilhe recursos de forma segura em sua organização.** Com o aumento do número de cargas de trabalho, talvez seja necessário compartilhar o acesso aos recursos nessas cargas de trabalho ou provisionar os recursos várias vezes em várias contas. Você pode ter construções para compartimentar seu ambiente, como ambientes de desenvolvimento, teste e produção. No entanto, ter construções de separação não impede você de compartilhar com segurança. Ao compartilhar componentes que se sobrepõem, é possível reduzir a sobrecarga operacional e criar uma experiência consistente sem adivinhar o que pode ter perdido ao criar o mesmo recurso várias vezes.

**Compartilhe recursos de forma segura com um terceiro.** A segurança de seu ambiente de nuvem não se limita à sua organização. Sua organização pode confiar em um terceiro para gerenciar uma parte de seus dados. O gerenciamento de permissões para o sistema gerenciado por terceiros deve seguir a prática de acesso just-in-time usando o princípio de menor privilégio com credenciais temporárias. Ao trabalhar em conjunto com um terceiro, você pode reduzir o escopo do impacto e o risco de acesso não intencional.

Práticas recomendadas para gerenciamento de permissões:

- Definir os requisitos de acesso
- Conceder acesso de menor privilégio
- Estabelecer um processo de acesso de emergência
- Reduzir as permissões continuamente
- Definir barreiras de proteção de permissões para sua organização
- Gerenciar o acesso com base no ciclo de vida
- Analisar o acesso público e entre contas
- Compartilhar recursos de forma segura em sua organização
- Compartilhar recursos de forma segura com um terceiro

### 5.17 Detecção

A próxima área de práticas recomendadas de segurança é a detecção. Você pode usar controles de detecção para identificar uma ameaça ou incidente de segurança potencial. Eles são parte essencial das estruturas de governança e podem ser usados para dar suporte a um processo de qualidade, a uma obrigação legal ou de conformidade e para esforços de identificação e resposta a ameaças.

### 5.18 Detecção

A detecção consiste em duas partes: detecção de alterações inesperadas ou indesejadas na configuração e detecção de comportamento inesperado. A detecção ajuda você a identificar uma possível configuração incorreta da segurança, uma ameaça ou um comportamento inesperado. Trata-se de parte essencial do ciclo de vida da segurança e pode ser usada para dar suporte a um processo de qualidade, a uma obrigação legal ou de conformidade e para esforços de identificação e resposta a ameaças. Para a AWS, há várias abordagens que você pode usar ao tratar de mecanismos de detecção.

**Configure o registro em log de serviços e aplicações.** Retenha os logs de eventos de segurança de serviços e aplicações. Esse é um princípio fundamental de segurança para auditoria, investigações e casos de uso operacional. É um requisito de segurança comum orientado por governança, risco e conformidade (GRC), padrões, políticas e procedimentos.

**Analise logs, descobertas e métricas de modo central.** As equipes de operações de segurança dependem da coleta de logs e do uso de ferramentas de pesquisa para descobrir possíveis eventos de interesse que possam indicar atividade não autorizada ou alteração não intencional. No entanto, a simples análise dos dados coletados e o processamento manual das informações são insuficientes para acompanhar o volume de informações que flui de arquiteturas complexas. A análise e os relatórios, por si só, não facilitam a atribuição dos recursos certos para trabalhar em um evento em tempo hábil.

**Automatize as respostas aos eventos.** O uso da automação para investigar e corrigir eventos reduz o esforço e o erro humano e ajuda a dimensionar os recursos de investigação. Por meio de revisões regulares, você pode ajustar as ferramentas de automação e iterar continuamente.

Por fim, **implemente eventos de segurança acionáveis.** Crie alertas que são enviados e podem ser acionados pela sua equipe. Garanta que os alertas incluam informações relevantes para que a equipe tome providências. Para cada mecanismo de detecção que tiver, você também deve ter um processo, na forma de um runbook ou playbook, para investigar.

Práticas recomendadas de detecção:

- Configurar o registro em log de serviços e aplicações
- Analisar logs, descobertas e métricas de modo central
- Automatizar as respostas aos eventos
- Implementar eventos de segurança acionáveis

### 5.19 Proteção de infraestrutura

A próxima área de práticas recomendadas de segurança é a proteção da infraestrutura. A proteção da infraestrutura abrange metodologias de controle, como defesa em profundidade, necessárias para atender às práticas recomendadas e às obrigações organizacionais ou regulatórias. O uso dessas metodologias é fundamental para o sucesso das operações contínuas na nuvem.

A proteção da infraestrutura é uma parte fundamental de um programa de segurança da informação. Ela garante que os sistemas e recursos em suas cargas de trabalho sejam protegidos contra acesso não intencional, não autorizado e outras possíveis vulnerabilidades.

### 5.20 Proteção de redes

Os usuários, tanto da sua força de trabalho quanto de seus clientes, podem estar localizados em qualquer lugar. Você precisa abandonar os modelos tradicionais de confiar em qualquer pessoa e em qualquer coisa que tenha acesso à sua rede. Quando você segue o princípio de aplicar a segurança em todas as camadas, emprega uma abordagem Zero Trust. A segurança Zero Trust é um modelo em que os componentes da aplicação ou os microsserviços são considerados distintos uns dos outros, e nenhum componente ou microsserviço confia em outro.

**Crie camadas de rede.** Agrupe os componentes que compartilham requisitos de confidencialidade em camadas para minimizar o escopo potencial do impacto do acesso não autorizado.

**Controle o tráfego em todas as camadas.** Ao arquitetar a topologia da rede, você deve examinar os requisitos de conectividade de cada componente.

**Automatize a proteção de rede** para fornecer uma rede autodefensiva com base na inteligência contra ameaças e na detecção de anomalias.

Por fim, **implemente inspeção e proteção.** Inspecione e filtre seu tráfego em cada camada.

Práticas recomendadas para proteção de redes:

- Criar camadas de rede
- Controlar o tráfego em todas as camadas
- Automatizar a proteção de rede
- Implementar inspeção e proteção

### 5.21 Proteção de computação

Os recursos de computação incluem instâncias do Amazon EC2, contêineres, funções do AWS Lambda, serviços de banco de dados, dispositivos da Internet das Coisas (IoT) e muito mais. Cada tipo de recurso exige abordagens próprias de proteção, mas todos compartilham estratégias importantes: defesa em profundidade, gerenciamento de vulnerabilidades, redução da superfície de ataque, automação da configuração e operação e execução de ações à distância.

Nesta seção, são apresentadas orientações gerais para proteger recursos de computação nos principais serviços. Para cada serviço AWS utilizado, verifique também as recomendações de segurança específicas na documentação do serviço.

**Realize o gerenciamento de vulnerabilidades.** Examine e corrija regularmente as vulnerabilidades no código, nas dependências e na infraestrutura para ajudar a proteger a carga de trabalho contra novas ameaças.

**Minimize a superfície de ataque.** Limite a exposição a acessos indesejados fortalecendo os sistemas operacionais e reduzindo os componentes, as bibliotecas e os serviços expostos externamente.

**Implemente serviços gerenciados.** Utilize serviços que gerenciam recursos, como o Amazon Relational Database Service (Amazon RDS), o Lambda e o Amazon Elastic Container Service (Amazon ECS). Isso reduz as tarefas de manutenção de segurança sob sua responsabilidade no modelo de responsabilidade compartilhada.

**Automatize a proteção da computação.** Automatize o gerenciamento de vulnerabilidades, a redução da superfície de ataque e o gerenciamento de recursos. A automação libera tempo para proteger outros aspectos da carga de trabalho e reduz o risco de erro humano.

**Ajude as pessoas a realizar ações à distância.** Remover a necessidade de acesso interativo reduz o risco de erro humano e a possibilidade de configurações ou gerenciamento manuais inadequados.

**Valide a integridade do software.** Implemente mecanismos como assinatura de código para confirmar que o software, o código e as bibliotecas utilizados pela carga de trabalho são de fontes confiáveis e não foram adulterados.

Práticas recomendadas para proteção de computação:

- Realizar o gerenciamento de vulnerabilidades
- Minimizar a superfície de ataque
- Implementar serviços gerenciados
- Automatizar a proteção da computação
- Ajudar as pessoas a realizar ações à distância
- Validar a integridade do software

### 5.22 Proteção de dados

A próxima área de práticas recomendadas de segurança é a proteção de dados. Antes de arquitetar qualquer carga de trabalho, as práticas fundamentais que influenciam a segurança devem estar em vigor.

Por exemplo, a classificação de dados oferece uma maneira de categorizar os dados com base em níveis de confidencialidade. A criptografia protege os dados, tornando-os inacessíveis para quem não tem autorização. Esses métodos são importantes porque apoiam objetivos como limitar o manuseio incorreto de dados ou ajudar a cumprir obrigações regulatórias.

Na AWS, há várias abordagens diferentes para tratar a proteção de dados. As seções a seguir descrevem como utilizar essas abordagens.

### 5.23 Classificação de dados

A classificação de dados permite categorizar os dados organizacionais conforme sua criticidade e confidencialidade. Isso ajuda a determinar os controles adequados de proteção e retenção.

É fundamental entender o tipo e a classificação dos dados processados pela carga de trabalho, os processos associados, onde os dados são armazenados e quem é seu proprietário. Também é necessário conhecer as normas de conformidade aplicáveis e quais controles de dados devem ser usados.

Identificar os dados é a primeira etapa da jornada de classificação. Em seguida, defina os controles de proteção conforme o nível de classificação. Automatizar a identificação e a classificação ajuda a implementar os controles corretos, reduzindo o risco de erro humano e exposição decorrente do acesso direto de uma pessoa.

Defina também o gerenciamento do ciclo de vida dos dados. A estratégia deve considerar o nível de confidencialidade, requisitos legais e organizacionais, duração da retenção, processos de destruição, gerenciamento de acesso, transformação e compartilhamento dos dados.

Práticas recomendadas para classificação de dados:

- Identificar dados em sua carga de trabalho
- Definir controles de proteção de dados
- Automatizar a identificação e classificação
- Definir o gerenciamento do ciclo de vida de dados

### 5.24 Proteger dados em repouso

Dados em repouso são aqueles persistidos em armazenamento volátil ou não volátil durante qualquer período da carga de trabalho. Isso inclui armazenamento em bloco, de objetos, bancos de dados, arquivos, dispositivos de IoT e outras mídias que mantenham os dados.

A proteção desses dados reduz o risco de acesso não autorizado quando há criptografia e controles de acesso apropriados. Considere as práticas a seguir para protegê-los.

**Implemente o gerenciamento seguro de chaves.** Defina uma abordagem de criptografia que inclua o gerenciamento, a alternância e o controle de acesso às chaves. Isso ajuda a proteger o conteúdo contra usuários não autorizados e a reduzir a exposição desnecessária para usuários autorizados.

**Aplique a criptografia em repouso.** Use a criptografia para dados em repouso a fim de manter sua confidencialidade contra acesso não autorizado ou divulgação acidental.

**Automatize a proteção dos dados em repouso.** Use ferramentas automatizadas para validar e aplicar continuamente os controles de proteção de dados em repouso.

**Aplique o controle de acesso.** Proteja os dados impondo controles de acesso, gerenciamento de identidade e o princípio do menor privilégio. Evite a concessão de acesso público aos dados.

**Use mecanismos para manter as pessoas longe dos dados.** Mantenha os usuários afastados do acesso direto a sistemas e dados sigilosos em circunstâncias operacionais normais.

Práticas recomendadas para proteger dados em repouso:

- Implementar gerenciamento seguro de chaves
- Aplicar a criptografia em repouso
- Automatizar a proteção dos dados em repouso
- Aplicar controle de acesso
- Usar mecanismos para manter as pessoas longe dos dados

### 5.25 Proteger dados em trânsito

Dados em trânsito são quaisquer dados enviados de um sistema para outro. Isso inclui a comunicação entre os recursos da carga de trabalho, entre outros serviços e com os usuários finais. A proteção desses dados preserva a confidencialidade e a integridade das informações da carga de trabalho.

**Implemente o gerenciamento seguro de chaves e certificados.** Armazene chaves de criptografia e certificados de forma segura, faça sua alternância em intervalos adequados e aplique controles de acesso rigorosos.

**Imponha a criptografia em trânsito.** Defina os requisitos de criptografia com base nas políticas, obrigações regulatórias e padrões da organização. Use protocolos criptografados ao transmitir dados sigilosos para fora da VPC; a criptografia preserva a confidencialidade mesmo quando os dados passam por redes não confiáveis.

**Automatize a detecção de acesso não intencional aos dados.** Use ferramentas como o Amazon GuardDuty para detectar automaticamente atividades suspeitas ou tentativas de movimentação de dados que excedam os limites definidos.

**Autentique comunicações de rede.** Verifique a identidade das comunicações usando protocolos compatíveis com autenticação, como Transport Layer Security (TLS) ou IPsec.

Práticas recomendadas para proteger dados em trânsito:

- Implementar o gerenciamento seguro de chaves e certificados
- Impor criptografia em trânsito
- Automatizar a detecção de acesso não intencional aos dados
- Autenticar comunicações de rede

### 5.26 Resposta a incidentes

A próxima área de práticas recomendadas de segurança é a resposta a incidentes. Mesmo com controles de prevenção e detecção extremamente desenvolvidos, a organização ainda precisa implementar processos para responder a incidentes de segurança e mitigar seu impacto potencial.

A arquitetura da carga de trabalho afeta diretamente a capacidade das equipes de operar com eficiência durante um incidente, isolar ou conter os sistemas afetados e restaurar as operações para um estado bom conhecido.

### 5.27 Objetivos de design da resposta à nuvem

Os processos e mecanismos gerais de resposta a incidentes, como os definidos no NIST SP 800-61 *Computer Security Incident Handling Guide*, são importantes. Em ambientes de nuvem, avalie também os seguintes objetivos de design para responder a incidentes de segurança.

**Estabeleça objetivos de resposta.** Trabalhe com as partes interessadas, a assessoria jurídica e a liderança organizacional para definir o objetivo da resposta a um incidente. Objetivos comuns incluem conter e mitigar o problema, recuperar os recursos afetados, preservar dados para análise forense e atribuição.

**Documente os planos.** Crie planos que auxiliem a responder, comunicar-se durante e recuperar-se de um incidente.

**Responda usando a nuvem.** Implemente os padrões de resposta onde o evento e os dados ocorrem.

**Saiba o que você tem e do que você precisa.** Preserve adequadamente logs, snapshots e outras evidências, copiando-os para uma conta de nuvem de segurança centralizada. Use tags, metadados e mecanismos que imponham políticas de retenção. Por exemplo, é possível usar o comando `dd` do Linux, ou um equivalente do Windows, para gerar uma cópia completa dos dados para investigação.

**Use mecanismos de reimplantação.** Se uma anomalia de segurança for causada por uma configuração incorreta, a correção pode ser tão rápida quanto remover a variação e reimplantar os recursos com a configuração adequada. Sempre que possível, torne os mecanismos de resposta seguros para execução repetida e em ambientes com estado desconhecido.

**Automatize sempre que possível.** Quando houver problemas ou incidentes recorrentes, crie mecanismos para fazer a triagem programática e responder às situações comuns. Reserve a resposta humana para incidentes únicos, novos e sigilosos.

**Escolha soluções dimensionáveis.** Faça com que a abordagem organizacional acompanhe a escala da computação em nuvem e reduza o tempo entre a detecção e a resposta.

**Aprenda e melhore seu processo.** Ao identificar lacunas nos processos, nas ferramentas ou nas pessoas, implemente planos para corrigi-las. Simulações são formas seguras de encontrar lacunas e aprimorar o processo.

Objetivos de design da resposta à nuvem:

- Estabelecer objetivos de resposta
- Documentar planos
- Responder usando a nuvem
- Saber o que você tem e do que você precisa
- Usar mecanismos de reimplantação
- Automatizar sempre que possível
- Escolher soluções dimensionáveis
- Aprender e melhorar seu processo

### 5.28 Instruir

Processos automatizados permitem que as organizações dediquem mais tempo a medidas que aumentam a segurança das cargas de trabalho. A resposta automatizada a incidentes também libera as pessoas para correlacionar eventos, praticar simulações, elaborar procedimentos de resposta, realizar pesquisas, desenvolver habilidades e testar ou criar ferramentas.

Mesmo com mais automação, equipes, especialistas e respondentes de segurança precisam de educação contínua. Considere as seguintes áreas ao capacitar suas equipes.

**Habilidades de desenvolvimento.** Capacitar profissionais de segurança em programação acelera os esforços de automação. Isso inclui linguagens como Python, sistemas de controle de origem e versão e processos de integração e entrega contínuas (CI/CD). Esses conhecimentos aumentam a eficiência e reduzem erros durante a automação.

**Serviços AWS.** Treine a equipe para utilizar os serviços de segurança oferecidos pela AWS. Conhecer as ferramentas de nuvem reduz o tempo de resposta e aumenta a confiança da equipe. Estabeleça uma cadência de aprendizado sobre novos serviços e recursos, pois tanto o cenário de ameaças quanto as ferramentas evoluem continuamente.

**Conscientização de aplicações.** Treine a equipe de resposta a incidentes sobre as particularidades das cargas de trabalho e dos ambientes sob sua responsabilidade: logs emitidos, conteúdo dos registros, fluxo de tráfego da aplicação e mecanismos de autenticação e autorização utilizados. O conhecimento profundo da infraestrutura e das aplicações fornece uma vantagem importante para protegê-las.

A prática é a melhor forma de aprender. Dias de teste de resposta a incidentes ajudam os especialistas a aperfeiçoar ferramentas e técnicas enquanto transmitem conhecimento a outras pessoas. Mantenha também o treinamento necessário para toda a organização: a conscientização sobre segurança é uma linha importante de defesa, e todos os usuários devem saber reportar comportamentos suspeitos para investigação.

Áreas de instrução para equipes de segurança:

- Habilidades de desenvolvimento
- Serviços AWS
- Conscientização de aplicações

### 5.29 Preparar, simular, iterar

Durante um incidente, as equipes de resposta precisam acessar diversas ferramentas e recursos da carga de trabalho afetada. Garanta que tenham acesso pré-provisionado para executar suas tarefas antes de um evento ocorrer. Ferramentas, acessos e planos devem ser documentados e testados para assegurar uma resposta oportuna.

**Identifique os principais funcionários e recursos externos.** Relacione o pessoal interno e externo, os recursos e as obrigações legais que ajudarão a organização a responder a um incidente.

**Desenvolva planos de gerenciamento de incidentes.** Crie planos que orientem a resposta, a comunicação durante o evento e a recuperação posterior.

**Prepare recursos forenses.** Os respondentes precisam saber quando e como a investigação forense se encaixa no plano de resposta. Defina as evidências a coletar e as ferramentas a utilizar, preparando especialistas externos, ferramentas e automações adequados.

**Pré-provisione o acesso.** Verifique se os respondentes têm na AWS o acesso correto antes de um incidente. Isso reduz o tempo entre a investigação e a recuperação.

**Automatize recursos de contenção e recuperação.** Após criar e praticar os processos e ferramentas dos playbooks, transforme sua lógica em soluções baseadas em código. Isso permite que vários respondentes automatizem a resposta, eliminando variações e suposições. Em seguida, automatize esse código para ser acionado por alertas ou eventos, criando uma resposta orientada por eventos e adicionando automaticamente dados relevantes aos sistemas de segurança. Por exemplo, tráfego de um endereço IP indesejado pode incluir automaticamente esse IP em uma lista de bloqueio do AWS WAF ou em um grupo de regras do AWS Network Firewall.

**Implante ferramentas antecipadamente.** Disponibilize previamente na AWS as ferramentas adequadas para a equipe de segurança, reduzindo o tempo de investigação e recuperação.

**Realize dias de teste.** Simulações ou exercícios internos permitem praticar os planos e procedimentos de gerenciamento de incidentes em cenários realistas. Os profissionais devem usar as mesmas ferramentas e técnicas que utilizariam em um incidente real; os exercícios podem inclusive imitar ambientes do mundo real. O objetivo é estar preparado e melhorar continuamente a capacidade de resposta.

Práticas recomendadas para preparar, simular e iterar:

- Identificar os principais funcionários e recursos externos
- Desenvolver planos de gerenciamento de incidentes
- Preparar recursos forenses
- Pré-provisionar acesso
- Automatizar recursos de contenção
- Implantar ferramentas antecipadamente
- Realizar dias de teste

### 5.30 Segurança de aplicações

A última área de práticas recomendadas de segurança é a segurança de aplicações. A segurança é um tema que abrange todas as áreas da tecnologia. Até aqui, foram abordadas identidade, proteção de infraestrutura, proteção de dados e resposta a incidentes. A seguir, são apresentadas as práticas de segurança de aplicações.

### 5.31 Segurança de aplicações

O treinamento de pessoas, os testes automatizados, a compreensão das dependências e a validação das propriedades de segurança de ferramentas e aplicações ajudam a reduzir a probabilidade de problemas de segurança em cargas de trabalho de produção.

**Treine para a segurança de aplicações.** Ofereça treinamento aos desenvolvedores sobre práticas comuns para desenvolver e operar aplicações com segurança. Adotar práticas de desenvolvimento com foco em segurança reduz a probabilidade de problemas serem descobertos apenas na revisão de segurança.

**Automatize os testes durante todo o ciclo de vida de desenvolvimento e lançamento.** Automatize os testes das propriedades de segurança ao longo de todo o ciclo. Isso identifica de maneira consistente e repetitiva possíveis problemas antes do lançamento e reduz o risco no software entregue.

**Realize testes regulares de penetração.** Testes de penetração ajudam a encontrar problemas que testes automatizados ou revisão manual de código não detectam, além de avaliar a eficácia dos controles de detecção. Eles devem verificar se o software pode ser executado de formas inesperadas, por exemplo, expondo dados protegidos ou concedendo permissões mais amplas que o esperado.

**Execute análises manuais de código.** Revise manualmente o código produzido para garantir que quem o escreveu não seja a única pessoa a verificar sua qualidade.

**Centralize serviços para pacotes e dependências.** Forneça serviços centralizados para que as equipes obtenham pacotes de software e outras dependências. Isso valida os pacotes antes de incorporá-los ao software e fornece uma fonte de dados para análise de software.

**Implante software de forma programática.** Sempre que possível, adote implantações programáticas. Essa abordagem reduz a chance de falha na implantação ou de introdução de problemas inesperados por erro humano.

**Avalie regularmente as propriedades de segurança das pipelines.** Aplique os princípios do pilar de segurança do AWS Well-Architected às pipelines, com atenção especial à separação de permissões. Avalie regularmente as propriedades de segurança da infraestrutura de pipeline, pois seu gerenciamento eficaz ajuda a garantir a segurança do software entregue por elas.

**Crie um programa que incorpore a propriedade da segurança nas equipes de carga de trabalho.** Capacite as equipes de construtores a tomar decisões de segurança sobre o software que criam. A equipe de segurança ainda deve validá-las em uma revisão, mas a propriedade distribuída resulta em cargas de trabalho mais rápidas e seguras e incentiva uma cultura que melhora a operação dos sistemas.

Práticas recomendadas para segurança de aplicações:

- Treinar para a segurança de aplicações
- Automatizar os testes durante todo o ciclo de vida de desenvolvimento e lançamento
- Realizar testes regulares de penetração
- Executar análises manuais de código
- Centralizar serviços para pacotes e dependências
- Implantar software de forma programática
- Avaliar regularmente as propriedades de segurança das pipelines
- Criar um programa que incorpore a propriedade da segurança nas equipes de carga de trabalho

### 5.32 Pergunta 1

Por que a segurança é importante na arquitetura de nuvem?

- A Para operar uma carga de trabalho com segurança, é importante aplicar práticas recomendadas abrangentes a todas as áreas de segurança.
- B A criptografia de envelopes torna tudo mais seguro.
- C Sem garantir a economia de custos, o negócio não será viável.
- D Ninguém usará a aplicação se ela não for segura.

**Resposta: A.** Para operar uma carga de trabalho com segurança, é importante aplicar práticas recomendadas abrangentes a todas as áreas de segurança.

### 5.33 Pergunta 2

Quais são as áreas de práticas recomendadas de segurança? (Selecione TRÊS.)

- A Formações de segurança
- B Proteção de dados
- C Resposta a incidentes
- D Identity and Access Management
- E Preparação para eventos de segurança
- F Manter as pessoas longe dos dados

**Resposta: B, C, D.** Proteção de dados, Resposta a incidentes e Identity and Access Management.

### 5.34 Pergunta 3

Quais são os princípios de design de segurança? (Selecione TRÊS.)

- A Aplicar a segurança em todas as camadas.
- B Proteger dados em trânsito e em repouso.
- C Compreender que a verdadeira segurança não requer planejamento.
- D Manter as pessoas longe dos dados.
- E Usar controles de detecção.
- F Responder a incidentes.

**Resposta: A, B, D.** Aplicar a segurança em todas as camadas; proteger dados em trânsito e em repouso; e manter as pessoas longe dos dados.

### 5.35 Resumo do Módulo 5

Neste módulo, você aprendeu sobre o pilar de segurança. Iniciamos com uma visão geral e incluímos uma discussão aprofundada sobre a proposta de valor, os princípios de design e as práticas recomendadas do pilar de segurança.

Neste módulo, você aprendeu sobre:

- A visão geral do pilar de segurança
- A proposta de valor da segurança
- Os diferentes princípios de design do pilar de segurança
- As práticas recomendadas do pilar de segurança

<a id="modulo-6"></a>

## Módulo 6 — Análise detalhada do pilar de confiabilidade

### 6.1 Boas-vindas!

Boas-vindas ao módulo seis do AWS Well-Architected: Análise detalhada do pilar de confiabilidade.

### 6.2 Objetivos de aprendizado

Neste módulo, você aprenderá sobre o pilar de confiabilidade do AWS Well-Architected Framework. Você também aprenderá os princípios de design e as práticas recomendadas do pilar de confiabilidade.

Neste módulo, você:

- Terá uma visão geral do pilar de confiabilidade do AWS Well-Architected Framework
- Aprenderá sobre os princípios de design e as práticas recomendadas do pilar de confiabilidade

### 6.3 Visão geral do pilar de confiabilidade

Para começar, você terá uma visão geral do pilar de confiabilidade.

### 6.4 Pilares do AWS Well-Architected

Atualmente, há seis pilares do AWS Well-Architected Framework: excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. Esses pilares são os fundamentos da arquitetura de soluções de tecnologia na nuvem.

Este módulo se concentra no pilar de confiabilidade.

- **01 Excelência operacional**
- **02 Segurança**
- **03 Confiabilidade**
- **04 Eficiência de desempenho**
- **05 Otimização de custos**
- **06 Sustentabilidade**

### 6.5 O que é o pilar de confiabilidade?

> Confiabilidade é a capacidade de uma carga de trabalho de executar sua função pretendida de forma correta e consistente durante um período de tempo esperado.

O pilar de confiabilidade concentra-se na capacidade de uma carga de trabalho executar sua função pretendida corretamente e de forma consistente quando esperado. Isso inclui a capacidade de operar e testar a carga de trabalho durante todo o seu ciclo de vida.

### 6.6 Princípios de design de confiabilidade

Na nuvem, vários princípios podem ajudar a aumentar a confiabilidade. Agora você aprenderá mais sobre esses princípios de design.

### 6.7 Princípios de design de confiabilidade

Antes de se aprofundar nas práticas recomendadas, analise os princípios de design de confiabilidade. Eles ajudam a formar um modelo mental para o pilar, especialmente ao migrar de um ambiente tradicional *on-premises* para a nuvem.

**Recupere-se automaticamente de falhas.** Monitore a carga de trabalho para obter os principais indicadores de desempenho (KPIs) e inicie automações quando um limite for violado. Os KPIs devem medir o valor comercial, não apenas aspectos técnicos da operação. Notificações, rastreamento automatizado e processos de recuperação permitem contornar ou reparar falhas; automação adicional também ajuda a prever e corrigir problemas antes que ocorram.

**Teste os procedimentos de recuperação.** Em ambientes *on-premises*, os testes geralmente validam o funcionamento da carga de trabalho em um cenário específico. Na nuvem, teste como a carga de trabalho falha e valide os procedimentos de recuperação. Use automação para simular falhas e recriar cenários que antes causaram problemas, expondo caminhos de falha para que possam ser corrigidos antes de um incidente real.

**Dimensione horizontalmente para aumentar a disponibilidade agregada da carga de trabalho.** Substitua um recurso grande por vários recursos menores para reduzir o impacto de uma única falha. Distribua as solicitações entre esses recursos, evitando que compartilhem um ponto comum de falha.

**Pare de adivinhar a capacidade.** A saturação de recursos é uma causa comum de falhas em cargas de trabalho *on-premises*, pois a demanda pode exceder a capacidade disponível. Na nuvem, monitore demanda e utilização e automatize a adição ou remoção de recursos para manter a capacidade ideal, evitando tanto excesso quanto insuficiência de provisionamento. Algumas cotas podem ser controladas; outras precisam ser gerenciadas.

**Gerencie alterações por meio da automação.** Realize alterações de infraestrutura de forma automatizada. As mudanças que exigem gestão devem incluir alterações na automação, permitindo que sejam rastreadas e analisadas.

Princípios de design de confiabilidade:

1. 1Recuperar-se automaticamente de falhas
2. 2Testar os procedimentos de recuperação
3. 3Dimensionar horizontalmente para aumentar a disponibilidade agregada da carga de trabalho
4. 4Parar de tentar adivinhar a capacidade
5. 5Gerenciar alterações por meio da automação

### 6.8 Práticas recomendadas de confiabilidade

Na nuvem, as práticas recomendadas podem ajudar a aumentar a confiabilidade. Nesta seção, você aprenderá mais sobre essas práticas recomendadas.

### 6.9 Áreas de práticas recomendadas de confiabilidade

As práticas recomendadas do pilar de confiabilidade são organizadas em quatro áreas: fundamentos, arquitetura de carga de trabalho, gerenciamento de alterações e gerenciamento de falhas.

**Fundamentos.** Essa área aborda requisitos fundamentais que vão além de uma única carga de trabalho ou projeto. Antes de projetar uma carga de trabalho, implemente os requisitos que influenciam sua confiabilidade. Em ambientes *on-premises*, por exemplo, largura de banda de rede insuficiente pode criar longos tempos de execução devido a dependências e deve ser considerada no planejamento inicial. Na AWS, muitos desses requisitos já são incorporados ou podem ser tratados conforme necessário. A nuvem foi projetada para ter capacidade quase ilimitada; a AWS é responsável por garantir capacidade computacional e de rede suficiente, enquanto você pode alterar tamanho e alocação de recursos conforme a demanda.

**Arquitetura de carga de trabalho.** Uma carga de trabalho confiável começa com decisões iniciais de design de software e infraestrutura. Essas escolhas definem o comportamento da carga de trabalho e de seus pilares do AWS Well-Architected; para atingir confiabilidade, siga padrões específicos de arquitetura.

**Gerenciamento de alterações.** As alterações na carga de trabalho ou em seu ambiente devem ser previstas e acomodadas para uma operação confiável. Isso inclui mudanças impostas à carga de trabalho, como picos de demanda, e alterações internas, como implantações de recursos e patches de segurança.

**Gerenciamento de falhas.** Em ambientes *on-premises*, falhas de baixo nível de componentes de hardware são comuns e limitadas aos dias em um data center. Na nuvem, você deve se proteger contra uma variedade maior de falhas. Por exemplo, volumes do Amazon EBS são alocados em uma Zona de Disponibilidade e replicados automaticamente para proteção contra a falha de um único componente; o Amazon S3 armazena objetos de maneira resiliente em pelo menos três Zonas de Disponibilidade. Independentemente do provedor, falhas podem afetar a carga de trabalho. Tome medidas para garantir a resiliência, assegurando que as pessoas responsáveis por implementar e operar as cargas entendam os objetivos comerciais e as metas de confiabilidade necessárias.

Áreas de práticas recomendadas de confiabilidade:

- **01 Fundamentos**
- **02 Arquitetura de carga de trabalho**
- **03 Gerenciamento de alterações**
- **04 Gerenciamento de falhas**

### 6.10 Fundamentos

Na área de práticas recomendadas de fundamentos, o escopo pode ir além de uma única carga de trabalho ou projeto. Ela deve ser compreendida e implementada antes de arquitetar qualquer sistema; caso contrário, podem ocorrer longos prazos de entrega e bloqueios ao longo do caminho.

Planeje esses fundamentos antecipadamente para manter a liberdade de alterar o tamanho e as alocações de recursos conforme a demanda. Nesta seção, você aprenderá a gerenciar cotas ou restrições de serviço e a planejar a topologia da rede.

### 6.11 Gerenciar cotas e restrições de serviço

Arquiteturas de carga de trabalho na nuvem estão sujeitas a cotas de serviço, também chamadas de limites de serviço. Elas evitam o provisionamento acidental de mais recursos do que o necessário e podem limitar a taxa de solicitações às operações de API para proteger os serviços contra abuso. Há também restrições de recursos, como a taxa de bits disponível em uma conexão de fibra óptica ou a capacidade de armazenamento de um disco físico.

**Esteja ciente das cotas e restrições de serviço.** Conheça as cotas padrão, o processo para solicitar aumentos e as restrições de recursos — como disco e rede — que podem afetar a arquitetura.

**Gerencie cotas de serviço em contas e Regiões.** Quando utilizar várias contas ou Regiões AWS, solicite as cotas apropriadas para todos os ambientes em que as cargas de trabalho de produção são executadas. As cotas são rastreadas por conta e, salvo indicação contrária, são específicas da Região AWS. Gerencie também as cotas dos ambientes de não produção para que os testes de desenvolvimento não sejam prejudicados.

**Acomode cotas de serviço fixas e restrições por meio da arquitetura.** Considere cotas de serviço e limites dos recursos físicos imutáveis ao projetar a arquitetura, evitando que prejudiquem a confiabilidade.

**Monitore e gerencie cotas.** Monitore o uso potencial e aumente as cotas com antecedência suficiente para absorver o crescimento planejado.

**Automatize o gerenciamento de cotas.** Implemente ferramentas que alertem quando um limite estiver se aproximando e, quando possível, automatize as solicitações de aumento usando as APIs do AWS Service Quotas.

**Garanta que haja uma lacuna suficiente entre as cotas atuais e o uso máximo.** Mantenha folga para acomodar falhas. Quando um recurso é reprovado, ele pode continuar sendo contabilizado nas cotas até ser totalmente removido. Verifique se as cotas cobrem a sobreposição entre recursos com falha e seus substitutos antes da remoção completa; considere também uma falha de Zona de Disponibilidade ao calcular essa margem.

Práticas recomendadas para gerenciar cotas e restrições de serviço:

- Estar ciente das cotas e restrições de serviço
- Gerenciar cotas de serviço em contas e Regiões
- Acomodar cotas de serviço fixas e restrições por meio da arquitetura
- Monitorar e gerenciar cotas
- Automatizar o gerenciamento de cotas
- Garantir que haja uma lacuna suficiente entre as cotas atuais e o uso máximo

### 6.12 Planejar a topologia da rede

As cargas de trabalho geralmente existem em vários ambientes: nuvens públicas e privadas e, possivelmente, uma infraestrutura de data center já existente. O planejamento deve considerar conectividade intra e intersistemas, gerenciamento de endereços IP públicos e privados e resolução de nomes de domínio. Ao arquitetar sistemas que usam redes baseadas em IP, planeje a topologia, antecipe falhas e acomode o crescimento futuro e a integração com outros sistemas e redes.

**Use conectividade de rede altamente disponível para os endpoints públicos de sua carga de trabalho.** Os endpoints e seu roteamento devem ter alta disponibilidade. Use DNS altamente disponível, CDN, API Gateway, balanceamento de carga ou proxies reversos. Para redes privadas, forneça conectividade redundante entre ambientes de nuvem e *on-premises*, usando várias conexões AWS Direct Connect ou túneis de VPN entre redes implantadas separadamente. Use diversos locais do Direct Connect e, se houver várias Regiões AWS, garanta redundância em pelo menos duas delas.

**Provenha conectividade de rede redundante entre ambientes.** Elimine pontos únicos de falha nas conexões entre os ambientes que compõem a carga de trabalho.

**Garanta que a alocação da sub-rede IP leve em conta a expansão e a disponibilidade.** Os intervalos de endereços IP da Amazon VPC devem ser grandes o bastante para os requisitos atuais, a expansão futura e a alocação em sub-redes nas Zonas de Disponibilidade. Inclua nessa avaliação balanceadores de carga, instâncias do Amazon EC2 e aplicações baseadas em contêineres.

**Prefira topologias hub-and-spoke em vez de malha muitos-para-muitos.** Quando mais de dois espaços de endereço — como VPCs e redes *on-premises* — estiverem conectados por peering de VPC, Direct Connect ou VPN, use uma topologia hub-and-spoke. O AWS Transit Gateway é um exemplo desse modelo.

**Garanta a não sobreposição de intervalos de endereços IP privados.** Os intervalos de IP de VPCs conectadas não devem se sobrepor, inclusive quando as conexões ocorrerem por VPN. Evite conflitos com ambientes *on-premises* ou outros provedores de nuvem e mantenha um método para alocar novos intervalos privados quando necessário.

Práticas recomendadas para planejar a topologia da rede:

- Usar conectividade de rede altamente disponível para os endpoints públicos de sua carga de trabalho
- Prover conectividade de rede redundante entre ambientes
- Garantir que a alocação da sub-rede IP leve em conta a expansão e a disponibilidade
- Preferir topologias hub-and-spoke em vez de malha muitos-para-muitos
- Garantir a não sobreposição de intervalos de endereços IP privados

### 6.13 Arquitetura de carga de trabalho

A arquitetura de carga de trabalho é a próxima área de práticas recomendadas de confiabilidade. Uma carga de trabalho confiável começa com decisões iniciais de design para o software e a infraestrutura. Essas escolhas afetam o comportamento da carga de trabalho em todos os seis pilares do AWS Well-Architected.

Para alcançar confiabilidade, há padrões específicos a serem seguidos. Nas seções seguintes, você aprenderá a projetar a arquitetura de serviço da carga de trabalho e as interações em sistemas distribuídos para evitar, atenuar ou resistir a falhas.

### 6.14 Projetar sua arquitetura de serviço de carga de trabalho

Crie cargas de trabalho altamente dimensionáveis e confiáveis usando arquitetura orientada a serviços ou de microsserviços. A arquitetura orientada a serviços transforma componentes reutilizáveis de software em interfaces de serviço; a de microsserviços busca componentes menores e mais simples.

**Escolha como segmentar sua carga de trabalho.** A segmentação é importante para determinar os requisitos de resiliência da aplicação. Evite, sempre que possível, uma arquitetura monolítica; avalie quais componentes podem ser divididos em microsserviços. Cargas de trabalho sem estado são mais adequadas para implantação como microsserviços.

**Crie serviços focados em domínios e funcionalidades comerciais específicos.** A arquitetura orientada a serviços cria recursos com funções bem definidas pelas necessidades de negócio. Microsserviços usam modelos de domínio e contexto delimitado para limitar seu escopo, permitindo que cada serviço faça apenas uma coisa. Esse foco diferencia os requisitos de confiabilidade de cada serviço, orienta os investimentos e facilita dimensionar partes específicas da organização diante de um problema comercial conciso e de uma pequena equipe responsável.

**Forneça contratos de serviço por API.** Contratos de serviço são acordos documentados entre equipes sobre a integração de serviços, incluindo definição de API legível por máquina, limites de taxa e expectativas de desempenho. Uma estratégia de versionamento permite que clientes continuem usando a API existente enquanto migram para uma versão nova quando estiverem prontos. Assim, a equipe provedora pode usar a tecnologia mais adequada ao contrato, e a consumidora pode manter sua própria tecnologia.

Práticas recomendadas para projetar a arquitetura de serviço da carga de trabalho:

- Escolher como segmentar sua carga de trabalho
- Criar serviços focados em domínios e funcionalidades comerciais específicos
- Fornecer contratos de serviço por API

### 6.15 Projetar interações em um sistema distribuído para evitar falhas

Sistemas distribuídos dependem de redes de comunicação para interconectar componentes, como servidores e serviços. A carga de trabalho deve operar de forma confiável mesmo diante de perda de dados ou latência de rede, e seus componentes não devem afetar negativamente uns aos outros. Essas práticas ajudam a evitar falhas e a melhorar o tempo médio entre falhas (MTBF).

**Identifique que tipo de sistema distribuído é necessário.** Sistemas em tempo real exigem respostas síncronas e rápidas. Sistemas flexíveis em tempo real têm uma janela mais generosa, de minutos ou mais, para responder; sistemas *off-line* processam respostas em lote ou de modo assíncrono. Sistemas distribuídos rígidos em tempo real têm requisitos de confiabilidade mais rigorosos.

**Implemente dependências com acoplamento fraco.** Sistemas de enfileiramento, streaming, fluxos de trabalho e balanceadores de carga são exemplos de dependências fracamente acopladas. Esse modelo isola o comportamento de cada componente daqueles que dependem dele, aumentando a resiliência e a agilidade.

**Faça um trabalho constante.** Evite grandes e rápidas alterações na carga. Por exemplo, se uma carga de trabalho executa verificações de integridade em milhares de servidores, ela deve enviar o mesmo tamanho de *payload* — um snapshot completo do estado atual — a todos, independentemente de haver falhas. Isso mantém um trabalho constante, mesmo sob grandes alterações.

**Torne todas as respostas idempotentes.** Um serviço idempotente garante que cada solicitação seja concluída exatamente uma vez, de forma que várias solicitações idênticas tenham o mesmo efeito de uma única solicitação. Isso permite novas tentativas sem o risco de processar a mesma solicitação indevidamente. Clientes podem usar um token de idempotência nas chamadas de API; o serviço usa esse token para retornar uma resposta idêntica àquela enviada quando a solicitação foi concluída pela primeira vez.

Práticas recomendadas para evitar falhas em sistemas distribuídos:

- Identificar que tipo de sistema distribuído é necessário
- Implementar dependências com acoplamento fraco
- Fazer um trabalho constante
- Tornar todas as respostas idempotentes

### 6.16 Projetar interações em um sistema distribuído para mitigar ou resistir a falhas

Sistemas distribuídos dependem de redes de comunicação e devem operar de forma confiável mesmo diante de perda de dados ou latência. Os componentes não devem afetar negativamente outros componentes nem a carga de trabalho. Estas práticas ajudam a resistir e a se recuperar mais rapidamente de falhas, atenuando seu impacto e melhorando o tempo médio de recuperação (MTTR).

**Implemente a degradação graciosa para transformar as dependências rígidas aplicáveis em dependências flexíveis.** Quando as dependências de um componente não estiverem saudáveis, o componente ainda pode operar de forma degradada. Por exemplo, se uma chamada a uma dependência falhar, faça *failover* para uma resposta estática predefinida.

**Limite solicitações.** A limitação de solicitações é um padrão de atenuação para responder a aumentos inesperados de demanda. Parte das solicitações é atendida, enquanto as que excedem um limite definido são rejeitadas e recebem uma mensagem indicando que foram limitadas. Espera-se que os clientes recuem, abandonando a solicitação ou tentando novamente em ritmo menor.

**Controle e limite as chamadas de repetição.** Use *backoff* exponencial para tentar novamente após intervalos progressivamente maiores, adicione *jitter* para randomizar esses intervalos e limite o número máximo de tentativas.

**Falhe rapidamente e limite filas.** Se a carga de trabalho não puder responder a uma solicitação com êxito, falhe rapidamente. Isso libera recursos e ajuda o serviço a se recuperar quando estiver sem recursos. Quando a taxa de solicitações for alta, use uma fila para armazená-las em buffer, mas não permita filas longas que possam gerar atendimento de solicitações obsoletas, das quais o cliente já desistiu.

**Defina tempos limite do cliente adequadamente.** Revise-os sistematicamente e não confie nos valores padrão, pois geralmente são definidos como altos. Esta prática se aplica ao lado do cliente ou remetente da solicitação.

**Torne os serviços stateless sempre que possível.** Serviços sem estado não exigem que o estado seja carregado ou descarregado entre solicitações de clientes, evitando a dependência de dados armazenados localmente em disco ou memória. Isso permite substituir servidores livremente, sem impacto na disponibilidade.

**Implemente alavancas de emergência.** Esses mecanismos rápidos reduzem o impacto da disponibilidade na carga de trabalho.

Práticas recomendadas para mitigar ou resistir a falhas em sistemas distribuídos:

- Implementar a degradação graciosa para transformar as dependências rígidas aplicáveis em dependências flexíveis
- Limitar solicitações
- Controlar e limitar as chamadas de repetição
- Falhar rapidamente e limitar filas
- Definir tempos limite do cliente adequadamente
- Tornar os serviços stateless sempre que possível
- Implementar alavancas de emergência

### 6.17 Gerenciamento de alterações

O gerenciamento de alterações é a próxima área de práticas recomendadas de confiabilidade. Mudanças na carga de trabalho ou em seu ambiente devem ser previstas e acomodadas para que a operação permaneça confiável. Elas incluem alterações impostas à carga de trabalho, como picos de demanda, e alterações internas, como implantações de recursos e patches de segurança.

Nas seções seguintes, você aprenderá a monitorar os recursos da carga de trabalho, projetá-la para se adaptar a mudanças na demanda e implementar alterações.

### 6.18 Monitorar recursos de carga de trabalho

Logs e métricas são ferramentas poderosas para conhecer a integridade da carga de trabalho. Configure-a para monitorar logs e métricas, e emita notificações quando limites forem excedidos ou ocorrerem eventos significativos. O monitoramento ajuda a reconhecer limites de baixo desempenho e falhas para que a carga possa se recuperar automaticamente.

**Monitore todos os componentes da carga de trabalho.** Monitore os componentes com o Amazon CloudWatch ou ferramentas de terceiros; acompanhe os serviços AWS com o AWS Health Dashboard.

**Defina e calcule métricas.** Armazene dados de log e aplique filtros quando necessário para calcular métricas, como contagens de eventos específicos ou latência derivada de carimbos de data e hora de eventos de log.

**Envie notificações.** As organizações que precisam saber sobre eventos significativos devem receber notificações quando eles ocorrerem.

**Automatize respostas.** Implemente processamento e alarmes em tempo real. Use automação para tomar medidas quando um evento for detectado, por exemplo, substituir componentes com falha.

**Realize analytics.** Colete arquivos de log e históricos de métricas e analise-os para obter tendências mais amplas e informações sobre a carga de trabalho.

**Conduza análises regularmente.** Revise com frequência como o monitoramento está implementado e atualize-o segundo eventos e mudanças significativas. O monitoramento eficaz é orientado pelas principais métricas de negócios, que devem ser acomodadas à medida que as prioridades comerciais mudam.

**Monitore o rastreamento de ponta a ponta das solicitações em seu sistema.** Use AWS X-Ray ou ferramentas de terceiros para permitir que desenvolvedores analisem e depurem rapidamente sistemas distribuídos, compreendendo o desempenho das aplicações e dos serviços subjacentes.

Práticas recomendadas para monitorar recursos da carga de trabalho:

- Monitorar todos os componentes da carga de trabalho
- Definir e calcular métricas
- Enviar notificações
- Automatizar respostas
- Realizar analytics
- Conduzir análises regularmente
- Monitorar o rastreamento de ponta a ponta das solicitações em seu sistema

### 6.19 Projetar uma carga de trabalho para se adaptar às mudanças na demanda

Uma carga de trabalho dimensionável oferece elasticidade para adicionar ou remover recursos automaticamente, aproximando-se da demanda atual no momento necessário. Use automação para obter ou escalar recursos. Ao substituir recursos com problemas ou escalar a carga, automatize o processo com serviços gerenciados pela AWS, como Amazon S3 e AWS Auto Scaling, ou com ferramentas de terceiros e SDKs da AWS.

**Use a automação ao obter ou escalar recursos.** Automatize a obtenção, substituição e o dimensionamento de recursos para acompanhar a demanda.

**Obtenha recursos após a detecção de comprometimento de uma carga de trabalho.** Dimensione recursos reativamente, quando necessário, caso a disponibilidade seja afetada. Configure *health checks* e seus critérios para indicar quando a disponibilidade é afetada pela falta de recursos; então, notifique a equipe apropriada ou use automação para dimensionar recursos.

**Obtenha recursos ao detectar que são necessários mais recursos para uma carga de trabalho.** Dimensione proativamente para atender à demanda e evitar impacto na disponibilidade.

**Teste a carga de trabalho.** Use metodologias de teste de carga para medir se as ações de *scaling* atendem aos requisitos da carga de trabalho.

Práticas recomendadas para adaptar a carga de trabalho às mudanças na demanda:

- Usar a automação ao obter ou escalar recursos
- Obter recursos após a detecção de comprometimento de uma carga de trabalho
- Obter recursos ao detectar que são necessários mais recursos para uma carga de trabalho
- Testar a carga de trabalho

### 6.20 Implementar alterações

Alterações controladas são necessárias para implantar novas funcionalidades e para garantir que a carga de trabalho e seu ambiente operacional continuem em um estado conhecido e recebam os patches adequados. Sem controle, torna-se difícil prever seus efeitos ou resolver os problemas resultantes.

**Use runbooks para atividades padrão, como a implantação.** Runbooks são procedimentos predefinidos para alcançar resultados específicos. Use-os em atividades padrão, de forma manual ou automática, como implantar uma carga de trabalho, aplicar patches ou realizar modificações de DNS.

**Integre o teste funcional como parte de sua implantação.** Execute testes funcionais na implantação automatizada. Se os critérios de sucesso não forem atendidos, interrompa os pipelines. Realize esses testes em pré-produção e, idealmente, como parte do pipeline de implantação.

**Integre o teste de resiliência como parte de sua implantação.** Prepare e execute testes de resiliência com princípios de engenharia do caos como parte do pipeline automatizado em pré-produção. Eles também devem ser executados em produção como parte de dias de teste.

**Implante usando uma infraestrutura imutável.** Nesse modelo, nenhuma atualização, patch de segurança ou alteração de configuração é aplicada à carga de trabalho de produção existente. Quando uma mudança é necessária, construa uma nova infraestrutura e a implante em produção. Automatize as implantações e a aplicação de patches para reduzir impactos negativos.

**Implante as alterações com automação.** Automatize a implantação para produzir mudanças consistentes, repetíveis e rastreáveis, reduzindo a chance de erro humano.

Práticas recomendadas para implementar alterações:

- Usar runbooks para atividades padrão, como a implantação
- Integrar o teste funcional como parte de sua implantação
- Integrar o teste de resiliência como parte de sua implantação
- Implantar usando uma infraestrutura imutável
- Implantar as alterações com automação

### 6.21 Gerenciamento de falhas

O gerenciamento de falhas é a próxima área de práticas recomendadas de confiabilidade. Falhas de baixo nível em componentes de hardware são comuns em data centers *on-premises*. Na nuvem, você deve estar protegido contra uma variedade maior de tipos de falha. Independentemente do provedor, falhas podem afetar a carga de trabalho; por isso, implemente resiliência para manter sua confiabilidade.

Um pré-requisito é garantir que as pessoas que projetam, implementam e operam a carga de trabalho entendam seus objetivos comerciais e metas de confiabilidade e sejam treinadas para esses requisitos.

As seções a seguir explicam práticas para gerenciar falhas e evitar seu impacto na carga de trabalho.

### 6.22 Backup de dados

**Identifique e faça o backup de todos os dados que precisam de backup.** Faça backup de dados, aplicações e configurações para atender aos objetivos de tempo de recuperação (RTO) e de ponto de recuperação (RPO). Ao escolher a estratégia, considere o tempo necessário para recuperar os dados, que varia conforme o tipo de backup — por exemplo, restauração de backup ou reprodução de dados — e garanta que fique dentro do RTO da carga de trabalho.

**Proteja e/ou criptografe backups.** Controle e detecte o acesso usando autenticação e autorização, como AWS Identity and Access Management (IAM). Previna e detecte comprometimento da integridade dos dados por meio de criptografia.

**Realize backup de dados automaticamente.** Configure backups automáticos com base em uma programação orientada pelo RPO ou por mudanças no conjunto de dados. Dados críticos com baixo RPO devem ser copiados com frequência; dados menos críticos, cuja perda é aceitável, podem ter menor frequência de cópia.

**Realize recuperação periódica de dados para verificar a integridade e os processos de backup.** Valide que a implementação e o processo de backup atendem ao RTO e ao RPO por meio de testes periódicos de recuperação.

Práticas recomendadas para backup de dados:

- Identificar e fazer o backup de todos os dados que precisam de backup
- Proteger e/ou criptografar backups
- Realizar backup de dados automaticamente
- Realizar recuperação periódica de dados para verificar a integridade e os processos de backup

### 6.23 Usar o isolamento de falhas para proteger sua carga de trabalho

Limites isolados de falhas confinam o efeito de uma falha a uma carga de trabalho ou a um número limitado de componentes. Componentes externos ao limite não são afetados. Ao usar diversos limites isolados, você reduz o impacto sobre a carga de trabalho.

**Implante cargas de trabalho em vários locais.** Distribua dados e recursos em várias Zonas de Disponibilidade ou, quando necessário, em várias Regiões AWS. Os locais podem ter a diversidade exigida pela carga de trabalho.

**Selecione os locais apropriados para sua implantação em vários locais.** Para obter alta disponibilidade, implante componentes em várias Zonas de Disponibilidade. Para requisitos extremos de resiliência, avalie cuidadosamente uma arquitetura multirregional.

**Automatize a recuperação de componentes restritos a um único local.** Se um componente só puder ser executado em uma única Zona de Disponibilidade ou em um data center *on-premises*, implemente recursos para reconstruir completamente a carga de trabalho dentro dos objetivos de recuperação definidos.

**Use arquiteturas de anteparo para limitar o escopo do impacto.** Assim como anteparos em um navio, esse padrão limita uma falha a um pequeno subconjunto de solicitações ou clientes, permitindo que a maior parte continue sem erros. Anteparos de dados são normalmente chamados de partições; anteparos de serviços, de células.

Práticas recomendadas para usar o isolamento de falhas:

- Implantar cargas de trabalho em vários locais
- Selecionar os locais apropriados para sua implantação em vários locais
- Automatizar a recuperação de componentes restritos a um único local
- Usar arquiteturas de anteparo para limitar o escopo do impacto

### 6.24 Projetar a carga de trabalho para resistir a falhas de componentes

Cargas de trabalho com requisitos de alta disponibilidade e baixo tempo médio de recuperação (MTTR) devem ser arquitetadas para resiliência.

**Monitore todos os componentes da carga de trabalho para detectar falhas.** Monitore continuamente sua integridade para que pessoas e sistemas automatizados identifiquem degradações ou falhas assim que ocorrerem. Monitore KPIs com base no valor comercial.

**Faça o failover para recursos íntegros.** Garanta que, se um recurso falhar, recursos saudáveis possam continuar atendendo às solicitações. Para falhas de local, como em uma Zona de Disponibilidade ou Região AWS, tenha sistemas capazes de realizar *failover* para recursos íntegros em locais não afetados.

**Automatize a recuperação em todas as camadas.** Após detectar uma falha, use recursos automatizados para executar ações de correção. A reinicialização é uma ferramenta importante para corrigir falhas; tornar os serviços *stateless* sempre que possível evita perda de dados ou indisponibilidade ao reiniciar.

**Confie no plano de dados, não no plano de controle, durante a recuperação.** O plano de controle configura recursos; o plano de dados fornece serviços. Normalmente, o plano de dados tem objetivos de disponibilidade mais altos e é menos complexo. Ao implementar respostas de recuperação ou atenuação, usar operações do plano de controle pode reduzir a resiliência geral.

**Use a estabilidade estática para evitar o comportamento bimodal.** Comportamento bimodal ocorre quando a carga apresenta comportamentos diferentes em modos normal e de falha. Crie cargas estaticamente estáveis que operem em apenas um modo. Por exemplo, provisione instâncias suficientes em cada Zona de Disponibilidade para suportar a carga se uma zona for removida e configure o Elastic Load Balancing e as verificações de integridade do Amazon Route 53 para desviar o tráfego das instâncias prejudicadas.

**Envie notificações quando os eventos afetarem a disponibilidade.** Envie notificações após detectar eventos significativos, mesmo que o problema tenha sido resolvido automaticamente.

**Arquitete o produto para atender às metas de disponibilidade e aos SLAs de tempo de atividade.** Se houver publicação ou acordo privado de metas de disponibilidade ou SLAs, confirme que a arquitetura e os processos operacionais foram projetados para sustentá-los.

Práticas recomendadas para resistir a falhas de componentes:

- Monitorar todos os componentes da carga de trabalho para detectar falhas
- Fazer o failover para recursos íntegros
- Automatizar a recuperação em todas as camadas
- Confiar no plano de dados, não no plano de controle, durante a recuperação
- Usar a estabilidade estática para evitar o comportamento bimodal
- Enviar notificações quando os eventos afetarem a disponibilidade
- Arquitetar o produto para atender às metas de disponibilidade e aos SLAs de tempo de atividade

### 6.25 Testar a confiabilidade

Depois de projetar a carga de trabalho para ser resiliente aos estresses de produção, o teste é a única forma de garantir que ela funcionará conforme planejado. Teste regularmente para validar requisitos funcionais e não funcionais, pois bugs ou gargalos de desempenho podem afetar a confiabilidade. Testes de resiliência também ajudam a encontrar falhas latentes que aparecem apenas em produção.

**Use playbooks para investigar falhas.** Configure respostas consistentes e rápidas para cenários de falha pouco compreendidos, documentando o processo de investigação em playbooks. Eles definem etapas predefinidas para identificar fatores que contribuem para um cenário de falha e usam os resultados de cada etapa para orientar as próximas até que o problema seja identificado ou encaminhado.

**Realize análise pós-incidente.** Analise eventos que afetam o cliente, identifique fatores contribuintes e itens de ação preventiva e use essas informações para desenvolver mitigações contra recorrência. Crie procedimentos de resposta rápida e eficaz, comunique os fatores e ações corretivas aos públicos adequados e documente um método de comunicação dessas causas.

**Teste os requisitos funcionais.** Use técnicas como testes de unidade e de integração para validar a funcionalidade necessária.

**Teste os requisitos de scaling e desempenho.** Use técnicas como teste de carga para validar se a carga de trabalho atende aos requisitos de escalabilidade e desempenho.

**Teste a resiliência usando a engenharia do caos.** Execute experimentos regulares em ambientes de produção ou o mais próximo possível dela para entender como o sistema responde a condições adversas.

**Realize dias de teste regularmente.** Use esses exercícios para praticar consistentemente procedimentos de resposta a eventos e falhas o mais próximo possível da produção. Inclua ambientes de produção e pessoas envolvidas em cenários reais de falha, aplicando medidas que protejam os usuários contra eventos de produção.

Práticas recomendadas para testar a confiabilidade:

- Usar playbooks para investigar falhas
- Realizar análise pós-incidente
- Testar os requisitos funcionais
- Testar os requisitos de scaling e desempenho
- Testar a resiliência usando a engenharia do caos
- Realizar dias de teste regularmente

### 6.26 Planejar para a recuperação de desastres

Backups e componentes de carga de trabalho redundantes são o início da estratégia de recuperação de desastres. Os objetivos de tempo de recuperação (RTO) e de ponto de recuperação (RPO) definem como restaurar a carga de trabalho; estabeleça-os com base nas necessidades empresariais. A probabilidade de interrupção e o custo de recuperação também ajudam a informar o valor comercial da solução.

Disponibilidade e recuperação de desastres dependem de práticas semelhantes, como monitoramento de falhas, implantação em vários locais e *failover* automático. A diferença é que disponibilidade se concentra nos componentes da carga de trabalho, enquanto recuperação de desastres se concentra em cópias discretas de toda a carga e em objetivos distintos de disponibilidade, voltados ao tempo de recuperação após um desastre.

**Defina objetivos de recuperação para tempo de inatividade e perda de dados.** A carga de trabalho possui um RTO e um RPO. O RTO é o atraso máximo aceitável entre a interrupção e a restauração do serviço — a janela aceitável de indisponibilidade. O RPO é a quantidade máxima aceitável de tempo desde o último ponto de recuperação de dados — a perda de dados aceitável entre esse ponto e a interrupção.

**Use estratégias de recuperação definidas para atingir os objetivos de recuperação.** Escolha e implemente uma estratégia, como backup e restauração, ativo-passivo ou ativo-ativo. Teste regularmente o *failover* no site de recuperação para confirmar que a operação é adequada e que RTO e RPO são atendidos.

**Teste a implementação da recuperação de desastres para validar a implementação.** Teste os mecanismos de recuperação para confirmar que as metas e a estratégia definida funcionam conforme planejado.

**Gerencie o desvio de configuração no site ou na Região de recuperação de desastres.** Garanta que infraestrutura, dados e configuração estejam de acordo com o necessário no local ou Região de DR. Por exemplo, confirme que AMIs e cotas de serviço estão atualizadas.

**Automatize a recuperação.** Use AWS ou ferramentas de terceiros para automatizar a recuperação do sistema e encaminhar o tráfego para o site ou Região de recuperação de desastres.

Práticas recomendadas para planejar a recuperação de desastres:

- Definir objetivos de recuperação para tempo de inatividade e perda de dados
- Usar estratégias de recuperação definidas para atingir os objetivos de recuperação
- Testar a implementação da recuperação de desastres para validar a implementação
- Gerenciar o desvio de configuração no site ou na Região de recuperação de desastres
- Automatizar a recuperação

### 6.27 Pergunta 1

Qual das seguintes opções é uma área de práticas recomendadas de confiabilidade?

- A Fundamentos
- B Arquitetura de rede
- C Gerenciamento de riscos
- D Alocação de custos

**Resposta: A.** Fundamentos.

### 6.28 Pergunta 2

Quais são os exemplos de práticas recomendadas de confiabilidade na arquitetura de cargas de trabalho? (Selecione TRÊS.)

- A Tornar todas as respostas idempotentes.
- B Falhar rapidamente e limitar filas.
- C Limitar solicitações.
- D Usar tags de alocação de custos.
- E Proteger e/ou criptografar backups.
- F Realizar análise pós-incidente.

**Resposta: A, B, C.** Tornar todas as respostas idempotentes; falhar rapidamente e limitar filas; e limitar solicitações.

### 6.29 Pergunta 3

Quais das práticas recomendadas a seguir são para testar a confiabilidade? (Selecione DUAS.)

- A Usar playbooks para investigar falhas.
- B Realizar análise pós-incidente.
- C Testar a conformidade com a segurança e os requisitos de desempenho.
- D Conduzir mensalmente o processo de análise do AWS Well-Architected.
- E Realizar reuniões diárias de trabalho para discutir possíveis pontos de ruptura no sistema.

**Resposta: A, B.** Usar playbooks para investigar falhas e realizar análise pós-incidente.

### 6.30 Resumo do Módulo 6

Neste módulo, você aprendeu sobre a importância do pilar de confiabilidade no AWS Well-Architected Framework e a proposta de valor para a confiabilidade em suas arquiteturas. Também aprendeu sobre os princípios de design e as práticas recomendadas desse pilar.

Neste módulo, você aprendeu sobre:

- A importância do pilar de confiabilidade no AWS Well-Architected Framework
- A proposta de valor para a confiabilidade em suas arquiteturas
- Os princípios de design do pilar de confiabilidade
- As práticas recomendadas do pilar de confiabilidade

<a id="modulo-7"></a>

## Módulo 7 — Análise detalhada do pilar de eficiência de desempenho

### 7.1 Boas-vindas!

Boas-vindas ao módulo sete do AWS Well-Architected: Análise detalhada do pilar de eficiência de desempenho.

### 7.2 Objetivos de aprendizado

Neste módulo, você terá uma visão geral do pilar de eficiência de desempenho do AWS Well-Architected Framework. Você também aprenderá os princípios de design e as práticas recomendadas do pilar de eficiência de desempenho.

Neste módulo, você:

- Terá uma visão geral do pilar de eficiência de desempenho do AWS Well-Architected Framework
- Aprenderá sobre os princípios de design e as práticas recomendadas do pilar de eficiência de desempenho

### 7.3 Visão geral do pilar de eficiência de desempenho

Para começar, você terá uma visão geral do pilar de eficiência de desempenho.

### 7.4 Pilares do Well-Architected

Atualmente, há seis pilares do AWS Well-Architected Framework: excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. Esses pilares são os fundamentos da arquitetura de soluções de tecnologia na nuvem.

Este módulo se concentra no pilar de eficiência de desempenho.

- **01 Excelência operacional**
- **02 Segurança**
- **03 Confiabilidade**
- **04 Eficiência de desempenho**
- **05 Otimização de custos**
- **06 Sustentabilidade**

### 7.5 O que é o pilar de eficiência de desempenho?

> O pilar de eficiência de desempenho concentra-se no uso eficiente dos recursos de computação para atender aos requisitos e em como manter a eficiência à medida que a demanda muda e as tecnologias evoluem.

### 7.6 Princípios de design de eficiência de desempenho

Agora que você já sabe o que é o pilar de eficiência de desempenho, vamos nos aprofundar nos princípios de design desse pilar.

### 7.7 Princípios de design de eficiência de desempenho

Há cinco princípios de design para a eficiência de desempenho na nuvem.

**Democratize tecnologias avançadas.** Simplifique a implementação de tecnologias avançadas para sua equipe e delegue tarefas complexas ao provedor de nuvem. Em vez de hospedar uma nova tecnologia internamente, considere consumi-la como serviço. Tecnologias que exigiriam conhecimento especializado, como Machine Learning e bancos de dados NoSQL, tornam-se serviços que a equipe pode usar, liberando tempo para o desenvolvimento de produtos em vez do provisionamento e gerenciamento de recursos.

**Tenha alcance global em minutos.** A implantação em várias Regiões aproxima a carga de trabalho de um público global, reduzindo latência e melhorando a experiência. Serviços como AWS CloudFormation permitem ativar rapidamente recursos em diferentes regiões geográficas com pouca sobrecarga, melhorando o desempenho e oferecendo acesso a recursos ou funcionalidades disponíveis em outras Regiões.

**Use arquiteturas sem servidor.** Arquiteturas *serverless* eliminam a necessidade de executar e manter servidores físicos para atividades tradicionais de computação. Serviços de armazenamento sem servidor podem hospedar sites estáticos, dispensando servidores web, e serviços de eventos podem hospedar código. Isso reduz a carga operacional e pode trazer custos transacionais menores, pois os serviços gerenciados operam em escala de nuvem.

**Faça experimentos com mais frequência.** Com recursos praticamente ilimitados, a nuvem permite comparar rapidamente configurações de cargas de trabalho: experimentar um tamanho de instância ou tipo de armazenamento diferente, ou serviços inteiramente distintos, como executar código em uma função AWS Lambda em vez de uma instância do Amazon EC2.

**Considere a afinidade mecânica.** Alinhe a abordagem tecnológica aos objetivos comerciais gerais, e não o contrário. Entenda como os serviços de nuvem são consumidos e escolha a abordagem que melhor atende às metas da carga de trabalho. Por exemplo, considere sempre os padrões de acesso aos dados ao selecionar tecnologias de banco de dados ou armazenamento.

Princípios de design de eficiência de desempenho:

1. 1Democratizar tecnologias avançadas
2. 2Ter alcance global em minutos
3. 3Usar arquiteturas sem servidor
4. 4Fazer experimentos com mais frequência
5. 5Considerar a afinidade mecânica

### 7.8 Práticas recomendadas de eficiência de desempenho

Agora que você entende os princípios de eficiência de desempenho, aprenderá sobre as práticas recomendadas de eficiência de desempenho.

### 7.9 Áreas de práticas recomendadas de eficiência de desempenho

O pilar de eficiência de desempenho está agrupado em quatro áreas de práticas recomendadas:

- **01 Seleção**
- **02 Análise**
- **03 Monitoramento**
- **04 Concessões**

### 7.10 Seleção

A seleção é a primeira área de práticas recomendadas de eficiência de desempenho.

### 7.11 Seleção da arquitetura de desempenho

Use uma abordagem orientada por dados para selecionar padrões e a implementação da arquitetura, obtendo uma solução econômica. A arquitetura provavelmente combinará várias abordagens e utilizará serviços específicos para otimizar seu desempenho.

**Entenda os serviços e recursos disponíveis.** Conheça a ampla gama de serviços e recursos disponíveis na nuvem. Identifique os serviços e as opções de configuração relevantes para a carga de trabalho e entenda como obter o desempenho ideal.

**Defina um processo para escolhas arquitetônicas.** Use a experiência e o conhecimento internos sobre nuvem, além de recursos externos — como casos de uso publicados, documentação e *whitepapers* — para criar um processo de escolha de recursos e serviços. Esse processo deve incentivar a experimentação e o *benchmarking*.

**Considere os requisitos de custo nas decisões.** Use controles de custos internos para selecionar tipos e tamanhos de recursos conforme a necessidade prevista. Avalie quais componentes podem ser substituídos por serviços totalmente gerenciados, como bancos de dados gerenciados e caches em memória, reduzindo a carga operacional e concentrando recursos nos resultados comerciais.

**Use políticas ou arquiteturas de referência.** Maximize desempenho e eficiência avaliando políticas internas e arquiteturas de referência existentes e usando a análise para selecionar serviços e configurações adequados.

**Use a orientação de seu provedor de nuvem ou de um parceiro apropriado.** Recorra a recursos como arquitetos de soluções, serviços profissionais ou parceiros adequados para orientar decisões, analisar e aprimorar a arquitetura.

**Compare as cargas de trabalho existentes.** Compare o desempenho de uma carga de trabalho atual para entender seu comportamento na nuvem. Use os dados de *benchmarks* para orientar decisões arquitetônicas; testes sintéticos geram dados sobre o desempenho de componentes específicos e costumam ser mais rápidos de configurar que testes de carga.

**Teste a carga de trabalho.** Implante a arquitetura mais recente na nuvem usando diferentes tipos e tamanhos de recursos. Monitore a implantação para capturar métricas que revelem gargalos ou excesso de capacidade e use essas informações para aprimorar a arquitetura e a seleção de recursos.

Práticas recomendadas para seleção da arquitetura de desempenho:

- Entender os serviços e recursos disponíveis
- Definir um processo para escolhas arquitetônicas
- Considerar os requisitos de custo nas decisões
- Usar políticas ou arquiteturas de referência
- Usar a orientação de seu provedor de nuvem ou de um parceiro apropriado
- Comparar as cargas de trabalho existentes
- Testar a carga de trabalho

### 7.12 Seleção da arquitetura de computação

Selecione recursos de computação que atendam aos requisitos e às necessidades de desempenho, oferecendo também eficiência de custo e esforço. A solução ideal varia conforme o design da aplicação, os padrões de uso e as configurações, mas pode ajudar a realizar mais com a mesma quantidade de recursos.

**Entenda opções de configuração de computação disponíveis.** Saiba como as opções complementam a carga de trabalho e escolha a configuração mais apropriada. Exemplos incluem família e tamanho de instância, GPU, E/S, tamanho de funções, instâncias de contêineres e ambiente de locatário único ou multilocatário.

**Avalie opções de computação disponíveis.** Entenda as características de desempenho de instâncias, contêineres e funções, incluindo suas vantagens e desvantagens para a carga de trabalho. Na AWS, a computação está disponível nessas três formas.

**Colete métricas relacionadas à computação.** Registre e acompanhe a utilização dos sistemas para entender o desempenho dos recursos e determinar com mais precisão os requisitos.

**Determine a configuração necessária por meio do dimensionamento correto.** Analise o desempenho da carga de trabalho em relação a memória, rede, E/S e CPU e escolha recursos adequados ao seu perfil. Por exemplo, um banco de dados intensivo em memória pode se beneficiar de mais memória por núcleo, enquanto uma carga intensiva em computação pode precisar de maior contagem e frequência de núcleos, mas menos memória por núcleo.

**Use a elasticidade disponível dos recursos.** Expanda ou reduza recursos dinamicamente para atender às mudanças de demanda. Combinada às métricas de computação, a elasticidade permite que a carga responda automaticamente, usando somente os recursos necessários.

**Avalie continuamente as necessidades de computação com base em métricas.** Use uma abordagem orientada por dados para avaliar e otimizar os recursos de computação ao longo do tempo.

Práticas recomendadas para seleção da arquitetura de computação:

- Entender opções de configuração de computação disponíveis
- Avaliar opções de computação disponíveis
- Coletar métricas relacionadas à computação
- Determinar a configuração necessária por meio do dimensionamento correto
- Usar a elasticidade disponível dos recursos
- Avaliar continuamente as necessidades de computação com base em métricas

### 7.13 Seleção da arquitetura de armazenamento

A solução ideal de armazenamento depende do método de acesso — bloco, arquivo ou objeto —, de padrões aleatórios ou sequenciais, do throughput necessário, das restrições de disponibilidade e durabilidade e da frequência de acesso ou atualização.

**Entenda as características e os requisitos de armazenamento.** Identifique e documente as necessidades da carga de trabalho e defina as características de cada local de armazenamento: acesso compartilhável, tamanho de arquivo, taxa de crescimento, throughput, operações de entrada e saída por segundo (IOPS), latência, padrões de acesso e persistência dos dados. Use essas informações para avaliar se o armazenamento em bloco, arquivo, objeto ou instância é mais eficiente.

**Tome decisões baseadas em padrões de acesso e métricas.** Escolha e configure os sistemas de armazenamento conforme os padrões de acesso da carga de trabalho. Aumente a eficiência, quando aplicável, escolhendo armazenamento de objetos em vez de blocos e configurando as opções selecionadas conforme os padrões de acesso aos dados.

**Avalie as opções de configuração disponíveis.** Avalie características e opções de configuração relacionadas ao armazenamento. Entenda onde e como usar IOPS provisionado, unidades de estado sólido (SSD), armazenamento magnético, de objetos, de arquivos ou temporário para otimizar espaço e desempenho.

Práticas recomendadas para seleção da arquitetura de armazenamento:

- Entender as características e os requisitos de armazenamento
- Tomar decisões baseadas em padrões de acesso e métricas
- Avaliar as opções de configuração disponíveis

### 7.14 Seleção da arquitetura do banco de dados

Escolher a solução e os recursos errados para um sistema pode reduzir a eficiência de desempenho. Ao selecionar a solução de banco de dados, considere requisitos como disponibilidade, consistência, tolerância a partições, latência, durabilidade, escalabilidade e capacidade de consulta.

**Entenda as características dos dados.** Escolha soluções de gerenciamento de dados que correspondam às características, padrões de acesso e requisitos dos conjuntos de dados. Verifique se características de consulta, escalabilidade e armazenamento são compatíveis com esses requisitos, entendendo como as opções de banco de dados se ajustam aos modelos de dados e ao caso de uso.

**Avalie as opções disponíveis.** Entenda as opções de banco de dados e como elas podem otimizar o desempenho antes da seleção. Use testes de carga para identificar métricas importantes e avalie grupos de parâmetros, armazenamento, memória, computação, réplicas de leitura, consistência eventual, *pool* de conexões e cache. Experimente as configurações para melhorar métricas.

**Colete e registre métricas de desempenho de banco de dados.** Use ferramentas, bibliotecas e sistemas que registrem medições de desempenho para compreender os sistemas de gerenciamento de dados, otimizar seus recursos e garantir os requisitos da carga de trabalho.

**Escolha o armazenamento de dados com base em padrões de acesso.** Use os padrões de acesso da carga de trabalho e os requisitos das aplicações para decidir as tecnologias e serviços de dados adequados.

**Otimize o armazenamento de dados com base em padrões de acesso e métricas.** Use características de desempenho e padrões de acesso para otimizar como os dados são armazenados ou consultados. Avalie o efeito de otimizações como indexação, distribuição de chaves, projeto de *data warehouse* e estratégias de cache sobre o desempenho e a eficiência geral.

Práticas recomendadas para seleção da arquitetura de banco de dados:

- Entender as características dos dados
- Avaliar as opções disponíveis
- Coletar e registrar métricas de desempenho de banco de dados
- Escolher o armazenamento de dados com base em padrões de acesso
- Otimizar o armazenamento de dados com base em padrões de acesso e métricas

### 7.15 Seleção de arquitetura de rede

A seleção da arquitetura de rede pode afetar positiva ou negativamente o desempenho e o comportamento da carga de trabalho, pois a rede conecta todos os seus componentes. Cargas como computação de alto desempenho (HPC) dependem especialmente desse desempenho. Determine requisitos de largura de banda, latência, *jitter* e throughput.

**Entenda como a rede afeta o desempenho.** A rede conecta componentes de aplicação, serviços de nuvem, redes de borda e dados no local. Latência, largura de banda, protocolos, local, congestionamento, *jitter*, throughput e regras de roteamento afetam tanto o desempenho da carga quanto a experiência do usuário.

**Avalie os recursos de rede disponíveis.** Avalie recursos de nuvem que possam aumentar o desempenho e meça seu impacto por testes, métricas e análises. Recursos de rede podem reduzir latência, distância de rede ou *jitter*.

**Escolha conectividade dedicada ou VPN de tamanho adequado para cargas de trabalho híbridas.** Quando recursos locais e de nuvem precisarem de uma rede comum, estime largura de banda e latência para definir o dimensionamento adequado das opções de conectividade.

**Aproveite o balanceamento de carga e o descarregamento de criptografia.** Balanceadores de carga melhoram a eficiência dos recursos de destino e a capacidade de resposta do sistema; o descarregamento de criptografia pode liberar recursos para outras tarefas.

**Escolha protocolos de rede para melhorar o desempenho.** Selecione protocolos que otimizem a carga conforme seus requisitos. A latência e a largura de banda afetam o throughput; por exemplo, latências maiores reduzem o throughput em transferências TCP. Use ajuste de TCP ou protocolos otimizados quando aplicável. O SRD, protocolo da AWS para Elastic Fabric Adapters (EFAs), permite entrega confiável de datagramas, inclusive fora de ordem, enviando pacotes em paralelo por caminhos alternativos para aumentar o throughput.

**Escolha o local da carga de trabalho com base nos requisitos de rede.** Avalie o posicionamento de recursos para reduzir latência e melhorar throughput, reduzindo tempos de carregamento de página e transferência de dados.

**Otimize a configuração da rede com base em métricas.** Configurações inadequadas afetam desempenho, eficiência e custo. Colete e analise dados do ambiente de rede, meça o impacto das alterações e use os resultados para orientar decisões futuras.

Práticas recomendadas para seleção da arquitetura de rede:

- Entender como a rede afeta o desempenho
- Avaliar os recursos de rede disponíveis
- Escolher conectividade dedicada ou VPN de tamanho adequado para cargas de trabalho híbridas
- Aproveitar o balanceamento de carga e o descarregamento de criptografia
- Escolher protocolos de rede para melhorar o desempenho
- Escolher o local da carga de trabalho com base nos requisitos de rede
- Otimizar a configuração da rede com base em métricas

### 7.16 Análise

A análise é a segunda área de práticas recomendadas de eficiência de desempenho.

### 7.17 Desenvolva sua carga de trabalho para aproveitar as novas versões

Ao arquitetar cargas de trabalho, há um número limitado de opções disponíveis em um momento específico. Com o tempo, novas tecnologias e abordagens podem melhorar o desempenho. Revise continuamente a carga de trabalho para aproveitar novas versões.

**Mantenha-se atualizado sobre novos recursos e serviços.** Avalie as melhorias de desempenho à medida que novos serviços, padrões de design e ofertas de produtos forem disponibilizados. Determine quais opções podem melhorar o desempenho ou a eficiência por meio de avaliação, discussão interna ou análise externa.

**Defina um processo para melhorar o desempenho da carga de trabalho.** Crie um processo de aprimoramento que avalie novos serviços, padrões de projeto, tipos de recursos e configurações. Por exemplo, execute testes de desempenho em novas ofertas de instância para verificar seu potencial de melhorar a carga.

**Desenvolva o desempenho da carga de trabalho ao longo do tempo.** Use as informações coletadas no processo de avaliação para promover ativamente a adoção de novos serviços ou recursos quando se tornarem disponíveis.

Práticas recomendadas para aproveitar as novas versões:

- Manter-se atualizado sobre novos recursos e serviços
- Definir um processo para melhorar o desempenho da carga de trabalho
- Desenvolver o desempenho da carga de trabalho ao longo do tempo

### 7.18 Monitoramento

O monitoramento é a terceira área de práticas recomendadas de eficiência de desempenho.

### 7.19 Monitorar os recursos para garantir o desempenho esperado

Após implementar a carga de trabalho, monitore os recursos para corrigir problemas ou desvios dos níveis de desempenho esperados.

**Registre métricas relacionadas ao desempenho.** Use serviços de monitoramento e observabilidade para registrar transações de banco de dados, consultas lentas, latência de E/S, throughput de solicitações HTTP, latência de serviço e outros dados relevantes.

**Analise as métricas quando ocorrerem eventos ou incidentes.** Use painéis ou relatórios de monitoramento para entender e diagnosticar o impacto de eventos, identificando as partes da carga de trabalho que não funcionam como esperado.

**Estabeleça KPIs para medir o desempenho da carga de trabalho.** Defina indicadores principais de desempenho que reflitam o resultado esperado. Por exemplo, uma API pode usar a latência geral de resposta; um site de comércio eletrônico pode usar o número de compras.

**Use o monitoramento para gerar notificações baseadas em alarme.** Configure o sistema para gerar alarmes automaticamente quando as medições de desempenho estiverem fora dos limites esperados.

**Analise as métricas em intervalos regulares.** Durante manutenções de rotina ou em resposta a eventos, revise as métricas coletadas. Identifique aquelas fundamentais para resolver problemas e as que poderiam ajudar a identificar, solucionar ou evitar novos problemas.

**Monitore e alarme proativamente.** Combine KPIs com monitoramento e alertas para tratar problemas de desempenho antecipadamente. Automatize ações corretivas quando possível e escale alarmes para pessoas capazes de responder quando a automação não for viável. Por exemplo, preveja valores esperados de KPIs e alerte sobre violações de limites, ou interrompa e reverta implantações automaticamente quando os KPIs saírem da faixa esperada.

Práticas recomendadas para monitorar recursos e garantir o desempenho esperado:

- Registrar métricas relacionadas ao desempenho
- Analisar as métricas quando ocorrerem eventos ou incidentes
- Estabelecer KPIs para medir o desempenho da carga de trabalho
- Usar o monitoramento para gerar notificações baseadas em alarme
- Analisar as métricas em intervalos regulares
- Monitorar e alarme proativamente

### 7.20 Concessões

As concessões são a última área de práticas recomendadas de eficiência de desempenho.

### 7.21 Usar concessões para melhorar o desempenho

O uso de concessões ao arquitetar soluções permite selecionar uma abordagem ideal. Muitas vezes, o desempenho pode melhorar ao trocar consistência, durabilidade e espaço por tempo e latência.

**Compreenda as áreas em que o desempenho é mais crítico.** Identifique onde aumentar o desempenho terá impacto positivo na eficiência ou na experiência do cliente. Por exemplo, um site com muita interação pode se beneficiar de serviços de borda que aproximem a entrega de conteúdo dos usuários.

**Saiba mais sobre padrões de design e serviços.** Pesquise padrões e serviços que melhoram o desempenho. Durante a análise, identifique o que pode ser negociado para obter maior desempenho. Um serviço de cache, por exemplo, pode reduzir a carga sobre bancos de dados, mas pode exigir engenharia para cache seguro ou introduzir consistência eventual em algumas áreas.

**Identifique como as concessões afetam os clientes e a eficiência.** Ao avaliar melhorias, determine quais opções afetam clientes e eficiência da carga. Se um armazenamento de dados de valor-chave aumentar o desempenho, por exemplo, avalie como sua natureza de consistência afetará os clientes.

**Meça o impacto das melhorias de desempenho.** Ao realizar alterações, avalie métricas e dados coletados para entender o efeito sobre a carga, seus componentes e clientes. Isso revela as melhorias obtidas e ajuda a detectar efeitos colaterais negativos.

**Use várias estratégias relacionadas ao desempenho.** Quando aplicável, combine estratégias como cache para evitar chamadas excessivas de rede ou banco de dados, réplicas de leitura para melhorar taxas de leitura, *sharding* ou compactação para reduzir volumes de dados e *buffering* ou streaming para evitar bloqueios.

Práticas recomendadas para usar concessões e melhorar o desempenho:

- Compreender as áreas em que o desempenho é mais crítico
- Saber mais sobre padrões de design e serviços
- Identificar como as concessões afetam os clientes e a eficiência
- Medir o impacto das melhorias de desempenho
- Usar várias estratégias relacionadas ao desempenho

### 7.22 Pergunta 1

Quais são as áreas de foco das perguntas do pilar de eficiência de desempenho? (Selecione TRÊS.)

- A Selecionar tipos de recursos corretos para computação, armazenamento, banco de dados e rede.
- B Recuperar facilmente de falhas.
- C Analisar sua seleção à medida que a AWS continua a inovar.
- D Fazer concessões de arquitetura para maximizar a eficiência.
- E Estar ciente do desempenho de seus recursos por meio de dias de teste e testes.
- F Manter a confidencialidade e a integridade dos dados.

**Resposta: A, C, D.** Selecionar os tipos corretos de recursos; analisar sua seleção conforme a AWS inova; e fazer concessões de arquitetura para maximizar a eficiência.

### 7.23 Pergunta 2

Qual desses é um exemplo de prática recomendada de eficiência de desempenho em computação, armazenamento, banco de dados e rede?

- A Selecionar o tipo de recurso mais barato.
- B Selecionar o tipo de recurso maior.
- C Selecionar o tipo de recurso menor.
- D Selecionar o tipo de recurso apropriado.

**Resposta: D.** Selecionar o tipo de recurso apropriado.

### 7.24 Pergunta 3

Qual é um exemplo de prática recomendada de eficiência de desempenho em concessões?

- A Armazenar dados em cache em uma Zona de Disponibilidade.
- B Posicionar recursos ou dados armazenados em cache mais perto dos usuários finais.
- C Criptografar o armazenamento.
- D Usar mais instâncias.

**Resposta: B.** Posicionar recursos ou dados armazenados em cache mais perto dos usuários finais.

### 7.25 Resumo do Módulo 7

Neste módulo, você aprendeu sobre o pilar de eficiência de desempenho. Iniciamos com uma visão geral e incluímos uma discussão aprofundada sobre a proposta de valor, os princípios de design e as práticas recomendadas desse pilar.

Neste módulo, você:

- Teve uma visão geral do pilar de eficiência de desempenho
- Aprendeu sobre a proposta de valor para a eficiência de desempenho
- Conheceu os diferentes princípios de design do pilar de eficiência de desempenho
- Aprendeu sobre as práticas recomendadas do pilar de eficiência de desempenho

<a id="modulo-8"></a>

## Módulo 8 — Análise detalhada do pilar de otimização de custos

### 8.1 Boas-vindas!

Boas-vindas ao módulo oito do AWS Well-Architected: Análise detalhada do pilar de otimização de custos.

### 8.2 Objetivos de aprendizado

Neste módulo, você terá uma visão geral do pilar de otimização de custos do AWS Well-Architected Framework. Também aprenderá os princípios de design e as práticas recomendadas desse pilar.

Neste módulo, você:

- Terá uma visão geral do pilar de otimização de custos do AWS Well-Architected Framework
- Aprenderá sobre os princípios de design e as práticas recomendadas do pilar de otimização de custos

### 8.3 Otimização de custos

Para começar, você terá uma visão geral do pilar de otimização de custos.

### 8.4 Pilares do Well-Architected

Atualmente, há seis pilares do AWS Well-Architected Framework: excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. Esses pilares são os fundamentos da arquitetura de suas soluções de tecnologia na nuvem.

Este módulo se concentrará no pilar de otimização de custos.

- **01 Excelência operacional**
- **02 Segurança**
- **03 Confiabilidade**
- **04 Eficiência de desempenho**
- **05 Otimização de custos**
- **06 Sustentabilidade**

### 8.5 O que é o pilar de otimização de custos?

> Uma carga de trabalho com custo otimizado utiliza totalmente todos os recursos, alcança o resultado com o menor preço possível e atende aos requisitos funcionais.

Assim como nos demais pilares do AWS Well-Architected Framework, há concessões a serem consideradas na otimização de custos. Por exemplo, pode haver uma escolha entre velocidade de entrada no mercado e custo: em alguns casos, é melhor otimizar a velocidade, enviando novos recursos ou cumprindo um prazo, em vez de investir na otimização inicial de custos.

Às vezes, as decisões de design são direcionadas pela pressa, e não pelos dados. Há a tentação de provisionar em excesso em vez de gastar tempo com *benchmarking* para alcançar a implantação mais econômica. Embora implantações excessivamente provisionadas e subutilizadas possam ser uma alternativa razoável ao migrar rapidamente um ambiente *on-premises* para a nuvem, investir uma quantidade adequada de esforço em uma estratégia de otimização de custos desde o início ajuda a perceber mais rapidamente seus benefícios econômicos.

Adote de forma consistente as práticas recomendadas e evite o excesso de provisionamento de recursos. As próximas seções apresentam técnicas e práticas recomendadas para implementar o gerenciamento financeiro na nuvem (Cloud Financial Management — CFM) e a otimização de custos para as cargas de trabalho.

### 8.6 Princípios de design de otimização de custos

Agora que você já sabe o que é o pilar de otimização de custos, vai se aprofundar nos princípios de design desse pilar.

### 8.7 Princípios de design de otimização de custos

Vários princípios podem ajudar você a otimizar os custos na nuvem:

- ****Praticar o gerenciamento financeiro na nuvem.**:** Para alcançar o sucesso financeiro e o valor comercial na nuvem, pratique o gerenciamento financeiro na nuvem (Cloud Financial Management — CFM). A organização deve dedicar tempo e recursos para desenvolver capacidade nesse domínio, por meio de conhecimento, programas, recursos e processos.
- ****Adotar um modelo de consumo.**:** Pague apenas pelos recursos de computação que consome e aumente ou diminua o uso conforme os requisitos empresariais. Por exemplo, ambientes de desenvolvimento e teste usados somente oito horas por dia durante a semana podem ser interrompidos quando não forem necessários, com potencial de economia de até 75% em comparação ao uso contínuo de 168 horas. Meça também a eficiência geral, monitorando o resultado comercial da carga de trabalho e seus custos associados à entrega.
- ****Avaliar a eficiência geral.**:** Use os dados de custo e de resultado comercial para entender os ganhos obtidos ao aumentar a produção ou a funcionalidade e ao reduzir custos.
- ****Parar de gastar dinheiro com trabalho pesado indiferenciado.**:** A AWS realiza o trabalho pesado das operações de data center, como armazenamento, alimentação e implementação de servidores, removendo a sobrecarga operacional de gerenciar sistemas e aplicações por meio de serviços gerenciados. Assim, a equipe pode se concentrar nos clientes e nos projetos de negócio, e não na infraestrutura.
- ****Analisar e atribuir despesas.**:** A nuvem ajuda a identificar com precisão o custo e o uso das cargas de trabalho e a atribuir os custos de TI de forma transparente aos proprietários. Isso permite medir o retorno sobre o investimento (ROI) e oferece aos responsáveis pelas cargas de trabalho a oportunidade de otimizar recursos e reduzir custos.

### 8.8 Áreas de práticas recomendadas de otimização de custos

Agora que você entende os princípios de design de otimização de custos, aprenderá sobre as práticas recomendadas desse pilar.

### 8.9 Áreas de práticas recomendadas de otimização de custos

O pilar de otimização de custos está agrupado em cinco áreas de práticas recomendadas:

- **01 Prática de gerenciamento financeiro na nuvem**
- **02 Conscientização sobre despesas e uso**
- **03 Recursos econômicos**
- **04 Gerenciamento de recursos de oferta e demanda**
- **05 Otimização ao longo do tempo**

### 8.10 Prática de gerenciamento financeiro na nuvem

A prática de gerenciamento financeiro na nuvem é a primeira área de práticas recomendadas de otimização de custos.

### 8.11 Prática de gerenciamento financeiro na nuvem

A prática de gerenciamento financeiro na nuvem, ou CFM, ajuda as organizações a obter valor comercial e sucesso financeiro à medida que otimizam o custo e o uso para dimensionamento na AWS.

**Estabeleça uma função de otimização de custos.** Crie uma equipe, como um *Cloud Business Office* ou um *Cloud Center of Excellence*, responsável por estabelecer e manter a conscientização sobre custos em toda a organização. Ela deve incluir participantes das áreas de finanças, tecnologia e negócios.

**Estabeleça uma parceria entre finanças e tecnologia.** Envolva ambas as equipes nas discussões sobre custo e uso em todos os estágios da jornada para a nuvem. Realize reuniões regulares para discutir metas e objetivos organizacionais, custo e uso atuais, além de práticas financeiras e contábeis.

**Estabeleça orçamentos e previsões para a nuvem.** Ajuste os processos organizacionais de orçamento e previsão para que sejam compatíveis com a natureza altamente variável do custo e uso na nuvem. Os processos devem ser dinâmicos, usando algoritmos baseados em tendências ou direcionadores de negócios, ou uma combinação deles.

**Implemente a conscientização de custos nos processos da organização.** Considere os processos organizacionais novos e existentes que afetam o uso e inclua a conscientização de custos, inclusive no treinamento dos funcionários.

**Relate e notifique sobre a otimização de custos.** Configure o AWS Budgets para fornecer notificações de custo e uso em relação às metas. Realize reuniões periódicas para analisar a eficiência de custos da carga de trabalho e promover uma cultura consciente dos custos.

**Monitore os custos de forma proativa.** Implemente ferramentas e painéis de controle para a carga de trabalho. Não analise somente custos e categorias quando receber notificações: use esse acompanhamento para identificar tendências positivas e promovê-las em toda a organização.

**Mantenha-se atualizado com as novas versões do serviço.** Consulte regularmente especialistas ou parceiros da AWS para considerar quais serviços e recursos oferecem menor custo. Analise os AWS Blogs e outras fontes de informação.

**Crie uma cultura consciente dos custos.** Implemente mudanças ou programas em toda a organização. Comece aos poucos e, conforme seus recursos aumentarem e o uso da nuvem crescer, implemente programas maiores e mais abrangentes.

**Quantifique o valor comercial da otimização de custos.** Entenda todos os benefícios para a organização, pois a otimização de custos é um investimento necessário. A quantificação do valor comercial permite explicar o retorno do investimento às partes interessadas, obter mais adesão para futuros investimentos e criar um *framework* para medir os resultados das atividades de otimização de custos.

### 8.12 Conscientização sobre despesas e uso

A conscientização sobre despesas e uso é a próxima área de práticas recomendadas de otimização de custos. Compreender os custos e os motivadores de sua organização é fundamental para gerenciar custos e uso de forma eficaz e identificar oportunidades de redução de custos.

Em geral, organizações operam várias cargas de trabalho executadas por diferentes equipes. Essas equipes podem estar em unidades organizacionais distintas, cada uma com sua própria transmissão de receita. A capacidade de atribuir os custos dos recursos às cargas de trabalho, à organização individual ou aos proprietários dos produtos melhora a compreensão do uso eficiente e ajuda a reduzir desperdícios.

O monitoramento preciso do custo e do uso ajuda a entender a rentabilidade das unidades da organização e dos produtos, permitindo decisões mais informadas sobre onde alocar recursos. A conscientização do uso em todos os níveis organizacionais é essencial para promover mudanças, porque mudanças no uso geram mudanças no custo.

### 8.13 Governança

A governança estabelece políticas e mecanismos para garantir que os custos apropriados sejam incorridos enquanto os objetivos são alcançados. Ao equilibrar a governança, é possível inovar sem gastar demais.

**Desenvolva políticas com base nos requisitos da organização.** Defina como os recursos serão gerenciados. As políticas devem abranger aspectos de custo de recursos e cargas de trabalho, incluindo criação, modificação e desativação durante a vida útil do recurso.

**Implemente objetivos e metas.** Defina metas de custo e uso para a carga de trabalho. Os objetivos orientam a organização quanto aos resultados esperados, enquanto as metas estabelecem resultados mensuráveis específicos a serem alcançados.

**Implemente uma estrutura de contas.** Crie uma estrutura que corresponda à organização para alocar e gerenciar custos em toda a empresa.

**Implemente grupos e funções.** Estabeleça grupos alinhados às políticas para controlar quem pode criar, modificar ou desativar instâncias e recursos em cada grupo. Por exemplo, separe os grupos de desenvolvimento, teste e produção, tanto para serviços AWS como para soluções de terceiros.

**Implemente controles de custos.** Aplique controles com base nas políticas organizacionais e nos grupos e funções definidos, garantindo que os custos ocorram somente conforme os requisitos. Um exemplo é controlar o acesso a Regiões ou tipos de recurso usando políticas do AWS Identity and Access Management (IAM).

**Acompanhe o ciclo de vida do projeto.** Rastreie, meça e audite o ciclo de vida de projetos, equipes e ambientes para evitar o uso e o pagamento de recursos desnecessários.

### 8.14 Monitorar o custo e o uso

Monitore o custo e o uso para estabelecer políticas e procedimentos que permitam monitorar e alocar adequadamente seus custos, medir e melhorar a eficiência de custo da carga de trabalho.

**Configure fontes de informações detalhadas.** Para obter dados detalhados de custo e uso, configure a granularidade horária do AWS Cost and Usage Report e do AWS Cost Explorer. Configure a carga de trabalho para registrar cada resultado comercial fornecido.

**Adicione informações da organização para custo e uso.** Defina um esquema de marcação baseado na organização, nos atributos da carga de trabalho e nas categorias de alocação de custos, para filtrar e pesquisar recursos ou monitorar custo e uso nas ferramentas de gerenciamento. Aplique marcação consistente, sempre que possível, por finalidade, equipe, ambiente ou outros critérios relevantes.

**Identifique categorias de atribuição de custos.** Identifique as categorias organizacionais mais apropriadas para alocar custos dentro da organização.

**Estabeleça métricas da organização.** Determine as métricas necessárias para a carga de trabalho, como relatórios de clientes produzidos ou páginas da web fornecidas aos clientes.

**Configure ferramentas de Billing and Cost Management.** Ajuste serviços, ferramentas e recursos às políticas da organização para gerenciar e otimizar gastos. Eles ajudam a organizar e rastrear dados de custo e uso, a aumentar o controle por cobrança consolidada e permissões de acesso, e a planejar orçamentos e previsões, com recursos e otimizações de preço.

**Aloque custos com base em métricas de carga de trabalho.** Aloque custos por métricas ou resultados comerciais para medir a eficiência de custo. Implemente um processo para analisar o AWS Cost and Usage Report no Amazon Athena, que pode fornecer informações e capacidade de estorno.

### 8.15 Desativar recursos

Desative recursos para implementar o controle de mudanças e o gerenciamento de recursos desde o início do projeto até o fim da vida útil. Isso ajuda a garantir que recursos não utilizados sejam encerrados e o desperdício seja reduzido.

**Controle os recursos ao longo de sua vida útil.** Rastreie recursos e suas associações durante toda a vida útil. Defina e implemente um método para esse rastreamento; use marcação para identificar a carga de trabalho ou função do recurso.

**Implemente um processo de desativação.** Identifique e desative recursos não utilizados, incluindo aqueles invocados por eventos periódicos ou alterados no uso. A desativação pode ser periódica, manual ou automatizada. Projete a carga de trabalho para identificar e desativar recursos não críticos, desnecessários ou com baixa utilização.

**Desative recursos automaticamente.** Automatize a desativação sempre que possível para remover recursos não necessários no momento adequado.

**Aplique políticas de retenção de dados.** Defina políticas nos recursos compatíveis para tratar a exclusão de objetos conforme os requisitos da organização. Identifique e exclua recursos e objetos desnecessários ou órfãos que não são mais necessários.

### 8.16 Recursos econômicos

Recursos econômicos são a próxima área de práticas recomendadas de otimização de custos. Usar os serviços, os recursos e as configurações apropriados para suas cargas de trabalho é fundamental para a economia de custos.

### 8.17 Avaliar o custo ao selecionar serviços

Avalie o custo ao selecionar serviços. Serviços básicos como Amazon EC2, Amazon EBS e Amazon S3, assim como serviços gerenciados de nível superior, como Amazon RDS e Amazon DynamoDB, podem ser combinados para otimizar uma carga de trabalho em termos de custo. O uso de serviços gerenciados pode reduzir ou eliminar grande parte da sobrecarga administrativa e operacional, liberando tempo para aplicações e atividades de negócio.

**Identifique os requisitos de custo da organização.** Trabalhe com os membros da equipe para definir o equilíbrio entre otimização de custos e outros pilares, como desempenho e confiabilidade.

**Analise todos os componentes da carga de trabalho.** Verifique se todos os componentes são analisados, independentemente de tamanho ou custos atuais. O esforço de revisão deve refletir o benefício potencial, considerando custos atuais e projetados.

**Realize uma análise completa de cada componente.** Analise o custo geral de cada componente para a organização e calcule o custo total de propriedade, incluindo custos de operações e gerenciamento, especialmente ao utilizar serviços gerenciados pelo provedor de nuvem.

**Selecione um software com licenciamento econômico.** O software de código aberto elimina custos de licenciamento que podem ser significativos. Quando o software licenciado for necessário, evite licenças vinculadas a atributos arbitrários, como CPUs; prefira licenças vinculadas a produtos ou resultados. O custo da licença deve ser proporcional ao benefício que ela entrega.

**Selecione os componentes para otimizar o custo conforme as prioridades da organização.** Considere o custo de todos os componentes da carga de trabalho, incluindo serviços gerenciados de nível de aplicação ou sem servidor, contêineres ou arquitetura orientada a eventos. Minimize custos de licença adotando código aberto, software sem taxas de licença ou alternativas de menor custo.

**Realize análises de custo para diferentes usos ao longo do tempo.** Alguns serviços e recursos são mais econômicos em diferentes níveis de uso. Ao analisar os componentes conforme o uso projetado, a carga de trabalho pode permanecer econômica durante toda sua vida útil.

### 8.18 Selecionar o tipo, o tamanho e o número corretos de recursos

Selecione o tipo, o tamanho e o número corretos de recursos para garantir a configuração adequada para a tarefa e minimizar desperdícios.

**Faça a modelagem de custos.** Identifique os requisitos da organização, como necessidades comerciais e compromissos existentes. Execute a modelagem de custos para os custos gerais da carga de trabalho e de cada componente. Faça *benchmarks* em diferentes cargas previstas e compare custos; o esforço de modelagem deve refletir o benefício potencial, como quando o gasto é proporcional ao custo do componente.

**Selecione o tipo, o tamanho e o número de recursos com base nos dados.** Use dados sobre a carga de trabalho e suas características de recurso, incluindo computação, memória, *throughput* ou gravação intensiva. Normalmente, a escolha é baseada em uma versão anterior da carga de trabalho *on-premises*, na documentação ou em outras fontes de informação.

**Selecione o tipo, o tamanho e o número de recursos automaticamente com base nas métricas.** Use métricas de execução em tempo real para selecionar tipo e tamanho de recursos que otimizem custo. Provisione adequadamente *throughput*, computação, armazenamento e rede. Isso pode ser feito por meio de circuitos de feedback, como *Auto Scaling* ou código personalizado na carga de trabalho.

### 8.19 Selecionar o modelo de preço

Selecione o modelo de preço mais adequado aos recursos para minimizar despesas.

**Faça análises de modelos de preços.** Analise cada componente da carga de trabalho e determine se o componente ou recurso será executado por períodos prolongados, adequado a descontos por compromisso, ou se terá uso dinâmico e de curta duração, adequado a descontos de curto prazo. Avalie a carga de trabalho com recomendações das ferramentas de gerenciamento de custos e aplique regras de negócios para obter altos retornos.

**Implemente Regiões com base no custo.** O preço dos recursos varia conforme a Região. Identifique diferenças de custo regionais e implante somente em Regiões de custos mais altos quando for necessário atender a requisitos de latência e soberania de dados. Considerar a Região ajuda a pagar o menor preço gerando valor à carga de trabalho.

**Selecione contratos de terceiros com termos econômicos.** Escolha contratos e preços dimensionados de acordo com os benefícios proporcionados à organização.

**Implemente modelos de preços para todos os componentes da carga de trabalho.** Recursos com execução permanente devem usar capacidade reservada, como Savings Plans ou instâncias reservadas. Capacidade de curto prazo e configurada pode usar instâncias Spot ou frotas Spot. Instâncias sob demanda são mais adequadas para cargas de trabalho de curto prazo que não podem ser interrompidas e não são executadas por tempo suficiente para capacidade reservada — geralmente entre 25% e 75% do período, conforme o tipo de recurso.

**Realize a análise do modelo de preços no nível da conta de gerenciamento.** Explore as ferramentas de Billing and Cost Management e considere descontos recomendados, compromissos e reservas para realizar análises regulares nesse nível.

### 8.20 Planejar a transferência de dados

Planeje a transferência de dados para monitorar as cobranças e tomar decisões arquitetônicas que minimizem custos. Uma pequena mudança arquitetônica pode reduzir diretamente os custos operacionais ao longo do tempo.

**Realize modelagem de transferência de dados.** Reúna os requisitos da organização e modele a transferência de dados da carga de trabalho e de cada componente para identificar a alternativa de menor custo conforme os requisitos atuais.

**Selecione componentes para otimizar o custo de transferência de dados.** Escolha todos os componentes e projete a arquitetura para reduzir custos de transferência. Isso inclui opções como otimização de rede de longa distância (WAN) e diferentes configurações de Zona de Disponibilidade.

**Selecione serviços para reduzir os custos de transferência de dados.** Use serviços adequados, como Amazon CloudFront para entregar conteúdo aos usuários finais, camadas de cache usando Amazon ElastiCache ou Amazon DynamoDB, ou AWS Direct Connect em vez de uma VPN para conexão com a AWS, quando apropriado.

### 8.21 Gerenciar recursos de oferta e demanda

Gerenciar a demanda e os recursos de suprimento é a próxima área de práticas recomendadas de otimização de custos. Na nuvem, você paga apenas pelo que precisa e pode fornecer recursos para atender à demanda da carga de trabalho no momento necessário, eliminando a necessidade de provisionamento excessivo.

Também é possível tratar a demanda com limitadores, *buffers* ou filas, suavizando-a e atendendo-a com menos recursos. O fornecimento *just-in-time* deve ser equilibrado com a necessidade de provisionamento, levando em conta falhas de recursos, alta disponibilidade e tempo de fornecimento.

Dependendo de a demanda ser fixa ou variável, planeje métricas e automação que mantenham o gerenciamento do ambiente no mínimo necessário, mesmo com mudanças na demanda. Ao modificá-la, saiba qual atraso máximo aceitável a carga de trabalho pode tolerar.

### 8.22 Gerenciar recursos de oferta e demanda

Gerencie recursos de oferta e demanda para que a carga de trabalho tenha gasto e desempenho equilibrados. O uso significativamente menor ou maior que o necessário pode afetar os custos operacionais, seja por desempenho degradado devido à utilização excessiva, seja por desperdício devido ao provisionamento em excesso.

**Realize análises sobre a demanda de carga de trabalho.** Analise a demanda ao longo do tempo, verificando se a análise abrange tendências sazonais e representa com precisão as condições operacionais durante toda a vida útil da carga de trabalho. O esforço de análise deve refletir o benefício potencial.

**Implemente *buffer* ou limitador para gerenciar a demanda.** O *buffering* e a limitação modificam a demanda, suavizando picos. Limite tentativas quando os clientes fizerem novas solicitações e use *buffering* para armazenar solicitações e adiar o processamento. Verifique se os mecanismos foram projetados para que os clientes recebam resposta no tempo necessário.

**Forneça recursos dinamicamente.** Provisione recursos de forma planejada, conforme a demanda — por exemplo, por meio de *Auto Scaling* — ou conforme o tempo, quando a demanda for previsível. Esses métodos reduzem tanto o excesso quanto a falta de provisionamento.

### 8.23 Otimizar ao longo do tempo

Otimizar ao longo do tempo é a próxima área de práticas recomendadas de otimização de custos. Avalie novos serviços e implemente-os na carga de trabalho. À medida que a AWS lança novos serviços e recursos, revise as decisões de arquitetura existentes para garantir que continuem econômicas. Conforme os requisitos mudarem, desative recursos, componentes e cargas de trabalho que deixarem de ser necessários.

### 8.24 Otimizar ao longo do tempo

À medida que a AWS lança novos serviços e recursos, revise as decisões de arquitetura existentes para garantir que continuem sendo as mais econômicas.

**Desenvolva um processo de análise da carga de trabalho.** Defina critérios e o processo de análise. O esforço deve refletir o benefício potencial: por exemplo, cargas de trabalho essenciais ou que representem mais de 10% da conta devem ser analisadas trimestralmente; cargas abaixo de 10% podem ser revisadas anualmente.

**Revise e analise a carga de trabalho regularmente.** Avalie as cargas existentes conforme um processo definido para identificar novos serviços que podem ser adotados, serviços existentes que podem ser substituídos ou cargas que podem ser reestruturadas.

**Realize automações para operações.** Avalie o custo do esforço operacional na nuvem e quantifique a redução necessária para tarefas de administrador, implementando automação sempre que possível. Avalie tempo e custo do esforço operacional e automatize tarefas administrativas para reduzir o trabalho humano.

### 8.25 Pergunta 1

Qual destas áreas é o foco do pilar de otimização de custos?

- A Usar a computação sem servidor.
- B Usar recursos econômicos.
- C Controlar e entender onde seu dinheiro está sendo gasto por meio de testes regulares.
- D Usar concessões.

**Resposta: B.** Usar recursos econômicos.

### 8.26 Pergunta 2

Qual é uma prática recomendada de otimização de custos na conscientização das despesas?

- A Gerenciar o acesso criando políticas de usuário.
- B Solicitar que um terceiro analise as despesas.
- C Usar o gerenciador de gastos para reduzir custos de transferência de dados.
- D Usar o AWS Cost Explorer para categorizar e acompanhar custos da AWS.

**Resposta: D.** Usar o AWS Cost Explorer para categorizar e acompanhar custos da AWS.

### 8.27 Resumo do Módulo 8

Neste módulo, você:

- Teve uma visão geral do pilar de otimização de custos.
- Aprendeu sobre a proposta de valor para otimização de custos.
- Conheceu os diferentes princípios de design do pilar de otimização de custos.
- Aprendeu as práticas recomendadas do pilar de otimização de custos.

<a id="modulo-9"></a>

## Módulo 9 — Análise detalhada do pilar de sustentabilidade

### 9.1 AWS Well-Architected

Boas-vindas ao módulo nove do AWS Well-Architected: Análise detalhada do pilar de sustentabilidade.

### 9.2 Objetivos de aprendizado

Neste módulo, você aprenderá sobre o pilar de sustentabilidade do AWS Well-Architected Framework. Você também aprenderá os princípios de design e as práticas recomendadas do pilar de sustentabilidade.

Neste módulo, você:

- Terá uma visão geral do pilar de sustentabilidade do AWS Well-Architected Framework
- Aprenderá sobre os princípios de design e as práticas recomendadas do pilar de sustentabilidade

### 9.3 Visão geral do pilar de sustentabilidade

Neste módulo, você aprenderá sobre o pilar de sustentabilidade do Well-Architected Framework e obterá exemplos práticos dos princípios de design usando elementos arquitetônicos da AWS.

### 9.4 Pilares do AWS Well-Architected

### 9.5 O que é o pilar de sustentabilidade?

O pilar de sustentabilidade aprimora o framework para fornecer uma maneira de medir consistentemente as arquiteturas em relação às práticas recomendadas de sustentabilidade e identificar áreas de melhoria, com foco na redução do consumo de energia das cargas de trabalho da AWS. Ele contém perguntas destinadas a ajudar os clientes a avaliar o design, a arquitetura e a implementação de suas cargas de trabalho para reduzir o consumo de energia e melhorar a eficiência. Muito mais do que uma simples lista de verificação, foi projetado para ser uma ferramenta que os clientes podem usar para acompanhar seu progresso em direção a políticas e práticas recomendadas que apoiam um futuro mais sustentável.

O pilar se concentra nas práticas recomendadas de sustentabilidade, que são entender, quantificar e aplicar. Ao criar cargas de trabalho na nuvem, a prática da sustentabilidade consiste em compreender os impactos dos serviços usados, quantificar os impactos durante todo o ciclo de vida da carga de trabalho e aplicar princípios de design e práticas recomendadas para reduzir esses impactos. Este módulo concentra-se nos impactos ambientais, especialmente no consumo e na eficiência de energia, pois são alavancas importantes para que os arquitetos informem a ação direta para reduzir o uso de recursos.

**Por que a sustentabilidade é importante para melhorar sua arquitetura?**

Ao pensar em sustentabilidade nas arquiteturas de seus clientes, é importante lembrar que a sustentabilidade é uma troca, assim como muitos dos outros pilares do AWS Well-Architected. Também é importante entender que, quando se trata de aprimorar as arquiteturas por meio da sustentabilidade, o modelo de responsabilidade compartilhada frequentemente usado na discussão de outros pilares também se aplica aqui. A AWS é responsável por criar uma infraestrutura de nuvem que seja sustentável, e os clientes da AWS são responsáveis por aplicar as práticas recomendadas de arquitetura para a sustentabilidade em suas cargas de trabalho na nuvem.

Há vários motivos pelos quais a sustentabilidade pode ser uma consideração importante no aprimoramento das arquiteturas, incluindo:

- Demanda dos clientes
- Regulamentações governamentais
- Demanda dos funcionários
- Investimento de impacto
- Sustentabilidade como posicionamento competitivo

### 9.6 Sustentabilidade

Agora que você tem uma melhor compreensão do pilar de sustentabilidade, pode aprender mais sobre os componentes, começando com os princípios de design de sustentabilidade.

### 9.7 Princípios de design de sustentabilidade

Há seis princípios de design para a sustentabilidade na nuvem.

**O primeiro princípio de design é compreender seu impacto.** Meça o impacto de sua carga de trabalho na nuvem e modele o impacto futuro. Inclua todas as fontes de impacto, inclusive aquelas resultantes do uso de seus produtos pelo cliente e aquelas resultantes de sua eventual desativação e retirada. Compare a saída da produção com o impacto total de suas cargas de trabalho na nuvem revisando os recursos e as emissões necessárias por unidade de trabalho. Use esses dados para estabelecer KPIs, avaliar maneiras de melhorar a produtividade e, ao mesmo tempo, reduzir o impacto e estimar o impacto das mudanças propostas ao longo do tempo.

**Estabeleça metas de sustentabilidade** de longo prazo, como a redução dos recursos de computação e armazenamento necessários por transação. Modele o retorno do investimento de melhorias na sustentabilidade para as cargas de trabalho existentes, e forneça aos proprietários os recursos necessários para investir nas metas de sustentabilidade. Você também deve planejar o crescimento e arquitetar suas cargas de trabalho para que o crescimento resulte em uma intensidade de impacto reduzida, medida em relação a uma unidade apropriada, como por usuário ou por transação. As metas ajudam a apoiar as metas de sustentabilidade mais amplas de sua empresa ou organização, a identificar regressões e a priorizar áreas com potencial de melhoria.

**Para maximizar a utilização**, você pode dimensionar as cargas de trabalho e implementar um design eficiente. Isso pode ajudar a garantir uma alta utilização e a maximizar a eficiência energética do hardware subjacente. Dois hosts executados com 30% de utilização são menos eficientes do que um host executado com 60% devido ao consumo de energia da linha de base por host. Ao mesmo tempo, elimine ou minimize os recursos, o processamento e o armazenamento ociosos para reduzir a energia total necessária para alimentar sua carga de trabalho.

Você também deve **antecipar e adotar novas ofertas de hardware e software mais eficientes.** Apoie os aprimoramentos a montante que seus parceiros e fornecedores fazem para ajudá-lo a reduzir o impacto de suas cargas de trabalho na nuvem. Você pode monitorar e avaliar continuamente suas ofertas de software e projetar a flexibilidade para impulsionar a rápida adoção de novas tecnologias eficientes.

Outro princípio de design é **usar serviços gerenciados.** O compartilhamento de serviços em uma base de clientes ampla ajuda a maximizar a utilização de recursos, o que reduz a quantidade de infraestrutura necessária para proporcionar suporte a cargas de trabalho na nuvem. Por exemplo, os clientes podem compartilhar o impacto dos componentes comuns do data center, como energia e rede, migrando as cargas de trabalho para a nuvem AWS e adotando serviços gerenciados, como o AWS Fargate para contêineres sem servidor, em que a AWS opera o dimensionamento e é responsável por sua operação eficiente. Use serviços gerenciados que possam ajudar a minimizar o impacto, como mover automaticamente dados acessados com pouca frequência para o armazenamento frio com as configurações do Amazon S3 Lifecycle ou o Amazon EC2 Auto Scaling para ajustar a capacidade para atender à demanda.

Por fim, **reduza o impacto posterior de suas cargas de trabalho na nuvem**, diminuindo a quantidade de energia ou recursos necessários para usar seus serviços, facilite ou elimine a necessidade de os clientes atualizarem seus dispositivos para usar seus serviços. Você pode testar usando device farms para entender o impacto esperado e testar com clientes reais para entender o impacto real do uso de seus serviços.

Os seis princípios de design de sustentabilidade:

1. 1Compreender seu impacto
2. 2Estabelecer metas de sustentabilidade
3. 3Maximizar a utilização
4. 4Antecipar e adotar novas ofertas de hardware e software mais eficientes
5. 5Usar serviços gerenciados
6. 6Reduzir o impacto posterior de suas cargas de trabalho na nuvem

### 9.8 Sustentabilidade

Agora que você entende os princípios de design de sustentabilidade, você se aprofundará ainda mais nas práticas recomendadas de sustentabilidade.

### 9.9 Áreas de práticas recomendadas de sustentabilidade

Além dos princípios de design, há também seis áreas de práticas recomendadas nas quais se concentrar ao trabalhar para implementar a sustentabilidade na nuvem. Essas áreas de práticas recomendadas são: seleção de Região; alinhamento à demanda; padrões de software e arquitetura; padrões de dados; hardware e serviços; além de processo e cultura.

No restante deste módulo, você se aprofundará em cada uma dessas áreas de práticas recomendadas.

- **01 Seleção de Região**
- **02 Alinhamento à demanda**
- **03 Padrões de software e arquitetura**
- **04 Padrões de dados**
- **05 Hardware e serviços**
- **06 Processo e cultura**

### 9.10 Seleção de Região

A seleção de Região é a primeira área de práticas recomendadas de sustentabilidade que você explorará.

### 9.11 Seleção de Região

A escolha da Região para sua carga de trabalho afeta significativamente seus KPIs, inclusive o desempenho, o custo e a pegada de carbono. Para melhorar efetivamente esses KPIs, você deve escolher Regiões para suas cargas de trabalho com base nos requisitos de negócios e nas metas de sustentabilidade.

- Escolha a Região com base nos requisitos comerciais e nas metas de sustentabilidade.

### 9.12 Alinhamento à demanda

A próxima área de práticas recomendadas em sustentabilidade sobre a qual você aprenderá é o alinhamento à demanda.

### 9.13 Alinhamento à demanda

A maneira como os usuários consomem suas cargas de trabalho e outros recursos pode ajudá-lo a identificar melhorias para atender às metas de sustentabilidade.

**Dimensione a infraestrutura com a carga do usuário.** Uma maneira de fazer isso é dimensionar a infraestrutura para corresponder continuamente à carga do usuário e garantir que apenas os recursos mínimos necessários para dar suporte aos usuários sejam implantados. Usando a elasticidade da nuvem, você pode dimensionar sua infraestrutura dinamicamente para adequar o fornecimento de recursos de nuvem à demanda e evitar o excesso de provisionamento de capacidade em sua carga de trabalho.

**Alinhe os SLAs com as metas de sustentabilidade.** Para fazer isso, revise e otimize os SLAs de carga de trabalho com base em suas metas de sustentabilidade para minimizar os recursos necessários para dar suporte à sua carga de trabalho e, ao mesmo tempo, continuar atendendo às necessidades dos negócios.

**Interrompa a criação e a manutenção de ativos não utilizados.** Desative ativos não utilizados em sua carga de trabalho para reduzir o número de recursos de nuvem necessários para atender à sua demanda e minimizar o desperdício.

**Otimize o posicionamento geográfico das cargas de trabalho** para os locais dos usuários, reduzindo a distância que o tráfego de rede deve percorrer e diminuindo o total de recursos de rede necessários para dar suporte à sua carga de trabalho.

**Otimize os recursos dos membros da equipe** para minimizar o impacto da sustentabilidade ambiental e, ao mesmo tempo, atender às necessidades deles para as atividades realizadas.

**Implemente buffering ou limitação** para achatar a curva de demanda e reduzir a capacidade provisionada necessária para sua carga de trabalho.

Práticas recomendadas para alinhamento à demanda:

- Dimensionar a infraestrutura com a carga do usuário
- Alinhar os SLAs com as metas de sustentabilidade
- Interromper a criação e a manutenção de ativos não utilizados
- Otimizar o posicionamento geográfico das cargas de trabalho para os locais dos usuários
- Otimizar os recursos dos membros da equipe para as atividades realizadas
- Implementar buffering ou limitação para achatar a curva de demanda

### 9.14 Padrões de software e arquitetura

A próxima área de práticas recomendadas em sustentabilidade é a de padrões de software e arquitetura.

### 9.15 Padrões de software e arquitetura

Existem algumas práticas recomendadas para considerar os padrões de comportamento.

**Otimize o software e a arquitetura para trabalhos assíncronos e agendados.** Use padrões eficientes de software e arquitetura, como os orientados por filas, para manter uma utilização alta e consistente dos recursos implantados.

**Remova ou refatore componentes de carga de trabalho com pouco ou nenhum uso.** Você pode remover componentes que não são usados e não são mais necessários e refatorar componentes com pouca utilização para minimizar o desperdício em sua carga de trabalho.

**Otimize as áreas de código que consomem mais tempo ou recursos.** Você pode otimizar o código que é executado em diferentes componentes da sua arquitetura para minimizar o uso de recursos e, ao mesmo tempo, maximizar o desempenho.

**Otimize o impacto nos dispositivos e nos equipamentos dos clientes** compreendendo como eles são usados em sua arquitetura e empregando estratégias para reduzir o uso deles. Isso pode minimizar o impacto ambiental geral de sua carga de trabalho na nuvem.

A última prática recomendada é **usar padrões e arquiteturas de software que melhor suportem os padrões de acesso e armazenamento de dados.** Entenda como os dados são usados em sua carga de trabalho, consumidos por seus usuários, transferidos e armazenados. Você pode usar padrões e arquiteturas de software que melhor suportem o acesso e o armazenamento de dados para minimizar os recursos de computação, rede e armazenamento necessários para suportar a carga de trabalho.

Práticas recomendadas para padrões de software e arquitetura:

- Otimizar o software e a arquitetura para trabalhos assíncronos e agendados
- Remover ou refatorar componentes de carga de trabalho com pouco ou sem uso
- Otimizar as áreas de código que consomem mais tempo ou recursos
- Otimizar o impacto nos dispositivos e nos equipamentos dos clientes
- Usar padrões e arquiteturas de software que suportem padrões de acesso e armazenamento de dados

### 9.16 Padrões de dados

Agora, você vai se aprofundar na área de práticas recomendadas de padrões de dados em sustentabilidade.

### 9.17 Padrões de dados

A primeira prática recomendada para considerar padrões de dados é **implementar uma política de classificação de dados.** Você precisa classificar os dados para entender a importância deles para os resultados comerciais e escolher a camada de armazenamento com eficiência energética correta para armazenar os dados.

Além disso, **use tecnologias que suportem padrões de acesso e armazenamento de dados.** Isso pode minimizar os recursos provisionados e, ao mesmo tempo, dar suporte à sua carga de trabalho.

Outra prática recomendada é **usar políticas para gerenciar o ciclo de vida de seus conjuntos de dados** e aplicar automaticamente cronogramas de exclusão para minimizar os requisitos totais de armazenamento de sua carga de trabalho.

Você também pode **usar a elasticidade e a automação para expandir o armazenamento em bloco ou o sistema de arquivos** à medida que os dados crescem para minimizar o armazenamento total provisionado.

Outra prática recomendada é **remover dados desnecessários ou redundantes** para minimizar os recursos de armazenamento necessários para armazenar seus conjuntos de dados. Além disso, o **uso de sistemas de arquivos compartilhados ou armazenamento de objetos** pode ajudá-lo a evitar a duplicação de dados e promover uma infraestrutura mais eficiente para sua carga de trabalho.

Você pode **minimizar a movimentação de dados nas redes.** Use sistemas de arquivos compartilhados ou armazenamento de objetos para acessar dados comuns e minimizar o total de recursos de rede necessários para dar suporte à movimentação de dados para sua carga de trabalho.

Por fim, para minimizar o consumo de armazenamento, **faça backup dos dados somente quando for difícil recriá-los**, apenas dos dados que tenham valor comercial ou que sejam necessários para atender aos requisitos de conformidade. Examine as políticas de backup e exclua o armazenamento temporário que não agrega valor em um cenário de recuperação.

Práticas recomendadas para padrões de dados:

- Implementar uma política de classificação de dados
- Usar tecnologias que suportem padrões de acesso e armazenamento de dados
- Usar políticas para gerenciar o ciclo de vida de seus conjuntos de dados
- Usar a elasticidade e a automação para expandir o armazenamento em bloco ou o sistema de arquivos
- Remover dados desnecessários ou redundantes
- Usar sistemas de arquivos compartilhados ou armazenamento de objetos para acessar dados comuns
- Minimizar a movimentação de dados nas redes
- Fazer backup dos dados somente quando for difícil recriá-los

### 9.18 Hardware e serviços

A próxima área de práticas recomendadas em sustentabilidade é a de hardware e serviços.

### 9.19 Hardware e serviços

Procure oportunidades para reduzir os impactos de sustentabilidade da carga de trabalho fazendo alterações em suas práticas de gerenciamento de hardware.

As práticas recomendadas para considerar os padrões de hardware incluem **usar a quantidade mínima de hardware para atender às suas necessidades** de forma eficiente e **usar tipos de instância com o menor impacto.** Monitore e use continuamente novos tipos de instância para aproveitar as melhorias na eficiência energética.

Outra prática recomendada é **usar serviços gerenciados** para operar com mais eficiência na nuvem.

Além disso, **otimize o uso de aceleradores de computação baseados em hardware** para reduzir as demandas de infraestrutura física de sua carga de trabalho.

Práticas recomendadas para hardware e serviços:

- Usar a quantidade mínima de hardware para atender às suas necessidades
- Usar tipos de instância com o menor impacto
- Usar serviços gerenciados
- Otimizar seu uso de aceleradores de computação baseados em hardware

### 9.20 Processo e cultura

A última área de práticas recomendadas de sustentabilidade que você explorará é a de processo e cultura.

### 9.21 Processo e cultura

Procure oportunidades de reduzir seu impacto na sustentabilidade fazendo alterações em suas práticas de desenvolvimento, teste e implantação. Práticas recomendadas incluem adotar métodos e processos para validar possíveis melhorias, minimizar os custos de testes e fornecer pequenas melhorias.

**Adote métodos que possam apresentar rapidamente melhorias de sustentabilidade.**

**Mantenha sua carga de trabalho atualizada** para adotar recursos eficientes, eliminar problemas e melhorar a eficiência geral de sua carga de trabalho.

Outra prática recomendada é **aumentar a utilização de ambientes de criação** para desenvolver, testar e criar suas cargas de trabalho.

Por fim, **use Device Farms gerenciadas para testes**, testando com eficiência um novo recurso em um conjunto representativo de hardware.

Práticas recomendadas para processo e cultura:

- Adotar métodos que possam apresentar rapidamente melhorias de sustentabilidade
- Manter sua carga de trabalho atualizada
- Aumentar a utilização de ambientes de criação
- Usar Device Farms gerenciadas para testes

### 9.22 Pergunta 1

Quais dos fatores a seguir são motivadores para considerar a sustentabilidade ao aprimorar as arquiteturas? (Selecione TRÊS.)

- A Demanda de clientes
- B Desempenho
- C Posicionamento competitivo
- D Regulamentos governamentais
- E Economia de custos
- F Segurança

**Resposta: A, B, D.** Demanda de clientes, Desempenho e Regulamentos governamentais.

### 9.23 Pergunta 2

Qual dos seguintes é um princípio de design de sustentabilidade do Well-Architected?

- A Processo e cultura
- B Seleção regional
- C Revisão regular dos relatórios de custo e uso
- D Compreensão do seu impacto

**Resposta: D.** Compreensão do seu impacto.

### 9.24 Pergunta 3

Quais são as práticas recomendadas em relação aos padrões de hardware para a sustentabilidade? (Selecione TRÊS.)

- A Usar os tipos de instância com o menor custo.
- B Usar serviços gerenciados.
- C Usar tipos de instância com o menor impacto.
- D Usar a quantidade mínima de hardware para atender às suas necessidades.
- E Usar políticas para gerenciar o ciclo de vida de seus conjuntos de dados.
- F Otimizar as áreas de código que consomem mais recursos.

**Resposta: B, C, D.** Usar serviços gerenciados, usar tipos de instância com o menor impacto e usar a quantidade mínima de hardware para atender às suas necessidades.

### 9.25 Resumo do Módulo 9

Neste módulo, você aprendeu sobre o pilar de sustentabilidade. Iniciamos com uma visão geral e incluímos uma discussão aprofundada sobre a proposta de valor, os princípios de design e as práticas recomendadas do pilar de sustentabilidade.

Neste módulo, você:

- Teve uma visão geral do pilar de sustentabilidade
- Aprendeu sobre a proposta de valor da sustentabilidade
- Conheceu os diferentes princípios de design do pilar de sustentabilidade
- Aprendeu as práticas recomendadas do pilar de sustentabilidade

<a id="modulo-10"></a>

## Módulo 10 — Questionário

### 10.1 Pergunta 01/14

Por que o pilar de segurança é importante?

- A As cargas de trabalho na nuvem são inerentemente mais sustentáveis do que as alternativas típicas on-premises, pois usam tecnologia mais eficiente e utilizam recursos somente quando necessário. No entanto, as empresas podem modificar as cargas de trabalho para reduzir ainda mais o impacto.
- B Para operar sua carga de trabalho com segurança, você deve aplicar as práticas recomendadas abrangentes a todas as áreas de segurança.
- C Ele mede o resultado comercial da carga de trabalho e os custos associados ao seu fornecimento. Use essa medida para conhecer os ganhos obtidos com o aumento da produção ou da funcionalidade e com a redução de custos.
- D A criação e a operação de cargas de trabalho econômicas ajudam a obter resultados comerciais com o menor preço possível. Isso minimiza o desperdício de retrabalho de arquitetura e permite maior investimento em novas oportunidades de negócios ou tecnologia.

**Resposta: B.** O pilar de segurança reúne práticas recomendadas para operar a carga de trabalho com segurança em todas as suas áreas.

### 10.2 Pergunta 02/14

Quais são os princípios de design do pilar de otimização de custos? (Selecione TRÊS.)

- A Implementar gerenciamento financeiro da nuvem (CFM).
- B Implementar uma base de identidade sólida.
- C Analisar e atribuir despesas.
- D Aplicar segurança em todas as camadas.
- E Adotar um modelo de consumo.
- F Usar arquiteturas sem servidor.

**Resposta: A, C, E.** Gerenciamento financeiro da nuvem, atribuição de despesas e modelo de consumo são princípios de otimização de custos apresentados no módulo 8.

### 10.3 Pergunta 03/14

Quais são os princípios de design do pilar de confiabilidade? (Selecione TRÊS.)

- A Recuperar-se automaticamente de falhas.
- B Parar de tentar adivinhar a capacidade.
- C Avaliar a eficiência geral.
- D Democratizar tecnologias avançadas.
- E Adotar um modelo de consumo.
- F Dimensionar horizontalmente para aumentar a disponibilidade agregada da carga de trabalho.

**Resposta: A, B, F.** Recuperar-se de falhas, evitar estimativas de capacidade e dimensionar horizontalmente são princípios de design da confiabilidade.

### 10.4 Pergunta 04/14

Uma equipe encontra alguns problemas de alto risco e problemas de médio risco identificados em seu Plano de Melhoria. O que eles devem fazer com essas informações?

- A Criar um gráfico ou uma lista de todos os problemas de alto risco e de médio risco para ajudar a priorizar um ponto de partida.
- B Demitir o engenheiro que construiu parte da carga de trabalho que apresenta um problema de alto risco.
- C Enviar um e-mail para toda a empresa explicando que todos precisam se empenhar para corrigir os problemas identificados.
- D Pausar todo o plano de lançamento.

**Resposta: A.** Organizar os riscos altos e médios ajuda a definir por onde começar o plano de aprimoramento.

### 10.5 Pergunta 05/14

Qual é a definição do pilar de excelência operacional?

- A A excelência operacional ajuda a empresa a otimizar o desempenho superior e a implementar um monitoramento que garanta que o desempenho da arquitetura não se degrade com o tempo.
- B A excelência operacional é a capacidade de proteger dados, sistemas e ativos para aproveitar as vantagens das tecnologias de nuvem.
- C A excelência operacional é a capacidade de proteger dados, redes e bancos de dados contra riscos.
- D A capacidade de dar suporte ao desenvolvimento e executar cargas de trabalho de modo eficiente, obter informações sobre as operações e melhorar continuamente os processos e os procedimentos de suporte para proporcionar valor comercial.

**Resposta: D.** A excelência operacional relaciona a execução eficiente das cargas de trabalho ao aprendizado com as operações e à melhoria contínua.

### 10.6 Pergunta 06/14

O que um membro da equipe deve fazer antes de iniciar a análise do AWS Well-Architected Framework? (Selecione DUAS.)

- A Agendar imediatamente uma reunião com a equipe de engenharia.
- B Ler sobre o Well-Architected Framework e como fazer uma análise.
- C Agendar uma reunião de análise do Well-Architected Framework de 30 minutos e planejar a explicação do que é o Well-Architected por 5 minutos antes da análise.
- D Fazer uma lista de tudo o que está errado com a arquitetura proposta.
- E Entrar em contato com stakeholders que devem participar da reunião. Enviar informações sobre o Well-Architected Framework e explicar os benefícios de realizar uma análise do Well-Architected Framework e, em seguida, agendá-la.

**Resposta: B, E.** Conhecer o framework e envolver os stakeholders prepara a equipe para uma análise colaborativa.

### 10.7 Pergunta 07/14

Qual é a definição do pilar de confiabilidade?

- A A confiabilidade tem padrões específicos e práticas recomendadas a serem adotadas para atingir as metas de sustentabilidade, antipadrões a serem evitados e terminologia para ajudar na comunicação com outras pessoas. O pilar também ajudará a identificar metas para reduzir o impacto e identificar as estruturas organizacionais necessárias para o sucesso a longo prazo.
- B A capacidade de uma carga de trabalho de executar sua função pretendida de forma correta e consistente durante um período de tempo esperado.
- C A solução ideal para uma carga de trabalho específica varia, e as soluções geralmente combinam várias abordagens.
- D A criação e a operação de cargas de trabalho econômicas ajudam a obter resultados comerciais com o menor preço possível. Isso minimiza o desperdício de retrabalho de arquitetura e permite maior investimento em novas oportunidades de negócios ou tecnologia.

**Resposta: B.** Confiabilidade é executar a função pretendida corretamente e de modo consistente durante o período esperado.

### 10.8 Pergunta 08/14

Um arquiteto de soluções pretende realizar uma análise do AWS Well-Architected Framework para uma carga de trabalho que está programada para entrar em operação em breve. Um dos principais stakeholders envia um e-mail para explicar que a equipe está muito ocupada para dedicar tempo à análise porque está trabalhando com um cronograma apertado antes do lançamento. Qual é a melhor resposta?

- A Explicar que uma análise deve ser feita com antecedência para que haja tempo de identificar e resolver problemas para um lançamento tranquilo. Essa revisão identificará os possíveis riscos que podem ocorrer durante o lançamento. Se houver muitos itens identificados, a equipe pode optar por adiar a data de lançamento.
- B Postergar a análise para depois que o produto for lançado, para que a equipe tenha mais tempo para se envolver.
- C Explicar que é melhor entender os possíveis problemas antes do lançamento. Mesmo que eles não consigam implementar todas as alterações antes de entrar em operação, isso ajudará a equipe a criar um plano de ação para o futuro.
- D Encaminhar o caso a um gerente para obter mais recursos atribuídos ao projeto.

**Resposta: C.** Conhecer os riscos antes do lançamento permite planejar as melhorias, mesmo quando nem todas cabem no prazo atual.

### 10.9 Pergunta 09/14

Depois de usar a ferramenta do AWS Well-Architected na análise, o plano de aprimoramento identifica os problemas de alto e médio risco. O que é um problema de alto risco?

- A Um problema que pode afetar negativamente os negócios, mas é algo menor que não requer atenção imediata.
- B Um problema de arquitetura que precisa ser resolvido imediatamente e é considerado uma emergência.
- C Uma escolha de arquitetura e operação que a AWS descobriu que poderia ter um impacto negativo significativo em uma empresa, afetando as operações organizacionais, os ativos e os indivíduos.
- D Alto potencial de falha na arquitetura.

**Resposta: C.** Alto risco indica uma escolha de arquitetura ou operação com possível impacto negativo significativo.

### 10.10 Pergunta 10/14

Quais são os princípios de design do pilar de eficiência de desempenho? (Selecione TRÊS.)

- A Fazer experimentos com mais frequência.
- B Usar arquiteturas sem servidor.
- C Ativar a rastreabilidade.
- D Testar procedimentos de recuperação.
- E Democratizar tecnologias avançadas.
- F Parar de tentar adivinhar a capacidade.

**Resposta: A, B, E.** Experimentar, usar arquiteturas sem servidor e democratizar tecnologias avançadas são princípios de eficiência de desempenho.

### 10.11 Pergunta 11/14

Se uma equipe achar que não tem os recursos certos para ajudar a corrigir os problemas identificados na análise do AWS Well-Architected Framework, quais são as opções disponíveis para obter ajuda? (Selecione DUAS.)

- A Contratar uma agência de talentos para criar um novo anúncio de emprego. Se a equipe não tiver um gerente de conta da AWS, nem a experiência ou o tempo, ela poderá entrar em contato com os membros do Programa de parceiros do AWS Well-Architected.
- B Entrar em contato com um gerente de conta da AWS para obter suporte e orientação adicionais.
- C Entrar em contato com os Recursos Humanos.
- D Continuar o lançamento do produto e realizar a análise posteriormente.
- E Pausar o plano de lançamento até que eles tenham recursos disponíveis.

**Resposta: A, B.** O material indica os parceiros do AWS Well-Architected e o gerente de conta da AWS como fontes de apoio.

### 10.12 Pergunta 12/14

Por que o pilar de otimização de custos é importante?

- A É importante usar os recursos de computação de forma eficiente para atender aos requisitos, mantendo a eficiência à medida que a demanda muda e as tecnologias evoluem.
- B É importante proteger dados, sistemas e ativos para aproveitar as vantagens das tecnologias de nuvem que podem melhorar a segurança.
- C Ele ajuda a empresa a otimizar o desempenho superior e a colocar em prática o monitoramento para ajudar a garantir que o desempenho da arquitetura não se degrade com o tempo.
- D Uma carga de trabalho com custo otimizado utiliza totalmente todos os recursos, alcança o resultado com o menor preço possível e atende aos seus requisitos funcionais.

**Resposta: D.** A otimização de custos busca atender aos requisitos funcionais com uso adequado dos recursos e o menor preço possível.

### 10.13 Pergunta 13/14

Qual é a definição do pilar de eficiência de desempenho?

- A A eficiência do desempenho mede o resultado comercial da carga de trabalho e os custos associados ao seu fornecimento. Use essa medida para conhecer os ganhos obtidos com o aumento da produção ou da funcionalidade e com a redução de custos.
- B A eficiência do desempenho inclui a capacidade de executar sistemas para fornecer valor comercial com o menor preço possível.
- C A eficiência de desempenho concentra-se no uso eficiente dos recursos de computação para atender aos requisitos e em como manter a eficiência à medida que a demanda muda e as tecnologias evoluem.
- D A eficiência do desempenho é a capacidade de uma carga de trabalho de executar sua função pretendida de forma correta e consistente quando se espera que ela o faça.

**Resposta: C.** O pilar trata do uso eficiente dos recursos de computação e da manutenção dessa eficiência conforme a demanda e a tecnologia mudam.

### 10.14 Pergunta 14/14

Todos os principais stakeholders estão na sala para uma análise do AWS Well-Architected Framework. Quais são as próximas etapas que a equipe deve seguir? (Selecione TRÊS.)

- A Começar a planejar a logística, como pedido de almoço, para que os stakeholders se envolvam mais.
- B Garantir que não haja distrações na sala, como blocos de anotações, lousas, etc.
- C Garantir que eles tenham as ferramentas para incentivar uma sessão de brainstorming e um local dedicado para documentar perguntas ou itens de ação.
- D Realinhar o propósito de fazer a análise com uma abordagem sem culpabilidade.
- E Escolher algumas metas comerciais importantes que a equipe deve atingir a partir da arquitetura antes de fazer a análise.
- F Fazer uma lista de tudo o que pode estar errado com a arquitetura proposta.

**Resposta: C, D, E.** A análise precisa registrar ideias e ações, manter uma abordagem sem culpabilidade e considerar as metas comerciais da arquitetura.

### 10.15 Gabarito

| Pergunta | Resposta |
| --- | --- |
| 01 | B |
| 02 | A, C, E |
| 03 | A, B, F |
| 04 | A |
| 05 | D |
| 06 | B, E |
| 07 | B |
| 08 | C |
| 09 | C |
| 10 | A, B, E |
| 11 | A, B |
| 12 | D |
| 13 | C |
| 14 | C, D, E |

<a id="resumo-final"></a>

## Resumo final

O AWS Well-Architected Framework orienta a avaliação e a melhoria contínua das cargas de trabalho por meio de princípios de design, perguntas e práticas recomendadas.

- Os seis pilares são excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade.
- A análise considera as decisões de arquitetura, identifica riscos e ajuda a priorizar um plano de aprimoramento.
- A ferramenta do AWS Well-Architected permite registrar cargas de trabalho e análises, além de acompanhar marcos e planos de melhoria.
- Aprender as práticas recomendadas, medir a carga de trabalho e aprimorá-la forma um ciclo contínuo.
