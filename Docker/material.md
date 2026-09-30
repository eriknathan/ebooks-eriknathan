## Como usar este guia

- Use os capítulos 1 a 12 para estudar o conteúdo. A ordem segue o caminho de quem usa Docker no dia a dia: fundamentos, ciclo de vida do contêiner, imagens, Dockerfile, build, rede, dados, Compose, segurança, observabilidade, orquestração e produção.
- Vai prestar o **Docker Certified Associate (DCA)**? O capítulo 13 liga cada objetivo do roteiro oficial ao ponto do guia que o cobre e explica os tópicos legados que a prova ainda cobra (UCP, DTR, Docker Content Trust, devicemapper) e o Kubernetes pedido.
- Use a tabela **Decisão rápida** ao final de cada capítulo como cheat sheet: cada uma reúne situações típicas, a abordagem recomendada e os erros mais comuns naquele tema.
- Use as tabelas **Números de…** para revisar portas, códigos de saída, padrões de tempo e limites que aparecem em entrevistas, provas e incidentes.
- Use as **Pegadinhas e padrões recorrentes** (capítulo 14) para revisar os erros de conceito mais frequentes, como "EXPOSE publica a porta" ou "`docker system prune` apaga volumes".
- Use a **Referência rápida de comandos** (capítulo 15) como consulta de bancada.
- Use o **Autoteste** (capítulo 16) para revisão ativa: cada flashcard esconde a resposta até você clicar.
- Os blocos de código podem ser copiados e executados em um host com Docker Engine 29 ou Docker Desktop recente. Comandos que exigem Linux (namespaces, `iptables`, `/var/lib/docker`) estão indicados.

### Versões, números e atualizações

Os comportamentos e padrões deste guia foram conferidos na documentação oficial (docs.docker.com, github.com/docker e github.com/moby) em **setembro de 2026**. Nessa data, as versões correntes eram **Docker Engine 29.8** e **Docker Compose 5.5**. Limites comerciais (como os do Docker Hub) mudam com frequência: confirme na documentação antes de depender de um valor exato.

*Mudanças recentes que ainda não aparecem na maior parte dos cursos e tutoriais:*

- ***Engine 29 (nov/2025)**: o **containerd image store** passou a ser o padrão em instalações novas, no lugar dos storage drivers clássicos (`overlay2` e afins); o daemon exige **API v1.44 ou mais nova** (clientes do Docker 25 em diante); **cgroup v1** foi marcado como obsoleto, com suporte garantido até pelo menos maio de 2029; há suporte **experimental a nftables** como backend de firewall.*
- ***Compose v5 (dez/2025)**: a numeração pulou da 2.x para a 5.0 para não ser confundida com as antigas versões `2.x`/`3.x` do formato de arquivo. O builder interno foi removido e os builds do Compose passaram a ser delegados ao **Docker Bake**. O Compose também passou a ser usado como SDK por outras ferramentas.*
- ***O campo `version:` do `compose.yaml` é obsoleto**: o Compose sempre valida com o schema mais recente e emite um aviso se o campo existir.*
- ***Compose v1** (`docker-compose`, em Python) chegou ao fim da vida em 2023. O comando atual é `docker compose` (com espaço), um plugin da CLI.*
- ***Docker Hardened Images (DHI)**: desde 17/dez/2025, mais de mil imagens base mínimas e endurecidas são gratuitas e open source (Apache 2.0), com SBOM e provenance assinados.*
- ***Docker Content Trust** (Notary v1) foi aposentado. Para assinar imagens, use Sigstore/cosign ou Notation (capítulo 9). A prova do DCA ainda o cobra (capítulo 13).*
- ***Kubernetes** não usa mais o Docker Engine como runtime desde a versão 1.24 (remoção do dockershim), mas executa normalmente as imagens criadas com Docker, porque elas seguem o padrão OCI.*

Se você estuda por um livro ou curso mais antigo, a tabela **Informações desatualizadas em materiais antigos** (capítulo 14) lista o que mudou em instalação, storage drivers, Docker Machine, Compose, registries e Swarm.

### Método para resolver problemas com Docker

1. **Identifique a camada**: o problema é de build (Dockerfile, contexto, cache), de execução (processo, sinais, recursos), de rede (DNS, portas, firewall) ou de dados (volumes, permissões)? Cada camada tem comandos próprios.
2. **Leia o estado real, não o esperado**: `docker ps -a`, `docker inspect`, `docker logs` e `docker events` mostram o que aconteceu. O código de saída costuma dizer mais que a mensagem de erro.
3. **Reproduza no menor escopo**: `docker run --rm -it <imagem> sh` e um contêiner de diagnóstico na mesma rede (`nicolaka/netshoot`) isolam a causa.
4. **Prefira o recurso nativo**: healthcheck, restart policy, volumes nomeados, redes definidas pelo usuário, build secrets e multi-stage costumam resolver o que scripts caseiros tentam resolver.
5. **Contêiner é descartável**: se a correção exige entrar no contêiner e mudar algo à mão, a correção certa está no Dockerfile, no Compose ou na configuração.

### Mapa do guia

| Bloco | Capítulos | O que você deve dominar ao final |
|---|---|---|
| Fundamentos | 1 e 2 | Como um contêiner funciona no kernel, a arquitetura do Docker, o ciclo de vida, sinais, códigos de saída e depuração |
| Imagens e build | 3, 4 e 5 | Camadas, tags e digests, registries, Dockerfile, cache, multi-stage, BuildKit, Buildx, Bake e multiplataforma |
| Rede, dados e Compose | 6, 7 e 8 | Drivers de rede, DNS interno, publicação de portas, volumes e bind mounts, aplicações multi-contêiner com Compose |
| Segurança e operação | 9 e 10 | Superfície de ataque, capabilities, rootless, segredos, cadeia de suprimentos, limites, logs e troubleshooting |
| Orquestração e produção | 11 e 12 | Swarm, equivalências com Kubernetes, pipeline de CI/CD e checklist de produção |
| Certificação | 13 | Roteiro do DCA, recursos legados cobrados na prova (UCP, DTR, DCT, devicemapper) e Kubernetes no nível da prova |
| Revisão | 14, 15 e 16 | Pegadinhas, referência de comandos e flashcards |

---

## 1. Fundamentos de Contêineres e Arquitetura do Docker

> **Ideia central**: um contêiner **não é uma máquina virtual**. É um **processo comum do Linux** isolado por **namespaces**, limitado por **cgroups** e com um sistema de arquivos próprio montado a partir das **camadas de uma imagem**. Todos os contêineres de um host compartilham o **mesmo kernel**.

### Por que contêineres e por que Docker

#### Problemas que os contêineres resolvem

| Problema clássico | Como os contêineres ajudam | Onde no guia |
|---|---|---|
| "Na minha máquina funciona": desenvolvimento, testes e produção com versões diferentes de SO, bibliotecas e runtimes | A imagem carrega a aplicação **com** suas dependências; o mesmo artefato passa por todos os ambientes | Capítulos 3 e 12 |
| Servidores preparados à mão para muitas aplicações, em linguagens, bibliotecas e versões diferentes e conflitantes | Cada aplicação roda isolada com as próprias dependências; o host só precisa do Docker | Capítulos 1 e 4 |
| Instalação de servidores e deploys demorados, acionamentos de madrugada porque um serviço não sobe em outro servidor | Subir a aplicação é baixar a imagem e iniciar o contêiner, em segundos, em qualquer host compatível | Capítulos 2 e 11 |
| Pico de demanda inesperado (uma campanha de marketing, por exemplo) | Novas réplicas sobem em segundos; um orquestrador distribui e substitui contêineres | Capítulos 8 e 11 |
| Custo alto de datacenter e recursos ociosos | Muito mais aplicações por host do que com VMs, porque não há um sistema operacional por aplicação | Capítulos 1 e 10 |
| Montar ambiente de desenvolvimento com banco, fila e cache | Um `docker compose up` sobe tudo, igual para todo o time | Capítulo 8 |
| Configurar a mesma aplicação para vários ambientes | Configuração por variáveis de ambiente e segredos, sem mudar a imagem | Capítulos 8 e 9 |
| Integração e entrega contínuas (CI/CD) | Build reproduzível, testes no mesmo ambiente da produção, promoção da mesma imagem | Capítulo 12 |
| Experimentar uma ferramenta sem "sujar" a máquina | `docker run --rm` executa e descarta, sem instalar nada no host | Capítulo 2 |

#### Para quem o Docker é bom
- **Desenvolvedores**: liberdade para escolher linguagem, banco de dados e distribuição por projeto, e reproduzir o ambiente de produção na própria máquina.
- **Administradores de sistemas e SRE**: não é preciso preparar o servidor com as dependências de cada aplicação; o host pode ser físico ou virtual, e toda aplicação é operada da mesma forma (iniciar, parar, logs, limites).
- **A empresa**: transição mais rápida entre QA, homologação e produção (é a **mesma imagem**), menos hardware pelo melhor aproveitamento dos recursos e overhead bem menor que o da virtualização.
- **Arquiteturas de microsserviços**: dividir uma aplicação grande em partes pequenas, cada uma com seu ciclo de vida, fica muito mais viável quando cada parte é um contêiner.

#### A inovação do Docker
- **O Docker não inventou os contêineres.** Isolamento de processos existe no Unix há décadas (veja a linha do tempo mais adiante neste capítulo).
- A principal inovação foi de **experiência**: tornar essa tecnologia acessível a qualquer desenvolvedor ou administrador, sem anos de prática nem ferramentas caseiras. Isso veio de quatro peças:
  - o **Dockerfile**, uma receita em texto, versionável, para construir o ambiente;
  - a **imagem em camadas**, portátil e reaproveitável;
  - o **registry público** (Docker Hub) para compartilhar imagens;
  - uma **CLI e uma API simples**, resumidas no lema *build, ship, run*.
- O objetivo final não é "usar Docker": é entregar software melhor, mais confiável e mais rápido, com menor custo de desenvolvimento e implantação. O Docker é um meio muito eficiente para isso.

### O que é um contêiner

#### Definição
- Um **contêiner** é uma aplicação empacotada **junto com suas dependências** (bibliotecas, runtime, arquivos de configuração) e executada como um **processo isolado** que **compartilha o kernel** do sistema operacional do host, seja ele uma máquina física ou virtual.
- Por isso se fala em **virtualização em nível de sistema operacional**: o contêiner não emula hardware nem executa outro kernel; o kernel do host apenas **isola** o que o processo enxerga e **limita** o que ele consome.
- A imagem de um contêiner costuma ser **enxuta**, com só o necessário para a aplicação. Em execução, o **overhead** em relação à mesma aplicação rodando nativamente é **pequeno**: não há hypervisor nem sistema operacional convidado. O custo que existe vem principalmente da rede com NAT e do sistema de arquivos em camadas, e desaparece com `--network host` e volumes.

#### Os três pilares do kernel

| Mecanismo | O que faz | Exemplo prático |
|---|---|---|
| **Namespaces** | Isolam o que o processo **enxerga** | O contêiner vê só os próprios processos (PID 1 é a aplicação), a própria interface de rede e o próprio hostname |
| **cgroups** (control groups) | Limitam e medem o que o processo **consome** | `--memory 512m`, `--cpus 1.5`, `--pids-limit 200` |
| **Union filesystem / snapshotter** | Monta várias camadas somente leitura e uma camada gravável por cima | Dez contêineres da mesma imagem compartilham as camadas em disco; cada um tem só sua camada gravável |

- **Namespaces usados pelo Docker**: `pid` (processos), `net` (interfaces, rotas, portas), `mnt` (pontos de montagem), `uts` (hostname), `ipc` (memória compartilhada, filas), `user` (mapeamento de UID/GID, usado no modo rootless e no `userns-remap`) e `cgroup`.
- **cgroups v2** é a versão atual. O cgroup v1 está obsoleto desde o Engine 29.
- Complementos de segurança do kernel: **capabilities** (dividem o poder do root em partes), **seccomp** (filtra chamadas de sistema) e **AppArmor/SELinux** (controle de acesso obrigatório). Veja o capítulo 9.
- Em **macOS e Windows**, o Docker Desktop roda uma **máquina virtual Linux** leve; os contêineres Linux rodam dentro dela. Contêineres Windows nativos existem, mas exigem host Windows e imagens Windows.

#### Namespaces em detalhe
Os namespaces foram entrando no kernel Linux aos poucos, entre 2002 e 2020. Não chegaram todos de uma vez.

| Namespace | Isola | Kernel | Como se vê no Docker |
|---|---|---|---|
| `mnt` | Pontos de montagem e o sistema de arquivos raiz. É a **evolução do `chroot`**: um processo não enxerga montagens de outro namespace | 2.4.19 (2002) | Cada contêiner tem seu próprio `/`, montado a partir da imagem |
| `uts` | **Hostname** e nome de domínio NIS | 2.6.19 (2006) | `--hostname`; por padrão, o ID curto do contêiner |
| `ipc` | Memória compartilhada e semáforos System V e **filas de mensagens POSIX** | 2.6.19 (2006) | `--ipc` (`private`, `shareable`, `container:<nome>`, `host`) |
| `pid` | **Árvore de processos**: cada contêiner numera os próprios processos a partir do PID 1 | 2.6.24 (2008) | O mesmo processo tem um PID dentro do contêiner e **outro** no host |
| `net` | Interfaces, endereços, rotas, portas e regras de firewall | 2.6.24–2.6.29 (2008–2009) | Interface `eth0` própria em cada contêiner |
| `user` | Mapeamento de **UIDs e GIDs**: o root de dentro pode ser um usuário comum fora | 3.8 (2013) | Modo rootless e `userns-remap` (capítulo 9) |
| `cgroup` | Visão da hierarquia de cgroups | 4.6 (2016) | O contêiner enxerga só o próprio cgroup (padrão com cgroup v2) |
| `time` | Relógios de tempo desde o boot | 5.6 (2020) | Não usado pelo Docker por padrão |

- **O mesmo processo, dois PIDs**: dentro do contêiner, a aplicação aparece como PID 1; no host, com um PID comum. Veja com:

```bash
docker run -d --name teste alpine sleep 600
docker exec teste ps -o pid,comm          # dentro: sleep é o PID 1
docker inspect -f '{{.State.Pid}}' teste  # no host: PID real, por exemplo 48213
ps -o pid,comm -p "$(docker inspect -f '{{.State.Pid}}' teste)"   # Linux
```

- **Como a rede de um contêiner é montada** (driver bridge): o Docker cria um **par veth**, como um cabo virtual com duas pontas. Uma ponta fica **no namespace de rede do contêiner**, com o nome `eth0` e um IP da rede (ex.: `172.17.0.3/16`). A outra fica **no host**, com o nome `vethXXXXXXX`, e é ligada à **bridge `docker0`** (IP `172.17.0.1`, o gateway dos contêineres). No host, `ip addr` mostra `docker0` e as interfaces `veth*`. No contêiner, `ip addr` mostra só `lo` e `eth0`.
- **`nsenter`** (Linux) entra nos namespaces de um processo: `sudo nsenter -t <PID> -n ip addr` mostra a rede vista pelo contêiner, mesmo em imagens sem ferramentas.

#### cgroups e netfilter
- **cgroups** controlam e contabilizam **CPU, memória, I/O de disco, número de processos e acesso a dispositivos** (`/dev`) de cada contêiner. As flags `--memory`, `--cpus`, `--pids-limit`, `--device-read-bps` e `--device` usam esse mecanismo (capítulo 10). O trabalho começou no Google em 2006 e entrou no kernel 2.6.24, em 2008.
- **netfilter** é o subsistema de filtragem de pacotes do kernel, configurado por **iptables** ou **nftables**. O Docker cria regras automaticamente:
  - **MASQUERADE** (NAT de origem): o tráfego que sai dos contêineres (ex.: `172.17.0.0/16`) aparece para fora com o IP do host;
  - **DNAT** na chain `DOCKER`: o tráfego que chega a uma porta publicada (`-p 8080:80`) é redirecionado ao IP e à porta do contêiner;
  - chains de filtro (`DOCKER-USER`, `DOCKER-FORWARD` e outras) isolam redes e permitem regras do administrador (capítulo 6).
- Para ver as regras de NAT no Linux: `sudo iptables -t nat -L -n -v` (ou `sudo nft list ruleset` com o backend nftables, experimental no Engine 29).
- **Outros recursos do kernel usados pelo Docker**: capabilities, seccomp, AppArmor/SELinux (capítulo 9) e **overlayfs** para as camadas (capítulo 7).

#### Nativo, máquina virtual e contêiner lado a lado

```text
   Execução nativa         Máquinas virtuais               Contêineres
 +------+------+      +------------+------------+     +----------+----------+
 | App A| App B|      | App A      | App B      |     | App A    | App B    |
 +------+------+      | Bibliotecas| Bibliotecas|     | Bibliot. | Bibliot. |
 | Bibliotecas |      | SO convid. | SO convid. |     +----------+----------+
 | (comuns, com|      | + kernel   | + kernel   |     | Docker Engine       |
 |  conflitos) |      +------------+------------+     | (containerd + runc) |
 +-------------+      | Hypervisor              |     +---------------------+
 | SO do host  |      +-------------------------+     | SO do host (kernel  |
 | + kernel    |      | SO do host / hardware   |     | compartilhado)      |
 +-------------+      +-------------------------+     +---------------------+
 | Hardware    |      | Hardware                |     | Hardware            |
 +-------------+      +-------------------------+     +---------------------+
```

- **Nativo**: as aplicações dividem bibliotecas e versões, então atualizar uma pode quebrar a outra.
- **Máquina virtual**: cada aplicação ganha um **sistema operacional completo**, com kernel e hardware virtualizado. O isolamento é forte, mas cada VM consome memória e disco de um SO inteiro e leva tempo para dar boot.
- **Contêiner**: cada aplicação tem **as próprias bibliotecas**, mas todas usam o **kernel do host**. Não há SO convidado, então cabem muito mais aplicações no mesmo hardware.

#### Contêiner vs. máquina virtual

| Aspecto | Contêiner | Máquina virtual |
|---|---|---|
| Isolamento | Processo isolado; **kernel compartilhado** com o host | Sistema operacional completo sobre um hypervisor; **kernel próprio** |
| Tamanho típico | Megabytes | Gigabytes |
| Inicialização | Milissegundos a segundos (é só iniciar um processo) | Dezenas de segundos a minutos (boot do SO) |
| Densidade | Centenas por host | Dezenas por host |
| Fronteira de segurança | Mais fina: uma falha no kernel afeta todos | Mais forte: o hypervisor separa os kernels |
| Portabilidade | Imagem roda em qualquer host com runtime compatível e mesma arquitetura de CPU | Imagem de disco depende do hypervisor |
| Uso típico | Empacotar e executar aplicações, microsserviços, CI | Isolar sistemas inteiros, SOs diferentes, multi-tenant hostil |

- As duas tecnologias se combinam: em nuvem, é comum rodar contêineres **dentro** de VMs. Serviços como AWS Fargate usam microVMs (Firecracker) para isolar cada tarefa.
- Um contêiner Linux **não roda em kernel Windows** nem vice-versa, e uma imagem `amd64` não roda nativamente em `arm64` (precisa de emulação ou de uma imagem multiplataforma, capítulo 5).
- **"Roda em qualquer lugar que tenha Docker"** vale com duas condições: kernel do mesmo tipo (Linux, na quase totalidade dos casos) e arquitetura de CPU compatível. No macOS e no Windows, a imagem Linux roda porque o Docker Desktop fornece a VM Linux. O desempenho de referência é o do Linux nativo; no Desktop, o maior custo extra aparece em bind mounts de diretórios do host.
- **O contêiner não "emula" a aplicação nem o sistema**: a aplicação roda direto no kernel do host, só que isolada. É isso que resolve o "na minha máquina funciona": todas as dependências de espaço de usuário vão na imagem.

### Uma breve história dos contêineres e do Docker

#### Antes do Docker

| Época | Marco | O que trouxe |
|---|---|---|
| 1979 | **`chroot`** (Unix V7, depois BSD) | Muda o diretório raiz de um processo. Isola **só a visão do sistema de arquivos** |
| 2000 | **FreeBSD Jails** | Além do sistema de arquivos, isola **processos**, rede e usuários |
| Início dos anos 2000 | **Virtuozzo** (SWsoft, depois Parallels) | Contêineres comerciais para Linux, com painel de gerenciamento |
| 2004–2005 | **Solaris Zones** (Sun) | Contêineres no Solaris, com controle de recursos; só para Solaris |
| 2005 | **OpenVZ** | O núcleo do Virtuozzo como open source. Popularizou os **VPS** e as empresas de hospedagem, mas exigia um **kernel Linux com patch** |
| 2006–2008 | **cgroups** (engenheiros do Google) | Limite e contabilização de recursos por grupo de processos. Entrou no kernel 2.6.24 (2008); o Google já usava contêineres em seus datacenters |
| 2008 | **LXC** (Linux Containers) | Combina cgroups, namespaces e `chroot` no **kernel padrão, sem patch**. Teve contribuições de Virtuozzo, IBM e Google |

#### O nascimento do Docker
- **2008**: Solomon Hykes funda a **dotCloud**, uma PaaS (Platform as a Service) que aceitava várias linguagens, numa época em que muitas plataformas nasciam presas a uma só (o Heroku, por exemplo, começou só com Ruby). Por baixo, a dotCloud já executava as aplicações em contêineres.
- **Março de 2013**: a dotCloud abre o código do núcleo da plataforma na PyCon, com o nome **Docker**. As primeiras versões eram basicamente um **wrapper do LXC** com um sistema de arquivos em camadas (**AUFS**).
- O crescimento foi muito rápido: em poucos meses, milhares de estrelas no GitHub e centenas de contribuidores. Em **outubro de 2013**, a dotCloud passa a se chamar **Docker, Inc.**
- **Março de 2014 (Docker 0.9)**: o Docker troca o LXC pela **libcontainer**, biblioteca própria que fala diretamente com o kernel e que depois deu origem ao **runc**.
- **Junho de 2014 (Docker 1.0)**: primeira versão considerada **pronta para produção**, lançada junto com o **Docker Hub**. Empresas como o Spotify já o usavam em escala; AWS e Google passaram a suportá-lo em suas nuvens, e a Red Hat o incorporou ao **OpenShift**.
- Ser **open source** acelerou tudo: qualquer pessoa pode ler o código, relatar e corrigir problemas, e a base de testes é a comunidade inteira.

#### Do Docker 1.0 aos dias de hoje

| Ano | Marco |
|---|---|
| 2015 | Criação da **OCI** (Open Container Initiative); o Docker doa o formato de imagem e o **runc** |
| 2016 | **Swarm mode** embutido no Engine (Docker 1.12); Docker for Mac e Windows (hoje Docker Desktop) |
| 2017 | Numeração por data (17.03), edições CE e EE, projeto **Moby** e doação do **containerd** à CNCF |
| 2019 | O negócio Docker Enterprise é vendido à Mirantis; a Docker, Inc. foca em ferramentas para desenvolvedores |
| 2020–2021 | Especificação aberta do Compose; **Compose v2** reescrito em Go como plugin (`docker compose`); nova licença do Docker Desktop para empresas maiores |
| 2022 | Kubernetes 1.24 remove o dockershim e passa a usar containerd ou CRI-O diretamente; as imagens continuam compatíveis |
| 2023 | Fim do Compose v1; o BuildKit já é o builder padrão desde o Engine 23 |
| 2025 | **Engine 29** com containerd image store padrão; **Compose v5**; **Docker Hardened Images** gratuitas; Docker Machine arquivado |

### Arquitetura do Docker

#### Componentes

| Componente | Papel |
|---|---|
| **Docker CLI** (`docker`) | Cliente. Converte comandos em chamadas à **Docker Engine API** (REST) |
| **Docker daemon** (`dockerd`) | Servidor. Gerencia imagens, contêineres, redes, volumes e builds; expõe a API em um socket Unix (`/var/run/docker.sock`), named pipe (Windows) ou TCP com TLS |
| **containerd** | Runtime de alto nível (projeto CNCF). Gerencia o ciclo de vida dos contêineres, o download e o armazenamento de imagens (no Engine 29, também é o **image store** padrão) |
| **containerd-shim** | Processo que fica entre o containerd e cada contêiner; permite reiniciar o daemon sem matar os contêineres (com `live-restore`) e guarda o código de saída |
| **runc** | Runtime de baixo nível (referência da especificação OCI). Cria os namespaces e cgroups e executa o processo; sai logo depois |
| **BuildKit** | Motor de build padrão desde o Engine 23; executa Dockerfiles em paralelo, com cache avançado e segredos (capítulo 5) |
| **Plugins da CLI** | `docker compose`, `docker buildx`, `docker scout`, `docker init`, `docker debug` etc. são plugins instalados em `~/.docker/cli-plugins` ou no diretório do sistema |

- **Fluxo de um `docker run`**: CLI → API do `dockerd` → (baixa a imagem se faltar) → containerd → shim → runc → processo do contêiner. Depois que o runc sai, o shim continua como pai do processo.
- **Moby** é o projeto open source de onde vem o Docker Engine. **Docker Desktop** é o produto comercial para estações de trabalho (Engine, CLI, Compose, Buildx, Kubernetes opcional, interface gráfica e VM).

#### Padrões OCI

A **Open Container Initiative** mantém três especificações. É por causa delas que imagens criadas com Docker rodam em containerd, Podman, CRI-O e Kubernetes.

| Especificação | Define |
|---|---|
| **Image spec** | Formato da imagem: manifest, config e camadas (tarballs) |
| **Runtime spec** | Como um runtime (runc, crun, gVisor, Kata) executa um bundle de sistema de arquivos + configuração |
| **Distribution spec** | API HTTP para enviar e baixar imagens e artefatos de um registry |

#### Objetos do Docker

| Objeto | O que é | Comando principal |
|---|---|---|
| **Imagem** | Modelo somente leitura, em camadas, com o sistema de arquivos e os metadados (comando padrão, variáveis, usuário) | `docker image` |
| **Contêiner** | Instância em execução (ou parada) de uma imagem, com uma camada gravável própria | `docker container` |
| **Volume** | Área de dados persistente gerenciada pelo Docker, fora do ciclo de vida do contêiner | `docker volume` |
| **Rede** | Rede virtual que conecta contêineres entre si e ao mundo externo | `docker network` |
| **Registry** | Serviço que armazena e distribui imagens (Docker Hub, GHCR, ECR, Harbor) | `docker login`, `push`, `pull` |
| **Contexto** | Aponta a CLI para um daemon (local, remoto via SSH, Docker Desktop) | `docker context` |

### Instalação e configuração do daemon

#### Requisitos
- **O daemon roda nativamente só no Linux.** Em outros sistemas, a instalação sobe uma **VM Linux** e roda o daemon nela (é o que o Docker Desktop faz). O **cliente** (`docker`) existe para Linux, macOS e Windows e pode apontar para qualquer daemon.
- **Arquiteturas de 64 bits**: os pacotes oficiais cobrem `x86_64`/`amd64` e `arm64`, e, conforme a distribuição, `armhf` (arm/v7), `ppc64le` e `s390x`. Os pacotes oficiais de **32 bits para Raspbian** foram removidos no Engine 29. Os contêineres usam o mesmo kernel do host, então herdam a arquitetura dele.
- **Distribuição suportada**: em vez de um número mínimo de kernel, a documentação lista as **versões de cada distribuição** suportadas (em set/2026, por exemplo, Debian 13 "Trixie" e 12 "Bookworm"). Na prática, qualquer distribuição mantida tem kernel com namespaces, cgroups (de preferência **cgroup v2**) e **overlayfs**.
- **Conferir o host**: `uname -r` (versão do kernel), `uname -m` (arquitetura) e o script `check-config.sh` do repositório moby, que verifica as opções do kernel necessárias. Depois de instalar, `docker info` mostra o driver de cgroup, a versão do cgroup, o storage e avisos.

#### Formas de instalar

| Ambiente | Opção recomendada | Observações |
|---|---|---|
| Linux servidor | Pacotes oficiais `docker-ce`, `docker-ce-cli`, `containerd.io`, `docker-buildx-plugin`, `docker-compose-plugin` do repositório `download.docker.com` | Os pacotes `docker.io` das distribuições costumam estar atrasados. O script `get.docker.com` é prático, mas não é recomendado para produção |
| macOS / Windows | Docker Desktop | Roda uma VM Linux; no Windows usa WSL 2. Licença paga para empresas maiores (abaixo) |
| Linux desktop | Docker Desktop ou Engine | Docker Desktop no Linux também usa uma VM, separada do Engine do host |
| CI | Engine já instalado no runner, ou serviço `docker:dind` | Veja "Docker-in-Docker" no capítulo 12 |

- **Licença do Docker Desktop**: é gratuito para uso pessoal, educação, projetos open source não comerciais e empresas com **menos de 250 funcionários E menos de US$ 10 milhões de receita anual**. Acima disso, e para órgãos de governo, exige assinatura Pro, Team ou Business. O **Docker Engine** (Moby) é open source (Apache 2.0) e não tem essa restrição.
- **Verificar a instalação**: `docker version` (versões do cliente e do servidor, e da API), `docker info` (storage, cgroup, runtimes, registries, avisos) e `docker run --rm hello-world`.
- **Script de conveniência**: `curl -fsSL https://get.docker.com | sh` detecta a distribuição, configura o repositório oficial e instala a versão mais recente. A própria Docker o recomenda **só para teste e desenvolvimento**: ele não deixa escolher a versão e instala tudo sem confirmação. Em produção, use o repositório (abaixo) com versão controlada.

#### Instalação pelo repositório oficial (Debian e Ubuntu)
Procedimento atual para Debian (no Ubuntu, troque `debian` por `ubuntu` nas URLs). Remova antes os pacotes não oficiais que conflitam: `docker.io`, `docker-compose`, `docker-doc`, `podman-docker`, `containerd` e `runc`.

```bash
# 1. Chave GPG do repositório em /etc/apt/keyrings
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# 2. Repositório no formato deb822 (.sources)
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

# 3. Instalação do Engine, da CLI e dos plugins
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

- **Versão específica**: `apt list --all-versions docker-ce` e depois `sudo apt install docker-ce=<versão> docker-ce-cli=<versão> …`. Em servidores, fixe a versão para atualizar de forma planejada.
- **Fedora, RHEL e derivados**: mesmo princípio, com `dnf` e o repositório `download.docker.com/linux/<distro>/docker-ce.repo`.
- **Materiais antigos** mostram `apt-key adv --keyserver …` e o repositório `apt.dockerproject.org`. Os dois estão **obsoletos**: o `apt-key` foi descontinuado no Debian e no Ubuntu, e o repositório antigo foi desativado em favor do `download.docker.com`.

#### Pós-instalação no Linux
- **Serviço**: em distribuições atuais, o Docker é gerenciado pelo **systemd**: `sudo systemctl status docker`, `sudo systemctl start docker`, `sudo systemctl restart docker`. Os comandos antigos `service docker …` e `/etc/init.d/docker …` são de sistemas com SysV/Upstart. Logs do daemon: `journalctl -u docker.service`.
- **Por que `sudo`**: por padrão, o daemon escuta em um **socket Unix** (`/var/run/docker.sock`) que pertence ao **root** e ao grupo `docker`, e não em uma porta TCP.
- **Grupo `docker`**: adicionar um usuário ao grupo permite usar a CLI sem `sudo`, mas **equivale a dar root no host** (quem controla o daemon pode montar `/` em um contêiner). Em servidores compartilhados, prefira o **modo rootless** (capítulo 9).

```bash
sudo groupadd docker            # normalmente o pacote já cria o grupo
sudo usermod -aG docker "$USER" # adiciona o seu usuário
newgrp docker                   # ou saia e entre de novo na sessão
docker run --rm hello-world     # agora sem sudo
```

- **Iniciar no boot**: `systemctl enable --now docker.service containerd.service`.
- **Dados do daemon**: ficam em `/var/lib/docker` (e em `/var/lib/containerd` com o containerd image store). Mude com `data-root` no `daemon.json`.

#### O arquivo `daemon.json`
Configuração do daemon em `/etc/docker/daemon.json` (Linux) ou nas configurações do Docker Desktop. Opções mais usadas:

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "20m", "max-file": "5" },
  "live-restore": true,
  "default-address-pools": [{ "base": "10.200.0.0/16", "size": 24 }],
  "registry-mirrors": ["https://mirror.exemplo.com"],
  "features": { "containerd-snapshotter": true },
  "userns-remap": "default"
}
```

| Opção | Para que serve |
|---|---|
| `log-driver` / `log-opts` | Driver de log padrão e rotação (capítulo 10) |
| `live-restore` | Mantém os contêineres rodando enquanto o daemon é reiniciado ou atualizado (não funciona com Swarm) |
| `default-address-pools` | Faixas de IP usadas nas redes criadas pelo Docker; evita conflito com a rede corporativa ou a VPN |
| `registry-mirrors` | Espelho (pull-through cache) para o Docker Hub |
| `insecure-registries` | Registries sem TLS válido. Evite fora de laboratório |
| `features.containerd-snapshotter` | Liga ou desliga o containerd image store (padrão ligado em instalações novas do Engine 29) |
| `userns-remap` | Mapeia o root do contêiner para um usuário sem privilégio no host |
| `data-root` | Diretório de dados do daemon |
| `dns` | Servidores DNS padrão para os contêineres |

- Depois de alterar: `sudo systemctl restart docker` (ou `reload` para algumas opções, como `log-driver` de novos contêineres e `insecure-registries`). Uma opção definida ao mesmo tempo no `daemon.json` e como flag no `dockerd` impede o daemon de subir.

#### O daemon e suas opções
- **`dockerd`** é o binário do daemon, separado da CLI desde o Docker 1.12 (antes era `docker -d` e depois `docker daemon`). Ele roda em segundo plano como serviço e é o processo que controla imagens, contêineres, redes e volumes.
- As opções podem ir como **flags** (`dockerd --log-level debug`) ou, de preferência, no **`daemon.json`**, que é o lugar persistente e versionável. `dockerd --help` lista todas; `dockerd --validate` checa o arquivo de configuração.

| Opção (`daemon.json` / flag) | Para que serve |
|---|---|
| `bip` / `--bip 192.168.100.1/24` | IP e sub-rede da bridge `docker0` (padrão `172.17.0.1/16`) |
| `fixed-cidr` | Restringe a faixa de IPs que os contêineres recebem dentro da sub-rede da `docker0` |
| `default-address-pools` | Faixas usadas nas **redes criadas** pelo usuário e pelo Compose |
| `default-gateway` | Gateway padrão dos contêineres na bridge `docker0` |
| `hosts` / `-H` | Onde a API escuta: `unix:///var/run/docker.sock` (padrão), `tcp://IP:2376` (com TLS), `ssh` (lado do cliente) ou `fd://` (**socket activation do systemd**: o systemd abre o socket e o entrega ao daemon) |
| `tls`, `tlsverify`, `tlscacert`, `tlscert`, `tlskey` | TLS mútuo para a API em TCP |
| `dns`, `dns-search` | DNS e domínios de busca padrão dos contêineres |
| `ip-forward` | Liga o roteamento IP no host (padrão `true`); necessário para os contêineres saírem para a rede |
| `iptables` / `ip6tables` | Permite ao Docker gerenciar o firewall (padrão `true`). Desligar exige recriar à mão todo o NAT |
| `icc` | Comunicação entre contêineres na bridge `docker0` (padrão `true`). Em redes definidas pelo usuário, o equivalente é a opção `com.docker.network.bridge.enable_icc` |
| `default-ulimits` | `ulimit` padrão dos contêineres; `--ulimit` no `docker run` sobrepõe |
| `log-level` | Verbosidade do **log do próprio daemon** (`debug`, `info`, `warn`, `error`); `debug: true` liga o modo depuração |
| `storage-driver`, `storage-opts` | Driver e opções de armazenamento (as antigas `dm.*` do devicemapper não existem mais; com `overlay2` sobre XFS com `pquota`, `overlay2.size` limita a camada gravável) |

- **Conflito com o systemd**: em muitas distribuições, a unit do serviço já passa `-H fd://`. Definir `hosts` também no `daemon.json` impede o daemon de subir (a mesma opção em dois lugares). Para mudar os endpoints, crie um override (`systemctl edit docker`) que redefine o `ExecStart` sem o `-H`.
- **Depurar o daemon**: `journalctl -u docker -f` mostra os logs; `"debug": true` e `sudo kill -SIGHUP $(pidof dockerd)` recarregam algumas opções sem reiniciar.

#### Contextos e acesso remoto
- **`docker context`** guarda endpoints de daemons: `docker context create producao --docker "host=ssh://deploy@servidor"`, depois `docker context use producao` ou `docker --context producao ps`.
- **`DOCKER_HOST`** (variável de ambiente) sobrepõe o contexto atual, por exemplo `DOCKER_HOST=ssh://deploy@servidor`.
- **SSH** é a forma mais simples e segura de acessar um daemon remoto. A alternativa é TCP com **TLS mútuo** na porta **2376**. Expor a API na porta **2375** sem TLS equivale a dar root no host a qualquer um na rede; o Docker descontinuou esse modo (obsoleto desde o Engine 26).
- **Docker Machine** (`docker-machine`), que criava hosts Docker em VMs locais ou na nuvem, chegou ao fim da vida e teve o repositório arquivado em julho de 2025, assim como o antigo Docker Toolbox. Hoje, crie o host com a ferramenta de infraestrutura do seu ambiente (Terraform, cloud-init, console da nuvem), instale o Engine pelo repositório oficial e acesse com `docker context` via SSH. Nas estações de trabalho, o Docker Desktop substituiu os dois.

#### Docker Machine: o que era e o que usar hoje
Materiais de 2015 a 2019 dedicam um capítulo ao **Docker Machine**, ferramenta que, com um comando, criava uma VM (VirtualBox, VMware, Hyper-V) ou uma instância de nuvem (AWS, GCP, Azure, DigitalOcean), instalava o Docker (em VMs locais, com a distribuição mínima **boot2docker**), gerava certificados TLS e configurava a CLI local para usar esse daemon remoto na porta 2376. Ela chegou ao fim da vida e teve o repositório arquivado em julho de 2025. Vale entender o que cada comando fazia para reconhecer o equivalente atual:

| Docker Machine (descontinuado) | O que fazia | Equivalente atual |
|---|---|---|
| `docker-machine create --driver virtualbox dev` | Criava uma VM local com Docker | Docker Desktop, Colima, OrbStack ou Rancher Desktop; ou `multipass`/Lima + instalação do Engine |
| `docker-machine create --driver amazonec2 prod` | Criava uma instância na nuvem com Docker | Terraform/OpenTofu, CLI da nuvem ou console, com **cloud-init** instalando o Engine pelo repositório oficial |
| `docker-machine env prod` + `eval "$(…)"` | Exportava `DOCKER_HOST`, `DOCKER_TLS_VERIFY`, `DOCKER_CERT_PATH` | `docker context create prod --docker host=ssh://usuario@ip` e `docker context use prod` |
| `docker-machine ls` | Listava os hosts e a URL do daemon | `docker context ls` (e o inventário da nuvem) |
| `docker-machine ssh prod` | Abria SSH no host | `ssh usuario@ip` |
| `docker-machine ip prod` | Mostrava o IP | CLI da nuvem, saída do Terraform |
| `docker-machine stop/start/rm prod` | Controlava a VM | Hypervisor, CLI da nuvem, `terraform destroy` |
| `docker-machine inspect prod` | Mostrava driver, certificados e opções do Engine | `docker context inspect prod` e `docker info` no host |

- As variáveis `DOCKER_HOST`, `DOCKER_TLS_VERIFY` e `DOCKER_CERT_PATH` continuam valendo na CLI. Contextos são preferíveis porque ficam salvos com nome e não dependem da sessão do shell.
- **boot2docker** e o **Docker Toolbox** (que empacotava Machine + VirtualBox para Mac e Windows) também foram descontinuados.

#### Números de fundamentos

| Item | Valor |
|---|---|
| Socket padrão da API (Linux) | `/var/run/docker.sock` |
| Porta da API sem TLS (não usar) | **2375/tcp** |
| Porta da API com TLS | **2376/tcp** |
| Diretório de dados padrão | `/var/lib/docker` (e `/var/lib/containerd`) |
| Arquivo de configuração do daemon | `/etc/docker/daemon.json` |
| Configuração da CLI (credenciais, contexto atual) | `~/.docker/config.json` |
| API mínima aceita pelo Engine 29 | **v1.44** (Docker 25+) |
| Suporte a cgroup v1 | Obsoleto no Engine 29; mantido até pelo menos **maio de 2029** |
| Docker Desktop gratuito | Empresas com **< 250 funcionários e < US$ 10 mi** de receita, uso pessoal, educação, OSS não comercial |

### Decisão rápida — Fundamentos

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Isolar aplicações que confiam umas nas outras no mesmo host | Contêineres | Uma VM por aplicação |
| Isolar cargas de clientes diferentes e não confiáveis | VM (ou runtime com sandbox, como gVisor/Kata) por tenant | Confiar só no isolamento de namespaces |
| Usar Docker em um Mac ou Windows de trabalho | Docker Desktop (verificando a licença) ou alternativa com VM Linux | Esperar contêineres Linux sem VM |
| Operar um daemon em outro servidor | `docker context` com SSH | Abrir a porta 2375 |
| Criar um host Docker na nuvem | Terraform/cloud-init + repositório oficial + `docker context` | Docker Machine (descontinuado) |
| Redes do Docker precisam de outra faixa de IP | `bip` (bridge padrão) e `default-address-pools` (redes novas) no `daemon.json` | Editar regras de iptables à mão |
| Permitir que o time rode `docker` sem `sudo` em um servidor compartilhado | Modo rootless por usuário | Colocar todos no grupo `docker` |
| Atualizar o Engine sem derrubar os contêineres | `live-restore: true` | Reiniciar no horário de pico e torcer |
| Redes do Docker conflitando com a VPN | `default-address-pools` no `daemon.json` | Apagar e recriar redes até funcionar |
| Descobrir versão da API, storage e cgroup em uso | `docker info` e `docker version` | Ler só o `docker --version` (mostra apenas o cliente) |

---

## 2. Ciclo de Vida de Contêineres

> **Ideia central**: um contêiner vive enquanto o seu **processo principal (PID 1)** vive. Quando o PID 1 termina, o contêiner para, e o **código de saída** dele vira o código de saída do contêiner. Quase todo problema de "contêiner que não fica de pé" ou "que demora a parar" se explica pelo PID 1.

### Primeiros passos

#### O que acontece em um `docker run hello-world`
A imagem `hello-world` existe para testar a instalação. Ela imprime uma mensagem e termina.

```bash
docker container run hello-world     # forma agrupada
docker run hello-world               # forma curta, equivalente
```

1. A **CLI** envia o pedido à API do **daemon**.
2. O daemon procura a imagem `hello-world:latest` **no host**. Como ela não existe, baixa do **Docker Hub** (`Unable to find image … locally` e depois `Pulling from library/hello-world`), escolhendo a variante da arquitetura do host.
3. O daemon **cria um contêiner** a partir da imagem e o inicia; o processo imprime a mensagem.
4. O daemon envia a saída à CLI, que a mostra no terminal. O processo termina, e o contêiner fica no estado **`exited`** com código 0.

- Desde o Docker 1.13, os comandos são agrupados por objeto (`docker container …`, `docker image …`, `docker volume …`, `docker network …`). As formas curtas antigas (`docker run`, `docker ps`, `docker rmi`) continuam válidas e equivalentes.

#### Listar imagens e contêineres

| Coluna de `docker image ls` | Significado |
|---|---|
| `REPOSITORY` | Nome da imagem (com namespace e registry, se houver) |
| `TAG` | Rótulo da versão (`latest` se nada foi indicado) |
| `IMAGE ID` | Início do digest do config da imagem |
| `CREATED` | Há quanto tempo a imagem foi **construída** (não baixada) |
| `SIZE` | Tamanho descompactado das camadas |

| Coluna de `docker container ls` (`docker ps`) | Significado |
|---|---|
| `CONTAINER ID` | Identificador curto (12 caracteres) do contêiner. Qualquer prefixo único serve nos comandos |
| `IMAGE` | Imagem usada para criar o contêiner |
| `COMMAND` | Comando em execução (`ENTRYPOINT` + `CMD`) |
| `CREATED` | Quando o contêiner foi criado |
| `STATUS` | `Up 5 minutes`, `Up … (healthy)`, `Up … (Paused)`, `Exited (0) 3 seconds ago`, `Created`, `Restarting` |
| `PORTS` | Portas publicadas (`0.0.0.0:8080->80/tcp`) |
| `NAMES` | Nome dado com `--name` ou gerado automaticamente |

- `docker container ls` mostra só os contêineres **em execução**. Com **`-a`**, mostra também os parados e os criados e nunca iniciados. `-q` imprime só os IDs (útil em scripts, como `docker rm $(docker ps -aq --filter status=exited)`), e `--format` escolhe as colunas.
- Nos comandos, o contêiner pode ser indicado pelo **nome** ou pelo **ID** (ou por um prefixo único do ID). O nome é mais legível e estável.

#### Modo interativo e modo em segundo plano

| Flag | Efeito |
|---|---|
| `-i` / `--interactive` | Mantém o **STDIN aberto**, mesmo sem terminal anexado |
| `-t` / `--tty` | Aloca um **pseudoterminal** (TTY): prompt, cores, edição de linha |
| `-d` / `--detach` | Executa em **segundo plano** e devolve o terminal, imprimindo o ID do contêiner |

- **Interativo (`-it`)**: para explorar uma imagem, depurar ou executar ferramentas de linha de comando: `docker run -it ubuntu:24.04 bash`. O prompt muda para `root@<id>:/#` porque você está **dentro** do contêiner (`cat /etc/os-release` confirma a distribuição).
- **Segundo plano (`-d`)**: para serviços que você só vai consumir (um servidor web, um banco): `docker run -d -p 8080:80 nginx`. A aplicação já está configurada na imagem; ninguém precisa entrar no contêiner.
- **Sair sem parar**: em uma sessão `-it`, o shell é o **PID 1**. Digitar `exit` encerra o shell e, portanto, **para o contêiner**. Para se desanexar e deixá-lo rodando, use **Ctrl+P seguido de Ctrl+Q** (a sequência pode ser trocada com `--detach-keys`).
- **Voltar ao terminal**: `docker container attach <contêiner>` reconecta ao STDIN/STDOUT do **PID 1**. Cuidado: Ctrl+C ou `exit` ali afetam o processo principal. Para abrir um **shell adicional** sem esse risco, prefira `docker exec -it <contêiner> bash` (ou `sh`); ao sair dele, o contêiner continua rodando.

#### Criar, iniciar, parar, pausar e remover

```bash
docker container create -it --name meu-ubuntu ubuntu:24.04   # só cria (status Created)
docker container ls -a                                       # aparece só com -a
docker container start -ai meu-ubuntu                        # inicia e anexa (-a) com STDIN (-i)

docker container stop meu-ubuntu      # SIGTERM, espera 10 s, depois SIGKILL
docker container start meu-ubuntu     # inicia de novo o mesmo contêiner
docker container restart meu-ubuntu   # stop + start
docker container pause meu-ubuntu     # congela os processos: STATUS "Up … (Paused)"
docker container unpause meu-ubuntu

docker container rm meu-ubuntu        # falha se estiver rodando
docker container rm -f meu-ubuntu     # força: mata (SIGKILL) e remove
```

- **`create` + `start`** é útil para preparar um contêiner (por exemplo, copiar arquivos com `docker cp`) antes de iniciá-lo.
- **`docker container rm` de um contêiner em execução** retorna erro (`cannot remove container … : container is running: stop the container before removing or force remove`). Pare antes ou use `-f`, sabendo que `-f` **não** faz parada graciosa.
- **Remover o contêiner não remove a imagem**: ela continua no host para novos contêineres. Para apagá-la, use `docker image rm`.
- `docker rm -v` remove também os **volumes anônimos** do contêiner.

### Executar contêineres

#### `docker run` em detalhe
`docker run` = `docker create` (cria o contêiner a partir da imagem) + `docker start` (inicia o processo). Se a imagem não existir localmente, é baixada antes.

```bash
docker run -d --name api \
  -p 8080:3000 \
  -e NODE_ENV=production \
  -v dados-api:/app/data \
  --network backend \
  --restart unless-stopped \
  --memory 512m --cpus 1 \
  minha-org/api:1.4.2
```

| Flag | Efeito |
|---|---|
| `-d` / `--detach` | Roda em segundo plano e imprime o ID |
| `-it` | `-i` mantém o STDIN aberto, `-t` aloca um terminal. Juntas, para sessões interativas (`docker run -it ubuntu bash`) |
| `--rm` | Remove o contêiner (e seus volumes anônimos) quando ele sair |
| `--name` | Nome fixo; sem ele, o Docker gera um aleatório (`quirky_turing`) |
| `-p host:contêiner` | Publica uma porta (capítulo 6) |
| `-e` / `--env-file` | Variáveis de ambiente |
| `-v` / `--mount` | Volumes, bind mounts e tmpfs (capítulo 7) |
| `--network` | Rede à qual o contêiner se conecta |
| `--restart` | Política de reinício (abaixo) |
| `-w` / `--workdir` | Diretório de trabalho |
| `-u` / `--user` | Usuário e grupo do processo (`-u 1000:1000`) |
| `--entrypoint` | Substitui o `ENTRYPOINT` da imagem |
| `--init` | Usa um init mínimo (`tini`) como PID 1, que repassa sinais e recolhe processos zumbis |
| `--memory`, `--cpus`, `--pids-limit` | Limites de recursos (capítulo 10) |
| `--read-only`, `--cap-drop`, `--security-opt` | Endurecimento (capítulo 9) |
| `--platform` | Força a plataforma da imagem (`linux/amd64`, `linux/arm64`) |
| `--pull always\|missing\|never` | Quando baixar a imagem (padrão `missing`) |

- **Argumentos depois da imagem** substituem o `CMD`: `docker run alpine echo oi`. Para substituir o `ENTRYPOINT`, use `--entrypoint`.
- **`docker run` sempre cria um contêiner novo**. Para voltar a um contêiner parado, use `docker start`.

#### Estados do contêiner

| Estado | Significado | Como chega lá |
|---|---|---|
| `created` | Contêiner criado, processo nunca iniciado | `docker create` |
| `running` | PID 1 em execução | `docker start`, `docker run` |
| `paused` | Processos congelados (cgroup freezer); memória preservada | `docker pause` / `unpause` |
| `restarting` | Saiu e a política de reinício está agindo | Falha com `--restart` |
| `exited` | PID 1 terminou; a camada gravável continua até o `docker rm` | Fim do processo, `docker stop`, `docker kill` |
| `removing` | Sendo removido | `docker rm` |
| `dead` | Remoção falhou parcialmente (em geral, recurso ocupado) | Raro; exige investigação |

- **Contêiner parado não perde dados** da camada gravável; só o `docker rm` os apaga. Mesmo assim, dados importantes devem ficar em volumes.

#### Políticas de reinício

| Política | Reinicia quando | Depois de `docker stop` manual | Depois de reiniciar o daemon |
|---|---|---|---|
| `no` (padrão) | Nunca | — | Não sobe |
| `on-failure[:N]` | O código de saída é diferente de 0 (até N tentativas) | Não reinicia | Sobe se tiver saído com erro |
| `always` | Sempre que sair | Não reinicia na hora, mas **volta a subir quando o daemon reiniciar** | Sobe |
| `unless-stopped` | Sempre que sair | Não reinicia | **Não sobe** se tinha sido parado manualmente |

- A política só passa a valer depois que o contêiner **fica de pé por pelo menos 10 segundos**, para evitar laços de reinício de contêineres que nunca iniciam.
- O intervalo entre tentativas começa em **100 ms** e **dobra** a cada falha (backoff), sendo zerado quando o contêiner fica estável.
- A política de reinício **não** reage a um healthcheck `unhealthy` no Engine puro. Quem troca contêineres doentes é um orquestrador (Swarm, Kubernetes) ou uma ferramenta externa.

### Sinais, PID 1 e parada graciosa

#### Como o Docker para um contêiner
1. `docker stop` envia o **sinal de parada** (padrão `SIGTERM`, ou o definido em `STOPSIGNAL`) ao **PID 1**.
2. Espera o **tempo de tolerância**: **10 segundos** por padrão (`docker stop -t 30`, `--stop-timeout` no `run`, `stop_grace_period` no Compose).
3. Se o processo não sair, envia **`SIGKILL`**, que não pode ser tratado. O contêiner sai com código **137**.

- `docker kill` envia `SIGKILL` direto (ou outro sinal com `-s`, como `docker kill -s HUP` para recarregar configuração).

#### O problema do PID 1
- O kernel trata o PID 1 de um namespace de forma especial: **sinais sem tratador explícito são ignorados**. Uma aplicação que não trata `SIGTERM` como PID 1 não para com `docker stop` e só morre no `SIGKILL`, depois de 10 segundos.
- **Forma shell** no Dockerfile (`CMD node server.js`) roda `/bin/sh -c "node server.js"`: o PID 1 é o **shell**, que **não repassa** o `SIGTERM` ao Node. Use a **forma exec** (`CMD ["node", "server.js"]`), veja o capítulo 4.
- **Scripts de entrada** (`entrypoint.sh`) devem terminar com `exec "$@"`, para que a aplicação substitua o shell e vire o PID 1.
- **Processos zumbis**: o PID 1 também precisa recolher filhos que terminam. Aplicações que criam subprocessos devem rodar com `--init` (ou `init: true` no Compose), que usa o `tini` como PID 1.

#### Códigos de saída

| Código | Significado | Causa típica |
|---|---|---|
| **0** | Sucesso | Processo terminou normalmente (esperado em jobs; em serviços, indica que o processo não ficou em primeiro plano) |
| **1** | Erro genérico da aplicação | Exceção não tratada, configuração inválida |
| **125** | O próprio `docker run` falhou | Flag inválida, conflito de nome, porta já em uso |
| **126** | Comando encontrado mas não executável | Falta permissão de execução no script, arquivo não é binário válido |
| **127** | Comando não encontrado | Erro de digitação, binário ausente na imagem, `PATH` errado, script com final de linha CRLF (`/bin/sh^M`) |
| **137** | Morto por `SIGKILL` (128 + 9) | **OOM kill** (confira `OOMKilled: true` no `inspect`), `docker kill` ou `docker stop` depois do tempo de tolerância |
| **139** | Falha de segmentação (128 + 11) | Bug nativo, biblioteca incompatível (ex.: musl vs. glibc), arquitetura errada |
| **143** | Terminou por `SIGTERM` (128 + 15) | Parada normal com `docker stop` em uma aplicação que não trata o sinal com código 0 |

- Descubra o código e a causa: `docker inspect -f '{{.State.ExitCode}} {{.State.OOMKilled}} {{.State.Error}}' <contêiner>`.

### Inspeção, depuração e limpeza

#### Comandos de observação

| Comando | Para que serve |
|---|---|
| `docker ps` / `docker ps -a` | Contêineres em execução / todos. `--filter status=exited`, `--format` |
| `docker logs -f --tail 100 --since 10m <c>` | STDOUT e STDERR do PID 1. Só funciona com drivers de log que guardam localmente |
| `docker inspect <c>` | JSON completo: estado, IP, montagens, variáveis, política de reinício. Use `-f` com template Go ou `--format json \| jq` |
| `docker exec -it <c> sh` | Abre um processo novo **dentro** de um contêiner em execução |
| `docker top <c>` | Processos do contêiner vistos do host |
| `docker stats` | CPU, memória, rede e disco em tempo real |
| `docker events` | Fluxo de eventos do daemon (create, start, die, oom, health_status) |
| `docker diff <c>` | Arquivos adicionados (A), alterados (C) ou apagados (D) na camada gravável |
| `docker cp <c>:/caminho ./local` | Copia arquivos entre o contêiner e o host (funciona com o contêiner parado) |
| `docker port <c>` | Mapeamentos de porta publicados |
| `docker debug <c>` | Abre um shell com ferramentas de depuração mesmo em imagens mínimas, sem alterar a imagem (recurso do Docker Desktop) |

- **Imagem mínima sem shell** (distroless, `scratch`): `docker exec` não tem o que executar. Alternativas: `docker debug`, ou um contêiner auxiliar que compartilha os namespaces do alvo: `docker run -it --rm --pid container:api --network container:api nicolaka/netshoot`.
- **Contêiner que sai logo ao iniciar**: `docker logs` mostra a última saída; para investigar, sobrescreva o comando: `docker run -it --entrypoint sh <imagem>`.

#### Limpeza

| Comando | Remove |
|---|---|
| `docker container prune` | Contêineres parados |
| `docker image prune` | Imagens **dangling** (sem tag, `<none>:<none>`) |
| `docker image prune -a` | Todas as imagens **não usadas** por nenhum contêiner |
| `docker volume prune` | Volumes **anônimos** não usados (desde o Engine 23). Use `-a` para incluir volumes nomeados |
| `docker network prune` | Redes personalizadas sem contêineres |
| `docker builder prune` | Cache de build |
| `docker system prune` | Contêineres parados, redes não usadas, imagens dangling e cache de build. **Não** remove volumes |
| `docker system prune -a --volumes` | Tudo acima + imagens não usadas + volumes anônimos não usados |
| `docker system df` / `df -v` | Mostra quanto espaço cada tipo de objeto usa e quanto pode ser liberado |

- Todos aceitam `--filter "until=24h"` e `--filter label=...`, úteis em jobs de limpeza de runners de CI.

### Decisão rápida — Ciclo de vida

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Contêiner leva 10 s para parar | Forma exec no `CMD`/`ENTRYPOINT`, `exec "$@"` no script, tratar `SIGTERM` ou `--init` | Aumentar o timeout de parada |
| Contêiner sai com 137 | Verificar `OOMKilled` no `inspect`; ajustar limite de memória ou vazamento | Tratar como erro da aplicação |
| Contêiner sai com 127 | Conferir binário, `PATH` e finais de linha (CRLF) do script | Reinstalar o Docker |
| Contêiner de serviço sai com 0 logo após iniciar | O processo foi para segundo plano (daemonizou); rodar em primeiro plano (`nginx -g 'daemon off;'`) | `tail -f /dev/null` no fim do script |
| Serviço deve voltar após reboot, mas respeitar uma parada manual | `--restart unless-stopped` | `--restart always` |
| Job que deve tentar de novo só se falhar | `--restart on-failure:3` | `always` |
| Investigar imagem distroless | `docker debug` ou contêiner auxiliar com `--pid`/`--network container:` | Trocar a base para ter shell |
| Ver o que o contêiner mudou no disco | `docker diff` | `docker exec` + `find` |
| Liberar espaço no runner de CI | `docker system prune -af --filter until=24h` | `rm -rf /var/lib/docker` com o daemon rodando |
| Sair de uma sessão `-it` sem parar o contêiner | Ctrl+P Ctrl+Q; depois `docker exec -it` para voltar | `exit` (para o PID 1) |
| Rodar comando único e descartar | `docker run --rm` | Acumular contêineres `exited` |

---

## 3. Imagens e Registries

> **Ideia central**: uma imagem é uma **lista ordenada de camadas** somente leitura mais um **arquivo de configuração**, descritos por um **manifest**. Tudo é endereçado por conteúdo (hash **SHA-256**): a **tag** é um rótulo móvel, o **digest** é imutável.

### Anatomia de uma imagem

#### Camadas, manifest e digest

| Peça | O que é |
|---|---|
| **Camada** (layer) | Tarball com as mudanças de sistema de arquivos de uma instrução do build (`RUN`, `COPY`, `ADD`). Camadas iguais são armazenadas e baixadas uma vez só |
| **Config** | JSON com metadados: `Cmd`, `Entrypoint`, `Env`, `User`, `WorkingDir`, `ExposedPorts`, `Labels`, histórico e a lista de `diff_ids` |
| **Manifest** | JSON que lista o config e as camadas (com seus digests e tamanhos) de **uma plataforma** |
| **Index** (manifest list) | JSON que aponta para vários manifests, um por plataforma (`linux/amd64`, `linux/arm64`…). O cliente escolhe o da sua plataforma |
| **Digest** | Hash SHA-256 do manifest (ou do index): `sha256:3f5a…`. Qualquer mudança gera outro digest |

- **Copy-on-write**: quando um contêiner altera um arquivo de uma camada inferior, o arquivo é copiado para a camada gravável do contêiner antes da mudança. Apagar um arquivo em uma camada superior **não reduz** o tamanho da imagem: ele continua na camada onde foi criado (capítulo 4).
- **Metadados sem camada**: `ENV`, `CMD`, `LABEL`, `EXPOSE` e similares só alteram o config; não criam camada de sistema de arquivos.

#### Copy-on-write em detalhe
- **Ideia**: um recurso (bloco de disco, página de memória, arquivo) só é **copiado quando alguém vai modificá-lo**. Até lá, todos compartilham o original. Uma analogia comum: é como fazer anotações em um livro emprestado, em que, no instante em que a caneta toca a página, alguém tira uma cópia daquela página e você escreve na cópia. O livro original continua intacto.
- **No Docker**, um contêiner é uma pilha de **N camadas somente leitura** (as da imagem) com **uma camada de leitura e escrita** por cima (a do contêiner). O union filesystem apresenta tudo como um único diretório.

| Operação no contêiner | O que acontece nas camadas |
|---|---|
| **Ler** um arquivo | A busca começa na camada superior e desce até encontrar o arquivo. Nada é copiado |
| **Criar** um arquivo | É gravado direto na camada gravável |
| **Alterar** um arquivo da imagem | Na primeira escrita, o arquivo **inteiro** é copiado para a camada gravável (**copy-up**) e alterado lá. Com overlayfs, a cópia acontece uma vez só; as escritas seguintes vão direto para a cópia |
| **Apagar** um arquivo da imagem | As camadas inferiores são somente leitura, então é criado um marcador **whiteout** na camada superior, que esconde o arquivo. O espaço **não** é liberado na imagem |

- **Consequências práticas**: alterar pela primeira vez um arquivo grande da imagem (um banco de dados embutido, um log grande) é caro, porque ele é copiado inteiro. Muitas camadas deixam buscas de arquivo um pouco mais lentas. E dados que mudam muito devem ficar em **volumes**, que ficam fora do union filesystem (capítulo 7).
- **Economia**: dez contêineres da mesma imagem ocupam o espaço da imagem **uma vez** mais dez camadas graváveis, geralmente pequenas. Com overlayfs, os contêineres também **compartilham o cache de páginas** dos arquivos comuns, o que economiza memória.
- `docker container ls -s` mostra o tamanho da camada gravável de cada contêiner (`size`) e o tamanho virtual (camada gravável + imagem).
- `docker image history <imagem>` mostra cada camada, a instrução que a criou e o tamanho. `docker image inspect` mostra config e digests.

#### Referências de imagem
Formato completo: `[registry[:porta]/][namespace/]repositório[:tag][@digest]`

| Referência escrita | Referência completa |
|---|---|
| `nginx` | `docker.io/library/nginx:latest` |
| `bitnami/redis:7.4` | `docker.io/bitnami/redis:7.4` |
| `ghcr.io/org/app:1.2.0` | Registry GitHub Container Registry |
| `123456789012.dkr.ecr.sa-east-1.amazonaws.com/app:abc123` | Amazon ECR |
| `localhost:5000/app` | Registry local na porta 5000 |
| `nginx:1.27@sha256:…` | O digest manda; a tag vira só documentação |

- **Sem registry**, assume `docker.io`. **Sem namespace** no Docker Hub, assume `library` (imagens oficiais). **Sem tag**, assume `latest`.
- **`latest` não significa "mais recente"**: é só a tag padrão. Ela aponta para o que foi enviado por último com esse nome, ou para nada.
- **Tags são mutáveis**: `node:22` hoje e daqui a um mês podem ser imagens diferentes. Para builds reproduzíveis, **fixe pelo digest** (`FROM node:22-slim@sha256:…`) e use uma ferramenta (Renovate, Dependabot) para atualizar.

### Registries

#### Docker Hub
- Registry padrão. Tipos de conteúdo confiável: **Docker Official Images** (namespace `library`, mantidas pela Docker com os upstreams), **Verified Publisher** (empresas parceiras) e **Docker-Sponsored Open Source**.
- **Docker Hardened Images (DHI)**: imagens mínimas, sem shell e sem gerenciador de pacotes na variante de runtime, que rodam como usuário não root, com SBOM e provenance assinados. Gratuitas e Apache 2.0 desde dez/2025; o plano Enterprise acrescenta SLA de correção de CVEs críticos, imagens FIPS e STIG.
- **Limites de pull** (janela de 6 horas, conferidos em set/2026):

| Tipo de usuário | Pulls por 6 horas |
|---|---|
| Não autenticado | **100** por endereço IPv4 ou sub-rede IPv6 /64 |
| Personal (conta gratuita autenticada) | **200** |
| Pro, Team e Business | Ilimitado (sujeito a uso justo) |

- Em CI e clusters, **sempre autentique** os pulls, use um **mirror/pull-through cache** (Harbor, ECR pull-through cache, `registry-mirrors`) e evite baixar a mesma imagem em cada job. Um NAT compartilhado faz vários servidores contarem como um único IP.

#### Outros registries

| Registry | Autenticação típica |
|---|---|
| **GitHub Container Registry** (`ghcr.io`) | `GITHUB_TOKEN` no Actions, ou personal access token com `write:packages` |
| **Amazon ECR** | `aws ecr get-login-password \| docker login --username AWS --password-stdin <conta>.dkr.ecr.<região>.amazonaws.com` (token vale 12 h), ou o credential helper `docker-credential-ecr-login` |
| **Azure Container Registry** | `az acr login --name <registry>` |
| **Google Artifact Registry** | `gcloud auth configure-docker <região>-docker.pkg.dev` |
| **GitLab Container Registry** | `CI_REGISTRY_USER` / `CI_REGISTRY_PASSWORD` no pipeline |
| **Harbor** (self-hosted, CNCF) | Usuários, robot accounts, replicação, scan e cache de proxy |
| **Distribution** (imagem oficial `registry`) | Registry mínimo open source do projeto CNCF `distribution/distribution`; versão atual `registry:3` (veja "Registry próprio" abaixo) |

#### Credenciais da CLI
- `docker login <registry>` grava a credencial em `~/.docker/config.json`. Sem **credential helper**, ela fica **codificada em base64, não criptografada**.
- Configure `credsStore` (`osxkeychain`, `wincred`, `secretservice`, `pass`, `desktop`) ou `credHelpers` por registry (ex.: `ecr-login`) para guardar no cofre do sistema.
- Em scripts, use `--password-stdin` para a senha não aparecer no histórico nem na lista de processos.


#### Avaliar uma imagem antes de usar
Imagens prontas economizam muito tempo, mas **não coloque em produção algo que você não sabe o que é**. Antes de adotar uma imagem de terceiros:

- **`docker image inspect <imagem>`** mostra o config completo: `Cmd`, `Entrypoint`, `Env`, `User`, `ExposedPorts`, `Volumes`, `Labels`, arquitetura, SO e digests. Filtre com `-f '{{.Config.User}}'` ou `--format json | jq`.
- **`docker image history <imagem>`** lista as camadas com a instrução que criou cada uma e o tamanho. Instruções só de metadados aparecem com tamanho 0; camadas de imagens baixadas aparecem com `<missing>` na coluna `IMAGE`, porque os IDs intermediários não são distribuídos. `--no-trunc` mostra o comando inteiro.
- **Dockerfile e repositório de origem**: imagens oficiais e boas imagens da comunidade publicam o Dockerfile. Confira o rótulo `org.opencontainers.image.source`.
- **Sem baixar a imagem**: o Docker Hub mostra as camadas de cada tag na página da imagem, e `docker buildx imagetools inspect` mostra plataformas e digests. O antigo site ImageLayers deixou de existir. Para explorar o conteúdo de cada camada, a ferramenta **dive** é bastante usada.
- **Vulnerabilidades e origem**: `docker scout quickview`/`cves`, SBOM e provenance (capítulo 9).

#### Enviar imagens ao Docker Hub
1. Crie a conta em **hub.docker.com** (a criação pela CLI não existe mais). Contas gratuitas têm repositórios públicos ilimitados e um número limitado de repositórios privados; builds automáticos a partir do GitHub/Bitbucket são recurso de planos pagos.
2. Autentique: `docker login` (Docker Hub) ou `docker login registry.exemplo.com` (outro registry). Prefira um **personal access token** no lugar da senha e um credential helper.
3. Nomeie a imagem no formato **`usuário-ou-organização/repositório:tag`** (ex.: `minhaconta/apache:1.0`). Sem o namespace, o push tenta `docker.io/library/…`, que é reservado às imagens oficiais, e falha com `denied`.
4. Envie: `docker push minhaconta/apache:1.0`. Camadas que o registry já tem aparecem como **`Layer already exists`** e não são reenviadas; no fim, o push mostra o **digest** da imagem.

```bash
docker login
docker image tag apache:1.0 minhaconta/apache:1.0
docker push minhaconta/apache:1.0

# Testar o caminho completo: remover a cópia local e baixar de novo
docker image rm minhaconta/apache:1.0
docker pull minhaconta/apache:1.0
docker run -d -p 8080:80 minhaconta/apache:1.0
```

- O repositório é criado **público** por padrão no primeiro push (configurável na conta).
- **`docker search <termo>`** procura repositórios no Docker Hub (colunas `NAME`, `DESCRIPTION`, `STARS`, `OFFICIAL`; a coluna `AUTOMATED` foi removida). Filtros: `--filter is-official=true`, `--filter stars=100`.
- **Remover imagem em uso**: `docker image rm` falha se algum contêiner (mesmo parado) usa a imagem. Com `-f`, a tag é removida (`Untagged: …`), mas as camadas continuam enquanto houver contêineres usando-as. O caminho limpo é remover os contêineres antes.

#### Registry próprio
Para guardar imagens dentro da empresa sem depender de um serviço externo, rode a imagem oficial **`registry`** (projeto **Distribution**, hoje na CNCF, que substituiu o antigo Docker Registry em Python):

```bash
docker run -d -p 5000:5000 --restart=always --name registry   -v registry-dados:/var/lib/registry registry:3

docker image tag minhaconta/apache:1.0 localhost:5000/apache:1.0
docker push localhost:5000/apache:1.0
docker pull localhost:5000/apache:1.0
curl http://localhost:5000/v2/_catalog        # lista os repositórios
```

- O **nome do registry faz parte da referência**: para enviar a outro registry, basta dar à imagem uma tag com o endereço dele (`host:porta/repositório:tag`).
- `localhost` é aceito sem TLS. Para outros hosts, o Docker exige **HTTPS**; sem certificado válido, cada cliente precisa listar o registry em `insecure-registries` no `daemon.json`, o que só é aceitável em laboratório.
- Para uso sério, configure **TLS**, **autenticação** (htpasswd ou token), armazenamento persistente (volume ou S3/Azure/GCS) e **garbage collection** para liberar espaço de camadas sem referência.
- Precisa de interface web, usuários e projetos, replicação, scan de vulnerabilidades e cache de proxy? Use o **Harbor** (CNCF) ou o registry gerenciado da sua nuvem (ECR, Artifact Registry, ACR, GHCR).

#### Certificados de registry: `/etc/docker/certs.d`
Quando o registry usa um certificado de uma **CA interna** (ou exige **certificado de cliente**, autenticação TLS mútua), o daemon precisa confiar nele. A alternativa correta a `insecure-registries` é colocar os arquivos em um diretório com o **nome exato do registry, incluindo a porta**:

```text
/etc/docker/certs.d/
└── registry.exemplo.com:5000/
    ├── ca.crt          # CA que assinou o certificado do registry
    ├── client.cert     # certificado de cliente (TLS mútuo)
    └── client.key      # chave do certificado de cliente
```

- O daemon trata arquivos **`.crt` como CA** e **`.cert` como certificado de cliente**. Trocar a extensão gera o erro `Missing key … for client certificate … CA certificates should use the extension .crt`.
- O nome do diretório precisa bater com a referência usada no `pull`/`push` (`registry.exemplo.com:5000/app:1.0`). Sem porta na referência, o diretório não leva porta.
- A configuração vale **por daemon**: cada nó que baixa do registry (todos os nós de um Swarm, por exemplo) precisa dos arquivos. No Docker Desktop, adicione a CA ao chaveiro do sistema operacional.
- Alternativa para CA interna: instalar a CA no repositório de certificados do sistema (`update-ca-certificates`) e reiniciar o daemon.

#### Apagar imagens de um registry
`docker image rm` apaga só a cópia **local**. No registry, a remoção tem duas etapas: apagar o **manifest** pela API e depois rodar o **garbage collection**, que libera as camadas sem referência.

```bash
# 1. O registry precisa aceitar DELETE (desligado por padrão)
docker run -d -p 5000:5000 --name registry \
  -e REGISTRY_STORAGE_DELETE_ENABLED=true \
  -v registry-dados:/var/lib/registry registry:3

# 2. Descobrir o digest da tag (cabeçalho Docker-Content-Digest)
curl -sI \
  -H "Accept: application/vnd.oci.image.index.v1+json" \
  -H "Accept: application/vnd.oci.image.manifest.v1+json" \
  -H "Accept: application/vnd.docker.distribution.manifest.v2+json" \
  http://localhost:5000/v2/apache/manifests/1.0 | grep -i docker-content-digest

# 3. Apagar o manifest pelo digest (não pela tag)
curl -X DELETE http://localhost:5000/v2/apache/manifests/sha256:…

# 4. Liberar as camadas, com o registry parado ou em modo somente leitura
docker exec registry registry garbage-collect --dry-run /etc/distribution/config.yml
docker exec registry registry garbage-collect --delete-untagged /etc/distribution/config.yml
```

- O `DELETE` é feito **pelo digest**. Apagar o manifest remove todas as tags que apontam para ele.
- O garbage collection é do tipo **stop-the-world**: um push durante a coleta pode perder camadas e corromper a imagem. Rode com o registry parado ou com `storage.maintenance.readonly` ligado.
- No `registry:3`, a configuração fica em `/etc/distribution/config.yml`; no `registry:2`, ficava em `/etc/docker/registry/config.yml`.
- Registries corporativos (Harbor, MSR, ECR, Artifact Registry) fazem o mesmo pela interface, com **políticas de retenção** (apagar tags antigas automaticamente) e garbage collection agendado.

### Gerenciar imagens

#### Comandos essenciais

| Comando | O que faz |
|---|---|
| `docker pull <ref>` | Baixa a imagem (a variante da plataforma local, se houver index) |
| `docker push <ref>` | Envia a imagem; camadas que o registry já tem não são reenviadas |
| `docker tag origem destino` | Cria outro nome para a mesma imagem (não copia dados) |
| `docker image ls` / `ls --digests` | Lista imagens locais |
| `docker image rm` / `rmi` | Remove tags; os dados só saem quando nenhuma tag ou contêiner os usa |
| `docker save -o app.tar app:1.0` / `docker load -i app.tar` | Exporta e importa **imagens completas** (camadas, tags e metadados). Serve para ambientes sem acesso a registry |
| `docker export <c> > fs.tar` / `docker import fs.tar` | Exporta o **sistema de arquivos achatado de um contêiner**; o import gera uma imagem de uma camada, **sem histórico, CMD ou ENV** |
| `docker commit <c> img:tag` | Cria uma imagem a partir do estado de um contêiner. Útil para investigação; **não** para produção (não é reproduzível) |
| `docker buildx imagetools inspect <ref>` | Mostra o index e as plataformas de uma imagem **no registry**, sem baixá-la |
| `docker manifest inspect <ref>` | Alternativa mais antiga ao `imagetools inspect` |

- **Imagem dangling**: aparece como `<none>:<none>` quando uma tag é movida para um build novo e a imagem antiga fica sem nome. É removida por `docker image prune`.

#### Filtros e formatação: `--filter` e `--format`
Os comandos de listagem aceitam **filtros** (`--filter chave=valor`, repetível) e **formatação** com templates Go (`--format`). É assim que se responde a perguntas como "quais imagens foram criadas depois de X" ou "qual é o usuário padrão desta imagem".

| Filtro de `docker image ls` | Seleciona |
|---|---|
| `dangling=true` | Imagens sem tag (`<none>:<none>`) |
| `reference='nginx:1.*'` | Imagens cujo nome e tag casam com o padrão |
| `before=app:1.4` / `since=app:1.4` | Criadas antes / depois de outra imagem |
| `label=org.opencontainers.image.vendor=Acme` | Com o rótulo (e o valor) indicado |

| Filtro de `docker ps` | Seleciona |
|---|---|
| `status=exited` (ou `running`, `paused`, `created`) | Contêineres no estado indicado |
| `ancestor=nginx` | Criados a partir da imagem (ou de descendentes dela) |
| `label=env=prod`, `name=api`, `network=app`, `volume=dados` | Por rótulo, nome, rede ou volume |
| `health=unhealthy`, `exited=137` | Por estado do healthcheck ou código de saída |

```bash
# Tabela personalizada (\t separa as colunas)
docker image ls --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}'
docker ps -a --filter status=exited --format '{{.Names}} {{.Status}}'

# Um objeto inteiro em JSON (bom para jq)
docker image ls --format json

# Campos de inspect
docker image inspect -f '{{.Os}}/{{.Architecture}}' nginx:1.29
docker image inspect -f '{{.Config.User}} {{json .Config.ExposedPorts}}' nginx:1.29
docker image inspect -f '{{json .RootFS.Layers}}' nginx:1.29     # digests das camadas
docker inspect -f '{{.State.Status}} {{.State.ExitCode}}' api
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}' api

# Remoção combinada com filtro
docker image prune -a --filter "until=168h"          # sem uso e com mais de 7 dias
docker rmi $(docker image ls -q --filter dangling=true)
```

- `-q` devolve só os IDs, para usar em outros comandos. `--no-trunc` mostra IDs e comandos completos.
- **Funções úteis nos templates**: `json` (serializa um campo), `range` (percorre listas e mapas), `index` (acessa uma chave com caracteres especiais: `{{index .Config.Labels "org.opencontainers.image.source"}}`), `upper`, `lower`, `join`.
- `docker inspect` devolve uma **lista JSON**; o `-f` é aplicado a cada objeto. Ele funciona em contêineres, imagens, redes, volumes, nós, serviços, tarefas, secrets e configs; use `--type` quando um nome existe em mais de um tipo de objeto.

#### Imagem com uma só camada
Às vezes se pede uma imagem com **uma única camada** (distribuição simples, sem histórico). As formas e o que cada uma perde:

| Técnica | Como | O que acontece |
|---|---|---|
| `export` + `import` | `docker export c1 \| docker import - app:flat` | Achata o sistema de arquivos de um **contêiner**. Perde histórico, `CMD`, `ENTRYPOINT`, `ENV`, `EXPOSE` (recoloque com `--change 'CMD ["app"]'`) |
| Multi-stage com `FROM scratch` | Último estágio: `FROM scratch` + `COPY --from=build / /` | Uma camada com o conteúdo do estágio anterior; os metadados são definidos no próprio Dockerfile |
| `docker build --squash` | Flag experimental do **builder clássico** | Não existe no BuildKit, o builder padrão. Aparece em materiais antigos |

- **Aplicar um arquivo para criar uma imagem**: `docker build -f caminho/Dockerfile.prod .` usa um Dockerfile com outro nome ou em outro lugar; `docker build - < Dockerfile` lê o Dockerfile do STDIN, sem contexto.
- **Ver as camadas**: `docker image history` (instrução e tamanho de cada camada) e `docker image inspect -f '{{json .RootFS.Layers}}'` (digests).

#### Criar uma imagem com `docker commit` (e por que evitar)
Há duas formas de criar uma imagem: **declarativa**, com um Dockerfile (capítulo 4), e **imperativa**, alterando um contêiner à mão e salvando o resultado.

```bash
docker run -it --name base debian:13 bash
# dentro do contêiner:
apt-get update && apt-get install -y apache2 && apt-get clean
# Ctrl+P Ctrl+Q para sair sem parar

docker container commit -m "Debian com Apache" \
  --change 'CMD ["apachectl", "-D", "FOREGROUND"]' base    # imagem <none>:<none>
docker image tag <IMAGE ID> minha-org/apache:1.0            # dá nome e tag
# ou, direto: docker container commit base minha-org/apache:1.0
```

- `-m` registra uma mensagem, `-a` o autor e `--change` aplica instruções de Dockerfile (`CMD`, `ENV`, `EXPOSE`, `WORKDIR`…) à nova imagem. Sem `--change`, a imagem herda o `CMD` do contêiner (no exemplo, `bash`), e o serviço precisaria ser iniciado à mão.
- **Por que evitar em produção**: ninguém sabe exatamente o que foi feito (não há receita), a imagem carrega sujeira da sessão (históricos, caches, arquivos temporários), não há cache de build nem revisão de código, e refazer a imagem com uma base atualizada exige repetir tudo à mão. Use `commit` para **investigação** (congelar um contêiner com problema) ou para descobrir os passos que depois vão para o Dockerfile.
- **Imagens prontas de terceiros** agilizam muito provas de conceito (POC): em minutos é possível testar várias ferramentas. Para uso contínuo, prefira imagens oficiais ou a sua própria imagem construída a partir de um Dockerfile.

#### Estratégia de tags
- **Tag imutável por build**: SHA do commit (`app:3f9c2ab`) ou versão semântica (`app:1.4.2`). É o que o deploy deve referenciar.
- **Tags móveis de conveniência**: `app:1.4`, `app:1`, `app:latest`, apontando para a última versão compatível.
- **Não reutilize** uma tag de versão para outro conteúdo; alguns registries (ECR, Harbor, GHCR com regras) permitem **tornar tags imutáveis**.
- **Promoção entre ambientes**: a mesma imagem (mesmo digest) passa por dev, homologação e produção; muda só a configuração. Rebuildar para cada ambiente quebra a garantia de que o que foi testado é o que vai para produção.

#### Números de imagens e registries

| Item | Valor |
|---|---|
| Registry padrão | `docker.io` (Docker Hub) |
| Namespace das imagens oficiais | `library` |
| Tag padrão | `latest` |
| Algoritmo do digest | SHA-256 |
| Janela dos limites de pull do Docker Hub | 6 horas |
| Pulls não autenticados no Docker Hub | 100 por IPv4 ou /64 IPv6 |
| Pulls autenticados (Personal) | 200 |
| Validade do token do `aws ecr get-login-password` | 12 horas |
| Porta convencional de um registry local | 5000 |

### Decisão rápida — Imagens e registries

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Garantir que o deploy use exatamente a imagem testada | Referenciar pelo digest ou por tag imutável por commit | Usar `latest` |
| Build reproduzível da imagem base | `FROM imagem:tag@sha256:…` + atualização automática | Tag flutuante sem digest |
| Levar imagens para um ambiente sem internet | `docker save` / `docker load` (ou registry interno) | `docker export` / `import` (perde metadados) |
| CI estourando o limite de pulls do Docker Hub | Autenticar, usar mirror/pull-through cache | Repetir o job até passar |
| Descobrir se uma imagem tem variante `arm64` sem baixá-la | `docker buildx imagetools inspect` | `docker pull` em cada máquina |
| Imagem ocupando espaço sem nome | `docker image prune` (dangling) | Apagar diretórios em `/var/lib/docker` |
| Guardar credenciais de registry com segurança | Credential helper (`credsStore`) e `--password-stdin` | Deixar o `config.json` com base64 |
| Escolher uma base mínima e mantida | Docker Official Image `-slim`, distroless ou Docker Hardened Image | Imagem aleatória do Docker Hub sem mantenedor |
| Criar uma imagem a partir de alterações feitas à mão em um contêiner | Levar as alterações para o Dockerfile | `docker commit` em produção |

---

## 4. Dockerfile

> **Ideia central**: o Dockerfile é a **receita reproduzível** da imagem. Cada instrução que altera arquivos gera uma camada, e o cache é reaproveitado **em ordem, de cima para baixo, até a primeira instrução que mudar**. Ordenar do que muda menos para o que muda mais é a otimização mais barata que existe.

### Primeiro Dockerfile e primeiro build

#### Do Dockerfile à imagem
- O **Dockerfile** é um arquivo de texto com a receita da imagem: a base, os pacotes a instalar, os arquivos a copiar, as variáveis, o usuário, a porta e o comando de início. Funciona como um **Makefile** para imagens, e a vantagem é a automação: a mesma receita gera a mesma imagem em qualquer máquina ou pipeline.

```dockerfile
# primeiro/Dockerfile
FROM debian:13
RUN echo "HELLO DOCKER"
```

```bash
cd primeiro
docker build -t primeiro:1.0 .
docker image ls primeiro
```

- O **último argumento** do `docker build` é o **contexto de build**, um **diretório** (ou URL de repositório Git), e não o arquivo. O `.` significa "o diretório atual". Por padrão, o builder procura um arquivo `Dockerfile` na raiz do contexto. Para usar outro nome ou lugar: `docker build -f docker/api.Dockerfile -t api:1.0 .`.
- **Sem `-t`**, a imagem é criada **sem nome**: aparece como `<none>:<none>` em `docker image ls` e só pode ser referenciada pelo ID. Dê o nome no build (`-t repositório:tag`, podendo repetir `-t`) ou depois, com `docker image tag`.
- A saída atual é a do **BuildKit** (`[+] Building`, passos numerados como `[2/2] RUN …`, `CACHED` quando reaproveita o cache). Materiais antigos mostram a saída do builder legado (`Sending build context to Docker daemon`, `Step 1/2`, `Removing intermediate container`), que só aparece hoje com `DOCKER_BUILDKIT=0` em imagens Windows. Use `--progress=plain` para ver a saída completa de cada `RUN` (por exemplo, o `HELLO DOCKER` do exemplo).

#### Processo em primeiro plano
Um erro comum ao começar: construir uma imagem com o serviço instalado, entrar no contêiner com `-it` e iniciar o serviço à mão (`/etc/init.d/apache2 start`). O serviço até responde, mas **ninguém deveria precisar entrar no contêiner** para isso, e o PID 1 continua sendo o `bash`.

- O contêiner deve iniciar a aplicação **sozinho**, com o processo em **primeiro plano** como PID 1. Serviços que se "daemonizam" (vão para segundo plano) fazem o contêiner terminar logo depois de iniciar.

```dockerfile
# syntax=docker/dockerfile:1
FROM debian:13
RUN apt-get update \
 && apt-get install -y --no-install-recommends apache2 \
 && rm -rf /var/lib/apt/lists/*
ENV APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_RUN_DIR=/var/run/apache2 \
    APACHE_PID_FILE=/var/run/apache2/apache2.pid \
    APACHE_LOCK_DIR=/var/lock/apache2 \
    APACHE_LOG_DIR=/var/log/apache2
LABEL org.opencontainers.image.description="Servidor web Apache"
EXPOSE 80
ENTRYPOINT ["apachectl"]
CMD ["-D", "FOREGROUND"]
```

- `ENTRYPOINT ["apachectl"]` + `CMD ["-D", "FOREGROUND"]` resulta em `apachectl -D FOREGROUND`: o `ENTRYPOINT` é o executável e o `CMD` são os **argumentos padrão**, que podem ser trocados no `docker run`.
- Equivalentes em outros servidores: `nginx -g 'daemon off;'`, `httpd -DFOREGROUND` (a imagem oficial `httpd` já faz isso), `php-fpm -F`.
- Várias instruções `ENV` podem ser agrupadas em uma só (`ENV A=1 B=2`), o que deixa o Dockerfile mais legível. Como `ENV` não cria camada de sistema de arquivos, o ganho é de organização, não de tamanho.
- Na prática, prefira a **imagem oficial** do serviço (`httpd`, `nginx`) a instalar o servidor sobre uma distribuição: ela já vem configurada para rodar em primeiro plano e é mantida pelos upstreams.

### Instruções

#### Referência das instruções

| Instrução | O que faz | Observação |
|---|---|---|
| `# syntax=docker/dockerfile:1` | Diretiva de parser: usa a versão mais recente estável do frontend do Dockerfile | Deve ser a primeira linha. Habilita recursos novos sem atualizar o Engine |
| `FROM imagem [AS nome]` | Define a imagem base (ou `scratch`, vazia) e inicia um estágio | Pode haver vários `FROM` (multi-stage). Antes do primeiro `FROM` só podem vir diretivas de parser, comentários e `ARG` |
| `ARG nome[=padrão]` | Variável **só de build** (`--build-arg`) | Antes do primeiro `FROM`, só vale para os `FROM`. Aparece no histórico: **não use para segredos** |
| `ENV nome=valor` | Variável de ambiente no build **e na execução** | Persiste na imagem e em todos os estágios filhos |
| `WORKDIR /app` | Diretório de trabalho (criado se não existir) | Prefira a `RUN cd …` |
| `COPY [--chown] [--chmod] [--link] [--from] origem destino` | Copia do contexto de build ou de outro estágio/imagem | Preferido para arquivos locais |
| `ADD origem destino` | Como `COPY`, mas também baixa URLs, clona repositórios Git e **extrai tarballs locais** | Use só quando precisar desses extras |
| `RUN comando` | Executa um comando no build e grava o resultado em uma camada | Suporta `--mount` (cache, secret, ssh, bind) e heredocs |
| `USER nome\|uid[:gid]` | Usuário das instruções seguintes e do processo em execução | O padrão é **root**, a menos que a base defina outro. Rode a aplicação como não root |
| `EXPOSE 8080[/tcp]` | **Documenta** a porta que a aplicação escuta | **Não publica** a porta; `-P` usa essa lista |
| `VOLUME /dados` | Declara um ponto de montagem; cria **volume anônimo** se nada for montado | Mudanças no diretório depois do `VOLUME` são descartadas no build |
| `CMD` | Comando (ou argumentos) padrão, executado **quando o contêiner inicia** (o `RUN` executa **no build**) | Substituído por argumentos no `docker run`. Só o último `CMD` vale |
| `ENTRYPOINT` | Executável fixo do contêiner; quando ele termina, o contêiner termina | Substituído só com `--entrypoint` |
| `HEALTHCHECK` | Comando que o Docker executa para saber se o contêiner está saudável | `HEALTHCHECK NONE` desliga o herdado |
| `STOPSIGNAL SIGQUIT` | Sinal enviado pelo `docker stop` | Padrão `SIGTERM` |
| `SHELL ["pwsh", "-c"]` | Troca o shell da forma shell | Útil em imagens Windows |
| `LABEL chave=valor` | Metadados (versão, fonte, licença) | Padrão `org.opencontainers.image.*` |
| `ONBUILD instrução` | Instrução executada quando **outra** imagem usar esta como base | Pouco usado; esconde comportamento |
| `MAINTAINER` | Obsoleto | Use `LABEL org.opencontainers.image.authors` |

#### Forma shell vs. forma exec

| Forma | Exemplo | Executa | Consequência |
|---|---|---|---|
| **Exec** (array JSON) | `CMD ["node", "server.js"]` | O binário diretamente, como PID 1 | Recebe os sinais; **sem** expansão de variáveis de shell |
| **Shell** | `CMD node server.js` | `/bin/sh -c "node server.js"` | Expansão de variáveis funciona, mas o PID 1 é o shell e os sinais não chegam à aplicação |

- O array JSON exige **aspas duplas**: `CMD ['node','server.js']` (aspas simples) é tratado como forma shell e falha.
- Precisa de variáveis e sinais corretos ao mesmo tempo? Use um script com `exec` no final, ou `CMD ["sh", "-c", "exec node server.js --port $PORT"]`.

#### CMD e ENTRYPOINT juntos

| | Sem `ENTRYPOINT` | `ENTRYPOINT ["app"]` (exec) | `ENTRYPOINT app` (shell) |
|---|---|---|---|
| **Sem `CMD`** | Erro: nada a executar (a menos que a base defina) | `app` | `/bin/sh -c app` |
| **`CMD ["--port", "80"]`** | `--port 80` (inválido) | `app --port 80` | `/bin/sh -c app` (**CMD ignorado**) |
| **`CMD ["sh", "-c", "x"]`** | `sh -c x` | `app sh -c x` | `/bin/sh -c app` (**CMD ignorado**) |

- **Padrão recomendado**: `ENTRYPOINT` em forma exec com o executável e `CMD` com os argumentos padrão, que o usuário troca no `docker run imagem --outro-arg`.
- `ENTRYPOINT` em forma shell **ignora o `CMD` e os argumentos do `docker run`**.
- Definir `ENTRYPOINT` em um estágio **zera** o `CMD` herdado da imagem base.

#### COPY vs. ADD e o `.dockerignore`
- **`COPY`** é o padrão. **`ADD`** só para: baixar um arquivo com verificação de checksum (`ADD --checksum=sha256:… https://…`), clonar um repositório Git (`ADD git@github.com:org/repo.git /src`) ou extrair um tarball local automaticamente.
- **`COPY --link`** cria a camada de forma independente das anteriores, permitindo reaproveitá-la mesmo quando a base muda (útil com `--from` em multi-stage).
- **`COPY --chown=app:app`** evita um `RUN chown -R` posterior, que duplicaria os arquivos em uma nova camada.
- **Contexto de build**: o diretório (ou URL) enviado ao builder. Tudo o que não está nele não pode ser copiado; tudo o que está nele é enviado, a menos que o `.dockerignore` exclua.
- **`.dockerignore`** deve excluir `.git`, `node_modules`, artefatos de build, arquivos `.env` e chaves. Sem ele, o build fica lento, o cache é invalidado à toa e segredos podem acabar na imagem com um `COPY . .`.

```text
# .dockerignore
.git
node_modules
dist
*.log
.env*
**/*.pem
Dockerfile*
compose*.yaml
```

#### HEALTHCHECK

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=20s --start-interval=2s --retries=3 \
  CMD ["wget", "-qO-", "http://localhost:8080/health"]
```

| Opção | Padrão | Significado |
|---|---|---|
| `--interval` | 30 s | Intervalo entre verificações |
| `--timeout` | 30 s | Tempo máximo de uma verificação |
| `--start-period` | 0 s | Período inicial em que falhas não contam para `unhealthy` |
| `--start-interval` | 5 s | Intervalo entre verificações durante o `start-period` (Engine 25+) |
| `--retries` | 3 | Falhas seguidas até marcar `unhealthy` |

- Estados: `starting` → `healthy` ou `unhealthy`. Código 0 = saudável, 1 = doente.
- O comando roda **dentro do contêiner**: a ferramenta (`curl`, `wget`) precisa existir na imagem. Em imagens mínimas, use um binário próprio (`/app/healthcheck`) ou a própria aplicação com uma flag.
- Quem usa o estado: `docker ps`, `depends_on: condition: service_healthy` no Compose, Swarm (substitui tarefas doentes) e ferramentas de deploy. Kubernetes **ignora** o `HEALTHCHECK` e usa probes próprias.

### Cache de build

#### Como o cache funciona
- Para cada instrução, o builder verifica se já existe uma camada gerada **a partir da mesma camada pai com a mesma instrução**.
- Para `COPY` e `ADD`, o que conta é o **conteúdo** (checksum) dos arquivos copiados, não a data.
- Para `RUN`, conta só o **texto do comando**: `RUN apt-get update` fica em cache para sempre, mesmo que os repositórios mudem. Por isso, **junte** `apt-get update` e `apt-get install` no mesmo `RUN`.
- **Quando uma instrução invalida o cache, todas as seguintes são refeitas.**

#### Ordem que aproveita o cache

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-slim
WORKDIR /app

# 1. Manifestos de dependências mudam pouco: copiados primeiro
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev

# 2. Código-fonte muda a cada commit: copiado depois
COPY . .

USER node
CMD ["node", "server.js"]
```

- Com essa ordem, mudar só o código-fonte **não** reinstala as dependências.
- **Cache mount** (`--mount=type=cache`) guarda o cache do gerenciador de pacotes (npm, pip, Maven, Go, apt) entre builds, **sem colocá-lo na imagem**.
- **Forçar um build limpo**: `docker build --no-cache`, ou `--no-cache-filter <estágio>` para um estágio específico. `--pull` força baixar a versão mais nova da imagem base.

### Multi-stage builds

#### Por que e como
Vários `FROM` no mesmo Dockerfile. Os estágios iniciais têm compiladores e ferramentas; o estágio final copia **só o artefato**. A imagem final não carrega o SDK, o código-fonte nem o cache.

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.25 AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod go mod download
COPY . .
RUN --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 go build -o /out/app ./cmd/app

FROM gcr.io/distroless/static-debian12:nonroot AS runtime
COPY --from=build /out/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

- **`--target <estágio>`** faz o build parar em um estágio: útil para ter um estágio `dev` (com ferramentas) e um `test` no mesmo arquivo.
- O BuildKit **só executa os estágios necessários** para o alvo e roda estágios independentes **em paralelo**.
- **`COPY --from=<imagem>`** também copia de uma imagem externa: `COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/`.
- Uma imagem Go estática pode partir de `scratch` (nada além do binário). Nesse caso, lembre de copiar certificados CA e dados de fuso horário se a aplicação precisar.
- **Ordem de grandeza**: uma imagem de estágio único baseada em `golang` passa de 800 MB, porque carrega o compilador e o SDK inteiros; o mesmo binário em um estágio final `alpine`, distroless ou `scratch` fica com poucos MB. Com o multi-stage, o estágio de build é descartado e só o binário vai para a imagem final.
- Se o estágio final for **Alpine** (musl libc), compile com `CGO_ENABLED=0` para gerar um binário estático, e use uma versão **mantida** do Alpine. Exemplos antigos com `alpine:3.1` ou `golang` sem tag usam versões fora de suporte.
- Prefira `COPY` a `ADD` para o código-fonte e a forma exec em `ENTRYPOINT ["./app"]`. A forma shell (`ENTRYPOINT ./app`) exige um shell na imagem final e deixa o `sh` como PID 1.

### Boas práticas

#### Escolha da imagem base

| Base | Tamanho típico | Tem shell e gerenciador de pacotes? | Quando usar |
|---|---|---|---|
| `debian`/`ubuntu` completa | 75–120 MB | Sim | Desenvolvimento, quando precisa de muitas ferramentas |
| `-slim` (Debian) | 25–80 MB | Sim (apt) | Bom equilíbrio para a maioria das linguagens interpretadas |
| `alpine` | 5–8 MB | Sim (apk) | Imagens pequenas. **Usa musl libc**: binários nativos compilados para glibc podem falhar ou ficar mais lentos |
| Distroless | 2–25 MB | **Não** | Produção; só a runtime da linguagem e suas bibliotecas |
| Docker Hardened Images | Varia | Não na variante de runtime; sim na variante `-dev` | Produção com SBOM, provenance e correção contínua de CVEs |
| `scratch` | 0 | Não | Binários estáticos (Go, Rust) |

#### Checklist de um bom Dockerfile
- Primeira linha `# syntax=docker/dockerfile:1`.
- Base oficial ou endurecida, com **tag específica e digest**.
- **Multi-stage**: build separado do runtime.
- Dependências antes do código, com **cache mounts**.
- `.dockerignore` completo.
- `RUN apt-get update && apt-get install -y --no-install-recommends … && rm -rf /var/lib/apt/lists/*` no mesmo `RUN`.
- **Usuário não root** (`USER 10001` ou o usuário da base, como `node` ou `nonroot`).
- `CMD`/`ENTRYPOINT` em **forma exec**; scripts de entrada com `exec "$@"`.
- **Um processo principal por contêiner**; processos auxiliares em outros contêineres.
- **Nenhum segredo** em `ARG`, `ENV` ou arquivos copiados: use build secrets (capítulo 5).
- Configuração por **variáveis de ambiente**, não embutida por ambiente.
- `HEALTHCHECK` quando quem executa usa o estado (Compose, Swarm).
- `LABEL org.opencontainers.image.source`, `.version`, `.revision`.
- Validar com `docker build --check` (build checks do BuildKit) e um linter como o **Hadolint**.

#### Por que apagar arquivos em outro `RUN` não reduz a imagem

```dockerfile
# Ruim: o arquivo de 500 MB continua na camada do primeiro RUN
RUN curl -o /tmp/pacote.tgz https://exemplo.com/pacote.tgz
RUN tar xzf /tmp/pacote.tgz -C /opt && rm /tmp/pacote.tgz

# Bom: baixa, extrai e apaga na mesma camada
RUN curl -fsSL https://exemplo.com/pacote.tgz | tar xz -C /opt
```

- Alternativas: fazer o download em um estágio de build e copiar só o resultado, ou usar `RUN --mount=type=bind`/`type=cache` para arquivos que não devem entrar na imagem.

### Decisão rápida — Dockerfile

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Qualquer mudança no código reinstala todas as dependências | Copiar manifestos de dependências antes do código | `COPY . .` no início |
| Imagem de produção com compilador e código-fonte | Multi-stage com estágio final mínimo | Apagar ferramentas com `RUN rm` |
| Aplicação não recebe `SIGTERM` | `CMD`/`ENTRYPOINT` em forma exec | Forma shell com timeout maior |
| Imagem aceitar argumentos extras no `docker run` | `ENTRYPOINT ["app"]` + `CMD ["--padrao"]` | `ENTRYPOINT` em forma shell |
| Copiar arquivos locais | `COPY` | `ADD` sem precisar de URL, Git ou extração |
| Baixar arquivo remoto com integridade | `ADD --checksum=sha256:…` ou `curl` + verificação | `ADD` sem checksum |
| `apt-get install` instala versões antigas | `update` e `install` no mesmo `RUN` | `RUN apt-get update` isolado (fica em cache) |
| Build lento por enviar gigabytes de contexto | `.dockerignore` | Mover o Dockerfile para outro lugar |
| Estágios de dev e produção no mesmo arquivo | Multi-stage com `--target` | Dois Dockerfiles quase iguais |
| Porta aparecer em `docker ps` sem `-p` | Não existe: `EXPOSE` só documenta | Esperar que `EXPOSE` publique |
| Binário nativo falha no Alpine | Base `-slim` (glibc) ou compilar para musl | Adicionar pacotes de compatibilidade até funcionar |
| Tamanho mínimo para Go/Rust estático | `scratch` ou distroless `static` | Base Debian completa |
| Serviço iniciado à mão dentro do contêiner | `ENTRYPOINT`/`CMD` com o processo em primeiro plano | `docker exec` + `/etc/init.d/<serviço> start` |
| Imagem sem nome (`<none>`) depois do build | `docker build -t nome:tag` ou `docker image tag` | Referenciar pelo ID em scripts |

---

## 5. BuildKit, Buildx e Builds Avançados

> **Ideia central**: o **BuildKit** é o motor que executa o build (padrão desde o Engine 23), o **Buildx** é a CLI que conversa com ele (`docker build` já é um alias de `docker buildx build`) e o **Bake** descreve vários builds em um arquivo. Juntos, entregam paralelismo, cache exportável, segredos que não vazam, imagens multiplataforma e atestados de cadeia de suprimentos.

### Recursos do BuildKit no Dockerfile

#### Montagens em `RUN --mount`

| Tipo | Para que serve | Exemplo |
|---|---|---|
| `cache` | Cache persistente entre builds que **não entra na imagem** | `RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt` |
| `secret` | Disponibiliza um segredo **só durante aquele `RUN`**, sem gravá-lo em camada nem no histórico | `RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci` |
| `ssh` | Encaminha o agente SSH do host para clonar repositórios privados | `RUN --mount=type=ssh git clone git@github.com:org/privado.git` |
| `bind` | Monta arquivos do contexto ou de outro estágio sem copiá-los para a imagem | `RUN --mount=type=bind,source=go.sum,target=go.sum go mod download` |
| `tmpfs` | Diretório temporário em memória durante o `RUN` | `RUN --mount=type=tmpfs,target=/tmp …` |

- **Passar os segredos no build**: `docker build --secret id=npmrc,src=$HOME/.npmrc .` e `docker build --ssh default .`. Por padrão, o segredo aparece em `/run/secrets/<id>`; com `env=NOME` ele vira uma variável de ambiente só naquele `RUN`.
- **Por que não `ARG TOKEN`**: valores de `ARG` e `ENV` ficam gravados no histórico e no config da imagem (`docker history`, `docker inspect`), e qualquer pessoa com a imagem os lê.

#### Heredocs e build checks
- **Heredocs** deixam scripts de várias linhas legíveis, em um único `RUN` (uma camada):

```dockerfile
RUN <<EOF
set -eux
apt-get update
apt-get install -y --no-install-recommends ca-certificates curl
rm -rf /var/lib/apt/lists/*
EOF
```

- **Build checks**: `docker build --check .` avalia o Dockerfile sem construir e aponta problemas como forma shell no `CMD`, `FROM` com maiúsculas e minúsculas inconsistentes, `ENV` em sintaxe antiga ou `ARG` com nome de segredo. A diretiva `# check=error=true` transforma os avisos em erro, útil no CI.
- **Saída do build**: `--progress=plain` mostra o log completo de cada passo (o padrão, `auto`, resume). Útil para depurar um `RUN` que falha.

### Buildx: builders, cache e saídas

#### Drivers de builder

| Driver | Onde roda o BuildKit | Uso |
|---|---|---|
| `docker` (padrão) | Embutido no daemon | Build local simples; com o containerd image store, já faz multiplataforma e exporta cache |
| `docker-container` | Contêiner `moby/buildkit` criado pelo Buildx | Recursos completos de cache e saída, versão do BuildKit independente do Engine |
| `kubernetes` | Pods em um cluster | Builders compartilhados e escaláveis |
| `remote` | Um BuildKit já em execução, acessado por TCP/socket | Infraestrutura de build própria |
| Docker Build Cloud | Builders gerenciados pela Docker (amd64 e arm64 nativos) | Cache compartilhado entre o time e o CI sem manter infraestrutura |

- `docker buildx create --name multi --driver docker-container --use`, `docker buildx ls`, `docker buildx inspect --bootstrap`, `docker buildx rm`.

#### Saídas do build

| Opção | Resultado |
|---|---|
| `--load` | Carrega a imagem no image store local (padrão com o driver `docker`) |
| `--push` | Envia ao registry (atalho para `--output type=registry`) |
| `--output type=local,dest=./out` | Grava o **sistema de arquivos final** em um diretório (ex.: extrair binários compilados) |
| `--output type=tar,dest=out.tar` | Tarball do sistema de arquivos |
| `--output type=oci,dest=img.tar` / `type=docker` | Tarball da imagem em formato OCI / Docker |

- Com o driver `docker-container`, a imagem **não aparece** em `docker image ls` a menos que você use `--load` ou `--push`.

#### Cache exportável
O cache local do builder se perde em runners efêmeros de CI. Exporte e importe:

| Backend | Exemplo | Quando usar |
|---|---|---|
| `inline` | `--cache-to type=inline` | Cache embutido na própria imagem; simples, só modo `min` |
| `registry` | `--cache-to type=registry,ref=org/app:buildcache,mode=max --cache-from type=registry,ref=org/app:buildcache` | Qualquer CI com acesso ao registry |
| `gha` | `--cache-to type=gha,mode=max --cache-from type=gha` | GitHub Actions |
| `local` | `--cache-to type=local,dest=/tmp/cache` | Cache em diretório persistido pelo CI |
| `s3` / `azblob` | Buckets de nuvem | Pipelines na AWS ou Azure |

- **`mode=min`** (padrão) exporta só as camadas da imagem final; **`mode=max`** exporta também as camadas dos estágios intermediários, que é o que acelera builds multi-stage.

### Imagens multiplataforma

#### Estratégias

| Estratégia | Como funciona | Prós e contras |
|---|---|---|
| **Emulação QEMU** | O builder executa instruções de outra arquitetura via `binfmt_misc` | Zero configuração no Docker Desktop; **lenta** em compilação pesada |
| **Nós nativos** | Um builder com um nó `amd64` e outro `arm64` (ou Docker Build Cloud) | Rápida; exige infraestrutura |
| **Compilação cruzada** | O estágio de build roda na plataforma nativa (`--platform=$BUILDPLATFORM`) e compila para `$TARGETOS/$TARGETARCH` | Rápida e barata; depende do suporte da linguagem (Go, Rust, .NET) |

```dockerfile
# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM golang:1.25 AS build
ARG TARGETOS TARGETARCH
WORKDIR /src
COPY . .
RUN GOOS=$TARGETOS GOARCH=$TARGETARCH CGO_ENABLED=0 go build -o /out/app .

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/app /app
ENTRYPOINT ["/app"]
```

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t org/app:1.0 --push .
```

- O resultado é um **index** com um manifest por plataforma, sob a mesma tag. Quem faz o pull recebe automaticamente a variante da sua arquitetura.
- **Requisito**: o image store clássico não guarda imagens multiplataforma. Com o **containerd image store** (padrão no Engine 29 e no Docker Desktop) funciona direto; antes disso, era preciso um builder `docker-container` e `--push`.
- **Argumentos automáticos**: `BUILDPLATFORM`, `TARGETPLATFORM`, `TARGETOS`, `TARGETARCH`, `TARGETVARIANT` (declare com `ARG` para usar).
- Sintoma clássico de arquitetura errada: `exec format error` ao iniciar o contêiner (por exemplo, imagem `amd64` construída em um Mac Apple Silicon sem `--platform`).

### Bake e atestados

#### Docker Bake
Arquivo declarativo (`docker-bake.hcl`, JSON ou o próprio `compose.yaml`) que descreve vários builds, executados em paralelo com `docker buildx bake`.

```hcl
variable "TAG" { default = "dev" }

group "default" { targets = ["api", "worker"] }

target "_comum" {
  platforms  = ["linux/amd64", "linux/arm64"]
  cache-from = ["type=gha"]
  cache-to   = ["type=gha,mode=max"]
}

target "api" {
  inherits = ["_comum"]
  context  = "./api"
  tags     = ["ghcr.io/org/api:${TAG}"]
}

target "worker" {
  inherits = ["_comum"]
  context  = "./worker"
  tags     = ["ghcr.io/org/worker:${TAG}"]
}
```

- `docker buildx bake --print` mostra a configuração resolvida; `TAG=1.4.2 docker buildx bake --push` constrói e envia tudo.
- Desde o **Compose v5**, o `docker compose build` delega os builds ao Bake.

#### SBOM e provenance
- **SBOM** (Software Bill of Materials): inventário dos pacotes da imagem. `docker buildx build --sbom=true …`
- **Provenance** (SLSA): como, onde e a partir de qual código a imagem foi construída. `--provenance=mode=max` inclui detalhes completos (em repositórios públicos, cuidado com o que o build expõe).
- Os atestados são anexados ao index da imagem no registry e podem ser lidos com `docker buildx imagetools inspect <ref> --format '{{ json .SBOM }}'` e analisados pelo Docker Scout (capítulo 9).

### Decisão rápida — BuildKit e Buildx

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Build precisa de token para baixar dependências privadas | `RUN --mount=type=secret` + `--secret` | `ARG TOKEN` ou `COPY .npmrc` |
| Clonar repositório privado no build | `RUN --mount=type=ssh` + `--ssh default` | Copiar a chave SSH para a imagem |
| Build lento no CI porque o cache se perde | `--cache-to/--cache-from` (`registry` ou `gha`, `mode=max`) | Desligar o cache |
| Instalação de pacotes lenta a cada build | `--mount=type=cache` no diretório do gerenciador | Aceitar a lentidão |
| Imagem para servidores `amd64` e Macs/Graviton `arm64` | `buildx build --platform linux/amd64,linux/arm64 --push` | Duas tags diferentes por arquitetura |
| Compilação sob QEMU muito lenta | Compilação cruzada com `$BUILDPLATFORM` ou nós nativos | Aumentar o timeout do CI |
| `exec format error` | Construir ou baixar para a plataforma certa (`--platform`) | Reinstalar dependências |
| Extrair só o binário compilado, sem gerar imagem | `--output type=local,dest=./out` | `docker create` + `docker cp` |
| Vários serviços construídos juntos, com configuração comum | Docker Bake | Script shell com vários `docker build` |
| Auditar de onde veio uma imagem | Provenance e SBOM no build | Confiar só na tag |
| Ver o log completo de um passo que falha | `--progress=plain` | Rodar de novo esperando outro resultado |

---

## 6. Redes

> **Ideia central**: coloque os contêineres que conversam entre si em uma **rede bridge definida pelo usuário**. Nela, eles se encontram **pelo nome** (DNS embutido) e ficam isolados de outras redes. **Publique portas** (`-p`) só para o que precisa ser acessado de fora do host.

### Modelo de rede do Docker

#### Container Network Model (CNM)
A rede do Docker segue o **Container Network Model (CNM)**, implementado pela biblioteca **libnetwork** (hoje parte do repositório do Moby). O CNM define três objetos e dois tipos de driver:

| Objeto do CNM | O que é | No Linux |
|---|---|---|
| **Sandbox** | A configuração de rede isolada de um contêiner: interfaces, rotas, DNS | Um **namespace de rede** |
| **Endpoint** | A ligação de um sandbox a uma rede. Um contêiner em duas redes tem dois endpoints | Um **par veth** (uma ponta no contêiner, outra na bridge) |
| **Network** | Um grupo de endpoints que se comunicam diretamente | Uma bridge Linux, uma VXLAN (overlay) etc. |

| Tipo de driver | Função | Exemplos |
|---|---|---|
| **Driver de rede** | Cria a rede e liga os endpoints a ela | Nativos: `bridge`, `host`, `none`, `overlay`, `macvlan`, `ipvlan`. Remotos: plugins de terceiros |
| **Driver de IPAM** | Gerencia os endereços: sub-redes, gateways e IPs dos endpoints | `default` (embutido) ou plugin de IPAM (`--ipam-driver`) |

- **Como o Engine usa o CNM**: `docker network create` pede ao driver de rede para criar a rede e ao driver de IPAM uma sub-rede; `docker run --network` cria o sandbox, pede um endpoint e um IP e liga os dois.
- **Escopo**: redes `local` (bridge, host, macvlan) valem em um host; redes `swarm` (overlay) valem no cluster inteiro. A coluna `SCOPE` de `docker network ls` mostra qual.
- **Kubernetes não usa o CNM**: usa o **CNI** (Container Network Interface), com plugins como Calico e Cilium. O modelo de rede do Kubernetes está resumido no capítulo 13.

#### Criar e inspecionar redes

```bash
# Bridge para um time de desenvolvimento, com faixa própria
docker network create --driver bridge \
  --subnet 172.30.0.0/24 --gateway 172.30.0.1 --ip-range 172.30.0.128/25 \
  --label equipe=dev dev-net

docker network ls --filter driver=bridge
docker network inspect dev-net -f '{{json .IPAM.Config}}'
docker run -d --name api --network dev-net --ip 172.30.0.200 app:1.0
docker network connect --alias cache backend api     # segunda rede, com alias
docker network disconnect backend api
docker network rm dev-net                            # falha se houver contêineres ligados
docker network prune                                 # remove redes sem contêineres
```

- `--subnet`, `--gateway` e `--ip-range` configuram o **IPAM** da rede; sem elas, a sub-rede sai de `default-address-pools`. `--ip` fixo só funciona em redes com `--subnet` declarada.
- `docker network inspect` mostra o driver, o escopo, o IPAM, as opções e os **contêineres conectados com IP e MAC**.

### Drivers de rede

#### Visão geral

| Driver | O que faz | Quando usar |
|---|---|---|
| **bridge** (padrão) | Rede virtual privada no host, com NAT para a saída e portas publicadas para a entrada | Contêineres de um mesmo host (caso mais comum) |
| **host** | O contêiner usa a pilha de rede do host diretamente; não há isolamento de rede nem mapeamento de portas | Desempenho máximo de rede, muitas portas, ferramentas de rede. Linux (no Docker Desktop, suporte recente e limitado) |
| **none** | Só a interface de loopback | Jobs que não devem ter rede |
| **overlay** | Rede distribuída entre vários hosts (VXLAN) | Swarm; contêineres em hosts diferentes |
| **macvlan** | Cada contêiner recebe um **MAC próprio** e aparece como um dispositivo físico na LAN | Aplicações legadas que precisam estar na rede física |
| **ipvlan** | IP próprio na LAN compartilhando o MAC do host (modos L2 e L3) | Quando a rede limita MACs por porta de switch |
| `container:<nome>` | Compartilha o namespace de rede de outro contêiner | Sidecars e depuração (`netshoot`) |
| Plugins | Drivers de terceiros | Integração com SDN específica |

#### Bridge padrão vs. bridge definida pelo usuário

| Aspecto | Bridge padrão (`bridge`, interface `docker0`) | Bridge definida pelo usuário (`docker network create app`) |
|---|---|---|
| Resolução de nomes | **Não há** DNS por nome (só IP ou o obsoleto `--link`) | **DNS embutido**: nome do contêiner, `--network-alias` e, no Compose, o nome do serviço |
| Isolamento | Todos os contêineres sem `--network` caem nela e se enxergam | Só os contêineres conectados àquela rede se enxergam |
| Conectar e desconectar em execução | Não | `docker network connect/disconnect` |
| Configuração | Global, no `daemon.json` | Por rede (sub-rede, gateway, MTU, `--internal`) |
| Recomendação | Evitar em aplicações | **Usar sempre** |

- O **DNS embutido** responde em `127.0.0.11` dentro do contêiner e encaminha nomes externos para os servidores do host.
- Um contêiner pode estar em **várias redes** ao mesmo tempo (ex.: `frontend` e `backend`), o que permite segmentar: o proxy fala com a API, a API fala com o banco, o proxy não enxerga o banco.
- **`--internal`** cria uma rede sem rota para fora: bom para bancos e serviços que não devem acessar a internet.

#### Opções de rede do `docker run`

| Opção | Efeito |
|---|---|
| `--network <rede\|host\|none\|container:<nome>>` | Rede ou modo de rede do contêiner. `--net` é o nome antigo, ainda aceito |
| `--network-alias <nome>` | Nome adicional no DNS da rede |
| `-p` / `--publish` | Publica uma porta do contêiner em uma porta do host |
| `--expose <porta>` | Equivale ao `EXPOSE` na execução: só documenta, não publica |
| `--hostname` / `-h` | Hostname do contêiner (namespace UTS) |
| `--dns`, `--dns-search`, `--dns-option` | Servidores DNS, domínios de busca e opções do `resolv.conf` do contêiner |
| `--add-host nome:ip` | Entrada extra no `/etc/hosts` do contêiner |
| `--ip`, `--ip6` | IP fixo (só em redes definidas pelo usuário com sub-rede declarada) |
| `--mac-address` | Endereço MAC da interface |
| `--link <contêiner>:<alias>` | **Legado**: ligação entre contêineres na bridge padrão, com variáveis de ambiente e entrada no `/etc/hosts`. Substituído pelas redes definidas pelo usuário |

- Não existe `--default-gateway` no `docker run`: o gateway é o da rede (definido com `docker network create --gateway`), e quem define o gateway padrão da bridge `docker0` é o daemon (capítulo 1).
- **Etapas ao conectar um contêiner a uma rede bridge**: o Docker cria um **par veth**, liga a ponta do host (`vethXXXX`) à bridge, move a outra ponta para o namespace de rede do contêiner com o nome `eth0`, define o MAC, aloca um **IP da sub-rede** da bridge e configura a rota padrão e o DNS.
- No **Linux**, o host alcança o IP interno do contêiner diretamente (`curl http://172.17.0.3`). No **Docker Desktop** não, porque os contêineres estão dentro da VM: use as portas publicadas.

### Portas, firewall e acesso ao host

#### Publicação de portas

| Sintaxe | Efeito |
|---|---|
| `-p 8080:80` | Porta 8080 de **todas as interfaces** do host (IPv4 e IPv6) → porta 80 do contêiner |
| `-p 127.0.0.1:8080:80` | Só no loopback do host: acessível apenas localmente |
| `-p 80` | Porta 80 do contêiner em uma porta **aleatória** do host |
| `-P` | Publica **todas as portas do `EXPOSE`** em portas aleatórias |
| `-p 5353:53/udp` | Porta UDP |
| `-p 8000-8010:8000-8010` | Faixa de portas |

- **`EXPOSE` não publica nada**; ele só documenta e alimenta o `-P`.
- Contêineres na **mesma rede** se comunicam pela porta interna, **sem** `-p`. Publicar a porta do banco "para a API acessar" é desnecessário e expõe o banco.
- Porta já em uso no host → o `docker run` falha com código **125** (`bind: address already in use`).

#### Docker e o firewall do host
- No Linux, o Docker cria regras de **iptables** (ou nftables, experimental no Engine 29) para NAT e portas publicadas. Essas regras são avaliadas **antes** das regras de ferramentas como **UFW** e **firewalld**: uma porta publicada com `-p 5432:5432` fica **acessível da internet mesmo com o UFW bloqueando a porta**.
- Formas corretas de restringir: publicar só no `127.0.0.1` (atrás de um proxy reverso), não publicar portas que não precisam, ou adicionar regras na chain **`DOCKER-USER`**, que o Docker reserva para regras do administrador.
- Desde o Engine 28, portas **não publicadas** de contêineres em redes bridge deixaram de ser alcançáveis diretamente por outros hosts da LAN.

#### Como a publicação de portas funciona por dentro
Não há mágica: o Docker programa o **netfilter** do kernel. Para `docker run -d -p 8080:80 --name web nginx`, com o contêiner em `172.17.0.3`:

```text
tabela nat
  PREROUTING / OUTPUT → chain DOCKER
    DNAT  tcp dpt:8080  to:172.17.0.3:80      # entrada: porta do host → contêiner
  POSTROUTING
    MASQUERADE  172.17.0.0/16 → fora          # saída: contêineres usam o IP do host
tabela filter
  FORWARD → chains do Docker (DOCKER, DOCKER-USER, isolamento entre redes)
    ACCEPT  tcp → 172.17.0.3 dpt:80           # libera o tráfego encaminhado
```

- **DNAT** (NAT de destino) troca `IP-do-host:8080` por `172.17.0.3:80`; **MASQUERADE** (NAT de origem) faz o tráfego de saída dos contêineres usar o IP do host.
- As chains de **isolamento** impedem que redes bridge diferentes se falem; a `DOCKER-USER` é avaliada antes das regras do Docker e é o lugar das regras do administrador. Os nomes exatos das chains mudaram ao longo das versões (o Engine 28 reorganizou a tabela filter), então consulte a sua versão com `sudo iptables -S` e `sudo iptables -t nat -S`.
- Além das regras, o Docker pode iniciar o **`docker-proxy`** (userland proxy) para cada porta publicada, que atende conexões vindas do próprio host via `localhost`. Pode ser desligado com `"userland-proxy": false` no `daemon.json`.

#### Acessar o host a partir do contêiner
- **Docker Desktop**: use o nome `host.docker.internal`.
- **Linux**: `docker run --add-host=host.docker.internal:host-gateway …` (ou `extra_hosts` no Compose). `localhost` dentro do contêiner é o **próprio contêiner**, não o host.
- O serviço no host precisa escutar em uma interface alcançável pela bridge (não só em `127.0.0.1`).

### Redes entre hosts

#### Overlay e redes de camada 2
- **Overlay** conecta contêineres em vários daemons de um Swarm, encapsulando o tráfego em **VXLAN**. Redes overlay criadas com `--attachable` aceitam contêineres avulsos (`docker run`), além de serviços.
- `--opt encrypted` cifra o tráfego de dados da overlay com IPsec (o tráfego de controle do Swarm já é cifrado). Tem custo de desempenho.
- **Portas necessárias entre os nós do Swarm**: **2377/tcp** (gerenciamento do cluster), **7946/tcp e udp** (descoberta e gossip entre nós) e **4789/udp** (dados da overlay, VXLAN).
- **macvlan**: por padrão, o **host não consegue falar** com os próprios contêineres macvlan (limitação do kernel); é preciso criar uma interface macvlan auxiliar no host. Muitas redes Wi-Fi e provedores de nuvem não aceitam vários MACs por interface.

#### Integração com sistemas legados
Aplicações em contêiner quase sempre precisam falar com sistemas que **não** estão em contêineres: bancos em servidores físicos, mainframes, serviços em VMs, APIs de parceiros.

| Necessidade | Solução |
|---|---|
| O contêiner acessa um sistema legado | Nada especial: o tráfego de saída sai pelo IP do host (NAT). Use o **DNS** da empresa (`dns` no `daemon.json` ou `--dns`) e, se preciso, `--add-host legado.local:10.0.5.20` |
| O sistema legado precisa chegar ao contêiner | **Publicar a porta** (`-p` ou `--publish` no Swarm) e apontar o legado para o host, um load balancer ou o routing mesh |
| O legado espera um IP na rede física (firewall por IP, licença por MAC, multicast) | **macvlan** ou **ipvlan**: o contêiner ganha IP próprio na LAN |
| Serviço Swarm e contêineres avulsos precisam se falar | Rede overlay com **`--attachable`** |
| O legado só aceita um IP de origem fixo | Sair por um host ou gateway de saída conhecido; em nuvem, NAT gateway com IP fixo |

- Nomes externos são resolvidos pelo DNS embutido (`127.0.0.11`), que encaminha para os servidores configurados. Em redes corporativas com DNS próprio, configurar `dns` e `dns-search` no daemon evita falhas de resolução.
- Conflitos de sub-rede com a rede corporativa (os `172.17.0.0/16` e `172.18.0.0/16` do Docker contra faixas internas) quebram o acesso ao legado; ajuste `bip` e `default-address-pools`.

#### Números de rede

| Item | Valor |
|---|---|
| Sub-rede padrão da bridge `docker0` | `172.17.0.0/16` |
| Endereço do DNS embutido | `127.0.0.11` |
| Gerenciamento do Swarm | **2377/tcp** |
| Descoberta entre nós do Swarm | **7946/tcp e 7946/udp** |
| Tráfego da overlay (VXLAN) | **4789/udp** |
| Chain de iptables para regras do administrador | `DOCKER-USER` |
| Nome do host visto do contêiner (Docker Desktop) | `host.docker.internal` |

### Diagnóstico de rede

#### Ferramentas e sequência
1. **O contêiner está na rede certa?** `docker network inspect <rede>` lista os contêineres e IPs; `docker inspect -f '{{json .NetworkSettings.Networks}}' <c>`.
2. **O nome resolve?** De um contêiner na mesma rede: `docker run --rm --network app nicolaka/netshoot nslookup api`.
3. **A porta responde internamente?** `curl http://api:3000/health` a partir do `netshoot`.
4. **A aplicação escuta em `0.0.0.0`?** Uma aplicação que escuta só em `127.0.0.1` **dentro do contêiner** não recebe conexões vindas de fora dele, nem por porta publicada. Esse é um dos erros mais comuns.
5. **A porta está publicada?** `docker port <c>`; confira se o mapeamento é `host:contêiner` e não o contrário.
6. **Há firewall ou conflito de sub-rede?** Redes do Docker sobrepostas à VPN ou à rede corporativa quebram rotas; ajuste `default-address-pools`.

### Decisão rápida — Redes

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| API precisa falar com o banco no mesmo host | Rede bridge definida pelo usuário e o nome do contêiner/serviço | IP fixo do contêiner ou `--link` |
| Banco não deve ser acessível de fora | Não publicar a porta; rede `--internal` se não precisar de saída | `-p 5432:5432` |
| Painel administrativo só para acesso local | `-p 127.0.0.1:8080:80` | Confiar no UFW |
| Porta publicada ignora o UFW | Regras na chain `DOCKER-USER` ou bind em `127.0.0.1` | Desligar o iptables do Docker |
| Contêiner precisa acessar serviço do host | `host.docker.internal` (+ `host-gateway` no Linux) | `localhost` |
| Conexão recusada mesmo com `-p` correto | Fazer a aplicação escutar em `0.0.0.0` | Trocar a porta do host |
| Máximo desempenho de rede no Linux | `--network host` | Bridge com muitas portas publicadas |
| Contêineres em hosts diferentes se falando | Overlay (Swarm) ou orquestrador | Publicar portas e usar o IP dos hosts |
| Aplicação legada precisa de IP na LAN física | macvlan ou ipvlan | `--network host` |
| Depurar rede de imagem sem ferramentas | `nicolaka/netshoot` com `--network container:<c>` | Instalar pacotes no contêiner em produção |
| Redes do Docker conflitam com a VPN | `default-address-pools` | Desligar a VPN |

---

## 7. Armazenamento e Dados

> **Ideia central**: a camada gravável do contêiner é **efêmera** (some com o `docker rm`) e **lenta** para escrita intensa. Dados que precisam sobreviver ao contêiner vão para **volumes** (gerenciados pelo Docker) ou **bind mounts** (diretório do host). Dados temporários sensíveis podem ir para **tmpfs**.

### Onde os dados ficam

#### Camada gravável e storage
- Cada contêiner recebe uma **camada gravável** sobre as camadas da imagem. No Engine 29, instalações novas usam o **containerd image store** com **snapshotters** (em geral `overlayfs`); instalações antigas podem continuar com o storage driver **`overlay2`**. `docker info` mostra qual está em uso.
- Trocar entre o image store clássico e o do containerd **não migra** imagens e contêineres: eles ficam invisíveis até voltar a configuração (e precisam ser baixados ou reconstruídos no novo store).
- Escrever muito na camada gravável (logs, bancos, uploads) é lento por causa do copy-on-write e faz o contêiner crescer sem controle. Use volumes.

#### Storage drivers: passado e presente
O **storage driver** define como o Engine monta as camadas e grava na camada do contêiner. Materiais antigos dedicam bastante espaço a drivers que já não existem.

| Driver | Como funciona | Situação em 2026 |
|---|---|---|
| **AUFS** | Union filesystem em nível de **arquivo**; foi o primeiro driver do Docker. Copia o arquivo inteiro na primeira escrita e procura cada diretório do caminho em todas as camadas (lento com muitas camadas e muitos `import`) | Obsoleto no 19.03 e **removido no Engine 24** |
| **devicemapper** | Thin provisioning em nível de **bloco** (framework do kernel usado por LVM). Criado pela Red Hat para distribuições sem AUFS. Em modo `loop-lvm` era lento; `direct-lvm` exigia configurar um dispositivo dedicado | Obsoleto no 18.09 e **removido no Engine 25** |
| **overlay** (v1) | OverlayFS com só **duas camadas** por montagem; consumia muitos inodes | Obsoleto no 18.09 e **removido no Engine 24** |
| **overlay2** | OverlayFS com suporte nativo a **várias camadas**, compartilhamento de cache de páginas e cópia do arquivo só uma vez | Driver clássico **recomendado**; continua em instalações existentes |
| **btrfs** / **zfs** | Snapshots copy-on-write em nível de bloco do próprio sistema de arquivos | Suportados apenas quando `/var/lib/docker` está em Btrfs ou ZFS; casos específicos |
| **fuse-overlayfs** | Overlay em espaço de usuário | Usado no modo rootless em kernels antigos |
| **vfs** | Sem copy-on-write: cópia completa por camada | Só para testes |
| **containerd snapshotters** (`overlayfs` e outros) | O containerd gerencia imagens e camadas | **Padrão em instalações novas do Engine 29** |

- **Trocar o storage driver** (ou o image store) torna **inacessíveis** as imagens, os contêineres e os volumes anônimos criados com o anterior: eles ficam no disco, mas o daemon não os enxerga. Faça backup, exporte o que precisa (`docker save`, backup de volumes) e recrie depois da troca.
- `docker info --format '{{.Driver}}'` mostra o driver em uso.

#### Driver por sistema operacional

| Sistema | Driver ou snapshotter | Observação |
|---|---|---|
| Ubuntu, Debian, Fedora, RHEL, SLES atuais | containerd `overlayfs` (instalações novas do Engine 29) ou **`overlay2`** | O sistema de arquivos de `/var/lib/docker` deve ser **ext4** ou **xfs com `ftype=1`** (suporte a `d_type`) |
| RHEL e CentOS 7 (histórico) | `devicemapper` em `direct-lvm` | Era o padrão antes do `overlay2` ser suportado no kernel da Red Hat |
| SLES antigo com raiz em Btrfs | `btrfs` | Só quando `/var/lib/docker` está em Btrfs |
| Ubuntu antigo (histórico) | `aufs` | Removido no Engine 24 |
| **Windows** (contêineres Windows) | **`windowsfilter`** | Único driver dos contêineres Windows; isolamento `process` (Windows Server) ou `hyperv` |
| Docker Desktop (macOS, Windows com WSL 2) | `overlay2` ou containerd, **dentro da VM Linux** | O host não vê os arquivos diretamente |

#### Onde as camadas ficam no disco
Com o storage driver **`overlay2`** (image store clássico), tudo fica sob o `data-root` (padrão `/var/lib/docker`):

| Caminho | Conteúdo |
|---|---|
| `/var/lib/docker/overlay2/<id>/diff` | Os arquivos de **uma camada** (de imagem ou a camada gravável de um contêiner) |
| `/var/lib/docker/overlay2/<id>/lower` | Lista das camadas inferiores (links curtos em `overlay2/l/`) |
| `/var/lib/docker/overlay2/<id>/merged` | A **visão unificada** montada para o contêiner em execução |
| `/var/lib/docker/overlay2/<id>/work` | Diretório de trabalho interno do OverlayFS |
| `/var/lib/docker/image/overlay2/` | Metadados das imagens (config, cadeia de camadas) |
| `/var/lib/docker/containers/<id>/` | Config do contêiner, `hostname`, `resolv.conf` e os logs do `json-file` |
| `/var/lib/docker/volumes/<nome>/_data` | Dados dos volumes nomeados |

```bash
docker inspect -f '{{json .GraphDriver.Data}}' api | jq
# LowerDir (camadas da imagem), UpperDir (camada gravável), MergedDir, WorkDir
docker image inspect -f '{{json .RootFS.Layers}}' nginx:1.29
```

- **Camadas de imagem são somente leitura** e compartilhadas por todos os contêineres da mesma imagem; cada contêiner tem só a **sua** camada gravável (`UpperDir`). Uma escrita em arquivo da imagem copia o arquivo para cima (copy-on-write) e o OverlayFS mostra a versão nova.
- Com o **containerd image store** (padrão em instalações novas do Engine 29), o conteúdo das imagens fica em `/var/lib/containerd` (`io.containerd.content.v1.content` para os blobs e `io.containerd.snapshotter.v1.overlayfs` para as camadas descompactadas). A lógica de camadas é a mesma.
- **Nunca edite ou apague arquivos dentro de `/var/lib/docker`** à mão; use `docker image prune`, `docker system prune` e afins.

#### Tipos de montagem

| Tipo | Origem dos dados | Gerenciado pelo Docker | Uso típico |
|---|---|---|---|
| **Volume nomeado** | Área do Docker (`/var/lib/docker/volumes/<nome>/_data` no Linux) | Sim | Bancos de dados, dados de aplicação em produção |
| **Volume anônimo** | Igual, com nome aleatório | Sim | Criado por `VOLUME` no Dockerfile ou `-v /caminho`; difícil de rastrear |
| **Bind mount** | Qualquer caminho do host | Não | Código-fonte em desenvolvimento, arquivos de configuração, sockets |
| **tmpfs** | Memória RAM do host | — | Dados temporários ou sensíveis que não devem tocar o disco (Linux) |
| **Image mount** | Conteúdo de outra imagem, somente leitura | Sim | Montar dados ou ferramentas empacotados como imagem (Engine 28+) |

#### `-v` vs. `--mount`

```bash
# Volume nomeado
docker run -v dados-pg:/var/lib/postgresql/data postgres:17
docker run --mount type=volume,src=dados-pg,dst=/var/lib/postgresql/data postgres:17

# Bind mount somente leitura
docker run -v "$(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro" nginx
docker run --mount type=bind,src="$(pwd)/nginx.conf",dst=/etc/nginx/nginx.conf,readonly nginx

# tmpfs
docker run --mount type=tmpfs,dst=/tmp,tmpfs-size=64m app
```

- **`--mount`** é mais explícito e recomendado em scripts. Diferença importante: com `-v`, um bind mount de caminho **inexistente cria um diretório vazio** no host (o que causa erros confusos, como um diretório no lugar de um arquivo de configuração); com `--mount`, o comando **falha** com erro claro.
- Sufixos do `-v`: `:ro` (somente leitura), `:z`/`:Z` (rótulo SELinux compartilhado/privado).
- **Montar um único arquivo** também funciona: `--mount type=bind,src=/etc/app/config.yaml,dst=/app/config.yaml,readonly`. Uma escrita em um ponto de montagem somente leitura falha com `Read-only file system`.

#### Características dos volumes
- Um volume **não passa pelo union filesystem**: leituras e escritas vão direto ao diretório do volume, sem copy-on-write.
- É criado (ou reaproveitado) quando o contêiner é criado e **continua existindo** depois que o contêiner é removido.
- Pode ser **reutilizado e compartilhado** entre contêineres.
- **Não entra na imagem**: `docker commit`, `docker export` e `docker save` ignoram o conteúdo dos volumes montados.
- **Onde fica no host**: `docker volume inspect --format '{{ .Mountpoint }}' meu-volume` retorna `/var/lib/docker/volumes/meu-volume/_data` no Linux. No Docker Desktop, esse caminho fica **dentro da VM**, não no macOS ou no Windows.
- **Bind mounts dependem do host**: o diretório precisa existir, com as permissões certas, em **cada** host onde o contêiner rodar. Em um cluster isso vira um problema (o contêiner pode ser agendado em outro nó). Volumes nomeados, com driver compartilhado quando necessário, deixam a aplicação portátil.

#### Padrão antigo: data-only container e `--volumes-from`
- Antes do comando `docker volume` (Docker 1.9, 2015), o jeito de ter um volume "com nome" era criar um **contêiner só de dados**, que nunca rodava, e montar os volumes dele em outros contêineres com `--volumes-from`:

```bash
# Padrão antigo (ainda funciona, mas não é mais necessário)
docker container create -v /data --name dbdados alpine
docker run -d --volumes-from dbdados app

# Equivalente atual: volume nomeado
docker volume create dbdados
docker run -d --mount type=volume,src=dbdados,dst=/data app
```

- `--volumes-from <contêiner>` monta **todos** os volumes de outro contêiner, nos mesmos caminhos. Ainda é útil para **backup** rápido dos volumes de um contêiner existente: `docker run --rm --volumes-from app -v "$(pwd)":/backup alpine tar czf /backup/app.tgz /data`.
- **Nunca rode duas instâncias de banco de dados sobre o mesmo diretório de dados** (dois PostgreSQL ou dois MySQL montando o mesmo volume). Cada instância supõe ser a dona exclusiva dos arquivos: o PostgreSQL recusa iniciar ao encontrar o `postmaster.pid` da outra ou, se forçado, **corrompe os dados**. Para ter duas instâncias, use volumes separados e replicação do próprio banco.

### Comportamento e permissões

#### Pré-população de volumes
- Ao montar um **volume vazio** em um diretório que já tem arquivos na imagem, o Docker **copia** esses arquivos para o volume na primeira vez (a menos que se use `volume-nocopy`).
- **Bind mounts não pré-populam**: montar um diretório do host **esconde** o conteúdo da imagem naquele caminho. Esse é o motivo clássico de "sumiu o `node_modules`" ao montar o código-fonte em `/app` no desenvolvimento. Solução comum: um volume (anônimo ou nomeado) em `/app/node_modules` por cima do bind mount, ou o `develop.watch` do Compose (capítulo 8).

#### Permissões e UIDs
- O contêiner vê **UIDs e GIDs numéricos**, não nomes. Se a aplicação roda como UID 10001 e o bind mount pertence ao UID 1000 do host, a escrita falha com `permission denied`.
- Soluções: rodar o contêiner com o UID do dono (`-u $(id -u):$(id -g)` em desenvolvimento), ajustar a posse dos arquivos no build (`COPY --chown`) e, para volumes, deixar a imagem criar o diretório com o dono certo antes da montagem (a pré-população copia as permissões).
- Com **SELinux** (Fedora, RHEL), bind mounts podem exigir `:z` ou `:Z`.
- No **modo rootless** e com `userns-remap`, o root do contêiner é mapeado para um UID alto do host; arquivos criados em bind mounts aparecem com esse UID.

#### Backup, restauração e drivers

```bash
# Backup de um volume para um tarball no diretório atual
docker run --rm -v dados-pg:/origem:ro -v "$(pwd)":/backup alpine \
  tar czf /backup/dados-pg.tgz -C /origem .

# Restauração em um volume novo
docker volume create dados-pg-restaurado
docker run --rm -v dados-pg-restaurado:/destino -v "$(pwd)":/backup alpine \
  tar xzf /backup/dados-pg.tgz -C /destino
```

- Para bancos de dados, prefira a ferramenta de backup do próprio banco (`pg_dump`, `mysqldump`, snapshots) em vez de copiar arquivos com o banco rodando.
- Copiar `/var/lib/docker/volumes` inteiro em rotinas de backup do host funciona só com os contêineres **parados** (ou com snapshot do sistema de arquivos). Com aplicações gravando, a cópia pode ficar inconsistente.
- **Drivers de volume**: o driver `local` aceita opções de montagem, inclusive **NFS** e CIFS (`docker volume create --driver local --opt type=nfs --opt o=addr=10.0.0.5,rw --opt device=:/export nfs-dados`). Plugins de terceiros integram storage de nuvem ou distribuído.
- **Volume compartilhado entre contêineres**: vários contêineres podem montar o mesmo volume, mas o Docker **não coordena** escrita concorrente; isso é responsabilidade da aplicação.

#### Blocos, arquivos e objetos
Os drivers de volume e os registries se apoiam em três tipos de armazenamento:

| Tipo | Como é acessado | Pontos fortes | Uso típico com contêineres |
|---|---|---|---|
| **Blocos** | Dispositivo com blocos endereçáveis, formatado com um sistema de arquivos e montado em **um** nó por vez (EBS, discos gerenciados, iSCSI, SAN) | Baixa latência, alto IOPS, escrita no meio do arquivo | **Bancos de dados** e qualquer volume com muitas escritas pequenas |
| **Arquivos** | Sistema de arquivos compartilhado pela rede (NFS, SMB/CIFS, EFS, Azure Files) | Vários nós montam ao mesmo tempo | Dados compartilhados entre réplicas, conteúdo estático, uploads |
| **Objetos** | API HTTP (`PUT`/`GET` de objetos inteiros com metadados: S3, Azure Blob, GCS, MinIO) | Escala praticamente sem limite, durável, barato, acessível de qualquer nó | Armazenamento de **registries** (camadas de imagem), backups, artefatos, mídia |

- **Qual preferir**: para o **armazenamento de um registry** (Distribution, Harbor, MSR), **objetos** é o preferido quando disponível: várias réplicas do registry leem e gravam o mesmo bucket, sem sistema de arquivos compartilhado. Para um **banco de dados**, **blocos**.
- Armazenamento de objetos **não é montado como volume** comum: a aplicação usa a API (ou um driver/ferramenta que a traduz, com desempenho e semântica limitados).

#### Comandos de volumes

| Comando | O que faz |
|---|---|
| `docker volume create <nome>` | Cria um volume |
| `docker volume ls` / `ls -f dangling=true` | Lista volumes / os que não estão em uso |
| `docker volume inspect <nome>` | Mostra driver, opções e `Mountpoint` |
| `docker volume rm <nome>` | Remove (falha se estiver em uso) |
| `docker volume prune` / `prune -a` | Remove anônimos não usados / todos os não usados |
| `docker run --rm` | Remove também os **volumes anônimos** do contêiner (não os nomeados) |

### Decisão rápida — Armazenamento

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Dados de banco em produção | Volume nomeado (ou storage gerenciado) + backup pela ferramenta do banco | Camada gravável do contêiner |
| Código-fonte com recarga automática em desenvolvimento | Bind mount ou `develop.watch` do Compose | Rebuild a cada alteração |
| Arquivo de configuração do host | Bind mount somente leitura (`:ro`) | Copiar para dentro com `docker cp` |
| Segredo temporário que não pode ir para o disco | tmpfs (ou secrets do Compose/Swarm) | Variável de ambiente logada |
| Bind mount criou um diretório no lugar do arquivo | Usar `--mount` (falha se a origem não existe) e corrigir o caminho | Criar o arquivo dentro do diretório |
| `node_modules` sumiu ao montar o código | Volume em `/app/node_modules` por cima do bind mount | Instalar dependências no host |
| `permission denied` em bind mount | Alinhar UID/GID (`-u`, `--chown`) ou `:z` no SELinux | `chmod 777` |
| Compartilhar dados entre hosts | Volume com driver NFS/plugin ou storage de objetos | Volume `local` achando que replica |
| Backup de um volume | Contêiner temporário com `tar` montando o volume | Copiar `/var/lib/docker/volumes` com o daemon rodando |
| Limpeza sem perder dados importantes | `docker volume prune` (só anônimos) e revisar antes de `-a` | `docker system prune -a --volumes` em produção |

---

## 8. Docker Compose

> **Ideia central**: o Compose descreve uma **aplicação multi-contêiner** em um arquivo YAML (`compose.yaml`) e a gerencia como um **projeto**: serviços, redes, volumes, segredos e configurações sobem, são atualizados e descem juntos. É a ferramenta padrão para desenvolvimento local, testes de integração e implantações simples em um único host.

### Modelo e comandos

#### Projeto, arquivos e nomes
- **Comando**: `docker compose` (plugin da CLI, versão 5.x em 2026). O antigo `docker-compose` (v1, Python) está fora de suporte desde 2023.
- **Arquivo padrão**: `compose.yaml` (também aceita `compose.yml`, `docker-compose.yaml` e `docker-compose.yml`). Se existir **`compose.override.yaml`**, ele é mesclado automaticamente por cima.
- **Nome do projeto** (prefixo de contêineres, redes e volumes), por ordem de precedência: flag `-p`, variável `COMPOSE_PROJECT_NAME`, atributo `name:` no topo do arquivo e, por fim, o nome do diretório.
- **Nomes gerados**: contêineres `<projeto>-<serviço>-<n>`, rede padrão `<projeto>_default`, volumes `<projeto>_<volume>`.
- **Rede padrão**: todos os serviços entram em uma rede bridge do projeto e se encontram pelo **nome do serviço** (`db`, `redis`).
- O **campo `version:`** é obsoleto e só gera aviso.

#### Exemplo completo

```yaml
name: loja

services:
  web:
    build:
      context: ./web
      target: runtime
    image: ghcr.io/org/loja-web:${TAG:-dev}
    ports:
      - "127.0.0.1:8080:3000"
    environment:
      DATABASE_URL: postgres://loja@db:5432/loja
      NODE_ENV: ${NODE_ENV:-production}
    env_file: .env.web
    depends_on:
      db:
        condition: service_healthy
        restart: true
      migracao:
        condition: service_completed_successfully
    secrets:
      - db_senha
    networks: [frontend, backend]
    restart: unless-stopped
    deploy:
      resources:
        limits: { cpus: "1.0", memory: 512M }

  migracao:
    image: ghcr.io/org/loja-web:${TAG:-dev}
    command: ["npm", "run", "migrate"]
    depends_on:
      db:
        condition: service_healthy
    networks: [backend]

  db:
    image: postgres:17
    environment:
      POSTGRES_USER: loja
      POSTGRES_PASSWORD_FILE: /run/secrets/db_senha
    secrets:
      - db_senha
    volumes:
      - dados-db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U loja"]
      interval: 10s
      timeout: 3s
      retries: 5
      start_period: 20s
    networks: [backend]

  adminer:
    image: adminer
    profiles: [debug]
    ports: ["127.0.0.1:8081:8080"]
    networks: [backend]

networks:
  frontend:
  backend:
    internal: true

volumes:
  dados-db:

secrets:
  db_senha:
    file: ./secrets/db_senha.txt
```

#### Comandos do dia a dia

| Comando | O que faz |
|---|---|
| `docker compose up -d` | Cria e inicia tudo em segundo plano; **recria** só os serviços cuja configuração ou imagem mudou |
| `docker compose up -d --build` | Reconstrói as imagens antes de subir |
| `docker compose up -d --wait` | Espera os serviços ficarem `running`/`healthy` antes de retornar (útil em CI) |
| `docker compose down` | Para e **remove** contêineres e redes do projeto. **Preserva** volumes nomeados |
| `docker compose down -v` | Remove também os volumes nomeados do projeto e os anônimos. **Apaga dados** |
| `docker compose stop` / `start` | Para e inicia sem remover |
| `docker compose ps` / `ls` | Serviços do projeto / projetos em execução |
| `docker compose logs -f web` | Logs de um ou mais serviços |
| `docker compose exec web sh` | Processo novo no contêiner em execução |
| `docker compose run --rm web npm test` | Contêiner **novo e avulso** do serviço, para tarefas pontuais |
| `docker compose build` / `pull` / `push` | Constrói (via Bake no v5), baixa ou envia as imagens |
| `docker compose config` | Mostra o modelo **resolvido** (interpolação, merge de arquivos, perfis). Primeiro passo para depurar |
| `docker compose up -d --scale worker=3` | Várias réplicas de um serviço (sem `container_name` nem porta fixa no host) |
| `docker compose watch` | Sincroniza e reconstrói automaticamente em desenvolvimento |
| `docker compose --profile debug up` | Inclui serviços do perfil `debug` |

### Ordem de inicialização, variáveis e composição de arquivos

#### `depends_on` e healthchecks

| Condição | Espera até |
|---|---|
| `service_started` (padrão na sintaxe curta) | O contêiner da dependência **iniciar** (não significa pronto) |
| `service_healthy` | O healthcheck da dependência ficar **`healthy`** |
| `service_completed_successfully` | A dependência **terminar com código 0** (migrações, seeds) |

- `restart: true` dentro do `depends_on` reinicia o serviço dependente quando a dependência for atualizada pelo Compose.
- `required: false` torna a dependência opcional.
- `depends_on` só controla a **ordem no `up`**. Se o banco cair depois, a aplicação precisa tratar reconexão; nenhum orquestrador substitui isso.

#### Variáveis de ambiente e interpolação
Há **dois mecanismos diferentes**, que costumam ser confundidos:

| Mecanismo | Para que serve | Onde |
|---|---|---|
| **Interpolação** `${VAR}` | Substituir valores **no arquivo Compose** antes de aplicá-lo | Lê do shell e do arquivo **`.env`** do diretório do projeto (ou `--env-file`) |
| **`environment`** / **`env_file`** | Definir variáveis **dentro do contêiner** | No serviço |

- Sintaxes de interpolação: `${VAR:-padrão}` (padrão se vazia ou ausente), `${VAR-padrão}` (só se ausente), `${VAR:?mensagem}` (erro se vazia ou ausente), `$$` para um `$` literal.
- **Precedência dentro do contêiner** (da maior para a menor): `docker compose run -e`, atributo `environment`, atributo `env_file` e, por último, o `ENV` da imagem.
- O `.env` **não é injetado** automaticamente nos contêineres; ele só alimenta a interpolação. Para levar variáveis ao contêiner, referencie-as em `environment` ou use `env_file`.

#### Segredos e configs
- **`secrets`**: montados como arquivo em **`/run/secrets/<nome>`**, a partir de um arquivo (`file:`) ou de uma variável de ambiente do host (`environment:`). Muitas imagens oficiais aceitam variáveis `*_FILE` (como `POSTGRES_PASSWORD_FILE`) para ler o segredo do arquivo.
- **`configs`**: mesma ideia para arquivos de configuração não sensíveis.
- Vantagem sobre variáveis de ambiente: segredos em arquivo não aparecem em `docker inspect`, em dumps de ambiente nem em logs de erro que imprimem o ambiente.

#### Combinar arquivos: override, `-f`, `extends` e `include`

| Recurso | Como funciona | Uso |
|---|---|---|
| `compose.override.yaml` | Mesclado automaticamente por cima do `compose.yaml` | Ajustes de desenvolvimento (bind mounts, portas de debug) |
| `-f base.yaml -f prod.yaml` | Mescla na ordem; o último vence em valores simples, listas como `ports` são concatenadas | Variações por ambiente |
| `extends` | Um serviço herda a definição de outro (mesmo arquivo ou outro) | Reaproveitar configuração comum |
| `include` | Importa outro projeto Compose inteiro, com caminhos relativos ao arquivo incluído | Aplicações com partes mantidas por times diferentes |
| Fragmentos YAML e `x-` | Âncoras (`&comum`, `<<: *comum`) em chaves de extensão `x-…` | Evitar repetição no mesmo arquivo |

#### Perfis
- Serviços com `profiles: [debug]` **só sobem** quando o perfil é ativado (`--profile debug` ou `COMPOSE_PROFILES=debug`). Serviços sem `profiles` sobem sempre.
- Uso típico: ferramentas de administração, mocks, serviços de observabilidade opcionais.

### Fluxo de desenvolvimento

#### `develop.watch`

```yaml
services:
  web:
    build: .
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
        - action: rebuild
          path: package.json
        - action: sync+restart
          path: ./config
          target: /app/config
```

| Ação | Efeito ao detectar mudança |
|---|---|
| `sync` | Copia os arquivos para o contêiner em execução (ideal com recarga automática do framework) |
| `rebuild` | Reconstrói a imagem e recria o contêiner (ex.: dependências mudaram) |
| `sync+restart` | Copia os arquivos e reinicia o contêiner (ex.: configuração lida só na inicialização) |
| `sync+exec` | Copia e executa um comando no contêiner |

- Rode com `docker compose watch` ou `docker compose up --watch`. Diferente do bind mount, o watch respeita o `.dockerignore`, funciona bem em sistemas de arquivos de VMs (Docker Desktop) e não esconde `node_modules`.

#### Outros recursos úteis
- **`docker init`**: gera `Dockerfile`, `compose.yaml` e `.dockerignore` iniciais com boas práticas para a linguagem detectada (Node, Python, Go, Java, Rust, .NET, PHP).
- **Hooks de ciclo de vida**: `post_start` e `pre_stop` executam comandos no contêiner depois de iniciar e antes de parar (ex.: ajustar permissões em um volume).
- **`init: true`**: usa o `tini` como PID 1 (o mesmo que `--init`).
- **`stop_grace_period: 30s`**: tempo entre o sinal de parada e o `SIGKILL`.
- **`deploy.resources.limits`** e **`deploy.replicas`** são respeitados também fora do Swarm.
- **Compose em produção** faz sentido em **um único host** (pequenas aplicações, VMs de borda). Para vários hosts, alta disponibilidade e rolling updates, use Swarm ou Kubernetes (capítulo 11).

### Decisão rápida — Compose

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| API sobe antes do banco aceitar conexões | `depends_on` com `condition: service_healthy` + healthcheck no banco | `sleep 30` no entrypoint |
| Rodar migrações antes da aplicação | Serviço de migração + `service_completed_successfully` | Migração no entrypoint de cada réplica |
| Ver o arquivo final depois de variáveis e overrides | `docker compose config` | Adivinhar a mesclagem |
| Variável do `.env` não aparece no contêiner | Referenciar em `environment` ou usar `env_file` | Esperar que o `.env` seja injetado |
| Senha do banco no Compose | `secrets` + variáveis `*_FILE` | Senha em `environment` versionada |
| Diferenças entre desenvolvimento e produção | `compose.override.yaml` ou `-f` por ambiente | Dois arquivos inteiros duplicados |
| Ferramenta de administração opcional | `profiles` | Comentar e descomentar serviços |
| Derrubar o ambiente sem perder o banco | `docker compose down` | `docker compose down -v` |
| Recarga rápida de código em desenvolvimento | `docker compose watch` | Rebuild manual a cada mudança |
| Tarefa pontual (testes, shell) com a configuração do serviço | `docker compose run --rm <serviço> <comando>` | `docker run` repetindo todas as flags |
| Aplicação em vários hosts com alta disponibilidade | Swarm ou Kubernetes | Compose em cada host sincronizado à mão |
| Começar a containerizar um projeto existente | `docker init` e revisão do resultado | Copiar um Dockerfile genérico da internet |

---

## 9. Segurança

> **Ideia central**: segurança em Docker tem três frentes. **O host e o daemon**: quem controla o daemon controla o host. **O contêiner em execução**: menos privilégios, menos capabilities, sistema de arquivos somente leitura, sem root. **A cadeia de suprimentos**: imagens mínimas, conhecidas, escaneadas, assinadas e fixadas por digest. Nenhuma camada substitui as outras.

### Proteger o host e o daemon

#### Superfície de ataque do daemon
- O `dockerd` tradicional roda como **root**. Acesso ao socket `/var/run/docker.sock` (grupo `docker`, bind mount do socket, API por TCP) permite `docker run -v /:/host --privileged …` e, portanto, **root no host**.
- **Montar o `docker.sock` em um contêiner** (Traefik, Portainer, runners de CI) dá a esse contêiner controle total do host, **mesmo com `:ro`** (o somente leitura vale para o arquivo, não para a API). Se for inevitável, use um **proxy de socket** que libere só os endpoints necessários, ou restrinja o que roda ali.
- **API remota**: só por SSH ou TLS mútuo (2376). Nunca a porta 2375 exposta.
- Mantenha o Engine atualizado: correções de runc e containerd (fugas de contêiner) chegam por atualização.

#### Modo rootless e `userns-remap`

| Recurso | Como funciona | Limitações |
|---|---|---|
| **Rootless** | O **daemon e os contêineres** rodam como um usuário comum, dentro de um user namespace (`dockerd-rootless-setuptool.sh install`) | Portas abaixo de 1024 exigem ajuste de `sysctl`; rede com desempenho um pouco menor; alguns drivers e opções indisponíveis; um daemon por usuário |
| **`userns-remap`** | O daemon continua root, mas o **root do contêiner** é mapeado para um UID alto sem privilégio no host | Afeta permissões de bind mounts; incompatível com alguns recursos (`--privileged`, `--network host` com certas opções) |
| **Enhanced Container Isolation** | Recurso do Docker Desktop Business que roda os contêineres com user namespace e bloqueia acesso ao socket do Docker | Só Docker Desktop, assinatura Business |

- Com qualquer um deles, uma fuga do contêiner cai em um usuário sem privilégios no host, em vez de root.

### Endurecer o contêiner em execução

#### Capabilities
O root do Linux é dividido em **capabilities**. Por padrão, o Docker concede um conjunto reduzido de **14**: `CHOWN`, `DAC_OVERRIDE`, `FOWNER`, `FSETID`, `KILL`, `SETGID`, `SETUID`, `SETPCAP`, `SETFCAP`, `NET_BIND_SERVICE`, `NET_RAW`, `SYS_CHROOT`, `MKNOD` e `AUDIT_WRITE`.

- **Remova tudo e adicione só o necessário**: `--cap-drop ALL --cap-add NET_BIND_SERVICE`.
- Capabilities perigosas que costumam ser pedidas sem necessidade: `SYS_ADMIN` (quase root), `NET_ADMIN`, `SYS_PTRACE`, `SYS_MODULE`.
- **`--privileged`** concede **todas** as capabilities, acesso a todos os dispositivos do host e desliga seccomp e AppArmor. Equivale a rodar sem isolamento. Use apenas em casos muito específicos (Docker-in-Docker, drivers) e nunca para "resolver" um erro de permissão.

#### Controles de segurança em execução

| Controle | Flag | Efeito |
|---|---|---|
| Usuário não root | `-u 10001:10001` ou `USER` no Dockerfile | Limita o impacto de uma falha na aplicação |
| Sem escalada de privilégio | `--security-opt no-new-privileges` | Impede que binários `setuid` ganhem privilégios |
| Sistema de arquivos somente leitura | `--read-only` + `--tmpfs /tmp` | Impede que um invasor grave binários ou altere a aplicação |
| seccomp | Perfil padrão ativo; `--security-opt seccomp=perfil.json` | Bloqueia chamadas de sistema perigosas (o padrão bloqueia cerca de 44, como `mount`, `reboot`, `kexec_load`) |
| AppArmor / SELinux | Perfil `docker-default` / rótulos SELinux | Controle de acesso obrigatório a arquivos e recursos |
| Limite de processos | `--pids-limit 200` | Protege contra fork bombs |
| Limites de memória e CPU | `--memory`, `--cpus` | Evita que um contêiner derrube o host (capítulo 10) |
| Sem compartilhar namespaces do host | Evitar `--pid host`, `--ipc host`, `--network host`, `--userns host` | Mantém o isolamento |
| Runtime com sandbox | `--runtime runsc` (gVisor) ou Kata Containers | Kernel intermediário ou microVM para código não confiável |

```bash
docker run -d --name api \
  --user 10001:10001 \
  --read-only --tmpfs /tmp:size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --pids-limit 200 --memory 512m --cpus 1 \
  ghcr.io/org/api@sha256:…
```

### Segredos

#### Onde (não) colocar segredos

| Local | Seguro? | Por quê |
|---|---|---|
| `ENV` ou `ARG` no Dockerfile | **Não** | Fica gravado na imagem e no histórico |
| Arquivo copiado para a imagem e apagado depois | **Não** | Continua na camada em que foi copiado |
| `-e SENHA=…` na execução | Fraco | Visível em `docker inspect`, no `/proc/<pid>/environ`, em dumps e logs de erro, e herdado por processos filhos |
| Build secret (`RUN --mount=type=secret`) | **Sim**, para o build | Não entra em camada nem no histórico |
| Compose/Swarm secrets em `/run/secrets` | **Sim**, para execução | Arquivo montado só no contêiner que precisa (no Swarm, cifrado no Raft e montado em tmpfs) |
| Cofre externo (Vault, AWS Secrets Manager, Azure Key Vault) | **Sim** | Rotação, auditoria e credenciais temporárias |

- Imagens enviadas por engano com segredos devem ser consideradas **comprometidas**: rotacione o segredo; apagar a tag não basta.
- Ferramentas como Docker Scout, Trivy e GitGuardian detectam segredos em camadas de imagens.

### Cadeia de suprimentos

#### Práticas e ferramentas

| Prática | Ferramentas | Observação |
|---|---|---|
| Imagens base mínimas e mantidas | Docker Official Images, **Docker Hardened Images**, distroless, Chainguard | Menos pacotes = menos CVEs e menos superfície |
| Fixar por digest e atualizar automaticamente | `FROM …@sha256:…`, Renovate, Dependabot | Reprodutível sem ficar parado no tempo |
| Escanear vulnerabilidades | **Docker Scout** (`docker scout quickview`, `docker scout cves`, `docker scout recommendations`), Trivy, Grype | Rode no CI e bloqueie severidades críticas com correção disponível |
| SBOM | `docker buildx build --sbom=true`, `docker scout sbom`, Syft | Saber o que existe em cada imagem quando surgir um novo CVE |
| Provenance (SLSA) | `--provenance=mode=max` | Liga a imagem ao commit e ao pipeline que a gerou |
| Assinatura | **Sigstore/cosign** (inclusive keyless, com OIDC do CI), **Notation** | O Docker Content Trust (Notary v1) foi aposentado |
| Verificar antes de executar | Políticas de admissão no Kubernetes (Kyverno, Sigstore policy-controller), políticas do Scout | Só roda imagem assinada, do registry permitido |
| Restringir registries | Registry Access Management (Docker Business), políticas do cluster | Evita imagens de origem desconhecida |
| Auditoria de configuração | CIS Docker Benchmark, `docker-bench-security` | Verifica daemon, host e contêineres |

- **Imagens de terceiros**: prefira oficiais ou de publicadores verificados; confira o repositório de origem (`org.opencontainers.image.source`), a frequência de atualização e o Dockerfile.
- **Atualização contínua**: reconstrua as imagens periodicamente (mesmo sem mudança no código) para incorporar correções da base.

### Decisão rápida — Segurança

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Aplicação precisa escutar na porta 80 sem root | `--cap-drop ALL --cap-add NET_BIND_SERVICE` (ou escutar em porta alta) | Rodar como root |
| Contêiner "precisa de permissão" para algo | Identificar a capability ou o dispositivo exato | `--privileged` |
| Ferramenta pede o `docker.sock` | Avaliar o risco; proxy de socket com endpoints mínimos | Montar o socket `:ro` achando que é seguro |
| Servidor compartilhado com vários usuários de Docker | Modo rootless | Grupo `docker` para todos |
| Impedir que um invasor altere binários | `--read-only` + tmpfs para diretórios temporários | Confiar só no usuário não root |
| Senha do banco na imagem | Secrets em tempo de execução ou cofre externo | `ENV DB_PASSWORD` |
| Token para baixar dependências no build | Build secret | `ARG` com o token |
| Segredo foi enviado em uma imagem pública | Rotacionar o segredo e reconstruir | Apagar a tag e seguir |
| Saber se as imagens em produção têm um CVE novo | SBOM + Docker Scout/Trivy no registry | Escanear só no build |
| Garantir que só imagens do pipeline rodem | Assinatura com cosign + verificação na admissão | Confiar na tag |
| Executar código não confiável de usuários | gVisor, Kata ou uma VM por carga | Contêiner padrão com `--cap-drop` |

---

## 10. Recursos, Logs, Observabilidade e Troubleshooting

> **Ideia central**: sem limites, um contêiner pode consumir **toda** a memória e CPU do host. Sem rotação, os logs enchem o disco. E sem logs em **STDOUT/STDERR**, `docker logs` e as ferramentas de coleta ficam cegas. Limites, rotação e saída padrão são a base da operação.

### Limites de recursos

#### Memória, CPU e outros

| Flag | Efeito | Observação |
|---|---|---|
| `--memory 512m` | Limite rígido de memória | Ao estourar, o kernel mata o processo (**OOM**, código **137**, `OOMKilled: true`) |
| `--memory-reservation 256m` | Limite flexível, aplicado quando o host está sob pressão | Deve ser menor que `--memory` |
| `--memory-swap` | Memória + swap. Igual a `--memory` = **sem swap**; `-1` = swap ilimitado | Sem definir, o contêiner pode usar swap igual ao limite de memória (se o host tiver swap) |
| `--oom-kill-disable` | Impede o OOM kill | **Perigoso sem `--memory`**: o host pode matar outros processos |
| `--cpus 1.5` | Até 1,5 CPU de tempo (cota do CFS) | Forma mais simples de limitar CPU |
| `--cpu-shares 512` | Peso **relativo** (padrão 1024), só vale quando há disputa | Não é um limite |
| `--cpuset-cpus 0,1` | Fixa o contêiner em núcleos específicos | Cargas sensíveis a latência |
| `--pids-limit 200` | Máximo de processos | Proteção contra fork bomb |
| `--shm-size 256m` | Tamanho do `/dev/shm` (padrão **64 MB**) | Navegadores headless e alguns bancos precisam de mais |
| `--ulimit nofile=65536:65536` | Limites do processo | Servidores com muitas conexões |
| `--gpus all` | Expõe GPUs NVIDIA | Exige o NVIDIA Container Toolkit no host |

- **Alterar sem recriar**: `docker update --memory 1g --cpus 2 <contêiner>` (também `docker container update`, disponível desde o Docker 1.10). Aceita CPU, memória, `--pids-limit`, `--blkio-weight` e `--restart`; `docker update --help` lista as opções.

#### Na prática: dimensionar e conferir limites
- **Sem limites, um contêiner pode usar todos os recursos do host** e prejudicar os vizinhos. Defina limites por tipo de serviço. Exemplo: servidores web com `--cpus 0.5 -m 128m` e bancos com `--cpus 1 -m 256m` (valores ilustrativos; meça o consumo real com `docker stats` antes de fixar).

```bash
docker run -d --name web --cpus 0.5 -m 128m nginx
docker inspect -f 'Memória: {{.HostConfig.Memory}} bytes | NanoCpus: {{.HostConfig.NanoCpus}}' web
# Memória: 134217728 bytes | NanoCpus: 500000000

docker update -m 256m --memory-swap 256m --cpus 1 web
docker stats --no-stream web
```

- Os valores aparecem no `inspect` em **bytes** (`Memory`) e em **bilionésimos de CPU** (`NanoCpus`: `0.5` CPU = `500000000`). `Memory: 0` e `NanoCpus: 0` significam **sem limite**.
- `-m` é a forma curta de `--memory` e aceita sufixos `b`, `k`, `m` e `g`. O mínimo é 6 MB.
- Ao **aumentar** `--memory` com `docker update` em um contêiner que já tem `--memory-swap`, ajuste os dois juntos: `--memory-swap` não pode ser menor que `--memory`.
- O campo `KernelMemory` (`--kernel-memory`) de saídas antigas foi descontinuado e não tem efeito com cgroup v2.

- **Runtimes precisam enxergar os limites**: a JVM (10+) respeita cgroups e dimensiona o heap com `-XX:MaxRAMPercentage`; o Node.js tem heap próprio (`--max-old-space-size`); o Go ajusta o `GOMAXPROCS` ao limite de CPU desde a versão 1.25. Aplicações antigas podem enxergar a memória do host inteiro e ser mortas por OOM.

### Logs

#### Drivers de log

| Driver | Destino | `docker logs` funciona? | Observação |
|---|---|---|---|
| `json-file` (padrão) | Arquivo JSON no host | Sim | **Sem rotação por padrão**: configure `max-size` e `max-file` |
| `local` | Arquivo em formato otimizado e comprimido | Sim | **Rotação por padrão** (20 MB × 5 arquivos). Recomendado para hosts de uso geral |
| `journald` | systemd journal | Sim | Integra com `journalctl` |
| `syslog`, `gelf`, `fluentd`, `splunk` | Servidor de logs remoto | Sim, pelo cache local (dual logging) | Envio direto a plataformas de log |
| `awslogs`, `gcplogs` | CloudWatch Logs, Cloud Logging | Sim, pelo cache local | Usados em ECS e VMs de nuvem |
| `none` | Nenhum | Não | Descarta a saída |

```bash
# Por contêiner
docker run --log-driver local --log-opt max-size=10m --log-opt max-file=3 app
# Global: log-driver e log-opts no daemon.json (vale para contêineres novos)
```

- **Aplicação deve escrever em STDOUT/STDERR**, não em arquivos dentro do contêiner. Imagens oficiais como a do nginx ligam `/var/log/nginx/access.log` a `/dev/stdout`.
- **Modo de entrega**: o padrão `mode=blocking` faz a aplicação **esperar** se o destino do log travar; `mode=non-blocking` com `max-buffer-size` evita isso, mas pode descartar mensagens quando o buffer enche.
- Logs estruturados (JSON) facilitam consultas no destino.

### Métricas e eventos

#### Fontes de informação
- **`docker stats`**: CPU, memória (uso e limite), rede, disco e PIDs em tempo real. `--no-stream` para uma leitura única (útil em scripts).
- **Métricas do daemon**: `"metrics-addr": "127.0.0.1:9323"` no `daemon.json` expõe métricas Prometheus do Engine.
- **cAdvisor**: exporta métricas por contêiner para Prometheus.
- **`docker events --filter event=die --filter event=oom`**: acompanha mortes, OOMs, mudanças de health e reinícios.
- **Healthcheck**: `docker inspect -f '{{json .State.Health}}' <c>` mostra as últimas execuções e suas saídas.
- **Rastreamento**: a aplicação instrumentada com OpenTelemetry envia traces a um coletor que roda como outro contêiner na mesma rede.

### Troubleshooting

#### Sintomas, causas e ações

| Sintoma / mensagem | Causa provável | O que fazer |
|---|---|---|
| `Cannot connect to the Docker daemon at unix:///var/run/docker.sock` | Daemon parado, contexto errado ou `DOCKER_HOST` apontando para outro lugar | `systemctl status docker`, `docker context ls`, `echo $DOCKER_HOST` |
| `permission denied while trying to connect to the Docker daemon socket` | Usuário sem acesso ao socket | Usar `sudo`, rootless ou (conscientemente) o grupo `docker` e novo login |
| `no space left on device` | Imagens, cache de build, volumes ou logs sem rotação | `docker system df`, prune seletivo, rotação de logs, `data-root` maior |
| Código **137** / `OOMKilled: true` | Memória acima do limite | Aumentar o limite, corrigir vazamento, ajustar heap do runtime |
| `exec format error` | Imagem de outra arquitetura | `--platform` correto ou imagem multiplataforma |
| `exec /entrypoint.sh: no such file or directory` com o arquivo presente | Finais de linha CRLF ou shebang para shell inexistente (`#!/bin/bash` no Alpine) | Converter para LF (`.gitattributes`), usar `#!/bin/sh` |
| `bind: address already in use` / `port is already allocated` | Porta do host ocupada | Outra porta no host ou parar o processo que a usa (`ss -ltnp`) |
| `toomanyrequests: You have reached your pull rate limit` | Limite do Docker Hub | Autenticar, mirror, cache de imagens |
| `manifest unknown` / `no matching manifest for linux/arm64` | Tag inexistente ou sem a plataforma pedida | Conferir a tag e as plataformas com `imagetools inspect` |
| `unauthorized` / `denied: requested access to the resource is denied` | Sem login, token expirado ou repositório errado | `docker login`, conferir o nome completo e as permissões |
| Contêiner em `Restarting` sem parar | Processo falha ao iniciar e a política reinicia | `docker logs`, `docker inspect`, rodar com `--entrypoint sh` |
| Contêiner saudável mas inacessível pela porta publicada | Aplicação escuta em `127.0.0.1` dentro do contêiner | Escutar em `0.0.0.0` |
| Resolução de nomes falha dentro do contêiner | DNS corporativo, VPN ou `resolv.conf` do host | `dns` no `daemon.json` ou `--dns` |
| Build não reflete a alteração | Cache de `RUN` com comando idêntico ou arquivo ignorado pelo `.dockerignore` | `--no-cache` pontual, revisar a ordem e o `.dockerignore` |
| Bind mounts lentos no macOS/Windows | Sincronização de arquivos entre o host e a VM | `develop.watch`, synchronized file shares, código dentro do WSL 2 |

#### Problemas de instalação e do daemon
Quando o daemon não sobe, a mensagem útil está no **log do serviço**, não na CLI. Sequência:

1. `systemctl status docker` mostra se o serviço falhou e as últimas linhas do log.
2. `journalctl -u docker --no-pager -n 100` (ou `-f`) mostra o erro completo.
3. `sudo dockerd --validate --config-file /etc/docker/daemon.json` valida a configuração sem subir o daemon.
4. Para ver a inicialização em detalhe: pare o serviço e rode `sudo dockerd --debug` em primeiro plano.

| Mensagem ou sintoma | Causa provável | Correção |
|---|---|---|
| `unable to configure the Docker daemon with file /etc/docker/daemon.json: … invalid character` | JSON inválido (vírgula sobrando, aspas) | Corrigir o arquivo; `dockerd --validate` ou `jq . daemon.json` |
| `the following directives are specified both as a flag and in the configuration file: hosts` | Mesma opção no `daemon.json` e na unit do systemd (`-H fd://`) | Tirar de um dos lugares; override com `systemctl edit docker` |
| `error initializing graphdriver` / `driver not supported` | Storage driver pedido não existe (ex.: `devicemapper` no Engine 25+) ou o sistema de arquivos não o suporta | Remover `storage-driver` ou escolher `overlay2`; conferir ext4 ou xfs com `ftype=1` |
| `Error initializing network controller` / erro de `iptables` | Módulos do kernel ausentes, conflito com nftables ou firewall | Carregar `br_netfilter`/`overlay`, conferir o backend de firewall, `journalctl` |
| `Conflicts: docker.io` / erro de pacote na instalação | Pacotes da distribuição (`docker.io`, `podman-docker`, `containerd`) conflitam com os oficiais | Remover os pacotes não oficiais antes de instalar |
| `docker: 'compose' is not a docker command` | Plugin não instalado | Instalar `docker-compose-plugin` (e `docker-buildx-plugin`) |
| `client version 1.43 is too old. Minimum supported API version is 1.44` | CLI antiga (Docker 24 ou anterior) contra o Engine 29 | Atualizar a CLI |
| Daemon sobe, mas `docker run` falha com erro de cgroup | cgroup v1 ou driver de cgroup divergente (`cgroupfs` vs. `systemd`) | `docker info` para ver `Cgroup Driver`/`Cgroup Version`; usar cgroup v2 com `systemd` |

- **Iniciar no boot**: `sudo systemctl enable --now docker containerd`. `systemctl is-enabled docker` confere.
- **Atualizar o Engine**: pelo gerenciador de pacotes (`apt install docker-ce=<versão> docker-ce-cli=<versão> containerd.io`). Com `live-restore`, os contêineres continuam rodando durante o restart do daemon (fora do Swarm). Em um Swarm, atualize um nó por vez (capítulo 11).

#### Números de operação

| Item | Valor |
|---|---|
| Tempo de tolerância do `docker stop` | **10 s** |
| Sinal de parada padrão | `SIGTERM` |
| Tamanho padrão do `/dev/shm` | **64 MB** |
| Peso padrão de `--cpu-shares` | **1024** |
| Rotação padrão do driver `local` | **20 MB × 5 arquivos** |
| Rotação padrão do `json-file` | **Nenhuma** |
| Healthcheck: intervalo / timeout / retries padrão | **30 s / 30 s / 3** |
| Atraso inicial da política de reinício | **100 ms**, dobrando a cada falha |
| Tempo mínimo em execução para a política de reinício valer | **10 s** |
| Porta padrão das métricas do daemon (convenção) | **9323** |

### Decisão rápida — Operação

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Disco do host cheio de logs | Driver `local` ou `max-size`/`max-file` no `daemon.json` | Apagar arquivos de log com o contêiner rodando |
| Um contêiner derruba os outros por memória | `--memory` em todos os serviços | `--oom-kill-disable` |
| Java morto por OOM com heap aparentemente pequeno | `-XX:MaxRAMPercentage` e limite coerente | Fixar `-Xmx` maior que o limite do contêiner |
| Coletar logs em uma plataforma central | Driver de log ou agente coletor lendo STDOUT | Logar em arquivo dentro do contêiner |
| Aplicação trava quando o servidor de logs cai | `mode=non-blocking` com buffer | Remover o driver de log |
| Saber quando contêineres morrem por OOM | `docker events --filter event=oom` ou métricas | Olhar `docker ps` de vez em quando |
| Navegador headless travando | `--shm-size` maior | Rodar com `--privileged` |
| Ajustar limites sem recriar o contêiner | `docker update` | Parar, remover e recriar |

---

## 11. Orquestração: Docker Swarm e o Caminho para Kubernetes

> **Ideia central**: o Docker Engine sozinho gerencia contêineres **em um host**. Quando é preciso **vários hosts**, alta disponibilidade, rolling updates e substituição automática de contêineres doentes, entra um **orquestrador**. O **Swarm mode** vem embutido no Engine e usa arquivos Compose; o **Kubernetes** é o padrão de mercado para ambientes maiores.

### Docker Swarm mode

#### Arquitetura
- **Managers**: mantêm o estado do cluster com o algoritmo de consenso **Raft**, agendam tarefas e atendem a API. Por padrão, também executam tarefas.
- **Workers**: executam as tarefas designadas pelos managers.
- **Serviço**: definição desejada (imagem, réplicas, portas, redes). **Tarefa**: cada contêiner que o Swarm cria para cumprir o serviço.
- Criar e entrar no cluster: `docker swarm init --advertise-addr <ip>` no primeiro manager; `docker swarm join-token worker` (ou `manager`) mostra o comando de entrada para os outros nós.
- O **Swarm clássico** (projeto separado, anterior a 2016) foi descontinuado; o que existe hoje é o **Swarm mode**, parte do Engine.

#### Criar e administrar o cluster
Cenário: três hosts Linux com Docker (`no1`, `no2`, `no3`), com as portas 2377/tcp, 7946/tcp e udp e 4789/udp liberadas entre eles.

```bash
# no1: cria o cluster e vira o primeiro manager (Leader)
docker swarm init --advertise-addr 10.0.0.11

# comandos de entrada (o token define o papel: worker ou manager)
docker swarm join-token worker
docker swarm join-token manager

# no2 e no3: entram no cluster com o comando mostrado
docker swarm join --token SWMTKN-1-… 10.0.0.11:2377

# em qualquer manager
docker node ls
docker node inspect no2 --pretty
docker node promote no2 no3     # workers viram managers (3 managers = tolera 1 falha)
docker node demote no3          # manager volta a ser worker
docker node update --availability drain no3
docker node update --label-add zona=a no2
```

| Coluna `MANAGER STATUS` em `docker node ls` | Significado |
|---|---|
| `Leader` | O manager que lidera o Raft no momento |
| `Reachable` | Manager saudável, participando do quórum |
| `Unreachable` | Manager que os outros não alcançam (conta como falha) |
| (vazio) | Worker |

- **Qualquer manager** aceita comandos de administração e encaminha o que for preciso ao líder. Não é preciso estar no `Leader`, e comandos de cluster **não funcionam em workers**.
- **Sair e remover um nó**: no próprio nó, `docker swarm leave` (manager precisa de `--force` e deve ser **rebaixado antes**, para não quebrar o quórum); depois, em um manager, `docker node rm <nó>` apaga o registro, que fica como `Down`.
- **Tokens**: quem tem o token de manager pode entrar como manager. Guarde-os como segredo e troque se vazarem: `docker swarm join-token --rotate worker`.

#### Quórum de managers

| Managers | Falhas toleradas | Quórum (maioria) |
|---|---|---|
| 1 | 0 | 1 |
| 3 | **1** | 2 |
| 5 | **2** | 3 |
| 7 | **3** | 4 |

- Fórmula: um cluster com **N** managers tolera **(N − 1) / 2** falhas. Use **número ímpar**: 4 managers toleram só 1 falha, como 3. Mais de 7 managers deixa o consenso lento sem ganho real.
- **Sem quórum**, as tarefas existentes continuam rodando, mas **não é possível alterar** o cluster (criar, atualizar ou reagendar serviços). Recuperação: `docker swarm init --force-new-cluster` em um manager sobrevivente.
- Distribua os managers em zonas de falha diferentes.
- **Dois managers não dão alta disponibilidade.** O quórum de 2 é 2: se um cair, o outro não consegue alterar o cluster. É pior que ter só um manager, porque dobra a chance de falha sem tolerar nenhuma. Um exemplo com "2 managers e 1 worker" deve ser lido como laboratório; em produção, use 3 managers.

#### Serviços, atualizações e stacks

```bash
docker service create --name web --replicas 3 -p 80:8080 \
  --update-parallelism 1 --update-delay 10s \
  --update-failure-action rollback --update-order start-first \
  ghcr.io/org/web:1.4.2

docker service scale web=5
docker service update --image ghcr.io/org/web:1.4.3 web
docker service rollback web
docker service ps web        # tarefas e histórico
docker service logs -f web
```

- **O que é um serviço**: a unidade que o Swarm mantém no estado desejado. Por padrão, recebe um **IP virtual (VIP)** na rede do serviço: conexões ao nome ou ao VIP são **balanceadas** entre as tarefas pelo IPVS do kernel. Com `--endpoint-mode dnsrr`, o DNS devolve os IPs das tarefas no lugar do VIP.
- `docker service ls` mostra as réplicas atuais/desejadas (`5/5`); `docker service ps web` mostra em que nó está cada tarefa e o histórico de falhas; `docker service inspect --pretty web` resume a configuração (inclusive `UpdateConfig`, `RestartPolicy` e o VIP em `Endpoint.VirtualIPs`); `docker service rm web` remove o serviço e as tarefas.
- **Agendamento**: o scheduler distribui as tarefas pela estratégia **spread**, considerando os nós elegíveis (constraints, recursos **reservados**, plataforma) e quantas tarefas cada um já tem. Ele **não mede a carga real** (CPU em uso) dos nós. Para reservar capacidade, use `--reserve-cpu` e `--reserve-memory`.
- **Volumes em serviços**: `--mount type=volume,src=dados,dst=/app` cria um volume **`local` em cada nó** onde uma tarefa roda. **Não é o mesmo volume compartilhado entre os nós**: réplicas em nós diferentes enxergam dados diferentes, e uma tarefa reagendada em outro nó começa com um volume vazio. Para dados compartilhados, use um driver de volume de rede (NFS, plugin de storage) ou um serviço de dados externo (banco, storage de objetos), ou fixe o serviço em um nó com constraint.

| Conceito | Detalhe |
|---|---|
| Modo **replicated** | Número fixo de réplicas distribuídas entre os nós |
| Modo **global** | Exatamente uma tarefa por nó elegível (agentes de monitoramento, coletores de log) |
| **Rolling update** | `parallelism` (quantas por vez), `delay`, `failure_action` (`pause` é o padrão; `continue` ou `rollback`), `order` (`stop-first` padrão ou `start-first`) |
| **Placement** | `--constraint node.role==worker`, `node.labels.zona==a`; `--placement-pref spread=node.labels.zona` |
| **Disponibilidade do nó** | `active`, `pause` (não recebe tarefas novas), `drain` (tarefas são movidas para outros nós; usado em manutenção) |
| **Stack** | `docker stack deploy -c compose.yaml loja` implanta um arquivo Compose no Swarm usando a seção `deploy` |

- Em stacks, `build:` é **ignorado**: as imagens precisam existir em um registry acessível por todos os nós.
- **Routing mesh**: uma porta publicada por um serviço fica disponível em **todos os nós** do cluster (rede `ingress`), que encaminham para uma tarefa saudável. Com `mode: host`, a porta é publicada só no nó onde a tarefa roda.
- **Secrets e configs do Swarm**: guardados **cifrados no log do Raft**, entregues só aos serviços autorizados e montados em **tmpfs** em `/run/secrets/<nome>`. São imutáveis: para rotacionar, crie um novo segredo e atualize o serviço.
- **Autolock** (`docker swarm update --autolock=true`): as chaves do Raft passam a ser protegidas por uma chave que precisa ser informada (`docker swarm unlock`) quando um manager reinicia.
- **Healthcheck no Swarm**: tarefas `unhealthy` são **substituídas** automaticamente.

#### Publicação de portas: modo `ingress` vs. modo `host`
A forma longa do `--publish` deixa explícito o modo:

```bash
# ingress (padrão): routing mesh, porta aberta em TODOS os nós
docker service create --name web --replicas 3 \
  --publish published=8080,target=80 nginx:1.29

# host: porta aberta só nos nós que rodam uma tarefa, sem routing mesh
docker service create --name coletor --mode global \
  --publish published=514,target=514,protocol=udp,mode=host coletor:1.0

docker service update --publish-add published=8443,target=443 web
docker service update --publish-rm 8080 web
```

| Aspecto | `mode=ingress` (padrão) | `mode=host` |
|---|---|---|
| Onde a porta abre | Em **todos os nós** do cluster | Só no nó onde a tarefa roda |
| Balanceamento | Pelo routing mesh (IPVS), entre todas as tarefas | Nenhum: o cliente fala com a tarefa daquele nó |
| IP de origem do cliente | Perdido (a aplicação vê um IP da rede `ingress`) | **Preservado** |
| Limite de tarefas por nó | Nenhum | **Uma** tarefa por nó para cada porta publicada; uma segunda réplica no mesmo nó fica `Pending` |
| Uso típico | Serviços web atrás de um load balancer externo que aponta para todos os nós | Serviços `global`, coletores UDP, quando o IP do cliente importa |

- **Descobrir onde o serviço está acessível**: `docker service inspect --format '{{json .Endpoint.Ports}}' web` mostra `PublishedPort`, `TargetPort` e `PublishMode`. Para um contêiner avulso, `docker port <c>` e `docker inspect -f '{{json .NetworkSettings.Ports}}' <c>`.

#### Templates em `docker service create`
Algumas flags aceitam **templates Go** que são resolvidos **por tarefa**. As flags suportadas são **`--hostname`, `--mount` e `--env`**.

| Placeholder | Valor |
|---|---|
| `{{.Service.ID}}`, `{{.Service.Name}}`, `{{.Service.Labels}}` | ID, nome e rótulos do serviço |
| `{{.Node.ID}}`, `{{.Node.Hostname}}` | ID e hostname do nó onde a tarefa roda |
| `{{.Task.ID}}`, `{{.Task.Name}}`, `{{.Task.Slot}}` | ID, nome e número da réplica (slot) da tarefa |

```bash
docker service create --name api --replicas 3 \
  --hostname '{{.Node.Hostname}}-{{.Service.Name}}' \
  --env TASK_SLOT='{{.Task.Slot}}' \
  --mount 'type=volume,src=dados-{{.Task.Slot}},dst=/data' \
  app:1.0

docker inspect -f '{{.Config.Hostname}}' $(docker ps -q -f name=api)   # confere o resultado
```

- Use aspas simples para o shell não interpretar as chaves. O `{{.Task.Slot}}` dá a cada réplica um volume próprio (`dados-1`, `dados-2`, `dados-3`).

#### Modos de serviço e limites de posicionamento

| Modo (`--mode`) | Comportamento |
|---|---|
| `replicated` (padrão) | Mantém `--replicas N` tarefas rodando |
| `global` | Uma tarefa em cada nó elegível, inclusive nos que entrarem depois |
| `replicated-job` | Roda até completar; `--replicas` define quantas execuções concorrentes e `--max-concurrent` o paralelismo |
| `global-job` | Roda até completar, uma vez em cada nó (ex.: limpeza de disco em todos os nós) |

- **`--replicas-max-per-node 1`**: no máximo uma réplica por nó (tarefas excedentes ficam `Pending`).
- **Constraints** (`--constraint`) aceitam `node.id`, `node.hostname`, `node.role`, `node.platform.os`, `node.platform.arch`, `node.labels.<chave>` e `engine.labels.<chave>`, com `==` e `!=`. Vários constraints são combinados com **E**.
- **Rótulos de nó** (`docker node update --label-add`) são definidos pelo administrador no cluster; **rótulos do Engine** (`labels` no `daemon.json`) são definidos em cada host. Para posicionamento, prefira os de nó: um nó comprometido pode alterar os próprios rótulos do Engine.
- **Rebalancear** depois que um nó volta: o Swarm **não** move tarefas sozinho; `docker service update --force web` redistribui (reiniciando as tarefas).

#### Serviço que não sobe: diagnóstico

```bash
docker service ls                                  # REPLICAS 0/3?
docker service ps web --no-trunc                   # ERROR com a mensagem completa
docker service ps web --filter desired-state=running
docker service inspect --pretty web                # constraints, portas, recursos
docker service logs web                            # saída da aplicação
docker node ls                                     # nós Ready e Active?
docker inspect <id-da-tarefa>                      # Status.Err e Status.State
```

| Estado ou erro em `docker service ps` | Causa provável | O que fazer |
|---|---|---|
| `Pending` com `no suitable node (scheduling constraints not satisfied …)` | Constraint que nenhum nó atende (rótulo inexistente, papel errado) | Conferir `docker node inspect` e os rótulos |
| `Pending` com `insufficient resources on N nodes` | `--reserve-memory`/`--reserve-cpu` maior que o livre nos nós | Reduzir a reserva ou adicionar nós |
| `Pending` com porta em uso | `mode=host` com mais réplicas que nós | Usar `ingress`, `global` ou `--replicas-max-per-node 1` |
| `Rejected` com `No such image` | Imagem inexistente, só local ou em registry privado sem credencial | Enviar a um registry; criar ou atualizar com **`--with-registry-auth`** |
| `Failed` com código de saída, reiniciando em loop | A aplicação falha ao iniciar | `docker service logs`, conferir env, secrets e comando |
| `Rejected` com secret, config ou rede inexistente | Referência a um objeto que não existe | Criar o objeto antes do serviço |
| Todas as tarefas em um só nó | Os outros nós estão em `drain` ou `pause` | `docker node update --availability active` |

- Nós `Down` em `docker node ls` não recebem tarefas; confira a rede entre os nós (portas 2377, 7946 e 4789) e o daemon do nó.

### Segurança, backup e manutenção do Swarm

#### Segurança padrão do Swarm
O Swarm vem seguro por padrão, sem configuração extra:

| Mecanismo | Como funciona |
|---|---|
| **CA embutida** | O primeiro manager cria uma **CA raiz** e emite um certificado para cada nó que entra. A identidade e o papel do nó (manager ou worker) estão no certificado |
| **TLS mútuo (mTLS)** | Toda comunicação entre os nós é **autenticada, autorizada e cifrada** com os certificados de ambos os lados |
| **Rotação automática** | Cada nó renova o próprio certificado a cada **3 meses (90 dias)** por padrão. Ajuste: `docker swarm update --cert-expiry 720h` |
| **Tokens de entrada** | `SWMTKN-1-<digest da CA raiz>-<segredo>`: o nó que entra confere a CA pelo digest, e o segredo define o papel. Há um token para workers e outro para managers |
| **Raft cifrado** | O log do Raft (estado do cluster, secrets, configs) é **cifrado em repouso** nos managers |
| **Autolock** | Protege as chaves de criptografia do Raft com uma chave que precisa ser informada após o restart de um manager |
| **Secrets** | Entregues só aos nós que executam tarefas autorizadas a usá-los, em tmpfs |
| **Tráfego da overlay** | Controle (gerenciamento e gossip) **cifrado**; dados dos contêineres **não cifrados** por padrão (`--opt encrypted` liga IPsec) |

```bash
docker swarm ca --rotate                         # nova CA raiz; os nós recebem certificados novos
docker swarm ca --rotate --external-ca protocol=cfssl,url=https://ca.exemplo.com
docker swarm init --external-ca protocol=cfssl,url=https://ca.exemplo.com   # CA própria desde o início
docker swarm join-token --rotate manager         # invalida o token antigo de manager
docker swarm update --autolock=true              # mostra a chave de desbloqueio
docker swarm unlock-key                          # mostra a chave atual (em um manager desbloqueado)
docker swarm unlock-key --rotate
```

- **Rotação da CA**: o Docker cria um certificado intermediário com assinatura cruzada entre a CA antiga e a nova, e os nós renovam os certificados sem perder a comunicação. Depois da rotação, **os tokens de entrada antigos deixam de valer** (eles contêm o digest da CA).
- **Token vazado**: `docker swarm join-token --rotate` resolve para quem ainda não entrou; nós que já entraram com o token precisam ser removidos com `docker node rm`.
- **Workers** não guardam o estado do cluster nem aceitam comandos de administração.

#### Backup e restauração do Swarm
O estado do cluster (Raft, serviços, secrets, configs, chaves de criptografia) fica em **`/var/lib/docker/swarm/`** em cada manager.

```bash
# Backup, em um manager que não seja o único (o cluster continua com quórum)
docker swarm unlock-key -q > unlock-key.txt      # se o autolock estiver ligado
sudo systemctl stop docker
sudo tar czf swarm-backup-$(date +%F).tgz -C /var/lib/docker swarm
sudo systemctl start docker

# Restauração em um host novo (mesma versão do Engine)
sudo systemctl stop docker
sudo rm -rf /var/lib/docker/swarm
sudo tar xzf swarm-backup-2026-09-30.tgz -C /var/lib/docker
sudo systemctl start docker
docker swarm unlock                              # se havia autolock
docker swarm init --force-new-cluster            # novo cluster de um manager com o estado restaurado
docker node promote …                            # voltar a ter 3 ou 5 managers
```

- **Pare o Docker antes de copiar**: com o daemon rodando, o Raft pode mudar durante a cópia. Por isso o backup é feito em um manager **não essencial ao quórum**.
- O backup **não inclui** dados dos volumes nem as imagens; faça backup dos volumes separadamente e mantenha as imagens em um registry.
- As chaves de criptografia e de desbloqueio **continuam as mesmas** do cluster original: guarde a chave de desbloqueio junto (e separada) do backup.
- `--force-new-cluster` também é o caminho quando o cluster **perde o quórum**: o manager mantém serviços, tarefas e workers, e os managers antigos precisam entrar de novo.
- Use um **IP fixo** no `--advertise-addr` dos managers: um IP que muda no reboot deixa o cluster instável.

#### Atualizar o Engine e fazer manutenção nos nós
1. `docker node update --availability drain <nó>`: as tarefas vão para outros nós.
2. Atualize o Engine pelo gerenciador de pacotes e reinicie o daemon.
3. `docker node update --availability active <nó>`, e confirme em `docker node ls` que ele voltou como `Ready`.
4. Repita **um nó por vez**. Managers primeiro, **um de cada vez**, esperando cada um voltar como `Reachable`, para nunca perder o quórum.

- Versões diferentes do Engine convivem no cluster durante a atualização, mas não por muito tempo.
- `live-restore` **não funciona** em nós do Swarm: reiniciar o daemon reinicia as tarefas daquele nó.
- **Promover um worker a manager** exige atenção: mais managers aumentam a tolerância, mas cada um participa do consenso. Workers dedicados rodam as aplicações; em clusters maiores, managers com `drain` só cuidam do cluster.

### Secrets e configs do Swarm

#### Comandos e uso
- **Docker secrets** (desde o Docker 1.13) guardam senhas, chaves e certificados de forma segura em clusters Swarm. Cada secret tem até **500 KB**.

| Comando | O que faz |
|---|---|
| `printf 'minha-senha' \| docker secret create db_pass -` | Cria a partir do STDIN (o `-` final). `printf` evita a quebra de linha que o `echo` acrescenta |
| `docker secret create tls_key ./chave.pem` | Cria a partir de um arquivo |
| `docker secret ls` | Lista (nome, datas) |
| `docker secret inspect db_pass` | Mostra metadados, **nunca o conteúdo** |
| `docker secret rm db_pass` | Remove (falha se algum serviço ainda usa) |

```bash
docker service create --name app \
  --secret source=db_pass,target=password,uid=10001,gid=10001,mode=0400 \
  minha-org/app:1.0
# dentro de cada tarefa: arquivo /run/secrets/password (tmpfs), dono 10001, modo 0400
```

- A aplicação **lê o arquivo** (`open('/run/secrets/password').read().strip()` em Python). Muitas imagens oficiais aceitam variáveis `*_FILE` apontando para ele.
- **Rotação** (secrets são imutáveis): crie uma nova versão, troque no serviço e remova a antiga.

```bash
printf 'nova-senha' | docker secret create db_pass_v2 -
docker service update --secret-rm db_pass \
  --secret-add source=db_pass_v2,target=password app
docker secret rm db_pass
```

- O `update` recria as tarefas (rolling update). Mantenha o mesmo `target` para a aplicação não precisar mudar o caminho. Trocar a senha também no banco é outra etapa, que precisa ser coordenada.
- **Configs** (`docker config create/ls/inspect/rm`, `--config source=…,target=…`) funcionam igual, para arquivos de configuração **não sensíveis** (o conteúdo aparece no `inspect`).
- **Fora do Swarm**: o Docker Compose também tem `secrets` (capítulo 8), mas lá são arquivos do host montados no contêiner, **sem** a criptografia do Raft.

### Stacks: arquivos Compose no Swarm

#### `docker stack` na prática
- **`docker compose`** executa um arquivo Compose em **um host**. **`docker stack deploy`** implanta o mesmo formato de arquivo em um **cluster Swarm**, transformando cada serviço em um serviço do Swarm. São ferramentas diferentes para o mesmo formato. O `docker stack` já vem com o Docker, e o Compose também, como plugin (`docker compose`).

```yaml
# stack.yaml (sem "version:", que é obsoleto)
services:
  web:
    image: nginx:1.29
    ports:
      - "8080:80"
    networks: [webnet]
    deploy:
      replicas: 5
      resources:
        limits: { cpus: "0.10", memory: 50M }
      restart_policy:
        condition: on-failure
        delay: 10s
        max_attempts: 3
        window: 120s
      update_config:
        parallelism: 2
        delay: 10s
        failure_action: rollback
        order: start-first
      placement:
        constraints: [node.role == worker]

networks:
  webnet:
    driver: overlay
```

```bash
docker stack deploy -c stack.yaml primeiro     # cria (e, rodando de novo, atualiza)
docker stack ls                                 # stacks e número de serviços
docker stack services primeiro                  # serviços do stack
docker stack ps primeiro                        # tarefas e nós
docker service logs -f primeiro_web
docker stack rm primeiro                        # remove serviços e redes (volumes ficam)
```

| Chave em `deploy` | Significado |
|---|---|
| `mode` | `replicated` (com `replicas`) ou `global` (uma tarefa por nó) |
| `replicas` | Número de tarefas |
| `resources.limits` / `reservations` | Limite e reserva de CPU e memória |
| `restart_policy` | `condition` (`none`, `on-failure`, `any`), `delay`, `max_attempts`, `window` (tempo para considerar que o reinício deu certo) |
| `update_config` / `rollback_config` | `parallelism`, `delay`, `failure_action`, `monitor`, `order` |
| `placement` | `constraints` (ex.: `node.role == manager`, `node.labels.zona == a`) e `preferences` |
| `labels` | Rótulos do **serviço** (os do contêiner ficam fora de `deploy`) |

- **Atualizar um stack** é rodar o mesmo `docker stack deploy`: o Swarm compara o estado e faz rolling update só no que mudou; serviços novos são criados. Serviços removidos do arquivo só saem com `--prune`.
- **Nomes**: serviços e redes ganham o prefixo do stack (`primeiro_web`, `primeiro_webnet`); sem `networks`, é criada a rede `<stack>_default`.
- **Ignorado ou diferente no stack**: `build` (use imagens de registry), `depends_on` (não há ordem de início: a aplicação deve tolerar dependências indisponíveis), `container_name`, `restart` (use `deploy.restart_policy`) e bind mounts relativos (o caminho precisa existir em **cada** nó).
- **YAML é sensível à indentação**: chaves de `deploy` fora do nível certo (`resources` alinhado com `deploy`, por exemplo) são ignoradas ou geram erro. Valide com `docker compose -f stack.yaml config` antes do deploy.
- **Senhas**: exemplos didáticos colocam senhas em `environment`. Em stacks, use `secrets` externos (`docker secret create`) com `external: true` e as variáveis `*_FILE` das imagens.
- **Cuidado com o `docker.sock`**: serviços de visualização e monitoramento (visualizer, cAdvisor, Portainer) costumam montar o socket e são restritos a managers com `constraints`. Isso dá a eles controle total do cluster; publique essas portas só em redes administrativas.
- **Imagens dos exemplos**: tutoriais antigos usam `mysql:5.7`, `postgres:9.4`, `mongo:3.2` e `google/cadvisor`, todas fora de suporte ou movidas (o cAdvisor hoje é `gcr.io/cadvisor/cadvisor`). Use versões mantidas e fixadas.

#### Exemplo de stack de monitoramento
Um stack clássico para observar o cluster e os hosts combina:

| Serviço | Papel | Modo típico |
|---|---|---|
| **Prometheus** | Coleta e guarda as métricas | `replicated`, 1 réplica, fixado em um nó com volume |
| **node-exporter** | Métricas do host (CPU, memória, disco, rede) | **`global`**: um por nó |
| **cAdvisor** | Métricas por contêiner | **`global`**: um por nó (monta `/`, `/sys`, `/var/lib/docker` e o socket, somente leitura) |
| **Alertmanager** | Agrupa e envia alertas (e-mail, Slack, Rocket.Chat, Teams) | `replicated` |
| **Grafana** | Dashboards sobre o Prometheus | `replicated`, com volume para dados |

- O modo `global` garante coletores em **todos os nós**, inclusive nos que entrarem depois. Nesses serviços, `hostname: "{{.Node.ID}}"` usa **templates do Swarm** para identificar o nó nas métricas.

### Do Docker ao Kubernetes

#### Equivalências

| Docker / Compose | Kubernetes |
|---|---|
| Contêiner | Contêiner dentro de um **Pod** |
| Serviço do Compose com réplicas | **Deployment** (ou StatefulSet para dados, DaemonSet para um por nó) |
| Nome do serviço na rede do Compose | **Service** (DNS interno, IP virtual) |
| `ports` publicadas | Service `NodePort`/`LoadBalancer`, **Ingress** ou Gateway API |
| Volume nomeado | **PersistentVolumeClaim** |
| `secrets` / `configs` | **Secret** / **ConfigMap** |
| `HEALTHCHECK` / `healthcheck` | **livenessProbe**, **readinessProbe** e **startupProbe** (o `HEALTHCHECK` da imagem é ignorado) |
| `deploy.resources.limits` | `resources.requests` e `resources.limits` |
| `depends_on` | Sem equivalente direto: **initContainers**, readiness probes e tolerância a falhas na aplicação |
| `restart: always` | Deployment + `restartPolicy: Always` |
| Rede definida pelo usuário | Namespace + **NetworkPolicy** |
| `docker stack deploy` | `kubectl apply`, Helm, Kustomize, GitOps (Argo CD, Flux) |

- **Kubernetes não usa o Docker Engine** como runtime desde a versão 1.24 (usa containerd ou CRI-O diretamente), mas **roda as mesmas imagens OCI**. Nada muda no Dockerfile.
- **Ferramentas de transição**: `kompose` converte arquivos Compose em manifests (ponto de partida, não resultado final); Kubernetes do Docker Desktop, **kind**, **k3d** e **minikube** para clusters locais.

#### Qual plataforma escolher

| Cenário | Opção adequada |
|---|---|
| Uma aplicação pequena em um servidor | Docker Engine + Compose |
| Poucos hosts, time pequeno, sem experiência em Kubernetes | Swarm mode |
| Muitas equipes, ecossistema, autoescalonamento, políticas | Kubernetes gerenciado (EKS, GKE, AKS) |
| Não quer operar servidores nem cluster | Contêineres serverless: AWS ECS com Fargate, Google Cloud Run, Azure Container Apps |
| Jobs de build e teste | Runners de CI com Docker ou builders remotos |

### Decisão rápida — Orquestração

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Swarm que sobreviva à perda de um manager | 3 managers (ou 5 para tolerar 2 falhas) | 2 managers (não toleram nenhuma falha) |
| Senha de banco em um stack do Swarm | `docker secret create` + `secrets` no stack + variáveis `*_FILE` | Senha em `environment` |
| Trocar a senha usada por um serviço | Novo secret + `docker service update --secret-rm/--secret-add` | Tentar editar o secret existente |
| Dados de uma réplica precisam sobreviver à troca de nó | Volume com driver de rede ou serviço de dados externo | Volume `local` achando que é compartilhado |
| Coletor de métricas em todos os nós | Serviço `global` (node-exporter, cAdvisor) | Uma réplica por nó contada à mão |
| Manutenção de um nó sem derrubar serviços | `docker node update --availability drain` | Desligar o nó direto |
| Um agente de monitoramento em cada nó | Serviço em modo `global` | Réplicas iguais ao número de nós |
| Atualização sem indisponibilidade e com volta automática | `update_config` com `order: start-first` e `failure_action: rollback` | Remover e recriar o serviço |
| Segredo compartilhado no cluster | `docker secret create` + referência no serviço | Variável de ambiente no stack |
| Stack não encontra a imagem nos workers | Enviar a imagem a um registry acessível | Construir em cada nó |
| Migrar um Compose para Kubernetes | `kompose` como ponto de partida + revisão (probes, recursos, Ingress) | Esperar que `depends_on` e o `HEALTHCHECK` funcionem iguais |
| Aplicação com tráfego variável sem operar cluster | Cloud Run, ECS Fargate ou Container Apps | Swarm em VMs superdimensionadas |

---

## 12. Docker em Produção e CI/CD

> **Ideia central**: em produção, a imagem é um **artefato imutável** construído **uma vez** pelo pipeline, testado, escaneado, assinado e promovido pelo **digest** entre ambientes. O que muda de um ambiente para outro é a **configuração**, injetada em tempo de execução.

### Pipeline de imagens

#### Etapas de um pipeline

1. **Lint**: `hadolint Dockerfile` e `docker build --check`.
2. **Build** com Buildx e cache exportado (`type=gha` ou `type=registry`), multiplataforma se necessário.
3. **Testes** dentro do contêiner: unitários no estágio `test` (`--target test`) e de integração com `docker compose up --wait` ou **Testcontainers**.
4. **Scan** de vulnerabilidades e segredos (Docker Scout, Trivy), com **política de bloqueio** (ex.: falhar com CVE crítico que tenha correção).
5. **SBOM e provenance** anexados à imagem.
6. **Push** com tags imutáveis (SHA do commit, versão semântica) e tags de conveniência.
7. **Assinatura** (cosign keyless com a identidade OIDC do CI).
8. **Deploy pelo digest** em homologação; depois, **promoção** do mesmo digest para produção.

#### Exemplo com GitHub Actions

```yaml
name: imagem
on:
  push:
    branches: [main]
    tags: ["v*"]

permissions:
  contents: read
  packages: write
  id-token: write      # assinatura keyless com cosign

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: docker/setup-qemu-action@v4
      - uses: docker/setup-buildx-action@v4
      - uses: docker/login-action@v4
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - id: meta
        uses: docker/metadata-action@v6
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=sha
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=ref,event=branch
      - id: build
        uses: docker/build-push-action@v7
        with:
          platforms: linux/amd64,linux/arm64
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          sbom: true
          provenance: mode=max
```

- A saída `steps.build.outputs.digest` traz o digest da imagem, que deve ser usado nos passos de assinatura e de deploy.
- Versões das actions conferidas em setembro de 2026.

#### Docker dentro do CI

| Abordagem | Como funciona | Riscos e cuidados |
|---|---|---|
| **Runner com Docker nativo** | O job usa o daemon da VM do runner (ex.: GitHub-hosted runners) | Simples; a VM é descartada ao fim do job |
| **Docker-in-Docker** (`docker:dind`) | Um daemon separado roda em um contêiner **privilegiado** | Exige `--privileged`; sem cache persistente a menos que configurado |
| **Socket do host** (Docker-out-of-Docker) | O job monta o `docker.sock` do host | O job ganha **root no host** e vê os contêineres de outros jobs |
| **BuildKit rootless ou builder remoto** | Build sem daemon privilegiado (`moby/buildkit:rootless`, driver `kubernetes`, Docker Build Cloud) | Opção mais segura em clusters compartilhados |

- O **Kaniko**, alternativa popular para builds sem daemon no Kubernetes, foi **arquivado pelo Google em 2025**; prefira BuildKit rootless ou builders remotos em projetos novos.

### Checklist de produção

#### Imagem
- Base mínima, mantida e fixada por digest; multi-stage; sem ferramentas de build no runtime.
- Usuário não root; sem segredos; `.dockerignore` completo.
- Scan sem vulnerabilidades críticas conhecidas com correção disponível; SBOM e provenance; assinatura.
- Rótulos OCI (`source`, `revision`, `version`).

#### Execução
- Configuração por variáveis de ambiente e segredos por arquivo ou cofre (princípios **12-factor**).
- **Limites** de memória, CPU e PIDs em todos os contêineres.
- **Healthcheck** (ou probes no Kubernetes) e política de reinício.
- **Parada graciosa**: tratar `SIGTERM`, forma exec, `stop_grace_period` coerente com o tempo de encerramento.
- Sistema de arquivos **somente leitura**, `--cap-drop ALL`, `no-new-privileges`.
- Portas publicadas apenas onde necessário, atrás de proxy reverso com TLS.

#### Host e operação
- Engine atualizado; `live-restore`; rotação de logs; monitoramento de disco.
- Daemon acessível só por SSH ou TLS mútuo; ninguém no grupo `docker` sem necessidade.
- Coleta centralizada de logs e métricas; alertas para OOM, reinícios e healthchecks.
- Backups de volumes testados (restauração, não só cópia).
- Limpeza periódica de imagens e cache de build.

### Ecossistema e alternativas

#### Ferramentas compatíveis

| Ferramenta | O que é |
|---|---|
| **Podman** | Motor de contêineres sem daemon, rootless por padrão, com CLI compatível com a do Docker e suporte a pods |
| **containerd + nerdctl** | Runtime do Kubernetes com uma CLI compatível com o Docker |
| **Colima**, **Rancher Desktop**, **OrbStack** | Alternativas ao Docker Desktop que rodam uma VM Linux com um Engine ou containerd |
| **Testcontainers** | Bibliotecas que sobem dependências reais (bancos, filas) em contêineres durante os testes |
| **Dev Containers** | Ambiente de desenvolvimento completo definido em `devcontainer.json`, usado pelo VS Code e pelo GitHub Codespaces |

- Como todos seguem as especificações **OCI**, imagens e Dockerfiles funcionam entre essas ferramentas com poucas ou nenhuma mudança.

### Decisão rápida — Produção e CI/CD

| Situação | Abordagem recomendada | Erro comum |
|---|---|---|
| Mesma imagem em homologação e produção | Construir uma vez e promover o digest | Rebuildar por ambiente |
| Configuração diferente por ambiente | Variáveis de ambiente, arquivos de configuração e segredos na execução | Uma imagem por ambiente |
| Build de imagens em Kubernetes compartilhado | BuildKit rootless ou builder remoto | Montar o socket do host no pod |
| Testes de integração com banco real | Testcontainers ou `docker compose up --wait` no CI | Mocks de tudo ou banco compartilhado |
| Bloquear imagens vulneráveis | Scan no pipeline com política de falha | Relatório que ninguém lê |
| Rastrear qual commit gerou a imagem em produção | Tag por SHA + provenance + rótulos OCI | Tag `latest` |
| Empresa grande sem licença do Docker Desktop | Assinatura paga ou alternativa (Colima, Rancher Desktop, Podman) | Ignorar a licença |
| Parada sem perder requisições em andamento | Tratar `SIGTERM`, drenar conexões, `stop_grace_period` | `SIGKILL` depois de 10 s |

---

## 13. Preparação para o DCA (Docker Certified Associate)

> **Ideia central**: o DCA cobra o Docker que está nos capítulos 1 a 12 **e** alguns assuntos que já saíram da prática: os produtos do antigo **Docker Enterprise** (UCP e DTR, hoje **MKE** e **MSR**, da Mirantis), o **Docker Content Trust** e o **devicemapper**. Este capítulo liga cada objetivo do roteiro oficial ao ponto do guia que o cobre, explica os tópicos legados no nível da prova e resume o Kubernetes que a prova pede.

### A prova

#### Formato

| Item | Valor (conferido em set/2026) |
|---|---|
| Quem aplica | **Mirantis**, que comprou o Docker Enterprise em 2019 |
| Questões | **55**: 13 de múltipla escolha tradicional e **42 no formato DOMC** |
| Duração | **90 minutos** |
| Preço | US$ 199 (ou € 200) |
| Aplicação | Online, com fiscal remoto, no seu computador Windows ou Mac; em inglês |
| Nota de aprovação | **Não divulgada** (pode mudar sem aviso) |
| Validade | **2 anos** |
| Experiência recomendada | 6 a 12 meses de uso de Docker |
| Roteiro oficial | *Docker Certification Study Guide*, versão 1.5 |

| Domínio | Peso |
|---|---|
| 1. Orquestração | **25%** |
| 2. Criação, gerenciamento e registry de imagens | **20%** |
| 3. Instalação e configuração | **15%** |
| 4. Redes | **15%** |
| 5. Segurança | **15%** |
| 6. Armazenamento e volumes | **10%** |

#### Como funciona o DOMC
No **Discrete Option Multiple Choice**, as alternativas aparecem **uma de cada vez** e você responde **SIM** ou **NÃO** para cada uma, sem poder voltar. A questão termina quando você acerta o que ela pede ou erra uma alternativa; você não sabe quantas alternativas ainda viriam.

- **Leia o enunciado inteiro** antes da primeira alternativa: ele não vai mudar, e a pergunta costuma ter um detalhe decisivo ("em um Swarm", "sem downtime", "com o menor privilégio").
- **Julgue cada alternativa sozinha**, como verdadeira ou falsa para aquele enunciado. Não espere uma "melhor" que talvez nunca apareça.
- Alternativas **quase certas** são o ponto fraco do formato: um comando com a flag errada (`docker service scale web 5` no lugar de `web=5`) ou um valor trocado (porta 2376 vs. 2377) é **NÃO**.
- Conheça **sintaxes exatas**: a prova testa flags, nomes de campos de `inspect` e a ordem dos argumentos.

### Roteiro oficial e onde estudar

#### Domínio 1 — Orquestração (25%)

| Objetivo | Onde está |
|---|---|
| Montar um Swarm com managers e workers | Cap. 11, "Criar e administrar o cluster" |
| Transformar instruções de um contêiner em serviço | Cap. 11, "Serviços, atualizações e stacks" |
| Importância do quórum | Cap. 11, "Quórum de managers" |
| Diferença entre contêiner e serviço | Cap. 11, "Serviços, atualizações e stacks" |
| Interpretar a saída de `docker inspect` | Cap. 3, "Filtros e formatação" |
| Converter uma aplicação em stack (`docker stack deploy`) e alterar um stack em execução | Cap. 11, "`docker stack` na prática" |
| Aumentar réplicas, adicionar redes, publicar portas, montar volumes | Cap. 11, "Serviços, atualizações e stacks" e "Publicação de portas" |
| Serviços replicated e global | Cap. 11, "Modos de serviço e limites de posicionamento" |
| Rótulos de nó para posicionar tarefas | Cap. 11, "Modos de serviço e limites de posicionamento" |
| Templates com `docker service create` | Cap. 11, "Templates em `docker service create`" |
| Diagnosticar um serviço que não sobe | Cap. 11, "Serviço que não sobe: diagnóstico" |
| Como uma aplicação em contêiner fala com sistemas legados | Cap. 6, "Integração com sistemas legados" |
| Kubernetes: Pods e Deployments; ConfigMaps e Secrets | Este capítulo, "Kubernetes no nível do DCA" |

#### Domínio 2 — Imagens e registry (20%)

| Objetivo | Onde está |
|---|---|
| Uso do Dockerfile e opções (`ADD`, `COPY`, `VOLUME`, `EXPOSE`, `ENTRYPOINT`) | Cap. 4, "Instruções" |
| Partes principais de um Dockerfile e imagem eficiente | Cap. 4, "Boas práticas" e "Multi-stage builds" |
| Gerenciar imagens (`ls`, `rm`, `prune`, `rmi`) | Cap. 3, "Comandos essenciais" |
| Inspecionar imagens com filtros e formatação | Cap. 3, "Filtros e formatação" |
| Criar tags | Cap. 3, "Enviar imagens ao Docker Hub" e "Estratégia de tags" |
| Aplicar um arquivo para criar uma imagem; ver camadas; imagem com uma camada | Cap. 3, "Imagem com uma só camada" |
| Implantar e configurar um registry; login; busca; push; pull | Cap. 3, "Registry próprio", "Credenciais da CLI" e "Enviar imagens ao Docker Hub" |
| Assinar uma imagem | Este capítulo, "Docker Content Trust" |
| Apagar imagens de um registry | Cap. 3, "Apagar imagens de um registry" |

#### Domínio 3 — Instalação e configuração (15%)

| Objetivo | Onde está |
|---|---|
| Requisitos de dimensionamento | Cap. 1, "Requisitos"; este capítulo, "Arquitetura, requisitos e alta disponibilidade" |
| Repositório, storage driver e instalação em várias plataformas | Cap. 1, "Formas de instalar" e "Instalação pelo repositório oficial"; cap. 7, "Driver por sistema operacional" |
| Drivers de log (splunk, journald etc.) | Cap. 10, "Drivers de log" |
| Montar o Swarm, configurar managers, adicionar nós e agendar backups | Cap. 11, "Criar e administrar o cluster" e "Backup e restauração do Swarm" |
| Criar e gerenciar usuários e times | Este capítulo, "Usuários, times e RBAC" |
| Iniciar o daemon no boot | Cap. 1, "Pós-instalação no Linux"; cap. 10, "Problemas de instalação e do daemon" |
| Autenticação por certificado entre daemon e registry | Cap. 3, "Certificados de registry" |
| Namespaces, cgroups e certificados | Cap. 1, "Os três pilares do kernel"; cap. 1, "O daemon e suas opções" |
| Diagnosticar erros de instalação | Cap. 10, "Problemas de instalação e do daemon" |
| Instalar Engine, UCP e DTR em alta disponibilidade; backups do UCP e do DTR | Este capítulo, "Docker Enterprise: UCP e DTR" |

#### Domínio 4 — Redes (15%)

| Objetivo | Onde está |
|---|---|
| Container Network Model, drivers de rede e de IPAM | Cap. 6, "Container Network Model (CNM)" |
| Drivers nativos e casos de uso | Cap. 6, "Drivers de rede" |
| Tráfego entre Engine, registry e controladores do UCP | Este capítulo, "Portas e tipos de tráfego" |
| Criar uma rede bridge para desenvolvedores | Cap. 6, "Criar e inspecionar redes" |
| Publicar uma porta; descobrir IP e porta de acesso | Cap. 6, "Publicação de portas"; cap. 11, "Publicação de portas: modo `ingress` vs. modo `host`" |
| Modos de publicação `host` e `ingress` | Cap. 11, "Publicação de portas: modo `ingress` vs. modo `host`" |
| Usar DNS externo | Cap. 1, "O arquivo `daemon.json`"; cap. 6, "Opções de rede do `docker run`" |
| Balanceamento HTTP/HTTPS (L7) | Este capítulo, "Roteamento L7 (Interlock)" |
| Serviço em rede overlay | Cap. 6, "Overlay e redes de camada 2"; cap. 11 |
| Diagnosticar conectividade com logs do contêiner e do Engine | Cap. 6, "Diagnóstico de rede"; cap. 10 |
| Kubernetes: Services ClusterIP e NodePort; modelo de rede | Este capítulo, "Kubernetes no nível do DCA" |

#### Domínio 5 — Segurança (15%)

| Objetivo | Onde está |
|---|---|
| Tarefas de administração de segurança; segurança padrão do Engine | Cap. 9, "Proteger o host e o daemon" e "Endurecer o contêiner em execução" |
| Segurança padrão do Swarm; mTLS | Cap. 11, "Segurança padrão do Swarm" |
| Assinatura de imagens; habilitar o Docker Content Trust | Este capítulo, "Docker Content Trust" |
| Scan de segurança de imagens | Cap. 9, "Cadeia de suprimentos"; este capítulo, "DTR: scan, assinatura, promoção e limpeza" |
| Papéis de identidade; RBAC no UCP; integração com LDAP/AD | Este capítulo, "Usuários, times e RBAC" e "LDAP/AD, client bundles e certificados" |
| Managers e workers do UCP | Este capítulo, "Arquitetura, requisitos e alta disponibilidade" |
| Certificados externos no UCP e no DTR; client bundles | Este capítulo, "LDAP/AD, client bundles e certificados" |

#### Domínio 6 — Armazenamento e volumes (10%)

| Objetivo | Onde está |
|---|---|
| Driver correto para cada sistema operacional | Cap. 7, "Driver por sistema operacional" |
| Configurar o devicemapper | Este capítulo, "devicemapper: `loop-lvm` e `direct-lvm`" |
| Armazenamento de objetos vs. de blocos | Cap. 7, "Blocos, arquivos e objetos" |
| Camadas de uma aplicação e onde ficam no disco | Cap. 3, "Camadas, manifest e digest"; cap. 7, "Onde as camadas ficam no disco" |
| Volumes para persistência | Cap. 7, "Tipos de montagem" e "Características dos volumes" |
| Limpar imagens não usadas no host e no DTR | Cap. 2, "Limpeza"; este capítulo, "DTR: scan, assinatura, promoção e limpeza" |
| Armazenamento entre nós do cluster | Cap. 7, "Backup, restauração e drivers"; cap. 11, "Serviços, atualizações e stacks" |
| Kubernetes: PersistentVolumes, CSI, StorageClass e PVC | Este capítulo, "Kubernetes no nível do DCA" |

### Recursos legados que a prova ainda cobra

#### Docker Content Trust
O **Docker Content Trust (DCT)** assina e verifica **tags** de imagem usando o **Notary** (implementação do framework TUF, The Update Framework). Ele foi aposentado e não deve ser adotado em projetos novos (use **cosign** ou **Notation**, capítulo 9), mas é o que a prova pergunta sobre "assinar uma imagem".

```bash
# Liga o DCT no CLIENTE (variável de ambiente, vale para a sessão)
export DOCKER_CONTENT_TRUST=1
docker push registry.exemplo.com/app:1.0     # assina a tag ao enviar
docker pull registry.exemplo.com/app:1.0     # só aceita a tag se estiver assinada
docker pull --disable-content-trust registry.exemplo.com/app:dev   # exceção pontual

# Gestão de chaves e signatários
docker trust key generate alice               # gera alice.pub e a chave privada
docker trust signer add --key alice.pub alice registry.exemplo.com/app
docker trust sign registry.exemplo.com/app:1.0
docker trust inspect --pretty registry.exemplo.com/app:1.0
docker trust revoke registry.exemplo.com/app:1.0
docker trust signer remove alice registry.exemplo.com/app
```

| Chave | Papel | Onde fica |
|---|---|---|
| **Root** (offline) | Raiz de confiança de todos os repositórios do usuário; cria as chaves de repositório | `~/.docker/trust/private`; guarde **offline** e com backup |
| **Repositório** (targets) | Assina as tags de **um** repositório | `~/.docker/trust/private` |
| **Delegação** | Chave de um signatário (pessoa ou pipeline) autorizado no repositório | Com o signatário |
| **Snapshot** e **timestamp** | Garantem a consistência e o frescor dos metadados | Gerenciadas pelo servidor Notary (timestamp sempre; snapshot opcional) |

- Com `DOCKER_CONTENT_TRUST=1`, `pull`, `run`, `create` e `build` (no `FROM`) **recusam tags sem assinatura**; `push` assina. A verificação é feita pelo **cliente**: o Engine comunitário não tem uma opção de daemon para exigir assinaturas. Essa exigência no nível do cluster era um recurso do **UCP** ("executar só imagens assinadas por times definidos").
- A assinatura é da **tag**; um pull pelo digest (`@sha256:`) já é verificável por si.
- Senhas das chaves em automação: `DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE` e `DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE`. Servidor Notary: `DOCKER_CONTENT_TRUST_SERVER`.
- **Perdeu a chave root**: não há recuperação; é preciso rotacionar as chaves (`notary key rotate`) e reassinar.

#### devicemapper: `loop-lvm` e `direct-lvm`
O **devicemapper** faz copy-on-write em nível de **bloco**, com thin provisioning do LVM. Foi o driver padrão do RHEL e do CentOS até o `overlay2` ser suportado lá, e foi **removido no Engine 25**. A prova cobra os dois modos:

| Modo | Como funciona | Uso |
|---|---|---|
| **`loop-lvm`** | Padrão quando se escolhe o devicemapper sem mais nada: dois **arquivos esparsos** (`data` e `metadata`) em `/var/lib/docker/devicemapper` montados como dispositivos de loopback | **Só testes**: desempenho ruim. O `docker info` avisa `Data loop file` e `usage of loopback devices is strongly discouraged for production use` |
| **`direct-lvm`** | Um **dispositivo de bloco dedicado** vira um thin pool do LVM | **Produção** |

```json
{
  "storage-driver": "devicemapper",
  "storage-opts": [
    "dm.directlvm_device=/dev/xvdf",
    "dm.thinp_percent=95",
    "dm.thinp_metapercent=1",
    "dm.thinp_autoextend_threshold=80",
    "dm.thinp_autoextend_percent=20",
    "dm.directlvm_device_force=false"
  ]
}
```

- Com `dm.directlvm_device`, o próprio Docker cria o physical volume, o volume group `docker` e o thin pool no disco indicado (o disco é **apagado**). A alternativa manual era criar o thin pool com `pvcreate`, `vgcreate`, `lvcreate` e `lvconvert` e apontar `dm.thinpooldev=/dev/mapper/docker-thinpool`.
- `dm.thinp_autoextend_*` configura a extensão automática do pool pelo LVM (a 80% de uso, cresce 20%). `dm.basesize` definia o tamanho máximo do sistema de arquivos de cada contêiner (padrão 10 GB). `dm.use_deferred_removal` e `dm.use_deferred_deletion` evitavam erros de "device busy".
- Mudar para `devicemapper` (ou sair dele) torna invisíveis as imagens e os contêineres existentes (capítulo 7).

### Docker Enterprise: UCP e DTR (hoje MKE e MSR)

#### O que eram e o que são hoje

| Produto do Docker Enterprise (até 2019) | Nome atual (Mirantis) | Papel |
|---|---|---|
| Docker Engine - Enterprise | **Mirantis Container Runtime (MCR)** | Engine com suporte comercial e recursos como FIPS |
| **Universal Control Plane (UCP)** | **Mirantis Kubernetes Engine (MKE)** | Interface web e API para gerenciar um cluster **Swarm e Kubernetes**, com usuários, times, RBAC e LDAP |
| **Docker Trusted Registry (DTR)** | **Mirantis Secure Registry (MSR)** | Registry privado com scan de vulnerabilidades, assinatura, promoção de imagens e espelhamento |

- A Mirantis comprou o Docker Enterprise em **novembro de 2019**; a Docker Inc. ficou com o Docker Desktop, o Docker Hub e as ferramentas de desenvolvedor.
- O **MKE 3** manteve a arquitetura do UCP, com Swarm e Kubernetes lado a lado. O **MKE 4** passou a ser baseado no **k0s** e **não suporta Swarm**; quem usa Swarm continua no MKE 3.
- A prova segue a arquitetura do UCP 3 e do DTR 2, descrita a seguir.

#### Arquitetura, requisitos e alta disponibilidade
- O UCP é instalado **sobre um Swarm**, como contêineres: `docker container run --rm -it --name ucp -v /var/run/docker.sock:/var/run/docker.sock docker/ucp install --host-address <ip> --interactive`. Nós que entram no Swarm depois passam a ser gerenciados automaticamente.

| Papel | O que roda | Observações |
|---|---|---|
| **Manager do UCP** (manager do Swarm) | Controlador do UCP (interface web e API), autenticação, armazenamento de chave-valor (etcd), banco de autenticação (RethinkDB), control plane do Kubernetes, CA do cluster | Para HA: **3, 5 ou 7** managers atrás de um **load balancer TCP** na porta 443 (**sem terminar o TLS**, em modo passthrough). Por padrão, **usuários comuns não podem agendar cargas nos managers** |
| **Worker do UCP** | Agente do UCP (`ucp-agent`, serviço global), proxy do Engine, kubelet e as **aplicações** | O **DTR** é instalado em **workers**, nunca em managers |
| **Réplica do DTR** | Registry, API, interface, banco de metadados (RethinkDB), jobs de scan e GC | Para HA: **3, 5 ou 7 réplicas** em workers diferentes, com **armazenamento compartilhado** (NFS ou, preferencialmente, objetos) e um load balancer à frente |

| Requisitos da época (UCP 3.x) | Mínimo | Recomendado para produção |
|---|---|---|
| Manager | **8 GB de RAM**, 2 vCPUs | **16 GB de RAM**, 4 vCPUs, 25 a 100 GB de disco livre |
| Worker | **4 GB de RAM** | Conforme a carga das aplicações |
| Nó com DTR | 16 GB de RAM, 2 vCPUs | 16 GB de RAM, 4 vCPUs, 25 a 100 GB de disco livre |

- Relógios sincronizados (NTP), IP fixo e hostnames resolvíveis em todos os nós; managers espalhados por zonas de falha.

#### Portas e tipos de tráfego

| Tráfego | De → para | Porta e protocolo |
|---|---|---|
| Interface web, API do UCP e CLI com client bundle | Usuários → managers | **443/tcp** (HTTPS) |
| API do Kubernetes (`kubectl`) | Usuários → managers | **6443/tcp** |
| Controle do UCP sobre cada Engine | Managers → proxy do Engine em todos os nós | **12376/tcp** (TLS mútuo) |
| Componentes internos do UCP (etcd, CA, autenticação, métricas) | Entre managers e nós | Faixa **12379–12388/tcp** |
| Gerenciamento do Swarm, gossip e overlay | Entre nós | **2377/tcp**, **7946/tcp e udp**, **4789/udp** |
| Rede de Pods do Kubernetes (Calico) | Entre nós | **179/tcp** (BGP) e o encapsulamento do Calico |
| Pull e push de imagens | Engines e usuários → DTR | **443/tcp** (HTTPS, com o certificado confiado em `certs.d`) |
| Login no DTR | DTR → UCP | O DTR usa o **UCP como provedor de identidade** (single sign-on) |
| Replicação entre réplicas do DTR | Réplica ↔ réplica | Rede overlay própria do DTR |

- Toda comunicação de controle é **TLS mútuo**, com certificados das CAs internas do UCP. O tráfego das aplicações segue a rede escolhida (overlay, com ou sem `encrypted`).

#### Usuários, times e RBAC

| Conceito | O que é |
|---|---|
| **Usuário** | Conta individual (local ou sincronizada do LDAP/AD). Pode ser **administrador** (acesso total) ou comum |
| **Organização** | Agrupa **times** |
| **Time** | Grupo de usuários dentro de uma organização; pode ter a lista de membros sincronizada de um grupo do LDAP |
| **Service account** | Identidade de aplicações no Kubernetes |
| **Sujeito** (*subject*) | Quem recebe a permissão: usuário, time, organização ou service account |
| **Papel** (*role*) | Conjunto de operações permitidas |
| **Conjunto de recursos** | **Coleção** (Swarm: hierarquia como `/Shared/Private/<usuário>`, contendo serviços, nós, redes, volumes, secrets) ou **namespace** (Kubernetes) |
| **Grant** | A regra de acesso: **sujeito + papel + conjunto de recursos** |

| Papel padrão | Permite |
|---|---|
| **None** | Nada |
| **View Only** | Ver recursos, sem alterar |
| **Restricted Control** | Criar e alterar recursos, **sem** operações que afetam o nó: nada de `--privileged`, bind mount do host, `exec` ou capabilities extras |
| **Scheduler** | Ver nós e **agendar** cargas neles (dado em coleções de nós) |
| **Full Control** | Tudo nos recursos do grant, inclusive operações privilegiadas |

- Além dos papéis padrão, é possível criar **papéis personalizados** escolhendo operações.
- Cada usuário novo recebe uma coleção privada (`/Shared/Private/<usuário>`); as coleções `/System` (componentes do UCP) e `/Shared` (nós compartilhados) já vêm criadas.
- O DTR usa os mesmos usuários, organizações e times do UCP; as permissões de repositório (leitura, leitura e escrita, admin) são dadas a times.

#### LDAP/AD, client bundles e certificados
- **LDAP ou Active Directory**: configurado em *Admin Settings → Authentication & Authorization*, com a URL do servidor, um usuário de leitura (reader DN e senha), a base de busca, o filtro e o atributo de nome de usuário. O UCP **sincroniza** os usuários periodicamente (intervalo configurável) e pode sincronizar a lista de membros de cada time a partir de um grupo do diretório. Use `ldaps://` ou StartTLS.
- **Client bundle**: arquivo zip gerado pelo usuário em *My Profile → Client Bundles* (ou pela API). Contém um **certificado de cliente** com a identidade do usuário (`cert.pem`, `key.pem`, `ca.pem`), um `kube.yml` e os scripts `env.sh`, `env.ps1` e `env.cmd`.

```bash
unzip ucp-bundle-alice.zip -d bundle && cd bundle
eval "$(<env.sh)"      # define DOCKER_HOST, DOCKER_TLS_VERIFY, DOCKER_CERT_PATH e KUBECONFIG
docker node ls          # o comando vai para o UCP, que aplica o RBAC de alice
kubectl get pods
```

- Os comandos feitos com o bundle passam pelo UCP e respeitam os **grants do usuário**; um bundle pode ser **revogado** na interface. Trate-o como uma senha.
- **Certificados externos** (de uma CA da empresa, para os navegadores confiarem): no UCP, em *Admin Settings → Certificates* (CA, certificado e chave) ou na instalação com `--external-server-cert`, colocando os arquivos no volume `ucp-controller-server-certs`. No DTR, com `--dtr-ca`, `--dtr-cert` e `--dtr-key` no `install` ou `reconfigure`, ou na interface. Os Engines que baixam do DTR precisam confiar na CA (`/etc/docker/certs.d/<dtr>/ca.crt`, capítulo 3).

#### Roteamento L7 (Interlock)
O **Interlock** (sucessor do *HTTP Routing Mesh*, HRM, do UCP 2) é o balanceador **HTTP/HTTPS de camada 7** do UCP para serviços Swarm. É ligado em *Admin Settings → Layer 7 Routing* e roda três serviços: `ucp-interlock` (lê a API do Swarm), `ucp-interlock-extension` (gera a configuração) e `ucp-interlock-proxy` (NGINX que recebe o tráfego, por padrão nas portas 8080 e 8443).

```bash
docker service create --name app --network app-net \
  --label com.docker.lb.hosts=app.exemplo.com \
  --label com.docker.lb.port=8080 \
  --label com.docker.lb.network=app-net \
  minha-org/app:1.0
```

- O roteamento é feito pelo **cabeçalho `Host`** (virtual hosts), com rótulos do serviço. Outros rótulos: `com.docker.lb.ssl_cert`/`ssl_key` (TLS no proxy), `com.docker.lb.sticky_session_cookie`, `com.docker.lb.redirects`, `com.docker.lb.context_root`.
- **Routing mesh (L4)** vs. **Interlock (L7)**: o routing mesh encaminha **portas TCP/UDP** para qualquer tarefa; o Interlock entende **HTTP**, roteia por nome de host e caminho e termina TLS. Para Kubernetes, o equivalente é Ingress ou Gateway API.
- Hoje, fora do MKE, o mesmo papel é feito por **Traefik**, Caddy ou NGINX configurados por rótulos de serviço.

#### DTR: scan, assinatura, promoção e limpeza
- **Scan de vulnerabilidades**: o DTR compara os componentes de cada camada com um **banco de CVEs** (atualizado online ou importado offline) e pode escanear **a cada push** ou manualmente. O resultado aparece por tag, com severidade por camada e componente.
- **Assinatura**: o DTR tem um servidor **Notary** embutido; com `DOCKER_CONTENT_TRUST=1`, o push para o DTR assina a tag. A interface mostra quais tags estão assinadas, e o UCP pode exigir assinatura de times específicos para rodar imagens.
- **Tags imutáveis**: uma opção por repositório impede sobrescrever uma tag existente.
- **Políticas de promoção**: copiam uma imagem para outro repositório quando atende a critérios (por exemplo, "sem vulnerabilidades críticas" ou "tag casa com `release-*`"). **Espelhamento** (*mirroring*) envia ou puxa imagens entre registries, e o **cache** atende sites remotos.
- **Limpeza no DTR**: apagar tags (interface ou API), configurar **políticas de pruning de tags** (por idade, quantidade ou padrão) e agendar o **garbage collection**, que remove camadas sem referência do armazenamento. Apagar uma tag **não** libera espaço até o garbage collection rodar.
- **Armazenamento**: sistema de arquivos local, NFS ou **objetos** (S3, Azure Blob, Google Cloud Storage, Swift). Com várias réplicas, o armazenamento precisa ser **compartilhado**, e objetos é o preferido.

#### Backup e restauração do Docker Enterprise
A ordem é sempre a mesma, tanto no backup quanto na restauração: **Swarm → UCP → DTR**.

| Componente | Como | O que o backup contém |
|---|---|---|
| **Swarm** | Cópia de `/var/lib/docker/swarm` com o Docker parado (capítulo 11) | Estado do cluster, serviços, secrets |
| **UCP** | `docker container run --rm --log-driver none --name ucp -v /var/run/docker.sock:/var/run/docker.sock docker/ucp backup --id <id-do-ucp> --passphrase "…" > ucp-backup.tar`, em **um** manager | Configuração do UCP, usuários, times, grants, coleções, certificados. **Não** inclui o estado do Swarm nem as cargas |
| **DTR** | `docker run --rm docker/dtr backup --ucp-url … --existing-replica-id <id> > dtr-metadata.tar` | **Só metadados**: configurações, repositórios, permissões, assinaturas. **Não inclui as imagens**: faça backup do armazenamento (bucket, NFS) à parte |

- O UCP também faz backup pela interface ou API, e o backup pode ser **agendado**. Durante o backup, os componentes do UCP **naquele manager** param por alguns instantes; os outros managers continuam atendendo.
- A restauração do UCP (`docker/ucp restore < ucp-backup.tar`) é feita em um Swarm onde o UCP **não** está instalado, com a **mesma versão** do backup.

### Kubernetes no nível do DCA

#### Objetos cobrados
A prova pede o Kubernetes **conceitual**: saber qual objeto usar e ler um manifest. O e-book de Kubernetes desta coleção aprofunda cada tema.

| Objeto | Para que serve | Equivalente no Swarm |
|---|---|---|
| **Pod** | Menor unidade: um ou mais contêineres que compartilham rede (mesmo IP) e volumes | Tarefa |
| **Deployment** | Mantém N réplicas de um Pod (por meio de um ReplicaSet) e faz rolling update e rollback | Serviço replicated |
| **ConfigMap** | Configuração não sensível, injetada como variáveis de ambiente ou arquivos | `docker config` |
| **Secret** | Dados sensíveis, injetados como variáveis ou arquivos. Por padrão só **codificados em base64** no etcd; a cifra em repouso precisa ser configurada | `docker secret` |
| **Service `ClusterIP`** (padrão) | IP virtual **interno** e nome DNS estável que balanceiam entre os Pods selecionados por rótulos | VIP do serviço |
| **Service `NodePort`** | Tudo do ClusterIP **mais** uma porta (faixa **30000–32767**) aberta em **todos os nós** | Routing mesh (`ingress`) |
| **PersistentVolume (PV)** | Um pedaço de armazenamento do cluster, criado pelo administrador ou dinamicamente | Volume com driver |
| **PersistentVolumeClaim (PVC)** | O **pedido** de armazenamento feito pela aplicação (tamanho e modo de acesso) | `--mount type=volume` |
| **StorageClass** | Define o **provisionador** (driver CSI) e os parâmetros para criar PVs sob demanda | Driver de volume e opções |

#### Um exemplo completo

```yaml
apiVersion: v1
kind: ConfigMap
metadata: { name: web-config }
data:
  APP_MODE: producao
---
apiVersion: v1
kind: Secret
metadata: { name: web-secret }
type: Opaque
stringData:                     # o Kubernetes converte para base64 em data
  DB_PASSWORD: troque-me
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata: { name: web-dados }
spec:
  accessModes: [ReadWriteOnce]
  storageClassName: standard    # a StorageClass aciona o driver CSI
  resources: { requests: { storage: 1Gi } }
---
apiVersion: apps/v1
kind: Deployment
metadata: { name: web }
spec:
  replicas: 3
  selector: { matchLabels: { app: web } }
  template:
    metadata: { labels: { app: web } }
    spec:
      containers:
        - name: web
          image: nginx:1.28
          ports: [{ containerPort: 80 }]
          envFrom:
            - configMapRef: { name: web-config }
          env:
            - name: DB_PASSWORD
              valueFrom: { secretKeyRef: { name: web-secret, key: DB_PASSWORD } }
          volumeMounts: [{ name: dados, mountPath: /usr/share/nginx/html }]
      volumes:
        - name: dados
          persistentVolumeClaim: { claimName: web-dados }
---
apiVersion: v1
kind: Service
metadata: { name: web }
spec:
  type: NodePort                # sem "type", seria ClusterIP
  selector: { app: web }
  ports: [{ port: 80, targetPort: 80, nodePort: 30080 }]
```

```bash
kubectl apply -f web.yaml
kubectl get deploy,pods,svc,pvc
kubectl scale deployment web --replicas 5
kubectl set image deployment/web web=nginx:1.29 && kubectl rollout status deployment/web
kubectl rollout undo deployment/web
```

- O PVC com `ReadWriteOnce` é montado por **um nó** de cada vez: réplicas em nós diferentes não conseguem montar o mesmo volume. Para várias réplicas com dados próprios, use StatefulSet; para compartilhar, um volume `ReadWriteMany` (NFS, sistemas de arquivos em rede).

#### Modelo de rede e armazenamento

- **Modelo de rede do Kubernetes**: cada Pod tem **um IP próprio**; todos os Pods se comunicam com todos os outros **sem NAT**, em qualquer nó; os contêineres de um Pod compartilham o IP e se falam por `localhost`. A implementação é feita por um plugin **CNI** (Calico, Cilium, Flannel), não pelo CNM do Docker. O `kube-proxy` (ou o próprio CNI) implementa os IPs virtuais dos Services, e o DNS do cluster resolve `web.<namespace>.svc.cluster.local`.
- **Isolamento**: por padrão, qualquer Pod fala com qualquer Pod; **NetworkPolicies** restringem o tráfego (se o CNI as suportar).
- **Relação CSI → StorageClass → PVC → PV → volume**: o administrador instala um **driver CSI** (Container Storage Interface, o padrão para plugins de armazenamento) e cria uma **StorageClass** que o referencia. A aplicação cria um **PVC** citando a StorageClass; o driver **provisiona dinamicamente** um **PV** e o liga ao PVC; o Pod declara um **volume** do tipo `persistentVolumeClaim` e o monta no contêiner.
- **Provisionamento estático**: o administrador cria PVs à mão, e o PVC é ligado a um PV compatível (tamanho, modo de acesso, StorageClass).
- **`reclaimPolicy`** da StorageClass ou do PV: `Delete` (padrão no provisionamento dinâmico, apaga o disco junto com o PVC) ou `Retain` (mantém o disco para recuperação manual).
- **Modos de acesso**: `ReadWriteOnce` (um nó), `ReadOnlyMany`, `ReadWriteMany` (vários nós) e `ReadWriteOncePod` (um único Pod).

### Decisão rápida — DCA

| Pergunta típica | Resposta | Alternativa que parece certa, mas não é |
|---|---|---|
| Como assinar uma imagem ao enviá-la? | `export DOCKER_CONTENT_TRUST=1` e `docker push` | `docker sign` (não existe) |
| Onde colocar a CA de um registry privado? | `/etc/docker/certs.d/<host:porta>/ca.crt` | `insecure-registries` (desliga a verificação) |
| Qual driver de armazenamento para contêineres Windows? | `windowsfilter` | `overlay2` |
| devicemapper em produção? | `direct-lvm` com dispositivo de bloco dedicado | `loop-lvm` (padrão, só para testes) |
| Armazenamento preferido para um registry em HA? | Objetos (S3, Azure Blob, GCS) | Volume local em cada réplica |
| Backup do Swarm? | `/var/lib/docker/swarm` com o Docker parado em um manager | Copiar com o daemon rodando |
| Ordem de backup e restauração do Docker Enterprise? | Swarm → UCP → DTR | Qualquer ordem |
| O backup do DTR inclui as imagens? | Não, só metadados | Sim |
| Porta aberta em todos os nós do Swarm? | `mode=ingress` (padrão) | `mode=host` |
| Preservar o IP do cliente em um serviço Swarm? | `mode=host` | `ingress` |
| Hostname diferente por tarefa? | `--hostname '{{.Node.Hostname}}-{{.Task.Slot}}'` | `--env HOSTNAME=…` fixo |
| Serviço com tarefas em `Pending`? | `docker service ps --no-trunc`: constraint, recursos ou porta | Remover e recriar o serviço |
| Imagem privada não encontrada pelos workers? | `--with-registry-auth` | Fazer `docker login` só no manager |
| Validade padrão do certificado de um nó do Swarm? | 90 dias, renovado automaticamente | 1 ano |
| Usar os comandos do UCP com as permissões do usuário? | Client bundle (`eval "$(<env.sh)"`) | Acesso direto ao `docker.sock` dos managers |
| Balancear HTTP por nome de host no UCP? | Interlock com `com.docker.lb.hosts` | Routing mesh (é L4) |
| Kubernetes: acesso interno estável a um conjunto de Pods? | Service `ClusterIP` | IP de um Pod |
| Kubernetes: acesso de fora por uma porta em todos os nós? | Service `NodePort` (30000–32767) | `ClusterIP` |
| Kubernetes: quem cria o PV dinamicamente? | O driver CSI indicado pela StorageClass, a partir de um PVC | O Pod |

---

## 14. Pegadinhas e Padrões Recorrentes

> **Como usar**: revise esta seção na véspera de uma entrevista, prova ou revisão de arquitetura. Cada linha é um erro de conceito que aparece com frequência em código real, em fóruns e em questões de certificação.

### Afirmações falsas clássicas

| Afirmação falsa | O que é verdade |
|---|---|
| "`EXPOSE` publica a porta" | `EXPOSE` só documenta. Quem publica é `-p` (ou `-P`, que usa a lista do `EXPOSE`) |
| "Contêiner é uma VM leve" | É um processo isolado por namespaces e cgroups, que compartilha o kernel do host |
| "`latest` é a versão mais nova" | É só a tag padrão; aponta para o que foi enviado por último com esse nome |
| "Apagar um arquivo em um `RUN` posterior diminui a imagem" | O arquivo continua na camada em que foi criado |
| "`docker system prune` apaga meus volumes" | Só com `--volumes`, e mesmo assim só os anônimos (use `docker volume prune -a` para os nomeados) |
| "`docker compose down` apaga o banco" | Só com `-v`. Sem a flag, volumes nomeados são preservados |
| "`depends_on` espera o banco ficar pronto" | Na forma curta, só espera o contêiner **iniciar**. Para esperar ficar pronto: `condition: service_healthy` |
| "O `.env` vai para dentro dos contêineres" | Ele só alimenta a interpolação do arquivo Compose |
| "`--restart always` reinicia contêineres `unhealthy`" | Políticas de reinício reagem à **saída** do processo, não ao healthcheck (no Engine sem orquestrador) |
| "Montar o `docker.sock` com `:ro` é seguro" | O somente leitura vale para o arquivo; a API continua com poder total |
| "Estar no grupo `docker` é mais seguro que usar `sudo`" | É equivalente a root no host |
| "UFW bloqueia portas publicadas pelo Docker" | As regras do Docker são avaliadas antes; use `DOCKER-USER` ou bind em `127.0.0.1` |
| "`ARG` serve para passar senhas ao build" | Valores de `ARG` ficam no histórico da imagem; use build secrets |
| "`docker export` faz backup da imagem" | `export` achata o sistema de arquivos de um **contêiner** e perde metadados; para imagens use `docker save` |
| "Kubernetes não roda imagens Docker" | Kubernetes não usa o Docker Engine, mas roda imagens OCI construídas com Docker normalmente |
| "`version: '3.8'` é obrigatório no Compose" | O campo é obsoleto e só gera aviso |
| "`CMD` e `ENTRYPOINT` são a mesma coisa" | `ENTRYPOINT` é o executável fixo; `CMD` são os argumentos padrão (ou o comando, se não houver `ENTRYPOINT`) |
| "Alpine é sempre a melhor base" | É pequena, mas usa musl libc; binários glibc e algumas bibliotecas nativas falham ou ficam mais lentos |
| "`--cpu-shares` limita a CPU" | É um peso relativo que só vale em disputa; para limitar use `--cpus` |
| "Dois managers dão alta disponibilidade ao Swarm" | Dois managers não toleram nenhuma falha; use 3 ou 5 |
| "O Docker inventou os contêineres" | `chroot`, Jails, Zones, OpenVZ e LXC vieram antes; a inovação do Docker foi tornar a tecnologia acessível |
| "O contêiner emula um sistema operacional" | Ele roda direto no kernel do host, isolado; quem emula hardware e roda outro kernel é a VM |
| "Um contêiner roda em qualquer sistema" | Precisa de kernel compatível (Linux, na prática) e da mesma arquitetura de CPU; no macOS e no Windows, roda numa VM Linux |
| "`exit` sai do contêiner e o deixa rodando" | Em `docker run -it … bash`, `exit` encerra o PID 1 e para o contêiner; use Ctrl+P Ctrl+Q |
| "Só o manager `Leader` aceita comandos do Swarm" | Qualquer manager aceita e encaminha ao líder |
| "O Swarm coloca a tarefa no nó com menor carga" | Ele distribui por quantidade de tarefas e recursos **reservados** (spread), não pela carga medida |
| "Docker secrets só existem no Swarm" | O Compose também tem `secrets` (arquivos montados, sem a criptografia do Raft) |


### Informações desatualizadas em materiais antigos
Livros, cursos e posts de 2015 a 2020 continuam circulando. Ao estudar por eles, atualize estes pontos:

| Se o material diz… | Hoje (set/2026) |
|---|---|
| Instalar com `apt-key adv` e o repositório `apt.dockerproject.org` | `apt-key` está descontinuado e o repositório foi desativado. Use `download.docker.com` com a chave em `/etc/apt/keyrings` (capítulo 1) |
| `service docker start` / `/etc/init.d/docker status` | `systemctl start docker` / `systemctl status docker` |
| Kernel 3.8 ou superior | A documentação lista as versões de distribuição suportadas; qualquer distribuição mantida atende |
| "Docker só roda em Linux 64 bits" | O daemon roda em Linux (`amd64`, `arm64` e outras arquiteturas de 64 bits); no macOS e no Windows, via VM. Há também contêineres Windows nativos |
| Storage drivers AUFS, devicemapper e `overlay` | Removidos (Engine 24 e 25). `overlay2` no store clássico ou containerd snapshotters, padrão no Engine 29 |
| `--storage-opt dm.basesize`, `dm.thinpooldev` | Opções do devicemapper, que não existe mais |
| `docker daemon …` ou `docker -d` | `dockerd` |
| Docker Machine, boot2docker, Docker Toolbox | Descontinuados. Docker Desktop (ou alternativas) localmente; Terraform/cloud-init + `docker context` para hosts remotos |
| `dockerd -H tcp://0.0.0.0:2375` | Nunca sem TLS; use SSH (`docker context`) ou TLS mútuo na porta 2376 |
| `--link` para ligar contêineres | Redes definidas pelo usuário com DNS embutido |
| Data-only container com `--volumes-from` | Volumes nomeados (`docker volume create`) |
| `docker-compose` (com hífen) e `version: "3"` | `docker compose` (plugin, v5) e arquivo `compose.yaml` sem `version` |
| "Para usar Compose, use `docker stack`" | `docker compose` para um host; `docker stack deploy` para Swarm |
| `registry:2` e `github.com/docker/distribution` | `registry:3`, projeto `distribution/distribution` na CNCF |
| Criar conta com `docker login` | Conta criada no site do Docker Hub; `docker login` só autentica |
| Site ImageLayers para ver camadas | Página da tag no Docker Hub, `docker image history`, `buildx imagetools inspect`, dive |
| Saída de build com `Step 1/2` e `Removing intermediate container` | Saída do BuildKit (`[+] Building`, `[1/2]`, `CACHED`) |
| `MAINTAINER` no Dockerfile | `LABEL org.opencontainers.image.authors=…` |
| Imagens `centos:7`, `debian:8`, `mysql:5.7`, `postgres:9.4`, `mongo:3.2`, `alpine:3.1` | Todas fora de suporte. Use versões mantidas e fixe a tag (e o digest) |
| `KernelMemory` / `--kernel-memory` | Descontinuado; sem efeito com cgroup v2 |
| Docker Content Trust (`DOCKER_CONTENT_TRUST=1`) | Aposentado. Use cosign ou Notation (a prova do DCA ainda cobra: capítulo 13) |
| Swarm com 2 managers | 3 (ou 5) managers; 2 não toleram nenhuma falha |
| "Volume de um serviço Swarm é compartilhado entre os nós" | Com o driver `local`, cada nó tem o seu volume; compartilhar exige driver de rede |
| Dois bancos de dados usando o mesmo volume de dados | Nunca: corrompe os dados. Um volume por instância e replicação do banco |

### Pares que mais se confundem

| Par | Diferença |
|---|---|
| `docker run` vs. `docker start` | `run` cria um contêiner **novo**; `start` inicia um contêiner **existente** |
| `docker exec` vs. `docker attach` | `exec` inicia um processo **novo** no contêiner; `attach` conecta ao STDIN/STDOUT do **PID 1** (sair com Ctrl+C pode parar o contêiner; use Ctrl+P Ctrl+Q para desanexar) |
| `docker stop` vs. `docker kill` | `stop` envia `SIGTERM` e espera; `kill` envia `SIGKILL` (ou outro sinal) imediatamente |
| `docker save` vs. `docker export` | `save` exporta **imagens** com camadas e metadados; `export` exporta o sistema de arquivos de um **contêiner** |
| `COPY` vs. `ADD` | `ADD` também baixa URLs, clona Git e extrai tarballs locais; prefira `COPY` |
| `CMD` vs. `ENTRYPOINT` | Argumentos do `docker run` substituem o `CMD`; o `ENTRYPOINT` só muda com `--entrypoint` |
| `ARG` vs. `ENV` | `ARG` só existe no build; `ENV` persiste na imagem e na execução |
| Volume vs. bind mount | Volume é gerenciado pelo Docker e pré-populado; bind mount é um caminho do host e esconde o conteúdo da imagem |
| Bridge padrão vs. definida pelo usuário | Só a definida pelo usuário tem DNS por nome e isolamento por rede |
| `-p 8080:80` vs. `-p 127.0.0.1:8080:80` | O primeiro expõe em todas as interfaces; o segundo só localmente |
| `always` vs. `unless-stopped` | Após reiniciar o daemon, `always` volta mesmo se tiver sido parado manualmente; `unless-stopped` não |
| `docker compose run` vs. `exec` | `run` cria um contêiner avulso novo; `exec` roda um processo em um contêiner já em execução |
| Imagem dangling vs. não usada | Dangling não tem tag (`<none>`); não usada pode ter tag, mas nenhum contêiner a usa |
| Tag vs. digest | A tag é móvel; o digest é imutável e identifica o conteúdo |
| Rootless vs. `userns-remap` | No rootless, o **daemon** também roda sem root; no `userns-remap`, só o root do contêiner é mapeado |
| `mode=min` vs. `mode=max` no cache | `max` exporta também as camadas de estágios intermediários |
| Replicated vs. global (Swarm) | Número fixo de réplicas vs. uma tarefa por nó |
| `docker compose` vs. `docker stack deploy` | O mesmo formato de arquivo: `compose` roda em um host; `stack` implanta como serviços de um Swarm |
| `dockerd` vs. `docker` | `dockerd` é o daemon (servidor); `docker` é a CLI (cliente) que fala com a API dele |
| `bip` vs. `default-address-pools` | `bip` define a sub-rede da bridge padrão `docker0`; `default-address-pools`, as faixas das redes criadas pelo usuário e pelo Compose |
| `docker secret` vs. `docker config` | Os dois são arquivos entregues aos serviços; o secret é cifrado e seu conteúdo nunca aparece no `inspect` |
| `docker node promote` vs. `docker swarm join-token manager` | `promote` transforma um worker existente em manager; o token de manager faz um nó novo entrar já como manager |

### Palavras-chave e respostas

| Se o problema diz… | Pense em… |
|---|---|
| "demora 10 segundos para parar" | PID 1 não trata `SIGTERM`; forma exec, `exec "$@"`, `--init` |
| "saiu com 137" | OOM kill ou `SIGKILL` |
| "`exec format error`" | Arquitetura errada; `--platform`, imagem multiplataforma |
| "o nome do outro contêiner não resolve" | Rede bridge definida pelo usuário |
| "funciona dentro, mas não pela porta publicada" | Aplicação escutando em `127.0.0.1` |
| "o build reinstala tudo a cada commit" | Ordem das instruções e `.dockerignore` |
| "token no build" | `RUN --mount=type=secret` |
| "imagem enorme" | Multi-stage, base mínima, limpar na mesma camada |
| "disco cheio" | `docker system df`, prune, rotação de logs |
| "precisa rodar em Mac M-series e servidor x86" | `buildx --platform linux/amd64,linux/arm64` |
| "sem perder dados ao recriar o contêiner" | Volume nomeado |
| "a API sobe antes do banco" | `depends_on` com `service_healthy` |
| "cluster tolerante a falha de um manager" | 3 managers |
| "garantir que o que foi testado é o que vai para produção" | Promover o digest |

---

## 15. Referência Rápida de Comandos

> **Como usar**: consulta de bancada. Os comandos seguem a forma agrupada (`docker container …`, `docker image …`); as formas curtas (`docker ps`, `docker rmi`) continuam válidas.

### Contêineres

| Comando | Para que serve |
|---|---|
| `docker run -d --name app -p 8080:80 imagem` | Cria e inicia em segundo plano |
| `docker run --rm -it imagem sh` | Sessão interativa descartável |
| `docker ps -a --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'` | Lista com colunas escolhidas |
| `docker logs -f --since 10m app` | Acompanha os logs |
| `docker exec -it app sh` | Shell no contêiner em execução |
| `docker stop app` / `docker start app` / `docker restart app` | Controle de execução |
| `docker rm -f app` | Remove (forçando a parada) |
| `docker inspect -f '{{.State.ExitCode}}' app` | Campo específico do estado |
| `docker stats --no-stream` | Consumo de recursos |
| `docker cp app:/etc/config.yaml .` | Copia arquivos do contêiner |
| `docker update --memory 1g app` | Ajusta limites em execução |

### Imagens e build

| Comando | Para que serve |
|---|---|
| `docker build -t org/app:1.0 .` | Build local |
| `docker build --target test .` | Build até um estágio |
| `docker build --check .` | Build checks sem construir |
| `docker build --secret id=npmrc,src=$HOME/.npmrc .` | Build com segredo |
| `docker buildx build --platform linux/amd64,linux/arm64 -t org/app:1.0 --push .` | Build multiplataforma |
| `docker buildx bake --push` | Vários builds a partir do arquivo Bake |
| `docker image history org/app:1.0` | Camadas e tamanhos |
| `docker buildx imagetools inspect org/app:1.0` | Plataformas e digests no registry |
| `docker tag org/app:1.0 ghcr.io/org/app:1.0` | Novo nome para a mesma imagem |
| `docker push ghcr.io/org/app:1.0` | Envio ao registry |
| `docker save -o app.tar org/app:1.0` / `docker load -i app.tar` | Transporte sem registry |
| `docker scout quickview org/app:1.0` | Resumo de vulnerabilidades |
| `docker image ls --filter dangling=true --format '{{.ID}}'` | Filtra e formata a listagem |
| `docker image inspect -f '{{json .RootFS.Layers}}' org/app:1.0` | Digests das camadas |
| `DOCKER_CONTENT_TRUST=1 docker push …` / `docker trust inspect --pretty …` | Assina e confere com o DCT (legado, cobrado no DCA) |

### Redes e volumes

| Comando | Para que serve |
|---|---|
| `docker network create app` | Rede bridge definida pelo usuário |
| `docker network create --internal dados` | Rede sem saída externa |
| `docker network create --subnet 172.30.0.0/24 --gateway 172.30.0.1 dev` | Bridge com sub-rede e gateway próprios |
| `docker network connect app contêiner` | Conecta um contêiner em execução |
| `docker network inspect app` | Contêineres e IPs da rede |
| `docker volume create dados` | Cria um volume nomeado |
| `docker volume inspect dados` | Driver e ponto de montagem |
| `docker run --rm -v dados:/d -v "$(pwd)":/b alpine tar czf /b/dados.tgz -C /d .` | Backup de volume |

### Compose

| Comando | Para que serve |
|---|---|
| `docker compose up -d --build --wait` | Sobe, reconstruindo e esperando ficar saudável |
| `docker compose config` | Modelo resolvido |
| `docker compose ps` / `logs -f` | Estado e logs |
| `docker compose exec web sh` | Shell em um serviço |
| `docker compose run --rm web npm test` | Tarefa avulsa |
| `docker compose watch` | Sincronização em desenvolvimento |
| `docker compose --profile debug up -d` | Inclui serviços de um perfil |
| `docker compose down` / `down -v` | Remove tudo / e também os volumes |

### Sistema, contextos e Swarm

| Comando | Para que serve |
|---|---|
| `docker version` / `docker info` | Versões e configuração do daemon |
| `docker system df -v` | Uso de disco |
| `docker system prune -af --filter until=24h` | Limpeza agressiva de itens antigos |
| `docker events --filter event=oom` | Eventos de OOM |
| `docker context create prod --docker host=ssh://user@host` | Contexto remoto |
| `docker context use prod` | Troca o daemon alvo |
| `docker swarm init --advertise-addr <ip>` | Cria um Swarm |
| `docker node ls` / `docker node update --availability drain <nó>` | Nós e manutenção |
| `docker stack deploy -c compose.yaml loja` | Implanta uma stack |
| `docker service ls` / `ps` / `logs` / `rollback` | Operação de serviços |
| `docker service ps --no-trunc web` | Erro completo de tarefas que não sobem |
| `docker service create --publish published=8080,target=80,mode=host …` | Porta só nos nós das tarefas |
| `docker service create --hostname '{{.Node.Hostname}}' …` | Template por tarefa |
| `docker service update --force web` | Redistribui as tarefas |
| `docker swarm ca --rotate` / `docker swarm update --cert-expiry 720h` | Troca a CA / validade dos certificados |

---

## 16. Autoteste — Flashcards de Revisão

Cada card abaixo esconde a resposta: clique para expandir só depois de tentar responder mentalmente. O objetivo é forçar a lembrança ativa, não a releitura. Uma rodada de 20 cards por dia cobre todo o banco em menos de uma semana.

### Fundamentos e ciclo de vida

> [!question]- Quais mecanismos do kernel Linux tornam um contêiner possível?
> **Namespaces** (isolam o que o processo enxerga), **cgroups** (limitam o que ele consome) e um **sistema de arquivos em camadas** (union filesystem/snapshotter). Capabilities, seccomp e AppArmor/SELinux complementam a segurança.

> [!question]- Qual é a principal diferença de isolamento entre contêiner e VM?
> O contêiner **compartilha o kernel** do host; a VM tem **kernel próprio** sobre um hypervisor. Por isso a VM oferece uma fronteira de segurança mais forte, e o contêiner é mais leve e rápido.

> [!question]- Qual é o caminho de um `docker run` até o processo?
> CLI → API do `dockerd` → containerd → containerd-shim → runc, que cria namespaces e cgroups, executa o processo e sai. O shim continua como pai do processo.

> [!question]- O que o Engine 29 mudou no armazenamento de imagens?
> O **containerd image store** passou a ser o padrão em instalações novas, no lugar dos storage drivers clássicos como `overlay2`. Ele suporta imagens multiplataforma e atestados nativamente.

> [!question]- Por que estar no grupo `docker` equivale a ter root?
> Porque quem controla o daemon pode executar um contêiner privilegiado montando `/` do host e alterar qualquer arquivo.

> [!question]- Qual é a forma recomendada de acessar um daemon Docker remoto?
> `docker context` com **SSH** (`host=ssh://usuario@servidor`), ou TCP com TLS mútuo na porta 2376. Nunca a porta 2375 sem TLS.

> [!question]- O que acontece, passo a passo, em um `docker stop`?
> O Docker envia `SIGTERM` (ou o `STOPSIGNAL`) ao PID 1, espera **10 segundos** e, se o processo não sair, envia `SIGKILL`.

> [!question]- Por que uma aplicação iniciada com `CMD node server.js` demora para parar?
> Na forma shell, o PID 1 é `/bin/sh`, que não repassa o `SIGTERM` ao Node. O Docker espera 10 s e mata com `SIGKILL`. A correção é a forma exec: `CMD ["node", "server.js"]`.

> [!question]- O que significam os códigos de saída 125, 126, 127 e 137?
> **125**: o próprio `docker run` falhou. **126**: comando não executável. **127**: comando não encontrado. **137**: morto por `SIGKILL` (128 + 9), muitas vezes por OOM.

> [!question]- Qual é a diferença entre as políticas `always` e `unless-stopped`?
> Ambas reiniciam o contêiner quando ele sai. Depois de reiniciar o daemon, `always` sobe o contêiner mesmo que ele tenha sido parado manualmente; `unless-stopped` respeita a parada manual.

> [!question]- Para que serve `--init`?
> Coloca um init mínimo (`tini`) como PID 1, que repassa sinais à aplicação e recolhe processos zumbis.

> [!question]- Como investigar um contêiner cuja imagem não tem shell?
> `docker debug <contêiner>` (Docker Desktop) ou um contêiner auxiliar compartilhando namespaces: `docker run -it --rm --pid container:app --network container:app nicolaka/netshoot`.

> [!question]- O que `docker system prune` remove por padrão?
> Contêineres parados, redes não usadas, imagens dangling e cache de build. **Não** remove volumes nem imagens com tag não usadas (isso exige `--volumes` e `-a`).

> [!question]- O Docker inventou os contêineres? Qual foi a inovação dele?
> Não. `chroot` (1979), FreeBSD Jails, Solaris Zones, OpenVZ e LXC vieram antes. A inovação do Docker foi de **experiência**: Dockerfile, imagem em camadas, registry público (Docker Hub) e uma CLI simples, que tornaram a tecnologia acessível a qualquer desenvolvedor.

> [!question]- Qual era a relação entre o Docker e o LXC?
> As primeiras versões do Docker (2013) eram um wrapper do LXC com AUFS. No Docker 0.9 (2014), o LXC foi trocado pela **libcontainer**, que depois deu origem ao **runc**.

> [!question]- Qual namespace isola hostname e qual isola a árvore de processos?
> **UTS** isola hostname e domínio; **PID** isola a árvore de processos (a aplicação é o PID 1 dentro do contêiner e tem outro PID no host).

> [!question]- Como a interface `eth0` de um contêiner se liga à rede do host?
> Por um **par veth**: uma ponta fica no namespace de rede do contêiner (`eth0`) e a outra no host (`vethXXXX`), ligada à bridge `docker0`, que é o gateway dos contêineres.

> [!question]- Que regras de netfilter o Docker cria para `-p 8080:80`?
> Um **DNAT** na chain `DOCKER` da tabela nat (porta 8080 do host → IP do contêiner:80), um **MASQUERADE** para a saída dos contêineres e um **ACCEPT** na tabela filter para o tráfego encaminhado.

> [!question]- Qual é a forma recomendada de instalar o Docker Engine em um servidor Debian ou Ubuntu?
> Pelo repositório oficial `download.docker.com`, com a chave em `/etc/apt/keyrings` e os pacotes `docker-ce`, `docker-ce-cli`, `containerd.io`, `docker-buildx-plugin` e `docker-compose-plugin`. O script `get.docker.com` é só para teste e desenvolvimento.

> [!question]- O que substituiu o Docker Machine?
> Localmente, o Docker Desktop (ou Colima, OrbStack, Rancher Desktop). Para hosts remotos, provisionamento com Terraform/cloud-init, instalação pelo repositório oficial e acesso com `docker context` via SSH.

> [!question]- Para que servem as opções `bip` e `fixed-cidr` do daemon?
> `bip` define o IP e a sub-rede da bridge `docker0`; `fixed-cidr` restringe a faixa de IPs entregue aos contêineres dentro dela. Para as redes criadas pelo usuário, use `default-address-pools`.

> [!question]- O que o `-H fd://` na unit do systemd significa?
> **Socket activation**: o systemd abre o socket e o entrega ao `dockerd`. Por isso, definir `hosts` também no `daemon.json` conflita e impede o daemon de subir.

> [!question]- Como sair de um `docker run -it ubuntu bash` sem parar o contêiner?
> Com **Ctrl+P seguido de Ctrl+Q**. `exit` encerra o bash, que é o PID 1, e para o contêiner. Para voltar, `docker attach` (ao PID 1) ou, melhor, `docker exec -it <c> bash`.

> [!question]- Qual é a diferença entre `docker create` e `docker run`?
> `create` só cria o contêiner (status `Created`); `run` cria e inicia. Um contêiner criado é iniciado com `docker start` (`-ai` para anexar).

### Imagens e Dockerfile

> [!question]- Qual é a diferença entre tag e digest?
> A **tag** é um rótulo móvel que pode apontar para outra imagem amanhã. O **digest** (`sha256:…`) é o hash do manifest: imutável e identifica exatamente o conteúdo.

> [!question]- Para que serve um image index (manifest list)?
> Agrupa um manifest por plataforma (`linux/amd64`, `linux/arm64`…) sob a mesma tag. O cliente baixa automaticamente a variante da sua arquitetura.

> [!question]- Qual é a referência completa de `nginx`?
> `docker.io/library/nginx:latest`.

> [!question]- Quais são os limites de pull do Docker Hub (set/2026)?
> Janela de 6 horas: **100** pulls para usuários não autenticados (por IPv4 ou /64 IPv6), **200** para contas Personal autenticadas e ilimitado para Pro, Team e Business.

> [!question]- Qual é a diferença entre `docker save` e `docker export`?
> `save` exporta **imagens** com camadas, tags e metadados (volta com `load`). `export` exporta o sistema de arquivos achatado de um **contêiner**, sem histórico, `CMD` nem `ENV` (volta com `import`).

> [!question]- Por que se deve copiar `package.json` antes do restante do código?
> Para que a camada de instalação de dependências fique em cache e só seja refeita quando os manifestos mudarem, e não a cada alteração no código.

> [!question]- Por que `RUN apt-get update` sozinho em uma linha é um problema?
> O cache de `RUN` depende só do texto do comando; a camada fica em cache para sempre e um `apt-get install` posterior pode usar índices desatualizados. Junte `update` e `install` no mesmo `RUN`.

> [!question]- Qual é o resultado de `ENTRYPOINT ["app"]` com `CMD ["--port", "80"]` e `docker run img --port 90`?
> `app --port 90`. Os argumentos do `docker run` substituem o `CMD` e são passados ao `ENTRYPOINT`.

> [!question]- Quando usar `ADD` em vez de `COPY`?
> Só para baixar uma URL (de preferência com `--checksum`), clonar um repositório Git ou extrair automaticamente um tarball local. Nos outros casos, `COPY`.

> [!question]- O que o `.dockerignore` evita?
> Enviar arquivos desnecessários ao builder (build lento), invalidar o cache sem motivo e copiar segredos (`.env`, chaves) e `.git` para a imagem com `COPY . .`.

> [!question]- O que é um multi-stage build e qual o principal ganho?
> Um Dockerfile com vários `FROM`: os estágios iniciais compilam e o estágio final copia só o artefato. A imagem final fica sem compiladores, código-fonte nem cache.

> [!question]- Quais são os padrões do `HEALTHCHECK`?
> Intervalo de 30 s, timeout de 30 s, `start-period` de 0 s, `start-interval` de 5 s e 3 tentativas até `unhealthy`.

> [!question]- Qual o risco de usar Alpine como base para qualquer aplicação?
> Alpine usa **musl libc**; binários e bibliotecas nativas compiladas para glibc podem falhar ou ter desempenho pior.

> [!question]- O que são as Docker Hardened Images?
> Imagens base mínimas e endurecidas mantidas pela Docker, sem shell na variante de runtime, rodando como não root, com SBOM e provenance assinados. Gratuitas e Apache 2.0 desde dezembro de 2025.

> [!question]- O que acontece com um arquivo da imagem quando o contêiner o altera pela primeira vez?
> É feito o **copy-up**: o arquivo inteiro é copiado para a camada gravável e alterado lá. Apagar um arquivo da imagem cria um **whiteout** na camada superior, sem liberar espaço na imagem.

> [!question]- O que acontece com `docker build .` sem `-t`?
> A imagem é criada sem nome, como `<none>:<none>`. Dê o nome com `-t repositório:tag` no build ou depois com `docker image tag`.

> [!question]- O `.` em `docker build -t app .` é o caminho do Dockerfile?
> Não: é o **contexto de build** (um diretório). O builder procura o `Dockerfile` na raiz do contexto; para outro arquivo, use `-f`.

> [!question]- Por que o serviço deve rodar em primeiro plano no contêiner?
> Porque o contêiner vive enquanto o PID 1 vive. Um serviço que vai para segundo plano faz o contêiner terminar, e iniciar o serviço à mão com `docker exec` não é reproduzível. Exemplo: `ENTRYPOINT ["apachectl"]` + `CMD ["-D", "FOREGROUND"]`.

> [!question]- Por que evitar `docker commit` para criar imagens de produção?
> Não há receita reproduzível: a imagem carrega a sujeira da sessão, não tem revisão nem cache de build, e refazê-la com uma base nova exige repetir tudo à mão. O Dockerfile resolve todos esses pontos.

> [!question]- Qual é o formato de nome necessário para enviar uma imagem ao Docker Hub?
> `usuário-ou-organização/repositório:tag`, por exemplo `minhaconta/apache:1.0`. Sem namespace, o push tenta o namespace `library`, reservado às imagens oficiais.

> [!question]- Como subir um registry local e enviar uma imagem a ele?
> `docker run -d -p 5000:5000 -v registry-dados:/var/lib/registry registry:3`, depois `docker tag app:1.0 localhost:5000/app:1.0` e `docker push localhost:5000/app:1.0`.

### BuildKit e Buildx

> [!question]- Como passar um token a um `RUN` sem deixá-lo na imagem?
> `RUN --mount=type=secret,id=token …` no Dockerfile e `docker build --secret id=token,src=arquivo .` (ou `env=VAR`). O segredo fica disponível só durante aquele `RUN`, em `/run/secrets/token`.

> [!question]- Para que serve `RUN --mount=type=cache`?
> Mantém o cache do gerenciador de pacotes (npm, pip, Go, Maven, apt) entre builds sem gravá-lo na imagem.

> [!question]- Qual é a diferença entre `mode=min` e `mode=max` no cache exportado?
> `min` exporta só as camadas da imagem final; `max` exporta também as camadas dos estágios intermediários, o que acelera builds multi-stage no CI.

> [!question]- Quais são as três estratégias de build multiplataforma?
> Emulação **QEMU** (simples e lenta), **nós nativos** de cada arquitetura (rápida, exige infraestrutura) e **compilação cruzada** com `$BUILDPLATFORM` e `$TARGETARCH` (rápida, depende da linguagem).

> [!question]- O que causa `exec format error`?
> Executar uma imagem (ou binário) de outra arquitetura de CPU, por exemplo `arm64` em um host `amd64` sem emulação.

> [!question]- Com o driver `docker-container`, por que a imagem não aparece em `docker image ls`?
> Porque o resultado fica no cache do builder. É preciso `--load` (carregar no image store local) ou `--push` (enviar ao registry).

> [!question]- O que o Compose v5 mudou no build?
> Removeu o builder interno e passou a delegar os builds ao **Docker Bake**.

> [!question]- O que são SBOM e provenance?
> **SBOM** é o inventário de pacotes da imagem. **Provenance** registra como, onde e a partir de qual código a imagem foi construída (SLSA). Ambos são anexados com `--sbom=true` e `--provenance=mode=max`.

### Redes e armazenamento

> [!question]- Por que usar uma rede bridge definida pelo usuário em vez da bridge padrão?
> Porque ela tem **DNS embutido** (contêineres se encontram pelo nome), isola os contêineres de outras redes e permite conectar e desconectar em execução.

> [!question]- Qual é o endereço do DNS embutido do Docker dentro do contêiner?
> `127.0.0.11`.

> [!question]- Um contêiner responde internamente, mas não pela porta publicada. Qual a causa mais comum?
> A aplicação está escutando em `127.0.0.1` dentro do contêiner. Ela precisa escutar em `0.0.0.0`.

> [!question]- Por que uma porta publicada fica acessível mesmo com o UFW bloqueando?
> As regras de iptables do Docker são avaliadas antes das regras do UFW. Restrinja com bind em `127.0.0.1` ou regras na chain `DOCKER-USER`.

> [!question]- Como um contêiner no Linux acessa um serviço do host?
> Com `--add-host=host.docker.internal:host-gateway` e o endereço `host.docker.internal` (no Docker Desktop o nome já existe). `localhost` aponta para o próprio contêiner.

> [!question]- Quais portas precisam estar abertas entre os nós de um Swarm?
> **2377/tcp** (gerenciamento), **7946/tcp e udp** (descoberta entre nós) e **4789/udp** (tráfego da overlay, VXLAN).

> [!question]- Qual é a diferença entre volume nomeado e bind mount?
> O volume é gerenciado pelo Docker, fica na área de dados do daemon e é pré-populado com o conteúdo da imagem. O bind mount aponta para um caminho qualquer do host e esconde o conteúdo da imagem naquele diretório.

> [!question]- Por que `-v ./config.yaml:/app/config.yaml` pode criar um diretório no host?
> Com `-v`, se o caminho de origem não existir, o Docker cria um **diretório** vazio. Com `--mount`, o comando falha com erro claro.

> [!question]- O que acontece com volumes anônimos em um `docker run --rm`?
> São removidos junto com o contêiner. Volumes nomeados são preservados.

> [!question]- Como fazer backup de um volume?
> Com um contêiner temporário que monta o volume e um diretório do host: `docker run --rm -v dados:/d -v "$(pwd)":/b alpine tar czf /b/dados.tgz -C /d .`. Para bancos, prefira a ferramenta de backup do próprio banco.

> [!question]- Quais storage drivers foram removidos do Docker e qual é o padrão hoje?
> AUFS e `overlay` (Engine 24) e devicemapper (Engine 25). O padrão é `overlay2` no store clássico e os **containerd snapshotters** em instalações novas do Engine 29.

> [!question]- O que foi o data-only container e o que o substituiu?
> Um contêiner que nunca rodava, só para guardar volumes, montados em outros com `--volumes-from`. Foi substituído pelos **volumes nomeados** (`docker volume create`).

> [!question]- Duas instâncias de PostgreSQL podem usar o mesmo volume de dados?
> Não. Cada instância supõe acesso exclusivo aos arquivos; isso impede a inicialização ou corrompe os dados. Use volumes separados e a replicação do banco.

> [!question]- Como descobrir onde um volume fica no host?
> `docker volume inspect --format '{{ .Mountpoint }}' <volume>`. No Linux, `/var/lib/docker/volumes/<volume>/_data`; no Docker Desktop, o caminho fica dentro da VM.

### Compose

> [!question]- Qual é a ordem de precedência do nome do projeto no Compose?
> Flag `-p`, depois `COMPOSE_PROJECT_NAME`, depois o atributo `name:` do arquivo e, por fim, o nome do diretório.

> [!question]- Quais são as condições do `depends_on`?
> `service_started` (padrão), `service_healthy` (espera o healthcheck) e `service_completed_successfully` (espera sair com código 0).

> [!question]- Qual é a diferença entre o arquivo `.env` e o atributo `env_file`?
> O `.env` alimenta a **interpolação** de `${VAR}` no arquivo Compose. O `env_file` define variáveis **dentro do contêiner**.

> [!question]- Qual é a precedência de variáveis de ambiente dentro de um contêiner do Compose?
> `docker compose run -e` > `environment` > `env_file` > `ENV` da imagem.

> [!question]- O que `docker compose down -v` faz a mais que `down`?
> Remove também os volumes nomeados declarados no projeto e os anônimos, apagando os dados.

> [!question]- Onde os `secrets` do Compose aparecem no contêiner?
> Como arquivos em `/run/secrets/<nome>`.

> [!question]- Para que servem os `profiles`?
> Serviços com perfil só sobem quando o perfil é ativado (`--profile` ou `COMPOSE_PROFILES`); serviços sem perfil sobem sempre.

> [!question]- Quais são as ações do `develop.watch`?
> `sync` (copia arquivos), `rebuild` (reconstrói e recria), `sync+restart` (copia e reinicia) e `sync+exec` (copia e executa um comando).

> [!question]- Qual comando mostra o Compose resolvido, com variáveis e arquivos mesclados?
> `docker compose config`.

> [!question]- O campo `version:` ainda é necessário no `compose.yaml`?
> Não. É obsoleto, só gera aviso; o Compose sempre valida com o schema mais recente.

### Segurança e operação

> [!question]- Quantas capabilities o Docker concede por padrão e como reduzi-las?
> **14** (como `CHOWN`, `NET_BIND_SERVICE`, `NET_RAW`, `SETUID`). Reduza com `--cap-drop ALL` e adicione só o necessário com `--cap-add`.

> [!question]- O que `--privileged` faz?
> Concede todas as capabilities, acesso a todos os dispositivos do host e desliga seccomp e AppArmor. Na prática, remove o isolamento.

> [!question]- Qual é a diferença entre o modo rootless e o `userns-remap`?
> No **rootless**, o daemon e os contêineres rodam como usuário comum. No **`userns-remap`**, o daemon continua root, mas o root do contêiner é mapeado para um UID sem privilégio no host.

> [!question]- Por que variáveis de ambiente não são o melhor lugar para segredos?
> Aparecem em `docker inspect`, em `/proc/<pid>/environ`, em dumps e logs de erro, e são herdadas por processos filhos. Segredos em arquivo (`/run/secrets`) ou em cofre são mais seguros.

> [!question]- O que substituiu o Docker Content Trust para assinar imagens?
> Sigstore/**cosign** (inclusive assinatura keyless com OIDC) e **Notation**. O DCT (Notary v1) foi aposentado.

> [!question]- O que acontece quando um contêiner ultrapassa `--memory`?
> O kernel mata o processo por OOM; o contêiner sai com código **137** e `OOMKilled: true`.

> [!question]- Qual é a diferença entre `--cpus` e `--cpu-shares`?
> `--cpus` é um **limite** de tempo de CPU. `--cpu-shares` é um **peso relativo** (padrão 1024) que só vale quando há disputa.

> [!question]- Qual driver de log faz rotação por padrão?
> O `local` (20 MB × 5 arquivos). O `json-file`, padrão do Docker, **não** faz rotação a menos que `max-size` e `max-file` sejam definidos.

> [!question]- Qual é o tamanho padrão do `/dev/shm` e quando aumentá-lo?
> **64 MB**. Aumente com `--shm-size` para navegadores headless e alguns bancos de dados.

### Orquestração e produção

> [!question]- Quantas falhas um Swarm com 5 managers tolera?
> **2**. A fórmula é (N − 1) / 2.

> [!question]- O que acontece com um Swarm que perde o quórum?
> As tarefas existentes continuam rodando, mas não é possível alterar o cluster. A recuperação é `docker swarm init --force-new-cluster` em um manager sobrevivente.

> [!question]- Qual é a diferença entre serviços replicated e global no Swarm?
> **Replicated** mantém um número fixo de réplicas; **global** roda exatamente uma tarefa em cada nó elegível.

> [!question]- O que é o routing mesh?
> A rede `ingress` do Swarm que publica a porta de um serviço em **todos os nós** e encaminha para uma tarefa saudável, mesmo em nós sem réplica.

> [!question]- Como colocar um nó do Swarm em manutenção?
> `docker node update --availability drain <nó>`: as tarefas são movidas para outros nós e o nó deixa de receber novas.

> [!question]- O Kubernetes usa o `HEALTHCHECK` da imagem?
> Não. Ele usa `livenessProbe`, `readinessProbe` e `startupProbe` definidos no manifest.

> [!question]- Por que promover o mesmo digest entre ambientes em vez de reconstruir?
> Porque garante que o artefato testado é exatamente o que vai para produção; um rebuild pode trazer dependências ou bases diferentes.

> [!question]- Qual é o risco de montar o `docker.sock` em um job de CI?
> O job ganha controle total do daemon, e portanto root no host, além de ver os contêineres de outros jobs.

> [!question]- Quando o Docker Desktop exige assinatura paga?
> Para uso profissional em empresas com 250 funcionários ou mais, **ou** com receita anual de US$ 10 milhões ou mais, e para órgãos de governo.

> [!question]- Em quais nós é possível executar comandos de administração do Swarm?
> Em **qualquer manager** (`Leader` ou `Reachable`); o pedido é encaminhado ao líder. Workers não aceitam comandos de cluster.

> [!question]- Como remover um manager do Swarm com segurança?
> Rebaixá-lo com `docker node demote`, depois `docker swarm leave` no próprio nó e `docker node rm` em um manager. Um manager saindo sem ser rebaixado exige `--force` e pode quebrar o quórum.

> [!question]- Um volume montado em um serviço com 5 réplicas é compartilhado entre os nós?
> Não, com o driver `local`: cada nó cria o próprio volume. Réplicas em nós diferentes veem dados diferentes. Para compartilhar, use um driver de rede (NFS, plugin) ou um serviço de dados externo.

> [!question]- O que é o VIP de um serviço do Swarm?
> Um IP virtual na rede do serviço; conexões a ele (ou ao nome do serviço) são balanceadas entre as tarefas. Aparece em `Endpoint.VirtualIPs` no `docker service inspect`.

> [!question]- Como rotacionar um secret usado por um serviço?
> Criar um secret novo, `docker service update --secret-rm antigo --secret-add source=novo,target=<mesmo-nome> <serviço>` e depois `docker secret rm antigo`. Secrets são imutáveis.

> [!question]- Qual é o tamanho máximo de um Docker secret e onde ele aparece no contêiner?
> **500 KB**. Aparece como arquivo em `/run/secrets/<nome>` (ou no `target` definido), montado em tmpfs.

> [!question]- Qual é a diferença entre `docker compose up` e `docker stack deploy`?
> Os dois usam arquivos Compose. `docker compose` roda os serviços em **um host**; `docker stack deploy` os cria como **serviços do Swarm** no cluster, usando a seção `deploy` e ignorando `build` e `depends_on`.

> [!question]- Como atualizar um stack já implantado?
> Rodando de novo `docker stack deploy -c arquivo.yaml <stack>`. O Swarm aplica rolling update só no que mudou; `--prune` remove serviços que saíram do arquivo.

> [!question]- Por que node-exporter e cAdvisor rodam em modo `global`?
> Porque precisam coletar métricas de **todos os nós**, inclusive dos que entrarem depois; o modo `global` garante uma tarefa por nó.

### Certificação DCA

> [!question]- Como é o formato da prova do DCA?
> **55 questões em 90 minutos**: 13 de múltipla escolha tradicional e 42 **DOMC**, em que as alternativas aparecem uma de cada vez e você responde sim ou não, sem voltar. A nota de aprovação não é divulgada.

> [!question]- Quais são os domínios do DCA e seus pesos?
> Orquestração **25%**, imagens e registry **20%**, instalação e configuração **15%**, redes **15%**, segurança **15%**, armazenamento e volumes **10%**.

> [!question]- Quais são os três objetos do Container Network Model?
> **Sandbox** (a pilha de rede isolada do contêiner, um namespace de rede), **endpoint** (a ligação do sandbox a uma rede, um par veth) e **network** (o grupo de endpoints que se comunicam). Os drivers são de dois tipos: de **rede** e de **IPAM**.

> [!question]- Qual é a diferença entre publicar uma porta de serviço em modo `ingress` e em modo `host`?
> `ingress` (padrão) abre a porta em **todos os nós** e balanceia pelo routing mesh, perdendo o IP do cliente. `host` abre a porta **só no nó da tarefa**, preserva o IP do cliente e permite uma tarefa por nó para aquela porta.

> [!question]- Quais flags do `docker service create` aceitam templates, e com quais placeholders?
> `--hostname`, `--mount` e `--env`. Placeholders: `.Service.ID/Name/Labels`, `.Node.ID/Hostname` e `.Task.ID/Name/Slot`.

> [!question]- Uma tarefa fica em `Pending` com `no suitable node`. O que investigar?
> Os **constraints** do serviço (rótulo ou papel que nenhum nó tem), as **reservas** de CPU e memória, portas em `mode=host` e a disponibilidade dos nós (`drain`, `Down`). `docker service ps --no-trunc` mostra a mensagem completa.

> [!question]- Os workers não conseguem baixar a imagem privada de um serviço. Qual é a correção?
> Criar ou atualizar o serviço com **`--with-registry-auth`**, que repassa as credenciais do cliente aos nós.

> [!question]- Como o Swarm protege a comunicação entre os nós?
> Com **TLS mútuo**, usando certificados emitidos pela **CA embutida** no primeiro manager e renovados automaticamente a cada **90 dias** (`--cert-expiry`). `docker swarm ca --rotate` troca a CA raiz.

> [!question]- O que o token de entrada do Swarm contém?
> O **digest do certificado da CA raiz** e um **segredo** aleatório. O digest permite ao nó conferir que está entrando no cluster certo; o segredo define o papel (worker ou manager).

> [!question]- Como fazer backup do estado de um Swarm?
> Em um manager que não seja essencial ao quórum: guardar a chave de desbloqueio (se houver autolock), **parar o Docker**, copiar **`/var/lib/docker/swarm`** e iniciar o Docker de novo. Na restauração, usar `docker swarm init --force-new-cluster`.

> [!question]- Como fazer o Engine confiar em um registry com certificado de uma CA interna?
> Colocar a CA em **`/etc/docker/certs.d/<host:porta>/ca.crt`**. Para TLS mútuo, acrescentar `client.cert` e `client.key` no mesmo diretório.

> [!question]- Por que o certificado de cliente do registry precisa ter a extensão `.cert`, e não `.crt`?
> Porque o daemon trata arquivos **`.crt` como CAs** e **`.cert` como certificados de cliente**.

> [!question]- Como apagar uma imagem de um registry Distribution e liberar espaço?
> Com `delete` habilitado no registry, apagar o **manifest pelo digest** pela API (`DELETE /v2/<nome>/manifests/<digest>`) e depois rodar **`registry garbage-collect`** com o registry parado ou somente leitura.

> [!question]- Como ligar o Docker Content Trust e assinar uma imagem?
> `export DOCKER_CONTENT_TRUST=1` e `docker push` (ou `docker trust sign <imagem:tag>`). Com a variável ligada, `pull` e `run` recusam tags sem assinatura. O DCT foi aposentado; hoje se usa cosign ou Notation.

> [!question]- Qual chave do Docker Content Trust deve ficar offline?
> A **chave root**, que cria as chaves de repositório. Sem ela não há recuperação; as chaves de repositório assinam as tags e as de delegação identificam os signatários.

> [!question]- Qual é a diferença entre `loop-lvm` e `direct-lvm` no devicemapper?
> `loop-lvm` (padrão) usa **arquivos esparsos** como dispositivos de loopback e serve só para testes. `direct-lvm` usa um **dispositivo de bloco dedicado** com thin pool do LVM e é o modo de produção (`dm.directlvm_device`). O devicemapper foi removido no Engine 25.

> [!question]- Qual storage driver os contêineres Windows usam?
> **`windowsfilter`**.

> [!question]- Armazenamento de objetos ou de blocos para um registry com várias réplicas?
> **Objetos** (S3, Azure Blob, GCS): todas as réplicas leem e gravam o mesmo bucket, com escala e durabilidade. Blocos servem melhor a bancos de dados em um nó.

> [!question]- Onde ficam as camadas de uma imagem com o driver `overlay2`?
> Em `/var/lib/docker/overlay2/<id>/diff`, uma pasta por camada. O contêiner tem `LowerDir` (camadas da imagem), `UpperDir` (camada gravável) e `MergedDir` (visão unificada), vistos em `docker inspect -f '{{json .GraphDriver.Data}}'`.

> [!question]- O que são UCP e DTR, e como se chamam hoje?
> **Universal Control Plane** (gerenciamento web e API de clusters Swarm e Kubernetes, com RBAC e LDAP) e **Docker Trusted Registry** (registry privado com scan e assinatura). Hoje são o **Mirantis Kubernetes Engine (MKE)** e o **Mirantis Secure Registry (MSR)**.

> [!question]- O que forma um grant no RBAC do UCP?
> **Sujeito** (usuário, time, organização ou service account) + **papel** (None, View Only, Restricted Control, Scheduler, Full Control ou personalizado) + **conjunto de recursos** (coleção no Swarm ou namespace no Kubernetes).

> [!question]- O que é um client bundle do UCP?
> Um zip com o **certificado de cliente do usuário** e scripts (`env.sh`) que apontam `DOCKER_HOST`, `DOCKER_TLS_VERIFY`, `DOCKER_CERT_PATH` e `KUBECONFIG` para o UCP. Os comandos passam pelo UCP e respeitam o RBAC do usuário.

> [!question]- Qual é a ordem de backup e restauração do Docker Enterprise, e o que o backup do DTR não inclui?
> **Swarm → UCP → DTR**. O backup do DTR tem só **metadados**: as imagens ficam no armazenamento, que precisa de backup próprio.

> [!question]- Qual é a diferença entre o routing mesh e o Interlock?
> O routing mesh é **L4**: encaminha portas TCP/UDP para qualquer tarefa. O Interlock é **L7**: roteia HTTP/HTTPS por nome de host (`com.docker.lb.hosts`) e termina TLS.

> [!question]- Qual é a diferença entre um Service `ClusterIP` e um `NodePort` no Kubernetes?
> `ClusterIP` (padrão) dá um IP virtual e um nome DNS **internos** ao cluster. `NodePort` acrescenta uma porta na faixa **30000–32767** aberta em **todos os nós**, para acesso de fora.

> [!question]- Como ConfigMaps e Secrets chegam a um Pod?
> Como **variáveis de ambiente** (`envFrom`, `valueFrom`) ou como **arquivos** em um volume. Secrets são só codificados em base64 por padrão; cifrá-los em repouso exige configuração.

> [!question]- Qual é a relação entre CSI, StorageClass, PVC e PV?
> O **driver CSI** implementa o armazenamento; a **StorageClass** aponta para ele e define parâmetros; a aplicação cria um **PVC** citando a StorageClass; o driver provisiona um **PV** e o liga ao PVC, que o Pod monta como volume.

> [!question]- Qual é o modelo de rede do Kubernetes?
> Cada Pod tem um **IP próprio**, e todos os Pods se falam **sem NAT**, em qualquer nó. Contêineres do mesmo Pod usam `localhost`. Quem implementa é um plugin **CNI** (não o CNM do Docker).
