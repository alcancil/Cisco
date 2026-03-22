# 📋 Guia de Commits Profissionais - Quick Reference

## 🎯 Formato Padrão

```
<tipo>(<escopo>): <descrição curta>

[corpo opcional - mais detalhes]

[rodapé opcional - breaking changes, issues]
```

---

## 📌 Tipos de Commit

### **feat** - Nova Funcionalidade

```bash
# Quando usar: Adicionar novo script, gráfico, funcionalidade

git commit -m "feat(basics): add line chart with weekly progress data"
git commit -m "feat(intermediate): add interactive filters to dashboard"
git commit -m "feat(advanced): integrate with Netmiko scripts"
```

### **fix** - Correção de Bug

```bash
# Quando usar: Corrigir erro de código, bug visual

git commit -m "fix(basics): correct color scheme in pie chart"
git commit -m "fix(dashboard): resolve hover tooltip display issue"
git commit -m "fix(data): correct JSON parsing error"
```

### **docs** - Documentação

```bash
# Quando usar: Mudar README, CHANGELOG, comentários

git commit -m "docs(readme): add installation instructions"
git commit -m "docs(readme): improve structure with file descriptions"
git commit -m "docs(changelog): add version 0.1.0 release notes"
git commit -m "docs(code): add docstrings to all functions"
```

### **style** - Formatação

```bash
# Quando usar: Indentação, espaços, formatação (não muda lógica)

git commit -m "style(basics): format code with black formatter"
git commit -m "style(dashboard): adjust spacing in layout"
git commit -m "style: add missing semicolons and fix indentation"
```

### **refactor** - Refatoração

```bash
# Quando usar: Melhorar código sem mudar comportamento

git commit -m "refactor(basics): extract chart creation to separate function"
git commit -m "refactor(data): reorganize JSON structure for better readability"
git commit -m "refactor: simplify color palette definition"
```

### **test** - Testes

```bash
# Quando usar: Adicionar/modificar testes

git commit -m "test(basics): add unit tests for data processing"
git commit -m "test(dashboard): add integration test for full workflow"
```

### **chore** - Manutenção

```bash
# Quando usar: Dependências, configs, build, tarefas gerais

git commit -m "chore(deps): update plotly to version 5.18.0"
git commit -m "chore(init): initialize project structure"
git commit -m "chore(gitignore): add Python cache files"
git commit -m "chore: update requirements.txt with new dependencies"
```

### **perf** - Performance

```bash
# Quando usar: Melhorias de performance

git commit -m "perf(data): optimize file reading with lazy loading"
git commit -m "perf(dashboard): reduce render time by caching data"
```

### **ci** - CI/CD

```bash
# Quando usar: Mudanças em GitHub Actions, pipelines

git commit -m "ci: add GitHub Actions workflow for auto-update"
git commit -m "ci(deploy): configure automatic dashboard deployment"
```

---

## 🎯 Escopos Comuns (para este projeto)

| Escopo | Quando Usar | Exemplo |
|--------|-------------|---------|
| `basics` | Scripts básicos | `feat(basics): add bar chart` |
| `intermediate` | Scripts intermediários | `feat(intermediate): add filters` |
| `advanced` | Scripts avançados | `feat(advanced): add KPI metrics` |
| `dashboard` | Dashboard geral | `fix(dashboard): correct layout` |
| `data` | Arquivos de dados | `feat(data): add weekly progress CSV` |
| `docs` | Documentação | `docs(readme): add usage examples` |
| `readme` | README específico | `docs(readme): improve structure` |
| `changelog` | CHANGELOG específico | `docs(changelog): add v0.1.0` |
| `deps` | Dependências | `chore(deps): update plotly` |
| `init` | Inicialização | `chore(init): setup project` |
| `gitignore` | .gitignore | `chore(gitignore): add venv/` |
| `ci` | CI/CD | `ci: add auto-deploy workflow` |

---

## 📝 Exemplos Práticos do SEU Projeto

### Situação 1: Criou novo script Python

```bash
# Arquivo: src/basics/05_scatter_plot.py
git add src/basics/05_scatter_plot.py docs/05_scatter_plot.html
git commit -m "feat(basics): add scatter plot for lab correlation analysis"
```

### Situação 2: Corrigiu bug em gráfico

```bash
# Arquivo: src/basics/02_bar_chart.py (tinha erro de cor)
git add src/basics/02_bar_chart.py
git commit -m "fix(basics): correct bar chart color assignment"
```

### Situação 3: Melhorou README

```bash
# Arquivo: README.md
git add README.md
git commit -m "docs(readme): add detailed file structure explanation"
```

### Situação 4: Adicionou nova dependência

```bash
# Arquivo: requirements.txt (adicionou pandas)
git add requirements.txt
git commit -m "chore(deps): add pandas for data manipulation"
```

### Situação 5: Criou pasta de dados

```bash
# Arquivos: data/ccnp_labs.json, data/weekly_progress.csv
git add data/
git commit -m "feat(data): add CCNP lab statistics and weekly progress data"
```

### Situação 6: Refatorou código

```bash
# Arquivo: src/basics/04_dashboard_mvp.py (extraiu função)
git add src/basics/04_dashboard_mvp.py
git commit -m "refactor(basics): extract color palette to reusable constant"
```

### Situação 7: Atualizou múltiplos arquivos relacionados

```bash
# Adicionou novo gráfico + documentou + dados
git add src/intermediate/05_interactive.py docs/05_interactive.html data/filters.json README.md
git commit -m "feat(intermediate): add interactive dashboard with dropdown filters

- Implement dropdown filters for domain selection
- Add date range slider
- Update README with usage instructions
- Include sample filter configuration
"
```

### Situação 8: Correção urgente (hotfix)

```bash
git add src/basics/01_first_graph.py
git commit -m "fix(basics)!: correct critical data loading error

BREAKING CHANGE: Changed data file format from CSV to JSON
Fixes #3
"
```

---

## 🚫 Exemplos de Commits RUINS (Evitar!)

```bash
# ❌ Muito vago
git commit -m "update"
git commit -m "fix"
git commit -m "changes"

# ❌ Sem tipo
git commit -m "added new file"
git commit -m "changed colors"

# ❌ Sem escopo quando relevante
git commit -m "feat: update"  # update o quê?

# ❌ Muito genérico
git commit -m "feat: improvements"
git commit -m "fix: bugs"

# ❌ Em português misturado
git commit -m "feat: adiciona gráfico"  # escolha um idioma
```

---

## ✅ Checklist Antes de Commitar

```bash
# 1. Ver o que mudou
git status

# 2. Ver diferenças em detalhe
git diff

# 3. Adicionar arquivos específicos (não use "git add ." sempre!)
git add <arquivo1> <arquivo2>

# 4. Verificar o que está no stage
git status

# 5. Commitar com mensagem semântica
git commit -m "tipo(escopo): descrição clara"

# 6. Push
git push origin main
```

---

## 🎯 Commit Message Template (Copiar e Colar)

Salve isso como `.gitmessage` na raiz do projeto:

```
# tipo(escopo): descrição curta (máx 50 caracteres)
# |<----  Preferível usar até 50 caracteres  ---->|

# [corpo opcional - explicação mais detalhada]
# |<----  Quebrar linha em 72 caracteres  ---->|

# [rodapé opcional]
# Fixes #123
# BREAKING CHANGE: descrição

# --- TIPOS ---
# feat:     Nova funcionalidade
# fix:      Correção de bug
# docs:     Documentação
# style:    Formatação (não afeta código)
# refactor: Refatoração
# test:     Testes
# chore:    Manutenção/config
# perf:     Performance
# ci:       CI/CD

# --- ESCOPOS COMUNS ---
# basics, intermediate, advanced, dashboard, data, docs, readme
```

Configurar:

```bash
git config commit.template .gitmessage
```

---

## 🔄 Workflow Completo Resumido

```bash
# Fluxo de trabalho diário:

# 1. Ver status
git status

# 2. Adicionar mudanças específicas
git add <arquivos-modificados>

# 3. Commit semântico
git commit -m "tipo(escopo): descrição"

# 4. Push
git push origin main

# Se errar o commit (antes de push):
git commit --amend -m "nova mensagem corrigida"
```

---

## 💡 Dicas Extras

### Commitar Apenas Parte de um Arquivo

```bash
git add -p arquivo.py
# Vai perguntar hunk por hunk o que adicionar
```

### Ver Histórico de Commits

```bash
git log --oneline --graph --decorate
```

### Desfazer Último Commit (antes de push)

```bash
git reset --soft HEAD~1  # Mantém mudanças
git reset --hard HEAD~1  # Descarta mudanças
```

---

## 📚 Referências

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

---

<div align="center">

**Salve este guia! Use sempre que for fazer commit! 🚀**

</div>
