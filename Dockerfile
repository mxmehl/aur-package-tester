FROM imrehg/archlinux-makepkg:latest

RUN sudo pacman -Syu --noconfirm python-srcinfo

COPY install_deps.py /home/builder/

WORKDIR /home/builder/aur/
