bin_SCRIPTS = subagent-shell
basedir = /etc/snmp
base_DATA =  *.xml subagent-shell-base.functions

mibsdir = $(basedir)/mibs
mibs_DATA = mibs/*

initdir = /etc/init.d
init_DATA = subagent-shell.init

install-data-hook:
	mv -v $(DESTDIR)$(initdir)/subagent-shell.init $(DESTDIR)$(initdir)/subagent-shell
