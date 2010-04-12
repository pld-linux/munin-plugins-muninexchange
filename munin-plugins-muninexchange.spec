# TODO:
#	- better descriptions?
#
%include	/usr/lib/rpm/macros.perl
Summary:	Munin plugins from MuninExchange
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange
Name:		munin-plugins-muninexchange
Version:	20091204
Release:	3
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

%package amavis
Summary:	Munin plugins from MuninExchange - amavis
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - amavis
Group:		Daemons
Requires:	munin-node

%description amavis
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description amavis -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package amule
Summary:	Munin plugins from MuninExchange - amule
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - amule
Group:		Daemons
Requires:	munin-node

%description amule
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description amule -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package apache
Summary:	Munin plugins from MuninExchange - apache
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - apache
Group:		Daemons
Requires:	munin-node
Requires:	perl(Linux::Smaps)

%description apache
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description apache -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package apt
Summary:	Munin plugins from MuninExchange - apt
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - apt
Group:		Daemons
Requires:	munin-node

%description apt
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description apt -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package asterisk
Summary:	Munin plugins from MuninExchange - asterisk
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - asterisk
Group:		Daemons
Requires:	munin-node

%description asterisk
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description asterisk -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package bacula
Summary:	Munin plugins from MuninExchange - bacula
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - bacula
Group:		Daemons
Requires:	munin-node

%description bacula
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description bacula -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package bind
Summary:	Munin plugins from MuninExchange - bind
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - bind
Group:		Daemons
Requires:	munin-node

%description bind
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description bind -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package boinc
Summary:	Munin plugins from MuninExchange - boinc
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - boinc
Group:		Daemons
Requires:	munin-node

%description boinc
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description boinc -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package condor
Summary:	Munin plugins from MuninExchange - condor
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - condor
Group:		Daemons
Requires:	munin-node

%description condor
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description condor -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package disk
Summary:	Munin plugins from MuninExchange - disk
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - disk
Group:		Daemons
Requires:	munin-node

%description disk
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description disk -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package flashmediaserver
Summary:	Munin plugins from MuninExchange - flashmediaserver
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - flashmediaserver
Group:		Daemons
Requires:	munin-node

%description flashmediaserver
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description flashmediaserver -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package freeradius
Summary:	Munin plugins from MuninExchange - freeradius
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - freeradius
Group:		Daemons
Requires:	munin-node

%description freeradius
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description freeradius -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package games
Summary:	Munin plugins from MuninExchange - games
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - games
Group:		Daemons
Requires:	munin-node

%description games
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description games -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package groupwise
Summary:	Munin plugins from MuninExchange - groupwise
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - groupwise
Group:		Daemons
Requires:	munin-node

%description groupwise
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description groupwise -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package heimdal
Summary:	Munin plugins from MuninExchange - heimdal
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - heimdal
Group:		Daemons
Requires:	munin-node

%description heimdal
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description heimdal -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package icecast
Summary:	Munin plugins from MuninExchange - icecast
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - icecast
Group:		Daemons
Requires:	munin-node

%description icecast
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description icecast -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package iperf
Summary:	Munin plugins from MuninExchange - iperf
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - iperf
Group:		Daemons
Requires:	munin-node

%description iperf
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description iperf -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package java
Summary:	Munin plugins from MuninExchange - java
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - java
Group:		Daemons
Requires:	munin-node

%description java
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description java -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package mediawiki
Summary:	Munin plugins from MuninExchange - mediawiki
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - mediawiki
Group:		Daemons
Requires:	munin-node

%description mediawiki
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description mediawiki -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package memcache
Summary:	Munin plugins from MuninExchange - memcache
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - memcache
Group:		Daemons
Requires:	munin-node

%description memcache
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description memcache -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package mysql
Summary:	Munin plugins from MuninExchange - mysql
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - mysql
Group:		Daemons
Requires:	munin-node

%description mysql
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description mysql -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package mythtv
Summary:	Munin plugins from MuninExchange - mythtv
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - mythtv
Group:		Daemons
Requires:	munin-node

%description mythtv
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description mythtv -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package network
Summary:	Munin plugins from MuninExchange - network
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - network
Group:		Daemons
Requires:	munin-node

%description network
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description network -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package nfs
Summary:	Munin plugins from MuninExchange - nfs
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - nfs
Group:		Daemons
Requires:	munin-node

%description nfs
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description nfs -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package nginx
Summary:	Munin plugins from MuninExchange - nginx
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - nginx
Group:		Daemons
Requires:	munin-node

%description nginx
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description nginx -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package openldap
Summary:	Munin plugins from MuninExchange - openldap
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - openldap
Group:		Daemons
Requires:	munin-node

%description openldap
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description openldap -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package openvpn
Summary:	Munin plugins from MuninExchange - openvpn
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - openvpn
Group:		Daemons
Requires:	munin-node

%description openvpn
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description openvpn -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package oracle
Summary:	Munin plugins from MuninExchange - oracle
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - oracle
Group:		Daemons
Requires:	munin-node

%description oracle
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description oracle -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package other
Summary:	Munin plugins from MuninExchange - other
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - other
Group:		Daemons
Requires:	munin-node

%description other
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description other -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package php
Summary:	Munin plugins from MuninExchange - php
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - php
Group:		Daemons
Requires:	munin-node

%description php
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description php -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package postfix
Summary:	Munin plugins from MuninExchange - postfix
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - postfix
Group:		Daemons
Requires:	munin-node

%description postfix
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description postfix -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package postgresql
Summary:	Munin plugins from MuninExchange - postgresql
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - postgresql
Group:		Daemons
Requires:	munin-node

%description postgresql
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description postgresql -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package powerdns
Summary:	Munin plugins from MuninExchange - powerdns
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - powerdns
Group:		Daemons
Requires:	munin-node

%description powerdns
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description powerdns -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package printing
Summary:	Munin plugins from MuninExchange - printing
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - printing
Group:		Daemons
Requires:	munin-node

%description printing
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description printing -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package processes
Summary:	Munin plugins from MuninExchange - processes
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - processes
Group:		Daemons
Requires:	munin-node

%description processes
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description processes -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package proftpd
Summary:	Munin plugins from MuninExchange - proftpd
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - proftpd
Group:		Daemons
Requires:	munin-node

%description proftpd
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description proftpd -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package puppet
Summary:	Munin plugins from MuninExchange - puppet
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - puppet
Group:		Daemons
Requires:	munin-node

%description puppet
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description puppet -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package pure-ftpd
Summary:	Munin plugins from MuninExchange - pure-ftpd
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - pure-ftpd
Group:		Daemons
Requires:	munin-node

%description pure-ftpd
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description pure-ftpd -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package qmail
Summary:	Munin plugins from MuninExchange - qmail
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - qmail
Group:		Daemons
Requires:	munin-node

%description qmail
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description qmail -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package radiator
Summary:	Munin plugins from MuninExchange - radiator
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - radiator
Group:		Daemons
Requires:	munin-node

%description radiator
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description radiator -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package rtorrent
Summary:	Munin plugins from MuninExchange - rtorrent
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - rtorrent
Group:		Daemons
Requires:	munin-node

%description rtorrent
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description rtorrent -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package samba
Summary:	Munin plugins from MuninExchange - samba
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - samba
Group:		Daemons
Requires:	munin-node

%description samba
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description samba -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package scalix
Summary:	Munin plugins from MuninExchange - scalix
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - scalix
Group:		Daemons
Requires:	munin-node

%description scalix
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description scalix -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package sensors
Summary:	Munin plugins from MuninExchange - sensors
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - sensors
Group:		Daemons
Requires:	munin-node

%description sensors
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description sensors -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package squid
Summary:	Munin plugins from MuninExchange - squid
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - squid
Group:		Daemons
Requires:	munin-node

%description squid
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description squid -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package system
Summary:	Munin plugins from MuninExchange - system
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - system
Group:		Daemons
Requires:	munin-node

%description system
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description system -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package teamspeak
Summary:	Munin plugins from MuninExchange - teamspeak
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - teamspeak
Group:		Daemons
Requires:	munin-node

%description teamspeak
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description teamspeak -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package time
Summary:	Munin plugins from MuninExchange - time
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - time
Group:		Daemons
Requires:	munin-node

%description time
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description time -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package tomcat
Summary:	Munin plugins from MuninExchange - tomcat
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - tomcat
Group:		Daemons
Requires:	munin-node

%description tomcat
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description tomcat -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package tor
Summary:	Munin plugins from MuninExchange - tor
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - tor
Group:		Daemons
Requires:	munin-node

%description tor
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description tor -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package ups
Summary:	Munin plugins from MuninExchange - ups
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - ups
Group:		Daemons
Requires:	munin-node

%description ups
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description ups -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package varnish
Summary:	Munin plugins from MuninExchange - varnish
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - varnish
Group:		Daemons
Requires:	munin-node

%description varnish
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description varnish -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package vmware
Summary:	Munin plugins from MuninExchange - vmware
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - vmware
Group:		Daemons
Requires:	munin-node

%description vmware
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description vmware -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package vserver
Summary:	Munin plugins from MuninExchange - vserver
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - vserver
Group:		Daemons
Requires:	munin-node

%description vserver
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description vserver -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package xen
Summary:	Munin plugins from MuninExchange - xen
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - xen
Group:		Daemons
Requires:	munin-node

%description xen
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description xen -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package yum
Summary:	Munin plugins from MuninExchange - yum
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - yum
Group:		Daemons
Requires:	munin-node

%description yum
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description yum -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

%package zyxel
Summary:	Munin plugins from MuninExchange - zyxel
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - zyxel
Group:		Daemons
Requires:	munin-node

%description zyxel
This package contains plugins for Munin from MuninExchange repository
located at <http://muninexchange.projects.linpro.no/>.

%description zyxel -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <http://muninexchange.projects.linpro.no/>.

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

grep -r bin/env -l . | xargs sed -i -e '1{
	s,#!.*bin/env ruby,#!%{__ruby},
	s,#!.*bin/env python2.5,#!%{__python},
	s,#!.*bin/env python,#!%{__python},
	s,#!.*bin/env perl,#!%{__perl},
}'

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/munin/plugins/

for i in *; do
	if [ -d $i ]; then
		if [ $i = "other" ]; then
			echo "%defattr(644,root,root,755)" > other.list
			echo "%defattr(644,root,root,755)" > heimdal.list
			(cd $i; for f in *; do [[ $f = heimdal* ]] || echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f"; done) >> other.list
			(cd $i; for f in *; do [[ $f = heimdal* ]] && echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f"; done) >> heimdal.list
		else
			echo "%defattr(644,root,root,755)" > $i.list
			(cd $i; for f in *; do echo "%attr(755,root,root) %{_datadir}/munin/plugins/$f"; done) >> $i.list
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
%defattr(644,root,root,755)
%files amule -f amule.list
%defattr(644,root,root,755)
%files apache -f apache.list
%defattr(644,root,root,755)
%files apt -f apt.list
%defattr(644,root,root,755)
%files asterisk -f asterisk.list
%defattr(644,root,root,755)
%files bacula -f bacula.list
%defattr(644,root,root,755)
%files bind -f bind.list
%defattr(644,root,root,755)
%files boinc -f boinc.list
%defattr(644,root,root,755)
%files condor -f condor.list
%defattr(644,root,root,755)
%files disk -f disk.list
%defattr(644,root,root,755)
%files flashmediaserver -f flashmediaserver.list
%defattr(644,root,root,755)
%files freeradius -f freeradius.list
%defattr(644,root,root,755)
%files games -f games.list
%defattr(644,root,root,755)
%files groupwise -f groupwise.list
%defattr(644,root,root,755)
%files heimdal -f heimdal.list
%defattr(644,root,root,755)
%files icecast -f icecast.list
%defattr(644,root,root,755)
%files iperf -f iperf.list
%defattr(644,root,root,755)
%files java -f java.list
%defattr(644,root,root,755)
%files mediawiki -f mediawiki.list
%defattr(644,root,root,755)
%files memcache -f memcache.list
%defattr(644,root,root,755)
%files mysql -f mysql.list
%defattr(644,root,root,755)
%files mythtv -f mythtv.list
%defattr(644,root,root,755)
%files network -f network.list
%defattr(644,root,root,755)
%files nfs -f nfs.list
%defattr(644,root,root,755)
%files nginx -f nginx.list
%defattr(644,root,root,755)
%files openldap -f openldap.list
%defattr(644,root,root,755)
%files openvpn -f openvpn.list
%defattr(644,root,root,755)
%files oracle -f oracle.list
%defattr(644,root,root,755)
%files other -f other.list
%defattr(644,root,root,755)
%files php -f php.list
%defattr(644,root,root,755)
%files postfix -f postfix.list
%defattr(644,root,root,755)
%files postgresql -f postgresql.list
%defattr(644,root,root,755)
%files powerdns -f powerdns.list
%defattr(644,root,root,755)
%files printing -f printing.list
%defattr(644,root,root,755)
%files processes -f processes.list
%defattr(644,root,root,755)
%files proftpd -f proftpd.list
%defattr(644,root,root,755)
%files puppet -f puppet.list
%defattr(644,root,root,755)
%files pure-ftpd -f pure-ftpd.list
%defattr(644,root,root,755)
%files qmail -f qmail.list
%defattr(644,root,root,755)
%files radiator -f radiator.list
%defattr(644,root,root,755)
%files rtorrent -f rtorrent.list
%defattr(644,root,root,755)
%files samba -f samba.list
%defattr(644,root,root,755)
%files scalix -f scalix.list
%defattr(644,root,root,755)
%files sensors -f sensors.list
%defattr(644,root,root,755)
%files squid -f squid.list
%defattr(644,root,root,755)
%files system -f system.list
%defattr(644,root,root,755)
%files teamspeak -f teamspeak.list
%defattr(644,root,root,755)
%files time -f time.list
%defattr(644,root,root,755)
%files tomcat -f tomcat.list
%defattr(644,root,root,755)
%files tor -f tor.list
%defattr(644,root,root,755)
%files ups -f ups.list
%defattr(644,root,root,755)
%files varnish -f varnish.list
%defattr(644,root,root,755)
%files vmware -f vmware.list
%defattr(644,root,root,755)
%files vserver -f vserver.list
%defattr(644,root,root,755)
%files xen -f xen.list
%defattr(644,root,root,755)
%files yum -f yum.list
%defattr(644,root,root,755)
%files zyxel -f zyxel.list
%defattr(644,root,root,755)
