Name:       net-snmp-subagent
Version:    2.0.0.0
Release:    ssv1
Summary:    Net SNMP subagent extends snmd mib
License:    GPL
Group:      Monitoring
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot
BuildArch:  noarch
Packager:   Serge <abrikus@gmail.com>
Requires:   curl ntp
URL: http://code.google.com/p/linux-administrator-tools

%description
Net SNMP subagent executes arbitrary commands and provide results via snmpd  

%prep
%setup 

%build

%install
%__rm -rf %buildroot
%configure
%makeinstall

%files
%defattr(-,root,root)
%_bindir/*
%dir /etc/snmp/subagent
%dir /etc/snmp/subagent/mibs
%dir /etc/snmp/subagent/conf.d
/etc/snmp/subagent/mibs/*
/etc/snmp/subagent/*.functions
%config(noreplace) %attr(444,root,root) /etc/snmp/subagent/*-conf.xml
%_sysconfdir/init.d/subagent-shell
%_sysconfdir/sysconfig/subagent-shell.options

%post
# FIX startup/exit priority for versions before 2.1.0.1
[ -s /etc/rc3.d/S22subagent-shell ] && /sbin/chkconfig --del subagent-shell 
/sbin/chkconfig --add subagent-shell
grep -P '^perl do.*/etc/snmp/subagent/snmpd-poller-agent' /etc/snmp/snmpd.conf
if [ $? == 0 ]; then
# removal embedded snmpd-poller for versions before 2.0.0.0
  sed -i -e 's!^\(perl do "/etc/snmp/subagent/snmpd-poller-agent\)!#\1!' /etc/snmp/snmpd.conf
  /sbin/service snmpd condrestart >/dev/null 2>&1 || :
fi
if [ "$1" -ge "1" ]; then
  /sbin/service subagent-shell condrestart >/dev/null 2>&1 || :
fi
exit 0

%preun
if [ $1 = 0 ] ; then
  /sbin/service subagent-shell stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del subagent-shell
fi
exit 0

%changelog
* Wed Nov 23 2011 Serge <abrikus@gmail.com> 1.1.0.0-ssv1
-- Initial release
