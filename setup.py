import pip
from setuptools import find_packages, setup

requirements = {
    "install": [
        "setuptools>=38.5.1",
        "soundfile>=0.10.2",
        "librosa",
        "tensorflow"
    ],
    "setup": ["numpy"]
}

install_requires = requirements["install"]
setup_requires = requirements["setup"]

setup(
    name='english_asr',
    version='1.0',
    #packages=['english_asr'],
    author="Neha Soni",
    author_email = 'soni.neha45@gmail.com',
    url = 'https://github.com/neso613/english_asr',
    description="An Automatic Speech Recognition(ASR) for English language trained on LibriSpeech dataset using Conformer.",
    license="Apache-2.0",
    install_requires=install_requires,
    setup_requires=setup_requires,
    classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: Apache-2.0',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.x',
    'Programming Language :: Python :: 2.x',
  ],
)

