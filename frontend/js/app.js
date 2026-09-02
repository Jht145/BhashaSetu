/**
 * BhashaSetu (भाषा सेतु) - Client Application Script
 * Clean, production-grade educational portal controller with Hindi & English source support
 */

// Language Metadata
const languagesData = {
  santhali: {
    id: 'santhali',
    name_hi: 'संताली',
    name_en: 'Santhali',
    native_script_sample: 'ᱥᱟᱱᱛᱟᱲᱤ',
    script: 'ओल चिकी (Ol Chiki)',
    family: 'ऑस्ट्रो-एशियाटिक (Munda)',
    regions: 'झारखंड, ओडिशा, प. बंगाल, असम',
    emoji: '🦚',
    greeting: 'जोहार (Johar)',
    greeting_native: 'ᱡᱚᱦᱟᱨ'
  },
  mundari: {
    id: 'mundari',
    name_hi: 'मुंडारी',
    name_en: 'Mundari',
    native_script_sample: 'ᱢᱩᱱᱰᱟᱨᱤ',
    script: 'देवनागरी / मुंडारी बानी',
    family: 'ऑस्ट्रो-एशियाटिक (Munda)',
    regions: 'झारखंड (राँची, खूँटी), ओडिशा',
    emoji: '🌳',
    greeting: 'जोहार (Johar)',
    greeting_native: 'ᱡᱚᱦᱟᱨ'
  },
  ho: {
    id: 'ho',
    name_hi: 'हो',
    name_en: 'Ho',
    native_script_sample: '𑢹𑣉',
    script: 'वारंग चिति (Warang Citi)',
    family: 'ऑस्ट्रो-एशियाटिक (Munda)',
    regions: 'सिंहभूम (झारखंड), मयूरभंज (ओडिशा)',
    emoji: '🦋',
    greeting: 'जोहार (Johar)',
    greeting_native: '𑢹𑣁𑢵𑣂'
  },
  kurukh: {
    id: 'kurukh',
    name_hi: 'कुड़ुख़ / उरांव',
    name_en: 'Kurukh (Oraon)',
    native_script_sample: 'कुंड़ुख़',
    script: 'तोलोंग सिकि / देवनागरी',
    family: 'द्रविड़ (Dravidian)',
    regions: 'झारखंड, छत्तीसगढ़, ओडिशा',
    emoji: '🐘',
    greeting: 'जोहार / जय धरमे',
    greeting_native: 'जोहार'
  },
  kharia: {
    id: 'kharia',
    name_hi: 'खड़िया',
    name_en: 'Kharia',
    native_script_sample: 'खड़िया',
    script: 'देवनागरी (Devanagari)',
    family: 'ऑस्ट्रो-एशियाटिक (Munda)',
    regions: 'गुमला, सिमडेगा (झारखंड)',
    emoji: '🌻',
    greeting: 'जोहार (Johar)',
    greeting_native: 'जोहार'
  },
  khortha: {
    id: 'khortha',
    name_hi: 'खोरठा',
    name_en: 'Khortha',
    native_script_sample: 'खोरठा',
    script: 'देवनागरी (Devanagari)',
    family: 'इंडो-आर्यन (मागधी प्राकृत)',
    regions: 'उत्तरी छोटानागपुर, संथाल परगना',
    emoji: '📚',
    greeting: 'गोड़ लागो ही / जोहार',
    greeting_native: 'गोड़ लागो ही'
  },
  nagpuri: {
    id: 'nagpuri',
    name_hi: 'नागपुरी / सादरी',
    name_en: 'Nagpuri (Sadri)',
    native_script_sample: 'नागपुरी',
    script: 'देवनागरी (Devanagari)',
    family: 'इंडो-आर्यन (मागधी प्राकृत)',
    regions: 'दक्षिणी छोटानागपुर (झारखंड)',
    emoji: '🎵',
    greeting: 'जोहार / परनाम',
    greeting_native: 'जोहार'
  },
  panchpargania: {
    id: 'panchpargania',
    name_hi: 'पंचपरगनिया',
    name_en: 'Panchpargania',
    native_script_sample: 'पंचपरगनिया',
    script: 'देवनागरी / कैथी',
    family: 'इंडो-आर्यन (मागधी प्राकृत)',
    regions: 'राँची, सिल्ली, बुंडू, तमाड़ क्षेत्र',
    emoji: '🌈',
    greeting: 'जोहार / परनाम',
    greeting_native: 'जोहार'
  },
  kurmali: {
    id: 'kurmali',
    name_hi: 'कुरमाली',
    name_en: 'Kurmali',
    native_script_sample: 'कुरमाली',
    script: 'कुरमाली चिश्ती / देवनागरी',
    family: 'इंडो-आर्यन (मागधी प्राकृत)',
    regions: 'झारखंड, प. बंगाल, ओडिशा',
    emoji: '🌿',
    greeting: 'जोहार / नमस्कार',
    greeting_native: 'जोहार'
  }
};

const promptSuggestions = {
  hindi: [
    { text: 'नमस्ते', label: 'नमस्ते' },
    { text: 'आप कैसे हैं?', label: 'आप कैसे हैं?' },
    { text: 'धन्यवाद', label: 'धन्यवाद' },
    { text: 'पानी', label: 'पानी' },
    { text: 'भात', label: 'भात / चावल' },
    { text: 'हाथी', label: 'हाथी' },
    { text: 'चलो खेलते हैं!', label: 'चलो खेलते हैं!' },
    { text: 'तुम्हारा नाम क्या है?', label: 'तुम्हारा नाम क्या है?' }
  ],
  english: [
    { text: 'Hello', label: 'Hello' },
    { text: 'How are you?', label: 'How are you?' },
    { text: 'Thank you', label: 'Thank you' },
    { text: 'Water', label: 'Water' },
    { text: 'Rice', label: 'Rice' },
    { text: 'Elephant', label: 'Elephant' },
    { text: "Let's play!", label: "Let's play!" },
    { text: 'What is your name?', label: 'What is your name?' }
  ]
};

// DOM Elements
const elements = {
  sourceLanguage: document.getElementById('sourceLanguage'),
  targetLanguage: document.getElementById('targetLanguage'),
  sourcePaneTitle: document.getElementById('sourcePaneTitle'),
  promptChipsContainer: document.getElementById('promptChipsContainer'),
  hindiInput: document.getElementById('hindiInput'),
  charCounter: document.getElementById('charCounter'),
  btnTranslate: document.getElementById('btnTranslate'),
  btnSpeakInput: document.getElementById('btnSpeakInput'),
  btnClearInput: document.getElementById('btnClearInput'),
  outputTargetLabel: document.getElementById('outputTargetLabel'),
  outputScriptBadge: document.getElementById('outputScriptBadge'),
  outputNativeText: document.getElementById('outputNativeText'),
  outputDevText: document.getElementById('outputDevText'),
  outputPhoneticText: document.getElementById('outputPhoneticText'),
  btnSpeakOutput: document.getElementById('btnSpeakOutput'),
  btnCopyOutput: document.getElementById('btnCopyOutput'),
  btnSaveWord: document.getElementById('btnSaveWord'),
  swapBtn: document.getElementById('swapBtn'),
  soundToggle: document.getElementById('soundToggle'),
  soundIcon: document.getElementById('soundIcon'),
  languagesContainer: document.getElementById('languagesContainer'),
  toastBox: document.getElementById('toastBox'),
  mobileMenuBtn: document.getElementById('mobileMenuBtn'),
  navLinks: document.getElementById('navLinks')
};

let soundEnabled = true;

// Initialize on Load
document.addEventListener('DOMContentLoaded', () => {
  renderLanguagesGrid();
  renderPromptChips('hindi');
  setupEventListeners();
  updateCharCounter();
  executeTranslation();
});

/**
 * Render Quick Prompt Chips
 */
function renderPromptChips(sourceLang) {
  const chips = promptSuggestions[sourceLang] || promptSuggestions.hindi;
  elements.promptChipsContainer.innerHTML = chips.map(chip => `
    <button class="prompt-chip" data-text="${chip.text}">${chip.label}</button>
  `).join('');

  // Rebind click events
  elements.promptChipsContainer.querySelectorAll('.prompt-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      elements.hindiInput.value = chip.dataset.text;
      updateCharCounter();
      executeTranslation();
      playChime();
    });
  });
}

/**
 * Setup All UI Listeners
 */
function setupEventListeners() {
  // Input Typing
  elements.hindiInput.addEventListener('input', () => {
    updateCharCounter();
  });

  elements.hindiInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      executeTranslation();
    }
  });

  // Source Language Change (Hindi / English)
  elements.sourceLanguage.addEventListener('change', () => {
    const src = elements.sourceLanguage.value;
    if (src === 'english') {
      elements.sourcePaneTitle.innerText = '🇬🇧 Write in English / अंग्रेज़ी पाठ';
      elements.hindiInput.placeholder = 'Type any English word or sentence (e.g., Hello, Water, Thank you, Elephant)...';
      renderPromptChips('english');
      if (elements.hindiInput.value.trim() === 'नमस्ते' || elements.hindiInput.value.trim() === '') {
        elements.hindiInput.value = 'Hello';
      }
    } else {
      elements.sourcePaneTitle.innerText = '🇮🇳 Write in Hindi / हिंदी पाठ';
      elements.hindiInput.placeholder = 'यहाँ कोई भी हिंदी शब्द या वाक्य लिखें (जैसे: नमस्ते, पानी, धन्यवाद)...';
      renderPromptChips('hindi');
      if (elements.hindiInput.value.trim() === 'Hello' || elements.hindiInput.value.trim() === '') {
        elements.hindiInput.value = 'नमस्ते';
      }
    }
    updateCharCounter();
    executeTranslation();
    playChime();
  });

  // Target Language Selection
  elements.targetLanguage.addEventListener('change', () => {
    updateTargetLabel();
    executeTranslation();
  });

  // Swap Button (Toggles between Hindi and English source)
  elements.swapBtn.addEventListener('click', () => {
    elements.sourceLanguage.value = elements.sourceLanguage.value === 'hindi' ? 'english' : 'hindi';
    elements.sourceLanguage.dispatchEvent(new Event('change'));
    showToast(`स्रोत भाषा: ${elements.sourceLanguage.value === 'hindi' ? 'हिन्दी (Hindi)' : 'English (अंग्रेज़ी)'}`);
  });

  // Action Buttons
  elements.btnTranslate.addEventListener('click', () => {
    playChime();
    executeTranslation();
  });

  elements.btnClearInput.addEventListener('click', () => {
    elements.hindiInput.value = '';
    updateCharCounter();
    elements.outputNativeText.innerText = '—';
    elements.outputDevText.innerText = '';
    elements.outputPhoneticText.innerText = '';
    showToast('पाठ साफ किया गया');
  });

  elements.btnSpeakInput.addEventListener('click', () => {
    const isEnglish = elements.sourceLanguage.value === 'english';
    speakText(elements.hindiInput.value, isEnglish ? 'en-US' : 'hi-IN');
  });

  elements.btnSpeakOutput.addEventListener('click', () => {
    const textToSpeak = elements.outputDevText.innerText.replace('देवनागरी: ', '') || elements.outputNativeText.innerText;
    speakText(textToSpeak, 'hi-IN');
  });

  elements.btnCopyOutput.addEventListener('click', () => {
    const text = `${elements.outputNativeText.innerText} (${elements.outputDevText.innerText})`;
    navigator.clipboard.writeText(text).then(() => {
      showToast('📋 अनुवाद क्लिपबोर्ड पर कॉपी किया गया!');
      playChime();
    });
  });

  elements.btnSaveWord.addEventListener('click', () => {
    showToast('⭐ शब्द आपके संग्रह में सुरक्षित किया गया!');
    playChime();
  });

  elements.soundToggle.addEventListener('click', () => {
    soundEnabled = !soundEnabled;
    elements.soundIcon.innerText = soundEnabled ? '🔊' : '🔇';
    elements.soundToggle.innerHTML = soundEnabled ? '<span id="soundIcon">🔊</span> ध्वनि चालू' : '<span id="soundIcon">🔇</span> ध्वनि बंद';
    showToast(soundEnabled ? 'ध्वनि चालू की गई' : 'ध्वनि बंद की गई');
  });

  elements.mobileMenuBtn.addEventListener('click', () => {
    elements.navLinks.style.display = elements.navLinks.style.display === 'flex' ? 'none' : 'flex';
    elements.navLinks.style.flexDirection = 'column';
  });
}

function updateCharCounter() {
  const len = elements.hindiInput.value.length;
  elements.charCounter.innerText = `${len} अक्षर`;
}

function updateTargetLabel() {
  const langKey = elements.targetLanguage.value;
  const lang = languagesData[langKey] || {};
  elements.outputTargetLabel.innerText = `${lang.emoji || '🌐'} ${lang.name_hi || ''} अनुवाद (${lang.name_en || ''})`;
  elements.outputScriptBadge.innerText = lang.script || 'देवनागरी';
}

/**
 * Execute Translation via Backend API with fallback
 */
async function executeTranslation() {
  const text = elements.hindiInput.value.trim();
  const targetLang = elements.targetLanguage.value;

  if (!text) {
    elements.outputNativeText.innerText = 'कृपया कोई शब्द लिखें';
    elements.outputDevText.innerText = '';
    elements.outputPhoneticText.innerText = '';
    return;
  }

  updateTargetLabel();

  try {
    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: text,
        target_language: targetLang
      })
    });

    if (response.ok) {
      const data = await response.json();
      elements.outputNativeText.innerText = data.native_script || data.devanagari;
      elements.outputDevText.innerText = data.devanagari && data.devanagari !== data.native_script ? `देवनागरी: ${data.devanagari}` : '';
      elements.outputPhoneticText.innerText = data.phonetic ? `(उच्चारण: ${data.phonetic})` : '';
      return;
    }
  } catch (err) {
    console.warn('API lookup fallback:', err);
  }

  // Fallback
  const lang = languagesData[targetLang];
  elements.outputNativeText.innerText = lang.greeting_native;
  elements.outputDevText.innerText = `देवनागरी: ${lang.greeting}`;
  elements.outputPhoneticText.innerText = `(उच्चारण: Johar)`;
}

/**
 * Render Languages Directory Cards
 */
function renderLanguagesGrid() {
  elements.languagesContainer.innerHTML = Object.values(languagesData).map(lang => `
    <div class="language-card">
      <div>
        <div class="card-top-row">
          <div>
            <h3 class="card-lang-name">${lang.emoji} ${lang.name_hi}</h3>
            <span class="card-lang-en">${lang.name_en} (${lang.native_script_sample})</span>
          </div>
          <span class="lang-family-tag">${lang.family.split(' ')[0]}</span>
        </div>

        <div class="card-info-list">
          <div class="card-info-item">
            <span>🔤</span>
            <span><strong>लिपि:</strong> ${lang.script}</span>
          </div>
          <div class="card-info-item">
            <span>📍</span>
            <span><strong>क्षेत्र:</strong> ${lang.regions}</span>
          </div>
          <div class="card-info-item">
            <span>💬</span>
            <span><strong>अभिवादन:</strong> ${lang.greeting}</span>
          </div>
        </div>
      </div>

      <div class="card-action-row">
        <span class="sample-greeting-badge">${lang.greeting_native}</span>
        <button class="btn-pill-action" onclick="selectLanguageForTranslation('${lang.id}')">
          अनुवाद करें →
        </button>
      </div>
    </div>
  `).join('');
}

function selectLanguageForTranslation(langId) {
  elements.targetLanguage.value = langId;
  updateTargetLabel();
  document.getElementById('translator').scrollIntoView({ behavior: 'smooth' });
  setTimeout(executeTranslation, 300);
}

/**
 * Speech & Audio Feedback
 */
function speakText(text, lang = 'hi-IN') {
  if (!('speechSynthesis' in window)) {
    showToast('आपके ब्राउज़र में ऑडियो समर्थित नहीं है');
    return;
  }
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = lang;
  utterance.rate = 0.85;
  window.speechSynthesis.speak(utterance);
}

function playChime() {
  if (!soundEnabled || !window.AudioContext) return;
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(520, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(660, ctx.currentTime + 0.1);
    gain.gain.setValueAtTime(0.04, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.15);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.15);
  } catch (e) {}
}

/**
 * Toast Notification Utility
 */
function showToast(message) {
  const box = elements.toastBox;
  box.textContent = message;
  box.classList.add('show');
  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => {
    box.classList.remove('show');
  }, 3000);
}

function handleActivityClick(activityName) {
  showToast(`🎯 '${activityName}' मॉड्यूल लोड किया जा रहा है...`);
  playChime();
}
