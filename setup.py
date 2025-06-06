from setuptools import find_packages, setup

setup(
    name="drf-mock-response",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    description="Reusable mock response views for Django REST Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ali Bagheri",
    author_email="khodealib@gmail.com.com",
    url="https://github.com/khodealib/drf-mock-response",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django",
        "djangorestframework",
    ],
)
