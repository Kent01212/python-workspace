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

WORKDIR /home/${USERNAME}
USER ${USERNAME}
ENV PATH="home/${USERNAME}/.local/bin:home/${USERNAME}/bin:${PATH}"
# install rye&pipenv
RUN <<EOM
curl -sL https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash
echo 'source "$HOME/.rye/env"' >> ~/.bashrc
EOM

# instll pipenv
RUN <<EOM
pip install pipenv --break-system-packages
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
EOM
WORKDIR /app

