from pathlib import Path

p=Path(__file__).parents[1]/'index.html';s=p.read_text();s=s.replace('<script>const DATA=','<script>let DATA=',1)

a="[q,place,min,state].forEach(x=>x.oninput=filtered);cut.textContent=new Date(FEED).toLocaleString('es-ES');asof.textContent=`Corte oficial: ${new Date(FEED).toLocaleString('es-ES')} (hace ${Math.max(0,Math.round((Date.now()-new Date(FEED))/36e5))} h) · ${DATA.length} registros`;render();"

b="[q,place,min,state].forEach(x=>x.oninput=filtered);function stamp(s){const d=s?.fetched_at||FEED;cut.textContent=new Date(d).toLocaleString('es-ES');asof.textContent=`Corte oficial: ${new Date(d).toLocaleString('es-ES')} · ${DATA.length} registros · refresh automático cada 6 h`}stamp();Promise.all([fetch('data/tenders.json').then(r=>r.json()),fetch('data/status.json').then(r=>r.json())]).then(([d,s])=>{if(s.ok&&d.length>=100){DATA=d;stamp(s);render()}}).catch(()=>{});render();"

if a in s:s=s.replace(a,b,1);p.write_text(s)
