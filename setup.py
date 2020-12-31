import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hb-organiser",
    version="0.0.1",
    author="James Whale",
    author_email="james@james-whale.com",
    description="Organises Humble Bundle bundles based on their platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WhaleJ84/hb-organiser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
    ],
    python_requires='>=3.8',
)