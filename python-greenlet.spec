%define module	greenlet
%define	rel		1
%if %mdkversion < 201100
%else
%endif

Name:           python-%{module}
Version:	0.4.15
Release:	1
Summary:        Lightweight in-process concurrent programming
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/%{module}
Source0:	https://files.pythonhosted.org/packages/f8/e8/b30ae23b45f69aa3f024b46064c0ac8e5fcb4f22ace0dca8d6f9c8bbe5e7/greenlet-0.4.15.tar.gz
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
PYTHONDONTWRITEBYTECODE= python setup.py build
chmod 644 benchmarks/*.py
pushd doc
export PYTHONPATH=`dir -1d ../build/lib* | head -1`
%__make html
popd

%install
python setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

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



