bin_SCRIPTS = subagent-shell

basedir = $(sysconfdir)/snmp/subagent-shell
base_DATA =  *.xml subagent-shell-base.functions

mibsdir = $(basedir)/mibs
mibs_DATA = mibs/*
dist_mibs_DATA = mibs/*

man8ddir = $(mandir)/man8
man8d_DATA = subagent-shell.8
dist_man8d_DATA = subagent-shell.8

dist_base_DATA = *.xml subagent-shell-base.functions
dist_bin_SCRIPTS = subagent-shell

EXTRA_DIST = subagent-shell.init.rhel subagent-shell.options debian 

install-data-hook:
	$(mkdir_p) $(DESTDIR)$(basedir)/conf.d
