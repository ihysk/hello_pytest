from setuptools import setup


setup(
    name='siro_uma.hello_pytest',
    version='0.1.0',
    description='A sample Pytest project',
    long_description='This is a sample to learn about pytest!',
    url='https://github.com/sirouma/hello_pytest',
    author='siro_uma',
    author_email='sirouma.09@gmail.com',
    license='MIT',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Topic :: Education',
    'Framework :: Pytest',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    ],
    keywords='sample setuptools development',
    packages=['hello_pytest'],
    entry_points={
        'pytest11': [
            'hello_pytest = hello_pytest.plugin',
        ],
    },
)
