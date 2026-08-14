(() => {
  const canvas = document.querySelector('#stickerCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const upload = document.querySelector('#stickerUpload');
  const topText = document.querySelector('#topText');
  const bottomText = document.querySelector('#bottomText');
  const style = document.querySelector('#stickerStyle');
  const zoom = document.querySelector('#stickerZoom');
  const download = document.querySelector('#downloadSticker');
  const status = document.querySelector('#stickerStatus');
  let image = null;

  const themes = {
    classic: { bg: '#ffd24a', ink: '#111111', accent: '#e94b2c' },
    neon: { bg: '#27124c', ink: '#ffffff', accent: '#57f5c6' },
    pitch: { bg: '#0a5b35', ink: '#ffffff', accent: '#d7ff5f' },
    clean: { bg: '#f4f5f6', ink: '#111111', accent: '#3ddc84' }
  };
  const fit = (text, max, font) => {
    let size = font;
    ctx.font = `900 ${size}px system-ui, sans-serif`;
    while (ctx.measureText(text).width > max && size > 26) {
      size -= 2; ctx.font = `900 ${size}px system-ui, sans-serif`;
    }
    return size;
  };
  const textLine = (text, y, color) => {
    text = text.trim(); if (!text) return;
    const size = fit(text.toUpperCase(), 430, 54);
    ctx.font = `900 ${size}px system-ui, sans-serif`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.lineJoin = 'round'; ctx.lineWidth = 12; ctx.strokeStyle = 'rgba(0,0,0,.72)';
    ctx.strokeText(text.toUpperCase(), 256, y); ctx.fillStyle = color; ctx.fillText(text.toUpperCase(), 256, y);
  };
  function roundRect(x, y, w, h, r) { ctx.beginPath(); ctx.roundRect(x, y, w, h, r); }
  function render() {
    const t = themes[style.value];
    ctx.clearRect(0, 0, 512, 512);
    roundRect(0, 0, 512, 512, 46); ctx.fillStyle = t.bg; ctx.fill();
    ctx.globalAlpha = .16; ctx.fillStyle = t.accent;
    for (let i = -400; i < 600; i += 72) { ctx.save(); ctx.rotate(-.42); ctx.fillRect(i, -120, 22, 850); ctx.restore(); }
    ctx.globalAlpha = 1;
    if (image) {
      const crop = 384, scale = Number(zoom.value);
      const ratio = Math.max(crop / image.width, crop / image.height) * scale;
      const w = image.width * ratio, h = image.height * ratio;
      const x = 256 - w / 2, y = 270 - h / 2;
      ctx.save(); roundRect(64, 78, crop, crop, 40); ctx.clip(); ctx.drawImage(image, x, y, w, h); ctx.restore();
      ctx.lineWidth = 12; ctx.strokeStyle = '#fff'; roundRect(64, 78, crop, crop, 40); ctx.stroke();
    } else {
      ctx.fillStyle = 'rgba(0,0,0,.16)'; roundRect(64, 78, 384, 384, 40); ctx.fill();
      ctx.fillStyle = t.ink; ctx.font = '700 22px system-ui, sans-serif'; ctx.textAlign = 'center'; ctx.fillText('Upload a photo to start', 256, 270);
    }
    textLine(topText.value, 45, '#fff'); textLine(bottomText.value, 474, '#fff');
  }
  function loadFile(file) {
    if (!file || !file.type.startsWith('image/')) return;
    const reader = new FileReader();
    reader.onload = () => { image = new Image(); image.onload = render; image.src = reader.result; status.textContent = 'Photo ready — add a caption, choose a style, then download.'; };
    reader.readAsDataURL(file);
  }
  upload.addEventListener('change', () => loadFile(upload.files[0]));
  [topText, bottomText, style, zoom].forEach(el => el.addEventListener('input', render));
  document.querySelectorAll('[data-caption]').forEach(button => button.addEventListener('click', () => {
    const [top, bottom] = button.dataset.caption.split('|'); topText.value = top; bottomText.value = bottom; render();
  }));
  download.addEventListener('click', () => {
    if (!image) { status.textContent = 'Upload a photo first, then your sticker will be ready to download.'; upload.click(); return; }
    canvas.toBlob(blob => {
      const url = URL.createObjectURL(blob), a = document.createElement('a');
      a.href = url; a.download = 'bryme-whatsapp-sticker.webp'; a.click(); URL.revokeObjectURL(url);
      status.textContent = 'Sticker downloaded as a WebP file. Open WhatsApp’s sticker importer to add it to your pack.';
    }, 'image/webp', .82);
  });
  render();
})();
