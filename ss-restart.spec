%global upstream le_platform_vendor_qcom_opensource_ss-restart
%global tag LE.QCLINUX.0.0-11500-K2C.0

Name:           ss-restart
Version:        1.0.0
Release:        1%{?dist}
Summary:        Qualcomm subsystem crash dump collection utility

License:        BSD-3-Clause-Clear
URL:            https://github.com/CodeLinaro-mirror/%{upstream}
# Release tag resolves to commit 533eb77f37cc3d7247eb3f59a5987e72402b07a7.
Source0:        https://github.com/CodeLinaro-mirror/%{upstream}/archive/%{tag}/%{name}-%{tag}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}

%description
ss-restart provides the subsystem_ramdump utility for collecting memory
dumps from Qualcomm subsystems. These dumps support failure analysis and
debugging of subsystem crashes. The package includes a systemd service
for running the collection utility.

%prep
%autosetup -n %{upstream}-%{tag}

%build
cd subsystem_ramdump
autoreconf -fiv
%configure --with-glib --with-systemd
%make_build

%install
cd subsystem_ramdump
%make_install subsystem_ramdump_systemddir=%{_unitdir}

%post
%systemd_post subsystem-ramdump.service

%preun
%systemd_preun subsystem-ramdump.service

%postun
%systemd_postun subsystem-ramdump.service

%files
%{_bindir}/subsystem_ramdump
%{_unitdir}/subsystem-ramdump.service

%changelog
* Mon Oct 26 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Build subsystem_ramdump from CodeLinaro release LE.QCLINUX.0.0-11500-K2C.0
- Correct the payload license to BSD-3-Clause-Clear
- Add systemd service lifecycle scriptlets
