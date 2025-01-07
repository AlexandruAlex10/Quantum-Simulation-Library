from setuptools import setup, find_packages

setup(
    name="quantum_simulation",
    version="1.0.0",
    description="A library to simulate quantum circuits",
    author="Alexandru Mitrofan, Oana Cazan",
    packages=find_packages(),
    url="https://github.com/AlexandruAlex10/Quantum-Simulation-Library",
    install_requires=["numpy>=1.21.0"],
)
