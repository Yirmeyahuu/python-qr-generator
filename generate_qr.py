import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from PIL import Image

# Your link
drive_url = "https://your-link-here.com/"

# Create QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(drive_url)
qr.make(fit=True)

# Generate QR code (still black-on-white)
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    fill_color="black",
    back_color="white"
)

# Convert image to RGBA (so we can handle transparency)
img = img.convert("RGBA")

# Make white background transparent & turn black pixels white
datas = img.getdata()
new_data = []
for item in datas:
    # item = (R, G, B, A)
    if item[0] < 50 and item[1] < 50 and item[2] < 50:
        # Convert black pixels to white
        new_data.append((255, 255, 255, 255))
    elif item[0] > 200 and item[1] > 200 and item[2] > 200:
        # Make white pixels transparent
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save("public_qr.png", "PNG")

print("✅ White transparent QR code saved as 'public_qr.png'")

