%define module	greenlet

Name:		python-%{module}
Version:	3.3.0
Release:	1
Summary:	Lightweight in-process concurrent programming
Group:		Development/Python
License:	MIT
URL:		https://pypi.python.org/pypi/greenlet
Source0:	https://github.com/python-greenlet/greenlet/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:  python-objgraph
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(psutil)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

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
export CFLAGS="%{optflags} -fno-tree-dominator-opts -fno-strict-aliasing"
export LDFLAGS="%{optflags} -lpython%{pyver}"
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE*
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info

%files devel
%license LICENSE*
%{_includedir}/python%{pyver}*/%{module}
