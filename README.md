
# Dramabox

Dramabox Block Ads

## Overview

Dramabox is a Python-based tool designed to block or skip ads on the Dramabox streaming platform. By leveraging browser automation, it helps users enjoy ad-free streaming experiences by intercepting and blocking advertisement content.

## Features

- Blocks ads on Dramabox streaming site
- Uses Python automation (e.g., Pyppeteer) to intercept ad requests
- Lightweight and easy to use
- Open source under the MIT License

## Installation

1. Clone the repository:

```
git clone https://github.com/DexterZero/Dramabox.git
cd Dramabox
```

2. Install dependencies (Pyppeteer):

```
pip install pyppeteer
```

## Usage

Run the main script to launch the automated browser session with ad blocking enabled:

```
python dr.py
```

This will open a Chromium browser window, navigate to Dramabox, and block ads automatically.

## Notes

- The script runs in non-headless mode for easier debugging.
- You can customize the ad-blocking rules by editing the script.
- Some ads may be served inline or via obfuscated scripts; blocking effectiveness may vary.

## License

This project is licensed under the MIT License.

---
