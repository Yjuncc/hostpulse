# HostPulse

[English](https://github.com/Yjuncc/hostpulse/blob/main/README.md) | [简体中文](https://github.com/Yjuncc/hostpulse/blob/main/README.zh-CN.md) | [繁體中文](https://github.com/Yjuncc/hostpulse/blob/main/README.zh-TW.md)

HostPulse is an open-source Python command-line tool for checking local system status.

It provides a quick overview of the operating system, CPU, memory, disk, and system uptime.

Each time HostPulse runs, it reads and displays the system status once and then exits automatically.

## Features

HostPulse v0.1.0 provides the following features:

- **Operating system**: Display the operating system in use.
- **CPU architecture**: Display the processor architecture, such as ARM64 or x86_64.
- **Logical CPU count**: Display the number of logical CPUs detected by the system.
- **Hostname**: Display the computer's hostname.
- **CPU usage**: Display the current CPU usage percentage.
- **Memory information**: Display total memory and memory usage percentage.
- **Disk information**: Display the capacity and usage percentage of the filesystem containing the system root directory.
- **System uptime**: Display the time elapsed since the last system boot.

## Requirements

- Python 3.14 or newer
- psutil 7.2.2

When HostPulse is installed through pip, the required psutil dependency is installed automatically.

## Tested Environment

HostPulse v0.1.0 has completed local installation and execution testing in the following environment:

- **Operating system**: macOS (Apple Silicon)
- **Python**: 3.14
- **psutil**: 7.2.2

Python package building, local installation, command-line execution, and uninstallation tests have passed.

The program currently displays system information labels in Traditional Chinese.

## Installation

HostPulse is distributed through PyPI (the Python Package Index) and can be installed using pip.

Using a Python virtual environment is recommended to avoid dependency conflicts with other projects.

**1. Create a virtual environment**

Run the following command in the macOS Terminal:

```bash
python3.14 -m venv .venv
```

**2. Activate the virtual environment**

```bash
source .venv/bin/activate
```

**3. Install HostPulse**

```bash
python -m pip install hostpulse
```

pip downloads and installs HostPulse and its required dependencies from PyPI.

## Usage

After installation, run the following command in the activated Python virtual environment:

```bash
hostpulse
```

The program displays the current system information, including CPU, memory, disk usage, and system uptime.

It exits automatically after displaying the results and requires no additional configuration.

## Running from Source

In addition to installing from PyPI, you can obtain the complete source code from GitHub.

**1. Clone the repository**

```bash
git clone https://github.com/Yjuncc/hostpulse.git
```

**2. Enter the project directory**

```bash
cd hostpulse
```

**3. Create and activate a virtual environment**

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

**4. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**5. Run HostPulse**

```bash
python hostpulse.py
```

You can also run the program from the project directory without activating the virtual environment:

```bash
.venv/bin/python hostpulse.py
```

## Project and Releases

HostPulse uses Git for version control. Its source code is hosted on GitHub, and Python packages are distributed through PyPI.

- **GitHub repository**: [Yjuncc/hostpulse](https://github.com/Yjuncc/hostpulse)
- **GitHub Releases**: [View official releases](https://github.com/Yjuncc/hostpulse/releases)
- **PyPI**: [HostPulse package](https://pypi.org/project/hostpulse/)

GitHub provides the complete source code, project documentation, and version release history.

PyPI provides Python installation packages so users can install HostPulse through pip.

## Current Version

**HostPulse v0.1.0 — Initial Release**

This version provides basic system status checking through a Python command-line interface.

## Open Source License

HostPulse is licensed under the MIT License.

You may use, modify, and distribute the project's source code under the terms of the MIT License.

For the complete license terms, see [LICENSE](https://github.com/Yjuncc/hostpulse/blob/main/LICENSE).

Copyright (c) 2026 Yjunc
