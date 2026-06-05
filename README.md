# Minecraft Forge 1.20.1 Server

Dự án chứa mã nguồn và các file cấu hình cho Minecraft Forge Server phiên bản 1.20.1.

## Hướng dẫn Khởi chạy trên GitHub Codespace

### 1. Khởi chạy Server
Để khởi động server Minecraft trong môi trường Codespace (Linux), hãy chạy lệnh sau trong Terminal:
```bash
chmod +x run.sh
./run.sh
```

*(Nếu chạy trên hệ điều hành Windows cục bộ, bạn có thể nhấp đúp vào `run.bat` hoặc chạy lệnh `./run.bat`)*

### 2. Cấu hình Port và Kết nối cho người chơi
Mặc định, server sẽ chạy trên cổng `25565` (được cấu hình trong `server.properties`). Để bạn bè có thể kết nối vào server:

1. Chuyển sang tab **Ports** trong cửa sổ VS Code / Codespaces (thường nằm ở thanh dưới cùng bên cạnh Terminal).
2. Chọn **Forward a Port** (nếu cổng `25565` chưa tự động được forward).
3. Nhập cổng `25565`.
4. **Quan trọng:** Nhấp chuột phải vào cổng `25565` vừa forward, chọn **Port Visibility** -> **Public** (để cho phép kết nối từ bên ngoài).
5. Copy địa chỉ ở cột **Forwarded Address** (ví dụ: `your-codespace-name-25565.app.github.dev`).

### 3. Nhập IP vào Game
* Mở Minecraft client (đã cài đặt Forge 1.20.1 và đồng bộ các mod trong thư mục `mods`).
* Chọn **Multiplayer** (Chơi mạng) -> **Direct Connection** (Kết nối trực tiếp) hoặc **Add Server** (Thêm máy chủ).
* Nhập địa chỉ đã copy ở trên (lưu ý xóa tiền tố `https://` đi nếu có, chỉ lấy phần domain: `your-codespace-name-25565.app.github.dev`).

> [!TIP]
> Nếu game Minecraft không hỗ trợ kết nối trực tiếp qua domain `.app.github.dev`, bạn có thể cài đặt `playit.gg` hoặc `ngrok` trực tiếp trên Codespace để lấy địa chỉ IP kết nối dạng `tên-miền:cổng` ổn định hơn.
