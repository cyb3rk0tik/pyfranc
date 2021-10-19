from setuptools import (
    setup,
    find_packages,
)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyfranc",
    version="0.1.1",
    description="Text language detection basic on trigrams.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyb3rk0tik/pyfranc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    entry_points={'console_scripts': ['pyfranc_cli = pyfranc.pyfranc_cli:main']},
    author="cyb3rk0tik",
    author_email="cyberkotik@riseup.net",
    python_requires=">=3",
    license='MIT',
)