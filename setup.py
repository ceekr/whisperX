import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="whisperx",
    py_modules=["whisperx"],
    version="3.1.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ] + ["git+https://github.com/ceekr/pyannote-audio.git@a127dd24f03605c501f575133d4c5a3b37562f2b"],
    entry_points = {
        'console_scripts': ['whisperx=whisperx.transcribe:cli'],
    },
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
