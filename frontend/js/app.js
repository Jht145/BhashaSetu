/**
 * BhashaSetu (भाषा सेतु) - Client Application Script
 * Robust, accessible client controller for vernacular translation and learning
 */

// Global state
let soundEnabled = true;
let isTranslating = false;
let currentAbortController = null;
let lastSuccessfulOutput = null;
let lastInputText = '';

// Prompt suggestions mapped by source language
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

// DOM Element References
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
  outputDisplay: document.getElementById('outputDisplay'),
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

// Initialize Application on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  renderLanguagesGrid();
  renderPromptChips('hindi');
  setupEventListeners();
  updateCharCounter();
  lastInputText = elements.hindiInput.value;
  executeTranslation();
});

/**
 * Render Quick Prompt Chips
 */
function renderPromptChips(sourceLang) {
  const chips = promptSuggestions[sourceLang] || promptSuggestions.hindi;
  if (!elements.promptChipsContainer) return;

  elements.promptChipsContainer.innerHTML = chips.map(chip => `
    <button class="prompt-chip" data-text="${escapeHtml(chip.text)}" aria-label="सुझाव: ${escapeHtml(chip.label)}">${escapeHtml(chip.label)}</button>
  `).join('');

  elements.promptChipsContainer.querySelectorAll('.prompt-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      elements.hindiInput.value = chip.dataset.text;
      updateCharCounter();
      lastInputText = elements.hindiInput.value;
      executeTranslation();
      playChime();
    });
  });
}

/**
 * Clear Stale Output Display
 */
function clearTranslationOutput() {
  if (elements.outputNativeText) {
    elements.outputNativeText.innerText = '—';
    elements.outputNativeText.classList.remove('ol-chiki-font');
  }
  if (elements.outputDevText) {
    elements.outputDevText.innerText = '';
  }
  if (elements.outputPhoneticText) {
    elements.outputPhoneticText.innerText = '';
  }
  lastSuccessfulOutput = null;
}

/**
 * Setup All UI Event Listeners
 */
function setupEventListeners() {
  // Input Typing and Counter
  elements.hindiInput.addEventListener('input', () => {
    updateCharCounter();
    const currentVal = elements.hindiInput.value;
    // If input is significantly changed or cleared, clear stale output
    if (Math.abs(currentVal.length - lastInputText.length) > 3 || currentVal.trim() === '') {
      clearTranslationOutput();
    }
    lastInputText = currentVal;
  });

  elements.hindiInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      executeTranslation();
    }
  });

  // Source Language Change
  elements.sourceLanguage.addEventListener('change', () => {
    const srcKey = elements.sourceLanguage.value;
    clearTranslationOutput();

    if (srcKey === 'english') {
      elements.sourcePaneTitle.innerText = '🇬🇧 Write in English / अंग्रेज़ी पाठ';
      elements.hindiInput.placeholder = 'Type any English word or sentence (e.g., Hello, Water, Thank you, Elephant)...';
      elements.hindiInput.setAttribute('aria-label', 'Enter English text to translate');
      renderPromptChips('english');
      if (elements.hindiInput.value.trim() === 'नमस्ते' || elements.hindiInput.value.trim() === '') {
        elements.hindiInput.value = 'Hello';
      }
    } else {
      elements.sourcePaneTitle.innerText = '🇮🇳 Write in Hindi / हिंदी पाठ';
      elements.hindiInput.placeholder = 'यहाँ कोई भी हिंदी शब्द या वाक्य लिखें (जैसे: नमस्ते, पानी, धन्यवाद)...';
      elements.hindiInput.setAttribute('aria-label', 'अनुवाद के लिए हिंदी पाठ दर्ज करें');
      renderPromptChips('hindi');
      if (elements.hindiInput.value.trim() === 'Hello' || elements.hindiInput.value.trim() === '') {
        elements.hindiInput.value = 'नमस्ते';
      }
    }
    updateCharCounter();
    lastInputText = elements.hindiInput.value;
    updateTargetLabel();
    executeTranslation();
    playChime();
  });

  // Target Language Selection
  elements.targetLanguage.addEventListener('change', () => {
    clearTranslationOutput();
    updateTargetLabel();
    executeTranslation();
  });

  // Swap Button (Toggles Source between Hindi and English)
  elements.swapBtn.addEventListener('click', () => {
    elements.sourceLanguage.value = elements.sourceLanguage.value === 'hindi' ? 'english' : 'hindi';
    elements.sourceLanguage.dispatchEvent(new Event('change'));
    showToast(`स्रोत भाषा: ${elements.sourceLanguage.value === 'hindi' ? 'हिन्दी (Hindi)' : 'English (अंग्रेज़ी)'}`);
  });

  // Translate Action Button
  elements.btnTranslate.addEventListener('click', () => {
    playChime();
    executeTranslation();
  });

  // Clear Input Button
  elements.btnClearInput.addEventListener('click', () => {
    elements.hindiInput.value = '';
    updateCharCounter();
    lastInputText = '';
    clearTranslationOutput();
    showToast('पाठ साफ किया गया');
  });

  // Speech for Input Text
  elements.btnSpeakInput.addEventListener('click', () => {
    const text = elements.hindiInput.value.trim();
    if (!text) {
      showToast('सुनने के लिए कोई पाठ नहीं है');
      return;
    }
    const srcConfig = getSourceLanguageConfig(elements.sourceLanguage.value);
    speakText(text, srcConfig.voiceLocale || 'hi-IN');
  });

  // Speech for Output Translation
  elements.btnSpeakOutput.addEventListener('click', () => {
    if (!lastSuccessfulOutput) {
      showToast('सुनने के लिए कोई मान्य अनुवाद उपलब्ध नहीं है');
      return;
    }
    const textToSpeak = lastSuccessfulOutput.devanagari || lastSuccessfulOutput.native || lastSuccessfulOutput.text;
    if (textToSpeak && textToSpeak !== '—') {
      speakText(textToSpeak, 'hi-IN');
    } else {
      showToast('सुनने के लिए कोई मान्य अनुवाद उपलब्ध नहीं है');
    }
  });

  // Copy Translation to Clipboard
  elements.btnCopyOutput.addEventListener('click', () => {
    if (!lastSuccessfulOutput || !lastSuccessfulOutput.native || lastSuccessfulOutput.native === '—') {
      showToast('कॉपी करने के लिए कोई मान्य अनुवाद उपलब्ध नहीं है');
      return;
    }
    const textToCopy = lastSuccessfulOutput.devanagari && lastSuccessfulOutput.devanagari !== lastSuccessfulOutput.native
      ? `${lastSuccessfulOutput.native} (${lastSuccessfulOutput.devanagari})`
      : lastSuccessfulOutput.native;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('📋 अनुवाद क्लिपबोर्ड पर कॉपी किया गया!');
        playChime();
      }).catch(() => {
        fallbackCopyText(textToCopy);
      });
    } else {
      fallbackCopyText(textToCopy);
    }
  });

  // Save Word Action
  elements.btnSaveWord.addEventListener('click', () => {
    if (!lastSuccessfulOutput || !lastSuccessfulOutput.native || lastSuccessfulOutput.native === '—') {
      showToast('सहेजने के लिए कोई मान्य अनुवाद उपलब्ध नहीं है');
      return;
    }
    showToast('⭐ शब्द आपके संग्रह में सुरक्षित किया गया!');
    playChime();
  });

  // Sound Toggle
  elements.soundToggle.addEventListener('click', () => {
    soundEnabled = !soundEnabled;
    elements.soundIcon.innerText = soundEnabled ? '🔊' : '🔇';
    elements.soundToggle.innerHTML = soundEnabled ? '<span id="soundIcon">🔊</span> ध्वनि चालू' : '<span id="soundIcon">🔇</span> ध्वनि बंद';
    showToast(soundEnabled ? 'ध्वनि चालू की गई' : 'ध्वनि बंद की गई');
  });

  // Mobile Menu Toggle
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
  const targetKey = elements.targetLanguage.value;
  const targetConfig = getTargetLanguageConfig(targetKey);
  elements.outputTargetLabel.innerText = `${targetConfig.emoji || '🌐'} ${targetConfig.name_hi || ''} अनुवाद (${targetConfig.name_en || ''})`;
  elements.outputScriptBadge.innerText = targetConfig.script || 'देवनागरी';
}

/**
 * Execute Safe Translation via Backend API
 */
async function executeTranslation() {
  // Prevent duplicate concurrent calls
  if (isTranslating) return;

  const rawText = elements.hindiInput.value;
  const trimmedText = rawText.trim();
  const sourceKey = elements.sourceLanguage.value;
  const targetKey = elements.targetLanguage.value;

  const sourceConfig = getSourceLanguageConfig(sourceKey);
  const targetConfig = getTargetLanguageConfig(targetKey);

  // 1. Validation: Empty or whitespace-only input
  if (!trimmedText) {
    clearTranslationOutput();
    showToast('कृपया अनुवाद के लिए कोई शब्द या वाक्य लिखें।');
    return;
  }

  // 2. Validation: Source and Target cannot be identical
  if (sourceConfig.code === targetConfig.code || sourceConfig.id === targetConfig.id) {
    clearTranslationOutput();
    showToast('स्रोत और लक्ष्य भाषा समान नहीं हो सकतीं।');
    return;
  }

  // 3. Validation: Unsupported target-language route
  if (!isTargetLanguageSupported(targetKey)) {
    clearTranslationOutput();
    showToast('Translation for this language is not available yet.');
    return;
  }

  updateTargetLabel();

  // Abort any ongoing pending request
  if (currentAbortController) {
    currentAbortController.abort();
  }
  currentAbortController = new AbortController();
  const timeoutId = setTimeout(() => currentAbortController.abort(), 30000); // 30s timeout

  isTranslating = true;
  elements.btnTranslate.setAttribute('aria-busy', 'true');

  try {
    const payload = {
      text: trimmedText,
      source_language: sourceConfig.code,
      target_language: targetConfig.code
    };

    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      signal: currentAbortController.signal
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    let data;
    try {
      data = await response.json();
    } catch (parseErr) {
      throw new Error('Malformed server response');
    }

    // Validate translation output structure
    const translatedText = data.translated_text || data.native_script || data.devanagari;
    const isSuccess = data.success !== false && Boolean(translatedText && translatedText.trim());

    if (!isSuccess) {
      throw new Error('Translation returned empty result');
    }

    const nativeOutput = data.native_script || data.translated_text || data.devanagari;
    const devanagariOutput = data.devanagari || (data.phonetic_devanagari ? data.phonetic_devanagari : '');
    const phoneticOutput = data.phonetic || data.transliteration || '';

    // Render result safely in the UI
    elements.outputNativeText.innerText = nativeOutput;
    elements.outputDevText.innerText = (devanagariOutput && devanagariOutput !== nativeOutput)
      ? `देवनागरी: ${devanagariOutput}`
      : '';
    elements.outputPhoneticText.innerText = phoneticOutput
      ? `(उच्चारण: ${phoneticOutput})`
      : '';

    // Apply Ol Chiki font class specifically for Santhali in Ol Chiki script
    if (targetConfig.code === 'sat_Olck' || targetConfig.id === 'santhali') {
      elements.outputNativeText.classList.add('ol-chiki-font');
    } else {
      elements.outputNativeText.classList.remove('ol-chiki-font');
    }

    // Save active valid output state
    lastSuccessfulOutput = {
      native: nativeOutput,
      devanagari: devanagariOutput,
      phonetic: phoneticOutput,
      text: translatedText,
      targetLang: targetConfig.id,
      requestId: data.request_id || null
    };

    // Quality Flags and Method Notifications
    if (data.translation_method === 'pivot_en_hi_tribal') {
      showToast('Hindi-assisted translation used. Please verify important educational content.');
    }

    const unverifiedFlags = [
      'missing_expected_script',
      'empty_output',
      'output_same_as_source',
      'unknown_token',
      'unresolved_placeholder',
      'unsupported_language_route'
    ];

    if (Array.isArray(data.quality_flags) && data.quality_flags.some(f => unverifiedFlags.includes(f))) {
      console.warn('Translation quality flags detected:', data.quality_flags);
    }

  } catch (err) {
    if (err.name === 'AbortError') {
      showToast('अनुरोध समय समाप्त (Request timed out). कृपया पुनः प्रयास करें।');
    } else {
      console.warn('Translation request issue:', err);
      // Fallback greeting only if input matches initial greeting, otherwise clear
      if (trimmedText.toLowerCase() === 'hello' || trimmedText === 'नमस्ते') {
        const langFallback = getTargetLanguageConfig(targetKey);
        elements.outputNativeText.innerText = langFallback.greeting_native || '—';
        elements.outputDevText.innerText = `देवनागरी: ${langFallback.greeting || ''}`;
        elements.outputPhoneticText.innerText = '(उच्चारण: Johar)';
        lastSuccessfulOutput = {
          native: langFallback.greeting_native,
          devanagari: langFallback.greeting,
          phonetic: 'Johar',
          text: langFallback.greeting_native,
          targetLang: targetKey
        };
      } else {
        clearTranslationOutput();
        showToast('अनुवाद सेवा से संपर्क नहीं हो सका। कृपया पुनः प्रयास करें।');
      }
    }
  } finally {
    isTranslating = false;
    currentAbortController = null;
    elements.btnTranslate.removeAttribute('aria-busy');
  }
}

/**
 * Render Languages Directory Cards
 */
function renderLanguagesGrid() {
  if (!elements.languagesContainer) return;
  const targets = Object.values(LANGUAGE_CONFIG.targets);

  elements.languagesContainer.innerHTML = targets.map(lang => `
    <div class="language-card">
      <div>
        <div class="card-top-row">
          <div>
            <h3 class="card-lang-name">${escapeHtml(lang.emoji)} ${escapeHtml(lang.name_hi)}</h3>
            <span class="card-lang-en">${escapeHtml(lang.name_en)} (${escapeHtml(lang.native_script_sample)})</span>
          </div>
          <span class="lang-family-tag">${escapeHtml(lang.family.split(' ')[0])}</span>
        </div>

        <div class="card-info-list">
          <div class="card-info-item">
            <span>🔤</span>
            <span><strong>लिपि:</strong> ${escapeHtml(lang.script)}</span>
          </div>
          <div class="card-info-item">
            <span>📍</span>
            <span><strong>क्षेत्र:</strong> ${escapeHtml(lang.regions)}</span>
          </div>
          <div class="card-info-item">
            <span>💬</span>
            <span><strong>अभिवादन:</strong> ${escapeHtml(lang.greeting)}</span>
          </div>
        </div>
      </div>

      <div class="card-action-row">
        <span class="sample-greeting-badge">${escapeHtml(lang.greeting_native)}</span>
        <button class="btn-pill-action" onclick="selectLanguageForTranslation('${escapeHtml(lang.id)}')" aria-label="${escapeHtml(lang.name_hi)} में अनुवाद करें">
          अनुवाद करें →
        </button>
      </div>
    </div>
  `).join('');
}

function selectLanguageForTranslation(langId) {
  elements.targetLanguage.value = langId;
  clearTranslationOutput();
  updateTargetLabel();
  const translatorSec = document.getElementById('translator');
  if (translatorSec) {
    translatorSec.scrollIntoView({ behavior: 'smooth' });
  }
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
  if (!box) return;
  box.textContent = message;
  box.setAttribute('role', 'alert');
  box.classList.add('show');
  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => {
    box.classList.remove('show');
  }, 3200);
}

function fallbackCopyText(text) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.style.position = 'fixed';
  textArea.style.opacity = '0';
  document.body.appendChild(textArea);
  textArea.select();
  try {
    document.execCommand('copy');
    showToast('📋 अनुवाद क्लिपबोर्ड पर कॉपी किया गया!');
    playChime();
  } catch (e) {
    showToast('कॉपी करने में त्रुटि हुई');
  }
  document.body.removeChild(textArea);
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

function handleActivityClick(activityName) {
  showToast(`🎯 '${activityName}' मॉड्यूल लोड किया जा रहा है...`);
  playChime();
}

/**
 * TODO: Connect translation feedback reporting when a public feedback API endpoint
 * (e.g. POST /api/v1/translation/feedback) is exposed by the backend.
 * Payload specification:
 * {
 *   source_text: string,
 *   source_language: string,
 *   target_language: string,
 *   machine_translation: string,
 *   translation_method: string,
 *   quality_flags: Array<string>
 * }
 */
