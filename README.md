# AUR package tester

[![Build Status](https://drone.fsfe.org/api/badges/max.mehl/aur-package-tester/status.svg)](https://drone.fsfe.org/max.mehl/aur-package-tester)

This repo contains scripts and Drone CI configuration to automatically test the
AUR packages I maintain.

By default, an automatic runner should check whether the packages build
correctly.

## Test before pushing to AUR

Since the Drone config builds the package from the PKGBUILD file, you can make
changes to the file and go one of these paths:

1. Push the changed PKGBUILD/.SRCINFO files only to this repo, and let the CI do
   its job.
2. Run the Drone CLI tool locally: `drone exec --event push --branch master --trusted`
