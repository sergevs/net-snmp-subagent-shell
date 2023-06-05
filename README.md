This is a fork on sergevs/net-snmp-subagent-shell


It creates an AgentX for NetSNMP using the Perl API.


This fork adds basic support for Kubernetes enabling a K8s node to be monitored from an SNMP system that is running NetSNMP.

The purpose is to provide a migration tool for organizations with network management systems that use SNMP that are implementing
alternatives to network equipment that use k8s as a foundation.  I would not suggest this is a long term solution.

It adds a KUBERNETES-MIB to the SUBAGENT-SHELL-MIB

To add additional mib objects

1.  Add objects to MIB file SUBAGENT-SHELL-KUBERNETES-MIB.txt
2.  Add logic to populate the MIB in subagents-shell-base.functions in the k8sMib function


The original documentation is available at  [wiki home](.https://github.com/sergevs/net-snmp-subagent-shell/wiki)



## Installation

## Ubuntu

1. Install netsnmp  (the package is called snmp in ubuntu 22.04)
2. Install snmp-mibs-downloader (get the mibs used by netsnmp) 
3. Install additional dependencies libnsnmp-perl, libxml-simple-perl, libjson-perl

4. Clone the repository onto the target k8s host

  ```  
   aclocal 
   automake --add-missing
   autoconf
   configure --prefix=/usr --sysconfdir=/etc # if you choose another directories, you have to amend path appropriately below
   make install
   ``` 

6. Test using subagent-shell -v
7. Run subagent-shell

   add the following to  snmpd.conf:

    ```
    perl do "/etc/snmp/subagent/subagent-shell";
    ```


Verification
```bash
snmpwalk -v2c -M+/home/adamd/snmp/net-snmp-subagent-shell/mibs -mALL -c public 172.30.255.222 SUBAGENT-SHELL
Bad operator (INTEGER): At line 73 in /usr/share/snmp/mibs/ietf/SNMPv2-PDU
SUBAGENT-SHELL-MIB::ssFunctionsCount = INTEGER: 3
SUBAGENT-SHELL-MIB::ssFunctionsSuccessCount = INTEGER: 3
SUBAGENT-SHELL-MIB::ssFunctionsFailedCount = INTEGER: 0
SUBAGENT-SHELL-MIB::ssTimeStamp = STRING: "05-Jun-2023 17:41:37 (1685986897)"
SUBAGENT-SHELL-MIB::ssTotalExecTime = STRING: "0.684"
SUBAGENT-SHELL-MIB::ssMasterAgentPid = INTEGER: 621446
SUBAGENT-SHELL-MIB::ssPollerPid = INTEGER: 621453
SUBAGENT-SHELL-OSINFO-MIB::osinfoRelease = STRING: "Debian bookworm/sid 5.15.0-69-generic x86_64"
SUBAGENT-SHELL-LAST-LOGINS-MIB::loggedInUsersCount = Gauge32: 2
SUBAGENT-SHELL-LAST-LOGINS-MIB::loggedInUserInfo.1 = STRING: "adamd    pts/1    192.168.152.100  11:42   41:05   0.13s  0.03s sshd: adamd [priv]"
SUBAGENT-SHELL-LAST-LOGINS-MIB::loggedInUserInfo.2 = STRING: "adamd    pts/2    192.168.152.100  17:00    1.00s  0.44s  0.06s sudo su -"
SUBAGENT-SHELL-LAST-LOGINS-MIB::wtmpBegins = STRING: "wtmp begins Tue Apr  4 21:03:52 2023"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.1 = STRING: "adamd    pts/1        192.168.152.100  Mon Jun  5 11:42   still logged in"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.2 = STRING: "adamd    pts/0        192.168.152.100  Mon Jun  5 11:42 - 17:03  (05:20)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.3 = STRING: "adamd    pts/0        192.168.152.100  Mon Jun  5 11:39 - 11:42  (00:02)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.4 = STRING: "adamd    pts/1        192.168.152.100  Fri Jun  2 16:21 - 23:04 (2+06:43)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.5 = STRING: "adamd    pts/2        192.168.152.100  Fri Jun  2 12:21 - 22:02  (09:41)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.6 = STRING: "adamd    pts/0        192.168.152.100  Fri Jun  2 11:59 - 22:02  (10:02)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.7 = STRING: "reboot   system boot  5.15.0-69-generic Fri Jun  2 11:51   still running"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.8 = STRING: "reboot   system boot  5.15.0-69-generic Wed May 31 12:17 - 17:48  (05:31)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.9 = STRING: "adamd    tty1                          Wed May 24 00:03 - down   (00:21)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.10 = STRING: "reboot   system boot  5.15.0-69-generic Tue May 23 21:04 - 00:24  (03:20)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.11 = STRING: "reboot   system boot  5.15.0-69-generic Mon Apr 10 15:22 - 20:15  (04:53)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.12 = STRING: "tobyc    pts/0        10.0.255.3       Thu Apr  6 20:57 - 20:59  (00:01)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.13 = STRING: "tobyc    pts/0        10.0.255.3       Thu Apr  6 20:55 - 20:57  (00:01)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.14 = STRING: "tobyc    pts/2        10.0.255.3       Thu Apr  6 20:20 - 20:38  (00:17)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.15 = STRING: "tobyc    pts/2        10.0.255.3       Thu Apr  6 20:19 - 20:20  (00:01)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.16 = STRING: "tobyc    pts/2        10.0.255.3       Thu Apr  6 20:15 - 20:19  (00:03)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.17 = STRING: "tobyc    pts/2        10.0.255.3       Thu Apr  6 20:14 - 20:15  (00:00)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.18 = STRING: "adamd    pts/0        192.168.152.100  Thu Apr  6 20:09 - 20:30  (00:20)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.19 = STRING: "adamd    pts/0        192.168.152.100  Thu Apr  6 14:58 - 14:58  (00:00)"
SUBAGENT-SHELL-LAST-LOGINS-MIB::lastUserInfo.20 = STRING: "adamd    pts/0        192.168.152.100  Thu Apr  6 13:32 - 13:36  (00:03)"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodesInfo.1 = STRING: "k8s-1-enp9s-f1   Ready      control-plane   61d   v1.26.3"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodesInfo.2 = STRING: "k8s-2-enp9s0f0   NotReady   <none>          61d   v1.26.3"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodesInfo.3 = STRING: "k8s-3-enp8s0f0   NotReady   <none>          61d   v1.26.3"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodeConditionsInfo.1 = STRING: "NetworkUnavailable False 2023-06-02T11:53:18Z 2023-06-02T11:53:18Z FlannelIsUp Flannel is running on this node"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodeConditionsInfo.2 = STRING: "MemoryPressure False 2023-06-05T17:39:25Z 2023-04-05T11:55:31Z KubeletHasSufficientMemory kubelet has sufficient memory available"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodeConditionsInfo.3 = STRING: "DiskPressure False 2023-06-05T17:39:25Z 2023-04-05T11:55:31Z KubeletHasNoDiskPressure kubelet has no disk pressure"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodeConditionsInfo.4 = STRING: "PIDPressure False 2023-06-05T17:39:25Z 2023-04-05T11:55:31Z KubeletHasSufficientPID kubelet has sufficient PID available"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sNodeConditionsInfo.5 = STRING: "Ready True 2023-06-05T17:39:25Z 2023-04-05T12:05:24Z KubeletReady kubelet is posting ready status. AppArmor enabled"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.1 = STRING: "demo-https     epic-demows-57cc9bcc59-l9rvz                             1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.2 = STRING: "demo-https     epic-demows-57cc9bcc59-mmcr9                             1/1   Terminating        4 (3d5h ago)      60d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.3 = STRING: "demo-https     epic-demows-57cc9bcc59-nhhkz                             1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.4 = STRING: "demo-https     epic-demows-57cc9bcc59-v6zpc                             1/1   Terminating        4 (3d5h ago)      60d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.5 = STRING: "demo-https     epic-demows-57cc9bcc59-z7rg5                             1/1   Running            4 (3d5h ago)      60d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.6 = STRING: "demo-lb        epic-demows-57cc9bcc59-2jfcb                             1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.7 = STRING: "demo-lb        epic-demows-57cc9bcc59-cjq6r                             1/1   Terminating        3 (3d5h ago)      56d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.8 = STRING: "demo-tcp       epictesttcp4-555fb5f44d-5clhb                            1/1   Terminating        4 (3d5h ago)      59d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.9 = STRING: "demo-tcp       epictesttcp4-555fb5f44d-kmghl                            1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.10 = STRING: "epic-gateway   controller-agent-d6rvn                                   0/1   Running            109 (5m54s ago)   59d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.11 = STRING: "epic-gateway   controller-agent-t8wjz                                   1/1   Running            4 (3d5h ago)      59d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.12 = STRING: "epic-gateway   controller-agent-zsd6w                                   1/1   Running            4 (3d5h ago)      59d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.13 = STRING: "epic-gateway   controller-manager-5487b6df85-4nlrx                      1/1   Terminating        4 (3d5h ago)      59d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.14 = STRING: "epic-gateway   controller-manager-5487b6df85-ppnwl                      1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.15 = STRING: "kube-flannel   kube-flannel-ds-9v2sr                                    1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.16 = STRING: "kube-flannel   kube-flannel-ds-j4krt                                    1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.17 = STRING: "kube-flannel   kube-flannel-ds-jxc9s                                    1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.18 = STRING: "kube-system    coredns-787d4945fb-7c2qs                                 1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.19 = STRING: "kube-system    coredns-787d4945fb-h4bws                                 1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.20 = STRING: "kube-system    etcd-k8s-1-enp9s-f1                                      1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.21 = STRING: "kube-system    kube-apiserver-k8s-1-enp9s-f1                            1/1   Running            110 (6h27m ago)   61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.22 = STRING: "kube-system    kube-controller-manager-k8s-1-enp9s-f1                   1/1   Running            7 (17h ago)       61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.23 = STRING: "kube-system    kube-proxy-lnhr2                                         1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.24 = STRING: "kube-system    kube-proxy-wfcfj                                         1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.25 = STRING: "kube-system    kube-proxy-wpfc2                                         1/1   Running            5 (3d5h ago)      61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.26 = STRING: "kube-system    kube-scheduler-k8s-1-enp9s-f1                            1/1   Running            6 (17h ago)       61d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.27 = STRING: "prom-stack     alertmanager-prom-stack-kube-prometheus-alertmanager-0   2/2   Terminating        4 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.28 = STRING: "prom-stack     prom-stack-grafana-5b84b54995-2pxrc                      3/3   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.29 = STRING: "prom-stack     prom-stack-grafana-5b84b54995-gkt9j                      3/3   Terminating        6 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.30 = STRING: "prom-stack     prom-stack-kube-prometheus-operator-5b85ddfb78-r5nrn     1/1   Terminating        2 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.31 = STRING: "prom-stack     prom-stack-kube-prometheus-operator-5b85ddfb78-tc92s     1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.32 = STRING: "prom-stack     prom-stack-kube-state-metrics-79b59f4546-8mz5t           1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.33 = STRING: "prom-stack     prom-stack-kube-state-metrics-79b59f4546-fqtt4           1/1   Terminating        2 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.34 = STRING: "prom-stack     prom-stack-prometheus-node-exporter-mq4kd                1/1   Running            2 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.35 = STRING: "prom-stack     prom-stack-prometheus-node-exporter-r6dx9                1/1   Running            2 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.36 = STRING: "prom-stack     prom-stack-prometheus-node-exporter-twk8w                0/1   CrashLoopBackOff   359 (3m25s ago)   12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.37 = STRING: "prom-stack     prometheus-prom-stack-kube-prometheus-prometheus-0       2/2   Terminating        4 (3d5h ago)      12d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.38 = STRING: "purelb         allocator-cd979f486-k6wh7                                1/1   Running            0                 19h"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.39 = STRING: "purelb         lbnodeagent-bbs7x                                        1/1   Running            3 (3d5h ago)      55d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.40 = STRING: "purelb         lbnodeagent-gl8zc                                        1/1   Running            3 (3d5h ago)      55d"
SUBAGENT-SHELL-KUBERNETES-MIB::k8sPodsInfo.41 = STRING: "purelb         lbnodeagent-z77cw                                        1/1   Running            3 (3d5h ago)      55d"
```