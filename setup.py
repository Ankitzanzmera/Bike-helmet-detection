from setuptools import setup,find_packages

project_name = "Bike-helmet-detection"

setup(
    name = project_name,
    version= "0.0.1",
    author="Ankit M Zanzmera",
    author_email="22msrds052@jainuniversity.ac.in",
    url= "https://github.com/Ankitzanzmera/Bike-helmet-detection",
    packages = find_packages(where="src"),  ## From where it starts to find package
    package_dir= {"":"src"}  ## root Dir
)