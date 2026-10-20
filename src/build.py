import base64,re,os,json
R='/mnt/project-files/focus-performance/'
t=open(R+'src/template.html').read()
def b64(p,m): return f'data:{m};base64,'+base64.b64encode(open(R+p,'rb').read()).decode()
SEND_REAL="fetch('/api/lead',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({nome:nome,telefone:tel,instagram:insta,faturamento:fat,qualificado:qualified})})\n      .then(function(r){if(!r.ok)throw 0})"
prod=t.replace('{{LOGO}}',b64('assets/logo.png','image/png')).replace('{{GLASS}}',b64('assets/icone.jpg','image/jpeg')).replace('{{FAVICON}}',b64('assets/icone.jpg','image/jpeg')).replace('{{TESTIMONIALS}}','[]').replace('{{CLIENTS}}','[]').replace('{{SEND}}',SEND_REAL)
open(R+'index.html','w').write(prod)
ex=json.dumps([{"texto":"Espaço para o depoimento de um parceiro, com o resultado que ele quiser contar.","nome":"Nome do cliente","cargo":"Cargo, Empresa","exemplo":True}]*3,ensure_ascii=False)
logo=b64('assets/logo.png','image/png'); glass=b64('assets/icone.jpg','image/jpeg')
prev=t.replace('{{LOGO}}',logo).replace('{{GLASS}}',glass).replace('{{FAVICON}}',glass).replace('{{TESTIMONIALS}}',ex).replace('{{CLIENTS}}','[]').replace('{{SEND}}','Promise.resolve()')
m=re.search(r'<title>.*?</title>',prev,re.S)
head_links=re.findall(r'<link href="https://fonts.googleapis[^>]*>',prev)[0]
style=re.search(r'<style>.*?</style>',prev,re.S).group(0)
body=re.search(r'<body>(.*)</body>',prev,re.S).group(1)
S='/tmp/claude-0/-home-user/7f612465-b7ad-5b39-8c3c-a3c4a58feca9/scratchpad/'
open(S+'artifact.html','w').write('<title>Focus Performance</title>\n'+head_links+'\n'+style.replace('<style>','<style>\n:root{color-scheme:light}',1)+'\n'+body)
