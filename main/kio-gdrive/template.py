pkgname = "kio-gdrive"
pkgver = "25.08.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kaccounts-integration-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "libkgapi-devel",
    "purpose-devel",
    "qt6-qtbase-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE KIO plugin for Google Drive"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kio_gdrive"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-gdrive-{pkgver}.tar.xz"
sha256 = "e6c371582454f53a9b807f0e0c340c155d61faca3cf1a247c18fa0e4f0d16325"
