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

Incrementa quando faz **mudanças incompatíveis** na API/código.

**Exemplos:**

- 💥 Remover funcionalidades antigas
- 🔄 Mudar completamente a estrutura do projeto
- 🏗️ Trocar biblioteca principal (ex: Plotly → Dash)
- 🚨 Mudanças que quebram código existente

```bash
0.9.0 → 1.0.0  # Primeira versão estável
1.5.0 → 2.0.0  # Mudança que quebra compatibilidade
```

---

### **MINOR** (segundo número)

Incrementa quando adiciona **nova funcionalidade** mantendo compatibilidade.

**Exemplos:**

- ✨ Adicionar novo gráfico
- 📊 Criar novo dashboard
- 🎨 Implementar nova feature
- 🔧 Adicionar opção/configuração

```bash
0.1.0 → 0.2.0  # Adicionou dashboard MVP
0.2.0 → 0.3.0  # Adicionou gráfico scatter
0.3.0 → 0.4.0  # Adicionou heatmap
```

---

### **PATCH** (terceiro número)

Incrementa quando faz **correções de bugs** (backwards compatible).

**Exemplos:**

- 🐛 Corrigir bug no código
- 🔧 Ajustar cores/estilos
- 📝 Corrigir documentação
- ⚡ Melhorar performance sem mudar funcionalidade

```bash
0.2.0 → 0.2.1  # Corrigiu bug no dashboard
0.2.1 → 0.2.2  # Ajustou cores do gráfico
0.2.2 → 0.2.3  # Corrigiu typo na documentação
```

---

## 🚦 Regras de Decisão

### Qual número incrementar?

```

┌─────────────────────────────────────────┐
│ Quebrou compatibilidade?                │
│ (código antigo para de funcionar)       │
└──────────┬──────────────────────────────┘
           │
    ┌──────┴──────┐
    │     SIM     │ → MAJOR++  (1.0.0 → 2.0.0)
    └─────────────┘
           │
    ┌──────┴──────┐
    │     NÃO     │
    └──────┬──────┘
           │
┌──────────┴───────────────────────────────┐
│ Adicionou funcionalidade nova?           │
└──────────┬───────────────────────────────┘
           │
    ┌──────┴──────┐
    │     SIM     │ → MINOR++  (0.1.0 → 0.2.0)
    └─────────────┘
           │
    ┌──────┴──────┐
    │     NÃO     │
    └──────┬──────┘
           │
┌──────────┴───────────────────────────────┐
│ Apenas correção/ajuste?                  │
└──────────┬───────────────────────────────┘
           │
    ┌──────┴──────┐
    │     SIM     │ → PATCH++  (0.2.0 → 0.2.1)
    └─────────────┘
```

---

## 🔢 Versão 0.x.x (Desenvolvimento)

Enquanto **MAJOR = 0**, o projeto está em:

- 🔨 Fase de **desenvolvimento**
- 🧪 **Experimentação** e aprendizado
- ⚠️ Pode ter mudanças frequentes
- 📚 Construção de **portfólio**

**Quando ir para v1.0.0?**

- ✅ Projeto completo e testado
- ✅ Documentação finalizada
- ✅ Funcionalidades principais implementadas
- ✅ Pronto para uso em produção

---

## 📊 Roadmap de Versões (Exemplo deste Projeto)

```
v0.1.0 - Gráficos básicos (linha, barras, pizza)
v0.2.0 - Dashboard MVP com 4 gráficos integrados
v0.3.0 - Gráfico scatter (latência vs perda)
v0.4.0 - Heatmap (utilização de dispositivos)
v0.5.0 - Gauge (medidor de banda)
v0.6.0 - Timeline (janelas de manutenção)
v0.7.0 - Conexão com dados reais (SNMP/SSH)
v0.8.0 - Filtros interativos
v0.9.0 - Refresh automático
v1.0.0 - Versão estável para produção
```

---

## 🏷️ Como Criar Tags no Git

### 1. Commit as mudanças

```bash
git add .
git commit -m "feat(dashboard): adiciona dashboard MVP"
```

### 2. Criar tag anotada

```bash
git tag -a v0.2.0 -m "Versão 0.2.0 - Dashboard MVP"
```

### 3. Push com tags

```bash
git push origin main
git push origin v0.2.0
```

### 4. Ver todas as tags

```bash
git tag -l
```

### 5. Ver detalhes de uma tag

```bash
git show v0.2.0
```

---

## 📝 Padrão de Mensagens de Commit

### Formato

```

tipo(escopo): descrição curta

- Detalhes da mudança 1
- Detalhes da mudança 2

Relacionado: contexto
Refs: #issue
```

### Tipos

- `feat`: nova funcionalidade → incrementa **MINOR**
- `fix`: correção de bug → incrementa **PATCH**
- `docs`: apenas documentação → não incrementa versão
- `style`: formatação → não incrementa versão
- `refactor`: refatoração → não incrementa versão
- `perf`: melhoria de performance → incrementa **PATCH**
- `test`: adiciona testes → não incrementa versão
- `chore`: tarefas de manutenção → não incrementa versão
- `BREAKING CHANGE`: quebra compatibilidade → incrementa **MAJOR**

### Exemplos
```bash
# MINOR (0.1.0 → 0.2.0)
git commit -m "feat(dashboard): adiciona dashboard MVP com 4 gráficos"

# PATCH (0.2.0 → 0.2.1)
git commit -m "fix(dashboard): corrige renderização do gráfico de pizza"

# MAJOR (0.9.0 → 1.0.0)
git commit -m "feat!: migra de Plotly para Dash

BREAKING CHANGE: remove suporte a gráficos estáticos"
```

---

## ✅ Checklist antes de Incrementar Versão

- [ ] Código testado e funcionando
- [ ] Documentação atualizada (README, CHANGELOG)
- [ ] Commit com mensagem descritiva
- [ ] Tag criada no formato `vX.Y.Z`
- [ ] Push da tag para o repositório remoto

---

## 🔗 Referências

- [Versionamento Semântico 2.0.0](https://semver.org/lang/pt-BR/)
- [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/)

---

## 📌 Resumo Rápido

| Mudança | Versão | Comando Git |
|---------|--------|-------------|
| 🐛 Bug fix | `0.2.X` | `fix: ...` → tag `v0.2.1` |
| ✨ Nova feature | `0.X.0` | `feat: ...` → tag `v0.3.0` |
| 💥 Breaking change | `X.0.0` | `feat!: ...` → tag `v1.0.0` |
| 📝 Docs apenas | - | `docs: ...` (sem tag) |

**Regra de Ouro:** Na dúvida, use **MINOR** durante desenvolvimento (0.x.x)