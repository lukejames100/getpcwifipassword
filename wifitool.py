import subprocess
import pandas as pd
import os
import sys
import ctypes

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def get_wifi_profiles():
    profiles_data = []
    
    # 尝试多种编码方案，确保读取不乱码
    encodings = ['cp932', 'utf-8', 'gbk']
    raw_out = ""
    
    for enc in encodings:
        try:
            raw_out = subprocess.check_output('netsh wlan show profiles', shell=True).decode(enc)
            break
        except: continue

    # 提取所有 SSID
    profile_names = []
    for line in raw_out.split('\n'):
        if ":" in line:
            name = line.split(":")[1].strip()
            if name and "---" not in name:
                profile_names.append(name)

    for name in profile_names:
        profile_info = {"SSID": name, "Password": "(None/無し)"}
        try:
            # 获取详细信息
            detail_raw = ""
            for enc in encodings:
                try:
                    detail_raw = subprocess.check_output(f'netsh wlan show profile name="{name}" key=clear', shell=True).decode(enc)
                    break
                except: continue
            
            # 【核心改进】：不再匹配固定词汇，扫描所有包含冒号的行
            for line in detail_raw.split('\n'):
                if ":" in line:
                    parts = line.split(":", 1)
                    value = parts[1].strip()
                    
                    # 关键逻辑：如果这一行不是 SSID 名字本身，且不是“有/无”，且长度符合密码特征
                    # 在 netsh 输出中，密码通常出现在“主要な内容”后面
                    # 我们通过排除法锁定它
                    label = parts[0].strip()
                    if any(x in label for x in ["主要", "Key", "关键", "内容"]):
                        if value != "Present" and value != "あり" and value != "内容":
                            profile_info["Password"] = value
                            break
        except:
            profile_info["Password"] = "(Error)"
            
        profiles_data.append(profile_info)
    
    return profiles_data

def main():
    if not is_admin():
        # 自动请求管理员权限
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    print("==================================================")
    print("WiFi Password Retriever / WiFiパスワード取得ツール")
    print("==================================================")
    
    wifi_list = get_wifi_profiles()
    df = pd.DataFrame(wifi_list)
    
    # 强制在控制台显示完整内容，不打省略号
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.unicode.east_asian_width', True) # 解决中日文对齐乱码
    
    print(df[['SSID', 'Password']].to_string(index=False))

    print("\n--------------------------------------------------")
    print("Export to Excel? (y: Yes / x: Exit)")
    user_input = input("Excelに書き出しますか？ (y: はい / x: 終了): ").lower()

    if user_input == 'y':
        file_path = os.path.join(os.getcwd(), "wifilist.xlsx")
        try:
            df.to_excel(file_path, index=False)
            print(f"\n[Success] {file_path}")
        except Exception as e:
            print(f"\n[Error] {e}")
        input("\nPress Enter to exit...")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
