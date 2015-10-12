from setuptools import setup


requires = open("requirements.txt").read().split()

setup(
    name='instantmusic',
    version='1.2',
    description='Instantly download any song! Without knowing the name of the song!!!!',
    url='https://github.com/yask123/Instant-Music-Downloader',
    author='Yask Srivastava',
    author_email='yask123@gmail.com',
    license='MIT',
    install_requires=requires,
    packages=['instantmusic'],
    entry_points={
        "console_scripts": [
            "instantmusic = instantmusic.instantmusic:main"
        ]
    },
    zip_safe=False,
)
