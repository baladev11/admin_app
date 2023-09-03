import streamlit as st
from pdf2image import convert_from_path
import io

# Main page heading
st.title("Profiling Report for Trained Image Data")

pdf_path = "Report.pdf"

# Convert the PDF to images
images = convert_from_path(pdf_path)
# Display each page as an image
for page_num, image in enumerate(images, 1):
        st.image(image, use_column_width=True, caption=f"Page {page_num}")