Name:		python-resolvelib
Version:	1.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/resolvelib/resolvelib-%{version}.tar.gz
Summary:	Resolve abstract dependencies into concrete ones
URL:		https://pypi.org/project/resolvelib/
License:	ISC License
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

%description
Resolve abstract dependencies into concrete ones

%prep
%autosetup -p1 -n resolvelib-%{version}

%files
%{py_sitedir}/resolvelib
%{py_sitedir}/resolvelib-*.*-info
