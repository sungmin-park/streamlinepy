from setuptools import setup

setup(
    name='streamline',
    version='0.0.1',
    author='Park Sung Min',
    author_email='vamf12@gmail.com',
    description='Python to JavaScript. Coroutine support with streamlinejs.',
    url='https://github.com/vamf12/streamlinepy',
    packages=['streamline'],
    install_requires=['jinja2'],
    test_suite='nose.collector',
    tests_require=['nose', 'pyexecjs'],
)
