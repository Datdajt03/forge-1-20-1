import os
import subprocess
import sys

# Chuyển thư mục làm việc về thư mục chứa file script này
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Lấy thông tin Codespace để tạo IP kết nối
codespace_name = os.environ.get("CODESPACE_NAME")
port_domain = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "app.github.dev")

print("=" * 70)
print("             MINECRAFT FORGE 1.20.1 SERVER LAUNCHER")
print("=" * 70)

if codespace_name:
    public_ip = f"{codespace_name}-25565.{port_domain}"
    print(f"\n[+] Phát hiện đang chạy trong GitHub Codespace!")
    print(f"[+] Cổng Server Minecraft: 25565")
    print(f"[+] ĐỊA CHỈ IP ĐỂ KẾT NỐI (Minecraft Server IP):")
    print(f"    \033[92m\033[1m{public_ip}\033[0m")
    print("\n[!] HƯỚNG DẪN KẾT NỐI:")
    print("    1. Vào tab 'Ports' (Cạnh Terminal).")
    print("    2. Nhấp chuột phải vào port 25565 -> Port Visibility -> Public.")
    print("    3. Copy địa chỉ trên vào mục Direct Connection trong game Minecraft.")
else:
    print(f"\n[+] Đang chạy ở máy local.")
    print(f"[+] IP kết nối: localhost:25565")

def start_playit():
    import urllib.request
    import shutil
    import platform

    if os.path.exists(".disable_playit"):
        print("[+] Phát hiện file .disable_playit, bỏ qua chạy Playit.gg")
        return None

    print("=" * 70)
    print("             CẤU HÌNH PLAYIT.GG (IP PUBLIC ONLINE)")
    print("=" * 70)

    # Xác định hệ điều hành và tải bản phù hợp
    machine = platform.machine().lower()
    
    bin_name = None
    download_url = None
    
    if os.name == 'nt':
        bin_name = "playit.exe"
        download_url = "https://github.com/playit-cloud/playit-agent/releases/download/v1.0.7/playit-windows-x86_64.exe"
    else:
        bin_name = "./playit"
        download_url = "https://github.com/playit-cloud/playit-agent/releases/download/v1.0.7/playit-linux-amd64"
        if "aarch64" in machine or "arm64" in machine:
            download_url = "https://github.com/playit-cloud/playit-agent/releases/download/v1.0.7/playit-linux-aarch64"

    # Kiểm tra xem playit đã được cài đặt trong hệ thống chưa
    global_playit = shutil.which("playit")
    if global_playit:
        print(f"[+] Tìm thấy playit trong hệ thống (PATH): {global_playit}")
        bin_path = global_playit
    else:
        bin_path = os.path.abspath(bin_name)
        if not os.path.exists(bin_path):
            print(f"[-] Không tìm thấy file playit cục bộ. Đang tải xuống từ:\n    {download_url}")
            try:
                # Cấu hình header để tải không bị chặn
                req = urllib.request.Request(
                    download_url, 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                with urllib.request.urlopen(req) as response, open(bin_path, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
                print(f"[+] Tải xuống thành công! Lưu tại: {bin_path}")
                if os.name != 'nt':
                    os.chmod(bin_path, 0o755)
            except Exception as e:
                print(f"[!] Lỗi khi tự động tải playit: {e}")
                print("[!] Vui lòng cài đặt playit thủ công hoặc chạy các lệnh cài đặt.")
                print("=" * 70)
                return None
        else:
            print(f"[+] Sử dụng playit có sẵn tại: {bin_path}")

    print("[+] Đang khởi động Playit.gg...")
    try:
        # Chạy playit và capture output để lấy link claim
        proc = subprocess.Popen([bin_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        # Đọc output để tìm link claim hoặc xác nhận đã kết nối
        claim_url = None
        
        # Đọc tối đa 30 dòng đầu tiên để tìm link
        import re
        import threading
        
        for _ in range(30):
            line = proc.stdout.readline()
            if not line:
                break
            
            line_str = line.strip()
            print(f"[Playit] {line_str}") # In log của playit cho người dùng thấy
            
            # Kiểm tra link claim
            if "claim" in line_str.lower():
                match = re.search(r'https://playit\.gg/claim/[^\s]+', line_str)
                if match:
                    claim_url = match.group(0)
            
            # Nếu đã chạy thành công hoặc tìm thấy link claim
            if "tunnel running" in line_str.lower() or "connected" in line_str.lower() or claim_url:
                break
                
        if claim_url:
            print("\n" + "="*70)
            print("\033[93m\033[1m[!] ĐÂY LÀ LẦN ĐẦU CHẠY PLAYIT.GG!")
            print("Vui lòng click hoặc copy link dưới đây để liên kết thiết bị:")
            print(f"👉 \033[92m{claim_url}\033[0m")
            print("="*70 + "\n")
            input("Sau khi đã liên kết xong trên trang web Playit, nhấn ENTER để tiếp tục chạy Server Minecraft...")
        
        # Khởi động thread phụ để giải phóng buffer tránh bị treo tiến trình
        def drain_output(p):
            for l in p.stdout:
                pass
        
        threading.Thread(target=drain_output, args=(proc,), daemon=True).start()
        
        print("[+] Playit.gg đã chạy thành công trong nền!")
        print("=" * 70)
        return proc
    except Exception as e:
        print(f"[!] Lỗi khi khởi chạy playit: {e}")
        print("=" * 70)
        return None

# Tạo thư mục crash-reports nếu chưa tồn tại
os.makedirs("crash-reports", exist_ok=True)

print("=" * 70)
print("Khởi động Minecraft Server... Vui lòng đợi...")
print("=" * 70)

# Khởi chạy server tùy theo hệ điều hành
playit_proc = None
try:
    playit_proc = start_playit()
    
    if os.name == 'nt':
        # Chạy trên Windows
        subprocess.run(["run.bat"], shell=True)
    else:
        # Chạy trên Linux / Codespace
        # Tìm Java 17 trong Codespace
        import glob
        java_cmd = "java"
        possible_patterns = [
            "/usr/local/sdkman/candidates/java/17*/bin/java",
            "/usr/lib/jvm/java-17*/bin/java",
            "/usr/lib/jvm/jdk-17*/bin/java",
        ]
        found_java_paths = []
        for pattern in possible_patterns:
            found_java_paths.extend(glob.glob(pattern))
        
        if found_java_paths:
            java_cmd = found_java_paths[0]
            print(f"[+] Tìm thấy Java 17 tại: {java_cmd}")
        else:
            print("[-] CẢNH BÁO: Không tìm thấy phiên bản Java 17 trong hệ thống!")
            print("[+] Các phiên bản Java đang có sẵn trong SDKMAN:")
            if os.path.exists("/usr/local/sdkman/candidates/java/"):
                try:
                    print("    " + ", ".join(os.listdir("/usr/local/sdkman/candidates/java/")))
                except Exception:
                    pass

        # Đảm bảo run.sh có quyền thực thi
        os.chmod("run.sh", 0o755)
        env = os.environ.copy()
        env["JAVA_CMD"] = java_cmd
        subprocess.run(["./run.sh"], env=env)
except KeyboardInterrupt:
    print("\n[!] Đang tắt server...")
except Exception as e:
    print(f"[!] Lỗi khi chạy server: {e}")
finally:
    if playit_proc:
        print("[+] Đang dừng Playit.gg...")
        try:
            playit_proc.terminate()
            playit_proc.wait(timeout=5)
            print("[+] Đã tắt Playit.gg thành công!")
        except Exception:
            pass

