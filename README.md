# 🧟 Minecraft Forge 1.20.1 Server — Zombie Apocalypse Modpack

Server Minecraft Forge 1.20.1 với modpack chủ đề **Zombie Apocalypse** — sinh tồn, súng, thành phố hoang phế và hàng trăm mod hấp dẫn.

---

## 📋 Thông tin Server

| Mục | Chi tiết |
|---|---|
| **Phiên bản MC** | 1.20.1 |
| **Forge** | 47.4.20 |
| **Java** | 17 (Eclipse Adoptium) |
| **RAM** | 4096 MB |
| **Game Mode** | Survival |
| **Online Mode** | Offline (cracked supported) |

---

## 🚀 Hướng dẫn Khởi chạy

### Trên GitHub Codespace (Linux)
```bash
chmod +x run.sh
./run.sh
```

### Trên Windows (Local)
```bat
run.bat
```
hoặc nhấp đúp vào file `run.bat`.

---

## 🌐 Kết nối vào Server

### Cách 1: Playit.gg (Khuyên dùng)
1. Chạy `playit` agent trong Codespace Terminal
2. Lấy địa chỉ IP từ Playit dashboard
3. Vào Minecraft → **Multiplayer** → **Direct Connection** → nhập IP

### Cách 2: GitHub Codespace Port Forward
1. Vào tab **Ports** trong VS Code / Codespaces
2. Forward cổng `25565` → đặt **Port Visibility** thành **Public**
3. Copy địa chỉ `*.app.github.dev` → xóa `https://` → nhập vào game

> [!IMPORTANT]
> Client phải cài **Forge 1.20.1** và có **cùng bộ mod** với server trong thư mục `mods/`.

---

## 🔫 Danh sách Mod chính

### 🧟 Zombie / Survival
| Mod | Mô tả |
|---|---|
| **Apocalypse Now** | Zombie apocalypse toàn diện |
| **The Hordes** | Làn sóng zombie theo ngày |
| **Zombie Awareness** | Zombie thông minh hơn |
| **Zombie Break & Build** | Zombie phá và xây block |
| **Mutant Zombies** | Zombie đột biến siêu mạnh |
| **Lost Souls** | Linh hồn trong thành phố |
| **Zombie Game** | Hệ thống zombie mới |

### 🔫 Súng & Vũ khí
| Mod | Mô tả |
|---|---|
| **TACZ** (Timeless & Classics Zero) | Hệ thống súng chi tiết |
| **LRADD** | Gun pack bổ sung cho TACZ |
| **LR Tactical** | Chiến thuật và phụ kiện |
| **Spartan Weaponry** | Vũ khí cận chiến đa dạng |
| **Spartan Shields** | Khiên chiến đấu |
| **Enchanted Arsenal** | Vũ khí phép thuật |

### 🏙️ Thế giới & Cấu trúc
| Mod | Mô tả |
|---|---|
| **Lost Cities** | Thành phố hoang phế |
| **Lost Cities Multithreaded** | Tăng tốc gen thành phố |
| **Biomes O' Plenty** | Biome phong phú |
| **Dungeon Crawl** | Ngục tối |
| **Underground Bunkers** | Hầm ngầm ẩn |
| **Post-Apocalypse Structures** | Công trình tận thế |
| **Modern Structures** | Cấu trúc hiện đại |
| **Radio Towers** | Tháp radio |

### 👥 NPC & AI
| Mod | Mô tả |
|---|---|
| **Recruits** | Tuyển quân chiến đấu |
| **Workers** | NPC làm việc |
| **Guard Villagers** | Villager có lính bảo vệ |
| **Enhanced AI** | AI mob thông minh hơn |
| **AI Improvements** | Cải thiện AI tổng thể |

### 🎒 Trang bị & Sinh tồn
| Mod | Mô tả |
|---|---|
| **Sophisticated Backpacks** | Ba lô nâng cấp |
| **Immersive Armors** | Giáp đa dạng đẹp mắt |
| **LR Armor** | Giáp chiến thuật |
| **Tough As Nails** | Cơ chế khát nước, thân nhiệt |
| **Comforts** | Ngủ túi ngủ & võng |
| **Caelus** | API Elytra |
| **Elytra Slot** | Slot Elytra riêng |
| **Gliders** | Lượn trên không |
| **Do a Barrel Roll** | Điều khiển Elytra tự do |

### 🗺️ Bản đồ & UI
| Mod | Mô tả |
|---|---|
| **Xaero's Minimap** | Bản đồ góc màn hình |
| **Xaero's World Map** | Bản đồ thế giới |
| **Waystones** | Điểm teleport |
| **FancyMenu** | Tùy chỉnh menu game |
| **JEI** | Xem công thức craft |
| **Jade** | Thông tin block/entity |
| **AppleSkin** | Hiển thị độ no chi tiết |

### ⚡ Tối ưu hiệu năng
| Mod | Mô tả |
|---|---|
| **ModernFix** | Fix và tối ưu Forge |
| **Embeddium** | Render nhanh hơn (Sodium fork) |
| **Radium** | Tối ưu vật lý |
| **Starlight** | Tối ưu hệ thống ánh sáng |
| **FerriteCore** | Giảm RAM usage |
| **MemoryLeakFix** | Fix memory leak |
| **Krypton** | Tối ưu network |

---

## 📁 Cấu trúc Thư mục

```
forge-1-20-1/
├── mods/           # Tất cả mod (.jar)
├── tacz/           # Gun pack cho TACZ
├── config/         # Cấu hình mod
├── world/          # Dữ liệu thế giới
├── run.sh          # Script khởi động (Linux/Codespace)
├── run.bat         # Script khởi động (Windows)
└── server.properties
```

---

## ⚠️ Lưu ý

> [!WARNING]
> Một số mod **chỉ dùng phía client** (như Embeddium, FancyMenu, Xaero's Map) — server tự động bỏ qua, không cần lo.

> [!TIP]
> Nếu server crash hoặc có lỗi, kiểm tra file `logs/latest.log` để xem nguyên nhân cụ thể.
