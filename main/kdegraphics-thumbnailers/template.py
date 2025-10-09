pkgname = "kdegraphics-thumbnailers"
pkgver = "25.08.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kdegraphics-mobipocket-devel",
    "kio-devel",
    "libkdcraw-devel",
    "libkexiv2-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE thumbnailers for PostScript/RAW/MobiPocket/Blender"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdegraphics_thumbnailers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdegraphics-thumbnailers-{pkgver}.tar.xz"
sha256 = "02e1fc5d2a77ad9c57173deae2333a0a3f04446e7ccf682f1f66b09902f01adf"
