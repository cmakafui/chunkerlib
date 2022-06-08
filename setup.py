from setuptools import find_packages, setup
setup(
    name='chunkerlib',
    packages=find_packages(include=['chunkerlib']),
    version='0.1.0',
    description='Chunking Library',
    author='Carl Kugblenu',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)