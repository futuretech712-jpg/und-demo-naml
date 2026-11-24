/* NAML 2027: shared behaviour (mobile menu, countdown). Safe to include on every page and in WordPress blocks. */
{
  // Mobile menu is a <details> element (works without JS). Close it after a link is chosen or on Escape.
  for (const d of document.querySelectorAll('.naml .mnav')) {
    d.addEventListener('click', (e) => { if (e.target.closest('nav a')) d.open = false; });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && d.open) { d.open = false; d.querySelector('summary').focus(); } });
  }

  // Countdown to the abstract deadline (end of Dec 4, 2026, Pacific time).
  // The visible cells are aria-hidden; screen readers get the static deadline text.
  const box = document.getElementById('naml-count');
  if (box) {
    const end = new Date('2026-12-04T23:59:59-08:00').getTime();
    let timer = 0;
    const tick = () => {
      const t = Math.max(0, end - Date.now());
      if (t === 0) {
        box.innerHTML = '<small>Abstract submission is closed. Acceptance notifications by mid-February 2027.</small>';
        clearInterval(timer);
        return;
      }
      const v = { d: Math.floor(t / 864e5), h: Math.floor(t / 36e5) % 24, m: Math.floor(t / 6e4) % 60, s: Math.floor(t / 1e3) % 60 };
      for (const k in v) {
        const el = box.querySelector(`[data-u="${k}"]`);
        if (el) el.textContent = String(v[k]).padStart(2, '0');
      }
    };
    timer = setInterval(tick, 1000);
    tick();
  }
}
