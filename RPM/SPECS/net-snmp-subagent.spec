Name:       net-snmp-subagent
Version: 1.1.0.0
Release:    ssv1
Summary:    Net SNMP subagent extends snmd mib
License:    GPL
Group:      Monitoring
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot
BuildArch:  noarch
Packager:   Serge <abrikus@gmail.com>

%description
Net SNMP subagent executes arbitrary commands and provide results via snmpd  

%prep
%setup 

%build

%install
%__rm -rf %buildroot
cd snmpd-agent 
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_sysconfdir/init.d
%__mkdir_p %buildroot%_sysconfdir/sysconfig
%__mkdir_p %buildroot/etc/snmp/subagent/{conf.d,mibs}
%__install subagent-shell %buildroot%_bindir
%__install subagent-shell{.conf,-base.functions,-functions.conf} %buildroot/etc/snmp/subagent
%__install mibs/* %buildroot/etc/snmp/subagent/mibs
%__install subagent-shell.init %buildroot%_sysconfdir/init.d/subagent-shell
%__install subagent-shell.options %buildroot%_sysconfdir/sysconfig

%files
%defattr(-,root,root)
%_bindir/*
%dir /etc/snmp/subagent
%dir /etc/snmp/subagent/mibs
%dir /etc/snmp/subagent/conf.d
/etc/snmp/subagent/mibs/*
/etc/snmp/subagent/*.functions
%config(noreplace) %attr(444,root,root) /etc/snmp/subagent/*.conf
%_sysconfdir/init.d/subagent-shell
%_sysconfdir/sysconfig/subagent-shell.options

%post
/sbin/chkconfig --add subagent-shell
grep -P '^perl do.*/etc/snmp/subagent/snmpd-poller-agent' /etc/snmp/snmpd.conf
if [ $? == 0 ]; then
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
- Checked out revision 9. from snmpd-agent/tags/1.1.0.0/

