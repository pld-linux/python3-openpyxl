%define 	module	openpyxl
Summary:	A Python library to read/write Excel 2007 xlsx/xlsm files
Summary(pl.UTF-8):	Biblioteka Pythona do odczytu/zapisu plików w formacie Excela 2007 xlsx/xlsm
Name:		python3-%{module}
Version:	3.1.5
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/openpyxl
Source0:	https://files.pythonhosted.org/packages/source/o/openpyxl/%{module}-%{version}.tar.gz
# Source0-md5:	13e63bdced2dbca00c8741eea3ecfa1c
URL:		https://openpyxl.readthedocs.io/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Openpyxl is a pure Python reader and writer of Excel OpenXML files. It
was initially ported from the PHPExcel project.

%description -l pl.UTF-8
Openpyxl to czysto pythonowa biblioteka do odczytu i zapisu plików
Excel OpenXML. Początkowo był to port projektu PHPExcel.

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
%doc AUTHORS.rst LICENCE.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
