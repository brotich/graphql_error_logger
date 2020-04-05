import setuptools

setuptools.setup(
    name="graphql_error_logger",
    version="0.0.3",
    author="Brian Rotich",
    author_email="opensource@brianrotich.com",
    description="Log expection from the GraphQL python server",
    url="https://github.com/brotich/graphql_error_logger",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    install_requires=["flask_graphql>=2.0.0"],
)
