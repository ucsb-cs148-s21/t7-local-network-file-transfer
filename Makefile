
# the name of the application
name := loft
src := loft/__main__.py
flask_resources := loft/web/
templates := $(flask_resources)/templates/
static := $(flask_resources)/static/

uname := $(shell uname)

ifeq ($(uname, Linux))
target := $(name)

else ifeq ($(uname, Darwin))
target := $(name).app

else
target := $(name).exe

endif

build: $(target)

# linux application
.PHONY: $(name)
$(name): $(src)
	pyinstaller -n $@ --onefile \
		--add-data "$(templates):$(templates)" \
		--add-data "$(static):$(static)" \
		$^

# mac application
.PHONY: $(name).app
$(name).app: $(src)
	pyinstaller -n $@ --onefile \
		--add-data "$(templates):$(templates)" \
		--add-data "$(static):$(static)" \
		$^

# windows application
.PHONY: $(name).exe
$(name).exe: $(src)
	pyinstaller -n $@ --onefile \
		--add-data "$(templates);$(templates)" \
		--add-data "$(static);$(static)" \
		$^

.PHONY: test
	pytest

.PHONY: clean
clean:
	rm -f $(name) $(name).app $(name).exe
