#!/usr/bin/env python3
"""Local preview. Bound to loopback unless explicitly exposed in a Codespace."""
import argparse,http.server,os
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8765);p.add_argument('--host',default='127.0.0.1');a=p.parse_args()
os.chdir(Path(__file__).resolve().parents[1]/'site')
print(f'Tcl Quest: http://{a.host}:{a.port}',flush=True)
http.server.ThreadingHTTPServer((a.host,a.port),http.server.SimpleHTTPRequestHandler).serve_forever()
