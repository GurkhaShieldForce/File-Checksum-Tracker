 # File Checksum Tracker

## Description
File Checksum Tracker is a Python script that monitors your Downloads folder for new or modified files, calculates their SHA256 checksums, and stores this information in both Excel and JSON formats. This tool is useful for maintaining file integrity and tracking changes in your Downloads folder.

## Features
- Real-time monitoring of the Downloads folder
- Automatic calculation of SHA256 checksums for new and modified files
- Storage of checksums in both Excel (.xlsx) and JSON formats
- Error handling and informative console output

## Requirements
- Python 3.6+
- Dependencies listed in `requirements.txt`

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/GurkhaShieldForce/File-Checksum-Tracker
   cd file-checksum-tracker
   ```

2. Install the required packages using the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

   Note: If you encounter issues with `openpyexcel`, you may need to manually install `openpyxl` instead:
   ```
   pip install openpyxl
   ```
   If using `openpyxl`, make sure to update the import statement in the script from `import openpyexcel` to `import openpyxl`.

## Usage
Run the script using Python:

```
python file_checksum_tracker.py
```

The script will start monitoring your Downloads folder. It will print information about new or modified files and update the Excel and JSON files with the latest checksums.

To stop the script, press Ctrl+C.

## Output Files
- `checksums.xlsx`: An Excel file containing the file paths and their corresponding SHA256 checksums.
- `checksums.json`: A JSON file containing the same information as the Excel file.

Both files are updated in real-time as files are added or modified in the Downloads folder.

## Contributing
Contributions to the File Checksum Tracker are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the creators and maintainers of the watchdog, pandas, and openpyexcel libraries.
- Special thanks to the open-source community for their continuous support and inspiration.

## Disclaimer
This script uses a library named `openpyexcel`, which is non-standard. If you encounter any issues, consider using the standard `openpyxl` library instead and updating the import statement in the script.

## Troubleshooting
If you encounter any issues during installation or execution:
1. Ensure you have Python 3.6+ installed.
2. Make sure you've installed all dependencies from `requirements.txt`.
3. If you have problems with `openpyexcel`, try using `openpyxl` as mentioned in the installation instructions.
4. Check your Python path and environment variables if you're having trouble running the script.

For any other issues, please open an issue on the GitHub repository.
