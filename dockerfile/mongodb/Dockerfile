FROM centos　　　　　　　　　　　　　　 
MAINTAINER zhangwuyi　　　　　　   


RUN yum -y install openssh-server;yum clean all  
RUN yum -y install epel-release
RUN yum -y install python34
RUN yum -y install python34-pip
RUN yum -y install gcc
RUN yum -y install python34-devel
RUN yum -y install emacs
RUN yum -y install git
RUN yum -y install wget


RUN mkdir /usr/work && cd /usr/work && git clone git://github.com/zhangwuyi1234/github.git
RUN mkdir /usr/local/mongodb && cd /usr/local/mongodb && wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.2.4.tgz && tar -zxvf mongodb-linux-x86_64-rhel70-3.2.4.tgz && mv mongodb-linux-x86_64-rhel70-3.2.4 mongodb3.2.4 && cd /usr/local/mongodb/mongodb3.2.4 && mkdir -p data/logs && mkdir -p data/db
RUN mkdir /data
RUN echo "/usr/local/mongodb/mongodb3.2.4/bin/mongod --dbpath=/data/ --logpath=/usr/local/mongodb/mongodb3.2.4/data/log/mongodb.log --logappend&" >> ~/.bashrc 
RUN echo "export /usr/local/mongodb/mongodb3.2.4/bin:$PATH" >> ~/.bashrc 
 

RUN pip3 install pymongo
RUN pip3 install oss2
RUN pip3 install qiniu
RUN pip3 install requests


RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
EXPOSE 22  
CMD /usr/sbin/sshd -D  






