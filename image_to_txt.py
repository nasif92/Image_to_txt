import os
import easyocr

print("Starting program")
# Initialize the reader once (English only, can add more languages like ['en','ch_sim'])
reader = easyocr.Reader(['en'])

# Input folder (current directory) and output folder
input_folder = "."
output_folder = "txt"
os.makedirs(output_folder, exist_ok=True)

print("Going over all images")
# Loop through image files
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff")):
        img_path = os.path.join(input_folder, filename)
        
        try:
            # Run OCR
            results = reader.readtext(img_path, detail=0)  # detail=0 returns only text
            
            # Join all detected text lines
            text = "\n".join(results)
            
            # Save as .txt file
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(output_folder, txt_filename)
            
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)
            
            print(f"Processed {filename} → {txt_filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Done")