# $Id$
# Authority: matthias

# Python name and version, use "--define 'python python2'"
%{!?python: %{expand: %%define python python}}
%define pyminver 2.1

Summary: Creates a common metadata repository
Name: createrepo
Version: 0.3.4
Release: 1
License: GPL
Group: System Environment/Base
Source: http://linux.duke.edu/projects/metadata/generate/%{name}-%{version}.tar.gz
URL: http://linux.duke.edu/projects/metadata/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: rpm-python, %{python} >= %{pyminver}, rpm >= 4.1.1, libxml2-python

%description
This utility will generate a common metadata repository from a directory of
rpm packages


%prep
%setup


%build


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_bindir}/createrepo
%{_datadir}/createrepo/


%changelog
* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 0.3.4-1
- Picked up package.

* Mon Jul 19 2004 Seth Vidal <skvidal@phy.duke.edu>
- re-enable groups
- update num to 0.3.4

* Tue Jun  8 2004 Seth Vidal <skvidal@phy.duke.edu>
- update to the format
- versioned deps
- package counts
- uncompressed checksum in repomd.xml

* Fri Apr 16 2004 Seth Vidal <skvidal@phy.duke.edu>
- 0.3.2 - small addition of -p flag

* Sun Jan 18 2004 Seth Vidal <skvidal@phy.duke.edu>
- I'm an idiot

* Sun Jan 18 2004 Seth Vidal <skvidal@phy.duke.edu>
- 0.3

* Tue Jan 13 2004 Seth Vidal <skvidal@phy.duke.edu>
- 0.2 - 

* Sat Jan 10 2004 Seth Vidal <skvidal@phy.duke.edu>
- first packaging

