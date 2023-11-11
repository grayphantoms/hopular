import setuptools

with open(r'README.md', mode=r'r') as readme_handle:
    long_description = readme_handle.read()

setuptools.setup(
    name=r'hopular',
    version=r'1.0.0',
    author=r'Bernhard Schäfl',
    author_email=r'schaefl@ml.jku.at',
    url=r'https://github.com/ml-jku/hopular',
    description=r'A novel deep learning architecture based on continuous modern Hopfield networks' +
                r' for tackling small tabular datasets.',
    long_description=long_description,
    long_description_content_type=r'text/markdown',
    packages=setuptools.find_packages(),
    python_requires=r'>=3.8.0',
    install_requires=[
        r'pytorch-lightning',
        r'fairscale',
        r'scikit-learn',
        r'pandas',
        r'hopfield-layers@git+https://github.com/ml-jku/hopfield-layers'
    ],
    zip_safe=True,
    include_package_data=True,
    entry_points={
        r'console_scripts': [
            r'hopular = hopular.interactive:console_entry'
        ]
    }
)
