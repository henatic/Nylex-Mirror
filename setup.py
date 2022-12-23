setup(
    name="Nylex-Mirror",
    version="1.0.0",
    description="Dashboard that displays people's latest messages.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/henatic/Nylex-Mirror",
    author="Henatic",
    author_email="henry@nylex.net",
    license="Apache-2.0 license",
    classifiers=[
        "License :: OSI Approved :: Apache-2.0 license",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader", "tkinter", "datetime", "pytz", "flask", "threading", "textwrap", "re", "collections", "random", "pyautogui", ""],
    include_package_data=True,
    install_requires=[
        "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["magic_mirror=reader.__main__:main"]},
)