from setuptools import setup, find_namespace_packages


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="shallowflow_base",
    description="Base components for the Python 3 shallowflow workflow engine.",
    long_description=(
        _read('DESCRIPTION.rst') + b'\n' +
        _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/waikato-datamining/shallowflow-base",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    namespace_packages=[
        "shallowflow",
    ],
    install_requires=[
        "shallowflow_api",
        "numexpr",
    ],
    entry_points={
        "console_scripts": [
            "sf-run-flow=shallowflow.base.tools.run_flow:sys_main",
            "sf-generate-md=shallowflow.base.help.generate_md:sys_main",
        ],
        "class_lister": [
            "sf.base=shallowflow.base.class_lister:list_classes",
        ],
    },
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
)
