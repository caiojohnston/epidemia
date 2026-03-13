# Epidemia - Frontend

Dashboard web para o sistema Epidemia, construído com Next.js e shadcn/ui.

## Tech Stack

- **Next.js 15** - Framework React com App Router
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização utility-first
- **shadcn/ui** - Componentes acessíveis (Radix UI)
- **TanStack Query** - Gerenciamento de estado do servidor
- **Zustand** - Gerenciamento de estado global
- **React Hook Form** - Formulários performáticos
- **Zod** - Validação de schemas
- **NextAuth.js** - Autenticação

## Requisitos

- Node.js 18+
- pnpm 8+

## Instalação

```bash
# Clonar o repositório (se ainda não tiver)
git clone <repo-url>
cd epidemia/web

# Instalar dependências
pnpm install

## Configuração

1. Copie o arquivo de variáveis de ambiente:

```bash
cp .env.example .env.local
```

2. Configure as variáveis necessárias:

```env
# API
NEXT_PUBLIC_API_URL=http://localhost:8000

# NextAuth
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=sua-chave-secreta-aqui
```

## Executando

```bash
# Desenvolvimento
pnpm dev

# Build de produção
pnpm build

# Executar build
pnpm start
```

O app estará disponível em [http://localhost:3000](http://localhost:3000).

## Estrutura do Projeto

```
src/
├── app/                    # App Router (páginas)
│   ├── (auth)/            # Rotas autenticadas
│   ├── (public)/          # Rotas públicas
│   └── api/               # API Routes
├── components/
│   ├── ui/                # Componentes shadcn
│   ├── forms/             # Formulários reutilizáveis
│   ├── layout/            # Header, Sidebar, etc
│   └── dashboard/         # Componentes de dashboard
├── hooks/                 # Custom hooks
├── lib/                   # Utilitários e configurações
├── providers/             # Context providers
├── stores/                # Zustand stores
└── types/                 # TypeScript types
```

## Adicionando Componentes shadcn

```bash
# Adicionar um componente
pnpm dlx shadcn@latest add button

# Adicionar múltiplos componentes
pnpm dlx shadcn@latest add button card input
```

## Scripts Disponíveis

| Comando | Descrição |
|---------|-----------|
| `pnpm dev` | Inicia servidor de desenvolvimento |
| `pnpm build` | Gera build de produção |
| `pnpm start` | Executa build de produção |
| `pnpm lint` | Executa linter |
