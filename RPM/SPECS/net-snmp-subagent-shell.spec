Name:       net-snmp-subagent-shell
Version:    2.0.0.0
Release:    ssv1
Summary:    Net SNMP subagent extends snmd mib
License:    BSD
Group:      Monitoring
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot
BuildArch:  noarch
Packager:   Serge <abrikus@gmail.com>
Requires:   curl ntp
BuildRequires: automake autoconf
Obsoletes: net-snmp-subagent
URL: http://github.com/sergevs/net-snmp-subagent-shell

%description
Net SNMP subagent executes arbitrary commands and provide results via snmpd  

%prep
%setup 

%build

%install
%__rm -rf %buildroot
%__aclocal
%__automake --add-missing
%__autoconf

%configure
%makeinstall

%files
%defattr(-,root,root)
%_bindir/*
%dir /etc/snmp/subagent-shell
%dir /etc/snmp/subagent-shell/mibs
%dir /etc/snmp/subagent-shell/conf.d
/etc/snmp/subagent-shell/mibs/*
/etc/snmp/subagent-shell/*.functions
%config(noreplace) %attr(444,root,root) /etc/snmp/subagent-shell/*-conf.xml
%_sysconfdir/init.d/subagent-shell
%_sysconfdir/sysconfig/subagent-shell.options
%_mandir/man8/*

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
