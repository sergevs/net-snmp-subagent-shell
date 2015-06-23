FROM docker.io/centos
MAINTAINER Serge at abrikus@gmail.com

RUN yum -y install https://github.com/sergevs/net-snmp-subagent-shell/releases/download/2.2.0.3/net-snmp-subagent-shell-2.2.0.3-ssv1.el7.noarch.rpm bind-utils net-snmp net-snmp-utils && \
    yum clean all

COPY snmpd.conf /etc/snmp/
COPY subagent-shell-functions-conf.xml /etc/snmp/subagent-shell/
COPY user.init /usr/bin/

EXPOSE 161/udp

ENTRYPOINT ["/usr/bin/user.init"]
