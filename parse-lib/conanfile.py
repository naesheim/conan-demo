from conans import ConanFile, tools

class RutercheckConan(ConanFile):
    name = "output-parser"
    version = "0.1.0"
    author = "naesheim"
    description = "parsing output"
    requires = "poco/1.9.4"

    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }

    # scm = {
	# "type": "git",
	# "url": "https://github.com/naesheim/whereshans-web",
	# "revision": "master",
	# "subfolder": "web"
    # }

    # def set_version(self):
    #     git = tools.Git(folder=self.recipe_folder)
    #     self.version = "%s_%s" % (git.get_branch(), git.get_revision())

    def package(self):
        self.copy("*.h",src="",dst="include/output-parser", keep_path=False)
