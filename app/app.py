import streamlit as st
from disease_info import get_disease_info
from crop_info import get_crop_info
from history import (
    initialize_database,
    save_prediction,
    get_prediction_history,
    clear_prediction_history
)
import tensorflow as tf
import numpy as np
import json
from PIL import Image


# ============================================================
# AYUBA CROP DOCTOR
# Main Application
# ============================================================

st.set_page_config(
    page_title="Ayuba Crop Doctor",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# INITIALIZE DATABASE
# ============================================================

initialize_database()


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_PATH = "model/toga_crop_doctor_cnn_final.h5"
CLASS_NAMES_PATH = "model/class_names.json"


@st.cache_resource
def load_cnn_model():
    return tf.keras.models.load_model(MODEL_PATH)


@st.cache_data
def load_class_names():

    with open(
        CLASS_NAMES_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


model = load_cnn_model()
class_names = load_class_names()


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_disease(image):

    image = image.convert("RGB")

    image = image.resize(
        (224, 224)
    )

    image_array = np.array(
        image
    )

    image_array = (
        image_array.astype("float32")
        / 255.0
    )

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    predictions = model.predict(
        image_array,
        verbose=0
    )

    predicted_index = int(
        np.argmax(
            predictions[0]
        )
    )

    confidence = float(
        predictions[0][predicted_index]
    )

    predicted_class = class_names[
        predicted_index
    ]

    top_indices = np.argsort(
        predictions[0]
    )[-3:][::-1]

    top_predictions = []

    for index in top_indices:

        top_predictions.append(
            {
                "class": class_names[index],
                "confidence": float(
                    predictions[0][index]
                )
            }
        )

    return (
        predicted_class,
        confidence,
        top_predictions
    )


# ============================================================
# FORMAT PREDICTION
# ============================================================

def format_prediction(predicted_class):

    parts = predicted_class.split("_")

    crop = parts[0]

    if len(parts) > 1 and parts[1] == "Healthy":

        disease = "Healthy"

    else:

        disease = " ".join(
            parts[1:]
        )

    return crop, disease


# ============================================================
# CONFIDENCE LEVEL
# ============================================================

def get_confidence_level(confidence):

    if confidence >= 0.80:

        return "High Confidence"

    elif confidence >= 0.60:

        return "Moderate Confidence"

    else:

        return "Low Confidence"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN APP
       ======================================================== */

    .main {
        background-color: #f7f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       MAIN TITLE
       ======================================================== */

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #0b4f6c;
        margin-bottom: 5px;
        letter-spacing: 0.5px;
    }

    .subtitle {
        font-size: 20px;
        color: #52727d;
        margin-bottom: 25px;
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #0b4f6c;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    .section-heading {
        color: #0b4f6c;
        font-weight: 700;
        font-size: 20px;
        margin-bottom: 8px;
    }


    /* ========================================================
       INFORMATION BOXES
       ======================================================== */

    .info-box {
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #d9e5ea;
        background-color: #ffffff;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(11, 79, 108, 0.06);
    }

    .info-box h2 {
        color: #0b4f6c;
    }

    .info-box h3 {
        color: #087f5b;
    }


    /* ========================================================
       RESULT BOX
       ======================================================== */

    .result-box {
        padding: 25px;
        border-radius: 14px;
        border: 1px solid #b8d8e3;
        background-color: #eef8fb;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 3px 10px rgba(11, 79, 108, 0.08);
    }


    /* ========================================================
       RESULT METRICS
       ======================================================== */

    .result-metric {
        background-color: #f0f7fa;
        border: 1px solid #d7e8ed;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        margin-bottom: 10px;
    }

    .result-metric-title {
        font-size: 13px;
        color: #5f6b72;
        margin-bottom: 6px;
    }

    .result-metric-value {
        font-size: 20px;
        font-weight: 700;
        color: #0b4f6c;
    }


    /* ========================================================
       CONFIDENCE BOX
       ======================================================== */

    .confidence-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #b7dfd0;
        background-color: #effaf5;
        color: #087f5b;
        margin-top: 15px;
        margin-bottom: 15px;
    }


    /* ========================================================
       TOP PREDICTIONS
       ======================================================== */

    .top-prediction-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #d9e5ea;
        background-color: #ffffff;
        margin-bottom: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }


    /* ========================================================
       ANALYSIS GUIDE
       ======================================================== */

    .analysis-guide {
        background-color: #eef7f8;
        border-left: 5px solid #087f5b;
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        margin-bottom: 20px;
    }


    /* ========================================================
       HISTORY
       ======================================================== */

    .history-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #d9e5ea;
        background-color: #ffffff;
        margin-bottom: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background-color: #eef7f8;
        border-right: 1px solid #d4e5e8;
    }

    [data-testid="stSidebar"] h1 {
        color: #0b4f6c;
        font-weight: 800;
    }

    [data-testid="stSidebar"] p {
        color: #52727d;
    }


    /* ========================================================
       SIDEBAR NAVIGATION
       ======================================================== */

    [data-testid="stSidebar"] div[role="radiogroup"] label {
        padding: 10px 12px;
        border-radius: 10px;
        margin-bottom: 5px;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: #d9eef2;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #0b4f6c;
        color: #ffffff;
        font-weight: 700;
        box-shadow: 0 3px 8px rgba(11, 79, 108, 0.20);
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {
        color: #ffffff !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #0b4f6c;
        background-color: #0b4f6c;
        color: #ffffff;
        font-weight: 600;
        padding: 8px 20px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #087f5b;
        border-color: #087f5b;
        color: #ffffff;
        transform: translateY(-1px);
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    [data-testid="stFileUploader"] {
        background-color: #ffffff;
        border: 1px solid #cfe0e5;
        border-radius: 12px;
        padding: 8px;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    [data-testid="stAlert"] {
        border-radius: 10px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;
        color: #52727d;
        font-size: 14px;
        padding-top: 30px;
        padding-bottom: 10px;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {
        border-color: #d9e5ea;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("AYUBA")

    st.caption("Crop Doctor")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Disease Detection",
            "Prediction History",
            "Crop Information",
            "About"
        ]
    )

    st.divider()

    st.caption(
        "AI-powered vegetable crop disease detection system."
    )


# ============================================================
# HOME
# ============================================================

if page == "Home":

    st.markdown(
        '<div class="main-title">'
        'AYUBA CROP DOCTOR'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-Based Vegetable Crop Disease Detection System'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div class="info-box">

        <h2>Welcome to AYUBA CROP DOCTOR</h2>

        <p>
        AYUBA CROP DOCTOR is an artificial intelligence-based
        system designed to assist in identifying selected
        vegetable crop diseases from leaf images.
        </p>

        <p>
        The system uses a trained
        <strong>Convolutional Neural Network (CNN)</strong>
        to analyze crop leaf images and generate a preliminary
        disease prediction.
        </p>

        <p>
        It is designed for learning, research, agricultural
        technology demonstration and preliminary decision support.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        'System Overview'
        '</div>',
        unsafe_allow_html=True
    )

    overview1, overview2, overview3 = st.columns(3)

    with overview1:

        st.markdown(
            """
            <div class="info-box">
            <h3>AI-Powered</h3>
            <p>
            Uses deep learning and image classification
            to analyze crop leaf images.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with overview2:

        st.markdown(
            """
            <div class="info-box">
            <h3>3 Crop Types</h3>
            <p>
            Supports selected disease categories for
            Tomato, Pepper and Potato.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with overview3:

        st.markdown(
            """
            <div class="info-box">
            <h3>Decision Support</h3>
            <p>
            Provides disease information, symptoms,
            management and prevention guidance.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">'
        'Supported Crops'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="info-box">
            <h3>Tomato</h3>
            <p>
            Detection of selected tomato diseases
            supported by the trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="info-box">
            <h3>Pepper</h3>
            <p>
            Detection of selected pepper diseases
            supported by the trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="info-box">
            <h3>Potato</h3>
            <p>
            Detection of selected potato diseases
            supported by the trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">'
        'How It Works'
        '</div>',
        unsafe_allow_html=True
    )

    step1, step2, step3 = st.columns(3)

    with step1:

        st.markdown(
            """
            <div class="info-box">
            <h3>1. Upload</h3>
            <p>
            Upload a clear and well-focused image
            of the crop leaf.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with step2:

        st.markdown(
            """
            <div class="info-box">
            <h3>2. Analyze</h3>
            <p>
            The trained CNN model processes and
            analyzes the uploaded image.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with step3:

        st.markdown(
            """
            <div class="info-box">
            <h3>3. Result</h3>
            <p>
            The system displays the predicted disease,
            confidence level and relevant information.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown(
        '<div class="section-title">'
        'Important Notice'
        '</div>',
        unsafe_allow_html=True
    )

    st.warning(
        """
        AYUBA CROP DOCTOR provides preliminary AI-based
        predictions and should not be considered a replacement
        for professional agricultural diagnosis.

        For important crop health decisions, users should verify
        the result with a qualified agricultural professional,
        agronomist or plant pathologist.
        """
    )

    st.markdown(
        '<div class="section-title">'
        'Ready to Analyze a Crop Leaf?'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        <p>
        Go to <strong>Disease Detection</strong> from the
        sidebar to upload a crop leaf image and obtain an
        AI-based preliminary prediction.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DISEASE DETECTION
# ============================================================

elif page == "Disease Detection":

    st.markdown(
        '<div class="main-title">'
        'Disease Detection'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Upload a crop leaf image for AI-powered analysis.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    upload_col, guide_col = st.columns([1.4, 1])

    with upload_col:

        st.markdown(
            '<div class="section-heading">'
            '📷 Upload Leaf Image'
            '</div>',
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
            "Choose a leaf image",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

        if uploaded_file is not None:

            image = Image.open(
                uploaded_file
            )

            st.image(
                image,
                caption="Selected leaf image"
            )

            st.success(
                "Image uploaded successfully."
            )

            if st.button(
                "🔍 Analyze Image"
            ):

                with st.spinner(
                    "Analyzing image with CNN model..."
                ):

                    (
                        predicted_class,
                        confidence,
                        top_predictions
                    ) = predict_disease(
                        image
                    )

                    crop, disease = (
                        format_prediction(
                            predicted_class
                        )
                    )

                    confidence_level = (
                        get_confidence_level(
                            confidence
                        )
                    )

                save_prediction(
                    crop,
                    disease,
                    confidence
                )

                st.divider()

                st.markdown(
                    '<div class="section-heading">'
                    '🎯 Prediction Result'
                    '</div>',
                    unsafe_allow_html=True
                )

                result_col1, result_col2, result_col3 = (
                    st.columns(3)
                )

                with result_col1:

                    st.markdown(
                        f"""
                        <div class="result-metric">
                            <div class="result-metric-title">
                                Crop
                            </div>
                            <div class="result-metric-value">
                                {crop}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with result_col2:

                    st.markdown(
                        f"""
                        <div class="result-metric">
                            <div class="result-metric-title">
                                Prediction
                            </div>
                            <div class="result-metric-value">
                                {disease}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with result_col3:

                    st.markdown(
                        f"""
                        <div class="result-metric">
                            <div class="result-metric-title">
                                Confidence
                            </div>
                            <div class="result-metric-value">
                                {confidence * 100:.2f}%
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"""
                    <div class="confidence-box">
                        <strong>Confidence Level:</strong>
                        {confidence_level}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.divider()

                st.markdown(
                    '<div class="section-heading">'
                    '📊 Top 3 Predictions'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.caption(
                    "The model's three highest-probability "
                    "predictions for the uploaded image."
                )

                for number, prediction in enumerate(
                    top_predictions,
                    start=1
                ):

                    (
                        top_crop,
                        top_disease
                    ) = format_prediction(
                        prediction["class"]
                    )

                    top_confidence = (
                        prediction["confidence"] * 100
                    )

                    st.markdown(
                        f"""
                        <div class="top-prediction-box">
                            <strong>
                                {number}. {top_crop} — {top_disease}
                            </strong>
                            <br>
                            Confidence:
                            {top_confidence:.2f}%
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                disease_data = get_disease_info(
                    predicted_class
                )

                if disease_data:

                    st.divider()

                    st.markdown(
                        '<div class="section-heading">'
                        '🌿 Disease Information'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    st.write(
                        f"**Disease:** "
                        f"{disease_data['name']}"
                    )

                    st.write(
                        f"**Crop:** "
                        f"{disease_data['crop']}"
                    )

                    st.write(
                        disease_data["description"]
                    )

                    st.markdown(
                        "### 🔍 Common Symptoms"
                    )

                    for symptom in disease_data[
                        "symptoms"
                    ]:

                        st.write(
                            f"• {symptom}"
                        )

                    st.markdown(
                        "### 🛠️ Management"
                    )

                    for item in disease_data[
                        "management"
                    ]:

                        st.write(
                            f"• {item}"
                        )

                    st.markdown(
                        "### 🛡️ Prevention"
                    )

                    for item in disease_data[
                        "prevention"
                    ]:

                        st.write(
                            f"• {item}"
                        )

                else:

                    st.info(
                        "Detailed information for this "
                        "prediction is currently being "
                        "added to the system."
                    )

        else:

            st.info(
                "Please upload a clear image of a tomato, "
                "pepper, or potato leaf."
            )

    with guide_col:

        st.markdown(
            '<div class="section-heading">'
            '🤖 How It Works'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="analysis-guide">

            <strong>Step 1 — Upload</strong><br>
            Select a clear image of a crop leaf.

            <br><br>

            <strong>Step 2 — Analyze</strong><br>
            The CNN model analyzes the visual
            characteristics of the leaf.

            <br><br>

            <strong>Step 3 — Prediction</strong><br>
            The system identifies the most likely
            crop disease and confidence level.

            <br><br>

            <strong>Step 4 — Guidance</strong><br>
            Available disease information, symptoms,
            management and prevention guidance are displayed.

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-heading">'
            '🌱 Supported Crops'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            "🍅 Tomato"
        )

        st.write(
            "🌶️ Pepper"
        )

        st.write(
            "🥔 Potato"
        )

        st.info(
            "For best results, use a clear image where "
            "the leaf is visible and well illuminated."
        )


# ============================================================
# PREDICTION HISTORY
# ============================================================

elif page == "Prediction History":

    st.markdown(
        '<div class="main-title">'
        'Prediction History'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Previously analyzed crop leaf predictions'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    history = get_prediction_history()

    if history:

        st.write(
            f"**Total Predictions:** {len(history)}"
        )

        st.divider()

        for record in history:

            confidence_percentage = (
                record["confidence"] * 100
            )

            st.markdown(
                f"""
                <div class="history-box">
                    <strong>
                        {record["crop"]} —
                        {record["prediction"]}
                    </strong>
                    <br>
                    Confidence:
                    {confidence_percentage:.2f}%
                    <br>
                    Date & Time:
                    {record["date_time"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        if st.button(
            "Clear Prediction History"
        ):

            clear_prediction_history()

            st.success(
                "Prediction history cleared successfully."
            )

            st.rerun()

    else:

        st.info(
            "No prediction history available yet. "
            "Analyze a crop leaf image to create your "
            "first history record."
        )


# ============================================================
# CROP INFORMATION
# ============================================================

elif page == "Crop Information":

    st.title("🌱 Crop Information")

    st.write(
        "Learn about the crops supported by "
        "AYUBA CROP DOCTOR and the diseases "
        "that the system can detect."
    )

    st.divider()

    selected_crop = st.selectbox(
        "Select Crop",
        [
            "Tomato",
            "Pepper",
            "Potato"
        ]
    )

    crop_info = get_crop_info(
        selected_crop
    )

    if crop_info:

        st.subheader(
            f"🌱 {selected_crop}"
        )

        st.write(
            crop_info["description"]
        )

        st.divider()

        st.subheader(
            "Diseases Supported"
        )

        for disease in crop_info["diseases"]:

            st.markdown(
                f"• {disease}"
            )

        st.divider()

        st.subheader(
            "Prevention Guidelines"
        )

        for prevention in crop_info["prevention"]:

            st.markdown(
                f"• {prevention}"
            )


# ============================================================
# ABOUT
# ============================================================

elif page == "About":

    st.markdown(
        '<div class="main-title">'
        'About AYUBA CROP DOCTOR'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-Based Vegetable Crop Disease Detection System'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="section-title">'
        'About the System'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">

        <p>
        <strong>AYUBA CROP DOCTOR</strong> is an artificial
        intelligence-based vegetable crop disease detection
        system designed to assist users in identifying selected
        crop diseases from leaf images.
        </p>

        <p>
        The system uses a <strong>Convolutional Neural Network
        (CNN)</strong>, a deep learning technique commonly used
        for image classification, to analyze uploaded crop leaf
        images and generate a predicted disease category.
        </p>

        <p>
        AYUBA CROP DOCTOR is designed as a practical academic
        and decision-support application that demonstrates the
        use of artificial intelligence in agricultural disease
        detection.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        'What AYUBA CROP DOCTOR Can Do'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="info-box">
            <h3>Image Analysis</h3>
            <p>
            Analyze uploaded crop leaf images using
            a trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="info-box">
            <h3>Disease Prediction</h3>
            <p>
            Predict selected disease categories and
            display the model confidence.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="info-box">
            <h3>Decision Support</h3>
            <p>
            Provide disease information, symptoms,
            management and prevention guidance.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">'
        'Technology'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">

        <p>
        <strong>Artificial Intelligence:</strong>
        Used for automated image-based disease classification.
        </p>

        <p>
        <strong>Deep Learning:</strong>
        The disease detection engine is based on a
        Convolutional Neural Network (CNN).
        </p>

        <p>
        <strong>Image Classification:</strong>
        Crop leaf images are processed and classified into
        supported disease categories.
        </p>

        <p>
        <strong>Application Interface:</strong>
        The system provides an interactive interface for
        image analysis, disease information, crop information
        and prediction history.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        'Supported Crops'
        '</div>',
        unsafe_allow_html=True
    )

    crop1, crop2, crop3 = st.columns(3)

    with crop1:

        st.markdown(
            """
            <div class="info-box">
            <h3>Tomato</h3>
            <p>
            Selected tomato diseases supported by
            the trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with crop2:

        st.markdown(
            """
            <div class="info-box">
            <h3>Pepper</h3>
            <p>
            Selected pepper diseases supported by
            the trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with crop3:

        st.markdown(
            """
            <div class="info-box">
            <h3>Potato</h3>
            <p>
            Selected potato diseases supported by
            the trained CNN model.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown(
        '<div class="section-title">'
        'Disclaimer'
        '</div>',
        unsafe_allow_html=True
    )

    st.warning(
        """
        AYUBA CROP DOCTOR is an AI-based preliminary
        decision-support tool. Its predictions are generated
        from image analysis by a trained machine learning model
        and may not always be correct.

        The system should not be considered a replacement for
        professional agricultural diagnosis, laboratory testing,
        or expert advice.

        Users should verify important disease diagnoses with a
        qualified agricultural professional, agronomist,
        plant pathologist, or other appropriate expert before
        taking significant treatment or management decisions.
        """
    )

    st.markdown(
        '<div class="section-title">'
        'Responsible Use'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">

        <p>
        For the best possible prediction, upload a clear,
        well-focused image showing the affected crop leaf.
        </p>

        <p>
        Avoid relying on a single AI prediction when the crop
        condition is serious, unusual, or unclear.
        </p>

        <p>
        Always consider environmental conditions, farming
        practices, pest activity and other possible causes
        when evaluating crop health.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        'Project Purpose'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        AYUBA CROP DOCTOR demonstrates how artificial intelligence
        and deep learning can be applied to agricultural problems.

        The project is intended to support learning, research,
        experimentation and practical demonstration of an
        AI-powered crop disease detection system.
        """
    )

    st.divider()

    st.markdown(
        '<div class="footer">'
        'AYUBA CROP DOCTOR<br>'
        'AI-Based Vegetable Crop Disease Detection System<br>'
        'AI for Agriculture • Learning • Research • Decision Support'
        '</div>',
        unsafe_allow_html=True
    )