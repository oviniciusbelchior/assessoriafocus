// Recebe o formulário e repassa para LEAD_WEBHOOK_URL (defina na Vercel).
// Leads desqualificados também são enviados, com qualificado=false.
module.exports = async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  const b = req.body || {};
  const lead = {
    nome: String(b.nome || '').slice(0, 120),
    telefone: String(b.telefone || '').replace(/\D/g, '').slice(0, 15),
    instagram: String(b.instagram || '').slice(0, 120),
    faturamento: String(b.faturamento || ''),
    qualificado: b.faturamento !== 'menos-25k',
    recebidoEm: new Date().toISOString(),
  };
  if (!lead.nome || lead.telefone.length < 10 || !lead.instagram || !lead.faturamento) {
    return res.status(400).json({ error: 'invalid' });
  }
  const url = process.env.LEAD_WEBHOOK_URL;
  if (url) {
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(lead) });
    if (!r.ok) return res.status(502).json({ error: 'webhook_failed' });
  } else {
    console.log('lead', JSON.stringify(lead));
  }
  return res.status(200).json({ ok: true });
};
