#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.upgradecheck
Version  : 1.0.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/6a/7c/225ebe0fe533ddfa6ae793493109c0019d44ec83f399be8f85b95ffc37ae/oslo.upgradecheck-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6a/7c/225ebe0fe533ddfa6ae793493109c0019d44ec83f399be8f85b95ffc37ae/oslo.upgradecheck-1.0.0.tar.gz
Summary  : Common code for writing OpenStack upgrade checks
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.upgradecheck-license = %{version}-%{release}
Requires: oslo.upgradecheck-python = %{version}-%{release}
Requires: oslo.upgradecheck-python3 = %{version}-%{release}
Requires: Babel
Requires: oslo.config
Requires: oslo.i18n
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : pbr
BuildRequires : prettytable
Patch1: req.patch

%description
=================
oslo.upgradecheck
=================

Common code for writing OpenStack upgrade checks

This project contains the common code necessary for writing upgrade checks
in OpenStack projects. It includes a module (oslo_upgradecheck.upgradecheck)
for the common code as well as an example (oslo_upgradecheck.__main__) of
integrating that code into a project.

* Free software: Apache license
* Documentation: https://docs.openstack.org/oslo.upgradecheck/latest/
* Source: https://opendev.org/openstack/oslo.upgradecheck
* Bugs: https://bugs.launchpad.net/oslo.upgradecheck

%package license
Summary: license components for the oslo.upgradecheck package.
Group: Default

%description license
license components for the oslo.upgradecheck package.


%package python
Summary: python components for the oslo.upgradecheck package.
Group: Default
Requires: oslo.upgradecheck-python3 = %{version}-%{release}

%description python
python components for the oslo.upgradecheck package.


%package python3
Summary: python3 components for the oslo.upgradecheck package.
Group: Default
Requires: python3-core
Provides: pypi(oslo.upgradecheck)

%description python3
python3 components for the oslo.upgradecheck package.


%prep
%setup -q -n oslo.upgradecheck-1.0.0
cd %{_builddir}/oslo.upgradecheck-1.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583195134
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.upgradecheck
cp %{_builddir}/oslo.upgradecheck-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/oslo.upgradecheck/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.upgradecheck/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
