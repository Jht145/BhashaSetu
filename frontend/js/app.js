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

// Translation Function
function translate() {
  const word = hindiText.value.trim();
  const language = targetLanguage.value;
  const exact = phrasebook[language] ? phrasebook[language][word] : null;

  if (exact) {
    translatedText.textContent = exact;
    translatedText.classList.remove('placeholder');
    resultLabel.textContent = `In ${language} ✨`;
    toast(`Wonderful! Here is your ${language} word.`);
    beep();
  } else {
    translatedText.textContent = `We are still learning “${word || 'this word'}” in ${language}. Try: नमस्ते, धन्यवाद, पानी, तुम कैसे हो, or मेरा नाम.`;
    translatedText.classList.add('placeholder');
    resultLabel.textContent = 'Learning together 🌱';
  }
}

// Speech Synthesis
function speak(text, lang = 'hi-IN') {
  if (!('speechSynthesis' in window)) {
    toast('Audio is not supported by this browser.');
    return;
  }
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = lang;
  utterance.rate = .8;
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
