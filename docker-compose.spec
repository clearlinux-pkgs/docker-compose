#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-compose
Version  : 1.23.2
Release  : 12
URL      : https://github.com/docker/compose/archive/1.23.2.tar.gz
Source0  : https://github.com/docker/compose/archive/1.23.2.tar.gz
Summary  : No detailed summary available
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
Requires: enum34
Requires: functools32
Requires: idna
Requires: ipaddress
Requires: jsonschema
Requires: requests
Requires: six
Requires: texttable
Requires: urllib3
Requires: websocket_client
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cached-property
BuildRequires : docker-py
BuildRequires : dockerpty
BuildRequires : docopt
BuildRequires : jsonschema
BuildRequires : requests
BuildRequires : six
BuildRequires : texttable
BuildRequires : websocket_client
Patch1: 0001-Allow-requests-2.21.patch

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

%description python3
python3 components for the docker-compose package.


%prep
%setup -q -n compose-1.23.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550879242
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/docker-compose
cp LICENSE %{buildroot}/usr/share/package-licenses/docker-compose/LICENSE
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
/usr/share/package-licenses/docker-compose/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
