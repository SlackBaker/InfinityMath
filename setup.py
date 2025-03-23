from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: Proprietary',  # Якщо це приватна ліцензія
    'Programming Language :: Python :: 3'
]

setup(
    name='better_math',
    version='0.0.1',
    description='Basic math module',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/better_math',  # Замініть на реальне посилання
    author='Ostap Dziubyk',
    author_email='your-email@example.com',  # Додай свою пошту або прибери цей параметр
    license='Proprietary',
    classifiers=classifiers,
    keywords='math, better_math, calculations',
    packages=find_packages()
)
