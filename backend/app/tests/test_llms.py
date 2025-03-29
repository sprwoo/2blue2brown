from app.controllers import Chunky
from dotenv import load_dotenv
import os

load_dotenv()

def test_chunky_basic():
    chunky = Chunky()
    prompt = "Explain who chunky kong is from the donkey kong series."
    response = chunky.basic_response(prompt)
    print("Response:", response)
    
def test_chunky_with_image():
    chunky = Chunky()
    prompt="Can you explain what is contents of this image?"
    image_path = "ass(ets)/1.jpg"
    response = chunky.basic_image_handling_stored_image(prompt, image_path)
    print("Image+Test Response:\n", response)

if __name__ == "__main__":
    test_chunky_basic()
    test_chunky_with_image()
