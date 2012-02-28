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
%__mkdir_p %buildroot/etc/snmp/subagent/{conf.d,mibs}
%__install subagent-shell %buildroot%_bindir
%__install subagent-shell{.conf,-base.functions,-functions.conf} %buildroot/etc/snmp/subagent
%__install mibs/* %buildroot/etc/snmp/subagent/mibs
%__install subagent-shell.init %buildroot%_sysconfdir/init.d/subagent-shell

%files
%attr(755,root,root) %_bindir/*
%attr(755,root,root) %dir /etc/snmp/subagent
%attr(755,root,root) %dir /etc/snmp/subagent/mibs
%attr(755,root,root) %dir /etc/snmp/subagent/conf.d
%attr(755,root,root) /etc/snmp/subagent/mibs/*
%attr(444,root,root) /etc/snmp/subagent/*.functions
%config(noreplace) %attr(444,root,root) /etc/snmp/subagent/*.conf
%attr(755,root,root) %_sysconfdir/init.d/subagent-shell

%post
/sbin/chkconfig --add subagent-shell

%postun
/sbin/chkconfig --del subagent-shell

%changelog
* Wed Nov 23 2011 Serge <abrikus@gmail.com> 1.1.0.0-ssv1
- Checked out revision 9. from snmpd-agent/tags/1.1.0.0/

