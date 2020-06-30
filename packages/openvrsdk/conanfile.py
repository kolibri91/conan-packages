import os
import glob

from conans import ConanFile, tools, CMake
from conans.model.version import Version


class OpenVrSdkConan(ConanFile):
    name = "openvrsdk"
    version="1.12.5"
    settings = "os", "arch", "compiler", "build_type"
    description = "OpenVR SDK"
    homepage = "https://github.com/ValveSoftware/openvr"
    repository = "https://github.com/ValveSoftware/openvr.git"
    url = "https://github.com/kolibri91/conan-packages"
    license = "BSD-3-Clause"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    _sources_dir = "sources"
    exports_sources = ["CMakeLists.txt"]

    def configure(self):
        pass

    def source(self):
        git = tools.Git(self._sources_dir)
        git.clone(
            url=self.repository,
            branch=f"v{self.version}",
            args="--depth 1")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED"] = self.options.shared
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._sources_dir)

        cmake = self.configure_cmake()
        cmake.install()

        for pdb_file in glob.glob(os.path.join(self.package_folder, "lib", "*.pdb")):
            os.unlink(pdb_file)

    def package_id(self):
        pass

    def package_info(self):
        pass
