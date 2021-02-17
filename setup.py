import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urbangrammar_graphics",
    version="1.1.0",
    author="Martin Fleischmann",
    author_email="martin@martinfleischmann.net",
    python_requires=">=3.6",
    install_requires=["matplotlib", "seaborn", "numpy", "contextily"],
    description="Visual style for Urban Grammar AI research project",
    long_description=long_description,
    url="https://github.com/urbangrammarai/graphics",
)
