# Focus Performance: página de vendas

Site estático (index.html) com uma função serverless (api/lead.js) que recebe o formulário.

## Publicar na Vercel
1. Suba esta pasta em um repositório no GitHub.
2. Na Vercel, importe o repositório (Framework Preset: Other, sem build command).
3. Em Settings > Environment Variables, crie `LEAD_WEBHOOK_URL` com a URL que receberá os leads (JSON). Sem ela, os leads só aparecem nos logs da função.

## Editar
Os ajustes de texto e design são feitos comigo: o `index.html` é gerado a partir de `src/template.html`.
