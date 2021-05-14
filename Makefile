
# the name of the application
name := loft
# folder where the built executable will be
dist := dist

ifeq ($(shell uname) == Darwin)
target := $(dist)/$(name).app
else
target := $(dist)/$(name)
endif

.PHONY: build
build: $(target)

$(dist)/$(name):
	python3 -OO -m build

$(dist)/$(name).app:
	python3 setup.py bdist_mac --custom-info-plist Info-highres.plist


.PHONY: test
test:
	pytest

.PHONY: clean
clean:
	# https://stackoverflow.com/a/41386937
	# clean up __pycache__, *.pyc, and *.pyo
	python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
	# remove pyinstaller build artifacts
	/bin/rm -f *.spec
	/bin/rm -rf build dist
