# HostPulse

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

HostPulse 是一款使用 Python 开发的命令行系统状态检查工具。

每次运行时读取并显示一次本机系统信息。当前版本不支持持续监控。

## 功能

- 查看操作系统、处理器架构和逻辑处理器数量
- 查看主机名称
- 查看 CPU 使用率
- 查看内存总量和使用率
- 查看硬盘容量和使用率
- 查看系统运行时间

## 已测试环境

- macOS
- Python 3.14
- psutil 7.2.2

Linux 和 Windows 兼容性尚未测试。

## 本地开发与运行

打开终端，进入 HostPulse 项目目录。

1. 创建虚拟环境：`python3.14 -m venv .venv`
2. 激活虚拟环境：`source .venv/bin/activate`
3. 安装依赖：`python -m pip install -r requirements.txt`
4. 运行程序：`python hostpulse.py`

如果已经创建虚拟环境并安装依赖，可以跳过前三步。

也可以在项目目录中直接运行，无需激活虚拟环境：

`.venv/bin/python hostpulse.py`

## 打包状态

HostPulse 使用 `pyproject.toml` 和 setuptools 配置 Python 标准打包。

已经配置 `hostpulse` 命令行入口，对应 `hostpulse:main`。

标准安装包构建、本地安装测试及 PyPI 正式发布尚未完成。

## 当前版本

**v0.1.0**

基础系统状态检查功能。

## 许可证

本项目采用 MIT 开源许可证，完整条款请参阅 [LICENSE](LICENSE)。

Copyright (c) 2026 Yjunc