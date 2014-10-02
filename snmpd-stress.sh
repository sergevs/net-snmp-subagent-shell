#!/bin/zsh 

cycles=100000
i=1
declare -A vmem rmem
echo `date`
while ( [ $i -le $cycles ] )
do
  [[ $((i%1000)) -eq 0 ]] && echo "cycle $i" `date`
  snmpwalk  -v2c  -M+/etc/snmp/subagent-shell/mibs -mALL -c public localhost SUBAGENT-SHELL > /dev/null
  snmpwalk  -v2c  -M+/etc/snmp/subagent-shell/mibs -mALL -c public localhost .1 > /dev/null
  ps=($(ps aux | awk '/\/usr\/bin\/subagent-shell|\/usr\/sbin\/snmpd/ {print $2 " " $5 " " $6}'))
  if [[ $i > 1 ]]; then
    if [ $vmem[$ps[1]] -gt $ps[2] ] || [ $rmem[$ps[1]] -gt $ps[3] ] || [ $vmem[$ps[4]] -gt $ps[5] ] || [ $rmem[$ps[4]] -gt $ps[6] ] ; then
      echo  cycle $i pid $ps[1] vmem $vmem[$ps[1]] ps $ps[2]  rmem $rmem[${ps[1]}]  ps $ps[3]  pid $ps[4] vmem $vmem[$ps[4]] ps $ps[5]  rmem $rmem[${ps[4]}]  ps $ps[6]
    fi
  fi
  vmem[$ps[1]]=$ps[2]
  rmem[$ps[1]]=$ps[3]
  vmem[$ps[4]]=$ps[5]
  rmem[$ps[4]]=$ps[6]
  i=$((i+1))
done
