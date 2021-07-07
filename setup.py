import os
import setuptools

with open("README.md", 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name="zlibrary_api",
    packages=["zlibrary_api"],
    description="Search Zlibrary(1lib.in) for info on books.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="",
    download_url="",
    author="adenosinetp10",
    author_email="adenosinetp10@gmail.com",
    license="MIT"
)