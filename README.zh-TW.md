# HostPulse

[English](https://github.com/Yjuncc/hostpulse/blob/main/README.md) | [简体中文](https://github.com/Yjuncc/hostpulse/blob/main/README.zh-CN.md) | [繁體中文](https://github.com/Yjuncc/hostpulse/blob/main/README.zh-TW.md)

HostPulse 是一款使用 Python 開發的開源命令行系統狀態檢查工具。

它可以快速查看本機的操作系統、CPU、內存、硬盤及系統運行時間等基本資訊。

每次執行時，HostPulse 會讀取並顯示一次系統狀態，隨後自動結束程序。

## 功能

HostPulse v0.1.0 提供以下功能：

- **操作系統**：查看目前使用的操作系統。
- **處理器架構**：查看 CPU 架構，例如 ARM64、x86_64。
- **邏輯處理器數量**：查看系統識別的邏輯 CPU 數量。
- **主機名稱**：查看電腦的主機名稱。
- **CPU 使用率**：查看目前的 CPU 使用率。
- **內存資訊**：查看內存總量和使用率。
- **硬盤資訊**：查看系統根目錄所在分區的容量和使用率。
- **系統運行時間**：查看距離上次開機經過的時間。

## 系統要求

- Python 3.14 或更高版本
- psutil 7.2.2

透過 pip 安裝 HostPulse 時，會自動安裝所需的 psutil 依賴。

## 測試環境

HostPulse v0.1.0 已在以下環境完成本地安裝與運行測試：

- **操作系統**：macOS（Apple Silicon）
- **Python**：3.14
- **psutil**：7.2.2

已通過 Python 安裝包構建、本地安裝、命令行運行及卸載測試。

目前程序輸出的系統資訊標籤使用繁體中文。

## 安裝

HostPulse 透過 PyPI（Python 軟件包索引）發布，可以使用 pip 安裝。

建議使用 Python 虛擬環境，避免與其他項目的依賴產生衝突。

**1. 建立虛擬環境**

在 macOS 終端機中執行：

```bash
python3.14 -m venv .venv
```

**2. 啟用虛擬環境**

```bash
source .venv/bin/activate
```

**3. 安裝 HostPulse**

```bash
python -m pip install hostpulse
```

pip 會從 PyPI 下載並安裝 HostPulse 及其所需依賴。

## 使用方法

安裝完成後，在已啟用的 Python 虛擬環境中執行：

```bash
hostpulse
```

程序會顯示目前的系統資訊，包括 CPU、內存、硬盤使用情況及系統運行時間。

輸出完成後，程序會自動退出，無需額外配置。

## 從源代碼運行

除了透過 PyPI 安裝，也可以從 GitHub 取得完整源代碼。

**1. 克隆項目倉庫**

```bash
git clone https://github.com/Yjuncc/hostpulse.git
```

**2. 進入項目目錄**

```bash
cd hostpulse
```

**3. 建立並啟用虛擬環境**

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

**4. 安裝依賴**

```bash
python -m pip install -r requirements.txt
```

**5. 運行 HostPulse**

```bash
python hostpulse.py
```

也可以在項目目錄中，不啟用虛擬環境，直接執行：

```bash
.venv/bin/python hostpulse.py
```

## 項目與版本發布

HostPulse 使用 Git 進行版本控制，源代碼託管於 GitHub，Python 安裝包透過 PyPI 分發。

- **GitHub 項目**：[Yjuncc/hostpulse](https://github.com/Yjuncc/hostpulse)
- **GitHub Releases**：[查看正式發布版本](https://github.com/Yjuncc/hostpulse/releases)
- **PyPI**：[HostPulse 軟件包](https://pypi.org/project/hostpulse/)

GitHub 提供完整源代碼、項目文檔和版本發布記錄。

PyPI 提供 Python 安裝包，方便使用者透過 pip 安裝。

## 當前版本

**HostPulse v0.1.0 — 首個正式版本**

此版本提供基礎系統狀態檢查功能，採用 Python 命令行方式運行。

## 開源許可證

HostPulse 採用 MIT 開源許可證。

你可以根據 MIT License 條款使用、修改及分發本項目的源代碼。

完整許可證內容請參閱 [LICENSE](https://github.com/Yjuncc/hostpulse/blob/main/LICENSE)。

Copyright (c) 2026 Yjunc
