/**
 * BhashaSetu Cosmic Space Audio Synthesizer & Speech Engine
 * Playful sci-fi space sounds & friendly speech synthesis
 */

class SoundEffects {
    constructor() {
        this.ctx = null;
        this.enabled = true;
    }

    _init() {
        if (!this.ctx) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (AudioContext) {
                this.ctx = new AudioContext();
            }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    playLaser() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(880, now);
        osc.frequency.exponentialRampToValueAtTime(110, now + 0.12);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now);
        osc.stop(now + 0.12);
    }

    playPop() {
        this.playLaser();
    }

    playBoing() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(320, now);
        osc.frequency.exponentialRampToValueAtTime(960, now + 0.1);
        osc.frequency.exponentialRampToValueAtTime(440, now + 0.2);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now);
        osc.stop(now + 0.2);
    }

    playXylophone() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const freqs = [659.25, 783.99, 1046.50, 1318.51]; // Starlight chimes
        const randomFreq = freqs[Math.floor(Math.random() * freqs.length)];

        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(randomFreq, now);

        gain.gain.setValueAtTime(0.35, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now);
        osc.stop(now + 0.35);
    }

    playSuccess() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51, 1567.98]; // Cosmic warp chime

        notes.forEach((freq, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const start = now + (i * 0.07);

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, start);

            gain.gain.setValueAtTime(0.28, start);
            gain.gain.exponentialRampToValueAtTime(0.001, start + 0.28);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(start);
            osc.stop(start + 0.28);
        });
    }

    playFanfare() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const notes = [523.25, 523.25, 523.25, 659.25, 783.99, 1046.50, 1318.51, 1567.98];
        const times = [0, 0.12, 0.24, 0.36, 0.48, 0.65, 0.85, 1.05];
        const durations = [0.1, 0.1, 0.1, 0.1, 0.15, 0.2, 0.3, 0.6];

        notes.forEach((freq, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const start = now + times[i];
            const dur = durations[i];

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, start);

            gain.gain.setValueAtTime(0.35, start);
            gain.gain.exponentialRampToValueAtTime(0.01, start + dur);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(start);
            osc.stop(start + dur);
        });
    }

    playWrong() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(260, now);
        osc.frequency.exponentialRampToValueAtTime(120, now + 0.3);

        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now);
        osc.stop(now + 0.3);
    }

    playGiggle() {
        if (!this.enabled) return;
        this._init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        for (let i = 0; i < 7; i++) {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const start = now + (i * 0.055);

            osc.type = 'sine';
            const freq = (i % 2 === 0) ? 700 : 950;
            osc.frequency.setValueAtTime(freq, start);

            gain.gain.setValueAtTime(0.2, start);
            gain.gain.exponentialRampToValueAtTime(0.01, start + 0.05);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(start);
            osc.stop(start + 0.05);
        }
    }
}

const soundFx = new SoundEffects();

let currentSpeechRate = 0.85;

function setSpeechSpeed(speed) {
    currentSpeechRate = speed;
}

function speakUtterance(text, lang = 'hi-IN') {
    if (!('speechSynthesis' in window)) {
        alert("Audio speech synthesis is not supported on this browser.");
        return;
    }

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    utterance.rate = currentSpeechRate;
    utterance.pitch = 1.25; // Playful astronaut voice

    const voices = window.speechSynthesis.getVoices();
    const matchVoice = voices.find(v => v.lang.startsWith('hi') || v.lang === 'hi-IN' || v.lang.includes('IN'));
    if (matchVoice) {
        utterance.voice = matchVoice;
    }

    window.speechSynthesis.speak(utterance);
}
