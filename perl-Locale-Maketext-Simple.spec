%define upstream_name	Locale-Maketext-Simple
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

License:	MIT
Group:		Development/Perl
Summary:	Perl module to use other catalog formats in Maketext
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildArch:	noarch
Requires:	perl(Locale::Maketext::Lexicon)

%description
Locale::Maketext::Simple is simple interface to Locale::Maketext::Lexicon,
a module providing lexicon-handling backends, for "Locale::Maketext" 
to read from other localization formats, such as PO files, MO files, 
or from databases via the "Tie" interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Locale
%{_mandir}/man3/*

%changelog
* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-3mdv2011.0
+ Revision: 554271
- rebuild

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-2mdv2010.0
+ Revision: 420980
- rebuild

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 418653
- update to 0.21

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 399586
- adding missing requires: & buildrequires:
- update to 0.20 for real this time
- using %%perl_convert_version

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.20

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.18-4mdv2009.0
+ Revision: 257648
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.18-3mdv2009.0
+ Revision: 245703
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.18-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2007.0
- New version 0.18

* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2007.0
- New version 0.17

* Thu May 04 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- New version
- Change license

* Wed May 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdk
- New release 0.15

* Tue May 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk
- New release 0.14

* Sat Apr 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- New release 0.13
- %%mkrel
- better source URL

* Mon Jun 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-5mdk 
- don't ship useless emtpy dirs
- spec cleanup
- better url
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-4mdk 
- removed MANIFEST
- added missing doc files

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-2mdk 
- rebuild

* Fri Apr 02 2004 Michael Scherer <misc@mandrake.org> 0.12-1mdk 
- First MandrakeSoft Package

