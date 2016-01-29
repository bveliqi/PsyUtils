from distutils.core import setup

setup(
    name='PsyUtils',
    version='1.1.3',
    author='Thomas S. A. Wallis',
    author_email='thomas.wallis@uni-tuebingen.de',
    packages=['psyutils', 'psyutils.image'],
    url='http://github.com/tomwallis/PsyUtils',
    license='LICENSE.txt',
    description='Utility functions for psychophysical experiments and \
                stimuli.',
    long_description=open('README.md').read(),
    install_requires=[
        # 'Python >= 2.7.0',
        'numpy >= 1.8.0',
        'scipy >= 0.13.0',
        'matplotlib',
        'scikit-image >= 0.11.0',
        'seaborn >= 0.6.0'
    ],
)
