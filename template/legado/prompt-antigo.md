# Converter material de estudo (.md) em e-book HTML e PDF

## Objetivo e entrega

Transforme o conteúdo Markdown fornecido em um **e-book de estudo** para leitura contínua e consulta posterior. Entregue um HTML e um PDF com nomes derivados do título ou assunto, sem usar nomes, marcas ou caminhos fixos de projetos anteriores. Se o ambiente permitir, publique também uma prévia do HTML como artifact, sem substituir os arquivos entregues.

Se houver um gerador de PDF no projeto, use-o com os caminhos de entrada e saída adequados. Caso contrário, exporte o HTML para PDF com um navegador que respeite o CSS de impressão. Se não for possível gerar o PDF no ambiente disponível, entregue o HTML e explique o impedimento.

Se o bloco `<conteudo>` estiver vazio ou ainda contiver o marcador de exemplo, peça o material antes de começar. Não produza conteúdo a partir do marcador.

## Regras de conteúdo (prioridade máxima)

1. **Preserve o original:** mantenha todas as informações, perguntas, respostas, referências e links do material, na mesma ordem. Não resuma nem elimine trechos do original. O trabalho principal é de diagramação.
2. **Faça apenas ajustes editoriais mínimos no original:** corrija erros evidentes de digitação e divida parágrafos longos sem mudar o sentido. Se encontrar um possível erro técnico ou uma afirmação ambígua, preserve o texto e avise na resposta; não corrija o conteúdo por conta própria.
3. **Separe o material original dos acréscimos de estudo:** perguntas criadas para o e-book e o resumo final são permitidos, mas devem apenas reorganizar ou perguntar sobre informações expressas no material. Identifique as perguntas criadas como “Perguntas de revisão elaboradas a partir do material” e o resumo como “Síntese de revisão”. Não acrescente fatos, exemplos técnicos ou conclusões sem apoio no original.
4. **Use português do Brasil**, mantendo os termos técnicos em inglês quando o original os utilizar.
5. **Não invente metadados:** título, subtítulo, curso, módulo, autor e data só devem aparecer na capa se estiverem presentes ou puderem ser descritos diretamente a partir do material. Omita os campos ausentes.

## Estrutura do e-book

Na ordem:

1. **Capa:** apresente apenas os elementos disponíveis: categoria, título, subtítulo e metadados. Dê destaque ao assunto do material; não use texto de preenchimento.
2. **Sumário:** coloque-o após a capa, com links âncora para todas as seções numeradas. Em materiais longos, agrupe as seções pelos capítulos ou títulos principais do original em controles expansíveis na tela e mostre o sumário completo na impressão.
3. **Seções:** preserve títulos, hierarquia e numeração do original (1.1, 1.2...). Se não houver numeração, numere os títulos na ordem em que aparecem. Mostre o número em um rótulo pequeno monoespaçado.
4. **Perguntas de fixação:** mantenha cada pergunta original no ponto em que aparece e preserve seu formato, inclusive verdadeiro/falso, múltipla seleção ou outra quantidade de alternativas. Se o material não tiver perguntas, crie de 3 a 5 perguntas baseadas somente nele, depois das seções de conteúdo, e identifique-as como elaboradas para revisão. Use `<details>` para mostrar a resposta e uma explicação curta quando ambas puderem ser fundamentadas no material. Não apresente um gabarito como oficial quando o original não o fornecer; se houver uma resposta dedutível com segurança, identifique-a como inferida. Se não for possível fundamentar a resposta, informe que o material não fornece gabarito.
5. **Síntese de revisão:** encerre o e-book com um bloco destacado que reúna os pontos centrais já expressos no material. Não substitua os resumos originais por esse bloco.

## Qual componente usar para cada tipo de conteúdo

Escolha o componente pelo formato do conteúdo, não para variar o visual. Texto corrido continua como parágrafo.

| Conteúdo no original | Componente |
| --- | --- |
| Definição-chave ou citação oficial | Blockquote em destaque |
| Aviso, dica, “importante”, “atenção” | Callout (caixa com ícone ou rótulo) |
| Lista de itens paralelos com descrição (categorias, componentes, serviços) | Cards em grid |
| Eventos com data ou sequência cronológica | Linha do tempo vertical |
| Dados com colunas ou comparações | Tabela estilizada |
| Lista curta de termos soltos (tags, siglas, nomes) | Chips/badges |
| Passo a passo | Lista numerada com marcadores destacados |

## Visual e acessibilidade

- **Arquivo:** mantenha HTML e CSS no mesmo arquivo, com o CSS no `<head>`. Não dependa de fontes ou scripts externos para que o conteúdo seja legível. Use JavaScript local apenas quando necessário para interações ou impressão.
- **Direção visual:** derive a capa, a paleta e os detalhes gráficos do assunto e do público do material. Prefira uma base clara para leitura e impressão; se outra abordagem for mais adequada, preserve a legibilidade. Não reutilize automaticamente a identidade visual de um e-book anterior.
- **Paleta:** escolha cores relacionadas ao tema e use os destaques com moderação. Garanta contraste mínimo AA para texto e controles.
- **Tipografia:** escolha fontes adequadas ao assunto, com hierarquia clara entre títulos, corpo e rótulos. Fontes externas são opcionais; inclua sempre alternativas locais para leitura sem rede.
- **Hierarquia:** bordas, raios e sombras devem indicar a importância dos elementos. Evite transformar parágrafos em cards apenas por decoração.
- **Leitura:** mantenha linhas de aproximadamente 65–75 caracteres, espaçamento confortável e quebras de palavras naturais.
- **Responsivo:** verifique a leitura em largura de celular. Cards devem caber em uma coluna quando necessário e tabelas devem rolar horizontalmente sem alargar a página.
- **Teclado e semântica:** use `<article>`, `<nav>`, `<section>` e níveis de título em ordem lógica; marque o foco dos links e controles com `:focus-visible`; use rótulos compreensíveis em `<details>`.
- **Movimento:** se houver animações, respeite `prefers-reduced-motion`.

## Impressão e PDF

- Inclua `@page` e `@media print` com margens, numeração de páginas e regras para evitar quebras dentro de cards, perguntas e linhas de tabela quando couberem na página. Use A4 por padrão, salvo indicação de outro formato.
- Na impressão, mostre o conteúdo dos `<details>` e todas as seções do sumário. Se CSS não bastar em todos os navegadores, use um JavaScript pequeno para abrir os `<details>` em `beforeprint` e restaurar o estado em `afterprint`.
- Gere o PDF a partir do HTML com uma ferramenta que respeite o CSS de impressão. Não substitua o PDF por uma captura de tela ou por uma renderização que ignore essas regras.

## Conferência antes de entregar

1. Compare o Markdown e o HTML seção por seção. Confirme que nenhum trecho, pergunta, resposta, referência ou link foi omitido ou alterado indevidamente.
2. Confira a hierarquia dos títulos, a numeração, a ausência de IDs duplicados e todos os destinos dos links do sumário.
3. Confira cada pergunta e seu gabarito ou indicação de inferência; não deixe respostas sem fundamento nem apresente inferências como respostas oficiais.
4. Inspecione o HTML em uma largura de celular e uma de desktop. Verifique navegação por teclado, foco visível e tabelas longas.
5. Gere o PDF e inspecione visualmente a capa, o sumário, páginas com tabelas ou perguntas longas e a última página. Confira respostas visíveis, margens, numeração e ausência de cortes ou páginas em branco inesperadas.

Na resposta final, forneça os links para o HTML e o PDF gerados, além de uma lista curta de possíveis erros ou ambiguidades encontrados no material original. Se alguma etapa de validação falhar, informe o que não foi possível verificar.

---

<conteudo>
[COLE O MARKDOWN AQUI]
</conteudo>
