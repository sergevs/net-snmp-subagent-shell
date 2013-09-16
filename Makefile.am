bin_SCRIPTS = subagent-shell
basedir = $(sysconfdir)/snmp
base_DATA =  *.xml subagent-shell-base.functions

initdir = $(sysconfdir)/init.d

mibsdir = $(basedir)/mibs
mibs_DATA = mibs/*

install-data-hook:
	if [ -f /etc/debian_version ]; then \
    $(mkdir_p) $(DESTDIR)$(initdir) $(DESTDIR)$(sysconfdir)/default; \
    $(INSTALL) subagent-shell.init.debian $(DESTDIR)$(initdir)/subagent-shell; \
    $(INSTALL) subagent-shell.options $(DESTDIR)$(sysconfdir)/default/subagent-shell; \
  elif [ -f /etc/redhat-release ]; then \
    $(mkdir_p) $(DESTDIR)$(initdir) $(DESTDIR)$(sysconfdir)/sysconfig; \
    $(INSTALL) subagent-shell.init.rhel $(DESTDIR)$(initdir)/subagent-shell; \
    $(INSTALL) subagent-shell.options $(DESTDIR)$(sysconfdir)/sysconfig; \
  else \
    echo "Release is not identified, please install init files by yourself"; \
  fi
