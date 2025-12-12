%define module	greenlet

Name:           python-%{module}
Version:	3.2.2
Release:	2
Summary:        Lightweight in-process concurrent programming
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/%{module}
Source0:        https://github.com/python-greenlet/greenlet/archive/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  python-devel, python-setuptools

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

%package devel
Summary:        C development headers for python-greenlet
Group:          Development/Python
Requires:       %{name} = %{EVRD}

%description devel
This package contains header files required for C modules development.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files 
%{py_platsitedir}/*

%files devel
%{_includedir}/python*/%{module}
