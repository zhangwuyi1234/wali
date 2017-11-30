FROM centos　　　　　　　　　　　　　　 
MAINTAINER zhangwuyi　　　
RUN yum -y install unzip
RUN yum -y install git
RUN yum -y install wget
RUN yum -y install openssh-server;yum clean all  
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN yum -y install gcc automake autoconf libtool make
RUN yum -y install gcc gcc-c++
RUN yum -y install python-devel
RUN yum -y install emacs
RUN yum -y install zlib-devel
RUN yum -y install openssl-devel
RUN mkdir /data 
RUN wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz && tar -zxvf Python-3.5.3.tgz && cd /Python-3.5.3/  && ./configure && make && make install
RUN wget --no-check-certificate  https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb
RUN tar -zxvf pip-8.0.2.tar.gz
RUN cd pip-8.0.2 && python3 setup.py build && python3 setup.py install
RUN mkdir -p /data && cd /data && git clone git://github.com/zhangwuyi1234/wali.git
RUN pip3 install pymongo
RUN pip3 install oss2
RUN pip3 install qiniu
RUN pip3 install requests
RUN pip3 install numpy
RUN pip3 install --upgrade tensorflow 
RUN pip3 install --upgrade tensorlayer



RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
EXPOSE 22  
CMD /usr/sbin/sshd -D  



