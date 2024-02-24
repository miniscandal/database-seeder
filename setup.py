from setuptools import setup, find_packages

setup(
    name="seeder-data-base",
    version="1.0",
    description="Mocks for data base",
    author="miniscandal",
    author_email="oscar01dev@gmail.com",
    url="https://github.com/miniscandal",
    packages=find_packages(),
    install_requires=["python-dotenv==1.0.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11.3",
    ],
)
