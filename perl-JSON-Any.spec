%define upstream_name	 JSON-Any
%define upstream_version 1.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Wrapper Class for the various JSON classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/JSON/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl(JSON)
Buildrequires:	perl(JSON::DWIW)
Buildrequires:	perl(JSON::Syck)
Buildrequires:	perl(JSON::XS)

Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module will provide a coherent API to bring together the various JSON
modules currently on CPAN. This module will allow you to code to any JSON
API and have it work regardless of which JSON module is actually installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/*/*
