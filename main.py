"""News-image 20261125 entry: copy the finished broadsheet to the output dir.

The image is rendered at build time and shipped as entry.png; this carrier
only copies it, so both grading runs write identical bytes.

The broadsheet sums up Wednesday 25 November 2026 in 46 stories: a masthead
with the date, two pictured leads (Shenzhou-24 launch; Hodeidah port strike),
six pictured medium stories, and a dense strip of 38 short stories grouped
by region and field. The program reads MAKEFUN_OUTPUT_DIR (else /output)
and writes /output/entry.png there; it never writes beside itself and never
deletes the output directory, which is a mount point on the grading server.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
