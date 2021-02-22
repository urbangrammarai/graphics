import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urbangrammar_graphics",
    version="1.2.1",
    author="Martin Fleischmann",
    author_email="martin@martinfleischmann.net",
    python_requires=">=3.6",
    install_requires=["matplotlib", "seaborn", "numpy", "contextily"],
    description="Visual style for Urban Grammar AI research project",
    url="https://github.com/urbangrammarai/graphics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
)
