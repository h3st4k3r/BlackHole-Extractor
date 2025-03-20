# Author h3st4k3r 2025 ©
# To all of you

import subprocess
import os
import argparse

def extract_embedded_files(file_path, output_dir, verbose=False):
    if not os.path.isfile(file_path):
        print("[ERROR] The specified file does not exist.")
        return

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract files using binwalk with advanced options
    command = [
        'binwalk', '--extract', '--dd=.*', '--matryoshka', '--run-as=root', '-C', output_dir, file_path
    ]

    if verbose:
        print("[INFO] Running command:", ' '.join(command))
    
    subprocess.run(command)
    print(f"[INFO] Extraction completed. Check the directory '{output_dir}' for extracted files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BlackHole Extractor - Uncover hidden embedded files in binaries.")
    parser.add_argument("file_path", help="Full path to the file to analyze.")
    parser.add_argument("output_dir", help="Directory to save extracted files.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()
    extract_embedded_files(args.file_path, args.output_dir, args.verbose)
