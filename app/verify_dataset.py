import os
import cv2

# ============================================================
# TOGA CROP DOCTOR
# DATASET VERIFICATION
# ============================================================

PROJECT = r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"

DATASET = os.path.join(PROJECT, "dataset")

SPLITS = [
    "train",
    "validation",
    "test"
]

CLASSES = [
    "Pepper_Bacterial_Spot",
    "Pepper_Healthy",
    "Potato_Early_Blight",
    "Potato_Late_Blight",
    "Potato_Healthy",
    "Tomato_Bacterial_Spot",
    "Tomato_Early_Blight",
    "Tomato_Late_Blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_Leaf_Spot",
    "Tomato_Spider_Mites",
    "Tomato_Target_Spot",
    "Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato_Mosaic_Virus",
    "Tomato_Healthy"
]

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png"
)

print("=" * 60)
print("TOGA CROP DOCTOR")
print("DATASET VERIFICATION")
print("=" * 60)

total_images = 0
total_corrupted = 0
total_invalid = 0

for split in SPLITS:

    print("\n" + "=" * 60)
    print(f"{split.upper()} DATASET")
    print("=" * 60)

    split_total = 0

    for class_name in CLASSES:

        class_folder = os.path.join(
            DATASET,
            split,
            class_name
        )

        if not os.path.exists(class_folder):

            print(
                f"ERROR: Missing class folder: {class_name}"
            )

            continue

        files = os.listdir(class_folder)

        image_count = 0
        corrupted_count = 0
        invalid_count = 0

        for file in files:

            file_path = os.path.join(
                class_folder,
                file
            )

            if not os.path.isfile(file_path):
                continue

            if not file.lower().endswith(
                VALID_EXTENSIONS
            ):

                invalid_count += 1

                continue

            image_count += 1

            image = cv2.imread(file_path)

            if image is None:

                corrupted_count += 1

        split_total += image_count

        total_images += image_count

        total_corrupted += corrupted_count

        total_invalid += invalid_count

        print(
            f"{class_name:<40}"
            f"{image_count:>6} images"
            f" | Corrupt: {corrupted_count}"
        )

    print("-" * 60)

    print(
        f"{split.upper()} TOTAL: {split_total}"
    )


print("\n")
print("=" * 60)
print("FINAL VERIFICATION REPORT")
print("=" * 60)

print(
    f"\nTotal valid images : {total_images}"
)

print(
    f"Corrupted images   : {total_corrupted}"
)

print(
    f"Invalid files      : {total_invalid}"
)

print(
    f"Total classes      : {len(CLASSES)}"
)

print("\n" + "-" * 60)

if total_corrupted == 0 and total_invalid == 0:

    print("DATASET STATUS: READY FOR TRAINING")

else:

    print(
        "DATASET STATUS: REVIEW REQUIRED"
    )

print("-" * 60)

print("\nTOGA CROP DOCTOR")
print("Dataset verification completed.")