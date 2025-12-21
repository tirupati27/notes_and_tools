import cv2
import os
import sys

def convert_folder_to_bw(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(".png"):
            continue

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        img = cv2.imread(input_path)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # OTSU automatically finds the best threshold
        _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Ensure white background + black text
        # If image is "dark", invert it
        white_ratio = cv2.countNonZero(bw) / bw.size
        if white_ratio < 0.5:     # too much black → wrong → invert
            bw = 255 - bw

        cv2.imwrite(output_path, bw)
        print("Converted:", filename)

    print("Done!")

convert_folder_to_bw(sys.argv[1], sys.argv[2])