FROM centos:6
MAINTAINER Serge at abrikus@gmail.com

RUN yum -y install bind-utils net-snmp net-snmp-utils && \
    yum -y install https://github.com/sergevs/net-snmp-subagent-shell/releases/download/2.3.0.1/net-snmp-subagent-shell-2.3.0.1-ssv1.el6.noarch.rpm && \
    yum clean all

COPY snmpd.conf /etc/snmp/
COPY subagent-shell-functions-conf.xml /etc/snmp/subagent-shell/
COPY user.init /usr/bin/

EXPOSE 161/udp

ENTRYPOINT ["/usr/bin/user.init"]
