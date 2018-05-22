from setuptools import setup, find_packages

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='terraform-docs',
    version='0.1.0a3',  # TODO change this to a git tag for Drone
    description='A Terragrunt rapid development tool to simplify '
                'overriding the source parameter in a terraform.tfvars '
                'file.',
    long_description=long_description,
    url='https://github.com/ddriddle/terraform-docs',
    author='David D. Riddle',
    author_email='ddriddle@illinois.edu',
    classifiers=[
#        'Development Status :: 4 - Beta',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='terraform module documentation docs',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=2.6',
    install_requires=[
       'pyhcl',
       "future ; python_version<'3'"
    ],
    tests_require=[
        "mock ; python_version<'3.4'"
    ],
    test_suite="tests",
    entry_points={
        'console_scripts': [
                    'terraform-docs=terraform_docs:main',
        ],
    },
    project_urls={
        'Bug Reports':
            'https://github.com/ddriddle/terraform-docs/issues',
        'Source': 'https://github.com/ddriddle/terraform-docs',
    },
)
