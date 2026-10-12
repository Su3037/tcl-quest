"""Version local modules and CSS together so a refresh cannot mix old/new releases."""
import hashlib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];site=ROOT/'site'
modules=sorted(site.glob('*.js'))
def normalized(source):
 source=re.sub(r"(from\s+['\"])(\./[^'\"]+\.js)(?:\?v=[^'\"]+)?",r'\1\2',source)
 source=re.sub(r"(['\"])(runner\.js|trace-source\.js)(?:\?v=[^'\"]+)?\1",r'\1\2\1',source)
 return source
sources={p:normalized(p.read_text()) for p in modules}
inputs=''.join(p.name+'\n'+s for p,s in sources.items())+(site/'style.css').read_text()
for p in sorted(site.glob('*.json')):inputs+=p.name+p.read_text()
inputs+=(site/'locales/en.json').read_text()
version=hashlib.sha256(inputs.encode()).hexdigest()[:12]
for p,s in sources.items():
 s=re.sub(r"(from\s+['\"])(\./[^'\"]+\.js)",lambda m:m[1]+m[2]+'?v='+version,s)
 s=re.sub(r"(['\"])(runner\.js|trace-source\.js)\1",lambda m:m[1]+m[2]+'?v='+version+m[1],s)
 p.write_text(s)
p=site/'index.html';s=p.read_text();s=re.sub(r'(style\.css|app\.js)(?:\?v=[^\"]+)?',lambda m:m[1]+'?v='+version,s);p.write_text(s)
print('Versioned local assets:',version)
