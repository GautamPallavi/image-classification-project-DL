import setuptools

with open ("README.md",'r', encoding="utf-8") as f:
    long_description=f.read()

__version__= "0.0.0"

REPO_Name="image-classification-project-DL"
AUTHOR_NAME="GautamPallavi"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="pallavigautam14052gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
