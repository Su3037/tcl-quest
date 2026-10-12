"""Bundle the authored Tcl observer as a local Worker import (no fetch dependency)."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
(root/'site/trace-source.js').write_text('// Generated from trace.tcl by scripts/build_trace.py.\nself.QUEST_TRACE_TCL = '+json.dumps((root/'site/trace.tcl').read_text(),ensure_ascii=False)+';\n')
