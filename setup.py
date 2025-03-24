import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weao-api",
    version="0.1.0",
    author="Flames",
    author_email="auraisme610@gmail.com",
    description="A Python client for interacting with the WEAO API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlamesIsCool/weao-api",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
