import os
import json
import numpy as np
import tensorflow as tf

# ============================================================
# TOGA CROP DOCTOR
# CNN PREDICTION ENGINE
# ============================================================

PROJECT = r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"

MODEL_PATH = os.path.join(
    PROJECT,
    "model",
    "toga_crop_doctor_cnn.h5"
)

CLASS_NAMES_PATH = os.path.join(
    PROJECT,
    "model",
    "class_names.json"
)

IMAGE_SIZE = (224, 224)


# ============================================================
# LOAD MODEL
# ============================================================

print("=" * 60)
print("TOGA CROP DOCTOR")
print("CNN PREDICTION ENGINE")
print("=" * 60)

print("\nLoading CNN model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("CNN model loaded successfully.")


# ============================================================
# LOAD CLASS NAMES
# ============================================================

with open(
    CLASS_NAMES_PATH,
    "r",
    encoding="utf-8"
) as file:

    class_names = json.load(file)

print(
    f"Classes loaded: {len(class_names)}"
)


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_image(image_path):

    if not os.path.exists(image_path):

        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    # Load image
    image = tf.keras.utils.load_img(
        image_path,
        target_size=IMAGE_SIZE
    )

    # Convert image to array
    image_array = tf.keras.utils.img_to_array(
        image
    )

    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Normalize
    image_array = image_array / 255.0

    # Predict
    predictions = model.predict(
        image_array,
        verbose=0
    )

    # Get predicted class
    predicted_index = np.argmax(
        predictions[0]
    )

    predicted_class = class_names[
        predicted_index
    ]

    confidence = float(
        predictions[0][predicted_index]
    )

    # Get top 3 predictions
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

    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "top_predictions": top_predictions
    }


# ============================================================
# TEST MODE
# ============================================================

if __name__ == "__main__":

    print("\nPrediction engine is ready.")

    print(
        "\nTo test an image, we will use:"
    )

    print(
        "predict_image('path_to_image')"
    )

    print("\nTOGA CROP DOCTOR PREDICTION ENGINE READY")

    print("=" * 60)