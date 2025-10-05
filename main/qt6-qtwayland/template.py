pkgname = "qt6-qtwayland"
pkgver = "6.9.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = [
    "-E",
    "(tst_seatv4|tst_client|tst_scaling|tst_compositor|tst_surface|test_waylandclient)",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen", "XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = ["qt6-qtbase-private-devel", "qt6-qtdeclarative-devel"]
checkdepends = ["mesa-dri"]
install_if = [self.with_pkgver("qt6-qtbase-gui"), "wayland"]
pkgdesc = "Qt6 Wayland component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwayland-everywhere-src-{pkgver}.tar.xz"
sha256 = "e413d4bc9263e80a465761debf8cb8317aa6b01e814b20046a05258e6573dadd"
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]


@subpackage("qt6-qtwayland-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/libexec",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
