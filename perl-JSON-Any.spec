%define module	JSON-Any
%define name	perl-%{module}
%define version	1.04
%define release	%mkrel 0.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wrapper Class for the various JSON classes
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	perl-devel
Buildrequires:	perl(JSON)

Buildarch:	noarch

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
