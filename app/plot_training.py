import os
import json

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


# ============================================================
# TOGA CROP DOCTOR
# CNN TRAINING GRAPHS
# ============================================================

PROJECT = r"C:\Users\DELL\Desktop\TOGA-CROP-DOCTOR"

RESULTS_DIR = os.path.join(
    PROJECT,
    "results"
)

HISTORY_PATH = os.path.join(
    RESULTS_DIR,
    "cnn_training_history.json"
)


print("=" * 60)
print("TOGA CROP DOCTOR")
print("CNN TRAINING GRAPHS")
print("=" * 60)


# ============================================================
# CHECK HISTORY FILE
# ============================================================

if not os.path.exists(HISTORY_PATH):

    print("\nERROR: Training history file not found!")

    print(HISTORY_PATH)

    raise SystemExit


# ============================================================
# LOAD TRAINING HISTORY
# ============================================================

with open(
    HISTORY_PATH,
    "r",
    encoding="utf-8"
) as file:

    history = json.load(file)


print("\nTraining history loaded successfully.")


# ============================================================
# GET TRAINING VALUES
# ============================================================

accuracy = history["accuracy"]
val_accuracy = history["val_accuracy"]

loss = history["loss"]
val_loss = history["val_loss"]

epochs = range(
    1,
    len(accuracy) + 1
)


print(
    f"Total epochs found: {len(accuracy)}"
)


# ============================================================
# ACCURACY GRAPH
# ============================================================

print("\nCreating accuracy graph...")


plt.figure(
    figsize=(10, 6)
)

plt.plot(
    epochs,
    accuracy,
    marker="o",
    label="Training Accuracy"
)

plt.plot(
    epochs,
    val_accuracy,
    marker="o",
    label="Validation Accuracy"
)

plt.title(
    "TOGA Crop Doctor - CNN Accuracy"
)

plt.xlabel(
    "Epoch"
)

plt.ylabel(
    "Accuracy"
)

plt.legend()

plt.grid(
    True
)

plt.tight_layout()


accuracy_path = os.path.join(
    RESULTS_DIR,
    "cnn_accuracy_graph.png"
)


plt.savefig(
    accuracy_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print(
    "Accuracy graph saved successfully."
)


# ============================================================
# LOSS GRAPH
# ============================================================

print("\nCreating loss graph...")


plt.figure(
    figsize=(10, 6)
)

plt.plot(
    epochs,
    loss,
    marker="o",
    label="Training Loss"
)

plt.plot(
    epochs,
    val_loss,
    marker="o",
    label="Validation Loss"
)

plt.title(
    "TOGA Crop Doctor - CNN Loss"
)

plt.xlabel(
    "Epoch"
)

plt.ylabel(
    "Loss"
)

plt.legend()

plt.grid(
    True
)

plt.tight_layout()


loss_path = os.path.join(
    RESULTS_DIR,
    "cnn_loss_graph.png"
)


plt.savefig(
    loss_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print(
    "Loss graph saved successfully."
)


# ============================================================
# COMPLETED
# ============================================================

print("\n")
print("=" * 60)
print("TRAINING GRAPHS COMPLETED")
print("=" * 60)

print("\nAccuracy graph:")
print(accuracy_path)

print("\nLoss graph:")
print(loss_path)

print(
    "\nTOGA CROP DOCTOR TRAINING GRAPHS READY"
)

print("=" * 60)