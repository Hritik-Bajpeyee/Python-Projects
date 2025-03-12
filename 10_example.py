import os
import shutil
import logging

# Configure logging (optional improvement)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'audio': ['.mp3', '.wav', '.aac', '.ogg'],
    'archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'scripts': ['.py', '.js', '.sh', '.bat', '.rb']
}

def get_unique_path(dest_dir: str, filename: str) -> str:
    """Generate a unique path to avoid overwriting existing files."""
    base, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_name = f"{base} ({counter}){ext}" if counter > 1 else filename
        new_path = os.path.join(dest_dir, new_name)
        if not os.path.exists(new_path):
            return new_path
        counter += 1

def organize_files(folder: str) -> None:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            # Try to match file extension with defined categories
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_dir = os.path.join(folder, category)
                    # Ensure the destination is a directory
                    if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
                        logging.warning(f"Skipping {category} (not a directory) for {filename}")
                        continue
                    try:
                        os.makedirs(dest_dir, exist_ok=True)
                    except Exception as e:
                        logging.error(f"Error creating {dest_dir}: {e}")
                        continue
                    dest_path = get_unique_path(dest_dir, filename)
                    try:
                        shutil.move(file_path, dest_path)
                        moved = True
                        break  # Exit loop once file is moved
                    except Exception as e:
                        logging.error(f"Error moving {filename}: {e}")
            
            # If file extension doesn't match any category, move to 'others'
            if not moved:
                dest_dir = os.path.join(folder, 'others')
                if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
                    logging.warning(f"Cannot move to 'others' (not a directory) for {filename}")
                    continue
                try:
                    os.makedirs(dest_dir, exist_ok=True)
                except Exception as e:
                    logging.error(f"Error creating 'others' directory: {e}")
                    continue
                dest_path = get_unique_path(dest_dir, filename)
                try:
                    shutil.move(file_path, dest_path)
                except Exception as e:
                    logging.error(f"Error moving {filename} to 'others': {e}")

if __name__ == '__main__':
    folder_path = input("Enter the folder path to organize: ").strip()
    if not os.path.isdir(folder_path):
        logging.error("Error: Invalid directory path.")
    else:
        organize_files(folder_path)
        logging.info("Files organized successfully!")
