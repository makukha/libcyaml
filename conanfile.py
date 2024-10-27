from os.path import join

from conan import ConanFile
from conan.tools.files import copy
from conan.tools.gnu import GnuToolchain, MakeDeps


class BasicConanfile(ConanFile):
    name = "cyaml"
    version = "2.0.0"
    description = (
        "LibCYAML is a C library for reading and writing structured YAML documents. "
        "It is written in ISO C11 and licensed under the ISC licence."
    )
    license = "ISC"
    author = 'Michael Drake <tlsa@netsurf-browser.org>'
    homepage = "https://github.com/tlsa/libcyaml"
    url = homepage
    exports_sources = 'examples*', 'include*', 'src*', 'libcyaml.pc.in', 'Makefile'

    def requirements(self):
        pass

    def build_requirements(self):
        pass

    def generate(self):
        deps = MakeDeps(self)
        deps.generate()
        tc = GnuToolchain(self)
        tc.generate()

    def build(self):
        self.run('make VARIANT=release')

    def package(self):
        copy(
            self, "cyaml.h", join(self.source_folder, 'include/cyaml'),
            join(self.package_folder, "include"), keep_path=False,
        )
        self.run('make install VARIANT=release')
