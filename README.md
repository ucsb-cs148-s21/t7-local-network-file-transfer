# LOFT: LOcal File Transfer #
> It’s not the cloud. It’s closer. It’s your Loft.

Loft makes moving files _easy_, without using the Internet! Anyone who just needs a simple solution to moving files between two devices on the same network can use Loft.

## Table of Contents ##
- [User Manual](docs/MANUAL.md)
- [Build Instructions](docs/BUILD.md)
- [Design](docs/DOCS.md)

## Repository Structure ##
- `loft/` Source files and assets.
  - `loft/ui` Native UI.
    - `loft/ui/widgets` Qt widget factories.
  - `loft/web` Web UI.
    - `loft/web/blueprints` API and template rendering.
    - `loft/web/templates` Flask templates for Web UI.
    - `loft/web/static` Static resources for Web UI.
- `test/` Tests.
- `docs/` Documentation.
- `team/` Agile development notes.

## Implementation ##
Loft is built using Flask and Werkzeug to provide file transfer, and PyQt5 to render its native UI on Linux, macOS, and Windows. The web client UI is rendered using standard HTML5 / JS.

## Contributing ##

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
4. Commit your changes: `git commit -am 'Add my new feature'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request :D


### Members ###
- Andrew Tran (`at527`)
- Ethan Wu (`ethwu`)
- Douglas Yuan (`dougyuan`)
- Zackery Mondin (`zmondin`)
- Kevin Pham (`kevbbn`)
