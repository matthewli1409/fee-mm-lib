from setuptools import setup

setup(name='fee-lib',
      version='1.2.5',
      description='external api lib',
      url='',
      author='Matthew Li',
      author_email='matthewli1409@gmail.com',
      license='MIT',
      install_requires=['dnspython==2.1.0', 'pymongo==3.11.0', 'python-dotenv==0.19.0', 'slackclient==2.5.0'],
      zip_safe=False)
