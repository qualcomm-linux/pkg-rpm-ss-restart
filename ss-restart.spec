%global debug_package %{nil}

Name:           ss-restart
Version:        1.0.0
Release:        2%{?dist}
Summary:        Qualcomm subsystem ramdump restart utility

License:        Qualcomm-Technologies-Inc.-Proprietary
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260624.1/prebuilt_resolute/%{name}_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
ss-restart is packaged from a Qualcomm Linux release tarball.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/%{name}/arm64/. %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
