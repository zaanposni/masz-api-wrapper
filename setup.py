from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name='masz',
  py_modules=["masz"],
  version='1.0',
  license='MIT',
  description='API Wrapper for MASZ (A discord moderation bot)',
  author='zaanposni',
  author_email='me@zaanposni.com',
  url='https://github.com/zaanposni/masz-api-wrapper',
  keywords=['MASZ', 'API', 'DISCORD', 'WRAPPER', 'JSON', 'REST', 'MODERATION', 'TOKEN', 'PYTHON'],
  packages=find_packages(exclude=["*tests"]),
  package_data={
    "masz": ["masz/*"]
  },
  install_requires=[
          'requests',
          'typing',
          'python-dateutil'
      ],
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  long_description=long_description,
  long_description_content_type="text/markdown"
)
