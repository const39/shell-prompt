import setuptools
with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shell-prompt",
    version="0.0.1",
    author="const39",
    author_email="author@example.com",
    description="Custom Linux shell prompt written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/const39/shell-prompt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.6',
)
