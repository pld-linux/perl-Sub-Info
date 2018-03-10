#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	pdir	Sub
%define	pnam	Info
%include	/usr/lib/rpm/macros.perl
Summary:	Sub::Info - Tool for inspecting subroutines
Summary(pl.UTF-8):	Sub::Info - Narzędzie do sprawdzania podprogramów
Name:		perl-Sub-Info
Version:	0.002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	335345b534fc0539c894050f7814cbda
URL:		http://search.cpan.org/dist/Sub-Info/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to inspect subroutines.

%description -l pl.UTF-8
Narzędzie do sprawdzania podprogramów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Sub/Info.pm
%{_mandir}/man3/Sub::Info.3pm*
