from setuptools import setup, find_packages

setup(
    name='spm_dictionary',
    version='0.1.1.3',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'spm_dictionary': ['csv/*.csv']
    },
    install_requires=[
        'dolphin-memory-engine',
    ],
    author='SacredGhostSPM',
    author_email='',
    description='A package for processing SPM dictionary data from CSV files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SacredGhost/SPM-Dictionary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)