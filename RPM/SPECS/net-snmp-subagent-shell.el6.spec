Name:       net-snmp-subagent-shell
Version:    2.2.0.3
Release:    ssv1%{?dist}
Summary:    Net SNMP subagent extends snmpd mib
License:    BSD
Group:      Monitoring
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot
BuildArch:  noarch
Packager:   Serge <abrikus@gmail.com>
Requires:   curl ntp
BuildRequires: automake autoconf
Provides: net-snmp-subagent
Obsoletes: net-snmp-subagent
URL: http://github.com/sergevs/net-snmp-subagent-shell

%description
Net SNMP subagent executes arbitrary commands and provide results via snmpd  

%prep
%setup 

%build
%__rm -rf %buildroot
%__aclocal
%__automake --add-missing
%__autoconf
%configure

%install
%makeinstall
%__install -d %buildroot%_sysconfdir/init.d
%__install subagent-shell.init.rhel %buildroot%_sysconfdir/init.d/subagent-shell
%__install -d %buildroot%_sysconfdir/sysconfig
%__install subagent-shell.options %buildroot%_sysconfdir/sysconfig

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/*
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
/sbin/chkconfig --add subagent-shell
if [ $? == 0 ]; then
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

# this section is required to smooth upgrade from net-snmp-subagent package
%triggerpostun -- net-snmp-subagent
if [ "$1" == "1" ]; then
  /sbin/chkconfig --add subagent-shell || :
  /sbin/service subagent-shell start >/dev/null 2>&1 || :
fi

%changelog
* Wed Nov 23 2011 Serge <abrikus@gmail.com> 1.1.0.0-ssv1
-- Initial release
