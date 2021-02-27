%define 	module	openpyxl
Summary:	A Python library to read/write Excel 2007 xlsx/xlsm files
Summary(pl.UTF-8):	Biblioteka umożliwiająca tworzenie plików w formacie xlsx/xlsm dla języka Python.
Name:		python3-%{module}
Version:	3.0.6
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	bfcd5a08491e4ac72c61d87d2bb22bb5
URL:		https://openpyxl.readthedocs.io
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Openpyxl is a pure python reader and writer of Excel OpenXML files. It
is ported from the PHPExcel project

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-*.egg-info
