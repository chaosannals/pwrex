import setuptools

with open('readme.md', 'r', encoding='utf8') as reader:
    long_description = reader.read()

setuptools.setup(
    name='pwrex',
    version='0.1.0',
    description='yet a playwright library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='chaosannals',
    author_email='chaosannals@outlook.com',
    url='https://github.com/chaosannals/pwrex',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'playwright>=1.16.1',
    ],
)