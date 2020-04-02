from conans import ConanFile, CMake

class RutercheckConan(ConanFile):
    name = "output-parser"
    version = "0.1.0"
    author = "naesheim"
    description = "parsing output"
    url = "https://github.com/naesheim/conan-demo"
    exports_sources = "include/*"
    no_copy_source = True
    requires = "poco/1.9.4"
    
    def package(self):
        self.copy("*.h", dst="include")
    