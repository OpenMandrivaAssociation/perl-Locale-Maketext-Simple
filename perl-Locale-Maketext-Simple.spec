%define upstream_name	Locale-Maketext-Simple
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

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
