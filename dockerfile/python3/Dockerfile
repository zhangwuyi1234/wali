FROM centos　　　　　　　　　　　　　　 
MAINTAINER zhangwuyi　　　　　　   


RUN yum -y install openssh-server;yum clean all  
RUN yum -y install epel-release

RUN yum install zlib-devel
RUN yum install openssl-devel
RUN　wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
RUN　tar -zxvf Python-3.5.3.tgz
RUN　cd Python-3.5.3
RUN　./configure --prefix=/usr/local/python3 --enable-shared
RUN　make && make install

RUN　wget --no-check-certificate  https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb
RUN　tar -zxvf pip-8.0.2.tar.gz
RUN　cd pip-8.0.2
RUN　python3 setup.py build
RUN　python3 setup.py install


RUN yum -y install gcc
RUN yum -y install python3-devel
RUN yum -y install emacs

RUN yum -y install unzip
RUN yum -y install git
RUN yum -y install wget

RUN mkdir /usr/work && cd /usr/work && git clone git://github.com/zhangwuyi1234/github.git

RUN pip3 install pymongo
RUN pip3 install oss2
RUN pip3 install qiniu
RUN pip3 install requests

RUN pip3 install Pillow
RUN pip3 install numpy
RUN pip3 install opencv-python



RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
EXPOSE 22  
CMD /usr/sbin/sshd -D  




