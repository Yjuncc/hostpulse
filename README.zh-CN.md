# HostPulse

[English](https://github.com/Yjuncc/hostpulse/blob/main/README.md) | [简体中文](https://github.com/Yjuncc/hostpulse/blob/main/README.zh-CN.md) | [繁體中文](https://github.com/Yjuncc/hostpulse/blob/main/README.zh-TW.md)

HostPulse 是一款使用 Python 开发的开源命令行系统状态检查工具。

它可以快速查看本机的操作系统、CPU、内存、硬盘及系统运行时间等基本信息。

每次执行时，HostPulse 会读取并显示一次系统状态，随后自动退出程序。

## 功能

HostPulse v0.1.0 提供以下功能：

- **操作系统**：查看当前使用的操作系统。
- **处理器架构**：查看 CPU 架构，例如 ARM64、x86_64。
- **逻辑处理器数量**：查看系统识别的逻辑 CPU 数量。
- **主机名称**：查看电脑的主机名称。
- **CPU 使用率**：查看当前的 CPU 使用率。
- **内存信息**：查看内存总量和使用率。
- **硬盘信息**：查看系统根目录所在分区的容量和使用率。
- **系统运行时间**：查看距离上次开机经过的时间。

## 系统要求

- Python 3.14 或更高版本
- psutil 7.2.2

通过 pip 安装 HostPulse 时，会自动安装所需的 psutil 依赖。

## 测试环境

HostPulse v0.1.0 已在以下环境完成本地安装与运行测试：

- **操作系统**：macOS（Apple Silicon）
- **Python**：3.14
- **psutil**：7.2.2

已通过 Python 安装包构建、本地安装、命令行运行及卸载测试。

目前程序输出的系统信息标签使用繁体中文。

## 安装

HostPulse 通过 PyPI（Python 软件包索引）发布，可以使用 pip 安装。

建议使用 Python 虚拟环境，避免与其他项目的依赖产生冲突。

**1. 创建虚拟环境**

在 macOS 终端中执行：

```bash
python3.14 -m venv .venv
```

**2. 激活虚拟环境**

```bash
source .venv/bin/activate
```

**3. 安装 HostPulse**

```bash
python -m pip install hostpulse
```

pip 会从 PyPI 下载并安装 HostPulse 及其所需依赖。

## 使用方法

安装完成后，在已激活的 Python 虚拟环境中执行：

```bash
hostpulse
```

程序会显示当前的系统信息，包括 CPU、内存、硬盘使用情况及系统运行时间。

输出完成后，程序会自动退出，无需额外配置。

## 从源代码运行

除了通过 PyPI 安装，也可以从 GitHub 获取完整源代码。

**1. 克隆项目仓库**

```bash
git clone https://github.com/Yjuncc/hostpulse.git
```

**2. 进入项目目录**

```bash
cd hostpulse
```

**3. 创建并激活虚拟环境**

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

**4. 安装依赖**

```bash
python -m pip install -r requirements.txt
```

**5. 运行 HostPulse**

```bash
python hostpulse.py
```

也可以在项目目录中，不激活虚拟环境，直接执行：

```bash
.venv/bin/python hostpulse.py
```

## 项目与版本发布

HostPulse 使用 Git 进行版本控制，源代码托管于 GitHub，Python 安装包通过 PyPI 分发。

- **GitHub 项目**：[Yjuncc/hostpulse](https://github.com/Yjuncc/hostpulse)
- **GitHub Releases**：[查看正式发布版本](https://github.com/Yjuncc/hostpulse/releases)
- **PyPI**：[HostPulse 软件包](https://pypi.org/project/hostpulse/)

GitHub 提供完整源代码、项目文档和版本发布记录。

PyPI 提供 Python 安装包，方便用户通过 pip 安装。

## 当前版本

**HostPulse v0.1.0 — 首个正式版本**

此版本提供基础系统状态检查功能，采用 Python 命令行方式运行。

## 开源许可证

HostPulse 采用 MIT 开源许可证。

你可以根据 MIT License 条款使用、修改及分发本项目的源代码。

完整许可证内容请参阅 [LICENSE](https://github.com/Yjuncc/hostpulse/blob/main/LICENSE)。

Copyright (c) 2026 Yjunc
