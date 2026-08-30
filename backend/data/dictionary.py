"""
Comprehensive Multilingual Dictionary & Phrasebook for BhashaSetu
Covers Hindi -> 5 Tribal + 4 Regional Languages across 12 child-friendly categories.
"""

CATEGORIES = [
    {"id": "greetings", "name_hi": "नमस्ते और शिष्टाचार", "name_en": "Greetings & Polite Words", "emoji": "🙏"},
    {"id": "family", "name_hi": "परिवार और रिश्ते", "name_en": "Family & Relations", "emoji": "👨‍👩‍👧‍👦"},
    {"id": "animals", "name_hi": "पशु और पक्षी", "name_en": "Animals & Birds", "emoji": "🐘"},
    {"id": "nature", "name_hi": "प्रकृति और वातावरण", "name_en": "Nature & Environment", "emoji": "🌲"},
    {"id": "food", "name_hi": "फल, खाना और पानी", "name_en": "Food, Fruits & Water", "emoji": "🥭"},
    {"id": "numbers", "name_hi": "गिनती (संख्याएँ)", "name_en": "Numbers & Counting", "emoji": "🔢"},
    {"id": "colors", "name_hi": "रंग-बिरंगे रंग", "name_en": "Colors", "emoji": "🎨"},
    {"id": "body", "name_hi": "शरीर के अंग", "name_en": "Body Parts", "emoji": "👀"},
    {"id": "actions", "name_hi": "दैनिक क्रियाएँ (खेलना-कूदना)", "name_en": "Daily Actions & Verbs", "emoji": "🏃"},
    {"id": "school", "name_hi": "स्कूल और खेल-खिलौने", "name_en": "School & Toys", "emoji": "🎒"},
    {"id": "feelings", "name_hi": "भावनाएँ और तारीफ", "name_en": "Feelings & Emotions", "emoji": "😊"},
    {"id": "phrases", "name_hi": "प्यारी-प्यारी बातें (वाक्य)", "name_en": "Daily Phrases & Sentences", "emoji": "💬"}
]

VOCABULARY = [
    # --- 1. GREETINGS & POLITE WORDS ---
    {
        "id": "greet_hello",
        "category": "greetings",
        "hindi": "नमस्ते / जोहार",
        "emoji": "🙏",
        "translations": {
            "santhali": {"dev": "जोहार", "native": "ᱡᱚᱦᱟᱨ", "phonetic": "Johar"},
            "mundari": {"dev": "जोहार", "phonetic": "Johar"},
            "ho": {"dev": "जोहार", "native": "𑢪𑣉𑢦𑢬𑣂", "phonetic": "Johar"},
            "kurukh": {"dev": "गोड़े / जोहार", "native": "ᱛᱚᱞᱚᱝ", "phonetic": "Godey / Johar"},
            "kharia": {"dev": "जोहार", "phonetic": "Johar"},
            "khortha": {"dev": "प्रनाम / जोहार", "phonetic": "Pranam / Johar"},
            "nagpuri": {"dev": "जोहार / पायलागी", "phonetic": "Johar / Paylagi"},
            "panchpargania": {"dev": "जोहार / नमस्कार", "phonetic": "Johar / Namaskar"},
            "kurmali": {"dev": "जोहार / पांय लागों", "phonetic": "Johar / Pay Lagon"}
        }
    },
    {
        "id": "greet_how_are_you",
        "category": "greetings",
        "hindi": "आप कैसे हैं? / तुम कैसे हो?",
        "emoji": "🤝",
        "translations": {
            "santhali": {"dev": "चेत लेका मेनामा?", "native": "ᱪᱮᱫ ᱞᱮᱠᱟ ᱢᱮᱱᱟᱢᱟ?", "phonetic": "Chet leka menama?"},
            "mundari": {"dev": "चिल्के मेनामा?", "phonetic": "Chilke menama?"},
            "ho": {"dev": "चिलके मेनामा?", "native": "𑢔𑢫𑢵 𑢬𑣂𑢶𑣁?", "phonetic": "Chilke menama?"},
            "kurukh": {"dev": "एकासे रअदय?", "native": "ᱮᱠᱟᱥᱮ ᱨᱟᱫᱟᱭ", "phonetic": "Ekase ra'aday?"},
            "kharia": {"dev": "हानी चिलके आसर?", "phonetic": "Hani chilke aasar?"},
            "khortha": {"dev": "तोहे केसन आहा? / कइसन छही?", "phonetic": "Tohe kesan aaha?"},
            "nagpuri": {"dev": "रउरे कइसन अही? / तोय कइसन अहिस?", "phonetic": "Raure kaisan ahi?"},
            "panchpargania": {"dev": "तहार कइसन आहा?", "phonetic": "Tahar kaisan aaha?"},
            "kurmali": {"dev": "तँय कइसन आहीस?", "phonetic": "Tany kaisan aahis?"}
        }
    },
    {
        "id": "greet_i_am_fine",
        "category": "greetings",
        "hindi": "मैं ठीक हूँ / मैं अच्छा हूँ",
        "emoji": "👍",
        "translations": {
            "santhali": {"dev": "इञ दो बोगी गे मेनाञा", "native": "ᱤᱧ ᱫᱚ ᱵᱳᱜᱤ ᱜᱮ ᱢᱮᱱᱟᱧᱟ", "phonetic": "Inj do bogi ge menanja"},
            "mundari": {"dev": "ऐंग बुगिन गे मेनाइंगा", "phonetic": "Aing bugin ge menainga"},
            "ho": {"dev": "ऐंग बोगी गे मेनेया", "native": "𑢠𑣂𑢵 𑢲𑣉𑢬𑣂 𑢶𑣂", "phonetic": "Aing bogi ge meneya"},
            "kurukh": {"dev": "एन बेस रअदन", "native": "ᱮᱱ ᱵᱮᱥ ᱨᱟᱫᱟᱱ", "phonetic": "En bes ra'adan"},
            "kharia": {"dev": "इञ बेस आञ", "phonetic": "Inj bes aanj"},
            "khortha": {"dev": "हम बेस हियो / हम ठीक छी", "phonetic": "Ham bes hiyo"},
            "nagpuri": {"dev": "हम बेस अही / हम ठीक छी", "phonetic": "Ham bes ahi"},
            "panchpargania": {"dev": "हम बेस आहि", "phonetic": "Ham bes aahi"},
            "kurmali": {"dev": "हम बेस आही", "phonetic": "Ham bes aahi"}
        }
    },
    {
        "id": "greet_thank_you",
        "category": "greetings",
        "hindi": "धन्यवाद / शुक्रिया",
        "emoji": "💐",
        "translations": {
            "santhali": {"dev": "सराहना / जोहार", "native": "ᱥᱟᱨᱦᱟᱣ", "phonetic": "Sarhaw / Johar"},
            "mundari": {"dev": "सराहाओ / धनबाद", "phonetic": "Sarahao"},
            "ho": {"dev": "सराहाओ / जोहार", "native": "𑢺𑣗𑢸𑢦𑣉", "phonetic": "Sarahao"},
            "kurukh": {"dev": "सुकरिया / गोड़े", "native": "ᱥᱩᱠᱨᱤᱭᱟ", "phonetic": "Sukariya"},
            "kharia": {"dev": "सराहना", "phonetic": "Sarahna"},
            "khortha": {"dev": "धनबाद / बेस बात", "phonetic": "Dhanbaad"},
            "nagpuri": {"dev": "धन्यबाद / बेस लगलक", "phonetic": "Dhanyabaad"},
            "panchpargania": {"dev": "धन्यबाद", "phonetic": "Dhanyabaad"},
            "kurmali": {"dev": "धनबाद", "phonetic": "Dhanbaad"}
        }
    },
    {
        "id": "greet_welcome",
        "category": "greetings",
        "hindi": "स्वागत है / आइए",
        "emoji": "🤗",
        "translations": {
            "santhali": {"dev": "दाराम / हिजूः मे", "native": "ᱫᱟᱨᱟᱢ", "phonetic": "Daram / Hijuh me"},
            "mundari": {"dev": "हिजुपे / जोहार", "phonetic": "Hijupe"},
            "ho": {"dev": "हिजुमे / दारोम", "native": "𑢹𑣂𑢪𑣁 𑢶𑣂", "phonetic": "Hijume"},
            "kurukh": {"dev": "बरआ / पाहीं", "native": "ᱵᱟᱨᱟ", "phonetic": "Bar'a"},
            "kharia": {"dev": "आवा / दारोम", "phonetic": "Aawa"},
            "khortha": {"dev": "आवा-आवा / स्वागत हे", "phonetic": "Aawa aawa"},
            "nagpuri": {"dev": "आउब / स्वागत हे", "phonetic": "Aaub / Swagat he"},
            "panchpargania": {"dev": "आसुक / स्वागत", "phonetic": "Aasuk"},
            "kurmali": {"dev": "आउक / स्वागत", "phonetic": "Aauk"}
        }
    },

    # --- 2. FAMILY & RELATIONS ---
    {
        "id": "fam_mother",
        "category": "family",
        "hindi": "माँ / माताजी",
        "emoji": "👩",
        "translations": {
            "santhali": {"dev": "आयो / एंगा", "native": "ᱟᱭᱳ", "phonetic": "Ayo / Enga"},
            "mundari": {"dev": "एंगा / माय", "phonetic": "Enga / Maay"},
            "ho": {"dev": "एंगा / माय", "native": "𑢣𑢵𑢬𑣁", "phonetic": "Enga"},
            "kurukh": {"dev": "अयंग / इयो", "native": "ᱟᱭᱟᱝ", "phonetic": "Ayang / Iyo"},
            "kharia": {"dev": "मा / माई", "phonetic": "Maa / Maai"},
            "khortha": {"dev": "माय / माई", "phonetic": "Maay"},
            "nagpuri": {"dev": "माय / आयो", "phonetic": "Maay / Aayo"},
            "panchpargania": {"dev": "माय / माँ", "phonetic": "Maay"},
            "kurmali": {"dev": "माय / माई", "phonetic": "Maay"}
        }
    },
    {
        "id": "fam_father",
        "category": "family",
        "hindi": "पिताजी / बाबा / पापा",
        "emoji": "👨",
        "translations": {
            "santhali": {"dev": "बाबा / आपा", "native": "ᱵᱟᱵᱟ", "phonetic": "Baba / Apa"},
            "mundari": {"dev": "अपु / बाबा", "phonetic": "Apu / Baba"},
            "ho": {"dev": "अपु / बाबा", "native": "𑢠𑢱𑣁", "phonetic": "Apu / Baba"},
            "kurukh": {"dev": "तम्बस / बाबा", "native": "ᱛᱟᱢᱵᱟᱥ", "phonetic": "Tambas / Baba"},
            "kharia": {"dev": "अप्पा / बाबा", "phonetic": "Appa / Baba"},
            "khortha": {"dev": "बाप / बाबुजी / बाबा", "phonetic": "Baap / Babuji"},
            "nagpuri": {"dev": "बाप / बाबा / आबा", "phonetic": "Baap / Baba"},
            "panchpargania": {"dev": "बाप / बापू", "phonetic": "Baap / Bapu"},
            "kurmali": {"dev": "बाप / बाबाजी", "phonetic": "Baap / Babaji"}
        }
    },
    {
        "id": "fam_brother",
        "category": "family",
        "hindi": "भाई / भैया",
        "emoji": "👦",
        "translations": {
            "santhali": {"dev": "बोयहा / दादा / बोको", "native": "ᱵᱚᱭᱦᱟ", "phonetic": "Boyha / Dada"},
            "mundari": {"dev": "हागा / बोको", "phonetic": "Haga / Boko"},
            "ho": {"dev": "हागा / दादा", "native": "𑢹𑣁𑢬𑣁", "phonetic": "Haga"},
            "kurukh": {"dev": "भय्या / दादा", "native": "ᱫᱟᱫᱟ", "phonetic": "Dada / Bhayya"},
            "kharia": {"dev": "बोको / दादा", "phonetic": "Boko / Dada"},
            "khortha": {"dev": "भाई / दादा / भाइया", "phonetic": "Bhai / Dada"},
            "nagpuri": {"dev": "भाई / दादा / भइया", "phonetic": "Bhai / Dada"},
            "panchpargania": {"dev": "भाई / दादा", "phonetic": "Bhai / Dada"},
            "kurmali": {"dev": "भाई / दादा", "phonetic": "Bhai / Dada"}
        }
    },
    {
        "id": "fam_sister",
        "category": "family",
        "hindi": "बहन / दीदी",
        "emoji": "👧",
        "translations": {
            "santhali": {"dev": "मिसि / दाई", "native": "ᱢᱤᱥᱤ", "phonetic": "Misi / Daai"},
            "mundari": {"dev": "मिसि / दाई", "phonetic": "Misi / Daai"},
            "ho": {"dev": "मिसि / दाई", "native": "𑢷𑣂𑢺𑣂", "phonetic": "Misi / Daai"},
            "kurukh": {"dev": "दई / बहिन", "native": "ᱫᱟᱭ", "phonetic": "Dai / Bahin"},
            "kharia": {"dev": "मिसि / दाई", "phonetic": "Misi / Daai"},
            "khortha": {"dev": "बहिन / दीदी / दीदीजी", "phonetic": "Bahin / Didi"},
            "nagpuri": {"dev": "बहिन / दीदी / दाई", "phonetic": "Bahin / Didi"},
            "panchpargania": {"dev": "बहिन / दीदी", "phonetic": "Bahin / Didi"},
            "kurmali": {"dev": "बहिन / दीदी", "phonetic": "Bahin / Didi"}
        }
    },
    {
        "id": "fam_child",
        "category": "family",
        "hindi": "बच्चा / नन्हा बच्चा",
        "emoji": "👶",
        "translations": {
            "santhali": {"dev": "गिदरा / होन", "native": "ᱜᱤᱫᱽᱨᱟᱹ", "phonetic": "Gidra / Hon"},
            "mundari": {"dev": "होन / गिदरा", "phonetic": "Hon / Gidra"},
            "ho": {"dev": "होन / लेड़का", "native": "𑢹𑣉𑢳", "phonetic": "Hon"},
            "kurukh": {"dev": "खद्द / कुँवर", "native": "ᱠᱷᱟᱫᱽᱫ", "phonetic": "Khadd"},
            "kharia": {"dev": "कनसुवा / छौआ", "phonetic": "Kansuwa / Chhoua"},
            "khortha": {"dev": "छौआ / गीदर / नूनू", "phonetic": "Chhoua / Geedar / Nunu"},
            "nagpuri": {"dev": "छौआ / नूनू / बच्चा", "phonetic": "Chhoua / Nunu"},
            "panchpargania": {"dev": "छौआ / नूनू", "phonetic": "Chhoua / Nunu"},
            "kurmali": {"dev": "छौआ / गीदर", "phonetic": "Chhoua / Geedar"}
        }
    },
    {
        "id": "fam_friend",
        "category": "family",
        "hindi": "दोस्त / मित्र / सखा",
        "emoji": "🧒🤝👧",
        "translations": {
            "santhali": {"dev": "गाते / संगी", "native": "ᱜᱟᱛᱮ", "phonetic": "Gate / Sangi"},
            "mundari": {"dev": "जोटा / गाते", "phonetic": "Jota / Gate"},
            "ho": {"dev": "जोटा / संगी", "native": "𑢪𑣉𑢵𑣁", "phonetic": "Jota / Sangi"},
            "kurukh": {"dev": "संगी / जोटा", "native": "ᱥᱟᱝᱜᱤ", "phonetic": "Sangi"},
            "kharia": {"dev": "जोटा / संगी", "phonetic": "Jota / Sangi"},
            "khortha": {"dev": "संगी / मीत / जोहारू", "phonetic": "Sangi / Meet"},
            "nagpuri": {"dev": "संगी / जोहारू / मीत", "phonetic": "Sangi / Meet"},
            "panchpargania": {"dev": "संगी / मीत", "phonetic": "Sangi / Meet"},
            "kurmali": {"dev": "संगी / साथी / मीत", "phonetic": "Sangi / Sathi"}
        }
    },

    # --- 3. ANIMALS & BIRDS ---
    {
        "id": "anim_elephant",
        "category": "animals",
        "hindi": "हाथी",
        "emoji": "🐘",
        "translations": {
            "santhali": {"dev": "हाथी / हाथी (हाथीः)", "native": "ᱦᱟᱹᱛᱤ", "phonetic": "Hathi"},
            "mundari": {"dev": "हाती", "phonetic": "Hati"},
            "ho": {"dev": "हाती", "native": "𑢹𑣁𑢵𑣂", "phonetic": "Hati"},
            "kurukh": {"dev": "हाथी / अत्ति", "native": "ᱦᱟᱛᱷᱤ", "phonetic": "Hathi / Atti"},
            "kharia": {"dev": "हाती", "phonetic": "Hati"},
            "khortha": {"dev": "हाथी", "phonetic": "Hathi"},
            "nagpuri": {"dev": "हाथी / हठी", "phonetic": "Hathi"},
            "panchpargania": {"dev": "हाथी", "phonetic": "Hathi"},
            "kurmali": {"dev": "हाथी", "phonetic": "Hathi"}
        }
    },
    {
        "id": "anim_peacock",
        "category": "animals",
        "hindi": "मोर (मयूर)",
        "emoji": "🦚",
        "translations": {
            "santhali": {"dev": "माराः", "native": "ᱢᱟᱨᱟᱜ", "phonetic": "Marag"},
            "mundari": {"dev": "माराः", "phonetic": "Marag"},
            "ho": {"dev": "माराः", "native": "𑢷𑣁𑢸𑣁𑢬", "phonetic": "Marag"},
            "kurukh": {"dev": "मंजुर / मोर", "native": "ᱢᱟᱧᱡᱩᱨ", "phonetic": "Manjur"},
            "kharia": {"dev": "माराः", "phonetic": "Marag"},
            "khortha": {"dev": "मंजूर / मोर", "phonetic": "Manjoor / Mor"},
            "nagpuri": {"dev": "मंजुर / मोर", "phonetic": "Manjur / Mor"},
            "panchpargania": {"dev": "मंजुर / मोर", "phonetic": "Manjur"},
            "kurmali": {"dev": "मंजुर / मोर", "phonetic": "Manjur / Mor"}
        }
    },
    {
        "id": "anim_cow",
        "category": "animals",
        "hindi": "गाय (गौमाता)",
        "emoji": "🐄",
        "translations": {
            "santhali": {"dev": "गाई / काडा", "native": "ᱜᱟᱹᱭ", "phonetic": "Gaai"},
            "mundari": {"dev": "गूरी / गाई", "phonetic": "Guri / Gaai"},
            "ho": {"dev": "गाई", "native": "𑢬𑣁𑢠𑣂", "phonetic": "Gaai"},
            "kurukh": {"dev": "ओय / गाय", "native": "ᱚᱭ", "phonetic": "Oy / Gaay"},
            "kharia": {"dev": "गाई", "phonetic": "Gaai"},
            "khortha": {"dev": "गाई / गरु", "phonetic": "Gaai / Garu"},
            "nagpuri": {"dev": "गाई / गरु", "phonetic": "Gaai / Garu"},
            "panchpargania": {"dev": "गाई", "phonetic": "Gaai"},
            "kurmali": {"dev": "गाई / गरु", "phonetic": "Gaai / Garu"}
        }
    },
    {
        "id": "anim_dog",
        "category": "animals",
        "hindi": "कुत्ता",
        "emoji": "🐕",
        "translations": {
            "santhali": {"dev": "सेता", "native": "ᱥᱮᱛᱟ", "phonetic": "Seta"},
            "mundari": {"dev": "सेता", "phonetic": "Seta"},
            "ho": {"dev": "सेता", "native": "𑢺𑣂𑢵𑣁", "phonetic": "Seta"},
            "kurukh": {"dev": "अल्ला", "native": "ᱟᱞᱞᱟ", "phonetic": "Alla"},
            "kharia": {"dev": "सोरलो / कुत्ता", "phonetic": "Sorlo / Kutta"},
            "khortha": {"dev": "कुकुर / कुत्ता", "phonetic": "Kukur"},
            "nagpuri": {"dev": "कुकुर", "phonetic": "Kukur"},
            "panchpargania": {"dev": "कुकुर", "phonetic": "Kukur"},
            "kurmali": {"dev": "कुकुर", "phonetic": "Kukur"}
        }
    },
    {
        "id": "anim_cat",
        "category": "animals",
        "hindi": "बिल्ली / बिलौटा",
        "emoji": "🐱",
        "translations": {
            "santhali": {"dev": "पुसी", "native": "ᱯᱩᱥᱤ", "phonetic": "Pusi"},
            "mundari": {"dev": "पुसी", "phonetic": "Pusi"},
            "ho": {"dev": "पुसी", "native": "𑢱𑣁𑢺𑣂", "phonetic": "Pusi"},
            "kurukh": {"dev": "बिरखी / पुसी", "native": "ᱵᱤᱨᱠᱷᱤ", "phonetic": "Birkhi / Pusi"},
            "kharia": {"dev": "पुसी", "phonetic": "Pusi"},
            "khortha": {"dev": "बिलाई / बिलाय", "phonetic": "Bilaai"},
            "nagpuri": {"dev": "बिलाई / बिलाय", "phonetic": "Bilaai"},
            "panchpargania": {"dev": "बिलाई", "phonetic": "Bilaai"},
            "kurmali": {"dev": "बिलाय / बिलाई", "phonetic": "Bilaay"}
        }
    },
    {
        "id": "anim_tiger",
        "category": "animals",
        "hindi": "बाघ / शेर",
        "emoji": "🐯",
        "translations": {
            "santhali": {"dev": "तारुप / कुल", "native": "ᱛᱟᱹᱨᱩᱵ", "phonetic": "Tarup / Kul"},
            "mundari": {"dev": "कुल / बुरु कुल", "phonetic": "Kul / Buru Kul"},
            "ho": {"dev": "कुल", "native": "𑢫𑣁𑢹", "phonetic": "Kul"},
            "kurukh": {"dev": "लक्खा / बघवा", "native": "ᱞᱟᱠᱷᱟ", "phonetic": "Lakkha / Baghwa"},
            "kharia": {"dev": "किरोंग / बाघ", "phonetic": "Kirong / Bagh"},
            "khortha": {"dev": "बाघ / बाघवा", "phonetic": "Bagh / Baghwa"},
            "nagpuri": {"dev": "बाघ / बघवा", "phonetic": "Bagh / Baghwa"},
            "panchpargania": {"dev": "बाघ", "phonetic": "Bagh"},
            "kurmali": {"dev": "बाघ / बाघवा", "phonetic": "Bagh"}
        }
    },
    {
        "id": "anim_bird",
        "category": "animals",
        "hindi": "चिड़िया / पक्षी",
        "emoji": "🐦",
        "translations": {
            "santhali": {"dev": "चेँड़े", "native": "ᱪᱮᱬᱮ", "phonetic": "Chenre"},
            "mundari": {"dev": "चेणे", "phonetic": "Chene"},
            "ho": {"dev": "चेणे", "native": "𑢔𑢫𑢳𑣂", "phonetic": "Chene"},
            "kurukh": {"dev": "ओड़ा / चिरई", "native": "ᱚᱲᱟ", "phonetic": "Or'a / Chirai"},
            "kharia": {"dev": "ओरते / चिंरई", "phonetic": "Orte / Chirai"},
            "khortha": {"dev": "चिरई / पंछी", "phonetic": "Chirai"},
            "nagpuri": {"dev": "चिरई / चरई", "phonetic": "Chirai / Charai"},
            "panchpargania": {"dev": "चिरई", "phonetic": "Chirai"},
            "kurmali": {"dev": "चिरई / पाखी", "phonetic": "Chirai / Pakhi"}
        }
    },
    {
        "id": "anim_fish",
        "category": "animals",
        "hindi": "मछली / मीन",
        "emoji": "🐟",
        "translations": {
            "santhali": {"dev": "हाकु", "native": "ᱦᱟᱹᱠᱩ", "phonetic": "Haku"},
            "mundari": {"dev": "हाकु", "phonetic": "Haku"},
            "ho": {"dev": "हाकु", "native": "𑢹𑣁𑢫𑣁", "phonetic": "Haku"},
            "kurukh": {"dev": "इंजो", "native": "ᱤᱧᱡᱳ", "phonetic": "Injo"},
            "kharia": {"dev": "कादो / हाकु", "phonetic": "Kado / Haku"},
            "khortha": {"dev": "माछ / मछली", "phonetic": "Machh"},
            "nagpuri": {"dev": "मछरी / माछ", "phonetic": "Machhari / Machh"},
            "panchpargania": {"dev": "माछ / मछली", "phonetic": "Machh"},
            "kurmali": {"dev": "माछ / माछी", "phonetic": "Machh"}
        }
    },
    {
        "id": "anim_butterfly",
        "category": "animals",
        "hindi": "तितली",
        "emoji": "🦋",
        "translations": {
            "santhali": {"dev": "पिपिड़ींञ", "native": "ᱯᱤᱯᱤᱲᱤᱧ", "phonetic": "Pipirinj"},
            "mundari": {"dev": "पिपिरबोंग", "phonetic": "Pipirbong"},
            "ho": {"dev": "पिपिरबोंग", "native": "𑢱𑣂𑢱𑣂𑢸", "phonetic": "Pipirbong"},
            "kurukh": {"dev": "भँवरो / पपली", "native": "ᱯᱟᱯᱞᱤ", "phonetic": "Papli / Bhanwro"},
            "kharia": {"dev": "पिपिरबोंग", "phonetic": "Pipirbong"},
            "khortha": {"dev": "तितली / फुदकी", "phonetic": "Titli / Phudki"},
            "nagpuri": {"dev": "तितली / भँवरी", "phonetic": "Titli"},
            "panchpargania": {"dev": "तितली", "phonetic": "Titli"},
            "kurmali": {"dev": "तितली / पखिया", "phonetic": "Titli"}
        }
    },

    # --- 4. NATURE & ENVIRONMENT ---
    {
        "id": "nat_sun",
        "category": "nature",
        "hindi": "सूरज / सूर्यदेव",
        "emoji": "☀️",
        "translations": {
            "santhali": {"dev": "सिंघी / बेड़ा", "native": "ᱥᱤᱧ ᱪᱟᱸᱫᱳ", "phonetic": "Singi / Sin Chando"},
            "mundari": {"dev": "सिंगी", "phonetic": "Singi"},
            "ho": {"dev": "सिंगी", "native": "𑢺𑣂𑢵𑢬𑣂", "phonetic": "Singi"},
            "kurukh": {"dev": "बिड़ी / बेड़ा", "native": "ᱵᱤᱲᱤ", "phonetic": "Biri / Bera"},
            "kharia": {"dev": "बेर", "phonetic": "Ber"},
            "khortha": {"dev": "सुरुज / बेरा", "phonetic": "Suruj / Bera"},
            "nagpuri": {"dev": "सुरुज / सुरुज देव", "phonetic": "Suruj"},
            "panchpargania": {"dev": "सुरुज / बेरा", "phonetic": "Suruj / Bera"},
            "kurmali": {"dev": "सुरुज / बेरा", "phonetic": "Suruj / Bera"}
        }
    },
    {
        "id": "nat_moon",
        "category": "nature",
        "hindi": "चाँद / चंदा मामा",
        "emoji": "🌙",
        "translations": {
            "santhali": {"dev": "ञिंदा चांदो", "native": "ᱧᱤᱫᱟᱹ ᱪᱟᱸᱫᱳ", "phonetic": "Nyinda Chando"},
            "mundari": {"dev": "चांदु", "phonetic": "Chandu"},
            "ho": {"dev": "चांदु", "native": "𑢔𑢫𑢵𑢶𑣁", "phonetic": "Chandu"},
            "kurukh": {"dev": "चन्दो", "native": "ᱪᱟᱱᱫᱳ", "phonetic": "Chando"},
            "kharia": {"dev": "चांदु", "phonetic": "Chandu"},
            "khortha": {"dev": "चाँद / चनवा मामा", "phonetic": "Chand / Chanwa"},
            "nagpuri": {"dev": "चाँद / चंदा मामा", "phonetic": "Chand / Chanda Mama"},
            "panchpargania": {"dev": "चाँद / चंदा", "phonetic": "Chand"},
            "kurmali": {"dev": "चाँद / चंदा मामा", "phonetic": "Chand / Chanda Mama"}
        }
    },
    {
        "id": "nat_tree",
        "category": "nature",
        "hindi": "पेड़ / वृक्ष",
        "emoji": "🌳",
        "translations": {
            "santhali": {"dev": "दारे", "native": "ᱫᱟᱨᱮ", "phonetic": "Dare"},
            "mundari": {"dev": "दारु", "phonetic": "Daru"},
            "ho": {"dev": "दारु", "native": "𑢶𑣁𑢸𑣁", "phonetic": "Daru"},
            "kurukh": {"dev": "मन", "native": "ᱢᱟᱱ", "phonetic": "Man"},
            "kharia": {"dev": "दारु", "phonetic": "Daru"},
            "khortha": {"dev": "गाछ / बिरिछ", "phonetic": "Gaachh / Birichh"},
            "nagpuri": {"dev": "गाछ / गछिया / पेड़", "phonetic": "Gaachh / Gachhiya"},
            "panchpargania": {"dev": "गाछ / रुख", "phonetic": "Gaachh / Rukh"},
            "kurmali": {"dev": "गाछ / रुख", "phonetic": "Gaachh / Rukh"}
        }
    },
    {
        "id": "nat_water",
        "category": "nature",
        "hindi": "पानी / जल",
        "emoji": "💧",
        "translations": {
            "santhali": {"dev": "दाः", "native": "ᱫᱟᱜ", "phonetic": "Daag / Dah"},
            "mundari": {"dev": "दाः", "phonetic": "Dah"},
            "ho": {"dev": "दाः", "native": "𑢶𑣁𑢬", "phonetic": "Dah"},
            "kurukh": {"dev": "अम्म", "native": "ᱟᱢᱢ", "phonetic": "Amm"},
            "kharia": {"dev": "दाः", "phonetic": "Dah"},
            "khortha": {"dev": "पानी / जल", "phonetic": "Paani"},
            "nagpuri": {"dev": "पानी / जल", "phonetic": "Paani"},
            "panchpargania": {"dev": "पानी / जल", "phonetic": "Paani"},
            "kurmali": {"dev": "पानी / जल", "phonetic": "Paani"}
        }
    },
    {
        "id": "nat_flower",
        "category": "nature",
        "hindi": "फूल / पुष्प",
        "emoji": "🌸",
        "translations": {
            "santhali": {"dev": "बाहा", "native": "ᱵᱟᱦᱟ", "phonetic": "Baha"},
            "mundari": {"dev": "बा", "phonetic": "Baa"},
            "ho": {"dev": "बा", "native": "𑢲𑣁", "phonetic": "Baa"},
            "kurukh": {"dev": "पुंप", "native": "ᱯᱩᱢᱯ", "phonetic": "Pump"},
            "kharia": {"dev": "बा", "phonetic": "Baa"},
            "khortha": {"dev": "फूल / फूलवा", "phonetic": "Phool / Phoolwa"},
            "nagpuri": {"dev": "फूल / फूलवा", "phonetic": "Phool"},
            "panchpargania": {"dev": "फूल", "phonetic": "Phool"},
            "kurmali": {"dev": "फूल / फूलवा", "phonetic": "Phool"}
        }
    },
    {
        "id": "nat_mountain",
        "category": "nature",
        "hindi": "पहाड़ / पर्वत",
        "emoji": "⛰️",
        "translations": {
            "santhali": {"dev": "बुरु", "native": "ᱵᱩᱨᱩ", "phonetic": "Buru"},
            "mundari": {"dev": "बुरु", "phonetic": "Buru"},
            "ho": {"dev": "बुरु", "native": "𑢲𑣁𑢸𑣁", "phonetic": "Buru"},
            "kurukh": {"dev": "पार्ट / टोंगरी", "native": "ᱴᱳᱝᱨᱤ", "phonetic": "Part / Tongri"},
            "kharia": {"dev": "बुरु", "phonetic": "Buru"},
            "khortha": {"dev": "पहाड़ / टोंगरी / डूंगरी", "phonetic": "Pahar / Tongri"},
            "nagpuri": {"dev": "पहाड़ / टोंगरी / डूंगरी", "phonetic": "Pahar / Tongri"},
            "panchpargania": {"dev": "पहाड़ / डूंगरी", "phonetic": "Pahar / Dungri"},
            "kurmali": {"dev": "पहाड़ / टोंगरी", "phonetic": "Pahar / Tongri"}
        }
    },
    {
        "id": "nat_rain",
        "category": "nature",
        "hindi": "बारिश / वर्षा",
        "emoji": "🌧️",
        "translations": {
            "santhali": {"dev": "दाः जाड़ी", "native": "ᱫᱟᱜ ᱡᱟᱹᱲᱤ", "phonetic": "Daag Jari"},
            "mundari": {"dev": "दाः जामा", "phonetic": "Daah Jama"},
            "ho": {"dev": "दाः जाड़ी", "native": "𑢶𑣁𑢬 𑢪𑣁𑢸𑣂", "phonetic": "Dah Jari"},
            "kurukh": {"dev": "छिटा / पूस पूस", "native": "ᱯᱩᱥ", "phonetic": "Chhita / Barasa"},
            "kharia": {"dev": "दाः जाड़ी", "phonetic": "Dah Jari"},
            "khortha": {"dev": "बरखा / पानी / झड़ी", "phonetic": "Barkha / Paani"},
            "nagpuri": {"dev": "बरखा / झड़ी / पानी", "phonetic": "Barkha / Jhari"},
            "panchpargania": {"dev": "बरखा / पानी", "phonetic": "Barkha"},
            "kurmali": {"dev": "बरखा / पानी", "phonetic": "Barkha"}
        }
    },

    # --- 5. FOOD, FRUITS & WATER ---
    {
        "id": "food_rice",
        "category": "food",
        "hindi": "चावल / भात",
        "emoji": "🍚",
        "translations": {
            "santhali": {"dev": "दाका (भात) / चाउले (चावल)", "native": "ᱫᱟᱠᱟ", "phonetic": "Daka / Chaule"},
            "mundari": {"dev": "मंडी / चाउली", "phonetic": "Mandi / Chauli"},
            "ho": {"dev": "मंडी", "native": "𑢷𑣁𑢳𑣂", "phonetic": "Mandi"},
            "kurukh": {"dev": "मंडी (भात) / कीचली", "native": "ᱢᱟᱱᱰᱤ", "phonetic": "Mandi / Kichli"},
            "kharia": {"dev": "मंडी", "phonetic": "Mandi"},
            "khortha": {"dev": "भात / चामल", "phonetic": "Bhaat / Chamal"},
            "nagpuri": {"dev": "भात / चाउर", "phonetic": "Bhaat / Chaur"},
            "panchpargania": {"dev": "भात / चाउर", "phonetic": "Bhaat / Chaur"},
            "kurmali": {"dev": "भात / चाउर", "phonetic": "Bhaat / Chaur"}
        }
    },
    {
        "id": "food_mango",
        "category": "food",
        "hindi": "आम",
        "emoji": "🥭",
        "translations": {
            "santhali": {"dev": "उल", "native": "ᱩᱞ", "phonetic": "Ul"},
            "mundari": {"dev": "उली", "phonetic": "Uli"},
            "ho": {"dev": "उली", "native": "𑢢𑢹𑣂", "phonetic": "Uli"},
            "kurukh": {"dev": "ततखा / आम", "native": "ᱛᱟᱛᱠᱷᱟ", "phonetic": "Tatkha"},
            "kharia": {"dev": "उली", "phonetic": "Uli"},
            "khortha": {"dev": "आमा / आम", "phonetic": "Aama / Aam"},
            "nagpuri": {"dev": "आमा / आम", "phonetic": "Aama / Aam"},
            "panchpargania": {"dev": "आमा", "phonetic": "Aama"},
            "kurmali": {"dev": "आमा / आम", "phonetic": "Aama"}
        }
    },
    {
        "id": "food_milk",
        "category": "food",
        "hindi": "दूध",
        "emoji": "🥛",
        "translations": {
            "santhali": {"dev": "तोवा", "native": "ᱛᱳᱣᱟ", "phonetic": "Towa"},
            "mundari": {"dev": "तोवा", "phonetic": "Towa"},
            "ho": {"dev": "तोवा", "native": "𑢵𑣉𑢮𑣁", "phonetic": "Towa"},
            "kurukh": {"dev": "दूधी / पय", "native": "ᱫᱩᱫᱷᱤ", "phonetic": "Dudhi / Pay"},
            "kharia": {"dev": "दूध", "phonetic": "Dudh"},
            "khortha": {"dev": "दूध / दुधवा", "phonetic": "Doodh"},
            "nagpuri": {"dev": "दूध / दूधी", "phonetic": "Doodh"},
            "panchpargania": {"dev": "दूध", "phonetic": "Doodh"},
            "kurmali": {"dev": "दूध", "phonetic": "Doodh"}
        }
    },
    {
        "id": "food_bread",
        "category": "food",
        "hindi": "रोटी",
        "emoji": "🫓",
        "translations": {
            "santhali": {"dev": "पीठा / रोटी", "native": "ᱯᱤᱴᱷᱟᱹ", "phonetic": "Pitha / Roti"},
            "mundari": {"dev": "लेड़ा / पीठा", "phonetic": "Lera / Pitha"},
            "ho": {"dev": "पीठा", "native": "𑢱𑣂𑢵𑣁", "phonetic": "Pitha"},
            "kurukh": {"dev": "अस्मा / रोटी", "native": "ᱟᱥᱢᱟ", "phonetic": "Asma / Roti"},
            "kharia": {"dev": "पीठा", "phonetic": "Pitha"},
            "khortha": {"dev": "रोटी / पीठा", "phonetic": "Roti / Pitha"},
            "nagpuri": {"dev": "रोटी / पीठा", "phonetic": "Roti / Pitha"},
            "panchpargania": {"dev": "रोटी / पीठा", "phonetic": "Roti"},
            "kurmali": {"dev": "रोटी / पीठा", "phonetic": "Roti / Pitha"}
        }
    },

    # --- 6. NUMBERS & COUNTING ---
    {
        "id": "num_1",
        "category": "numbers",
        "hindi": "एक (1)",
        "emoji": "1️⃣",
        "translations": {
            "santhali": {"dev": "मित् (१)", "native": "ᱢᱤᱫ", "phonetic": "Mit'"},
            "mundari": {"dev": "मियाद (१)", "phonetic": "Miyad"},
            "ho": {"dev": "मियाद (१)", "native": "𑢷𑣂𑢠𑣁𑢶", "phonetic": "Miyad"},
            "kurukh": {"dev": "ओंद (१)", "native": "ᱚᱱᱫ", "phonetic": "Ond"},
            "kharia": {"dev": "मोय (१)", "phonetic": "Moy"},
            "khortha": {"dev": "एक / एकेगो (१)", "phonetic": "Ek / Ekgo"},
            "nagpuri": {"dev": "एक / एगो (१)", "phonetic": "Ek / Eko"},
            "panchpargania": {"dev": "एक / एगो (१)", "phonetic": "Ek / Ekgo"},
            "kurmali": {"dev": "एक / एकेक (१)", "phonetic": "Ek"}
        }
    },
    {
        "id": "num_2",
        "category": "numbers",
        "hindi": "दो (2)",
        "emoji": "2️⃣",
        "translations": {
            "santhali": {"dev": "बार (२)", "native": "ᱵᱟᱨ", "phonetic": "Bar"},
            "mundari": {"dev": "बारिया (२)", "phonetic": "Bariya"},
            "ho": {"dev": "बारिया (२)", "native": "𑢲𑣁𑢸𑣂𑢠𑣁", "phonetic": "Bariya"},
            "kurukh": {"dev": "एन्द (२)", "native": "ᱮᱱᱫ", "phonetic": "End"},
            "kharia": {"dev": "उबार (२)", "phonetic": "Ubar"},
            "khortha": {"dev": "दू / दुगो (२)", "phonetic": "Doo / Dugo"},
            "nagpuri": {"dev": "दू / दुईगो (२)", "phonetic": "Doo / Duego"},
            "panchpargania": {"dev": "दू / दुगो (२)", "phonetic": "Doo"},
            "kurmali": {"dev": "दू / दुई (२)", "phonetic": "Doo / Dui"}
        }
    },
    {
        "id": "num_3",
        "category": "numbers",
        "hindi": "तीन (3)",
        "emoji": "3️⃣",
        "translations": {
            "santhali": {"dev": "पे (३)", "native": "ᱯᱮ", "phonetic": "Pe"},
            "mundari": {"dev": "आपि (३)", "phonetic": "Aapi"},
            "ho": {"dev": "आपि (३)", "native": "𑢠𑢱𑣂", "phonetic": "Aapi"},
            "kurukh": {"dev": "मूंद (३)", "native": "ᱢᱩᱱᱫ", "phonetic": "Moond"},
            "kharia": {"dev": "उफे (३)", "phonetic": "Uphe"},
            "khortha": {"dev": "तीन / तीनगो (३)", "phonetic": "Teen / Teengo"},
            "nagpuri": {"dev": "तीन / तीनगो (३)", "phonetic": "Teen"},
            "panchpargania": {"dev": "तीन / तीनगो (३)", "phonetic": "Teen"},
            "kurmali": {"dev": "तीन (३)", "phonetic": "Teen"}
        }
    },
    {
        "id": "num_4",
        "category": "numbers",
        "hindi": "चार (4)",
        "emoji": "4️⃣",
        "translations": {
            "santhali": {"dev": "पोन (४)", "native": "ᱯᱳᱱ", "phonetic": "Pon"},
            "mundari": {"dev": "उपून (४)", "phonetic": "Upun"},
            "ho": {"dev": "उपून (४)", "native": "𑢢𑢱𑣁𑢳", "phonetic": "Upun"},
            "kurukh": {"dev": "नाख (४)", "native": "ᱱᱟᱠᱷ", "phonetic": "Naakh"},
            "kharia": {"dev": "इपोन (४)", "phonetic": "Ipon"},
            "khortha": {"dev": "चार / चारगो (४)", "phonetic": "Chaar"},
            "nagpuri": {"dev": "चार / चारगो (४)", "phonetic": "Chaar"},
            "panchpargania": {"dev": "चार (४)", "phonetic": "Chaar"},
            "kurmali": {"dev": "चार (४)", "phonetic": "Chaar"}
        }
    },
    {
        "id": "num_5",
        "category": "numbers",
        "hindi": "पाँच (5)",
        "emoji": "5️⃣",
        "translations": {
            "santhali": {"dev": "मोणे (५)", "native": "ᱢᱚᱬᱮ", "phonetic": "Mone"},
            "mundari": {"dev": "मोड़े (५)", "phonetic": "More"},
            "ho": {"dev": "मोड़े (५)", "native": "𑢷𑣉𑢳𑣂", "phonetic": "More"},
            "kurukh": {"dev": "पांच (५)", "native": "ᱯᱟᱧᱪ", "phonetic": "Panch"},
            "kharia": {"dev": "मलोय (५)", "phonetic": "Moloy"},
            "khortha": {"dev": "पाँच / पांचगो (५)", "phonetic": "Paanch"},
            "nagpuri": {"dev": "पाँच (५)", "phonetic": "Paanch"},
            "panchpargania": {"dev": "पाँच (५)", "phonetic": "Paanch"},
            "kurmali": {"dev": "पाँच (५)", "phonetic": "Paanch"}
        }
    },
    {
        "id": "num_10",
        "category": "numbers",
        "hindi": "दस (10)",
        "emoji": "🔟",
        "translations": {
            "santhali": {"dev": "गेल (१०)", "native": "ᱜᱮᱞ", "phonetic": "Gel"},
            "mundari": {"dev": "गेल (१०)", "phonetic": "Gel"},
            "ho": {"dev": "गेल (१०)", "native": "𑢬𑣂𑢹", "phonetic": "Gel"},
            "kurukh": {"dev": "दओ (१०)", "native": "ᱫᱟᱥ", "phonetic": "Dao / Das"},
            "kharia": {"dev": "घोल (१०)", "phonetic": "Ghol"},
            "khortha": {"dev": "दस / दसगो (१०)", "phonetic": "Das"},
            "nagpuri": {"dev": "दस (१०)", "phonetic": "Das"},
            "panchpargania": {"dev": "दस (१०)", "phonetic": "Das"},
            "kurmali": {"dev": "दस (१०)", "phonetic": "Das"}
        }
    },

    # --- 7. COLORS ---
    {
        "id": "col_red",
        "category": "colors",
        "hindi": "लाल रंग",
        "emoji": "🔴",
        "translations": {
            "santhali": {"dev": "आराः", "native": "ᱟᱨᱟᱜ", "phonetic": "Aaraag"},
            "mundari": {"dev": "आराः", "phonetic": "Aarah"},
            "ho": {"dev": "आराः", "native": "𑢠𑢸𑣁𑢬", "phonetic": "Aarah"},
            "kurukh": {"dev": "खेखो / लाल", "native": "ᱠᱷᱮᱠᱷᱳ", "phonetic": "Khekho / Lal"},
            "kharia": {"dev": "रंगिन / आराः", "phonetic": "Aarah"},
            "khortha": {"dev": "लाल / ललका", "phonetic": "Laal / Lalka"},
            "nagpuri": {"dev": "लाल / ललका", "phonetic": "Laal / Lalka"},
            "panchpargania": {"dev": "लाल / ललका", "phonetic": "Laal"},
            "kurmali": {"dev": "लाल / रता", "phonetic": "Laal / Rata"}
        }
    },
    {
        "id": "col_green",
        "category": "colors",
        "hindi": "हरा रंग",
        "emoji": "🟢",
        "translations": {
            "santhali": {"dev": "हरियाड़", "native": "ᱦᱟᱹᱨᱭᱟᱹᱲ", "phonetic": "Hariyar"},
            "mundari": {"dev": "हरियर", "phonetic": "Hariyar"},
            "ho": {"dev": "हरियर", "native": "𑢹𑣁𑢸𑣂𑢠𑣁𑢸", "phonetic": "Hariyar"},
            "kurukh": {"dev": "हरियर", "native": "ᱦᱟᱨᱤᱭᱟᱨ", "phonetic": "Hariyar"},
            "kharia": {"dev": "हरियर", "phonetic": "Hariyar"},
            "khortha": {"dev": "हरियर / हरियरका", "phonetic": "Hariyar"},
            "nagpuri": {"dev": "हरियर / हरियरा", "phonetic": "Hariyar"},
            "panchpargania": {"dev": "हरियर", "phonetic": "Hariyar"},
            "kurmali": {"dev": "हरियर / हरियरा", "phonetic": "Hariyar"}
        }
    },
    {
        "id": "col_yellow",
        "category": "colors",
        "hindi": "पीला रंग",
        "emoji": "🟡",
        "translations": {
            "santhali": {"dev": "सासांग", "native": "ᱥᱟᱥᱟᱝ", "phonetic": "Sasang"},
            "mundari": {"dev": "ससांग", "phonetic": "Sasang"},
            "ho": {"dev": "ससांग", "native": "𑢺𑣁𑢺𑣁𑢵𑢬", "phonetic": "Sasang"},
            "kurukh": {"dev": "पियर / ससांग", "native": "ᱯᱤᱭᱟᱨ", "phonetic": "Piyar"},
            "kharia": {"dev": "ससांग", "phonetic": "Sasang"},
            "khortha": {"dev": "पियर / पियरका", "phonetic": "Piyar / Piyarka"},
            "nagpuri": {"dev": "पियर / पियरा", "phonetic": "Piyar / Piyara"},
            "panchpargania": {"dev": "पियर", "phonetic": "Piyar"},
            "kurmali": {"dev": "पियर / पियरा", "phonetic": "Piyar"}
        }
    },
    {
        "id": "col_white",
        "category": "colors",
        "hindi": "सफेद (उजला) रंग",
        "emoji": "⚪",
        "translations": {
            "santhali": {"dev": "पोंड", "native": "ᱯᱳᱸᱰ", "phonetic": "Pond"},
            "mundari": {"dev": "पुंदी", "phonetic": "Pundi"},
            "ho": {"dev": "पुंदी", "native": "𑢱𑣁𑢳𑣂", "phonetic": "Pundi"},
            "kurukh": {"dev": "पंड़ू", "native": "ᱯᱟᱱᱰᱩ", "phonetic": "Pandu"},
            "kharia": {"dev": "पोंड", "phonetic": "Pond"},
            "khortha": {"dev": "चरका / उज्जर", "phonetic": "Charka / Ujjar"},
            "nagpuri": {"dev": "चरका / उज्जर", "phonetic": "Charka / Ujjar"},
            "panchpargania": {"dev": "चरका / उजला", "phonetic": "Charka"},
            "kurmali": {"dev": "चरका / सादा", "phonetic": "Charka / Sada"}
        }
    },
    {
        "id": "col_black",
        "category": "colors",
        "hindi": "काला रंग",
        "emoji": "⚫",
        "translations": {
            "santhali": {"dev": "हेंदे", "native": "ᱦᱮᱸᱫᱮ", "phonetic": "Hende"},
            "mundari": {"dev": "हेंदे", "phonetic": "Hende"},
            "ho": {"dev": "हेंदे", "native": "𑢹𑣂𑢳𑢶𑣂", "phonetic": "Hende"},
            "kurukh": {"dev": "करिया / खोरखा", "native": "ᱠᱟᱨᱤᱭᱟ", "phonetic": "Kariya / Khorkha"},
            "kharia": {"dev": "हेंदे", "phonetic": "Hende"},
            "khortha": {"dev": "करिया / करियाका", "phonetic": "Kariya"},
            "nagpuri": {"dev": "करिया / करियाका", "phonetic": "Kariya"},
            "panchpargania": {"dev": "करिया", "phonetic": "Kariya"},
            "kurmali": {"dev": "करिया / करियाका", "phonetic": "Kariya"}
        }
    },

    # --- 8. BODY PARTS ---
    {
        "id": "body_eye",
        "category": "body",
        "hindi": "आँख / नयन",
        "emoji": "👁️",
        "translations": {
            "santhali": {"dev": "मेद", "native": "ᱢᱮᱫ", "phonetic": "Med"},
            "mundari": {"dev": "मेद", "phonetic": "Med"},
            "ho": {"dev": "मेद", "native": "𑢷𑣂𑢶", "phonetic": "Med"},
            "kurukh": {"dev": "खन्न", "native": "ᱠᱷᱟᱱᱱ", "phonetic": "Khann"},
            "kharia": {"dev": "मेद", "phonetic": "Med"},
            "khortha": {"dev": "आँख / आँखिया", "phonetic": "Aankh"},
            "nagpuri": {"dev": "आँख / अँखिया", "phonetic": "Aankh"},
            "panchpargania": {"dev": "आँख", "phonetic": "Aankh"},
            "kurmali": {"dev": "आँख / आँखि", "phonetic": "Aankh"}
        }
    },
    {
        "id": "body_hand",
        "category": "body",
        "hindi": "हाथ",
        "emoji": "✋",
        "translations": {
            "santhali": {"dev": "ती", "native": "ᱛᱤ", "phonetic": "Ti"},
            "mundari": {"dev": "ती", "phonetic": "Ti"},
            "ho": {"dev": "ती", "native": "𑢵𑣂", "phonetic": "Ti"},
            "kurukh": {"dev": "खेक्खा", "native": "ᱠᱷᱮᱠᱠᱷᱟ", "phonetic": "Khekkha"},
            "kharia": {"dev": "ती", "phonetic": "Ti"},
            "khortha": {"dev": "हाथ / हथवा", "phonetic": "Haath"},
            "nagpuri": {"dev": "हाथ / हथिया", "phonetic": "Haath"},
            "panchpargania": {"dev": "हाथ", "phonetic": "Haath"},
            "kurmali": {"dev": "हाथ", "phonetic": "Haath"}
        }
    },
    {
        "id": "body_ear",
        "category": "body",
        "hindi": "कान",
        "emoji": "👂",
        "translations": {
            "santhali": {"dev": "लुथुर", "native": "ᱞᱩᱛᱷᱩᱨ", "phonetic": "Luthur"},
            "mundari": {"dev": "लुथुर", "phonetic": "Luthur"},
            "ho": {"dev": "लुथुर", "native": "𑢹𑣁𑢵𑣁𑢸", "phonetic": "Luthur"},
            "kurukh": {"dev": "खेबड़ा", "native": "ᱠᱷᱮᱵᱲᱟ", "phonetic": "Khebda"},
            "kharia": {"dev": "लुथुर", "phonetic": "Luthur"},
            "khortha": {"dev": "कान / कनवा", "phonetic": "Kaan"},
            "nagpuri": {"dev": "कान", "phonetic": "Kaan"},
            "panchpargania": {"dev": "कान", "phonetic": "Kaan"},
            "kurmali": {"dev": "कान", "phonetic": "Kaan"}
        }
    },
    {
        "id": "body_head",
        "category": "body",
        "hindi": "सिर / माथा",
        "emoji": "👦",
        "translations": {
            "santhali": {"dev": "बोहोक", "native": "ᱵᱚᱦᱚᱜ", "phonetic": "Bohok"},
            "mundari": {"dev": "बोः", "phonetic": "Boh"},
            "ho": {"dev": "बोः", "native": "𑢲𑣉𑢬", "phonetic": "Boh"},
            "kurukh": {"dev": "कुक", "native": "ᱠᱩᱠ", "phonetic": "Kuk"},
            "kharia": {"dev": "बोहोक", "phonetic": "Bohok"},
            "khortha": {"dev": "माथा / मूंड़ी", "phonetic": "Matha / Moondi"},
            "nagpuri": {"dev": "माथा / मूड़", "phonetic": "Matha / Mood"},
            "panchpargania": {"dev": "माथा / मूड़", "phonetic": "Matha"},
            "kurmali": {"dev": "माथा / मूड़", "phonetic": "Matha"}
        }
    },

    # --- 9. DAILY ACTIONS & VERBS ---
    {
        "id": "act_play",
        "category": "actions",
        "hindi": "खेलना / खेलो",
        "emoji": "⚽",
        "translations": {
            "santhali": {"dev": "एनेच", "native": "ᱮᱱᱮᱡ", "phonetic": "Enej"},
            "mundari": {"dev": "इनुंग", "phonetic": "Inung"},
            "ho": {"dev": "इनुंग", "native": "𑢠𑢳𑣁𑢵𑢬", "phonetic": "Inung"},
            "kurukh": {"dev": "बेचना", "native": "ᱵᱮᱪᱱᱟ", "phonetic": "Bechna"},
            "kharia": {"dev": "इनुंग", "phonetic": "Inung"},
            "khortha": {"dev": "खेलना / खेला कर", "phonetic": "Khelna"},
            "nagpuri": {"dev": "खेलना / खेलब", "phonetic": "Khelna / Khelab"},
            "panchpargania": {"dev": "खेलना / खेला", "phonetic": "Khelna"},
            "kurmali": {"dev": "खेलना / खेला", "phonetic": "Khelna"}
        }
    },
    {
        "id": "act_eat",
        "category": "actions",
        "hindi": "खाना / खाओ",
        "emoji": "🍽️",
        "translations": {
            "santhali": {"dev": "जोम / जोम मे", "native": "ᱡᱚᱢ", "phonetic": "Jom / Jom me"},
            "mundari": {"dev": "जोम", "phonetic": "Jom"},
            "ho": {"dev": "जोम", "native": "𑢪𑣉𑢷", "phonetic": "Jom"},
            "kurukh": {"dev": "ओनना / मोखना", "native": "ᱢᱳᱠᱷᱱᱟ", "phonetic": "Onna / Mokhna"},
            "kharia": {"dev": "जोम", "phonetic": "Jom"},
            "khortha": {"dev": "खाय / खाना खा", "phonetic": "Khaay"},
            "nagpuri": {"dev": "खाएक / खावा", "phonetic": "Khaek"},
            "panchpargania": {"dev": "खाएक / खा", "phonetic": "Khaek"},
            "kurmali": {"dev": "खाएक / खावा", "phonetic": "Khaek"}
        }
    },
    {
        "id": "act_drink",
        "category": "actions",
        "hindi": "पीना / पानी पियो",
        "emoji": "🥤",
        "translations": {
            "santhali": {"dev": "ञूँ / दाः ञूँ मे", "native": "ᱧᱩ", "phonetic": "Nyun / Daah nyun me"},
            "mundari": {"dev": "नू", "phonetic": "Nu"},
            "ho": {"dev": "नू", "native": "𑢳𑣁", "phonetic": "Nu"},
            "kurukh": {"dev": "ओन्ना", "native": "ᱚᱱᱱᱟ", "phonetic": "Onna"},
            "kharia": {"dev": "नू", "phonetic": "Nu"},
            "khortha": {"dev": "पीना / पी", "phonetic": "Peena"},
            "nagpuri": {"dev": "पीयेक / पिया", "phonetic": "Piyek"},
            "panchpargania": {"dev": "पीयेक", "phonetic": "Piyek"},
            "kurmali": {"dev": "पीयेक / पी", "phonetic": "Piyek"}
        }
    },
    {
        "id": "act_read",
        "category": "actions",
        "hindi": "पढ़ना / किताब पढ़ो",
        "emoji": "📖",
        "translations": {
            "santhali": {"dev": "पाड़हाव / ओल-पाड़हाव", "native": "ᱯᱟᱲᱦᱟᱣ", "phonetic": "Parhaw"},
            "mundari": {"dev": "पड़ाव", "phonetic": "Paraw"},
            "ho": {"dev": "पड़ाव", "native": "𑢱𑣁𑢸𑣁𑢮", "phonetic": "Paraw"},
            "kurukh": {"dev": "पढ़ना / पोथी पढ़ना", "native": "ᱯᱟᱲᱦᱱᱟ", "phonetic": "Parhna"},
            "kharia": {"dev": "पड़ाव", "phonetic": "Paraw"},
            "khortha": {"dev": "पढ़े / पढ़ाई कर", "phonetic": "Parhe"},
            "nagpuri": {"dev": "पढ़े / पढ़ब", "phonetic": "Parhe"},
            "panchpargania": {"dev": "पढ़े / पढ़ाई", "phonetic": "Parhe"},
            "kurmali": {"dev": "पढ़े / पढ़ाई", "phonetic": "Parhe"}
        }
    },
    {
        "id": "act_dance",
        "category": "actions",
        "hindi": "नाचना / नृत्य करना",
        "emoji": "💃",
        "translations": {
            "santhali": {"dev": "एनेच / रू-एनेच", "native": "ᱮᱱᱮᱡ", "phonetic": "Enej"},
            "mundari": {"dev": "सुसुन", "phonetic": "Susun"},
            "ho": {"dev": "सुसुन", "native": "𑢺𑣁𑢺𑣁𑢳", "phonetic": "Susun"},
            "kurukh": {"dev": "नाचना / झूमर नाचना", "native": "ᱱᱟᱪᱱᱟ", "phonetic": "Nachna"},
            "kharia": {"dev": "सुसुन", "phonetic": "Susun"},
            "khortha": {"dev": "नाचेक / झूमर नाच", "phonetic": "Nachek"},
            "nagpuri": {"dev": "नाचेक / झुमइर", "phonetic": "Nachek / Jhumair"},
            "panchpargania": {"dev": "नाचेक", "phonetic": "Nachek"},
            "kurmali": {"dev": "नाचेक / झुमइर नाच", "phonetic": "Nachek"}
        }
    },

    # --- 10. SCHOOL & TOYS ---
    {
        "id": "sch_book",
        "category": "school",
        "hindi": "किताब / पुस्तक",
        "emoji": "📚",
        "translations": {
            "santhali": {"dev": "पुथी", "native": "ᱯᱩᱛᱷᱤ", "phonetic": "Puthi"},
            "mundari": {"dev": "पुथी", "phonetic": "Puthi"},
            "ho": {"dev": "पुथी", "native": "𑢱𑣁𑢵𑣂", "phonetic": "Puthi"},
            "kurukh": {"dev": "पोथी", "native": "ᱯᱳᱛᱷᱤ", "phonetic": "Pothi"},
            "kharia": {"dev": "पुथी", "phonetic": "Puthi"},
            "khortha": {"dev": "किताब / पोथी", "phonetic": "Kitaab / Pothi"},
            "nagpuri": {"dev": "किताब / पोथी", "phonetic": "Kitaab / Pothi"},
            "panchpargania": {"dev": "किताब / पोथी", "phonetic": "Kitaab"},
            "kurmali": {"dev": "किताब / पोथी", "phonetic": "Kitaab"}
        }
    },
    {
        "id": "sch_school",
        "category": "school",
        "hindi": "स्कूल / पाठशाला / विद्यालय",
        "emoji": "🏫",
        "translations": {
            "santhali": {"dev": "बिरदागाड़ / इसकुल", "native": "ᱵᱤᱨᱫᱟᱹᱜᱟᱲ", "phonetic": "Birdagar / Iskul"},
            "mundari": {"dev": "इस्कूल / बिरदागाड़", "phonetic": "Iskul / Birdagar"},
            "ho": {"dev": "बिरदागाड़ / इस्कुल", "native": "𑢲𑣂𑢸𑢶𑣁", "phonetic": "Birdagar"},
            "kurukh": {"dev": "इस्कुल / पढ़ना घर", "native": "ᱤᱥᱠᱩᱞ", "phonetic": "Iskul"},
            "kharia": {"dev": "इस्कुल", "phonetic": "Iskul"},
            "khortha": {"dev": "स्कूल / पाठशाला", "phonetic": "School"},
            "nagpuri": {"dev": "स्कूल / पाठशाला", "phonetic": "School"},
            "panchpargania": {"dev": "स्कूल", "phonetic": "School"},
            "kurmali": {"dev": "स्कूल / साला", "phonetic": "School"}
        }
    },

    # --- 11. FEELINGS & EMOTIONS ---
    {
        "id": "feel_happy",
        "category": "feelings",
        "hindi": "खुश / प्रसन्न / आनंद",
        "emoji": "😄",
        "translations": {
            "santhali": {"dev": "रास्का", "native": "ᱨᱟᱹᱥᱠᱟᱹ", "phonetic": "Raska"},
            "mundari": {"dev": "रास्का", "phonetic": "Raska"},
            "ho": {"dev": "रास्का", "native": "𑢸𑣁𑢺𑣫𑣁", "phonetic": "Raska"},
            "kurukh": {"dev": "खुस / बेस", "native": "ᱠᱷᱩᱥ", "phonetic": "Khus / Bes"},
            "kharia": {"dev": "रास्का", "phonetic": "Raska"},
            "khortha": {"dev": "खुश / बेस लागे", "phonetic": "Khush"},
            "nagpuri": {"dev": "खुश / आनन्द", "phonetic": "Khush / Anand"},
            "panchpargania": {"dev": "खुश", "phonetic": "Khush"},
            "kurmali": {"dev": "खुश / राजी", "phonetic": "Khush / Raaji"}
        }
    },
    {
        "id": "feel_love",
        "category": "feelings",
        "hindi": "प्यार / स्नेह / दुलार",
        "emoji": "💖",
        "translations": {
            "santhali": {"dev": "दुलार", "native": "ᱫᱩᱞᱟᱹᱲ", "phonetic": "Dular"},
            "mundari": {"dev": "दुलार", "phonetic": "Dular"},
            "ho": {"dev": "दुलार", "native": "𑢶𑣁𑢹𑣁𑢸", "phonetic": "Dular"},
            "kurukh": {"dev": "दुलार / मया", "native": "ᱫᱩᱞᱟᱨ", "phonetic": "Dular / Maya"},
            "kharia": {"dev": "दुलार", "phonetic": "Dular"},
            "khortha": {"dev": "पिरीत / दुलार / मया", "phonetic": "Pirit / Dular"},
            "nagpuri": {"dev": "दुलार / मया / पिरीत", "phonetic": "Dular / Maya"},
            "panchpargania": {"dev": "दुलार / मया", "phonetic": "Dular"},
            "kurmali": {"dev": "दुलार / माया", "phonetic": "Dular / Maya"}
        }
    },
    {
        "id": "feel_beautiful",
        "category": "feelings",
        "hindi": "सुंदर / प्यारा / बहुत अच्छा",
        "emoji": "✨",
        "translations": {
            "santhali": {"dev": "मोज / नापाय", "native": "ᱢᱚᱡᱽ", "phonetic": "Moj / Napay"},
            "mundari": {"dev": "बुगिन / बेस", "phonetic": "Bugin / Bes"},
            "ho": {"dev": "बुगिन / मोज", "native": "𑢲𑣁𑢬𑣂𑢳", "phonetic": "Bugin / Moj"},
            "kurukh": {"dev": "दओ / बेस", "native": "ᱫᱟᱣ", "phonetic": "Dao / Bes"},
            "kharia": {"dev": "बेस / मोज", "phonetic": "Bes"},
            "khortha": {"dev": "सुन्दर / बेजोड़ / बेस", "phonetic": "Sundar / Bejor"},
            "nagpuri": {"dev": "सुन्दर / बेस / चिकन", "phonetic": "Sundar / Chikan"},
            "panchpargania": {"dev": "सुन्दर / बेस", "phonetic": "Sundar"},
            "kurmali": {"dev": "सुन्दर / बेस", "phonetic": "Sundar"}
        }
    },

    # --- 12. DAILY PHRASES & SENTENCES ---
    {
        "id": "phr_what_is_your_name",
        "category": "phrases",
        "hindi": "तुम्हारा नाम क्या है?",
        "emoji": "📛",
        "translations": {
            "santhali": {"dev": "आमाः ञुतुम दो चेत?", "native": "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ ᱫᱚ ᱪᱮᱫ?", "phonetic": "Aamag nyutum do chet?"},
            "mundari": {"dev": "आमाः नुतुम चिनाः?", "phonetic": "Aamah nutum chinaah?"},
            "ho": {"dev": "अमाः नुतुम चिनाः?", "native": "𑢠𑢷𑣁𑢬 𑢳𑣁𑢵𑣁𑢷?", "phonetic": "Amah nutum chinah?"},
            "kurukh": {"dev": "निंघै नामे एन्दिर तके?", "native": "ᱱᱤᱝᱜᱷᱟᱭ ᱱᱟᱢᱮ ᱮᱱᱫᱤᱨ?", "phonetic": "Ninghai name endir take?"},
            "kharia": {"dev": "अमना नामे चिलके?", "phonetic": "Amna name chilke?"},
            "khortha": {"dev": "तोर नाम की लागे? / तोहर नाम की हक?", "phonetic": "Tor naam ki laage?"},
            "nagpuri": {"dev": "तोहर नाम का हेके? / राउर नाम का हेके?", "phonetic": "Tohar naam ka heke?"},
            "panchpargania": {"dev": "तहार नाम की हेके?", "phonetic": "Tahar naam ki heke?"},
            "kurmali": {"dev": "तोर नाम की आहै?", "phonetic": "Tor naam ki aahai?"}
        }
    },
    {
        "id": "phr_my_name_is",
        "category": "phrases",
        "hindi": "मेरा नाम ... है",
        "emoji": "🙋",
        "translations": {
            "santhali": {"dev": "इञाः ञुतुम दो ... काना", "native": "ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ ᱫᱚ ... ᱠᱟᱱᱟ", "phonetic": "Injagh nyutum do ... kana"},
            "mundari": {"dev": "ऐंगाः नुतुम ... ताना", "phonetic": "Aingah nutum ... tana"},
            "ho": {"dev": "ऐंगाः नुतुम ... ताना", "native": "𑢠𑣂𑢵𑢬 𑢳𑣁𑢵𑣁𑢷 ... 𑢵𑣁𑢳𑣁", "phonetic": "Aingah nutum ... tana"},
            "kurukh": {"dev": "एंग्है नामे ... तके", "native": "ᱮᱝᱜᱷᱟᱭ ᱱᱟᱢᱮ ... ᱛᱟᱠᱮ", "phonetic": "Enghai name ... take"},
            "kharia": {"dev": "इञना नामे ... आके", "phonetic": "Injna name ... aake"},
            "khortha": {"dev": "हमर नाम ... लागे", "phonetic": "Hamar naam ... laage"},
            "nagpuri": {"dev": "मोर नाम ... हेके", "phonetic": "Mor naam ... heke"},
            "panchpargania": {"dev": "हमर नाम ... हेके", "phonetic": "Hamar naam ... heke"},
            "kurmali": {"dev": "हमर नाम ... आहै", "phonetic": "Hamar naam ... aahai"}
        }
    },
    {
        "id": "phr_lets_play",
        "category": "phrases",
        "hindi": "चलो खेलते हैं!",
        "emoji": "🎉",
        "translations": {
            "santhali": {"dev": "देलाबोन एनेच लागीत!", "native": "ᱫᱮᱞᱟᱵᱳᱱ ᱮᱱᱮᱡ ᱞᱟᱹᱜᱤᱫ!", "phonetic": "Delabon enej lagit!"},
            "mundari": {"dev": "दोलाबोन इनुंग लागीद!", "phonetic": "Dolabon inung lagid!"},
            "ho": {"dev": "दोलाबोन इनुंग ते!", "native": "𑢶𑣉𑢹𑣁𑢲𑣉𑢳 𑢠𑢳𑣁𑢵𑢬!", "phonetic": "Dolabon inung te!"},
            "kurukh": {"dev": "चला बेचना कालोम!", "native": "ᱪᱟᱞᱟ ᱵᱮᱪᱱᱟ ᱠᱟᱞᱳᱢ!", "phonetic": "Chala bechna kalom!"},
            "kharia": {"dev": "दोलों इनुंग लागीद!", "phonetic": "Dolon inung lagid!"},
            "khortha": {"dev": "चल खेला करेगे!", "phonetic": "Chal khela karege!"},
            "nagpuri": {"dev": "चला खेलेक जाब!", "phonetic": "Chala khelek jaab!"},
            "panchpargania": {"dev": "चल खेला कोरबो!", "phonetic": "Chal khela korbo!"},
            "kurmali": {"dev": "चल खेले जाइब!", "phonetic": "Chal khele jaib!"}
        }
    },
    {
        "id": "phr_where_are_you_going",
        "category": "phrases",
        "hindi": "तुम कहाँ जा रहे हो?",
        "emoji": "🚶",
        "translations": {
            "santhali": {"dev": "आम दो ओका तेम चालाः काना?", "native": "ᱟᱢ ᱫᱚ ᱚᱠᱟ ᱛᱮᱢ ᱪᱟᱞᱟᱜ ᱠᱟᱱᱟ?", "phonetic": "Aam do oka tem chalah kana?"},
            "mundari": {"dev": "आम ओका ते सेन तना?", "phonetic": "Aam oka te sen tana?"},
            "ho": {"dev": "आम ओका ते सेन ताना?", "native": "𑢠𑢷 𑢤𑢫𑣁 𑢵𑣂 𑢺𑣂𑢳?", "phonetic": "Aam oka te sen tana?"},
            "kurukh": {"dev": "नीन एका तरा कालोय?", "native": "ᱱᱤᱱ ᱮᱠᱟ ᱛᱟᱨᱟ ᱠᱟᱞᱳᱭ?", "phonetic": "Neen eka tara kaloy?"},
            "kharia": {"dev": "हानी ओका ते चाला?", "phonetic": "Hani oka te chala?"},
            "khortha": {"dev": "तोहे कहाँ जा रहल ही?", "phonetic": "Tohe kahan ja rahal hi?"},
            "nagpuri": {"dev": "तोय कहाँ जात अहिस? / राउर कहाँ जात ही?", "phonetic": "Toy kahan jaat ahis?"},
            "panchpargania": {"dev": "तहार कहाँ जाहा?", "phonetic": "Tahar kahan jaaha?"},
            "kurmali": {"dev": "तँय कहाँ जाहीस?", "phonetic": "Tany kahan jaahis?"}
        }
    },
    {
        "id": "phr_i_want_water",
        "category": "phrases",
        "hindi": "मुझे पानी पीना है / मुझे पानी चाहिए",
        "emoji": "🥤",
        "translations": {
            "santhali": {"dev": "इञ दो दाः ञूँ सानाइञ काना", "native": "ᱤᱧ ᱫᱚ ᱫᱟᱜ ᱧᱩ ᱥᱟᱱᱟᱹᱧ ᱠᱟᱱᱟ", "phonetic": "Inj do daah nyun sananj kana"},
            "mundari": {"dev": "ऐंग के दाः नू सनांग तना", "phonetic": "Aing ke daah nu sanang tana"},
            "ho": {"dev": "ऐंग के दाः नू सनांग ताना", "native": "𑢠𑣂𑢵𑢬 𑢶𑣁𑢬 𑢳𑣁", "phonetic": "Aing ke dah nu sanang tana"},
            "kurukh": {"dev": "एंगोन अम्म ओन्ना मन लग्गी", "native": "ᱮᱝᱜᱳᱱ ᱟᱢᱢ ᱚᱱᱱᱟ", "phonetic": "Engon amm onna man laggi"},
            "kharia": {"dev": "इञ के दाः नू साना", "phonetic": "Inj ke dah nu sana"},
            "khortha": {"dev": "हमरा पानी पियेक हे", "phonetic": "Hamra paani piyek he"},
            "nagpuri": {"dev": "मोके पानी पीयेक हे", "phonetic": "Moke paani piyek he"},
            "panchpargania": {"dev": "मोके पानी पियेक लागे", "phonetic": "Moke paani piyek laage"},
            "kurmali": {"dev": "हमरा पानी पियेक आहै", "phonetic": "Hamra paani piyek aahai"}
        }
    },
    {
        "id": "phr_this_is_good",
        "category": "phrases",
        "hindi": "यह बहुत अच्छा है!",
        "emoji": "⭐",
        "translations": {
            "santhali": {"dev": "नोवा दो आडी मोज काना!", "native": "ᱱᱳᱣᱟ ᱫᱚ ᱟᱹᱰᱤ ᱢᱚᱡᱽ ᱠᱟᱱᱟ!", "phonetic": "Nowa do adi moj kana!"},
            "mundari": {"dev": "नेया पुरो बुगिन ताना!", "phonetic": "Neya puro bugin tana!"},
            "ho": {"dev": "नेया पुरो बुगिन ताना!", "native": "𑢳𑣂𑢠𑣁 𑢲𑣁𑢬𑣂𑢳 𑢵𑣁𑢳𑣁!", "phonetic": "Neya puro bugin tana!"},
            "kurukh": {"dev": "ई बेस रअई!", "native": "ᱤ ᱵᱮᱥ ᱨᱟᱭ!", "phonetic": "Ee bes ra'ee!"},
            "kharia": {"dev": "नेया बेस आके!", "phonetic": "Neya bes aake!"},
            "khortha": {"dev": "ई भारी बेस हे!", "phonetic": "Ee bhaari bes he!"},
            "nagpuri": {"dev": "ई बहुत बेस हेके!", "phonetic": "Ee bahut bes heke!"},
            "panchpargania": {"dev": "ईटा खूब बेस हेके!", "phonetic": "Eeta khoob bes heke!"},
            "kurmali": {"dev": "ईटा भारी बेस आहै!", "phonetic": "Eeta bhaari bes aahai!"}
        }
    }
]
