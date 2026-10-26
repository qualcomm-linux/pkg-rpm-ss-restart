<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# ss-restart RPM - CentOS Stream 10

ss-restart provides the subsystem_ramdump utility for collecting memory
dumps from Qualcomm subsystems. These dumps support failure analysis and
debugging of subsystem crashes. The package includes a systemd service
for running the collection utility.

The [`c10s`](https://github.com/qualcomm-linux/pkg-rpm-ss-restart/tree/c10s) branch contains
the CentOS Stream 10 RPM packaging, built from the open-source
[subsystem_ramdump](https://github.com/CodeLinaro-mirror/le_platform_vendor_qcom_opensource_ss-restart/tree/LE.QCLINUX.0.0-11500-K2C.0/subsystem_ramdump)
component in the CodeLinaro mirror.
Check out that branch to access the spec file and `sources`.

## Package

| Field | Value |
|---|---|
| Package | ss-restart |
| Summary | Qualcomm subsystem crash dump collection utility |
| Version | 1.0.0 |
| Release | 2 |
| Architecture | aarch64 |
| License | BSD-3-Clause-Clear |
| Upstream release | [LE.QCLINUX.0.0-11500-K2C.0](https://github.com/CodeLinaro-mirror/le_platform_vendor_qcom_opensource_ss-restart/releases/tag/LE.QCLINUX.0.0-11500-K2C.0) |
| Upstream commit | 533eb77f37cc3d7247eb3f59a5987e72402b07a7 |
| Source | ss-restart-LE.QCLINUX.0.0-11500-K2C.0.tar.gz |
| Source checksum | See sources |

The RPM version follows upstream's `AC_INIT` version (`1.0.0`). The Qualcomm
release tag identifies the source snapshot used for this build.

The package installs:

- /usr/bin/subsystem_ramdump
- /usr/lib/systemd/system/subsystem-ramdump.service

The service runs `subsystem_ramdump` with `Restart=always`. Installation applies
the system's preset policy; uninstalling the package stops and disables the
service. Package upgrades do not automatically restart an active dump collector.

## Files

- ss-restart.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. The source tarball is resolved from the dist-git `sources` file and the spec `Source0` URL.

## Build

The spec builds `subsystem_ramdump/` with Autotools, GLib, and systemd support.
Build dependencies are declared in the spec and installed by qcom-rpm-utils in
its CentOS Stream 10 builder container.

Download the upstream release archive and build with qcom-rpm-utils:

    curl --fail --location \
      --output /path/to/ss-restart-LE.QCLINUX.0.0-11500-K2C.0.tar.gz \
      https://github.com/CodeLinaro-mirror/le_platform_vendor_qcom_opensource_ss-restart/archive/LE.QCLINUX.0.0-11500-K2C.0/ss-restart-LE.QCLINUX.0.0-11500-K2C.0.tar.gz

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/ss-restart-LE.QCLINUX.0.0-11500-K2C.0.tar.gz \
      --spec ss-restart.spec \
      --output /path/to/output

For CI, open a PR against the `c10s` branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.

## License

pkg-rpm-ss-restart is licensed under the [BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](LICENSE.txt) for the full license text.

The upstream source and service identify their license as BSD-3-Clause-Clear.
