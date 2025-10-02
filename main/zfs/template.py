# also update linux-*-zfs-bin
pkgname = "zfs"
pkgver = "2.3.4"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--with-config=user",
    "--with-mounthelperdir=/usr/bin",
    "--with-udevdir=/usr/lib/udev",
    "--with-udevruledir=/usr/lib/udev/rules.d",
    "--with-dracutdir=/usr/lib/dracut",
    "--with-tirpc",
    "--without-libunwind",
]
# we generate, then create tarball, then configure, so do that manually
configure_gen = []
hostmakedepends = ["pkgconf", "automake", "libtool", "python"]
makedepends = [
    "attr-devel",
    "dinit-chimera",
    "libtirpc-devel",
    "linux-headers",
    "linux-pam-devel",
    "openssl3-devel",
    "udev-devel",
    "util-linux-blkid-devel",
    "util-linux-uuid-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "OpenZFS for Linux"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
source = [
    f"https://github.com/openzfs/zfs/releases/download/zfs-{pkgver}/zfs-{pkgver}.tar.gz",
    # not shipped in tarballs? why
    f"!https://raw.githubusercontent.com/openzfs/zfs/zfs-{pkgver}/config/kernel-dentry-operations.m4>kernel-dentry-operations-{pkgver}.m4",
    f"!https://raw.githubusercontent.com/openzfs/zfs/zfs-{pkgver}/contrib/debian/tree/zfs-initramfs/usr/share/initramfs-tools/hooks/zdev>zdev-{pkgver}",
]
sha256 = [
    "9ec397cf360133161a1180035f3e7d6962186ed2b3457953a28d45aa883fa495",
    "4071c1f9e2136d5df77b68a944c4988c3aca78faf1e6cb87f74d420d38c2d4e2",
    "c541dfec33ba7dfec3fb85a4532fc9c7a72035316716e93074b2cfa030ca2d12",
]
hardening = ["!vis", "!cfi"]


def post_extract(self):
    self.cp(self.sources_path / f"zdev-{pkgver}", ".")
    self.cp(
        self.sources_path / f"kernel-dentry-operations-{pkgver}.m4",
        "config/kernel-dentry-operations.m4",
    )


def pre_configure(self):
    self.do("autoreconf", "-if")
    # unfuck the perms of files introduced by autoreconf
    self.chmod("config/config.guess", 0o755)
    self.chmod("config/config.sub", 0o755)
    self.chmod("config/install-sh", 0o755)
    # compress source tree for ckms
    fn = f"{pkgname}-{pkgver}.tar"
    self.do("tar", "cf", fn, "--exclude", fn, ".")


def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_license("LICENSE")
    self.install_license("NOTICE")

    # TODO: clean up the initramfs + /etc/default/zfs of sysvinit cruft
    self.uninstall("usr/share/zfs/zfs-tests")
    self.uninstall("etc/init.d")
    self.uninstall("usr/share/pam-configs/zfs_key")
    self.uninstall("usr/share/man/man8/zfs-mount-generator.8")

    # install the zdev hook for udev rules (also handles enc keys)
    self.install_initramfs(f"zdev-{pkgver}", name="zdev")

    # install ckms source tree
    srcp = f"usr/src/{pkgname}-{pkgver}"
    self.install_dir(srcp)
    self.do(
        "tar",
        "xf",
        self.chroot_cwd / f"{pkgname}-{pkgver}.tar",
        wrksrc=self.chroot_destdir / srcp,
    )
    self.install_file(
        self.files_path / "ckms.ini", srcp, template={"VERSION": pkgver}
    )

    self.install_service(self.files_path / "zed")
    # just say no to hardlinks
    self.uninstall("usr/share/bash-completion/completions/zpool")
    self.install_link("usr/share/bash-completion/completions/zpool", "zfs")


@subpackage("zfs-dracut")
def _(self):
    self.subdesc = "dracut module"
    self.install_if = [self.parent, "dracut"]
    self.depends = [self.parent]

    return ["usr/lib/dracut"]


@subpackage("zfs-devel")
def _(self):
    return self.default_devel()


@subpackage("zfs-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends = [
        self.parent,
        "ckms",
        "perl",
        "python",
        "gmake",
    ]

    return ["usr/src"]
