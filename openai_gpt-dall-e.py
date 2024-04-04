from openai import OpenAI
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

client = OpenAI()

# For image generation
response = client.images.generate(
    model="dall-e-3",
    prompt="A cute puppy wearing a tuxedo",
    n=1,
    size="1024x1024"
)

# Extract the image URL from the response output
image_url = response.data[0].url

print(image_url)
