from amazon_photos import AmazonPhotos
import os
import time
from datetime import datetime

def process_photos(download_dir, cookies):
   os.makedirs(download_dir, exist_ok=True)
   os.chdir(download_dir)
   
   ap = AmazonPhotos(cookies=cookies)
   photos = ap.photos()
   
   log_file = f"photos_to_review_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
   
   with open(log_file, 'w') as f:
       for _, photo in photos.iterrows():
           if photo['name'].startswith('PXL_'):
               continue
               
           width = photo.get('width', 0)
           height = photo.get('height', 0)
           max_dimension = max(width, height)
           has_device = bool(photo.get('model'))
           
           if max_dimension < 1000 and not has_device:
               print(f"\nDownloading: {photo['name']}")
               print(f"Size: {width}x{height}")
               
               ap.download([photo['id']])
               time.sleep(2)
               
               f.write(f"{photo['name']}, {width}x{height}, ID: {photo['id']}\n")

if __name__ == "__main__":
   cookies = {
       'session-id': '',
       'ubid-acbuk': '',
       'at-acbuk': ''
   }
   process_photos("small_photos_no_device")
