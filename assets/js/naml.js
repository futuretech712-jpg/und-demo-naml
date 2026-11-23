/* NAML 2027 – shared behaviour (menu, countdown, sonar network). Safe to include on every page. */
{
  // Mobile menu
  const burger = document.querySelector('.naml .burger');
  const menu = document.getElementById('naml-menu');
  if (burger && menu) {
    burger.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
    });
  }

  // Sensor network inside every sonar plot (<g class="naml-net">, 600x600 viewBox)
  const pts = [[300,300],[380,240],[430,330],[250,200],[190,320],[330,420],[460,180],[150,220],[240,460],[420,450],[520,300],[110,360],[350,110],[200,110]];
  const links = [[0,1],[0,3],[0,4],[0,5],[1,2],[1,6],[1,12],[2,10],[2,9],[3,13],[3,7],[4,11],[4,8],[5,8],[5,9],[6,10],[7,11],[12,13],[3,12]];
  for (const g of document.querySelectorAll('.naml-net')) {
    g.innerHTML =
      links.map(([a,b]) => `<line x1="${pts[a][0]}" y1="${pts[a][1]}" x2="${pts[b][0]}" y2="${pts[b][1]}" stroke="#8FD3D9" stroke-opacity=".55" stroke-width="2"/>`).join('') +
      pts.map(([x,y],i) => `<circle cx="${x+3}" cy="${y+3}" r="${i?8:13}" fill="#FF544B"/><circle cx="${x}" cy="${y}" r="${i?8:13}" fill="${i?'#FFC54B':'#FFA04B'}"/>`).join('');
  }

  // Countdown to the abstract deadline (end of Dec 4, 2026, Pacific time)
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
      const v = { d: Math.floor(t/864e5), h: Math.floor(t/36e5)%24, m: Math.floor(t/6e4)%60, s: Math.floor(t/1e3)%60 };
      for (const k in v) {
        const el = box.querySelector(`[data-u="${k}"]`);
        if (el) el.textContent = String(v[k]).padStart(2, '0');
      }
    };
    timer = setInterval(tick, 1000);
    tick();
  }
}
