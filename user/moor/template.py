pkgname = "moor"
pkgver = "2.12.2"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}", "./cmd/moor"]
hostmakedepends = ["go"]
renames = ["moar"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ee0e14c80651bc12f2e6c8ede41d632aca46043e46171f328c24a208213e802"


def install(self):
    self.install_bin("build/moor")
    self.install_license("LICENSE")
    self.install_man("moor.1")
