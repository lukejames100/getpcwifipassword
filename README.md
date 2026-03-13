# getpcwifipassword
EN: A lightweight Windows tool to retrieve saved WiFi passwords and export them to Excel. Supports English &amp; Japanese. JP: 接続済みWiFiのパスワードを取得し、Excelに保存できるWindows向け軽量ツール。英語・日本語の両方に対応。
# WiFi Password Retriever | WiFiパスワード取得ツール

[English](#english) | [日本語](#日本語)

---

## English

### Description
A simple Python-based utility for Windows that retrieves all saved WiFi SSIDs and their corresponding passwords. The tool displays the information in a clear table and provides an option to export the results to an Excel file.

### Key Features
* **Retrieve Passwords**: Fetch clear-text passwords for all previously connected WiFi networks.
* **Dual Language**: Support for English and Japanese (auto-detects system encoding to prevent mojibake/garbled text).
* **Excel Export**: Save your WiFi list to `wifilist.xlsx` in the same directory.
* **UAC Support**: Automatically requests Administrator privileges to ensure system access.

### How to Use
1. Download the `WiFiScanner.exe` from the Releases page (or run the script directly).
2. **Right-click** and select **"Run as Administrator"**.
3. View the WiFi list on the console.
4. Type `y` to export to Excel or `x` to exit.

### Requirements (For source code)
* Python 3.x
* pandas
* openpyxl

---

## 日本語

### 概要
Windows PCに保存されているWiFiのSSIDとパスワードを一覧表示するシンプルなツールです。取得したデータはコンソール上で確認できるほか、Excelファイルとして書き出すことも可能です。

### 主な機能
* **パスワード取得**: 過去に接続したWiFiのパスワードをプレーンテキストで取得。
* **二ヶ国語対応**: 英語と日本語のバイリンガル表示。システム文字コード（CP932/UTF-8）を自動判別し、文字化けを防止します。
* **Excel出力**: 実行ファイルと同じディレクトリに `wifilist.xlsx` という名前で保存。
* **管理者権限の自動要求**: パスワード読み取りに必要な権限を自動的にリクエストします。

### 使い方
1. `WiFiScanner.exe` をダウンロードします。
2. ファイルを**右クリック**し、**「管理者として実行」**を選択します。
3. 画面上に表示されるWiFiリストを確認します。
4. Excelに保存する場合は `y` を、終了する場合は `x` を入力してください。

### 動作環境（ソースコードから実行する場合）
* Python 3.x
* pandas
* openpyxl

---

## Disclaimer / 免責事項
* **EN**: This tool is for personal use and educational purposes only. Do not use it on computers you do not own or have explicit permission to access.
* **JP**: 本ツールは個人利用および学習目的のみを意図しています。所有権のない、またはアクセス許可を得ていないデバイスでの使用は固く禁じます。

## License
MIT License
