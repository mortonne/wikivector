import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='wikivector',
    version='0.1.0',
    description='Tools for encoding Wikipedia articles as vectors.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Neal Morton',
    author_email='mortonne@gmail.com',
    license='GPLv3',
    url='http://github.com/mortonne/wikivector',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
    ]
)