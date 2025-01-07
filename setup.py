from setuptools import setup, find_packages

setup(
    name="quslapi",
    version="1.0.0",
    description="A library to simulate quantum circuits",
    author="Alexandru Mitrofan, Oana Cazan",
    package_dir={"": "quantum_simulation"},
    packages=find_packages(where="quantum_simulation"),
    url="https://github.com/AlexandruAlex10/Quantum-Simulation-Library",
    install_requires=["numpy>=1.21.0"],
)
