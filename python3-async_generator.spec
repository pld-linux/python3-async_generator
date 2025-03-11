#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Async generators and context managers for Python 3.5+
Summary(pl.UTF-8):	Asynchroniczne generatory i zarządcy kontekstu dla Pythona 3.5+
Name:		python3-async_generator
Version:	1.10
Release:	6
License:	Apache v2.0 or MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/async_generator/
Source0:	https://files.pythonhosted.org/packages/source/a/async_generator/async_generator-%{version}.tar.gz
# Source0-md5:	078a29b4afb3d7f38c097a530f042a55
URL:		https://pypi.org/project/async_generator/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinxcontrib-trio
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 3.6 added async generators (PEP-525). Python 3.7 adds some more
tools to make them usable, like contextlib.asynccontextmanager.

This library gives you all that back to Python 3.5.

%description -l pl.UTF-8
W Pythonie 3.6 zostały wprowadzone asynchroniczne generatory
(PEP-525). W Pythonie 3.7 doszło kilka nowych narzędzi, czyniących je
bardziej użytecznymi, jak contextlib.asynccontextmanager.

Ta biblioteka udostępnia to wszystko dla Pythona 3.5.

%package apidocs
Summary:	async_generator API documentation
Summary(pl.UTF-8):	Dokumentacja API async_generator
Group:		Documentation

%description apidocs
API documentation for async_generator.

%description apidocs -l pl.UTF-8
Dokumentacja API async_generator.

%prep
%setup -q -n async_generator-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest async_generator/_tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE LICENSE.MIT README.rst
%{py3_sitescriptdir}/async_generator
%{py3_sitescriptdir}/async_generator-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
