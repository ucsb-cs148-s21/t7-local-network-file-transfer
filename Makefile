
.PHONY: build
build:
	python3 -OO -m build

.PHONY: test
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
