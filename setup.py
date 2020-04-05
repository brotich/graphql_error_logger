import setuptools

setuptools.setup(
    name="graphql_error_logger",
    version="0.0.1",
    author="Brian Rotich",
    author_email="opensource@brianrotich.com",
    description="Log expection from the GraphQL python server",
    url="https://github.com/brotich/graphql_error_logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["flask_graphql>=2.0.0"],
)
