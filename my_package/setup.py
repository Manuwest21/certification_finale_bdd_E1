from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0.0',
    author='manu',
    author_email='manman@email.com',
    description='Une courte description de votre package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://lien_vers_votre_projet',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    packages=find_packages(),
    python_requires='>=3.6',
)

