import base64
import io

from PIL import Image


def convert_image_to_base64(uploaded_file) -> str:
    """
    Convert uploaded image file to base64 string

    Args:
        uploaded_file: Streamlit uploaded file object

    Returns:
        Base64 encoded string of the image
    """
    # Open image with PIL
    pil_image = Image.open(uploaded_file)

    # Create buffer
    buffered = io.BytesIO()

    # Convert RGBA or P mode images to RGB
    if pil_image.mode in ("RGBA", "P"):
        pil_image = pil_image.convert("RGB")

    # Save to buffer as JPEG
    pil_image.save(buffered, format="JPEG")

    # Encode to base64
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    return img_base64
