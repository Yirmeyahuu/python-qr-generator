# 🎨 Transparent QR Code Generator

A sleek Python-based QR code generator that creates beautiful, white-on-transparent QR codes with rounded corners. Perfect for overlaying on dark backgrounds, presentations, or modern web designs!

## ✨ Features

- 🔲 **Rounded Corner Design** - Smooth, modern aesthetic with `RoundedModuleDrawer`
- 🎭 **Transparent Background** - White QR codes on transparent backgrounds
- 🛡️ **High Error Correction** - Uses `ERROR_CORRECT_H` for maximum resilience
- 📦 **Multiple Outputs** - Generate QR codes for different purposes with ease

## 🚀 Quick Start

### Prerequisites

```bash
pip install qrcode[pil] Pillow
```

### Usage

1. **Public QR Code** - Generate a general-purpose QR code:
   ```bash
   python generate_qr.py
   ```
   Output: `public_qr.png`

2. **Team QR Code** - Generate a team-specific QR code:
   ```bash
   python generate_qr_team.py
   ```
   Output: `team-qr.png`

3. **Registration QR Code** - Generate a registration-specific QR code:
   ```bash
   python generate_qr_register.py
   ```
   Output: `sentinels-register-qr.png`

## 🎨 How It Works

The generator follows a unique three-step process:

1. **Generate** - Creates a standard black-on-white QR code with rounded corners
2. **Invert** - Converts black pixels to white
3. **Transparency** - Makes the white background transparent

This results in a professional, modern QR code that looks stunning on any dark surface!

## 📝 Customization

Edit the `drive_url` variable in any script to change the target URL:

```python
drive_url = "https://your-link-here.com/"
```

### Advanced Options

You can customize the QR code appearance by modifying these parameters in the scripts:

- `version` - Controls the size (1-40, auto-fits by default)
- `error_correction` - Options: `ERROR_CORRECT_L`, `M`, `Q`, `H`
- `box_size` - Pixel size of each QR code box (default: 10)
- `border` - Width of the border in boxes (default: 4)

## 📸 Output Examples

All generated QR codes feature:
- ✅ White pixels on transparent background
- ✅ Rounded corners for modern aesthetic
- ✅ High error correction for reliability
- ✅ PNG format with alpha channel

## 🛠️ Technical Details

- **Library**: `qrcode` with PIL/Pillow support
- **Image Format**: PNG with RGBA color space
- **Style**: `RoundedModuleDrawer` for smooth edges
- **Error Correction**: Level H (30% of data can be restored)

## 💡 Use Cases

Perfect for:
- 📱 Mobile app registration
- 👥 Team collaboration links
- 🎫 Event check-ins
- 📄 Document sharing
- 🌐 Website URLs on dark-themed materials

## 📄 License

Free to use and modify for your projects!
