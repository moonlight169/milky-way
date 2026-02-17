import qrcode

# ลิงก์ที่ได้จาก IP ของเครื่องเรา (Wireless LAN adapter Wi-Fi)
# อ้างอิงจากเลข IP: 192.168.1.39 ของน้อง
data = "https://milky-way-yvev.onrender.com"

# ปรับแต่งค่า QR Code ให้ดู Pro
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# สร้างภาพ (เลือกสีให้เข้ากับธีม Milky-Way: Navy Blue & White)
img = qr.make_image(fill_color="#0f172a", back_color="white")

# เซฟไฟล์
img.save("milkyway_qr.png")

print(f"✅ สร้าง QR Code สำเร็จ! ลิงก์ไปที่: {data}")
print("ไฟล์ภาพถูกบันทึกในชื่อ: milkyway_qr.png")