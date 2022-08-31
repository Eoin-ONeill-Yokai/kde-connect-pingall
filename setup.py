from setuptools import setup

setup(
    name="kdeconnect-pingall",
    version="0.1",
    py_modules=['pingall'],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        kdeconnect-pingall=pingall:ping
    ''',
    )

