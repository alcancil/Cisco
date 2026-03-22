# 📌 Guia de Versionamento Semântico

Este projeto utiliza [Versionamento Semântico](https://semver.org/lang/pt-BR/) (SemVer).

---

## 🎯 Formato da Versão

```
MAJOR.MINOR.PATCH
  ↑     ↑     ↑
  1     2     3
```

### **MAJOR** (primeiro número)

Incrementa quando ocorre uma **mudança estrutural incompatível** no repositório — algo que reorganiza completamente a forma como o conteúdo está organizado, ou que marca um marco de carreira definitivo.

**Exemplos neste repositório:**

- 🏆 Aprovação em um exame de certificação (CCNP ENCOR, ENARSI, etc.)
- 🔄 Reestruturação completa da arquitetura do repositório
- 🚨 Mudança de trilha de certificação (ex: Enterprise → Security)
- 💥 Renomeação ou reorganização de pastas que quebra todos os links existentes

```bash
0.9.0 → 1.0.0  # Aprovação no exame CCNP ENCOR 350-401
1.5.0 → 2.0.0  # Aprovação no exame CCNP ENARSI 300-410
```

---

### **MINOR** (segundo número)

Incrementa quando um **novo bloco de conteúdo** é adicionado ao repositório, mantendo compatibilidade com o que já existe.

**Exemplos neste repositório:**

- ✨ Conclusão de um domínio inteiro do ENCOR (ex: todos os labs de Architecture)
- 📂 Adição de uma nova certificação ao repositório (ex: pasta ENARSI/)
- 🐍 Adição de um novo módulo Python integrado aos estudos
- 📊 Novo script de automação ou ferramenta de progresso funcional
- 📚 Adição de uma nova seção estrutural (ex: study-interview-prep/)

```bash
0.3.0 → 0.4.0  # Concluiu os labs do domínio 01 - Architecture
0.4.0 → 0.5.0  # Concluiu os labs do domínio 03 - Infrastructure
0.5.0 → 0.6.0  # Adicionou pasta e estrutura do ENARSI
```

---

### **PATCH** (terceiro número)

Incrementa quando há **correções, ajustes ou adições pontuais** que não representam a conclusão de um bloco completo.

**Exemplos neste repositório:**

- 🐛 Correção de link quebrado, typo em arquivo .md ou erro em script
- 📝 Adição de um único lab ou nota de estudo isolada
- 🔧 Ajuste de formatação, padronização de nomes de arquivo (kebab-case)
- ⚡ Melhoria em script existente sem mudar sua função
- 📋 Atualização de CHANGELOG ou README sem novo conteúdo técnico

```bash
0.3.0 → 0.3.1  # Corrigiu link quebrado no README do ENCOR
0.3.1 → 0.3.2  # Adicionou lab isolado de OSPF single-area
0.3.2 → 0.3.3  # Padronizou nomes de pasta para kebab-case
```

---

## 🚦 Regras de Decisão

### Qual número incrementar?

```
┌─────────────────────────────────────────────────┐
│ Aprovei em uma certificação?                    │
│ Ou reestruturei completamente o repositório?    │
└──────────┬──────────────────────────────────────┘
           │
    ┌──────┴──────┐
    │     SIM     │ → MAJOR++  (0.9.0 → 1.0.0)
    └─────────────┘
           │
    ┌──────┴──────┐
    │     NÃO     │
    └──────┬──────┘
           │
┌──────────┴───────────────────────────────────────┐
│ Conclui um domínio inteiro, adicionei            │
│ nova certificação ou novo módulo estrutural?     │
└──────────┬───────────────────────────────────────┘
           │
    ┌──────┴──────┐
    │     SIM     │ → MINOR++  (0.4.0 → 0.5.0)
    └─────────────┘
           │
    ┌──────┴──────┐
    │     NÃO     │
    └──────┬──────┘
           │
┌──────────┴───────────────────────────────────────┐
│ É uma correção, ajuste pontual ou lab isolado?   │
└──────────┬───────────────────────────────────────┘
           │
    ┌──────┴──────┐
    │     SIM     │ → PATCH++  (0.4.0 → 0.4.1)
    └─────────────┘
```

---

## 🔢 Versão 0.x.x (Fase de Desenvolvimento)

Enquanto **MAJOR = 0**, o repositório está em:

- 🔨 Fase ativa de **construção e estudo**
- 🧪 Experimentação com ferramentas, labs e automação
- ⚠️ A estrutura ainda pode evoluir com frequência
- 📚 Construção do **portfólio técnico**

**Quando ir para v1.0.0?**

- ✅ Aprovação no primeiro exame principal mapeado (CCNP ENCOR 350-401)
- ✅ Todos os 6 domínios do ENCOR com pelo menos um lab documentado
- ✅ README e CHANGELOG atualizados e consistentes
- ✅ Scripts Python integrados e funcionais

---

## 📊 Roadmap de Versões (Este Repositório)

```
v0.1.0  → Estrutura inicial + docs de governança (commits, versionamento, dicionário)
v0.2.0  → README com badges, certificações e padrões de engenharia
v0.3.0  → Dicionário Semântico + refinamento geral do repositório
v0.4.0  → Primeiro domínio concluído: 01 - Architecture (labs + notas)
v0.5.0  → Segundo domínio concluído: 02 - Virtualization
v0.6.0  → Terceiro domínio concluído: 03 - Infrastructure
v0.7.0  → Quarto domínio concluído: 04 - Network Assurance
v0.8.0  → Quinto domínio concluído: 05 - Security
v0.9.0  → Sexto domínio concluído: 06 - Automation + scripts Python integrados
v1.0.0  → ✅ Aprovação no exame CCNP ENCOR 350-401

v1.1.0  → Estrutura ENARSI adicionada ao repositório
v1.2.0  → Primeiro domínio ENARSI concluído
  ...
v2.0.0  → ✅ Aprovação no exame CCNP ENARSI 300-410
```

> **Nota:** Cada certificação futura segue o mesmo padrão — MINOR para domínios concluídos, MAJOR para aprovação no exame.

---

## 🏷️ Como Criar Tags no Git

### 1. Faça commit das mudanças

```bash
git add .
git commit -m "feat(encor): conclude architecture domain labs and notes"
```

### 2. Crie uma tag anotada

```bash
git tag -a v0.4.0 -m "v0.4.0 - ENCOR domain 01 Architecture completed"
```

### 3. Envie com as tags

```bash
git push origin main
git push origin v0.4.0
```

### 4. Veja todas as tags

```bash
git tag -l
```

### 5. Veja detalhes de uma tag

```bash
git show v0.4.0
```

---

## 📝 Padrão de Mensagens de Commit

### Formato

```
tipo(escopo): descrição curta

- Detalhe da mudança 1
- Detalhe da mudança 2

Refs: #issue
```

### Tipos e impacto na versão

| Tipo                         | Quando usar                                    | Impacto no SemVer    |
|------------------------------|------------------------------------------------|----------------------|
| `feat`                       | Nova funcionalidade / novo conteúdo de domínio | Incrementa **MINOR** |
| `fix`                        | Correção de bug, link ou typo                  | Incrementa **PATCH** |
| `docs`                       | Apenas documentação (README, CHANGELOG)        | Sem incremento       |
| `style`                      | Formatação, kebab-case, padronização           | Sem incremento       |
| `refactor`                   | Refatoração de script sem mudar comportamento  | Sem incremento       |
| `chore`                      | Manutenção, .gitignore, dependências           | Sem incremento       |
| `feat!` ou `BREAKING CHANGE` | Reestruturação completa / aprovação em exame   | Incrementa **MAJOR** |

### Exemplos práticos

```bash
# PATCH — corrigiu um link no README
git commit -m "fix(docs): correct broken link to ENCOR blueprint"

# PATCH — adicionou lab isolado
git commit -m "feat(encor): add ospf single-area lab to architecture domain"

# MINOR — concluiu um domínio completo
git commit -m "feat(encor): complete all labs for domain 01 architecture"

# MINOR — adicionou nova certificação ao repo
git commit -m "feat(enarsi): add folder structure and README for ENARSI studies"

# MAJOR — aprovação no exame (marco de carreira)
git commit -m "feat!: CCNP ENCOR 350-401 exam passed

BREAKING CHANGE: repository transitions from study phase to certified status.
Bump to v1.0.0."
```

---

## ✅ Checklist antes de Incrementar Versão

- [ ] Conteúdo testado e funcionando (labs, scripts)
- [ ] Documentação atualizada (README, CHANGELOG)
- [ ] Commit com mensagem semântica descritiva
- [ ] Tag criada no formato `vX.Y.Z`
- [ ] Push da tag para o repositório remoto

---

## 📌 Resumo Rápido

| Mudança                          | Versão   | Exemplo de commit                                          |
|----------------------------------|----------|------------------------------------------------------------|
| 🐛 Correção / lab isolado        | `0.3.X`  | `fix: ...` ou `feat(encor): add single lab` → tag `v0.3.1` |
| ✨ Domínio concluído / nova cert | `0.X.0`  | `feat(encor): complete domain 01` → tag `v0.4.0`           |
| 🏆 Aprovação em exame            | `X.0.0`  | `feat!: exam passed` → tag `v1.0.0`                        |
| 📝 Docs apenas                   | —        | `docs: ...` (sem tag necessária)                           |

**Regra de Ouro:** Na dúvida durante a fase de estudo (0.x.x), use **MINOR** para conclusões de domínio e **PATCH** para adições pontuais.

---

## 🔗 Referências

- [Versionamento Semântico 2.0.0](https://semver.org/lang/pt-BR/)
- [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/)
- [CCNP ENCOR 350-401 Blueprint](https://learningnetwork.cisco.com/s/encor-exam-topics)

---

*Última atualização: Março de 2026*
