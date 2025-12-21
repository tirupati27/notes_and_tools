import sys
from docx import Document
from docx.shared import Inches
from docx.oxml import parse_xml
from docx.oxml.ns import qn

def create_docx_with_image(image_path, output_file="output.docx"):
    # Default PowerPoint slide size in inches
    ppt_width_in = 13.33
    ppt_height_in = 7.5

    # Create new document
    doc = Document()

    # Set custom page size to match PowerPoint slide
    section = doc.sections[0]
    section.page_width = Inches(ppt_width_in)
    section.page_height = Inches(ppt_height_in)

    # Remove all margins
    section.top_margin = Inches(0)
    section.bottom_margin = Inches(0)
    section.left_margin = Inches(0)
    section.right_margin = Inches(0)

    # Add image as full-page fit
    doc.add_picture(image_path, width=Inches(ppt_width_in), height=Inches(ppt_height_in))

    # Save file
    doc.save(output_file)
    print(f"✅ Created DOCX file: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python ppt_layout_docx.py <image_path> [output_file]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.docx"
    create_docx_with_image(image_path, output_file)
