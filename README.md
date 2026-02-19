# bson-modern

[![PyPI version](https://badge.fury.io/py/bson-modern.svg)](https://pypi.org/project/bson-modern/)
[![Python versions](https://img.shields.io/pypi/pyversions/bson-modern.svg)](https://pypi.org/project/bson-modern/)
[![Downloads](https://static.pepy.tech/badge/bson-modern)](https://pepy.tech/project/bson-modern)
[![License](https://img.shields.io/pypi/l/bson-modern.svg)](https://github.com/westover/bson-modern/blob/main/LICENSE)

A modernized fork of the [bson](https://github.com/py-bson/bson) package with Python 3.9+ support.

**PyPI:** https://pypi.org/project/bson-modern/

## Why this fork?

The original `bson` package has not been updated since 2019 and is incompatible with Python 3.12+ due to:
- Use of deprecated `pkgutil.find_loader()` (removed in Python 3.12)
- Dependency on the `six` package for Python 2/3 compatibility

This fork removes all Python 2 compatibility code and modernizes the package for Python 3.9+.

## Installation

```bash
pip install bson-modern
```

## Usage

```python
import bson

# Encode a dictionary to BSON
data = {"name": "Alice", "age": 30, "active": True}
encoded = bson.dumps(data)

# Decode BSON back to dictionary
decoded = bson.loads(encoded)
print(decoded)  # {'name': 'Alice', 'age': 30, 'active': True}
```

## Compatibility with antares-client

This package is designed to be a drop-in replacement for `bson` when using packages like `antares-client` that depend on standalone BSON support.

To use with `antares-client`, install `bson-modern` before `antares-client`:

```bash
pip install bson-modern antares-client
```

Or in your `pyproject.toml`:

```toml
dependencies = [
    "bson-modern>=1.0.0",
    "antares-client>=1.3.0",
]
```

## Changes from original bson

- **Python 3.9+ only** - Dropped Python 2.x and early Python 3.x support
- **Removed `six` dependency** - No longer needed for Python 2/3 compatibility
- **Modern packaging** - Uses `pyproject.toml` and `hatchling`
- **Fixed build system** - No longer uses deprecated `pkgutil.find_loader()`

## License

BSD-3-Clause (same as original)

## Credits

- Original `bson` package by Kou Man Tong and Ayun Park
- Modernization by James Westover
