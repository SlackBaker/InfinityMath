from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("CHANGELOG.md", "r", encoding="utf-8") as f:
    long_description += "\n\n" + f.read()

setup(
    name='InfinityMath',
    version='0.0.6',
    description='The math module where you can sum numbers, make functions and other things',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SlackBaker/better_math.git',
    author='Ostap Dziubyk',
    author_email='your-email@example.com',
    license='MIT',
    classifiers=classifiers,
    keywords='math, better_math, calculations, InfinityMath, XMath',
    packages=find_packages(include=["better_math"]),
    install_requires=['numpy', 'scipy', 'matplotlib'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'infinitymath-version=better_math:show_version',
        ],
    },
)
