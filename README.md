PREREQUISITES:
==============
You need [Poetry](https://python-poetry.org/).

Check for it with `poetry -V`.

If not present, install it with [Scoop](https://scoop.sh/) via [pipx](https://pipx.pypa.io/):

```
scoop install python
scoop install pipx
pipx install poetry
```

RUN:
====

Run `start.py`, **or** directly `poetry run jupyter lab`.


MODIFY:
=======

[Add](https://python-poetry.org/docs/cli/#add) dependenties:
```
poetry add numpy
```
```
poetry add numpy tensorflow
```

[Remove](https://python-poetry.org/docs/cli/#remove) dependenties:
```
poetry remove numpy
```
```
poetry remove numpy tensorflow
```

[Update](https://python-poetry.org/docs/cli/#update) `poetry.lock`:
```
poetry update
```
```
poetry update numpy
```
```
poetry update numpy tensorflow
```
