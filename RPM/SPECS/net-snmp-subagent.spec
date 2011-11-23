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
%__mkdir_p %buildroot/etc/snmp/subagent/conf.d
%__install common %buildroot/etc/snmp/subagent
%__install snmpd-* %buildroot/etc/snmp/subagent
%__install *.functions %buildroot/etc/snmp/subagent
%__install reload %buildroot/etc/snmp/subagent

%files
%attr(755,root,root) %dir /etc/snmp/subagent
%attr(755,root,root) %dir /etc/snmp/subagent/conf.d
%attr(444,root,root) /etc/snmp/subagent/common
%attr(744,root,root) /etc/snmp/subagent/snmpd-poller
%attr(444,root,root) /etc/snmp/subagent/snmpd-poller-agent
%attr(744,root,root) /etc/snmp/subagent/reload
%attr(444,root,root) /etc/snmp/subagent/*.functions
%config(noreplace) %attr(444,root,root) /etc/snmp/subagent/*.conf

%changelog
* Wed Nov 23 2011 Serge V. Sergeev <serge@phorm.com> 1.1.0.0-ssv1
- Checked out revision 9. from snmpd-agent/tags/1.1.0.0/

