from conans import ConanFile, CMake

class RutercheckConan(ConanFile):
    name = "ruter-check"
    version = "0.1.0"
    author = "<naesheim>"
    description = "<When does my train go?>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "gcc"
    requires = "poco/1.9.4"

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
    
    def package(self):
        self.copy("*")