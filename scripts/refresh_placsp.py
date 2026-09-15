import json,urllib.request,xml.etree.ElementTree as E

from datetime import datetime,timezone

from pathlib import Path

U='https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom';D=Path(__file__).parents[1]/'data';D.mkdir(exist_ok=True);root=E.fromstring(urllib.request.urlopen(U,timeout=90).read());a=[]

def t(e,n):
  
 x=next((z for z in e.iter() if z.tag.endswith(n) and z.text),None);return x.text.strip() if x is not None else ''
  
for e in (x for x in root.iter() if x.tag.endswith('entry')):
  
 u=next((x.get('href','') for x in e.iter() if x.tag.endswith('link') and x.get('href')), '');q=t(e,'title')
  
 if q and u:a.append({'id':t(e,'ContractFolderID'),'title':q,'updated':t(e,'updated'),'org':t(e,'PartyName'),'city':t(e,'CityName'),'region':t(e,'CountrySubentity'),'amount':0,'currency':'EUR','deadline':t(e,'EndDate')[:10],'time':t(e,'EndTime')[:8],'status':t(e,'ContractFolderStatusCode') or 'PUB','cpv':[x.text.strip() for x in e.iter() if x.tag.endswith('ItemClassificationCode') and x.text][:8],'url':u})
   
s={'source':U,'fetched_at':datetime.now(timezone.utc).isoformat(),'records_published':len(a),'ok':len(a)>=100};(D/'tenders.json').write_text(json.dumps(a));(D/'status.json').write_text(json.dumps(s));assert s['ok']




