from setuptools import setup

setup(
    name="inkutils",
    version="0.1",
    author="Veridise Inc.",
    description="This provides utils for processing ink! contracts for Vanguard.",
    packages=["inkutils"],
    py_modules=["inkutils"],
    scripts=["bin/ink-summarizer"],
    install_requires=[
        "setuptools",
    ],
    python_requires=">=3.8",
)