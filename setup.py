import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='zomathon',
    version=1.3,
    description='Zomato API Python Module',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),

    author='abhishtagatya',
    author_email='gatya.dev@yahoo.com',
    url='https://github.com/abhishtagatya/zomathon',

    license='MIT',
    packages=['zomathon'],
    zip_safe=False
)
