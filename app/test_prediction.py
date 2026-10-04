import os
import sys
import glob

sys.path.append(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

from predict import predict_image


print("=" * 70)
print("TOGA CROP DOCTOR")
print("CNN BATCH PREDICTION TEST")
print("=" * 70)


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------
TEST_FOLDER = (
    r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"
    r"\dataset\test\Tomato_Late_Blight"
)

TRUE_CLASS = "Tomato_Late_Blight"


NUMBER_OF_IMAGES = 10


# --------------------------------------------------
# FIND TEST IMAGES
# --------------------------------------------------

image_files = glob.glob(
    os.path.join(TEST_FOLDER, "*.JPG")
)

image_files += glob.glob(
    os.path.join(TEST_FOLDER, "*.jpg")
)


image_files = image_files[:NUMBER_OF_IMAGES]


print()
print(f"Test folder: {TEST_FOLDER}")
print(f"Images found: {len(image_files)}")
print()


# --------------------------------------------------
# BATCH TEST
# --------------------------------------------------

correct = 0
total = len(image_files)


for number, image_path in enumerate(
    image_files,
    start=1
):

    try:

        result = predict_image(
            image_path
        )

        predicted_class = result[
            "prediction"
        ]

        confidence = result[
            "confidence"
        ] * 100

        if predicted_class == TRUE_CLASS:
            status = "CORRECT"
            correct += 1
        else:
            status = "WRONG"

        print("-" * 70)

        print(
            f"Image {number}/{total}"
        )

        print(
            f"Actual     : {TRUE_CLASS}"
        )

        print(
            f"Prediction : {predicted_class}"
        )

        print(
            f"Confidence : {confidence:.2f}%"
        )

        print(
            f"Status     : {status}"
        )

    except Exception as error:

        print("-" * 70)

        print(
            f"Image {number}/{total}"
        )

        print(
            "ERROR:"
        )

        print(error)


# --------------------------------------------------
# FINAL RESULT
# --------------------------------------------------

print()
print("=" * 70)
print("BATCH TEST RESULT")
print("=" * 70)

if total > 0:

    accuracy = (
        correct / total
    ) * 100

    print(
        f"Correct Predictions : "
        f"{correct}/{total}"
    )

    print(
        f"Batch Accuracy      : "
        f"{accuracy:.2f}%"
    )

else:

    print(
        "No test images found."
    )


print()
print("=" * 70)
print("BATCH TEST COMPLETED")
print("=" * 70)