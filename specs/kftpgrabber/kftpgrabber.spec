# $Id$
# Authority: dag

Summary: Graphical FTP client for the K Desktop Environment.
Name: kftpgrabber
Version: 0.5.0
Release: 1.beta1
License: GPL
Group: Applications/Internet
URL: http://kftpgrabber.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://kftpgrabber.sf.net/releases/kftpgrabber-%{version}-beta1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.3.2, kdelibs-devel >= 3.2.0, openssl-devel >= 0.9.7

%description
KFTPGrabber is a graphical FTP client for KDE. It provides a nice GUI
for all file transfer operations, it supports encrypted connections
(both SSL and SFTP), site-to-site (FXP) transfers, a complete bookmark
system and also has a built in support for Zeroconf site discovery.

%prep
%setup -n %{name}-%{version}-beta1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 755)
%doc %{_datadir}/doc/HTML/en/kftpgrabber/
%{_bindir}/kftpgrabber
%{_datadir}/applications/kde/kftpgrabber.desktop
%{_datadir}/apps/kftpgrabber/
%{_datadir}/icons/hicolor/*/apps/kftpgrabber.png
%{_datadir}/services/kftpimportplugin_gftp.desktop
%{_datadir}/servicetypes/kftpbookmarkimportplugin.desktop
%{_includedir}/kftpgrabber/
%exclude %{_libdir}/libkftpinterfaces.la
%{_libdir}/libkftpinterfaces.so.0
%{_libdir}/libkftpinterfaces.so.0.0.0
%exclude %{_libdir}/kde3/kftpimportplugin_gftp.la
%{_libdir}/kde3/kftpimportplugin_gftp.so

%changelog
* Tue Nov 02 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1.beta1
- Added contributed SPEC files. (Kevin Smith)
