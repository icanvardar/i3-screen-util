from setuptools import setup, find_packages

setup(
    name = "i3-screen-util",
    version = "0.1.0",
    description = "A screen utility wrapper for i3wm.",
    url = "https://github.com/icanvardar/i3-screen-util",
    author = "Can Vardar",
    author_email = "me@icanvardar.com",
    license = "MIT",
    install_requires = ["json", "os", "re", "subprocess", "sys"],
    packages = find_packages(),
    entry_points=dic(
        console_scripts=['rq=main:main']
    )
)
