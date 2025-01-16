import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key
from openai import OpenAI
#client = OpenAI(api_key=openai_api_key)


genai.configure(api_key = google_gemini_api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

st.set_page_config(
    page_title="BlogWok: An AI Blog Companion",
    page_icon="✍️",
    layout="wide"
)
st.title("BlogWok: An AI Blog Companion")

st.subheader("Now you can create exciting blog posts with the help of BlogWok! Just enter your text and let BlogWok do the rest!")
blog = ""
# sidebar
with st.sidebar:
  st.title("Input Your Blog Details")

  st.subheader("Enter your blog details below to generate:")

  blog_title = st.text_input("Blog Title")

  keywords = st.text_input("Keywords(comma separated)")

  num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=250)

  num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

  promt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\"  Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original and informative, and maintain a consistent tone throughout with important pointers.",
      ]




  submit_button = st.button("Generate Blog")

if submit_button:
  #st.image("")
  response = model.generate_content(promt_parts)

  #images = []

  #for i in range(num_images):
   #  image_response = client.images.generate(
    #  model="dall-e-3",
      #prompt=f"Genrate a Blog Port Image on the title: {blog_title}",
      #size="1024x1024",
      #quality="standard",
      #n=1,
     # )
     #images.append(image_response.data[0].url)"""


  #for i in range(num_images):
   # st.write(images[i])

  st.title("Your Blog Post:")
  st.write(response.text)