# $Id$
# Authority: cmr
# Upstream: Vincent Pit <perl$profvince,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Variable-Magic

Summary: Associate user-defined magic to variables from Perl
Name: perl-Variable-Magic
Version: 0.35
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Variable-Magic/

Source: http://www.cpan.org/modules/by-module/Variable/Variable-Magic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.008
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl >= 1:5.008

%description
Associate user-defined magic to variables from Perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
%doc %{_mandir}/man3/Variable::Magic.3pm*
%dir %{perl_vendorarch}/auto/Variable/
%{perl_vendorarch}/auto/Variable/Magic/
%dir %{perl_vendorarch}/Variable/
%{perl_vendorarch}/Variable/Magic.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.35-1
- Initial package. (using DAR)