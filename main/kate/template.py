pkgname = "kate"
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
    "karchive-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "kwallet-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
depends = ["konsole"]
pkgdesc = "KDE Advanced Text Editor"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kate-{pkgver}.tar.xz"
sha256 = "b5eefa519690983ef92be8cc30eaface1fc8c9f225d9d851a5c1819a52634770"
hardening = ["vis"]
# no idea
options = ["!check"]


# for kwrite to not pull in kate
@subpackage("kate-libs")
def _(self):
    return self.default_libs()


@subpackage("kate-kwrite")
def _(self):
    self.subdesc = "KWrite"
    self.provides = [self.with_pkgver("kwrite")]
    return [
        "usr/bin/kwrite",
        "usr/share/icons/hicolor/*/apps/kwrite.*",
        "usr/share/applications/org.kde.kwrite.desktop",
        "usr/share/metainfo/org.kde.kwrite.appdata.xml",
    ]
