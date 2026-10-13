from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

# PalayCheck AI: Paddy Leaf Disease Classification
st.set_page_config(
    page_title="PalayCheck AI",
    page_icon="🌾",
    layout="centered"
)

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = (
    PROJECT_DIR
    / "model_outputs"
    / "palaycheck_mobilenetv2_best.keras"
)

# Must match the class order used during model training.
CLASS_NAMES = [
    "bacterial_leaf_blight",
    "bacterial_leaf_streak",
    "bacterial_panicle_blight",
    "blast",
    "brown_spot",
    "dead_heart",
    "downy_mildew",
    "hispa",
    "normal",
    "tungro",
]


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}"
        )

    return tf.keras.models.load_model(MODEL_PATH)


st.title("🌾 PalayCheck AI")
st.subheader("AI-Assisted Paddy Leaf Disease Classification")

st.write(
    "Upload a rice or paddy leaf image to receive "
    "an AI-generated classification prediction."
)

st.info(
    "For experimental and educational use. "
    "Predictions are not confirmed disease diagnoses."
)

try:
    model = load_model()

    if model.output_shape[-1] != len(CLASS_NAMES):
        st.error(
            "The number of model outputs does not match "
            "the configured class names."
        )
        st.stop()

except Exception as error:
    st.error(f"Could not load the trained model: {error}")
    st.stop()

uploaded_file = st.file_uploader(
    "Choose a paddy leaf image",
    type=["jpg", "jpeg", "png", "bmp"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded paddy leaf image",
            use_container_width=True
        )

        if st.button("Classify Leaf Image", type="primary"):
            with st.spinner("Analyzing image..."):
                # Match the TensorFlow resizing and preprocessing
                # used by the notebook's training pipeline.
                image_array = np.asarray(image)

                resized_image = tf.image.resize(
                    image_array,
                    (224, 224)
                ).numpy()

                preprocessed_image = (
                    tf.keras.applications.mobilenet_v2
                    .preprocess_input(resized_image)
                )

                image_batch = np.expand_dims(
                    preprocessed_image,
                    axis=0
                )

                scores = model.predict(
                    image_batch,
                    verbose=0
                )[0]

                predicted_index = int(np.argmax(scores))
                predicted_class = CLASS_NAMES[predicted_index]
                confidence = float(scores[predicted_index]) * 100

            st.success("Prediction completed")

            st.metric(
                "Predicted class",
                predicted_class.replace("_", " ").title()
            )

            st.metric(
                "Model confidence score",
                f"{confidence:.2f}%"
            )

            st.caption(
                "The score reflects the model's output and "
                "does not guarantee that the prediction is correct."
            )

            with st.expander("View top 3 predictions"):
                top_indices = np.argsort(scores)[::-1][:3]

                for index in top_indices:
                    st.write(
                        f"**{CLASS_NAMES[index].replace('_', ' ').title()}**"
                        f" — {scores[index] * 100:.2f}%"
                    )

    except Exception as error:
        st.error(f"Could not process the uploaded image: {error}")