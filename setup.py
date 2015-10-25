from setuptools import find_packages
from setuptools import setup


setup(
    name='android_pre_commit_hooks',
    description='Some hooks for pre_commit and android development.',
    url='https://github.com/pre-commit/pre-commit-hooks',
    version='0.4.2',

    author='Tyler Argo',
    author_email='argo_49@hotmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'java-function-spacer-fixer = pre_commit_hooks.java_function_spacer_fixer:fix_spaces_between_java_functions',
			],
    },
)
