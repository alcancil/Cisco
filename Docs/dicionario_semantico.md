# 📖 Dicionário Semântico

Este guia estabelece os padrões de nomenclatura para ativos deste repositório. A adoção destes padrões garante a escalabilidade do projeto, a compatibilidade com ferramentas de automação (NetDevOps) e a integridade dos links no GitHub.

## 🎯 Padrões de Nomenclatura

### 1. Pastas (Diretórios)

Utilizamos o padrão **kebab-case** (letras minúsculas separadas por hífen).

- **Regra:** `[prefixo]-[nome-do-tema]`
- **Prefixos Operacionais:**
  - `lab-`: Para laboratórios práticos (Substitui o termo "Exemplo Prático").
  - `study-`: Para anotações teóricas e resumos de capítulos.
  - `asset-`: Para recursos de suporte como diagramas, ícones ou documentos auxiliares.

*Exemplo:* Em vez de `01 - Exemplo Prático OSPF`, utilizamos `01-lab-ospf-area-zero`.

### 2. Arquivos

- **Documentação (Markdown):** Letras minúsculas e hífens. (*Ex: resumo-bgp-attributes.md*)
- **Scripts (Python):** Devem seguir o padrão **snake_case**. (*Ex: task_backup_ios.py*)
- **Arquivos de Configuração:** `[hostname].cfg` ou `[hostname].txt`.

## 🚫 O que evitar

- **Espaços em branco:** Quebram a execução de scripts e dificultam a navegação via CLI.
- **Acentos e Caracteres Especiais:** Podem causar erros de *encoding* em diferentes sistemas de arquivos (Windows vs. Linux).

---

## 🔗 Referências e Metodologia

A padronização deste repositório foi fundamentada nas seguintes normas e guias de estilo da indústria:

### 1. Interoperabilidade de Sistemas

- **Norma:** [POSIX Compliance (IEEE Std 1003.1)](https://standards.ieee.org/ieee/1003.1/7700/)
- **Aplicação:** O uso de caracteres alfanuméricos simples e a substituição de espaços por hífens garante que o repositório seja totalmente compatível com ambientes POSIX (Linux/Unix), onde ferramentas como **Ansible, Terraform e scripts Python** operam nativamente.

### 2. Consistência e Legibilidade

- **Guia:** [Google Open Source Style Guides](https://google.github.io/styleguide/)
- **Aplicação:** Adotamos a filosofia de "escaneabilidade" do Google, onde a nomenclatura deve ser intuitiva e consistente, permitindo que colaboradores ou recrutadores compreendam a estrutura do projeto em segundos.

### 3. Integridade de Endereçamento Web

- **Norma:** [RFC 3986 (URI Generic Syntax)](https://datatracker.ietf.org/doc/html/rfc3986)
- **Aplicação:** Como o GitHub é uma plataforma web, os nomes de pastas tornam-se parte de uma URL. O padrão **kebab-case** evita a geração de caracteres de escape (como `%20` para espaços), resultando em links mais limpos e seguros.

### 4. Semântica e Intencionalidade

- **Conceito:** [Clean Code (Robert C. Martin)](https://www.amazon.com.br/C%C3%B3digo-limpo-Habilidades-pr%C3%A1ticas-Software/dp/8576082675)
- **Aplicação:** Aplicamos o princípio de que nomes de arquivos devem ser "reveladores de intenção". O nome do arquivo deve explicar sua função sem a necessidade de comentários adicionais.

---

*Última atualização: Março de 2026*