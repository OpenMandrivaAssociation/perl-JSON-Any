%define upstream_name	 JSON-Any
%define upstream_version 1.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.30
Release:	1

Summary:	Wrapper Class for the various JSON classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/JSON/JSON-Any-1.30.tar.gz

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.290.0-1mdv2011.0
+ Revision: 684769
- update to new version 1.29

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.280.0-1
+ Revision: 673800
- update to new version 1.28

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.270.0-1
+ Revision: 654092
- update to new version 1.27

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.260.0-1
+ Revision: 650311
- update to new version 1.26

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.250.0-1mdv2011.0
+ Revision: 601898
- update to new version 1.25

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2011.0
+ Revision: 596611
- update to 1.24

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.220.0-1mdv2011.0
+ Revision: 461540
- adding missing buildrequires:
- update to 1.22

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.0
+ Revision: 393423
- update to 1.21
- using %%perl_convert_version
- fixed license field

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-0.1mdv2010.0
+ Revision: 371726
- new version

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.04-0.2mdv2009.0
+ Revision: 245452
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.04-0.1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.04-0.1mdv2008.0
+ Revision: 19748
- buildrequires
- 1.04
- Create perl-JSON-Any


