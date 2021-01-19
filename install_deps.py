"""Parse and install dependencies of a PKGBUILD/.SRCINFO file"""

import sys
import subprocess
from srcinfo.parse import parse_srcinfo

package = sys.argv[1]

def install_package(app):
    """Install a given package with yay"""
    subprocess.call(["yay", "--useask", "--noconfirm", "--needed", "-S", app])

def install_dependencies(srcinfo, deptype):
    """Parse dependency type (e.g. makedepends) and install if applicable"""

    try:
        deps = srcinfo[0][deptype]
    except KeyError:
        deps = None
        print(f"[INFO] No {deptype} required by package")
    else:
        print(f"[INFO] Installing {deps} as {deptype}")
        for dep in deps:
            install_package(dep)

# Open .SRCINFO and parse it
with open(f"{package}/.SRCINFO", "r") as file:
    parsed = parse_srcinfo(file.read())

# Install runtime dependencies
install_dependencies(parsed, "depends")

# Install make dependencies
install_dependencies(parsed, "makedepends")

# Install check dependencies
install_dependencies(parsed, "checkdepends")
