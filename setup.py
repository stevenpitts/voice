import sys
#from setupGUI import SetupGUI
from setuptools import setup

setup(
    name = "voice",        # what you want to call the archive/egg
    version = "0.1",
    packages=["voice voiceServer makuUtil sound sGUI SGUI"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    #package_data = {},
    author="Steven Pitts",
    author_email = "makucross@gmail.com",
    description = "An intercom system for any laptop on a network",
    #license = "makuLicense",
    #keywords= "",
    url = "https://github.com/makusu2/voice",
	"""
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "helloworld_in_python = helloworld.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
	"""
)
