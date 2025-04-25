# Metadata Tools

A Python package for working with metadata in various file formats.

## Installation

### From GitHub Package Registry

```bash
pip install cas-metadata-tools --index-url https://github.com/calacademy-research/metadata_tools/packages
```

## Requirements

- Python 3.8 or higher
- ExifTool (must be installed on your system)

### Installing ExifTool

#### macOS
```bash
brew install exiftool
```

#### Ubuntu/Debian
```bash
sudo apt-get install libimage-exiftool-perl
```

#### Windows
Download from [ExifTool website](https://exiftool.org/) and add to your PATH.

## Usage

```python
from cas_metadata_tools import your_module

# Add usage examples here
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/calacademy-research/metadata_tools.git
cd metadata_tools
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

3. Run tests:
```bash
python -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
