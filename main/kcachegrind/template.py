pkgname = "kcachegrind"
pkgver = "25.04.3"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE profiling visualisation tool"
license = "GPL-2.0-only"
url = "https://apps.kde.org/kcachegrind"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcachegrind-{pkgver}.tar.xz"
sha256 = "23c7dcbbf15c5ee00ddac068022f118b5de939d097199b0f918df9f94f74d9e1"
hardening = ["vis"]


def post_install(self):
    # python2
    self.uninstall("usr/bin/hotshot2calltree")


@subpackage("kcachegrind-scripts")
def _(self):
    self.subdesc = "perl script utilities"
    self.install_if = [self.parent]
    self.depends += ["perl"]

    return [
        "usr/bin/dprof2calltree",
        "usr/bin/memprof2calltree",
        "usr/bin/op2calltree",
        # technically the above is a lie and this is php, but it also needs a pear plugin for Console_Getopt, so whatever
        "usr/bin/pprof2calltree",
    ]
