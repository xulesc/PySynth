#!/usr/bin/env python

from distutils.core import setup

setup(name="PySynth",
        version="1.0.1",
        description="A simple music synthesizer for Python",
        author="XXXX",
        author_email="XXXX",
	url="XXXX",
        py_modules=["pysynth", "pysynth_b", "pysynth_s", "pysynth_beeper","play_wav"],
	scripts=["read_abc.py", "nokiacomposer2wav.py", "test_nokiacomposer2wav.py","menv.py"],
)
