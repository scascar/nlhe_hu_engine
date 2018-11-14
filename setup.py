"""
Simple Poker engine for head's up no limit hold'em 
"""

from setuptools import setup

setup(
    name='nlhe-hu-engine',
    version='0.0.1',
    description='Simple Poker engine for head\'s up no limit hold\'em',
    long_description=open('README.md').read(),
    author='Oscar Blazejewski',
    url='https://github.com/scascar/nlhe-hu-engine',
    license='MIT',
    packages=['nlhe_hu_engine'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment'
    ],
    install_requires=[
        'numpy',
        'treys'
    ]
)
