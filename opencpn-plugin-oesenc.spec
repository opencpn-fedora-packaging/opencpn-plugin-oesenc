%global commit 5b6bc712e85130ca1d080780ee9f4816b8f69940
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner bdbcat
%global project oesenc_pi
%global plugin oesenc

Name: opencpn-plugin-%{plugin}
Summary: oeSENC plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
oeSENC plugin for OpenCPN provides support for encrypted OpenCPN
vector charts. These are licensed and sourced from chart providers
like Hydrographic Offices. These - non free - charts must be installed
with appropriate encryption certificates in place. Chart source
o-charts.org

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_bindir}/oeserverd

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi
