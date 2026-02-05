# XSS_Scanner
Python-based XSS Scanner that detects reflected XSS vulnerabilities using payload injection. Built for cybersecurity learning and SOC analyst practice.
# XSS Scanner 🔍

A simple Python-based XSS scanner that detects reflected Cross-Site Scripting (XSS) vulnerabilities by injecting payloads into URL parameters.

## Features
- Reflected XSS detection
- Custom payload list
- Beginner-friendly Python code
- Uses requests library

## Requirements
- Python 3.x
- requests

## Installation
```bash
pip install -r requirements.txt
python scanner.py
http://testphp.vulnweb.com/listproducts.php?cat=
