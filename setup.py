import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='k13',
    version='0.0.1',
    author='Andreas Slåttelid',
    description='Implementation of k13',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AndreasSlattelid/k13',
    packages=['k13'],
    install_requires=['numpy', 'scipy'],
)
