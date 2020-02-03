import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="<my-package>",
    version="0.0.0",
    author="Harry Wei",
    author_email="pepsimixt@gmail.com",
    description="<my-package-description>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haochuanwei/<my-package>",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
