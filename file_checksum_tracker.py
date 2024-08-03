# Import necessary libraries
import os
import hashlib
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import openpyexcel

# Define a custom FileSystemEventHandler
class ChecksumHandler(FileSystemEventHandler):
    def __init__(self, checksums, excel_file, json_file):
        self.checksums = checksums
        self.excel_file = excel_file
        self.json_file = json_file
    
    # Handle file creation events
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            self.update_checksum(event.src_path)
    
    # Handle file modification events
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
            self.update_checksum(event.src_path)
    
    # Update checksum for a given file
    def update_checksum(self, file_path):
        try:
            checksum = self.get_file_hash(file_path)
            self.checksums[file_path] = checksum
            print(f"Updated checksum for {file_path}: {checksum}")
            self.save_to_excel()
            self.save_to_json()
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    # Calculate SHA256 hash for a file
    def get_file_hash(self, file_path):
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"Error calculating hash for {file_path}: {str(e)}")
            raise
    
    # Save checksums to Excel file
    def save_to_excel(self):
        try:
            df = pd.DataFrame(list(self.checksums.items()), columns=['File Path', 'Checksum'])
            df.to_excel(self.excel_file, index=False)
            print(f"Updated Excel file: {self.excel_file}")
        except Exception as e:
            print(f"Error saving to Excel: {str(e)}")
    
    # Save checksums to JSON file
    def save_to_json(self):
        try:
            with open(self.json_file, 'w') as f:
                json.dump(self.checksums, f, indent=4)
            print(f"Updated JSON file: {self.json_file}")
        except Exception as e:
            print(f"Error saving to JSON: {str(e)}")

# Main function to set up and run the file monitoring
def main():
    # Set up file paths
    downloads_folder = os.path.expanduser("~/Downloads")
    excel_file = "checksums.xlsx"
    json_file = "checksums.json"
    
    print(f"Monitoring folder: {downloads_folder}")
    print(f"Excel output file: {excel_file}")
    print(f"JSON output file: {json_file}")
    
    # Initialize checksums dictionary
    checksums = {}
    
    # Load existing checksums if JSON file exists
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r') as f:
                checksums = json.load(f)
            print(f"Loaded {len(checksums)} existing checksums from {json_file}")
        except Exception as e:
            print(f"Error loading existing checksums: {str(e)}")
    
    # Create an instance of our custom handler
    event_handler = ChecksumHandler(checksums, excel_file, json_file)
    
    # Initialize and start the observer
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=False)
    observer.start()
    
    print("File monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping file monitoring...")
        observer.stop()
    observer.join()

# Entry point of the script
if __name__ == "__main__":
    main()