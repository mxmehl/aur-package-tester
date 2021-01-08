FROM imrehg/archlinux-makepkg:latest

RUN sudo pacman -S --noconfirm python-srcinfo

COPY install_deps.py /home/builder/

WORKDIR /home/builder/aur/
