#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-compose
Version  : 1.24.1
Release  : 24
URL      : https://github.com/docker/compose/archive/1.24.1/compose-1.24.1.tar.gz
Source0  : https://github.com/docker/compose/archive/1.24.1/compose-1.24.1.tar.gz
Summary  : Multi-container orchestration for Docker
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-compose-bin = %{version}-%{release}
Requires: docker-compose-license = %{version}-%{release}
Requires: docker-compose-python = %{version}-%{release}
Requires: docker-compose-python3 = %{version}-%{release}
Requires: PySocks
Requires: PyYAML
Requires: backports.ssl_match_hostname
Requires: cached-property
Requires: certifi
Requires: chardet
Requires: docker
Requires: docker-py
Requires: docker-pycreds
Requires: dockerpty
Requires: docopt
Requires: idna
Requires: jsonschema
Requires: paramiko
Requires: requests
Requires: six
Requires: texttable
Requires: urllib3
Requires: websocket_client
BuildRequires : PySocks
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cached-property
BuildRequires : certifi
BuildRequires : chardet
BuildRequires : docker
BuildRequires : docker-py
BuildRequires : docker-pycreds
BuildRequires : dockerpty
BuildRequires : docopt
BuildRequires : idna
BuildRequires : jsonschema
BuildRequires : paramiko
BuildRequires : requests
BuildRequires : six
BuildRequires : texttable
BuildRequires : urllib3
BuildRequires : websocket_client
Patch1: 0001-Unfreeze-requests-dependency.patch
Patch2: 0002-Unfreeze-PyYAML-and-jsonschema.patch

%description
Docker Compose
==============
![Docker Compose](logo.png?raw=true "Docker Compose Logo")

%package bin
Summary: bin components for the docker-compose package.
Group: Binaries
Requires: docker-compose-license = %{version}-%{release}

%description bin
bin components for the docker-compose package.


%package license
Summary: license components for the docker-compose package.
Group: Default

%description license
license components for the docker-compose package.


%package python
Summary: python components for the docker-compose package.
Group: Default
Requires: docker-compose-python3 = %{version}-%{release}

%description python
python components for the docker-compose package.


%package python3
Summary: python3 components for the docker-compose package.
Group: Default
Requires: python3-core
Provides: pypi(docker_compose)
Requires: pypi(cached_property)
Requires: pypi(docker)
Requires: pypi(dockerpty)
Requires: pypi(docopt)
Requires: pypi(jsonschema)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(texttable)
Requires: pypi(websocket_client)

%description python3
python3 components for the docker-compose package.


%prep
%setup -q -n compose-1.24.1
cd %{_builddir}/compose-1.24.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588358258
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/docker-compose
cp %{_builddir}/compose-1.24.1/LICENSE %{buildroot}/usr/share/package-licenses/docker-compose/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docker-compose

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/docker-compose/8ff574408142cd6bbb2a1b83302de24cb7b35e8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
