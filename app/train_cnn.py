import os
import json
import tensorflow as tf
from tensorflow.keras import layers, models

# ============================================================
# TOGA CROP DOCTOR
# CUSTOM CNN TRAINING
# ============================================================

PROJECT = r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"

DATASET = os.path.join(PROJECT, "dataset")

TRAIN_DIR = os.path.join(DATASET, "train")
VALIDATION_DIR = os.path.join(DATASET, "validation")

MODEL_DIR = os.path.join(PROJECT, "model")

RESULTS_DIR = os.path.join(PROJECT, "results")

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

IMAGE_SIZE = (224, 224)

BATCH_SIZE = 32

EPOCHS = 15

SEED = 42

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

print("=" * 60)
print("TOGA CROP DOCTOR")
print("CUSTOM CNN TRAINING")
print("=" * 60)

print("\nTensorFlow version:", tf.__version__)

print("\nLoading training dataset...")

# ------------------------------------------------------------
# LOAD TRAINING DATA
# ------------------------------------------------------------

train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True,
    seed=SEED
)

print("\nLoading validation dataset...")

# ------------------------------------------------------------
# LOAD VALIDATION DATA
# ------------------------------------------------------------

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    VALIDATION_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# ------------------------------------------------------------
# CLASS NAMES
# ------------------------------------------------------------

class_names = train_dataset.class_names

NUM_CLASSES = len(class_names)

print("\nClasses detected:", NUM_CLASSES)

for index, class_name in enumerate(class_names):

    print(
        f"{index + 1:02d}. {class_name}"
    )

# ------------------------------------------------------------
# SAVE CLASS NAMES
# ------------------------------------------------------------

class_names_path = os.path.join(
    MODEL_DIR,
    "class_names.json"
)

with open(
    class_names_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        class_names,
        file,
        indent=4
    )

print(
    "\nClass names saved to:",
    class_names_path
)

# ------------------------------------------------------------
# DATA PREFETCHING
# ------------------------------------------------------------

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(
    buffer_size=AUTOTUNE
)

validation_dataset = validation_dataset.prefetch(
    buffer_size=AUTOTUNE
)

# ------------------------------------------------------------
# DATA AUGMENTATION
# ------------------------------------------------------------

data_augmentation = tf.keras.Sequential(
    [

        layers.RandomFlip(
            "horizontal"
        ),

        layers.RandomRotation(
            0.15
        ),

        layers.RandomZoom(
            0.15
        ),

        layers.RandomTranslation(
            height_factor=0.10,
            width_factor=0.10
        )

    ],
    name="data_augmentation"
)

# ------------------------------------------------------------
# CUSTOM CNN MODEL
# ------------------------------------------------------------

model = models.Sequential(

    [

        layers.Input(
            shape=(224, 224, 3)
        ),

        data_augmentation,

        layers.Rescaling(
            1.0 / 255
        ),

        # -------------------------
        # CONVOLUTION BLOCK 1
        # -------------------------

        layers.Conv2D(
            32,
            (3, 3),
            activation="relu"
        ),

        layers.MaxPooling2D(
            (2, 2)
        ),

        # -------------------------
        # CONVOLUTION BLOCK 2
        # -------------------------

        layers.Conv2D(
            64,
            (3, 3),
            activation="relu"
        ),

        layers.MaxPooling2D(
            (2, 2)
        ),

        # -------------------------
        # CONVOLUTION BLOCK 3
        # -------------------------

        layers.Conv2D(
            128,
            (3, 3),
            activation="relu"
        ),

        layers.MaxPooling2D(
            (2, 2)
        ),

        # -------------------------
        # CLASSIFICATION
        # -------------------------

        layers.Flatten(),

        layers.Dense(
            128,
            activation="relu"
        ),

        layers.Dropout(
            0.5
        ),

        layers.Dense(
            NUM_CLASSES,
            activation="softmax"
        )

    ],

    name="TOGA_Custom_CNN"
)

# ------------------------------------------------------------
# MODEL SUMMARY
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("MODEL ARCHITECTURE")
print("=" * 60)

model.summary()

# ------------------------------------------------------------
# COMPILE MODEL
# ------------------------------------------------------------

model.compile(

    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.001
    ),

    loss="sparse_categorical_crossentropy",

    metrics=[
        "accuracy"
    ]
)

# ------------------------------------------------------------
# CALLBACKS
# ------------------------------------------------------------

best_model_path = os.path.join(
    MODEL_DIR,
    "toga_crop_doctor_cnn.h5"
)

checkpoint = tf.keras.callbacks.ModelCheckpoint(

    best_model_path,

    monitor="val_accuracy",

    save_best_only=True,

    mode="max",

    verbose=1
)

early_stopping = tf.keras.callbacks.EarlyStopping(

    monitor="val_loss",

    patience=4,

    restore_best_weights=True,

    verbose=1
)

# ------------------------------------------------------------
# TRAINING
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("STARTING CNN TRAINING")
print("=" * 60)

history = model.fit(

    train_dataset,

    validation_data=validation_dataset,

    epochs=EPOCHS,

    callbacks=[
        checkpoint,
        early_stopping
    ]

)

# ------------------------------------------------------------
# SAVE FINAL MODEL
# ------------------------------------------------------------

final_model_path = os.path.join(
    MODEL_DIR,
    "toga_crop_doctor_cnn_final.h5"
)

model.save(
    final_model_path
)

# ------------------------------------------------------------
# SAVE TRAINING HISTORY
# ------------------------------------------------------------

history_path = os.path.join(
    RESULTS_DIR,
    "cnn_training_history.json"
)

history_data = {
    key: [float(value) for value in values]
    for key, values in history.history.items()
}

with open(
    history_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        history_data,
        file,
        indent=4
    )

# ------------------------------------------------------------
# COMPLETED
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("CNN TRAINING COMPLETED")
print("=" * 60)

print(
    "\nBest model:",
    best_model_path
)

print(
    "\nFinal model:",
    final_model_path
)

print(
    "\nTraining history:",
    history_path
)

print("\nTOGA CROP DOCTOR CNN MODEL READY")
print("=" * 60)