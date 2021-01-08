"""Parse and install dependencies of a PKGBUILD/.SRCINFO file"""

import sys
import subprocess
from srcinfo.parse import parse_srcinfo

package = sys.argv[1]

def install(dependency):
    """Install a given package with yay"""
    subprocess.call(["yay", "--useask", "--noconfirm", "--needed", "-S", dependency])

with open(f"{package}/.SRCINFO", "r") as file:
    SRCINFO = file.read()
    parsed = parse_srcinfo(SRCINFO)
    deps = parsed[0]["depends"]

for dep in deps:
    install(dep)
