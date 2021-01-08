"""Parse and install dependencies of a PKGBUILD/.SRCINFO file"""

import sys
import subprocess
from srcinfo.parse import parse_srcinfo

package = sys.argv[1]

def install(dependency):
    """Install a given package with yay"""
    subprocess.call(["yay", "--useask", "--noconfirm", "--needed", "-S", dependency])

# Open file
with open(f"{package}/.SRCINFO", "r") as file:
    parsed = parse_srcinfo(file.read())

# Normal dependencies
try:
    deps = parsed[0]["depends"]
except KeyError:
    deps = None
    print("[INFO] no depends")

if deps:
    for dep in deps:
        install(dep)

# Make dependencies
try:
    makedeps = parsed[0]["makedepends"]
except KeyError:
    makedeps = None
    print("[INFO] no makedepends")

if makedeps:
    for dep in makedeps:
        install(dep)

# Check dependencies
try:
    checkdeps = parsed[0]["checkdepends"]
except KeyError:
    checkdeps = None
    print("[INFO] no checkdepends")

if checkdeps:
    for dep in checkdeps:
        install(dep)
