# ============================================================
# AYUBA CROP DOCTOR
# Disease Information Database
# ============================================================

DISEASE_INFO = {

    # ========================================================
    # PEPPER
    # ========================================================

    "Pepper_Bacterial_Spot": {

        "name": "Pepper Bacterial Spot",

        "crop": "Pepper",

        "description": (
            "Bacterial Spot is a bacterial disease that can "
            "affect pepper plants and cause lesions on leaves "
            "and fruits, especially under warm and humid conditions."
        ),

        "symptoms": [
            "Small dark or water-soaked spots on leaves",
            "Spots may enlarge and become brown",
            "Affected leaves may yellow and fall",
            "Dark lesions may appear on fruits"
        ],

        "management": [
            "Remove severely affected plant material",
            "Improve air circulation around plants",
            "Avoid unnecessary leaf wetness",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Use healthy planting materials",
            "Maintain good field sanitation",
            "Avoid working with plants when leaves are wet",
            "Monitor plants regularly"
        ]
    },


    "Pepper_Healthy": {

        "name": "Healthy Pepper",

        "crop": "Pepper",

        "description": (
            "The pepper leaf appears healthy based on the "
            "AI model prediction."
        ),

        "symptoms": [
            "No major visible disease symptoms detected",
            "Leaf structure appears generally healthy"
        ],

        "management": [
            "Continue normal crop management",
            "Provide adequate water and nutrients",
            "Monitor the plant regularly"
        ],

        "prevention": [
            "Maintain good field sanitation",
            "Monitor plants for early disease symptoms",
            "Use healthy planting materials"
        ]
    },


    # ========================================================
    # POTATO
    # ========================================================

    "Potato_Early_Blight": {

        "name": "Potato Early Blight",

        "crop": "Potato",

        "description": (
            "Early Blight is a fungal disease that commonly "
            "affects potato leaves and can reduce plant growth "
            "and yield."
        ),

        "symptoms": [
            "Brown circular spots on older leaves",
            "Dark rings may form inside leaf lesions",
            "Affected leaves may turn yellow",
            "Severe infection can cause leaf drop"
        ],

        "management": [
            "Remove severely infected plant material",
            "Improve field sanitation",
            "Avoid excessive leaf wetness",
            "Use appropriate fungicide management when necessary"
        ],

        "prevention": [
            "Use healthy planting materials",
            "Practice crop rotation",
            "Remove infected plant debris",
            "Maintain good field sanitation"
        ]
    },


    "Potato_Late_Blight": {

        "name": "Potato Late Blight",

        "crop": "Potato",

        "description": (
            "Late Blight is a serious potato disease that can "
            "spread rapidly under cool and wet conditions."
        ),

        "symptoms": [
            "Dark irregular lesions on leaves",
            "Rapid browning of affected tissues",
            "Leaves may die quickly",
            "Dark lesions may develop on tubers"
        ],

        "management": [
            "Remove severely affected plant material",
            "Improve field air circulation",
            "Avoid prolonged leaf wetness",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Use healthy seed potatoes",
            "Practice good field sanitation",
            "Monitor crops regularly",
            "Avoid unnecessary moisture on leaves"
        ]
    },


    "Potato_Healthy": {

        "name": "Healthy Potato",

        "crop": "Potato",

        "description": (
            "The potato leaf appears healthy based on the "
            "AI model prediction."
        ),

        "symptoms": [
            "No major visible disease symptoms detected",
            "Leaf structure appears generally healthy"
        ],

        "management": [
            "Continue normal crop management",
            "Provide adequate water and nutrients",
            "Monitor the crop regularly"
        ],

        "prevention": [
            "Use healthy planting materials",
            "Maintain field sanitation",
            "Monitor plants regularly"
        ]
    },


    # ========================================================
    # TOMATO
    # ========================================================

    "Tomato_Bacterial_Spot": {

        "name": "Tomato Bacterial Spot",

        "crop": "Tomato",

        "description": (
            "Bacterial Spot is a bacterial disease that can "
            "affect tomato leaves and fruits, particularly "
            "under warm and humid conditions."
        ),

        "symptoms": [
            "Small dark spots on leaves",
            "Spots may become larger and irregular",
            "Leaves may yellow and fall",
            "Dark spots may appear on fruits"
        ],

        "management": [
            "Remove severely affected plant material",
            "Improve air circulation",
            "Avoid unnecessary leaf wetness",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Use healthy planting materials",
            "Maintain good field sanitation",
            "Avoid overhead irrigation when possible",
            "Monitor plants regularly"
        ]
    },


    "Tomato_Early_Blight": {

        "name": "Tomato Early Blight",

        "crop": "Tomato",

        "description": (
            "Early Blight is a fungal disease that commonly "
            "affects tomato leaves and stems."
        ),

        "symptoms": [
            "Dark circular spots on older leaves",
            "Concentric rings may appear within lesions",
            "Leaves may turn yellow",
            "Severe infection may cause leaf drop"
        ],

        "management": [
            "Remove infected leaves",
            "Improve air circulation",
            "Avoid prolonged leaf wetness",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Practice crop rotation",
            "Remove infected plant debris",
            "Use healthy planting materials",
            "Maintain good field sanitation"
        ]
    },


    "Tomato_Healthy": {

        "name": "Healthy Tomato",

        "crop": "Tomato",

        "description": (
            "The tomato leaf appears healthy based on the "
            "AI model prediction."
        ),

        "symptoms": [
            "No major visible disease symptoms detected",
            "Leaf structure appears generally healthy"
        ],

        "management": [
            "Continue normal crop management",
            "Provide adequate water and nutrients",
            "Monitor the plant regularly"
        ],

        "prevention": [
            "Maintain good field sanitation",
            "Use healthy planting materials",
            "Monitor plants regularly"
        ]
    },


    "Tomato_Late_Blight": {

        "name": "Tomato Late Blight",

        "crop": "Tomato",

        "description": (
            "Late Blight is a serious disease that can affect "
            "tomato plants and spread rapidly under favorable "
            "environmental conditions."
        ),

        "symptoms": [
            "Dark or irregular spots on leaves",
            "Rapid browning and death of affected leaf tissue",
            "Dark lesions may appear on stems",
            "Fruit may develop dark, firm lesions"
        ],

        "management": [
            "Remove and properly dispose of severely affected plant material",
            "Avoid unnecessary leaf wetness",
            "Improve air circulation around plants",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Use healthy planting materials",
            "Maintain good field sanitation",
            "Avoid prolonged moisture on leaves",
            "Monitor plants regularly for early symptoms"
        ]
    },


    "Tomato_Leaf_Mold": {

        "name": "Tomato Leaf Mold",

        "crop": "Tomato",

        "description": (
            "Tomato Leaf Mold is a fungal disease that commonly "
            "develops under humid conditions."
        ),

        "symptoms": [
            "Yellowish spots on the upper leaf surface",
            "Olive or grayish fungal growth underneath leaves",
            "Affected leaves may curl",
            "Severe infection may cause leaf drop"
        ],

        "management": [
            "Improve ventilation around plants",
            "Reduce excessive humidity",
            "Remove severely infected leaves",
            "Avoid prolonged leaf wetness"
        ],

        "prevention": [
            "Provide good air circulation",
            "Avoid excessive humidity",
            "Maintain field sanitation",
            "Monitor plants regularly"
        ]
    },


    "Tomato_Septoria_Leaf_Spot": {

        "name": "Tomato Septoria Leaf Spot",

        "crop": "Tomato",

        "description": (
            "Septoria Leaf Spot is a fungal disease that mainly "
            "affects tomato leaves."
        ),

        "symptoms": [
            "Small circular spots on leaves",
            "Spots may have dark borders",
            "Centers may appear gray or tan",
            "Severe infection may cause leaf drop"
        ],

        "management": [
            "Remove infected leaves",
            "Improve air circulation",
            "Avoid overhead watering",
            "Maintain field sanitation"
        ],

        "prevention": [
            "Remove infected plant debris",
            "Practice crop rotation",
            "Avoid prolonged leaf wetness",
            "Monitor plants regularly"
        ]
    },


    "Tomato_Spider_Mites": {

        "name": "Tomato Spider Mites",

        "crop": "Tomato",

        "description": (
            "Spider mites are small pests that feed on plant "
            "tissues and can cause damage to tomato leaves."
        ),

        "symptoms": [
            "Small yellow or pale spots on leaves",
            "Leaves may appear speckled",
            "Fine webbing may be visible",
            "Severe infestation can cause leaf drying"
        ],

        "management": [
            "Inspect plants regularly",
            "Remove heavily affected leaves",
            "Maintain appropriate plant moisture",
            "Use suitable pest management practices"
        ],

        "prevention": [
            "Monitor plants frequently",
            "Maintain healthy plant growth",
            "Remove heavily infested plant material",
            "Control weeds around the crop"
        ]
    },


    "Tomato_Target_Spot": {

        "name": "Tomato Target Spot",

        "crop": "Tomato",

        "description": (
            "Target Spot is a fungal disease that can affect "
            "tomato leaves and fruits."
        ),

        "symptoms": [
            "Circular brown spots on leaves",
            "Concentric rings may create a target-like appearance",
            "Leaves may yellow and fall",
            "Fruit lesions may develop"
        ],

        "management": [
            "Remove severely infected leaves",
            "Improve air circulation",
            "Avoid prolonged leaf wetness",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Maintain good field sanitation",
            "Avoid excessive moisture",
            "Remove infected plant debris",
            "Monitor crops regularly"
        ]
    },


    "Tomato_Yellow_Leaf_Curl_Virus": {

        "name": "Tomato Yellow Leaf Curl Virus",

        "crop": "Tomato",

        "description": (
            "Tomato Yellow Leaf Curl Virus is a viral disease "
            "that can cause severe growth and leaf development "
            "problems in tomato plants."
        ),

        "symptoms": [
            "Yellowing of leaf margins",
            "Upward curling of leaves",
            "Reduced leaf size",
            "Stunted plant growth"
        ],

        "management": [
            "Remove severely affected plants when appropriate",
            "Control insect vectors such as whiteflies",
            "Maintain field sanitation",
            "Monitor plants regularly"
        ],

        "prevention": [
            "Use healthy planting materials",
            "Control whitefly populations",
            "Remove infected plants when appropriate",
            "Maintain good field sanitation"
        ]
    },


    "Tomato_Mosaic_Virus": {

        "name": "Tomato Mosaic Virus",

        "crop": "Tomato",

        "description": (
            "Tomato Mosaic Virus is a viral disease that can "
            "cause characteristic patterns and reduced plant growth."
        ),

        "symptoms": [
            "Mosaic patterns on leaves",
            "Light and dark green patches",
            "Leaf distortion",
            "Reduced plant growth"
        ],

        "management": [
            "Remove severely infected plants",
            "Maintain good sanitation",
            "Avoid spreading plant sap between plants",
            "Use appropriate disease management practices"
        ],

        "prevention": [
            "Use healthy seeds and planting materials",
            "Disinfect tools regularly",
            "Avoid unnecessary plant injury",
            "Maintain good field hygiene"
        ]
    }

}


# ============================================================
# GET DISEASE INFORMATION
# ============================================================

def get_disease_info(disease_key):

    return DISEASE_INFO.get(
        disease_key
    )


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("AYUBA CROP DOCTOR")
    print("DISEASE INFORMATION DATABASE")
    print("=" * 60)

    print(
        f"\nTotal disease classes: "
        f"{len(DISEASE_INFO)}"
    )

    disease = get_disease_info(
        "Tomato_Late_Blight"
    )

    if disease:

        print(
            "\nDisease:",
            disease["name"]
        )

        print(
            "Crop:",
            disease["crop"]
        )

        print(
            "Description:",
            disease["description"]
        )

    print(
        "\nDisease information system ready."
    )