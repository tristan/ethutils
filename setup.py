from setuptools import setup

setup(
    name='ethutils',
    version='0.0.1',
    author='Tristan King',
    author_email='tristan.king@gmail.com',
    packages=['ethutils'],
    url='http://github.com/tristan/ethutils',
    description='Common utility functions used in ethereum related code',
    long_description=open('README.md').read(),
    install_requires=[
        'pycryptodome>=3.3.1',
        'secp256k1'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest'
    ]
)
