%define upstream_name	Locale-Maketext-Simple
%define upstream_version 0.20

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    %mkrel 1

License:	    MIT
Group:		    Development/Perl
Summary:	    Perl module to use other catalog formats in Maketext
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl(Locale::Maketext::Lexicon)

%description
Locale::Maketext::Simple is simple interface to Locale::Maketext::Lexicon,
a module providing lexicon-handling backends, for "Locale::Maketext" 
to read from other localization formats, such as PO files, MO files, 
or from databases via the "Tie" interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%check
%{__make} test
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Locale
%{_mandir}/man3/*

