import cv2
import base64
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def capture_image():
    """ 
    Captures one frame from the default webcam, resize it, 
    encodes it as Base64JPEG and returns it.
    """
    for idx in range(4):
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            for _ in range(10):  # For Warm up
                cap.read()
            ret, frame = cap.read()
            cap.read()
            if not ret:
                continue 
            cv2.imwrite("sample.jpg", frame)
            ret, buf = cv2.imencode(".jpg", frame)
            if ret:
                return base64.b64encode(buf).decode("utf-8")
    raise RuntimeError("Could not open any webcam")


def analyze_image_with_query(query):
    """
    Expects a string with 'query'.
    Captures the image and sends the query and the image to Groq's
    vision chat API and return the analysis.
    """
    img_b64 = capture_image()
    model = "meta-llama/llama-4-scout-17b-16e-instruct"

    if not query or not img_b64:
        return "Error: Both 'query' and 'image' fields required."
    
    client  = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_b64}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

#query = "how many people do you see?"
#print(analyze_image_with_query(query))
            

