/**
 * BhashaSetu (भाषा सेतु) - Client Application Script
 * Type: JS (JavaScript)
 */

// Phrasebook Data
const phrasebook = {
  Santhali: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Johar / धन्यवाद',
    'पानी': 'Daak\' / Water',
    'तुम कैसे हो': 'Chet kana me?',
    'मेरा नाम': 'Injań ñutum'
  },
  Mundari: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Johar',
    'पानी': 'Da\' / Water',
    'तुम कैसे हो': 'Am chetana?',
    'मेरा नाम': 'Aing ren nutum'
  },
  Ho: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Johar',
    'पानी': 'Da\'',
    'तुम कैसे हो': 'Am chekana?',
    'मेरा नाम': 'Anga nutum'
  },
  Kurukh: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Dhanyabad',
    'पानी': 'Daa',
    'तुम कैसे हो': 'Nin ekkan men?',
    'मेरा नाम': 'En naame'
  },
  Kharia: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Johar',
    'पानी': 'Daa',
    'तुम कैसे हो': 'Am chetana?',
    'मेरा नाम': 'Ing nam'
  },
  Khortha: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Dhanyabad',
    'पानी': 'Pani',
    'तुम कैसे हो': 'Tu kaise he?',
    'मेरा नाम': 'Hamar naav'
  },
  Nagpuri: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Dhanyabad',
    'पानी': 'Pani',
    'तुम कैसे हो': 'Tuin kaise hasa?',
    'मेरा नाम': 'Mor naav'
  },
  Panchpargania: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Dhanyabad',
    'पानी': 'Pani',
    'तुम कैसे हो': 'Tui kemon achis?',
    'मेरा नाम': 'Mor nam'
  },
  Kurmali: {
    'नमस्ते': 'Johar',
    'धन्यवाद': 'Dhanyabad',
    'पानी': 'Pani',
    'तुम कैसे हो': 'Tui kemne achis?',
    'मेरा नाम': 'Mor nam'
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

const hindiText = $('hindiText');
const targetLanguage = $('targetLanguage');
const translatedText = $('translatedText');
const resultLabel = $('resultLabel');
let soundEnabled = true;

// Render Language Adventure Grid
$('languageGrid').innerHTML = languageData.map(([name, type, sticker, color]) => `
  <article class="lang-card ${color}">
    <span class="sticker">${sticker}</span>
    <h3>${name}</h3>
    <p>${type}</p>
    <button data-language="${name}">Explore words →</button>
  </article>
`).join('');

// Toast Notification
function toast(message) {
  const box = $('toast');
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
        source_language: 'hin_Deva'
      })
    });

    if (response.ok) {
      const data = await response.json();
      const output = data.native_script || data.translated_text || data.devanagari;
      const phonetic = data.phonetic || data.transliteration;
      const dev = data.devanagari;

      if (output) {
        if (phonetic && phonetic !== output && (language === 'santhali' || language === 'sat')) {
          translatedText.innerHTML = `<span class="native-out" style="font-size: 1.15em; font-weight: 600;">${escapeHtml(output)}</span><br><small style="font-size: 0.85em; opacity: 0.85; display: inline-block; margin-top: 4px;">(उच्चारण: ${escapeHtml(phonetic)}${dev && dev !== output ? ' | देवनागरी: ' + escapeHtml(dev) : ''})</small>`;
        } else if (dev && dev !== output) {
          translatedText.innerHTML = `<span class="native-out" style="font-size: 1.15em; font-weight: 600;">${escapeHtml(output)}</span><br><small style="font-size: 0.85em; opacity: 0.85; display: inline-block; margin-top: 4px;">(देवनागरी: ${escapeHtml(dev)})</small>`;
        } else {
          translatedText.textContent = output;
        }

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
  const exact = phrasebook[targetLanguage.value] ? phrasebook[targetLanguage.value][word] : null;
  if (exact) {
    translatedText.textContent = exact;
    translatedText.classList.remove('placeholder');
    resultLabel.textContent = `In ${targetLanguage.value} ✨`;
    toast(`Wonderful! Here is your ${targetLanguage.value} word.`);
    beep();
  } else {
    translatedText.textContent = `${word} (${targetLanguage.value})`;
    translatedText.classList.remove('placeholder');
    resultLabel.textContent = `In ${targetLanguage.value} ✨`;
  }
}

// Speech Synthesis with Backend Vernacular TTS Audio + Browser Fallback
async function speak(text, lang = 'hi-IN') {
  if (!text || !text.trim()) return;
  const clean = text.split('(')[0].replace(/[^a-zA-Z0-9\u0900-\u097F\u1C50-\u1C7F\s]/g, '').trim();
  
  try {
    const langCode = (targetLanguage.value || 'sat').toLowerCase().slice(0, 3);
    const scriptCode = langCode === 'sat' ? 'olck' : 'deva';
    const res = await fetch('/api/v1/speech/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: clean,
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
    toast('Audio playback is not supported by this browser.');
    return;
  }
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(clean);
  utterance.lang = lang;
  utterance.rate = 0.85;
  window.speechSynthesis.speak(utterance);
}

// Event Listeners
$('translateBtn').addEventListener('click', translate);

hindiText.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    translate();
  }
});

targetLanguage.addEventListener('change', translate);

$('speakInput').addEventListener('click', () => speak(hindiText.value, 'hi-IN'));
$('speakResult').addEventListener('click', () => speak(translatedText.textContent));

$('saveWord').addEventListener('click', () => toast('⭐ Saved! Your word collection is growing.'));
$('swapBtn').addEventListener('click', () => toast('Hindi is the starting language for this BhashaSetu prototype.'));

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
