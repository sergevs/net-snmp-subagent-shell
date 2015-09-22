bin_SCRIPTS = subagent-shell subagent-shell-test

basedir = $(sysconfdir)/snmp/subagent-shell
base_DATA =  *.xml subagent-shell-base.functions

mibsdir = $(basedir)/mibs
mibs_DATA = mibs/*
dist_mibs_DATA = mibs/*

man8ddir = $(mandir)/man8
man8d_DATA = subagent-shell.8
dist_man8d_DATA = subagent-shell.8

dist_base_DATA = subagent-shell-conf.xml subagent-shell-functions-conf.xml subagent-shell-base.functions

EXTRA_DIST = subagent-shell.init.rhel  subagent-shell.service subagent-shell.options debian 

install-data-hook:
	$(mkdir_p) $(DESTDIR)$(basedir)/conf.d

check:	
	perl -c subagent-shell-base.functions
	perl -c subagent-shell

test:
	if test -z "$(SNMPD)" ; then \
		echo "snmpd is not found"; \
		exit 1; \
	fi 
	echo $(SNMPWALK) snmpwalk is not found
	if test -z "$(SNMPWALK)" ; then \
		echo "snmpwalk is not found"; \
		exit 1; \
	fi 
	make all
	make check
	/bin/sh subagent-shell-test

clean:
	rm -rf stest subagent-shell subagent-shell-test
