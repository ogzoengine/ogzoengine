from setuptools import setup

with open("ogzoengine/README.md", "r") as f:
    long_description_read = f.read()

setup(
      name='ogzoengine',
      version='1.3.5.4',
      description='basic pygame engine',
      license='Apache License, Version 2.0',
      author='Coguz',
      packages=['ogzoengine'],
      long_description=long_description_read,
      long_description_content_type="text/markdown",
      zip_safe=False,
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
      ],
      install_requires=[
        'pygame >= 2.0.1',
        'keyboard >= 0.13.3'],
      extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2", 'some_other_dependency>=1.0'],
      },

      python_requires=">=3.10",
    )