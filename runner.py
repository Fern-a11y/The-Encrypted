import base64
import sys

def run_enc_file(filename):
    try:
        # 1. Open the .enc file
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 2. Verify if it matches your custom file format header
        if not content.startswith("CUSTOM_ENC_V1::"):
            print("Error: This is not a valid or supported .enc file!")
            return
            
        # 3. Strip the header and decode the hidden code back to normal
        encoded_data = content.replace("CUSTOM_ENC_V1::", "")
        decoded_bytes = base64.b64decode(encoded_data.encode("utf-8"))
        original_code = decoded_bytes.decode("utf-8")
        
        print(f"--- [STARTING EXECUTION OF: {filename}] ---")
        
        # 4. Execute the code directly in Python on the fly
        exec(original_code)
        
        print(f"--- [EXECUTION FINISHED] ---")
        
    except Exception as e:
        print(f"An error occurred while running the file: {e}")

if __name__ == "__main__":
    # Ask the user for the file path or name
    file_path = input("Drag your .enc file here or type the filename (e.g., script.enc): ").strip('"')
    run_enc_file(file_path)
