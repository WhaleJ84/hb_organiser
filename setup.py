from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hb_organiser",
    version="1.0.9",
    author="James Whale",
    author_email="james@james-whale.com",
    description="Organises Humble Bundle bundles based on their platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WhaleJ84/hb_organiser",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
    ],
    entry_points={
        'console_scripts': [
            'hb_organiser=hb_organiser.cli:main',
        ],
    },
    python_requires='>=3.6',
)
