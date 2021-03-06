# $Id$
# Authority: shuff
# Upstream: Stevan Little <stevan$iinteractive,com>
# needs new Scalar::Util
# ExcludeDist: el2 el3 el4 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-MOP

Summary: Meta Object Protocol for Perl 5
Name: perl-Class-MOP
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-MOP/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Class-MOP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(Carp)
BuildRequires: perl(Data::OptList)
BuildRequires: perl(Devel::GlobalDestruction)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils) >= 0.12
BuildRequires: perl(MRO::Compat) >= 0.05
BuildRequires: perl(Package::DeprecationManager) >= 0.10
BuildRequires: perl(Package::Stash) >= 0.13
BuildRequires: perl(Scalar::Util) >= 1.18
BuildRequires: perl(Sub::Name) >= 0.04
BuildRequires: perl(Task::Weaken)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny) >= 0.02
BuildRequires: perl >= 5.8.1
Requires: perl(Carp)
Requires: perl(Data::OptList)
Requires: perl(Devel::GlobalDestruction)
Requires: perl(List::MoreUtils) >= 0.12
Requires: perl(MRO::Compat) >= 0.05
Requires: perl(Package::DeprecationManager) >= 0.10
Requires: perl(Package::Stash) >= 0.13
Requires: perl(Scalar::Util) >= 1.18
Requires: perl(Sub::Name) >= 0.04
Requires: perl(Task::Weaken)
Requires: perl(Try::Tiny) >= 0.02
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup

%description
This module is a fully functioning meta object protocol for the Perl 5 object
system. It makes no attempt to change the behavior or characteristics of the
Perl 5 object system, only to create a protocol for its manipulation and
introspection.

That said, it does attempt to create the tools for building a rich set of
extensions to the Perl 5 object system. Every attempt has been made to abide by
the spirit of the Perl 5 object system that we all know and love.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Class::MOP.3pm*
%doc %{_mandir}/man3/Class::MOP::*.3pm*
%doc %{_mandir}/man3/metaclass.3pm*
%dir %{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/auto/Class/MOP/
%dir %{perl_vendorarch}/Class/
%{perl_vendorarch}/Class/MOP/
%{perl_vendorarch}/Class/MOP.pm
%{perl_vendorarch}/metaclass.pm

%changelog
* Tue Aug 23 2011 Steve Huff <shuff@vecna.org> - 1.12-1
- Updated to version 1.12 (>=el6 only).
- Split off perl-Class-MOP-1.01 into its own spec.

* Fri Feb 25 2011 Steve Huff <shuff@vecna.org> - 1.01-1
- Updated to version 1.01.
- Changed source URL.
- NB: later versions require a newer Moose that won't work on el5.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.98-1
- Updated to version 0.98.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.97-1
- Updated to version 0.97.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.95-2
- dependencies from yaml

* Tue Dec 01 2009 Steve Huff <shuff@vecna.org> - 0.95-1
- Updated to version 0.95.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 0.92-1
- Updated to version 0.92.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.91-1
- Updated to version 0.91.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.89-1
- Updated to version 0.89.

* Thu May 28 2009 Christoph Maser <cmr@financial.com>  0.84-1
- Updated to release 0.84.

* Thu May 28 2009 Christoph Maser <cmr@financial.com>  0.78-1
- Updated to release 0.78.

* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.67-1
- Updated to release 0.67.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Fri Aug 22 2008 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Updated to release 0.63.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.55-1
- Updated to release 0.55.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 0.53-1
- Updated to release 0.53.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.52-1
- Updated to release 0.52.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.51-1
- Updated to release 0.51.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.50-1
- Updated to release 0.50.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.48-1
- Updated to release 0.48.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.37-1
- Initial package. (using DAR)
