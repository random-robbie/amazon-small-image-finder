# Amazon Photos Small Image Finder

Identifies and downloads low-resolution photos from Amazon Photos that lack device metadata - typically memes and social media images.

WIP: Remove the crap!

## Features

- Detects images under 1000px without device metadata
- Downloads identified images locally for review
- Generates timestamped log file of found images
- Skips Google Pixel photos automatically
- Respects API rate limits
- No automatic deletion - review before removing

## Requirements

```bash
pip install amazon-photos pillow
```

## Configuration

1. Get required cookies from Amazon Photos UK:
   - session-id
   - ubid-acbuk  
   - at-acbuk

2. Add cookies to script:

```python
cookies = {
    'session-id': '',    # Your session ID
    'ubid-acbuk': '',    # Your UBID 
    'at-acbuk': ''      # Your AT token
}
```

## Usage

```bash
python small_image_finder.py
```

Files are downloaded to `small_photos_no_device/` directory.

A log file `photos_to_review_[timestamp].txt` is created containing:
- Filename
- Image dimensions
- Amazon Photos ID

## Sample Output

Terminal:
```
Downloading: photo.jpg
Size: 800x600
```

Log file:
```
photo.jpg, 800x600, ID: AbC123XyZ
meme.png, 500x500, ID: DeF456UvW
```

## Warning

Always review downloaded images before deletion from Amazon Photos.

## License

MIT

## Security Note

Keep your Amazon Photos cookies secure and never share them.
