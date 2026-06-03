import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
from streamlit_drawable_canvas import st_canvas

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Digit Recognizer AI", layout="wide")

st.title("✍️ Handwritten Digit Recognition System")
st.markdown("Draw a digit OR upload an image and let AI predict it!")

# ----------------------------
# LOAD MODEL
# ----------------------------
model = tf.keras.models.load_model("digit_model.keras")

# ----------------------------
# SIDEBAR OPTIONS
# ----------------------------
st.sidebar.header("⚙️ Options")
mode = st.sidebar.radio("Choose Input Method:", ["Draw Digit", "Upload Image"])

# ----------------------------
# PREPROCESS FUNCTION
# ----------------------------
def preprocess(img):
    img = cv2.resize(img, (28, 28))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

# ----------------------------
# PREDICTION FUNCTION
# ----------------------------
def predict(img):
    prediction = model.predict(img)
    label = np.argmax(prediction)
    confidence = np.max(prediction)
    return label, confidence, prediction[0]

# ----------------------------
# DRAWING CANVAS MODE
# ----------------------------
if mode == "Draw Digit":

    st.subheader("🎨 Draw a Digit Below")

    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=10,
        stroke_color="white",
        background_color="black",
        height=250,
        width=250,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("Predict Digit"):

        if canvas_result.image_data is not None:

            img = canvas_result.image_data.astype(np.uint8)

            # Convert RGBA → RGB
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

            processed = preprocess(img)

            label, confidence, probs = predict(processed)

            st.success(f"🎯 Predicted Digit: {label}")
            st.info(f"📊 Confidence: {confidence*100:.2f}%")

            # Probability Chart
            fig, ax = plt.subplots()
            ax.bar(range(10), probs)
            ax.set_title("Prediction Probabilities")
            ax.set_xlabel("Digit")
            ax.set_ylabel("Probability")
            st.pyplot(fig)

# ----------------------------
# UPLOAD IMAGE MODE
# ----------------------------
elif mode == "Upload Image":

    st.subheader("📤 Upload a Digit Image")

    uploaded_file = st.file_uploader("Upload PNG/JPG image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img = np.array(image)

        processed = preprocess(img)

        label, confidence, probs = predict(processed)

        st.success(f"🎯 Predicted Digit: {label}")
        st.info(f"📊 Confidence: {confidence*100:.2f}%")

        # Probability Chart
        fig, ax = plt.subplots()
        ax.bar(range(10), probs)
        ax.set_title("Prediction Probabilities")
        ax.set_xlabel("Digit")
        ax.set_ylabel("Probability")
        st.pyplot(fig)

# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")
st.markdown("✨ Built with Streamlit + CNN + MNIST Dataset")