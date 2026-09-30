# Guia de estudo Kubernetes

- `material.md`: fonte do conteúdo, com 21 capítulos em cinco blocos: fundamentos (runtimes, OCI e CRI, arquitetura, kubectl e clusters locais), workloads e cluster (Pods, Deployments e ReplicaSets, DaemonSets e probes, kubeadm), dados, rede e configuração (volumes e CSI, Services e DNS, StatefulSets, ConfigMaps, Secrets e External Secrets, Ingress, Gateway API e cert-manager), operação e segurança (Metrics Server e HPA, taints, tolerations e afinidade, políticas de admissão e Kyverno, Network Policies, RBAC) e Helm e revisão (Helm 4, pegadinhas e informações desatualizadas, referência de comandos e flashcards). Cada capítulo de conteúdo termina com uma tabela de decisão rápida.
- O conteúdo foi escrito a partir do roteiro de estudos do treinamento "Descomplicando Kubernetes" (LINUXtips), usado apenas como base de temas, e conferido na documentação oficial em setembro de 2026: Kubernetes 1.37, kind 0.33, cert-manager 1.21, Kyverno 1.19, Helm 4, aposentadoria do ingress-nginx (março de 2026), pkgs.k8s.io, drivers CSI e EndpointSlices.
- `gerar_ebook.py`: converte o Markdown em `ebook.html`. Os títulos `##` viram capítulos, `###` seções e `####` tópicos; a numeração (1, 1.1, 1.1.1) é gerada pelo script. Os callouts `> [!question]-` viram flashcards.
- `ebook.html`: gerado pelo script; não edite à mão.
- `output/pdf/kubernetes-guia-de-estudo.pdf`: versão para impressão (A4).

```bash
python3 -m pip install markdown-it-py beautifulsoup4 pymupdf
python3 gerar_ebook.py
python3 gerar_pdf.py
```

Ou, para todos os e-books de uma vez, `python3 gerar-all-pdfs.py` na raiz (os PDFs vão para `PDF-Geral/`). Os scripts são cópias adaptadas dos do [`Docker`](../Docker/). O visual segue [`../template/DESIGN-SYSTEM.md`](../template/DESIGN-SYSTEM.md).
