from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="NotifierClient",  # How you named your package folder
    packages=["notifier_client"],  # Chose the same as "name"
    include_package_data=True,
    version="v0.1.1",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Python client for QwhaleNotifier",  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yehoyada.s",  # Type in your name
    author_email="hvuhsg6@gmail.com",  # Type in your E-Mail
    url="https://notifier.qwhale.ml",  # Provide either the link to your github or to your website
    download_url="",
    keywords=[
        "API",
        "Client",
        "Qwhale",
        "qWhale",
        "client",
        "notification",
        "application"
    ],  # Keywords that define your package best
    install_requires=["requests"],  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
