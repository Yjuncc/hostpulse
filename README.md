# HostPulse

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

HostPulse is a Python command-line tool for checking the status of your local system.

It displays a snapshot of system information each time it runs. Continuous monitoring is not supported in this version.

## Features

- Display the operating system, CPU architecture, and logical CPU count
- Display the hostname
- Display CPU usage
- Display total memory and memory usage
- Display disk capacity and disk usage
- Display system uptime

## Tested Environment

- macOS
- Python 3.14
- psutil 7.2.2

Linux and Windows compatibility have not yet been tested.

## Local Development and Usage

Open a terminal and navigate to the HostPulse project directory.

1. Create a virtual environment: `python3.14 -m venv .venv`
2. Activate it: `source .venv/bin/activate`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run HostPulse: `python hostpulse.py`

If the virtual environment and dependencies are already set up, you can skip the first three steps.

Alternatively, run HostPulse directly from the project directory without activating the virtual environment:

`.venv/bin/python hostpulse.py`

## Packaging Status

HostPulse uses `pyproject.toml` and setuptools for Python packaging.

The command-line entry point `hostpulse` is configured to call `hostpulse:main`.

Package building, local installation testing, and publication to PyPI have not yet been completed.

## Version

**v0.1.0**

Initial system status checking functionality.

## License

HostPulse is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Copyright (c) 2026 Yjunc