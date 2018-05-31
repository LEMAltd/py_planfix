from distutils.core import setup

setup(
    name='py_planfix',
    version='0.0.1',
    packages=['py_planfix'],
    url='https://github.com/LEMAltd/py_planfix',
    license='MIT',
    author='LEMAltd',
    author_email='github@hunterhelp.biz',
    description='',
    install_requires= [
        'requests',
        'schema',
        'dicttoxml'
    ],
)
