bin_SCRIPTS = subagent-shell
basedir = $(sysconfdir)/snmp/subagent-shell
base_DATA =  *.xml subagent-shell-base.functions
initdir = $(sysconfdir)/init.d
mibsdir = $(basedir)/mibs
mibs_DATA = mibs/*
dist_mibs_DATA = mibs/*
dist_base_DATA = *.xml subagent-shell-base.functions
dist_bin_SCRIPTS = subagent-shell

install-data-hook:
	$(mkdir_p) $(DESTDIR)$(basedir)/conf.d; \
  if [ -f /etc/debian_version ]; then \
    echo "Init scripts and default file a part of debian package"; \
  elif [ -f /etc/redhat-release ]; then \
    $(mkdir_p) $(DESTDIR)$(initdir) $(DESTDIR)$(sysconfdir)/sysconfig; \
    $(INSTALL) subagent-shell.init.rhel $(DESTDIR)$(initdir)/subagent-shell; \
    $(INSTALL) subagent-shell.options $(DESTDIR)$(sysconfdir)/sysconfig; \
  else \
    echo "Release is not identified, please install init files by yourself"; \
  fi
