# 构建tensorflow 环境
FROM ubuntu

MAINTAINER henrry

# 安装python 和 pip
RUN apt update \
        && apt install -y python3-pip python3-dev vim \
        && apt install -y emacs
        && apt install -y git
        && apt install -y wget
        && pip3 install --upgrade pip \
        && pip3 install tensorflow \
        && pip3 install tensorlayer \
        # && pip3 install tensorflow-gpu \ 
        && ln -s /usr/bin/python3 /usr/bin/python \
        && ln -s /usr/bin/pip3 /usr/bin/pip

# 映射端口
EXPOSE 8888

# 添加文件
ADD vimrc /root/.vimrc
