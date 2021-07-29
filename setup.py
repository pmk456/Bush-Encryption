import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='Bush-Encryption',
    version='0.3',
    description="Bush-Encryption A New Type Of Algorithm Using AES",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/pmk456/Bush-Encryptor",
    author="Patan Musthakheem",
    author_email="patanmusthakheem786@gmail.com",
    license="Apache 2.0",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords=[
        'encryption',
        'encryptors',
        'aes'
    ],
    project_urls={
        'Documentation': 'https://github.com/pmk456/Bush-Encryption',
        'Source': 'https://github.com/pmk456/Bush-Encryption',
        'Tracker': 'https://github.com/pmk456/Bush-Encryption/issues'
    },
    install_requires=[
        'pycryptodome >= 3.9.6'
    ],
    python_requires=">=3.5",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
