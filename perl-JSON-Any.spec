%define upstream_name	 JSON-Any
%define upstream_version 1.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Wrapper Class for the various JSON classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/JSON/JSON-Any-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::DWIW)
BuildRequires:	perl(JSON::Syck)
BuildRequires:	perl(JSON::XS)

BuildArch: noarch

%description
This module will provide a coherent API to bring together the various JSON
modules currently on CPAN. This module will allow you to code to any JSON
API and have it work regardless of which JSON module is actually installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files 
%{perl_vendorlib}/*
%{_mandir}/*/*


