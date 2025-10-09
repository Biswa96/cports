pkgname = "tealdeer"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features", "native-tls"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=test_autoupdate_cache",
    "--skip=test_create_cache_directory_path",
    "--skip=test_pager_flag_enable",
    "--skip=test_quiet_cache",
    "--skip=test_quiet_failures",
    "--skip=test_quiet_old_cache",
    "--skip=test_spaces_find_command",
    "--skip=test_update_cache",
    "--skip=test_warn_invalid_tls_backend",
    "--skip=test_update_language_arg",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
pkgdesc = "Alternative implementation of tldr"
license = "MIT"
url = "https://github.com/tealdeer-rs/tealdeer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b1f1262de60ef3105ff93de71568a68a56ad5874a28f105ab7cb5857d305cdb9"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tldr")
    self.install_license("LICENSE-MIT")
    self.install_completion("completion/bash_tealdeer", "bash", "tldr")
    self.install_completion("completion/zsh_tealdeer", "zsh", "tldr")
    self.install_completion("completion/fish_tealdeer", "fish", "tldr")
