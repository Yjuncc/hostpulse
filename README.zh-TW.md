# HostPulse

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

HostPulse 是一款使用 Python 開發的命令行系統狀態檢查工具。

每次運行時讀取並顯示一次本機系統資訊。目前版本不支援持續監控。

## 功能

- 查看操作系統、處理器架構和邏輯處理器數量
- 查看主機名稱
- 查看 CPU 使用率
- 查看內存總量和使用率
- 查看硬盤容量和使用率
- 查看系統運行時間

## 已測試環境

- macOS
- Python 3.14
- psutil 7.2.2

Linux 和 Windows 兼容性尚未測試。

## 本地開發與運行

打開終端機，進入 HostPulse 項目目錄。

1. 建立虛擬環境：`python3.14 -m venv .venv`
2. 啟用虛擬環境：`source .venv/bin/activate`
3. 安裝依賴：`python -m pip install -r requirements.txt`
4. 運行程序：`python hostpulse.py`

如果已經建立虛擬環境並安裝依賴，可以跳過前三步。

也可以在項目目錄中直接運行，無需啟用虛擬環境：

`.venv/bin/python hostpulse.py`

## 打包狀態

HostPulse 使用 `pyproject.toml` 和 setuptools 配置 Python 標準打包。

已經配置 `hostpulse` 命令行入口，對應 `hostpulse:main`。

標準安裝包構建、本地安裝測試及 PyPI 正式發布尚未完成。

## 當前版本

**v0.1.0**

基礎系統狀態檢查功能。

## 許可證

本項目採用 MIT 開源許可證，完整條款請參閱 [LICENSE](LICENSE)。

Copyright (c) 2026 Yjunc