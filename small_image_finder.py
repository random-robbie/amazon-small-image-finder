from amazon_photos import AmazonPhotos
import os
import time
from datetime import datetime
import argparse
from PIL import Image

def process_photos(download_dir, cookies, trash=False):
   os.makedirs(download_dir, exist_ok=True)
   os.chdir(download_dir)
   
   ap = AmazonPhotos(cookies=cookies)
   photos = ap.photos()
   
   log_file = f"downloaded_photos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
   
   with open(log_file, 'w') as f:
       for _, photo in photos.iterrows():
           original_name = photo.get('originalFileName', photo['name'])
           id_name = photo['id']
           
           if any(original_name.startswith(prefix) for prefix in ['PXL_', 'IMG-']):
               continue
               
           width = float(photo['image.width'])
           height = float(photo['image.height'])
           max_dimension = max(width, height)
           has_device = bool(photo.get('model'))
           
           print(f"\nChecking {original_name}:")
           print(f"Dimensions: {width}x{height}, Max: {max_dimension}")
           print(f"Has device: {has_device}")
           
           if max_dimension < 1400 and not has_device:
               print(f"Processing: {original_name}")
               ap.download([id_name])
               if trash:
                  print(f"Trashing and removing: {original_name}")
                  ap.trash([id_name])
               time.sleep(2)
               f.write(f"{original_name}, {width}x{height}, ID: {id_name}\n")

                   
if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Download small images from Amazon Photos')
   parser.add_argument('--trash', action='store_true', help='Move downloaded photos to trash')
   args = parser.parse_args()

   cookies = {
       'session-id': '',
       'ubid-acbuk': '',
       'at-acbuk': ''
   }

   process_photos("small_photos_no_device", cookies, args.trash)
