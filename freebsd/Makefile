# $FreeBSD$

PORTNAME=	net-snmp-subagent-shell
PORTVERSION=	2.3.0.1
CATEGORIES=	net-mgmt
MASTER_SITES=	https://github.com/sergevs/net-snmp-subagent-shell/releases/tag/${PORTVERSION}

MAINTAINER=	abrikus@gmail.com
COMMENT=	A complete implementation of net-snmp subagent written on perl. Can be used to define arbitrary functions and provide the results via snmp.

USE_RC_SUBR=    subagent_shell

USES=perl5
USE_PERL5=      run
USE_AUTOTOOLS=  aclocal:env automake:env autoconf:env

RUN_DEPENDS:=	p5-XML-Simple>=2.10:${PORTSDIR}/textproc/p5-XML-Simple \
		net-snmp>=5.5:${PORTSDIR}/net-mgmt/net-snmp

SUB_FILES=	pkg-message
SUB_LIST=	PERL=${PERL}

post-configure:
	@cd ${CONFIGURE_WRKSRC}; \
	aclocal; \
	automake --add-missing; \
	autoconf; \
	./configure

post-install:
	@mv ${STAGEDIR}${PREFIX}/bin/subagent-shell ${STAGEDIR}${PREFIX}/bin/subagent_shell

.include <bsd.port.mk>
