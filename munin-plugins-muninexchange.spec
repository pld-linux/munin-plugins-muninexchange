#
# TODO:
#	- better descriptions?
#
%include	/usr/lib/rpm/macros.perl
Summary:	Munin plugins from MuninExchange
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange
Name:		munin-plugins-muninexchange
Version:	20081128
Release:	1.3
License:	GPL
Group:		Daemons
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	a8622f88eb7105220d358a8d7d764c96
Patch0:		%{name}-vserver.patch
Patch1:		%{name}-postfix.patch
Patch2:		%{name}-other.patch
Patch3:		%{name}-php.patch
URL:		http://muninexchange.projects.linpro.no/
BuildRequires:	dos2unix
BuildRequires:	perl-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package amavis
Summary:	Munin plugins from MuninExchange - amavis
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - amavis
Group:		Daemons
Requires:	munin-common

%description amavis
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 amavis
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package amule
Summary:	Munin plugins from MuninExchange - amule
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - amule
Group:		Daemons
Requires:	munin-common

%description amule
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 amule
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package apache
Summary:	Munin plugins from MuninExchange - apache
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - apache
Group:		Daemons
Requires:	munin-common
Requires:	perl(Linux::Smaps)

%description apache
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 apache
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package apt
Summary:	Munin plugins from MuninExchange - apt
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - apt
Group:		Daemons
Requires:	munin-common

%description apt
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 apt
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package bind
Summary:	Munin plugins from MuninExchange - bind
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - bind
Group:		Daemons
Requires:	munin-common

%description bind
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 bind
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package condor
Summary:	Munin plugins from MuninExchange - condor
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - condor
Group:		Daemons
Requires:	munin-common

%description condor
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 condor
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package disk
Summary:	Munin plugins from MuninExchange - disk
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - disk
Group:		Daemons
Requires:	munin-common

%description disk
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 disk
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package freeradius
Summary:	Munin plugins from MuninExchange - freeradius
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - freeradius
Group:		Daemons
Requires:	munin-common

%description freeradius
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 freeradius
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package games
Summary:	Munin plugins from MuninExchange - games
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - games
Group:		Daemons
Requires:	munin-common

%description games
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 games
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package groupwise
Summary:	Munin plugins from MuninExchange - groupwise
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - groupwise
Group:		Daemons
Requires:	munin-common

%description groupwise
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 groupwise
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package icecast
Summary:	Munin plugins from MuninExchange - icecast
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - icecast
Group:		Daemons
Requires:	munin-common

%description icecast
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 icecast
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package iperf
Summary:	Munin plugins from MuninExchange - iperf
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - iperf
Group:		Daemons
Requires:	munin-common

%description iperf
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 iperf
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package java
Summary:	Munin plugins from MuninExchange - java
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - java
Group:		Daemons
Requires:	munin-common

%description java
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 java
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package mediawiki
Summary:	Munin plugins from MuninExchange - mediawiki
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - mediawiki
Group:		Daemons
Requires:	munin-common

%description mediawiki
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 mediawiki
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package memcache
Summary:	Munin plugins from MuninExchange - memcache
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - memcache
Group:		Daemons
Requires:	munin-common

%description memcache
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 memcache
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package mysql
Summary:	Munin plugins from MuninExchange - mysql
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - mysql
Group:		Daemons
Requires:	munin-common

%description mysql
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 mysql
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package mythtv
Summary:	Munin plugins from MuninExchange - mythtv
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - mythtv
Group:		Daemons
Requires:	munin-common

%description mythtv
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 mythtv
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package network
Summary:	Munin plugins from MuninExchange - network
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - network
Group:		Daemons
Requires:	munin-common

%description network
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 network
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package nfs
Summary:	Munin plugins from MuninExchange - nfs
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - nfs
Group:		Daemons
Requires:	munin-common

%description nfs
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 nfs
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package nginx
Summary:	Munin plugins from MuninExchange - nginx
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - nginx
Group:		Daemons
Requires:	munin-common

%description nginx
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 nginx
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package openldap
Summary:	Munin plugins from MuninExchange - openldap
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - openldap
Group:		Daemons
Requires:	munin-common

%description openldap
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 openldap
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package openvpn
Summary:	Munin plugins from MuninExchange - openvpn
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - openvpn
Group:		Daemons
Requires:	munin-common

%description openvpn
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 openvpn
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package oracle
Summary:	Munin plugins from MuninExchange - oracle
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - oracle
Group:		Daemons
Requires:	munin-common

%description oracle
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 oracle
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package other
Summary:	Munin plugins from MuninExchange - other
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - other
Group:		Daemons
Requires:	munin-common

%description other
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 other
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package php
Summary:	Munin plugins from MuninExchange - php
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - php
Group:		Daemons
Requires:	munin-common

%description php
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 php
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package postfix
Summary:	Munin plugins from MuninExchange - postfix
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - postfix
Group:		Daemons
Requires:	munin-common

%description postfix
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 postfix
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package postgresql
Summary:	Munin plugins from MuninExchange - postgresql
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - postgresql
Group:		Daemons
Requires:	munin-common

%description postgresql
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 postgresql
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package powerdns
Summary:	Munin plugins from MuninExchange - powerdns
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - powerdns
Group:		Daemons
Requires:	munin-common

%description powerdns
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 powerdns
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package printing
Summary:	Munin plugins from MuninExchange - printing
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - printing
Group:		Daemons
Requires:	munin-common

%description printing
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 printing
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package processes
Summary:	Munin plugins from MuninExchange - processes
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - processes
Group:		Daemons
Requires:	munin-common

%description processes
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 processes
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package proftpd
Summary:	Munin plugins from MuninExchange - proftpd
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - proftpd
Group:		Daemons
Requires:	munin-common

%description proftpd
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 proftpd
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package pure-ftpd
Summary:	Munin plugins from MuninExchange - pure-ftpd
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - pure-ftpd
Group:		Daemons
Requires:	munin-common

%description pure-ftpd
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 pure-ftpd
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package qmail
Summary:	Munin plugins from MuninExchange - qmail
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - qmail
Group:		Daemons
Requires:	munin-common

%description qmail
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 qmail
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package rtorrent
Summary:	Munin plugins from MuninExchange - rtorrent
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - rtorrent
Group:		Daemons
Requires:	munin-common

%description rtorrent
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 rtorrent
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package samba
Summary:	Munin plugins from MuninExchange - samba
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - samba
Group:		Daemons
Requires:	munin-common

%description samba
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 samba
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package scalix
Summary:	Munin plugins from MuninExchange - scalix
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - scalix
Group:		Daemons
Requires:	munin-common

%description scalix
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 scalix
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package sensors
Summary:	Munin plugins from MuninExchange - sensors
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - sensors
Group:		Daemons
Requires:	munin-common

%description sensors
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 sensors
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package squid
Summary:	Munin plugins from MuninExchange - squid
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - squid
Group:		Daemons
Requires:	munin-common

%description squid
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 squid
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package system
Summary:	Munin plugins from MuninExchange - system
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - system
Group:		Daemons
Requires:	munin-common

%description system
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 system
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package teamspeak
Summary:	Munin plugins from MuninExchange - teamspeak
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - teamspeak
Group:		Daemons
Requires:	munin-common

%description teamspeak
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 teamspeak
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package tomcat
Summary:	Munin plugins from MuninExchange - tomcat
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - tomcat
Group:		Daemons
Requires:	munin-common

%description tomcat
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 tomcat
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package ups
Summary:	Munin plugins from MuninExchange - ups
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - ups
Group:		Daemons
Requires:	munin-common

%description ups
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 ups
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package varnish
Summary:	Munin plugins from MuninExchange - varnish
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - varnish
Group:		Daemons
Requires:	munin-common

%description varnish
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 varnish
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package vmware
Summary:	Munin plugins from MuninExchange - vmware
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - vmware
Group:		Daemons
Requires:	munin-common

%description vmware
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 vmware
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package vserver
Summary:	Munin plugins from MuninExchange - vserver
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - vserver
Group:		Daemons
Requires:	munin-common

%description vserver
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 vserver
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package xen
Summary:	Munin plugins from MuninExchange - xen
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - xen
Group:		Daemons
Requires:	munin-common

%description xen
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 xen
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package yum
Summary:	Munin plugins from MuninExchange - yum
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - yum
Group:		Daemons
Requires:	munin-common

%description yum
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 yum
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.


%prep
%setup -q

find -type f -print0 | xargs -0 dos2unix

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/munin/plugins/

for i in * ; do
	if [ -d $i ]; then
		echo "%defattr(644,root,root,755)" >$i.list
		(cd $i ; for f in * ; do echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f" ; done) >>$i.list
	fi
done

cp -a */* $RPM_BUILD_ROOT%{_datadir}/munin/plugins/
chmod 755 $RPM_BUILD_ROOT%{_datadir}/munin/plugins/*

for i in $RPM_BUILD_ROOT%{_datadir}/munin/plugins/* ; do
	sed -i -e 's|#!.*/usr/local/bin/|#!/usr/bin/|' "$i"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files amavis -f amavis.list
%files amule -f amule.list
%files apache -f apache.list
%files apt -f apt.list
%files bind -f bind.list
%files condor -f condor.list
%files disk -f disk.list
%files freeradius -f freeradius.list
%files games -f games.list
%files groupwise -f groupwise.list
%files icecast -f icecast.list
%files iperf -f iperf.list
%files java -f java.list
%files mediawiki -f mediawiki.list
%files memcache -f memcache.list
%files mysql -f mysql.list
%files mythtv -f mythtv.list
%files network -f network.list
%files nfs -f nfs.list
%files nginx -f nginx.list
%files openldap -f openldap.list
%files openvpn -f openvpn.list
%files oracle -f oracle.list
%files other -f other.list
%files php -f php.list
%files postfix -f postfix.list
%files postgresql -f postgresql.list
%files powerdns -f powerdns.list
%files printing -f printing.list
%files processes -f processes.list
%files proftpd -f proftpd.list
%files pure-ftpd -f pure-ftpd.list
%files qmail -f qmail.list
%files rtorrent -f rtorrent.list
%files samba -f samba.list
%files scalix -f scalix.list
%files sensors -f sensors.list
%files squid -f squid.list
%files system -f system.list
%files teamspeak -f teamspeak.list
%files tomcat -f tomcat.list
%files ups -f ups.list
%files varnish -f varnish.list
%files vmware -f vmware.list
%files vserver -f vserver.list
%files xen -f xen.list
%files yum -f yum.list
