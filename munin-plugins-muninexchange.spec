# TODO:
#	- better descriptions?
#
%define	contrib_package()\
%package %1\
Summary:	Munin plugins from MuninExchange - %1\
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - %1\
Group:		Daemons\
Requires:	munin-node\
\
%description %1\
This package contains plugins for Munin from MuninExchange repository\
located at https://github.com/munin-monitoring/contrib/.\
\
%description %1 -l pl.UTF-8\
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,\
znajdującym się na https://github.com/munin-monitoring/contrib/.\
\
%files %1 -f %1.list\
%defattr(644,root,root,755)\
%{nil}

%include	/usr/lib/rpm/macros.perl
Summary:	Munin plugins from MuninExchange
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange
Name:		munin-plugins-muninexchange
Version:	20130823
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	https://github.com/munin-monitoring/contrib/tarball/master/%{name}.tar.gz
# Source0-md5:	d0b1caf2e18a0edc349184f51d7d0cb5
Patch0:		%{name}-vserver.patch
Patch1:		%{name}-postfix.patch
Patch2:		%{name}-other.patch
Patch3:		%{name}-php.patch
Patch4:		%{name}-openvpn.patch
Patch5:		%{name}-samba.patch
Patch6:		%{name}-apache.patch
Patch7:		%{name}-passenger.patch
URL:		http://exchange.munin-monitoring.org/
BuildRequires:	dos2unix
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package databases
Summary:	Munin plugins from MuninExchange - databases
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - databases
Group:		Daemons
Requires:	munin-node
Obsoletes:	munin-plugins-muninexchange-mysql

%description databases
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description databases -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package network
Summary:	Munin plugins from MuninExchange - network
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - network
Group:		Daemons
Requires:	munin-node
Obsoletes:	munin-plugins-muninexchange-powerdns

%description network
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description network -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package other
Summary:	Munin plugins from MuninExchange - other
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - other
Group:		Daemons
Requires:	munin-node
Obsoletes:	munin-plugins-muninexchange-amavis
Obsoletes:	munin-plugins-muninexchange-amule
Obsoletes:	munin-plugins-muninexchange-apache
Obsoletes:	munin-plugins-muninexchange-apt
Obsoletes:	munin-plugins-muninexchange-asterisk
Obsoletes:	munin-plugins-muninexchange-bacula
Obsoletes:	munin-plugins-muninexchange-bind
Obsoletes:	munin-plugins-muninexchange-boinc
Obsoletes:	munin-plugins-muninexchange-condor
Obsoletes:	munin-plugins-muninexchange-disk
Obsoletes:	munin-plugins-muninexchange-flashmediaserver
Obsoletes:	munin-plugins-muninexchange-freeradius
Obsoletes:	munin-plugins-muninexchange-games
Obsoletes:	munin-plugins-muninexchange-groupwise
Obsoletes:	munin-plugins-muninexchange-heimdal
Obsoletes:	munin-plugins-muninexchange-icecast
Obsoletes:	munin-plugins-muninexchange-iperf
Obsoletes:	munin-plugins-muninexchange-java
Obsoletes:	munin-plugins-muninexchange-mediawiki
Obsoletes:	munin-plugins-muninexchange-memcache
Obsoletes:	munin-plugins-muninexchange-mysql
Obsoletes:	munin-plugins-muninexchange-mythtv
Obsoletes:	munin-plugins-muninexchange-nfs
Obsoletes:	munin-plugins-muninexchange-openldap
Obsoletes:	munin-plugins-muninexchange-openvpn
Obsoletes:	munin-plugins-muninexchange-oracle
Obsoletes:	munin-plugins-muninexchange-php
Obsoletes:	munin-plugins-muninexchange-postfix
Obsoletes:	munin-plugins-muninexchange-postgresql
Obsoletes:	munin-plugins-muninexchange-printing
Obsoletes:	munin-plugins-muninexchange-processes
Obsoletes:	munin-plugins-muninexchange-proftpd
Obsoletes:	munin-plugins-muninexchange-puppet
Obsoletes:	munin-plugins-muninexchange-pure-ftpd
Obsoletes:	munin-plugins-muninexchange-qmail
Obsoletes:	munin-plugins-muninexchange-radiator
Obsoletes:	munin-plugins-muninexchange-rtorrent
Obsoletes:	munin-plugins-muninexchange-samba
Obsoletes:	munin-plugins-muninexchange-scalix
Obsoletes:	munin-plugins-muninexchange-sensors
Obsoletes:	munin-plugins-muninexchange-squid
Obsoletes:	munin-plugins-muninexchange-teamspeak
Obsoletes:	munin-plugins-muninexchange-time
Obsoletes:	munin-plugins-muninexchange-tor
Obsoletes:	munin-plugins-muninexchange-ups
Obsoletes:	munin-plugins-muninexchange-varnish
Obsoletes:	munin-plugins-muninexchange-vmware
Obsoletes:	munin-plugins-muninexchange-vserver
Obsoletes:	munin-plugins-muninexchange-xen
Obsoletes:	munin-plugins-muninexchange-yum
Obsoletes:	munin-plugins-muninexchange-zyxel

%description other
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description other -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package services
Summary:	Munin plugins from MuninExchange - services
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - services
Group:		Daemons
Requires:	munin-node
Obsoletes:	munin-plugins-muninexchange-icecast
Obsoletes:	munin-plugins-muninexchange-postfix
Obsoletes:	munin-plugins-muninexchange-proftpd
Obsoletes:	munin-plugins-muninexchange-pure-ftpd
Obsoletes:	munin-plugins-muninexchange-sensors
Obsoletes:	munin-plugins-muninexchange-squid
Obsoletes:	munin-plugins-muninexchange-time
Obsoletes:	munin-plugins-muninexchange-varnish

%description services
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description services -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package system
Summary:	Munin plugins from MuninExchange - system
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - system
Group:		Daemons
Requires:	munin-node
Obsoletes:	munin-plugins-muninexchange-disk

%description system
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description system -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package web-servers
Summary:	Munin plugins from MuninExchange - web servers
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - web servers
Group:		Daemons
Requires:	munin-node
Obsoletes:	munin-plugins-muninexchange-apache
Obsoletes:	munin-plugins-muninexchange-nginx
Obsoletes:	munin-plugins-muninexchange-tomcat

%description web-servers
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description web-servers -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%prep
%setup -q -n munin-monitoring-contrib-538cdc9

find -type f -print0 | xargs -0 dos2unix

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1

grep -r bin/env -l . | xargs sed -i -e '1{
	s,#!.*bin/env ruby,#!%{__ruby},
	s,#!.*bin/env python[^ ]*,#!%{__python},
	s,#!.*bin/env perl,#!%{__perl},
}'

sed -i -e 's|#!.*/usr/local/bin/|#!/usr/bin/|' */*

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/munin/plugins/

for i in *; do
	[ -d $i ] || continue
	echo "%defattr(644,root,root,755)" > $i.list
	(cd $i; for f in *; do echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f"; done) >> $i.list
done

cp -a */* $RPM_BUILD_ROOT%{_datadir}/munin/plugins/
chmod 755 $RPM_BUILD_ROOT%{_datadir}/munin/plugins/*

touch $RPM_BUILD_ROOT/dupa
echo /dupa >dupa.list

%clean
rm -rf $RPM_BUILD_ROOT

%files databases -f databases.list
%defattr(644,root,root,755)

%files network -f network.list
%defattr(644,root,root,755)

%files other -f other.list
%defattr(644,root,root,755)

%files services -f services.list
%defattr(644,root,root,755)

%files system -f system.list
%defattr(644,root,root,755)

%files web-servers -f web-servers.list
%defattr(644,root,root,755)

%contrib_package dupa
