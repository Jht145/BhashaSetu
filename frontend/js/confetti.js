/**
 * BhashaSetu Pastel Celebration Engine
 */

class ConfettiLauncher {
    constructor() {
        this.canvas = null;
        this.ctx = null;
        this.particles = [];
        this.animationFrame = null;
        this.initCursorSparkles();
    }

    _setupCanvas() {
        if (!this.canvas) {
            this.canvas = document.createElement('canvas');
            this.canvas.id = 'confetti-canvas';
            this.canvas.style.position = 'fixed';
            this.canvas.style.top = '0';
            this.canvas.style.left = '0';
            this.canvas.style.width = '100vw';
            this.canvas.style.height = '100vh';
            this.canvas.style.pointerEvents = 'none';
            this.canvas.style.zIndex = '99999';
            document.body.appendChild(this.canvas);
            this.ctx = this.canvas.getContext('2d');
            this._resize();
            window.addEventListener('resize', () => this._resize());
        }
    }

    _resize() {
        if (this.canvas) {
            this.canvas.width = window.innerWidth;
            this.canvas.height = window.innerHeight;
        }
    }

    launch(count = 70) {
        this._setupCanvas();
        // Exact reference palette: #99CDD8, #DAEBE3, #FDE8D3, #F3C3B2, #CFD6C4, #657166
        const colors = ['#99CDD8', '#DAEBE3', '#FDE8D3', '#F3C3B2', '#CFD6C4', '#F8B39F', '#87C0CD'];
        const shapes = ['circle', 'star', 'bubble'];

        for (let i = 0; i < count; i++) {
            this.particles.push({
                x: window.innerWidth * 0.5 + (Math.random() - 0.5) * 240,
                y: window.innerHeight * 0.4,
                vx: (Math.random() - 0.5) * 14,
                vy: Math.random() * -12 - 4,
                size: Math.random() * 9 + 6,
                color: colors[Math.floor(Math.random() * colors.length)],
                shape: shapes[Math.floor(Math.random() * shapes.length)],
                rotation: Math.random() * 360,
                rotationSpeed: (Math.random() - 0.5) * 10,
                gravity: 0.32,
                opacity: 1,
                decay: Math.random() * 0.015 + 0.008
            });
        }

        if (!this.animationFrame) {
            this._animate();
        }
    }

    _animate() {
        if (!this.ctx || !this.canvas) return;

        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        for (let i = this.particles.length - 1; i >= 0; i--) {
            const p = this.particles[i];
            p.x += p.vx;
            p.y += p.vy;
            p.vy += p.gravity;
            p.rotation += p.rotationSpeed;
            p.opacity -= p.decay;

            if (p.opacity <= 0 || p.y > window.innerHeight + 50) {
                this.particles.splice(i, 1);
                continue;
            }

            this.ctx.save();
            this.ctx.globalAlpha = Math.max(0, p.opacity);
            this.ctx.translate(p.x, p.y);
            this.ctx.rotate((p.rotation * Math.PI) / 180);
            this.ctx.fillStyle = p.color;

            if (p.shape === 'star') {
                this._drawStar(this.ctx, 0, 0, 5, p.size, p.size / 2);
            } else {
                this.ctx.beginPath();
                this.ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
                this.ctx.fill();
            }

            this.ctx.restore();
        }

        if (this.particles.length > 0) {
            this.animationFrame = requestAnimationFrame(() => this._animate());
        } else {
            this.animationFrame = null;
            if (this.ctx && this.canvas) {
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            }
        }
    }

    _drawStar(ctx, cx, cy, spikes, outerRadius, innerRadius) {
        let rot = (Math.PI / 2) * 3;
        let x = cx;
        let y = cy;
        const step = Math.PI / spikes;

        ctx.beginPath();
        ctx.moveTo(cx, cy - outerRadius);
        for (let i = 0; i < spikes; i++) {
            x = cx + Math.cos(rot) * outerRadius;
            y = cy + Math.sin(rot) * outerRadius;
            ctx.lineTo(x, y);
            rot += step;

            x = cx + Math.cos(rot) * innerRadius;
            y = cy + Math.sin(rot) * innerRadius;
            ctx.lineTo(x, y);
            rot += step;
        }
        ctx.lineTo(cx, cy - outerRadius);
        ctx.closePath();
        ctx.fill();
    }

    initCursorSparkles() {
        let lastTime = 0;
        const spawnSparkle = (x, y) => {
            const now = Date.now();
            if (now - lastTime < 50) return;
            lastTime = now;

            const sparkle = document.createElement('div');
            sparkle.innerText = ['✨', '🌸', '⭐', '🎈', '💖'][Math.floor(Math.random() * 5)];
            sparkle.style.position = 'fixed';
            sparkle.style.left = `${x - 10}px`;
            sparkle.style.top = `${y - 10}px`;
            sparkle.style.fontSize = `${Math.random() * 14 + 12}px`;
            sparkle.style.pointerEvents = 'none';
            sparkle.style.zIndex = '99998';
            sparkle.style.transition = 'all 0.5s ease-out';
            sparkle.style.transform = `translate(0, 0) scale(1)`;
            document.body.appendChild(sparkle);

            const destX = (Math.random() - 0.5) * 40;
            const destY = Math.random() * 30 + 15;

            requestAnimationFrame(() => {
                sparkle.style.transform = `translate(${destX}px, ${destY}px) scale(0)`;
                sparkle.style.opacity = '0';
            });

            setTimeout(() => {
                if (sparkle.parentNode) sparkle.parentNode.removeChild(sparkle);
            }, 500);
        };

        window.addEventListener('mousemove', (e) => spawnSparkle(e.clientX, e.clientY));
        window.addEventListener('touchmove', (e) => {
            if (e.touches && e.touches[0]) {
                spawnSparkle(e.touches[0].clientX, e.touches[0].clientY);
            }
        });
    }
}

const confetti = new ConfettiLauncher();
