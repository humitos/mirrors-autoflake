from setuptools import setup


setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=['autoflake==1.3-munkyshi'],
    dependency_links=[
        'git+ssh://git@github.com/munkyshi/autoflake.git#egg=autoflake-1.3-munkyshi',
    ]
)
