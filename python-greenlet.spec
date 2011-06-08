%define module greenlet

Name:           python-%{module}
Version:        0.3.1
Release:        %mkrel 1
Summary:        Lightweight in-process concurrent programming
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/%{module}
Source0:        http://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

%package devel
Summary:        C development headers for python-greenlet
Group:          Development/Python
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains header files required for C modules development.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
chmod 644 benchmarks/*.py

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%files 
%defattr(-,root,root)
%{python_sitearch}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/python*/%{module}

