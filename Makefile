PKGNAME=twist-op
all:
	echo Hello.
# register:
#	./setup.py register -r yaplotlib
# edit ~/.pypirc


test-deploy: build
	twine upload -r pypitest dist/*
test-install:
	pip install --index-url https://test.pypi.org/simple/ $(PKGNAME)

install: check
	./setup.py install
uninstall:
	pip uninstall $(PKGNAME)
build: README.md twist_op.py
	./setup.py sdist bdist_wheel

deploy: build
	twine upload dist/*
test:
	./twist_op.py
check:
	./setup.py check
clean:
	-rm *~ 
	-rm -rf build dist *.egg-info
