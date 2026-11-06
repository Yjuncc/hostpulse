# HostPulse

使用 Python 開發的命令行系統狀態檢查工具。

目前已在 macOS 上完成開發與運行測試，Linux 版本尚未測試。

## 功能

- 查看操作系統、處理器架構和邏輯處理器數量
- 查看主機名稱
- 查看 CPU 使用率
- 查看內存總量和使用率
- 查看硬盤容量和使用率
- 查看系統運行時間

## 運行環境

- Python 3.14
- psutil 7.2.2

## 使用方法

在項目目錄中建立並啟用 Python 虛擬環境：

1. 建立虛擬環境：`python3.14 -m venv .venv`
2. 啟用虛擬環境：`source .venv/bin/activate`
3. 安裝依賴：`python -m pip install -r requirements.txt`
4. 運行程序：`python hostpulse.py`

以上命令適用於 macOS。已建立虛擬環境並安裝依賴的使用者，不需要重複執行前三步。

## 當前版本

v0.1 — 基礎系統資訊檢查工具。每次運行讀取一次系統狀態，不提供持續監控功能。