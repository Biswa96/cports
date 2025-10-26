pkgname = "starship"
pkgver = "1.24.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=battery,notify",
]
make_install_args = [*make_build_args]
make_check_args = [
    *make_build_args,
    # /tmp is home of the cbuild user so tests that check for /tmp/dir get ~/dir as exact path
    "--",
    "--skip=modules::directory::tests::fish_directory_config_small",
    "--skip=modules::directory::tests::fish_style_directory_config_large",
    "--skip=modules::directory::tests::highlight_git_root_dir_zero_truncation_length",
    "--skip=modules::directory::tests::truncated_directory_config_large",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["git"]
pkgdesc = "Cross-shell prompt"
license = "ISC"
url = "https://starship.rs"
source = (
    f"https://github.com/starship/starship/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "3d98e2c57dcfea36c6035e2ad812f91cfe33099e4b67f6ea7728e2294f02ca61"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(self.cwd / f"starship.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/starship",
                "completions",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/starship")
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"starship.{shell}", shell)
