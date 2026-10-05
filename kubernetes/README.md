# Guia de estudo Kubernetes

- `material.md`: fonte do conteúdo, com 21 capítulos em cinco blocos: fundamentos (runtimes, OCI e CRI, arquitetura, kubectl e clusters locais), workloads e cluster (Pods, Deployments e ReplicaSets, DaemonSets e probes, kubeadm), dados, rede e configuração (volumes e CSI, Services e DNS, StatefulSets, ConfigMaps, Secrets e External Secrets, Ingress, Gateway API e cert-manager), operação e segurança (Metrics Server e HPA, taints, tolerations e afinidade, políticas de admissão e Kyverno, Network Policies, RBAC) e Helm e revisão (Helm 4, pegadinhas e informações desatualizadas, referência de comandos e flashcards). Cada capítulo de conteúdo termina com uma tabela de decisão rápida.
- O conteúdo foi escrito a partir do roteiro de estudos do treinamento "Descomplicando Kubernetes" (LINUXtips), usado apenas como base de temas, e conferido na documentação oficial em setembro de 2026: Kubernetes 1.37, kind 0.33, cert-manager 1.21, Kyverno 1.19, Helm 4, aposentadoria do ingress-nginx (março de 2026), pkgs.k8s.io, drivers CSI e EndpointSlices.
- `ebook.toml`: capa, síntese, rodapé e nome do PDF.
- `ebook.html`: gerado por [`ferramentas/gerar_ebook.py`](../ferramentas/gerar_ebook.py); edite o Markdown ou o `ebook.toml`, nunca este arquivo.
- [`PDF-Geral/kubernetes-guia-de-estudo.pdf`](../PDF-Geral/kubernetes-guia-de-estudo.pdf): versão para impressão (A4).

Para regenerar o HTML e o PDF, a partir da raiz: `python3 ferramentas/gerar_todos.py --apenas kubernetes`. Os outros comandos estão no [README da raiz](../README.md#gerar-os-e-books). O visual segue o padrão do repositório, descrito em [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
