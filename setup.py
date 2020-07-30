from setuptools import setup
import re

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('discord/ext/template/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='discord-ext-template',
    author='Ext-Creators',
    python_requires='>=3.5.3',
    url='https://github.com/Ext-Creators/template',
    version=version,
    packages=['discord.ext.template'],
    license='Apache Software License',
    description='Template repository for extensions.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
