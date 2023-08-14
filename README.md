# Favicon-Grabber

Python functions to download favicons using internal google api

## Installation

Install function by running the following command.

```bash
  pip install favicon-grabber
```

## Usage/Examples

```python
from favicon-grabber import download_favicon, download_favicons

# Single download
download_favicon("google.com", size=128)

# Multiple downloads
websites = ["google.com", "stackoverflow.com", "github.com"]
download_favicons(websites, path="my/path/favicons")
```

NOTE: The file is saved to a directory under the name *website.com*.png

## Acknowledgements
- [aanupam23](https://github.com/aanupam23/FaviconGrabber/tree/main)