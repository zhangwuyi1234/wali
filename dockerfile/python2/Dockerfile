FROM centos　　　　　　　　　　　　　  
MAINTAINER zhangwuyi　　　   


RUN yum -y install openssh-server;yum clean all  
RUN yum -y install epel-release

RUN yum -y install cmake 
RUN yum -y install opencv
RUN yum -y install opencv-devel

RUN yum -y install python-pip
RUN yum -y install python-devel

RUN yum -y install emacs
RUN yum -y install wget
RUN yum -y install unzip


RUN pip install oss2
RUN pip install qiniu
RUN pip install requests

RUN pip install Pillow
RUN pip install numpy
RUN pip install opencv-python
 
RUN yum -y install git
RUN mkdir /usr/work $$ cd /usr/work $$ git clone git://github.com/zhangwuyi1234/github.git


RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
EXPOSE 22  
CMD /usr/sbin/sshd -D  




