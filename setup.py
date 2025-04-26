from setuptools import setup, find_packages
from pathlib import Path

# Читаємо README.md та CHANGELOG.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
changelog = (this_directory / "CHANGELOG.md").read_text(encoding="utf-8")
long_description += "\n\n" + changelog

setup(
    name='InfinityMath',
    version='1.0.0',
    description='A math module with custom functions, utilities and calculations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SlackBaker/better_math',
    author='Ostap Dziubyk',
    author_email='your-email@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',  # Краще поставити Beta поки build не стабільний
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',  # Не лише Windows
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='math, calculations, functions, InfinityMath, XMath, numpy',
    packages=find_packages(include=["better_math", "better_math.*"]),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    python_requires='>=3.6',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'infinitymath-version=better_math:show_version',
        ],
    },
)
