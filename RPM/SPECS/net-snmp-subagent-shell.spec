Name:       net-snmp-subagent-shell
Version:    2.2.0.1
Release:    ssv1%{?dist}
Summary:    Net SNMP subagent extends snmd mib
License:    BSD
Group:      Monitoring
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot
BuildArch:  noarch
Packager:   Serge <abrikus@gmail.com>
Requires:   curl net-snmp
BuildRequires: automake autoconf
Provides: net-snmp-subagent
Obsoletes: net-snmp-subagent
URL: http://github.com/sergevs/net-snmp-subagent-shell

%description
Net SNMP subagent executes arbitrary commands and provide results via snmpd  

%prep
%setup 

%build
%__aclocal
%__automake --add-missing
%__autoconf
%configure

%install
%__rm -rf %buildroot
%makeinstall
%__mkdir_p %buildroot%_unitdir
%__mkdir_p %buildroot%_sysconfdir/sysconfig/
%__install -m 644 subagent-shell.service %buildroot%_unitdir/
%__install subagent-shell.options %buildroot%_sysconfdir/sysconfig/subagent-shell

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/*
%dir /etc/snmp/subagent-shell
%dir /etc/snmp/subagent-shell/mibs
%dir /etc/snmp/subagent-shell/conf.d
/etc/snmp/subagent-shell/mibs/*
/etc/snmp/subagent-shell/*.functions
%config(noreplace) %attr(444,root,root) /etc/snmp/subagent-shell/*-conf.xml
%_unitdir/*
%_sysconfdir/sysconfig/subagent-shell
%_mandir/man8/*

%post
%systemd_post subagent-shell.service

%preun
%systemd_preun subagent-shell.service

%postun
%systemd_postun_with_restart subagent-shell.service

%changelog
* Wed Nov 23 2011 Serge <abrikus@gmail.com> 1.1.0.0-ssv1
-- Initial release
