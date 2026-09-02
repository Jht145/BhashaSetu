/**
 * BhashaSetu (भाषा सेतु) - Client Application Script
 * Full Bilingual & Multi-Language Vernacular Learning Platform
 */

// Phrasebook Data (Bilingual: Hindi & English -> Tribal / Regional Languages)
const phrasebook = {
  Santhali: {
    'नमस्ते': 'Johar (ᱡᱚᱦᱟᱨ)',
    'hello': 'Johar (ᱡᱚᱦᱟᱨ)',
    'hi': 'Johar (ᱡᱚᱦᱟᱨ)',
    'धन्यवाद': 'Johar / Sarhao (ᱥᱟᱨᱦᱟᱣ)',
    'thank you': 'Sarhao (ᱥᱟᱨᱦᱟᱣ)',
    'thanks': 'Sarhao (ᱥᱟᱨᱦᱟᱣ)',
    'पानी': 'Daak\' (ᱫᱟᱜ)',
    'water': 'Daak\' (ᱫᱟᱜ)',
    'तुम कैसे हो': 'Chet leka menama? (ᱪᱮᱫ ᱞᱮᱠᱟ ᱢᱮᱱᱟᱢᱟ?)',
    'how are you': 'Chet leka menama? (ᱪᱮᱫ ᱞᱮᱠᱟ ᱢᱮᱱᱟᱢᱟ?)',
    'मेरा नाम': 'Injań ñutum (ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ)',
    'my name': 'Injań ñutum (ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ)'
  },
  Mundari: {
    'नमस्ते': 'Johar (जोहार)',
    'hello': 'Johar (जोहार)',
    'hi': 'Johar (जोहार)',
    'धन्यवाद': 'Johar / Dhanyabad',
    'thank you': 'Johar / Dhanyabad',
    'thanks': 'Johar / Dhanyabad',
    'पानी': 'Da\' (दाः)',
    'water': 'Da\' (दाः)',
    'तुम कैसे हो': 'Am chetana? (अम चेतना?)',
    'how are you': 'Am chetana? (अम चेतना?)',
    'मेरा नाम': 'Aing ren nutum',
    'my name': 'Aing ren nutum'
  },
  Ho: {
    'नमस्ते': 'Johar (𑢪𑣉𑢦𑢬𑣂)',
    'hello': 'Johar (𑢪𑣉𑢦𑢬𑣂)',
    'hi': 'Johar (𑢪𑣉𑢦𑢬𑣂)',
    'धन्यवाद': 'Johar (𑢪𑣉𑢦𑢬𑣂)',
    'thank you': 'Johar (𑢪𑣉𑢦𑢬𑣂)',
    'thanks': 'Johar (𑢪𑣉𑢦𑢬𑣂)',
    'पानी': 'Da\' (𑢵𑢁)',
    'water': 'Da\' (𑢵𑢁)',
    'तुम कैसे हो': 'Am chekana? (𑢁𑢪 𑢹𑣂𑢮𑢳𑢪)',
    'how are you': 'Am chekana? (𑢁𑢪 𑢹𑣂𑢮𑢳𑢪)',
    'मेरा नाम': 'Anga nutum (𑢁𑢬 𑢳𑢱𑢷𑢳)',
    'my name': 'Anga nutum (𑢁𑢬 𑢳𑢱𑢷𑢳)'
  },
  Kurukh: {
    'नमस्ते': 'Johar / Godey (गोड़े)',
    'hello': 'Johar / Godey (गोड़े)',
    'hi': 'Johar / Godey (गोड़े)',
    'धन्यवाद': 'Dhanyabad / Johar',
    'thank you': 'Dhanyabad / Johar',
    'thanks': 'Dhanyabad / Johar',
    'पानी': 'Daa (दाअ)',
    'water': 'Daa (दाअ)',
    'तुम कैसे हो': 'Nin ekkan men? (नीन एकन मेन?)',
    'how are you': 'Nin ekkan men? (नीन एकन मेन?)',
    'मेरा नाम': 'En naame (एन नामे)',
    'my name': 'En naame (एन नामे)'
  },
  Kharia: {
    'नमस्ते': 'Johar (जोहार)',
    'hello': 'Johar (जोहार)',
    'hi': 'Johar (जोहार)',
    'धन्यवाद': 'Johar / Dhanyabad',
    'thank you': 'Johar / Dhanyabad',
    'thanks': 'Johar / Dhanyabad',
    'पानी': 'Daa (दाअ)',
    'water': 'Daa (दाअ)',
    'तुम कैसे हो': 'Am chetana? (अम चेतना?)',
    'how are you': 'Am chetana? (अम चेतना?)',
    'मेरा नाम': 'Ing nam (इंग नाम)',
    'my name': 'Ing nam (इंग नाम)'
  },
  Khortha: {
    'नमस्ते': 'Johar / Pranam (प्रनाम)',
    'hello': 'Johar / Pranam (प्रनाम)',
    'hi': 'Johar / Pranam (प्रनाम)',
    'धन्यवाद': 'Dhanyabad (धन्यबाद)',
    'thank you': 'Dhanyabad (धन्यबाद)',
    'thanks': 'Dhanyabad (धन्यबाद)',
    'पानी': 'Pani (पानी)',
    'water': 'Pani (पानी)',
    'तुम कैसे हो': 'Tu kaise he? (तोएं केसन ही?)',
    'how are you': 'Tu kaise he? (तोएं केसन ही?)',
    'मेरा नाम': 'Hamar naav (हामर नाव)',
    'my name': 'Hamar naav (हामर नाव)'
  },
  Nagpuri: {
    'नमस्ते': 'Johar / Paylagi (पायलागी)',
    'hello': 'Johar / Paylagi (पायलागी)',
    'hi': 'Johar / Paylagi (पायलागी)',
    'धन्यवाद': 'Dhanyabad (धन्यबाद)',
    'thank you': 'Dhanyabad (धन्यबाद)',
    'thanks': 'Dhanyabad (धन्यबाद)',
    'पानी': 'Pani (पानी)',
    'water': 'Pani (पानी)',
    'तुम कैसे हो': 'Tuin kaise hasa? (तोर का हाल हे?)',
    'how are you': 'Tuin kaise hasa? (तोर का हाल हे?)',
    'मेरा नाम': 'Mor naav (मोर नाव)',
    'my name': 'Mor naav (मोर नाव)'
  },
  Panchpargania: {
    'नमस्ते': 'Johar / Namaskar (नमस्कार)',
    'hello': 'Johar / Namaskar (नमस्कार)',
    'hi': 'Johar / Namaskar (नमस्कार)',
    'धन्यवाद': 'Dhanyabad (धन्यबाद)',
    'thank you': 'Dhanyabad (धन्यबाद)',
    'thanks': 'Dhanyabad (धन्यबाद)',
    'पानी': 'Pani (पानी / जल)',
    'water': 'Pani (पानी / जल)',
    'तुम कैसे हो': 'Tui kemon achis? (तोर केसन हाल?)',
    'how are you': 'Tui kemon achis? (तोर केसन हाल?)',
    'मेरा नाम': 'Mor nam (मोर नाम)',
    'my name': 'Mor nam (मोर नाम)'
  },
  Kurmali: {
    'नमस्ते': 'Johar / Pay Lagon (पांय लागों)',
    'hello': 'Johar / Pay Lagon (पांय लागों)',
    'hi': 'Johar / Pay Lagon (पांय लागों)',
    'धन्यवाद': 'Dhanyabad (धन्यबाद)',
    'thank you': 'Dhanyabad (धन्यबाद)',
    'thanks': 'Dhanyabad (धन्यबाद)',
    'पानी': 'Pani (पानी)',
    'water': 'Pani (पानी)',
    'तुम कैसे हो': 'Tui kemne achis? (तोए केसन आही?)',
    'how are you': 'Tui kemne achis? (तोए केसन आही?)',
    'मेरा नाम': 'Mor nam (मोर नाम)',
    'my name': 'Mor nam (मोर नाम)'
  }
};

const languageData = [
  ['Santhali', 'Austroasiatic language', '🌾', 'c1'],
  ['Mundari', 'Austroasiatic language', '🌳', 'c2'],
  ['Ho', 'Austroasiatic language', '🦋', 'c3'],
  ['Kurukh', 'Dravidian language', '🐘', 'c4'],
  ['Kharia', 'Austroasiatic language', '🌻', 'c5'],
  ['Khortha', 'Regional language', '📚', 'c6'],
  ['Nagpuri', 'Regional language', '🎵', 'c7'],
  ['Panchpargania', 'Regional language', '🌈', 'c8'],
  ['Kurmali', 'Regional language', '🌿', 'c9']
];

// Utility selector helper
const $ = (id) => document.getElementById(id);

const sourceLanguage = $('sourceLanguage');
const hindiText = $('hindiText');
const targetLanguage = $('targetLanguage');
const translatedText = $('translatedText');
const resultLabel = $('resultLabel');
const inputCardLabel = $('inputCardLabel');
const inputTryNote = $('inputTryNote');
let soundEnabled = true;

// Render Language Adventure Grid
if ($('languageGrid')) {
  $('languageGrid').innerHTML = languageData.map(([name, type, sticker, color]) => `
    <article class="lang-card ${color}">
      <span class="sticker">${sticker}</span>
      <h3>${name}</h3>
      <p>${type}</p>
      <button data-language="${name}">Explore words →</button>
    </article>
  `).join('');
}

// Toast Notification
function toast(message) {
  const box = $('toast');
  if (!box) return;
  box.textContent = message;
  box.classList.add('show');
  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => box.classList.remove('show'), 3300);
}

// Sound Synthesis Beep
function beep() {
  if (!soundEnabled || !window.AudioContext) return;
  try {
    const context = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = context.createOscillator();
    const gain = context.createGain();
    oscillator.frequency.value = 580;
    gain.gain.setValueAtTime(.04, context.currentTime);
    gain.gain.exponentialRampToValueAtTime(.001, context.currentTime + .12);
    oscillator.connect(gain);
    gain.connect(context.destination);
    oscillator.start();
    oscillator.stop(context.currentTime + .12);
  } catch (e) {
    // Audio Context restricted or unavailable
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Translation Function connected to backend AI translation service
async function translate() {
  const word = hindiText.value.trim();
  if (!word) {
    translatedText.textContent = 'कृपया अनुवाद के लिए कुछ लिखें (Please enter text)';
    translatedText.classList.add('placeholder');
    return;
  }

  const srcLang = sourceLanguage ? sourceLanguage.value : 'auto';
  const language = targetLanguage.value.toLowerCase();
  resultLabel.textContent = `In ${targetLanguage.value} ⏳`;
  translatedText.textContent = 'अनुवाद हो रहा है... ✨';
  translatedText.classList.remove('placeholder');

  try {
    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: word,
        target_language: language,
        source_language: srcLang
      })
    });

    if (response.ok) {
      const data = await response.json();
      const output = data.native_script || data.translated_text || data.devanagari;
      const phonetic = data.phonetic || data.transliteration;
      const dev = data.devanagari;

      if (output) {
        // Store for speech synthesis
        translatedText.dataset.speakDeva = dev || '';
        translatedText.dataset.speakPhonetic = phonetic || '';
        translatedText.dataset.speakText = output;

        let html = `<div class="native-output-text" style="font-size: 1.35em; font-weight: 700; line-height: 1.45; color: #1b5e20; word-break: break-word;">${escapeHtml(output)}</div>`;
        let subItems = [];

        if (phonetic && phonetic.trim().toLowerCase() !== output.trim().toLowerCase()) {
          subItems.push(`<div style="font-size: 0.88em; color: #424242; margin-top: 6px;"><strong>🔊 उच्चारण (Pronunciation):</strong> <span style="color: #004d40; font-weight: 600;">${escapeHtml(phonetic)}</span></div>`);
        }

        const isIndigenousScript = (language === 'santhali' || language === 'sat' || language === 'ho' || language === 'hoc');
        if (isIndigenousScript && dev && dev.trim().toLowerCase() !== output.trim().toLowerCase()) {
          subItems.push(`<div style="font-size: 0.88em; color: #d84315; margin-top: 4px;"><strong>🔤 देवनागरी लिपि:</strong> <span>${escapeHtml(dev)}</span></div>`);
        }

        if (subItems.length > 0) {
          html += `<div class="script-details" style="margin-top: 10px; padding-top: 8px; border-top: 1px dashed rgba(0,0,0,0.12); text-align: left;">${subItems.join('')}</div>`;
        }

        translatedText.innerHTML = html;
        translatedText.classList.remove('placeholder');
        resultLabel.textContent = `In ${targetLanguage.value} ✨`;
        toast(`Wonderful! Here is your ${targetLanguage.value} translation.`);
        beep();
        return;
      }
    }
  } catch (err) {
    console.warn('Backend translation API error, checking fallback:', err);
  }

  // Fallback to phrasebook if network is unavailable
  const normKey = word.toLowerCase();
  const exact = (phrasebook[targetLanguage.value] && (phrasebook[targetLanguage.value][word] || phrasebook[targetLanguage.value][normKey])) || null;

  if (exact) {
    translatedText.dataset.speakDeva = '';
    translatedText.dataset.speakPhonetic = exact;
    translatedText.dataset.speakText = exact;
    translatedText.textContent = exact;
    translatedText.classList.remove('placeholder');
    resultLabel.textContent = `In ${targetLanguage.value} ✨`;
    toast(`Wonderful! Here is your ${targetLanguage.value} word.`);
    beep();
  } else {
    translatedText.dataset.speakDeva = '';
    translatedText.dataset.speakPhonetic = word;
    translatedText.dataset.speakText = `${word} (${targetLanguage.value})`;
    translatedText.textContent = `${word} (${targetLanguage.value})`;
    translatedText.classList.remove('placeholder');
    resultLabel.textContent = `In ${targetLanguage.value} ✨`;
  }
}

// High-Quality Reliable Speech Synthesis (Zero Hissing, Smooth Human Voice)
let cachedVoices = [];

function loadVoices() {
  if ('speechSynthesis' in window) {
    cachedVoices = window.speechSynthesis.getVoices() || [];
  }
}

if ('speechSynthesis' in window) {
  loadVoices();
  window.speechSynthesis.onvoiceschanged = loadVoices;
}

// Map vernacular Ol Chiki / Ho / tribal scripts to standard pronounceable phonetic words
function getPronounceableText(rawText) {
  if (!rawText) return { text: '', lang: 'hi-IN' };

  // 1. Check data attributes from last translation
  const devAttr = translatedText.dataset.speakDeva;
  const phonAttr = translatedText.dataset.speakPhonetic;

  if (devAttr && devAttr.trim()) {
    return { text: devAttr.trim(), lang: 'hi-IN' };
  }
  if (phonAttr && phonAttr.trim() && /[a-zA-Z\u0900-\u097F]/.test(phonAttr)) {
    return { text: phonAttr.replace(/[^a-zA-Z0-9\u0900-\u097F\s]/g, '').trim(), lang: /[\u0900-\u097F]/.test(phonAttr) ? 'hi-IN' : 'en-IN' };
  }

  // 2. Extract Devanagari or Roman phonetics from HTML or text format
  const devaMatch = rawText.match(/देवनागरी:\s*([^)<>|]+)/);
  if (devaMatch && devaMatch[1]) {
    return { text: devaMatch[1].trim(), lang: 'hi-IN' };
  }

  const pronMatch = rawText.match(/उच्चारण:\s*([^)<>|]+)/);
  if (pronMatch && pronMatch[1]) {
    const p = pronMatch[1].trim();
    return { text: p, lang: /[\u0900-\u097F]/.test(p) ? 'hi-IN' : 'en-IN' };
  }

  // 3. Strip HTML tags, Ol Chiki / Ho unicodes, and parentheses
  let clean = rawText.replace(/<[^>]*>/g, ' ')
                     .replace(/[\u1C50-\u1C7F\u{16860}-\u{1689F}]/gu, '') // Remove Ol Chiki & Warang Citi
                     .replace(/\([^)]*\)/g, ' ') // Remove parenthesized metadata
                     .replace(/[^\w\s\u0900-\u097F]/g, ' ')
                     .replace(/\s+/g, ' ')
                     .trim();

  if (!clean) {
    clean = rawText.replace(/<[^>]*>/g, '').trim();
  }

  const isHindi = /[\u0900-\u097F]/.test(clean);
  return { text: clean, lang: isHindi ? 'hi-IN' : 'en-IN' };
}

async function speak(text, overrideLang) {
  if (!text || !text.trim()) {
    toast('No text to speak.');
    return;
  }

  // Try backend TTS API first
  try {
    const langCode = (targetLanguage.value || 'sat').toLowerCase().slice(0, 3);
    const scriptCode = langCode === 'sat' ? 'olck' : 'deva';
    const cleanWord = text.split('(')[0].replace(/<[^>]*>/g, '').trim();

    const res = await fetch('/api/v1/speech/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: cleanWord,
        language_code: langCode,
        script_code: scriptCode,
        speed: 1.0
      })
    });
    if (res.ok) {
      const data = await res.json();
      if (data.audio_url) {
        const audio = new Audio(data.audio_url);
        audio.play();
        return;
      }
    }
  } catch (e) {
    // Fallback to browser synthesis
  }

  if (!('speechSynthesis' in window)) {
    toast('Speech synthesis is not supported on this browser.');
    return;
  }

  // Unfreeze speech synthesis pipeline in browser
  window.speechSynthesis.cancel();
  if (window.speechSynthesis.paused) {
    window.speechSynthesis.resume();
  }

  const { text: speakable, lang: autoLang } = getPronounceableText(text);
  const targetLang = overrideLang || autoLang || 'hi-IN';

  if (!speakable || !speakable.trim()) {
    toast('Could not find pronounceable audio text.');
    return;
  }

  const utterance = new SpeechSynthesisUtterance(speakable);
  utterance.lang = targetLang;
  utterance.rate = 0.85;
  utterance.pitch = 1.0;
  utterance.volume = 1.0;

  // Select the best natural Indian or language voice
  if (cachedVoices.length === 0) loadVoices();
  if (cachedVoices.length > 0) {
    let chosenVoice = null;
    if (targetLang.startsWith('hi')) {
      chosenVoice = cachedVoices.find(v => v.lang.startsWith('hi') || v.name.includes('Hindi') || v.name.includes('Lekha') || v.name.includes('Rishi'));
    } else if (targetLang.includes('IN') || targetLang.includes('en')) {
      chosenVoice = cachedVoices.find(v => v.lang === 'en-IN' || v.name.includes('India') || v.name.includes('Veena') || v.lang.startsWith('en'));
    }
    if (chosenVoice) {
      utterance.voice = chosenVoice;
    }
  }

  utterance.onstart = () => {
    toast(`🔊 Speaking: "${speakable}"`);
  };

  utterance.onerror = (e) => {
    console.warn('SpeechSynthesis error:', e);
    if (e.error !== 'canceled' && e.error !== 'interrupted') {
      window.speechSynthesis.resume();
    }
  };

  // Safe execution with microtask delay to prevent immediate cancel in Chrome/Safari
  setTimeout(() => {
    window.speechSynthesis.speak(utterance);
    if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }
  }, 20);
}

// Event Listeners
$('translateBtn').addEventListener('click', translate);

hindiText.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    translate();
  }
});

// Source Language Dropdown Change
if (sourceLanguage) {
  sourceLanguage.addEventListener('change', () => {
    const src = sourceLanguage.value;
    if (src === 'eng' || src === 'English') {
      if (inputCardLabel) inputCardLabel.textContent = 'Write in English ✍️';
      if (inputTryNote) inputTryNote.textContent = 'Try: Hello, Thank you, Water';
      hindiText.placeholder = 'e.g.: Hello, Water, Thank you...';
      if (hindiText.value.trim() === 'नमस्ते' || !hindiText.value.trim()) {
        hindiText.value = 'Hello';
      }
    } else if (src === 'hin' || src === 'Hindi') {
      if (inputCardLabel) inputCardLabel.textContent = 'Write in Hindi ✍️';
      if (inputTryNote) inputTryNote.textContent = 'Try: नमस्ते, धन्यवाद, पानी';
      hindiText.placeholder = 'जैसे: नमस्ते, पानी, धन्यवाद...';
      if (hindiText.value.trim() === 'Hello' || !hindiText.value.trim()) {
        hindiText.value = 'नमस्ते';
      }
    } else {
      if (inputCardLabel) inputCardLabel.textContent = 'Write in Hindi / English / Hinglish ✍️';
      if (inputTryNote) inputTryNote.textContent = 'Try: नमस्ते, Water, Ped, Mera naam';
      hindiText.placeholder = 'जैसे: नमस्ते, Water is life, Mera naam Dev hai...';
    }
    translate();
  });
}

targetLanguage.addEventListener('change', translate);

$('speakInput').addEventListener('click', () => {
  const isEng = sourceLanguage && (sourceLanguage.value === 'eng' || sourceLanguage.value === 'English');
  speak(hindiText.value, isEng ? 'en-US' : 'hi-IN');
});

$('speakResult').addEventListener('click', () => {
  const dev = translatedText.dataset.speakDeva;
  const phon = translatedText.dataset.speakPhonetic;
  const txt = translatedText.dataset.speakText || translatedText.textContent;
  speak(dev || phon || txt);
});

$('saveWord').addEventListener('click', () => toast('⭐ Saved! Your word collection is growing.'));

// Swap Button (Toggle between Hindi and English source)
$('swapBtn').addEventListener('click', () => {
  if (!sourceLanguage) return;
  if (sourceLanguage.value === 'hin' || sourceLanguage.value === 'Hindi') {
    sourceLanguage.value = 'eng';
    toast('Source language: English (अंग्रेज़ी)');
  } else if (sourceLanguage.value === 'eng' || sourceLanguage.value === 'English') {
    sourceLanguage.value = 'hin';
    toast('Source language: Hindi (हिन्दी)');
  } else {
    sourceLanguage.value = 'eng';
    toast('Source language: English (अंग्रेज़ी)');
  }
  sourceLanguage.dispatchEvent(new Event('change'));
});

$('soundToggle').addEventListener('click', function() {
  soundEnabled = !soundEnabled;
  this.textContent = soundEnabled ? '🔊' : '🔇';
  toast(soundEnabled ? 'Happy sounds are on!' : 'Happy sounds are off.');
});

$('mobileMenu').addEventListener('click', (e) => {
  e.stopPropagation();
  $('navigation').classList.toggle('open');
});

document.addEventListener('click', (e) => {
  const nav = $('navigation');
  const btn = $('mobileMenu');
  if (nav && nav.classList.contains('open') && !nav.contains(e.target) && e.target !== btn) {
    nav.classList.remove('open');
  }
});

document.querySelectorAll('#navigation a').forEach(a => {
  a.addEventListener('click', () => $('navigation').classList.remove('open'));
});

document.querySelectorAll('[data-language]').forEach(button => {
  button.addEventListener('click', () => {
    targetLanguage.value = button.dataset.language;
    document.querySelector('#translate').scrollIntoView({ behavior: 'smooth' });
    setTimeout(translate, 450);
  });
});

document.querySelectorAll('.game-btn').forEach(button => {
  button.addEventListener('click', () => toast(`🎮 ${button.dataset.game} is coming soon! You can use this card as the next feature in your project.`));
});

/* Sparkling Cursor Trail Effect */
(function initSparkleCursor() {
  let lastTime = 0;
  const sparkles = ['✨', '⭐', '🌟', '💫', '🎈', '💖'];

  function createSparkle(x, y) {
    const now = Date.now();
    if (now - lastTime < 35) return; // Smooth 35ms throttling
    lastTime = now;

    const el = document.createElement('div');
    el.className = 'sparkle-particle';
    el.textContent = sparkles[Math.floor(Math.random() * sparkles.length)];
    el.style.left = x + 'px';
    el.style.top = y + 'px';
    el.style.fontSize = (Math.random() * 10 + 14) + 'px';

    document.body.appendChild(el);

    const deltaX = (Math.random() - 0.5) * 45;
    const deltaY = Math.random() * 30 + 15;
    const rotation = (Math.random() - 0.5) * 90;

    requestAnimationFrame(() => {
      el.style.transform = `translate(calc(-50% + ${deltaX}px), calc(-50% + ${deltaY}px)) scale(0) rotate(${rotation}deg)`;
      el.style.opacity = '0';
    });

    setTimeout(() => {
      if (el.parentNode) el.parentNode.removeChild(el);
    }, 650);
  }

  window.addEventListener('mousemove', (e) => createSparkle(e.clientX, e.clientY));
  window.addEventListener('touchmove', (e) => {
    if (e.touches && e.touches[0]) {
      createSparkle(e.touches[0].clientX, e.touches[0].clientY);
    }
  });
})();
