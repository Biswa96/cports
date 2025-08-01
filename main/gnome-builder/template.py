pkgname = "gnome-builder"
pkgver = "48.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dnetwork_tests=false"]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "clang-devel",
    "cmark-devel",
    "editorconfig-devel",
    "enchant-devel",
    "flatpak-devel",
    "gom-devel",
    "gtksourceview-devel",
    "json-glib-devel",
    "jsonrpc-glib-devel",
    "libadwaita-devel",
    "libdex-devel",
    "libgit2-devel",
    "libgit2-glib-devel",
    "libpanel-devel",
    "libpeas2-devel",
    "libportal-devel",
    "libsoup-devel",
    "libspelling-devel",
    "libxml2-devel",
    "ostree-devel",
    "sysprof-capture",
    "template-glib-devel",
    "vte-gtk4-devel",
    "webkitgtk4-devel",
]
depends = [
    "flatpak-builder",
    "python-gobject",
    "python-lxml",
]
checkdepends = [
    "dbus",
    "xwayland-run",
    *depends,
]
pkgdesc = "Developer-oriented editor for GNOME"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Builder"
source = f"$(GNOME_SITE)/gnome-builder/{'.'.join(pkgver.rsplit('.')[:-1])}/gnome-builder-{pkgver}.tar.xz"
sha256 = "ec1280d47e814a313b74cb927d5a059380544aa0f56e87552978397d6c74cc63"
# gobject-introspection
options = ["!cross"]


@subpackage("gnome-builder-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
