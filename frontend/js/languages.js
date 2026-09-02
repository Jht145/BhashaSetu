/**
 * BhashaSetu Language Configuration & Mapping Module
 * Standardizes BCP-47 / IndicTrans2 language-script codes
 * while strictly preserving the existing UI dropdown labels and appearances.
 */

const LANGUAGE_CONFIG = {
  // Source Language Mappings
  sources: {
    hindi: {
      id: 'hindi',
      code: 'hin_Deva',
      shortCode: 'hin',
      scriptCode: 'deva',
      name_hi: 'हिन्दी',
      name_en: 'Hindi',
      displayLabel: '🇮🇳 Hindi (हिन्दी)',
      voiceLocale: 'hi-IN',
      isSupported: true
    },
    english: {
      id: 'english',
      code: 'eng_Latn',
      shortCode: 'eng',
      scriptCode: 'latn',
      name_hi: 'अंग्रेज़ी',
      name_en: 'English',
      displayLabel: '🇬🇧 English (अंग्रेज़ी)',
      voiceLocale: 'en-US',
      isSupported: true
    }
  },

  // Target Language Mappings (5 Tribal + 4 Regional)
  targets: {
    santhali: {
      id: 'santhali',
      code: 'sat_Olck',
      shortCode: 'sat',
      scriptCode: 'olck',
      name_hi: 'संताली',
      name_en: 'Santhali',
      native_script_sample: 'ᱥᱟᱱᱛᱟᱲᱤ',
      script: 'ओल चिकी (Ol Chiki)',
      family: 'ऑस्ट्रो-एशियाटिक (Munda)',
      regions: 'झारखंड, ओडिशा, प. बंगाल, असम',
      emoji: '🦚',
      greeting: 'जोहार (Johar)',
      greeting_native: 'ᱡᱚᱦᱟᱨ',
      isSupported: true,
      requiresOlChikiFont: true
    },
    mundari: {
      id: 'mundari',
      code: 'unr_Deva',
      shortCode: 'unr',
      scriptCode: 'deva',
      name_hi: 'मुंडारी',
      name_en: 'Mundari',
      native_script_sample: 'ᱢᱩᱱᱰᱟᱨᱤ',
      script: 'देवनागरी / मुंडारी बानी',
      family: 'ऑस्ट्रो-एशियाटिक (Munda)',
      regions: 'झारखंड (राँची, खूँटी), ओडिशा',
      emoji: '🌳',
      greeting: 'जोहार (Johar)',
      greeting_native: 'जोहार',
      isSupported: true,
      requiresOlChikiFont: false
    },
    ho: {
      id: 'ho',
      code: 'hoc_Wara',
      shortCode: 'hoc',
      scriptCode: 'wara',
      name_hi: 'हो',
      name_en: 'Ho',
      native_script_sample: '𑢹𑣉',
      script: 'वारंग चिति (Warang Citi)',
      family: 'ऑस्ट्रो-एशियाटिक (Munda)',
      regions: 'सिंहभूम (झारखंड), मयूरभंज (ओडिशा)',
      emoji: '🦋',
      greeting: 'जोहार (Johar)',
      greeting_native: '𑢹𑣁𑢵𑣂',
      isSupported: true,
      requiresOlChikiFont: false
    },
    kurukh: {
      id: 'kurukh',
      code: 'kru_Deva',
      shortCode: 'kru',
      scriptCode: 'deva',
      name_hi: 'कुड़ुख़ / उरांव',
      name_en: 'Kurukh (Oraon)',
      native_script_sample: 'कुंड़ुख़',
      script: 'तोलोंग सिकि / देवनागरी',
      family: 'द्रविड़ (Dravidian)',
      regions: 'झारखंड, छत्तीसगढ़, ओडिशा',
      emoji: '🐘',
      greeting: 'जोहार / जय धरमे',
      greeting_native: 'जोहार',
      isSupported: true,
      requiresOlChikiFont: false
    },
    kharia: {
      id: 'kharia',
      code: 'khr_Deva',
      shortCode: 'khr',
      scriptCode: 'deva',
      name_hi: 'खड़िया',
      name_en: 'Kharia',
      native_script_sample: 'खड़िया',
      script: 'देवनागरी (Devanagari)',
      family: 'ऑस्ट्रो-एशियाटिक (Munda)',
      regions: 'गुमला, सिमडेगा (झारखंड)',
      emoji: '🌻',
      greeting: 'जोहार (Johar)',
      greeting_native: 'जोहार',
      isSupported: true,
      requiresOlChikiFont: false
    },
    khortha: {
      id: 'khortha',
      code: 'kht_Deva',
      shortCode: 'kht',
      scriptCode: 'deva',
      name_hi: 'खोरठा',
      name_en: 'Khortha',
      native_script_sample: 'खोरठा',
      script: 'देवनागरी (Devanagari)',
      family: 'इंडो-आर्यन (मागधी प्राकृत)',
      regions: 'उत्तरी छोटानागपुर, संथाल परगना',
      emoji: '📚',
      greeting: 'गोड़ लागो ही / जोहार',
      greeting_native: 'गोड़ लागो ही',
      isSupported: true,
      requiresOlChikiFont: false
    },
    nagpuri: {
      id: 'nagpuri',
      code: 'sck_Deva',
      shortCode: 'sck',
      scriptCode: 'deva',
      name_hi: 'नागपुरी / सादरी',
      name_en: 'Nagpuri (Sadri)',
      native_script_sample: 'नागपुरी',
      script: 'देवनागरी (Devanagari)',
      family: 'इंडो-आर्यन (मागधी प्राकृत)',
      regions: 'दक्षिणी छोटानागपुर (झारखंड)',
      emoji: '🎵',
      greeting: 'जोहार / परनाम',
      greeting_native: 'जोहार',
      isSupported: true,
      requiresOlChikiFont: false
    },
    panchpargania: {
      id: 'panchpargania',
      code: 'tdb_Deva',
      shortCode: 'tdb',
      scriptCode: 'deva',
      name_hi: 'पंचपरगनिया',
      name_en: 'Panchpargania',
      native_script_sample: 'पंचपरगनिया',
      script: 'देवनागरी / कैथी',
      family: 'इंडो-आर्यन (मागधी प्राकृत)',
      regions: 'राँची, सिल्ली, बुंडू, तमाड़ क्षेत्र',
      emoji: '🌈',
      greeting: 'जोहार / परनाम',
      greeting_native: 'जोहार',
      isSupported: true,
      requiresOlChikiFont: false
    },
    kurmali: {
      id: 'kurmali',
      code: 'kyw_Deva',
      shortCode: 'kyw',
      scriptCode: 'deva',
      name_hi: 'कुरमाली',
      name_en: 'Kurmali',
      native_script_sample: 'कुरमाली',
      script: 'कुरमाली चिश्ती / देवनागरी',
      family: 'इंडो-आर्यन (मागधी प्राकृत)',
      regions: 'झारखंड, प. बंगाल, ओडिशा',
      emoji: '🌿',
      greeting: 'जोहार / नमस्कार',
      greeting_native: 'जोहार',
      isSupported: true,
      requiresOlChikiFont: false
    }
  }
};

/**
 * Get normalized backend language code for a given source or target key
 */
function getSourceLanguageConfig(key) {
  return LANGUAGE_CONFIG.sources[key] || LANGUAGE_CONFIG.sources.hindi;
}

function getTargetLanguageConfig(key) {
  return LANGUAGE_CONFIG.targets[key] || LANGUAGE_CONFIG.targets.santhali;
}

function isTargetLanguageSupported(key) {
  const target = LANGUAGE_CONFIG.targets[key];
  return target && target.isSupported !== false;
}
