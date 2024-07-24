FROM ubuntu:24.04
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN <<EOM
apt-get update
apt-get install -y sudo
EOM
# 作業用ユーザーの作成、シェルは/bin/bash
RUN userdel -r ubuntu
RUN groupadd --gid $USER_GID $USERNAME
RUN useradd  --uid ${USER_UID} --gid ${USER_GID} -G sudo -s /bin/bash -m ${USERNAME}
#RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}
# $USERNAMEにはsudo権限を付与
RUN <<EOM
echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USERNAME
EOM

# unzip/git/curlをインストール
RUN <<EOM
apt-get update
apt-get install -y unzip git curl
EOM

# # node.jsをインストール
# RUN <<EOM
# apt-get update
# apt-get install  -y  nodejs npm
# EOM

# install python
RUN <<EOM
apt-get update
apt-get install -y python3 python3-pip
EOM
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install pipenv --break-system-packages

# install vim(tiny)
RUN <<EOM
apt-get update
apt-get install -y vim-tiny
EOM

WORKDIR /home/${USERNAME}
USER ${USERNAME}
ENV PATH="home/${USERNAME}/.local/bin:home/${USERNAME}/bin:${PATH}"
# # install rye&pipenv
# RUN <<EOM
# curl -sL https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash
# echo 'source "$HOME/.rye/env"' >> ~/.bashrc
# EOM

# RUN <<EOM
# curl -LO https://bootstrap.pypa.io/get-pip.py
# . $HOME/.rye/env; python get-pip.py --user
# echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
# rm get-pip.py
# EOM

# instll pipenv
WORKDIR /app

# install nvm/node.js
RUN <<EOM
cd
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
bash -c "source $HOME/.nvm/nvm.sh; nvm install --lts"
EOM

# # modify prompt
# RUN <<EOM
# cd /home/${USERNAME}
# cat <<'EOL' >> .bashrc
# color_prompt=yes
# if [ "$color_prompt" = yes ]; then
#     PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n\$ '
# else
#     PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\n\$ '
# fi
# EOL
# EOM
