import setuputools
with open('README.md', 'r', encoding='utf-8')as fh:
  long_description = fh.read()
setuptools.setup(
  #
  name='good_name',
  version='0.01',
  author='Takeru_Wakatsuki',
  author_email='s2222100@stu.musashino-u.ac.jp',
  #
  description='how can',
  long_description=long_description,
  long_description_content_type='text/markdown',
  #
  url='https://github.com/s2222100/make_pypi',
  #
  project_urls={
    "Bug Tracker":"https://github.com/s2222100/make_pypi"
  },
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSIApproved :: MIT License',
    'Operating System :: OS Independent',
  ],
  package_dir={'':'src'},
  #
  py_modules=["good_name"],
  packages=setuptools.find_package(where='src'),
  python_requires='>=3.7',
  entry_points={
    'console_points={
      'console_scripts':[
      #
        'name=name:main'
    ]
  },
)
