from setuptools import setup

setup(
    name='Snapshot-Tool',
    version='0.1',
    author="Andy Chandy",
    summary="Tool to create snapshots of ec2 volumes",
    license="GPLv3+",
    packages=['Snapshot'],
    url="https://github.com/Chandy13/AWS-Snapshot",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        Snapshot=Snapshot.Snapshot:cli
    ''',
)
