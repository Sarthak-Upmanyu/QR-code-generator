import qrcode
import os

text = input("Enter your Text (leave blank if using URL): ").strip()
url = input("Enter your URL (leave blank if using Text): ").strip()
filename = input("Enter your Filename: ").strip()

# Add .png if no valid extension is provided
name, ext = os.path.splitext(filename)

if ext.lower() not in [".png", ".jpg", ".jpeg"]:
    filename += ".png"

# Check input
if url and text:
    print("Error: Please enter either a URL or text, not both.")
    exit()

if url:
    data = url
elif text:
    data = text
else:
    print("Error: Please enter either a URL or some text.")
    exit()

# Generate QR code
img = qrcode.make(data)

# Save image
img.save(filename)

print(f"QR Code generated successfully as '{filename}'!")
