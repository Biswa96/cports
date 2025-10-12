pkgname = "knotifications"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "kconfig-devel",
    "libcanberra-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Desktop notifications"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/knotifications/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/knotifications-{pkgver}.tar.xz"
sha256 = "86f2645f2bc43440f119099bf25aa5329e8457761a855e4bd5f08a5f7809b2b6"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("knotifications-devel")
def _(self):
    return self.default_devel()
