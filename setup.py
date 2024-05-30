import setuptools
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding = "utf-8") as f:
    long_description = "\n" + f.read()

VERSION = "0.1"
REPO_NAME = "deephub"
AUTHOR_USER_NAME = "4insu"
DESCRIPTION = "Deep Learning Models implemented in PyTorch"
LONG_DESCRIPTION = "A package that allows to import research level deep learning models."

# setting up
setuptools.setup(
    name = "deephub",
    version = VERSION,
    author = "4insu",
    author_email = "supriyo.ain.02@gmail.com",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    long_description = long_description,
    package_dir = {"": "deephub"},
    packages = setuptools.find_packages(where = "deephub"),
    install_requires = ["torch"],
    keywords = ["python", "deep learning"],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Deep Learning :: Research Models",
    ]
)