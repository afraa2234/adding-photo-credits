# Adding Photo Credits

Python script that bulk renames files by appending photographer credit information to filenames.

## How to Run the Solution

1. Open `renameFileWithCredits.py` in your text editor
2. Update the `folder_path` variable with your target folder path:
```python
folder_path = r"C:\path\to\your\folder"
```
3. Update the `append_text` variable with your desired credit text:
```python
append_text = " by Photographer Name"
```
4. Run the script:
```bash
python renameFileWithCredits.py
```

## What It Does

The script loops through all files in the specified folder and appends credit text to each filename before the file extension.

**Example:**
- Original: `image1.jpg`
- Renamed: `image1 by Craig Bailey-Perspective Photo-cbzperspective on IG.jpg`

**Important:** The script skips folders and only renames files. Make sure to test on a backup folder first to verify the renaming works as expected.

## Customization

You can modify the `append_text` variable to add any photographer credit, copyright notice, or metadata you need to include in your filenames. The text will be inserted between the original filename and the file extension.

## Use Case

Built for quickly adding photographer credits to batch image files for cultural preservation projects and event documentation.
