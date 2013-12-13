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
Version:        0.4.1
Release:        1
Summary:        Lightweight in-process concurrent programming
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/%{module}
Source0:		http://pypi.python.org/packages/source/g/greenlet/greenlet-%{version}.zip
BuildRequires:  python-devel, python-setuptools, python-sphinx

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
%{__python} setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

%check
./run-tests.py

%files 
%doc doc/_build/html
%{py_platsitedir}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/python*/%{module}



%changelog
* Wed Aug 22 2012 Lev Givon <lev@mandriva.org> 0.4.0-1
+ Revision: 815588
- Update to 0.4.0.

* Wed Mar 21 2012 Lev Givon <lev@mandriva.org> 0.3.4-1
+ Revision: 785946
- Update to 0.3.4.

* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.3.1-1
+ Revision: 683252
- import python-greenlet


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.10.7
- first release for Mandriva


