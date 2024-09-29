from setuptools import setup, find_packages

setup(
    name="i3-screen-util",
    version="0.1.0",
    description="A screen management tool for your lovely i3wm config.",
    url="https://github.com/icanvardar/i3-screen-util",
    author="Can Vardar",
    author_email="ismailcanvardar@gmail.com",
    license="MIT",
    install_requires=[],
    packages=find_packages(),
    entry_points={"console_scripts": ["rq=main:main"]},
)

