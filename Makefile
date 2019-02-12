all:
	echo Hello.
# register:
#	./setup.py register -r yaplotlib
# edit ~/.pypirc
check:
	./setup.py check
install: check
	./setup.py install
pypi: check
	./setup.py sdist bdist_wheel upload
build.:
	-rm *.so
	-rm -rf build
	python setup.py build_ext --inplace
clean:
	-rm *~ 
	-rm -rf build dist *.egg-info
