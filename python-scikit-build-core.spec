# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-scikit-build-core
Epoch: 100
Version: 0.10.7
Release: 1%{?dist}
BuildArch: noarch
Summary: Build backend for CMake based projects
License: MIT
URL: https://github.com/scikit-build/scikit-build-core/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools >= 42.0.0

%description
Scikit-build-core is a build backend for Python that uses CMake to build
extension modules. It has a simple yet powerful static configuration
system in pyproject.toml, and supports almost unlimited flexibility via
CMake. It was initially developed to support the demanding needs of
scientific users, but can build any sort of package that uses CMake.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-scikit-build-core
Summary: Build backend for CMake based projects
Requires: python3
Requires: python3-exceptiongroup >= 1.0
Requires: python3-importlib-metadata >= 4.13
Requires: python3-importlib-resources >= 1.3
Requires: python3-packaging >= 21.3
Requires: python3-pathspec >= 0.10.1
Requires: python3-tomli >= 1.2.2
Requires: python3-typing-extensions >= 3.10.0
Provides: python3-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-build-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-build-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-build-core) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-scikit-build-core
Scikit-build-core is a build backend for Python that uses CMake to build
extension modules. It has a simple yet powerful static configuration
system in pyproject.toml, and supports almost unlimited flexibility via
CMake. It was initially developed to support the demanding needs of
scientific users, but can build any sort of package that uses CMake.

%files -n python%{python3_version_nodots}-scikit-build-core
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-scikit-build-core
Summary: Build backend for CMake based projects
Requires: python3
Requires: python3-exceptiongroup >= 1.0
Requires: python3-importlib-metadata >= 4.13
Requires: python3-importlib-resources >= 1.3
Requires: python3-packaging >= 21.3
Requires: python3-pathspec >= 0.10.1
Requires: python3-tomli >= 1.2.2
Requires: python3-typing-extensions >= 3.10.0
Provides: python3-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-build-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-build-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-build-core) = %{epoch}:%{version}-%{release}

%description -n python3-scikit-build-core
Scikit-build-core is a build backend for Python that uses CMake to build
extension modules. It has a simple yet powerful static configuration
system in pyproject.toml, and supports almost unlimited flexibility via
CMake. It was initially developed to support the demanding needs of
scientific users, but can build any sort of package that uses CMake.

%files -n python3-scikit-build-core
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-scikit-build-core
Summary: Build backend for CMake based projects
Requires: python3
Requires: python3-exceptiongroup >= 1.0
Requires: python3-importlib-metadata >= 4.13
Requires: python3-importlib-resources >= 1.3
Requires: python3-packaging >= 21.3
Requires: python3-pathspec >= 0.10.1
Requires: python3-tomli >= 1.2.2
Requires: python3-typing-extensions >= 3.10.0
Provides: python3-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-build-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-build-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-build-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-build-core) = %{epoch}:%{version}-%{release}

%description -n python3-scikit-build-core
Scikit-build-core is a build backend for Python that uses CMake to build
extension modules. It has a simple yet powerful static configuration
system in pyproject.toml, and supports almost unlimited flexibility via
CMake. It was initially developed to support the demanding needs of
scientific users, but can build any sort of package that uses CMake.

%files -n python3-scikit-build-core
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
