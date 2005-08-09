# $Id$
# Authority: dries
# Upstream: Stephan Buys <sbproxy$icon,co,za>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kolab-Cyrus

Summary: Perl extension for interfacing with the Kolab Cyrus admin module
Name: perl-Kolab-Cyrus
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kolab-Cyrus/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STEPHANB/Kolab-Cyrus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.3

%description
Perl extension for interfacing with the Kolab Cyrus admin module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Kolab/
%{perl_vendorlib}/Kolab/Cyrus.pm

%changelog
* Sun Jul 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
