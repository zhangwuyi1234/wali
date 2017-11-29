FROM centos　　　　　　　　　　　　　　 
MAINTAINER zhangwuyi　　　　　　   


RUN yum -y install openssh-server;yum clean all  
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN yum -y install gcc
RUN yum -y install python-devel
RUN yum -y install emacs

RUN yum -y install unzip
RUN yum -y install git
RUN yum -y install wget

RUN mkdir /data && cd /data && git clone git://github.com/zhangwuyi1234/wali.git

RUN pip3 install pymongo
RUN pip3 install oss2
RUN pip3 install qiniu
RUN pip3 install requests

RUN pip3 install Pillow
RUN pip3 install numpy
RUN pip3 install opencv-python
RUN pip3 install tensorflow
RUN pip3 install tensorlayer


RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
EXPOSE 22  
CMD /usr/sbin/sshd -D  



