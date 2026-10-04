import os
import json
import numpy as np
import tensorflow as tf

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# ============================================================
# TOGA CROP DOCTOR
# CNN MODEL EVALUATION
# ============================================================

PROJECT = r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"

DATASET = os.path.join(
    PROJECT,
    "dataset"
)

TEST_DIR = os.path.join(
    DATASET,
    "test"
)

MODEL_PATH = os.path.join(
    PROJECT,
    "model",
    "toga_crop_doctor_cnn.h5"
)

MODEL_DIR = os.path.join(
    PROJECT,
    "model"
)

RESULTS_DIR = os.path.join(
    PROJECT,
    "results"
)

os.makedirs(
    RESULTS_DIR,
    exist_ok=True
)

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

IMAGE_SIZE = (224, 224)

BATCH_SIZE = 32

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

print("=" * 60)
print("TOGA CROP DOCTOR")
print("CNN MODEL EVALUATION")
print("=" * 60)

print(
    "\nTensorFlow version:",
    tf.__version__
)

# ------------------------------------------------------------
# CHECK MODEL
# ------------------------------------------------------------

if not os.path.exists(MODEL_PATH):

    print("\nERROR: Model file not found!")

    print(
        "\nExpected model:"
    )

    print(MODEL_PATH)

    raise SystemExit

print(
    "\nLoading best CNN model..."
)

# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------

model = tf.keras.models.load_model(
    MODEL_PATH
)

print(
    "Best CNN model loaded successfully."
)

# ------------------------------------------------------------
# LOAD CLASS NAMES
# ------------------------------------------------------------

class_names_path = os.path.join(
    MODEL_DIR,
    "class_names.json"
)

if os.path.exists(class_names_path):

    with open(
        class_names_path,
        "r",
        encoding="utf-8"
    ) as file:

        class_names = json.load(file)

else:

    class_names = sorted(
        [
            folder
            for folder in os.listdir(TEST_DIR)
            if os.path.isdir(
                os.path.join(
                    TEST_DIR,
                    folder
                )
            )
        ]
    )

NUM_CLASSES = len(class_names)

print(
    "\nNumber of classes:",
    NUM_CLASSES
)

print("\nClasses:")

for index, class_name in enumerate(
    class_names
):

    print(
        f"{index + 1:02d}. {class_name}"
    )

# ------------------------------------------------------------
# LOAD TEST DATASET
# ------------------------------------------------------------

print(
    "\nLoading test dataset..."
)

test_dataset = tf.keras.utils.image_dataset_from_directory(

    TEST_DIR,

    image_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    shuffle=False
)

print(
    "\nTest dataset loaded successfully."
)

# ------------------------------------------------------------
# MODEL EVALUATION
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

test_loss, test_accuracy = model.evaluate(
    test_dataset,
    verbose=1
)

print("\n")
print(
    f"Test Loss     : {test_loss:.4f}"
)

print(
    f"Test Accuracy : {test_accuracy * 100:.2f}%"
)

# ------------------------------------------------------------
# GENERATE PREDICTIONS
# ------------------------------------------------------------

print("\nGenerating predictions...")

predictions = model.predict(
    test_dataset,
    verbose=1
)

predicted_classes = np.argmax(
    predictions,
    axis=1
)

# ------------------------------------------------------------
# TRUE LABELS
# ------------------------------------------------------------

true_classes = np.concatenate(
    [
        labels.numpy()
        for images, labels
        in test_dataset
    ]
)

# ------------------------------------------------------------
# ACCURACY CHECK
# ------------------------------------------------------------

accuracy = accuracy_score(
    true_classes,
    predicted_classes
)

print(
    f"\nAccuracy check: {accuracy * 100:.2f}%"
)

# ------------------------------------------------------------
# CLASSIFICATION REPORT
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

report = classification_report(

    true_classes,

    predicted_classes,

    target_names=class_names,

    digits=4,

    zero_division=0
)

print(report)

# ------------------------------------------------------------
# SAVE CLASSIFICATION REPORT
# ------------------------------------------------------------

report_path = os.path.join(
    RESULTS_DIR,
    "cnn_classification_report.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "TOGA CROP DOCTOR\n"
    )

    file.write(
        "CNN MODEL EVALUATION REPORT\n"
    )

    file.write(
        "=" * 60 + "\n\n"
    )

    file.write(
        f"Test Accuracy: "
        f"{test_accuracy * 100:.2f}%\n\n"
    )

    file.write(
        report
    )

print(
    "\nClassification report saved:"
)

print(report_path)

# ------------------------------------------------------------
# CONFUSION MATRIX
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

cm = confusion_matrix(
    true_classes,
    predicted_classes
)

print(cm)

# ------------------------------------------------------------
# SAVE CONFUSION MATRIX
# ------------------------------------------------------------

cm_path = os.path.join(
    RESULTS_DIR,
    "cnn_confusion_matrix.npy"
)

np.save(
    cm_path,
    cm
)

print(
    "\nConfusion matrix saved:"
)

print(cm_path)

# ------------------------------------------------------------
# FINAL RESULT
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("CNN EVALUATION COMPLETED")
print("=" * 60)

print(
    f"\nFINAL TEST ACCURACY: "
    f"{test_accuracy * 100:.2f}%"
)

print(
    "\nTOGA CROP DOCTOR CNN EVALUATION READY"
)

print("=" * 60)