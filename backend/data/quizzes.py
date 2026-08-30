"""
Gamified Quizzes, Picture Identification & Word Match Game Data for Kids
"""

QUIZZES = [
    {
        "id": "quiz_1",
        "question_hi": "संताली (Santhali) भाषा में 'पानी' (Water) को क्या कहते हैं?",
        "options": [
            {"text": "दाः (ᱫᱟᱜ)", "is_correct": True, "explanation": "संताली में 'दाः' का अर्थ पानी या जल होता है!"},
            {"text": "तोवा (ᱛᱳᱣᱟ)", "is_correct": False, "explanation": "'तोवा' का अर्थ दूध होता है।"},
            {"text": "बाहा (ᱵᱟᱦᱟ)", "is_correct": False, "explanation": "'बाहा' का अर्थ फूल होता है।"},
            {"text": "उल (ᱩᱞ)", "is_correct": False, "explanation": "'उल' का अर्थ आम होता है।"}
        ],
        "badge": "⭐ जल सेतु सितारा"
    },
    {
        "id": "quiz_2",
        "question_hi": "मुंडारी (Mundari) और हो (Ho) भाषा में 'नमस्ते / प्रणाम' को क्या कहते हैं?",
        "options": [
            {"text": "जोहार (Johar)", "is_correct": True, "explanation": "शाबाश! 'जोहार' प्रकृति और सभी लोगों के प्रति आदर का प्रतीक अभिवादन है।"},
            {"text": "बाय-बाय", "is_correct": False, "explanation": "यह विदाई का शब्द है।"},
            {"text": "मंडी", "is_correct": False, "explanation": "'मंडी' का अर्थ भात/खाना होता है।"},
            {"text": "दारु", "is_correct": False, "explanation": "'दारु' का अर्थ पेड़ होता है।"}
        ],
        "badge": "🌟 जोहार मास्टर"
    },
    {
        "id": "quiz_3",
        "question_hi": "नागपुरी (Nagpuri) और खोरठा में 'माँ' को प्यार से क्या पुकारते हैं?",
        "options": [
            {"text": "माय (Maay)", "is_correct": True, "explanation": "बिलकुल सही! 'माय' बहुत ही प्यारा और आदरसूचक शब्द है।"},
            {"text": "संगी", "is_correct": False, "explanation": "'संगी' का अर्थ दोस्त/मित्र होता है।"},
            {"text": "छौआ", "is_correct": False, "explanation": "'छौआ' का अर्थ बच्चा होता है।"},
            {"text": "गाते", "is_correct": False, "explanation": "'गाते' का अर्थ मित्र होता है।"}
        ],
        "badge": "💖 परिवार रत्न"
    },
    {
        "id": "quiz_4",
        "question_hi": "संताली भाषा की अपनी प्रसिद्ध लिपि का क्या नाम है?",
        "options": [
            {"text": "ओल चिकी (Ol Chiki)", "is_correct": True, "explanation": "अद्भुत! ओल चिकी लिपि का आविष्कार पंडित रघुनाथ मुर्मू जी ने किया था।"},
            {"text": "रोमन लिपि", "is_correct": False, "explanation": "यह अंग्रेजी की लिपि है।"},
            {"text": "देवनागरी", "is_correct": False, "explanation": "यह हिंदी की मुख्य लिपि है।"},
            {"text": "ब्राह्मी", "is_correct": False, "explanation": "यह एक प्राचीन लिपि है।"}
        ],
        "badge": "📜 लिपि ज्ञानी"
    },
    {
        "id": "quiz_5",
        "question_hi": "कुड़ुख़ (Kurukh) भाषा में 'घर' या 'पक्षी' के लिए कौन सा शब्द आता है?",
        "options": [
            {"text": "ओड़ा (Or'a - चिड़िया)", "is_correct": True, "explanation": "बहुत खूब! कुड़ुख़ में 'ओड़ा' चिड़िया/पक्षी को कहते हैं।"},
            {"text": "अल्ला", "is_correct": False, "explanation": "'अल्ला' का अर्थ कुत्ता होता है।"},
            {"text": "इंजो", "is_correct": False, "explanation": "'इंजो' का अर्थ मछली होता है।"},
            {"text": "पुंप", "is_correct": False, "explanation": "'पुंप' का अर्थ फूल होता है।"}
        ],
        "badge": "🦜 प्रकृति मित्र"
    }
]

MATCH_GAMES = [
    {
        "id": "match_animals",
        "title": "पशु-पक्षियों का मिलान (Animals Match)",
        "language": "santhali",
        "lang_name": "संताली (Santhali)",
        "pairs": [
            {"hi": "हाथी 🐘", "target": "ᱦᱟᱹᱛᱤ (हाथीः)"},
            {"hi": "मोर 🦚", "target": "ᱢᱟᱨᱟᱜ (माराः)"},
            {"hi": "कुत्ता 🐕", "target": "ᱥᱮᱛᱟ (सेता)"},
            {"hi": "बिल्ली 🐱", "target": "ᱯᱩᱥᱤ (पुसी)"},
            {"hi": "मछली 🐟", "target": "ᱦᱟᱹᱠᱩ (हाकु)"}
        ]
    },
    {
        "id": "match_numbers",
        "title": "गिनती का खेल (Numbers Match)",
        "language": "mundari",
        "lang_name": "मुंडारी (Mundari)",
        "pairs": [
            {"hi": "एक (1)", "target": "मियाद (Miyad)"},
            {"hi": "दो (2)", "target": "बारिया (Bariya)"},
            {"hi": "तीन (3)", "target": "आपि (Aapi)"},
            {"hi": "चार (4)", "target": "उपून (Upun)"},
            {"hi": "पाँच (5)", "target": "मोड़े (More)"}
        ]
    },
    {
        "id": "match_colors",
        "title": "रंगों की पहचान (Colors Match)",
        "language": "nagpuri",
        "lang_name": "नागपुरी (Nagpuri)",
        "pairs": [
            {"hi": "लाल 🔴", "target": "ललका (Lalka)"},
            {"hi": "हरा 🟢", "target": "हरियर (Hariyar)"},
            {"hi": "पीला 🟡", "target": "पियरा (Piyara)"},
            {"hi": "सफेद ⚪", "target": "उज्जर / चरका (Ujjar)"},
            {"hi": "काला ⚫", "target": "करिया (Kariya)"}
        ]
    }
]
