import requests
import argparse
import urllib3
import time

from PIL import Image
from io import BytesIO

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download, crop, and convert an image to 1-bit raw format")
    parser.add_argument("image_url", help="URL of the image to process (you can use 'now', 'start', 'height', 'width' formater)")
    parser.add_argument("output", help="Output path without file extension to save the processed image")
    parser.add_argument("--crop-top", type=int, default=0, help="Number of pixels to crop from the top (default: 0)")
    parser.add_argument("--threshold", type=int, default=100, help="Threshold for black and white conversion (0-255)")
    parser.add_argument("--timeline", type=int, default=3600, help="Timeline formater in seconds")
    args = parser.parse_args()

    now = int(time.time()) * 1000
    start = now - (args.timeline * 1000) 
    url = args.image_url.format(now=now, start=start, height=args.crop_top+480, width=800)

    print(f"url={url}")
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))

        if args.crop_top > 0:
            width, height = image.size
            image = image.crop((0, args.crop_top, width, height))

        grayscale_image = image.convert('L')
        
        # NOTE: my display has inverted color black is 255 and white is 0
        bw_image = grayscale_image.point(lambda x: 255 if x > 128 else 0, mode='1')
        #bw_image = bw_image.convert('1')
        bw_image.save(args.output + ".png")

        # Save the raw pixel data without file header, top to bottom
        with open(args.output + ".img", 'wb') as f:
            # Calculate row size (must be a multiple of 4 bytes)
            row_size = ((bw_image.width + 31) // 32) * 4
            
            # Write pixel data row by row, top to bottom
            for y in range(bw_image.height):
                row_data = bytearray(row_size)
                for x in range(bw_image.width):
                    if bw_image.getpixel((x, y)) == 0:  # Black pixel
                        byte_index = x // 8
                        bit_index = 7 - (x % 8)
                        row_data[byte_index] |= (1 << bit_index)
                f.write(row_data)
        
        width, height = bw_image.size
        print(f"Image successfully downloaded and converted to 1-bit {width}x{height} BMP: {args.output}.(img|png)")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
