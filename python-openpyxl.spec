# Conditional build:
%bcond_without  tests   # do not perform "make test"

%define 	module	openpyxl
Summary:	A Python library to read/write Excel 2007 xlsx/xlsm files
Summary(pl.UTF-8):	Biblioteka umożliwiająca tworzenie plików w formacie xlsx/xlsm dla języka Python.
Name:		python-%{module}
Version:	1.6.1
Release:	2
License:	MIT/Expat
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	d0d92b3b8128609be93a044ce3dac3f8
URL:		http://bitbucket.org/ericgazoni/openpyxl/wiki/Home
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Openpyxl is a pure python reader and writer of Excel OpenXML files. It
is ported from the PHPExcel project

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

#%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/reader
%{py_sitescriptdir}/%{module}/reader/*.py[co]
%dir %{py_sitescriptdir}/%{module}/shared
%{py_sitescriptdir}/%{module}/shared/*.py[co]
%dir %{py_sitescriptdir}/%{module}/shared/compat
%{py_sitescriptdir}/%{module}/shared/compat/*.py[co]
%dir %{py_sitescriptdir}/%{module}/writer
%{py_sitescriptdir}/%{module}/writer/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
