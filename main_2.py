import qrcode

text = input("Enter your Text (leave blank if using URL): ").strip()
url = input("Enter your URL (leave blank if using Text): ").strip()
filename = input("Enter your Filename: ").strip()
if not(filename.endswith(".png")):
    filename = filename + ".png"

if url:
    data = url
elif text:
    data = text
else:
    print("Error: Please enter either a URL or some text.")
    exit()

img = qrcode.make(data)
img.save(filename)

print("QR Code generated successfully!")