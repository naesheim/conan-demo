from conans import ConanFile, CMake

class RutercheckConan(ConanFile):
    name = "ruter-check"
    version = "0.1.0"
    author = "naesheim"
    description = "When does my train go?"
    url = "https://github.com/naesheim/conan-demo"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "poco/1.9.4","output-parser/0.1.0"

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()