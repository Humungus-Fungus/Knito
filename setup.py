from setuptools import find_packages, setup
setup(
	name ='knito',
	packages=find_packages(include=['pylib']),
	version='0.1.0',
	description='Magic with strings.',
	author='HumFung',
	license='MIT',
	install_requires=[],
	setup_requires=['pytest-runner'],
	tests_require=['pytest==4.4.1'],
	test_suite='tests'
)
