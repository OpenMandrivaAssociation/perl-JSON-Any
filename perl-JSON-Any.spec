%define module	JSON-Any
%define name	perl-%{module}
%define version	1.19
%define release	%mkrel 0.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wrapper Class for the various JSON classes
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/JSON/%{module}-%{version}.tar.gz
Buildrequires:	perl(JSON)
Buildrequires:	perl(JSON::XS)
Buildrequires:	perl(JSON::DWIW)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module will provide a coherent API to bring together the various JSON
modules currently on CPAN. This module will allow you to code to any JSON
API and have it work regardless of which JSON module is actually installed.

%prep
%setup -q -n %{module}-%{version}

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
