import os
import random
import shutil

# ============================================================
# TOGA CROP DOCTOR
# DATASET PREPARATION
# ============================================================

# ------------------------------------------------------------
# 1. PLANTVILLAGE SOURCE FOLDER
# ------------------------------------------------------------

SOURCE = r"C:\Users\DELL\Downloads\PlantVillage-Dataset-master\PlantVillage-Dataset-master\raw\color"

# ------------------------------------------------------------
# 2. TOGA CROP DOCTOR PROJECT FOLDER
# ------------------------------------------------------------

PROJECT = r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"

DATASET = os.path.join(PROJECT, "dataset")

# ------------------------------------------------------------
# 3. SOURCE CLASS → CLEAN TOGA CLASS
# ------------------------------------------------------------

CLASS_MAPPING = {

    "Pepper,_bell___Bacterial_spot":
        "Pepper_Bacterial_Spot",

    "Pepper,_bell___healthy":
        "Pepper_Healthy",

    "Potato___Early_blight":
        "Potato_Early_Blight",

    "Potato___Late_blight":
        "Potato_Late_Blight",

    "Potato___healthy":
        "Potato_Healthy",

    "Tomato___Bacterial_spot":
        "Tomato_Bacterial_Spot",

    "Tomato___Early_blight":
        "Tomato_Early_Blight",

    "Tomato___Late_blight":
        "Tomato_Late_Blight",

    "Tomato___Leaf_Mold":
        "Tomato_Leaf_Mold",

    "Tomato___Septoria_leaf_spot":
        "Tomato_Septoria_Leaf_Spot",

    "Tomato___Spider_mites Two-spotted_spider_mite":
        "Tomato_Spider_Mites",

    "Tomato___Target_Spot":
        "Tomato_Target_Spot",

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus":
        "Tomato_Yellow_Leaf_Curl_Virus",

    "Tomato___Tomato_mosaic_virus":
        "Tomato_Mosaic_Virus",

    "Tomato___healthy":
        "Tomato_Healthy"
}

# ------------------------------------------------------------
# 4. SETTINGS
# ------------------------------------------------------------

TRAIN_RATIO = 0.70
VALIDATION_RATIO = 0.20
TEST_RATIO = 0.10

RANDOM_SEED = 42

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png"
)

random.seed(RANDOM_SEED)

# ------------------------------------------------------------
# 5. CHECK SOURCE FOLDER
# ------------------------------------------------------------

print("=" * 60)
print("TOGA CROP DOCTOR")
print("DATASET PREPARATION")
print("=" * 60)

print("\nChecking PlantVillage source folder...")

if not os.path.exists(SOURCE):

    print("\nERROR: PlantVillage source folder was not found.")

    print("\nExpected location:")
    print(SOURCE)

    print("\nPlease check the path and try again.")

    raise SystemExit

print("Source folder found successfully.")

# ------------------------------------------------------------
# 6. CLEAN OLD PREPARED DATASET
# ------------------------------------------------------------

print("\nCleaning old prepared dataset...")

for split in ["train", "validation", "test"]:

    split_folder = os.path.join(DATASET, split)

    if os.path.exists(split_folder):

        for item in os.listdir(split_folder):

            item_path = os.path.join(split_folder, item)

            if os.path.isdir(item_path):

                shutil.rmtree(item_path)

            else:

                os.remove(item_path)

print("Old dataset cleaned successfully.")

# ------------------------------------------------------------
# 7. CREATE CLEAN CLASS FOLDERS
# ------------------------------------------------------------

print("\nCreating TOGA class folders...")

for split in ["train", "validation", "test"]:

    for clean_class in CLASS_MAPPING.values():

        folder = os.path.join(
            DATASET,
            split,
            clean_class
        )

        os.makedirs(folder, exist_ok=True)

print("Class folders created successfully.")

# ------------------------------------------------------------
# 8. PREPARE EACH CLASS
# ------------------------------------------------------------

grand_total = 0
grand_train = 0
grand_validation = 0
grand_test = 0

for source_class, clean_class in CLASS_MAPPING.items():

    source_folder = os.path.join(
        SOURCE,
        source_class
    )

    print("\n" + "-" * 60)

    print("Source class:")
    print(source_class)

    print("TOGA class:")
    print(clean_class)

    # --------------------------------------------------------
    # CHECK CLASS
    # --------------------------------------------------------

    if not os.path.exists(source_folder):

        print("ERROR: Source class not found!")

        continue

    # --------------------------------------------------------
    # GET IMAGES
    # --------------------------------------------------------

    files = [

        file

        for file in os.listdir(source_folder)

        if file.lower().endswith(VALID_EXTENSIONS)

    ]

    # --------------------------------------------------------
    # SHUFFLE
    # --------------------------------------------------------

    random.shuffle(files)

    total = len(files)

    # --------------------------------------------------------
    # CALCULATE SPLITS
    # --------------------------------------------------------

    train_end = int(total * TRAIN_RATIO)

    validation_end = (
        train_end
        + int(total * VALIDATION_RATIO)
    )

    train_files = files[:train_end]

    validation_files = files[
        train_end:validation_end
    ]

    test_files = files[
        validation_end:
    ]

    # --------------------------------------------------------
    # DESTINATION FOLDERS
    # --------------------------------------------------------

    train_destination = os.path.join(
        DATASET,
        "train",
        clean_class
    )

    validation_destination = os.path.join(
        DATASET,
        "validation",
        clean_class
    )

    test_destination = os.path.join(
        DATASET,
        "test",
        clean_class
    )

    # --------------------------------------------------------
    # COPY TRAIN
    # --------------------------------------------------------

    for file in train_files:

        source_file = os.path.join(
            source_folder,
            file
        )

        destination_file = os.path.join(
            train_destination,
            file
        )

        shutil.copy2(
            source_file,
            destination_file
        )

    # --------------------------------------------------------
    # COPY VALIDATION
    # --------------------------------------------------------

    for file in validation_files:

        source_file = os.path.join(
            source_folder,
            file
        )

        destination_file = os.path.join(
            validation_destination,
            file
        )

        shutil.copy2(
            source_file,
            destination_file
        )

    # --------------------------------------------------------
    # COPY TEST
    # --------------------------------------------------------

    for file in test_files:

        source_file = os.path.join(
            source_folder,
            file
        )

        destination_file = os.path.join(
            test_destination,
            file
        )

        shutil.copy2(
            source_file,
            destination_file
        )

    # --------------------------------------------------------
    # UPDATE TOTALS
    # --------------------------------------------------------

    grand_total += total

    grand_train += len(train_files)

    grand_validation += len(validation_files)

    grand_test += len(test_files)

    # --------------------------------------------------------
    # SHOW RESULT
    # --------------------------------------------------------

    print(
        f"Total      : {total}"
    )

    print(
        f"Train      : {len(train_files)}"
    )

    print(
        f"Validation : {len(validation_files)}"
    )

    print(
        f"Test       : {len(test_files)}"
    )

# ------------------------------------------------------------
# 9. FINAL SUMMARY
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("DATASET PREPARATION COMPLETE")
print("=" * 60)

print(
    f"\nTotal Images      : {grand_total}"
)

print(
    f"Training Images   : {grand_train}"
)

print(
    f"Validation Images : {grand_validation}"
)

print(
    f"Testing Images    : {grand_test}"
)

print(
    f"\nTotal Classes     : {len(CLASS_MAPPING)}"
)

print("\nDataset location:")

print(DATASET)

print("\n" + "=" * 60)

print("TOGA CROP DOCTOR DATASET READY")

print("=" * 60)