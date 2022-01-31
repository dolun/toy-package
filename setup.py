import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="is_number",
    version="0.0.2",
    author="Thomas Dautremer",
    author_email="thomas.dautremer@cea.fr",
    description="A Python library to determine if something is a number.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/dolun/toy-package.git",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    tests_require=['pytest']
)

