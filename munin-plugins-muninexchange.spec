# TODO:
#	- better descriptions?
#
%include	/usr/lib/rpm/macros.perl
Summary:	Munin plugins from MuninExchange
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange
Name:		munin-plugins-muninexchange
Version:	20130823
Release:	7
License:	GPL
Group:		Daemons
Source0:	https://github.com/munin-monitoring/contrib/tarball/master/%{name}.tar.gz
# Source0-md5:	d0b1caf2e18a0edc349184f51d7d0cb5
Patch0:		%{name}-postfix.patch
Patch1:		%{name}-other.patch
Patch2:		%{name}-php.patch
Patch3:		%{name}-samba.patch
Patch4:		%{name}-apache.patch
Patch5:		%{name}-passenger.patch
Patch6:		xen.patch
URL:		http://exchange.munin-monitoring.org/
BuildRequires:	dos2unix
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl		DateTime::Format::ISO8601 Sys::Virt Sys::Virt::.* VMware::.* File::Tail::Multi nvidia::ml WWW::Mechanize::TreeBuilder Sun::Solaris::Kstat

%description
This package contains plugins for Munin from MuninExchange repository
located at <https://github.com/munin-monitoring/contrib/>.

%description -l pl.UTF-8
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,
znajdującym się na <https://github.com/munin-monitoring/contrib/>.

%define	contrib_package()\
%package %1\
Summary:	Munin plugins from MuninExchange - %1\
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - %1\
Group:		Daemons\
Requires:	munin-node\
\
%description %1\
This package contains plugins for Munin from MuninExchange repository\
located at <https://github.com/munin-monitoring/contrib/>.\
\
%description %1 -l pl.UTF-8\
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,\
znajdującym się na <https://github.com/munin-monitoring/contrib/>.\
\
%files %1 -f %1.list\
%defattr(755,root,root,755)\
%{nil}

%prep
%setup -q -n munin-monitoring-contrib-538cdc9

find -type f -print0 | xargs -0 dos2unix

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

grep -r bin/env -l plugins/ | xargs sed -i -e '1{
	s,#!.*bin/env ruby,#!%{__ruby},
	s,#!.*bin/env python[^ ]*,#!%{__python},
	s,#!.*bin/env perl,#!%{__perl},
}'

find plugins/ -type f | xargs sed -i -e '1{
	s,#!.*/usr/local/bin/,#!/usr/bin/,
	s,#!.*/opt/csw/bin/ruby,#!%{__ruby},
	s,#!.*/usr/bin/bash,#!/bin/bash,
	s,#!.*/sbin/sh,#!/bin/sh,
}'

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%{__rm} -r plugins/asterisk/asterisk_*_fax_*
%{__rm} -r plugins/mail/dovecot

for f in plugins/apache/apache_byprojects/byprojects_* ; do
	%{__mv} $f plugins/apache/apache_byprojects/apache_$(basename $f)
done
for f in plugins/nginx/nginx_byprojects/byprojects_* ; do
	%{__mv} $f plugins/nginx/nginx_byprojects/nginx_$(basename $f)
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/munin/plugins/

for i in plugins/*; do
	[ -d $i ] || continue
	j=$(basename $i)
	>$j.list
	find $i/* -type f | while read f ; do
		if file $f | grep -qs script ; then
			ff=$(basename $f)
			echo "%{_datadir}/munin/plugins/$ff" >>$j.list
			install -p $f $RPM_BUILD_ROOT%{_datadir}/munin/plugins/
		fi
	done
done

%clean
rm -rf $RPM_BUILD_ROOT

%contrib_package amule
%contrib_package apache
%contrib_package apt
%contrib_package aris
%contrib_package asterisk
%contrib_package audit
%contrib_package backuppc
%contrib_package bacula
%contrib_package beboxsync
%contrib_package boinc
%contrib_package cacti
%contrib_package celery
%contrib_package ceph
%contrib_package chassis
%contrib_package cherokee
%contrib_package condor
%contrib_package cpan
%contrib_package currentcost
%contrib_package cyrus
%contrib_package db2
%contrib_package disk
%contrib_package djabberd
%contrib_package dovecot
%contrib_package drbd
%contrib_package drupal
%contrib_package dspam
%contrib_package dvb
%contrib_package dxtv
%contrib_package ejabberd
%contrib_package fax
%contrib_package firebird
%contrib_package forums
%contrib_package ftp
%contrib_package funkytown
%contrib_package games
%contrib_package geowebcache
%contrib_package glance
%contrib_package glassfish
%contrib_package google
%contrib_package gpu
%contrib_package gunicorn
%contrib_package hadoop
%contrib_package haproxy
%contrib_package healthcheck
%contrib_package heimdal
%contrib_package http
%contrib_package ipvs
%contrib_package java
%contrib_package joomla
%contrib_package kamailio
%contrib_package keystone
%contrib_package licensing
%contrib_package lighttpd
%contrib_package logins
%contrib_package lustre
%contrib_package mail
%contrib_package memcached
%contrib_package minecraft
%contrib_package moblock
%contrib_package mod_jk
%contrib_package mogilefs
%contrib_package mongodb
%contrib_package monit
%contrib_package mpd
%contrib_package mssql
%contrib_package munin
%contrib_package mysql
%contrib_package mythtv
%contrib_package nagios
%contrib_package network
%contrib_package newznab
%contrib_package nfs-freebsd
%contrib_package nginx
%contrib_package noaaport
%contrib_package nova
%contrib_package openvpn
%contrib_package openvz
%contrib_package oracle
%contrib_package ossec
%contrib_package other
%contrib_package passenger
%contrib_package php
%contrib_package postgresql
%contrib_package power5
%contrib_package powermta
%contrib_package printer
%contrib_package processes
%contrib_package prosody
%contrib_package puppet
%contrib_package qpid
%contrib_package qpsmtpd
%contrib_package rabbitmq
%contrib_package rackspace
%contrib_package radiator
%contrib_package reddit_karma
%contrib_package redis
%contrib_package relayd
%contrib_package requesttracker
%contrib_package riak
%contrib_package rsync
%contrib_package rtorrent
%contrib_package s3
%contrib_package sabnzbd
%contrib_package samba
%contrib_package san
%contrib_package scalix
%contrib_package security
%contrib_package senderscore
%contrib_package sensors
%contrib_package services
%contrib_package sge
%contrib_package sickbeard
%contrib_package slony
%contrib_package smstools
%contrib_package snmp
%contrib_package solr
%contrib_package sourceds
%contrib_package sphinx
%contrib_package spotweb
%contrib_package squeezebox
%contrib_package squid
%contrib_package streaming
%contrib_package swift
%contrib_package syslog
%contrib_package system
%contrib_package teamspeak
%contrib_package thin
%contrib_package time
%contrib_package tomcat
%contrib_package trafic_ro
%contrib_package tv
%contrib_package ubuntu
%contrib_package ultramonkey
%contrib_package unicorn
%contrib_package ups
%contrib_package varnish
%contrib_package vdr
%contrib_package virtualization
%contrib_package voip
%contrib_package voldemort
%contrib_package weather
%contrib_package websphere
%contrib_package wiki
%contrib_package wowza
%contrib_package wuala
%contrib_package xastir
%contrib_package xbnbt
%contrib_package yacy
%contrib_package zeo
%contrib_package zfs
%contrib_package zimbra
%contrib_package zope
