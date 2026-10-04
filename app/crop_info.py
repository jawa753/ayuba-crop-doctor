# ============================================================
# AYUBA CROP DOCTOR
# Crop Information Database
# ============================================================

CROP_INFORMATION = {

    "Tomato": {
        "description":
            "Tomato is an important vegetable crop widely cultivated "
            "for food and commercial production.",

        "diseases": [
            "Bacterial Spot",
            "Early Blight",
            "Healthy",
            "Late Blight",
            "Leaf Mold",
            "Septoria Leaf Spot",
            "Spider Mites",
            "Target Spot",
            "Yellow Leaf Curl Virus",
            "Mosaic Virus"
        ],

        "prevention": [
            "Use healthy and disease-free planting materials.",
            "Maintain proper spacing between plants.",
            "Avoid unnecessary wetting of leaves.",
            "Remove severely infected plant materials.",
            "Keep the farm free from weeds and plant debris.",
            "Monitor plants regularly for early signs of disease."
        ]
    },

    "Pepper": {
        "description":
            "Pepper is a widely cultivated vegetable crop used "
            "for food, seasoning and commercial production.",

        "diseases": [
            "Bacterial Spot",
            "Healthy"
        ],

        "prevention": [
            "Use healthy seedlings.",
            "Maintain good field sanitation.",
            "Avoid excessive moisture around plants.",
            "Provide adequate spacing for air circulation.",
            "Remove infected leaves and plant materials.",
            "Inspect plants regularly."
        ]
    },

    "Potato": {
        "description":
            "Potato is an important food crop that can be affected "
            "by several fungal and environmental diseases.",

        "diseases": [
            "Early Blight",
            "Late Blight",
            "Healthy"
        ],

        "prevention": [
            "Use healthy seed potatoes.",
            "Practice proper crop rotation.",
            "Maintain good field sanitation.",
            "Avoid prolonged leaf wetness.",
            "Remove infected plant materials.",
            "Monitor crops regularly for disease symptoms."
        ]
    }
}


def get_crop_info(crop):

    return CROP_INFORMATION.get(
        crop,
        None
    )


if __name__ == "__main__":

    print("=" * 60)
    print("AYUBA CROP DOCTOR")
    print("CROP INFORMATION DATABASE")
    print("=" * 60)

    print()
    print(
        f"Total crops: {len(CROP_INFORMATION)}"
    )

    print()

    for crop, information in CROP_INFORMATION.items():

        print(
            f"Crop: {crop}"
        )

        print(
            f"Diseases supported: "
            f"{len(information['diseases'])}"
        )

        print()

    print(
        "Crop information system ready."
    )

    print("=" * 60)