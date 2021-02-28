import glob
import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


scripts = glob.glob('bin/[a-z]*')

setuptools.setup(
    name='wikivector',
    version='1.2.0',
    description='Tools for encoding Wikipedia articles as vectors.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Neal Morton',
    author_email='mortonne@gmail.com',
    license='GPLv3',
    url='http://github.com/mortonne/wikivector',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    scripts=scripts,
    install_requires=[
        'selectolax',
        'numpy',
        'h5py>=3',
        'pandas',
        'tensorflow_hub',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
    ]
)
