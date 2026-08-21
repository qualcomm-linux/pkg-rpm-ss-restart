<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# ss-restart RPM - CentOS Stream 10

This branch contains the CentOS Stream 10 RPM packaging for ss-restart from a prebuilt payload tarball.

## Package

| Field | Value |
|---|---|
| Package | ss-restart |
| Version | 1.0.0 |
| Source | ss-restart-prebuilt-1.0.0.tar.gz |
| Source checksum | See sources |

The prebuilt payload installs:

- /usr/bin/subsystem_ramdump
- /usr/lib/systemd/system/subsystem-ramdump.service

## Files

- ss-restart.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. This package uses a prebuilt payload tarball, so the tarball must be available in the lookaside cache before CI can build it.

## Build

Local validation can be run with qcom-rpm-utils:

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/ss-restart-prebuilt-1.0.0.tar.gz \
      --spec ss-restart.spec \
      --output /path/to/output

For CI, open a PR against this c10s branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.
