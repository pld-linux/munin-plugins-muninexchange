#
# TODO:
#	- better descriptions?
#
%include	/usr/lib/rpm/macros.perl
Summary:	Munin plugins from MuninExchange
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange
Name:		munin-plugins-muninexchange
Version:	20091204
Release:	2
License:	GPL
Group:		Daemons
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	f4d293b86cb6bb7ed30a9c67559a2c52
Patch0:		%{name}-vserver.patch
Patch1:		%{name}-postfix.patch
Patch2:		%{name}-other.patch
Patch3:		%{name}-php.patch
Patch4:		%{name}-openvpn.patch
Patch5:		%{name}-samba.patch
Patch6:		%{name}-apache.patch
Patch7:		%{name}-heimdal.patch
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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node
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
Requires:	munin-node

%description apt
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 apt
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package asterisk
Summary:	Munin plugins from MuninExchange - asterisk
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - asterisk
Group:		Daemons
Requires:	munin-node

%description asterisk
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 asterisk
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package bacula
Summary:	Munin plugins from MuninExchange - bacula
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - bacula
Group:		Daemons
Requires:	munin-node

%description bacula
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 bacula
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package bind
Summary:	Munin plugins from MuninExchange - bind
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - bind
Group:		Daemons
Requires:	munin-node

%description bind
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 bind
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package boinc
Summary:	Munin plugins from MuninExchange - boinc
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - boinc
Group:		Daemons
Requires:	munin-node

%description boinc
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 boinc
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package condor
Summary:	Munin plugins from MuninExchange - condor
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - condor
Group:		Daemons
Requires:	munin-node

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
Requires:	munin-node

%description disk
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 disk
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package flashmediaserver
Summary:	Munin plugins from MuninExchange - flashmediaserver
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - flashmediaserver
Group:		Daemons
Requires:	munin-node

%description flashmediaserver
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 flashmediaserver
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package freeradius
Summary:	Munin plugins from MuninExchange - freeradius
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - freeradius
Group:		Daemons
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

%description groupwise
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 groupwise
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package heimdal
Summary:	Munin plugins from MuninExchange - heimdal
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - heimdal
Group:		Daemons
Requires:	munin-node

%description heimdal
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 heimdal
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package icecast
Summary:	Munin plugins from MuninExchange - icecast
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - icecast
Group:		Daemons
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

%description proftpd
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 proftpd
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package puppet
Summary:	Munin plugins from MuninExchange - puppet
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - puppet
Group:		Daemons
Requires:	munin-node

%description puppet
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 puppet
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package pure-ftpd
Summary:	Munin plugins from MuninExchange - pure-ftpd
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - pure-ftpd
Group:		Daemons
Requires:	munin-node

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
Requires:	munin-node

%description qmail
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 qmail
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package radiator
Summary:	Munin plugins from MuninExchange - radiator
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - radiator
Group:		Daemons
Requires:	munin-node

%description radiator
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 radiator
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package rtorrent
Summary:	Munin plugins from MuninExchange - rtorrent
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - rtorrent
Group:		Daemons
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

%description teamspeak
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 teamspeak
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package time
Summary:	Munin plugins from MuninExchange - time
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - time
Group:		Daemons
Requires:	munin-node

%description time
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 time
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package tomcat
Summary:	Munin plugins from MuninExchange - tomcat
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - tomcat
Group:		Daemons
Requires:	munin-node

%description tomcat
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 tomcat
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package tor
Summary:	Munin plugins from MuninExchange - tor
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - tor
Group:		Daemons
Requires:	munin-node

%description tor
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 tor
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package ups
Summary:	Munin plugins from MuninExchange - ups
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - ups
Group:		Daemons
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

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
Requires:	munin-node

%description yum
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 yum
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%package zyxel
Summary:	Munin plugins from MuninExchange - zyxel
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - zyxel
Group:		Daemons
Requires:	munin-node

%description zyxel
This package contains plugins for Munin from MuninExchange
repository located at http://muninexchange.projects.linpro.no/.

%description -l pl.UTF-8 zyxel
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na http://muninexchange.projects.linpro.no/.

%prep
%setup -q

find -type f -print0 | xargs -0 dos2unix

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/munin/plugins/

for i in * ; do
	if [ -d $i ]; then
		if [ $i = "other" ]; then
			echo "%defattr(644,root,root,755)" >other.list
			echo "%defattr(644,root,root,755)" >heimdal.list
			(cd $i ; for f in * ; do [[ $f = heimdal* ]] || echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f" ; done) >>other.list
			(cd $i ; for f in * ; do [[ $f = heimdal* ]] && echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f" ; done) >>heimdal.list
		else
			echo "%defattr(644,root,root,755)" >$i.list
			(cd $i ; for f in * ; do echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f" ; done) >>$i.list
		fi
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
%files asterisk -f asterisk.list
%files bacula -f bacula.list
%files bind -f bind.list
%files boinc -f boinc.list
%files condor -f condor.list
%files disk -f disk.list
%files flashmediaserver -f flashmediaserver.list
%files freeradius -f freeradius.list
%files games -f games.list
%files groupwise -f groupwise.list
%files heimdal -f heimdal.list
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
%files puppet -f puppet.list
%files pure-ftpd -f pure-ftpd.list
%files qmail -f qmail.list
%files radiator -f radiator.list
%files rtorrent -f rtorrent.list
%files samba -f samba.list
%files scalix -f scalix.list
%files sensors -f sensors.list
%files squid -f squid.list
%files system -f system.list
%files teamspeak -f teamspeak.list
%files time -f time.list
%files tomcat -f tomcat.list
%files tor -f tor.list
%files ups -f ups.list
%files varnish -f varnish.list
%files vmware -f vmware.list
%files vserver -f vserver.list
%files xen -f xen.list
%files yum -f yum.list
%files zyxel -f zyxel.list
