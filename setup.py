from setuptools import setup, find_packages

setup(
    name='gossipy-dfl',
    packages=find_packages(exclude=['docsrc', 'docs']),
    version='0.0.1',    
    description='Python module for simulating gossip learning and decentralized federated learning.',
    url='https://github.com/andr3w003/gossipy',
    license='Apache License, Version 2.0',
    install_requires=['matplotlib>=3.3.4',
                        'tqdm>=4.59.0',
                        'pytest>=6.2.3',
                        'pandas>=1.2.4',
                        'networkx>=2.6.2',
                        'dill>=0.3.4',
                        'numpy>=1.19.2',
                        'torch>=1.8.0',
                        'scikit_learn>=1.0',
                        'rich>=12.2.0'],
)