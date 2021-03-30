import glob
import setuptools

scripts = glob.glob('bin/[a-z]*')
setuptools.setup(scripts=scripts)
