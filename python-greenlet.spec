%define module	greenlet
%define	name	python-%{module}
%define	version	0.4.0
%define	rel		1
%if %mdkversion < 201100
%define release	%mkrel %{rel}
%else
%define release	%{rel}
%endif

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Lightweight in-process concurrent programming
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/%{module}
Source0:		http://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.zip
BuildRequires:  python-devel, python-setuptools, python-sphinx
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
PYTHONDONTWRITEBYTECODE= %{__python} setup.py build
chmod 644 benchmarks/*.py
pushd doc
export PYTHONPATH=`dir -1d ../build/lib* | head -1`
%__make html
popd

%install
rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} --install-purelib=%{python_sitearch}

%check
./run-tests.py

%files 
%defattr(-,root,root)
%doc doc/_build/html
%{python_sitearch}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/python*/%{module}

