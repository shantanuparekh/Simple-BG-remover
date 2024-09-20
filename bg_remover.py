from rembg import remove
from PIL import Image
from tkinter import Tk, filedialog
import os

def main():
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    print("All modules imported successfully!")

    # Open file dialog for selecting the input image
    input_img = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    # Check if the user selected a file
    if not input_img:
        print("No file selected. Exiting.")
        input("Press Enter to exit...")
        return

    print("Image selected. Starting background removal...")

    # Load the image and remove the background
    inp = Image.open(input_img)
    output = remove(inp)

    print("Background removed!")

    # Ask user to select the folder to save the output file
    output_folder = filedialog.askdirectory(title="Select Folder to Save Output")

    # Check if the user selected a folder
    if not output_folder:
        print("No folder selected. Exiting.")
        input("Press Enter to exit...")
        return

    # Generate the output file name with '_rmbg' suffix
    output_filename = os.path.basename(input_img).replace(".jpg", "_rmbg.png").replace(".jpeg", "_rmbg.png").replace(".png", "_rmbg.png")
    output_path = os.path.join(output_folder, output_filename)

    # Save the output image
    output.save(output_path)
    print(f"Background removed image saved to: {output_path}")

    # Keep the terminal open until the user presses Enter
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
