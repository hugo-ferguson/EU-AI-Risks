const CACHE_KEY = 'eu_ai_risks_cache';
const appShell = document.querySelector('.app-shell');
const phase = appShell?.dataset.phase || 'empty';

const uploadForm = document.querySelector('#upload-form');
const assessForm = document.querySelector('#assess-form');
const fileInput = document.querySelector('#requirements-file');
const fileLabel = document.querySelector('#file-label');
const fileHelper = document.querySelector('#file-helper');
const dropzone = document.querySelector('#dropzone');
const statusBox = document.querySelector('.nav-status');
const resultsPanel = document.querySelector('.results-panel');

// ── File input ──────────────────────────────────────────────────────────
if (fileInput) {
  fileInput.addEventListener('change', () => {
    const file = fileInput.files?.[0];
    if (!file) return;
    fileLabel.textContent = file.name;
    fileHelper.textContent = 'Ready to upload';
    dropzone.classList.add('has-file');
  });
}

// ── Form submit feedback ────────────────────────────────────────────────
function disableButton(btn, label) {
  if (!btn) return;
  btn.disabled = true;
  const span = btn.querySelector('span');
  if (span) span.textContent = label;
}

if (uploadForm) {
  uploadForm.addEventListener('submit', () => {
    disableButton(document.querySelector('#upload-btn'), 'Parsing...');
    if (statusBox) statusBox.lastChild.textContent = ' Parsing requirements...';
  });
}

if (assessForm) {
  assessForm.addEventListener('submit', () => {
    disableButton(document.querySelector('#run-btn'), 'Running...');
    disableButton(document.querySelector('#hero-run-btn'), 'Running...');
    if (statusBox) statusBox.lastChild.textContent = ' Running assessment pipeline...';
  });
}

// ── localStorage: save on assessed, restore on empty ────────────────────
function saveCache() {
  try {
    const filename = appShell?.dataset.filename || '';
    const heroActions = document.querySelector('.hero-actions');
    const pipelineCard = document.querySelector('.pipeline-card');
    localStorage.setItem(CACHE_KEY, JSON.stringify({
      resultsHTML: resultsPanel.innerHTML,
      heroActionsHTML: heroActions ? heroActions.innerHTML : '',
      pipelineHTML: pipelineCard ? pipelineCard.innerHTML : '',
      statusText: statusBox?.textContent?.trim() || '',
      filename: filename,
      url: location.href,
      savedAt: new Date().toISOString(),
    }));
  } catch (_) { /* quota exceeded or private mode — ignore */ }
}

function restoreCache() {
  try {
    const raw = localStorage.getItem(CACHE_KEY);
    if (!raw) return false;
    const cache = JSON.parse(raw);
    if (!cache.resultsHTML) return false;

    resultsPanel.innerHTML = cache.resultsHTML;

    // restore pipeline step highlights
    const pipelineCard = document.querySelector('.pipeline-card');
    if (pipelineCard && cache.pipelineHTML) pipelineCard.innerHTML = cache.pipelineHTML;

    // restore hero actions (download report link)
    const heroActions = document.querySelector('.hero-actions');
    if (heroActions && cache.heroActionsHTML) heroActions.innerHTML = cache.heroActionsHTML;

    // update status bar
    if (statusBox) {
      statusBox.classList.remove('error');
      statusBox.lastChild.textContent = ' ' + (cache.statusText || 'Cached results');
    }

    // add cache banner above results
    const banner = document.createElement('div');
    banner.className = 'cache-banner';
    banner.innerHTML = '<span>Showing cached results' +
      (cache.filename ? ' from <strong>' + escapeHtml(cache.filename) + '</strong>' : '') +
      '.</span> <button id="clear-cache-btn" class="secondary-btn" style="padding:5px 10px;font-size:12px">Clear</button>';
    resultsPanel.prepend(banner);

    document.querySelector('#clear-cache-btn')?.addEventListener('click', () => {
      localStorage.removeItem(CACHE_KEY);
      location.reload();
    });

    return true;
  } catch (_) { return false; }
}

function escapeHtml(text) {
  const el = document.createElement('span');
  el.textContent = text;
  return el.innerHTML;
}

if (phase === 'assessed') {
  saveCache();
} else if (phase === 'empty') {
  const restored = restoreCache();
  if (restored) initResultsInteractivity();
}

// ── Findings interactivity (runs on server-rendered or cache-restored) ──
function initResultsInteractivity() {
  const cards = Array.from(document.querySelectorAll('.finding-card'));
  const panels = Array.from(document.querySelectorAll('.detail-panel'));
  const search = document.querySelector('#search-input');
  const level = document.querySelector('#level-filter');
  const category = document.querySelector('#category-filter');
  const noRes = document.querySelector('#no-results');

  function showDetail(targetId) {
    cards.forEach((c) => c.classList.toggle('active', c.dataset.target === targetId));
    panels.forEach((p) => p.classList.toggle('hidden', p.id !== targetId));
  }

  cards.forEach((c) => c.addEventListener('click', () => showDetail(c.dataset.target)));

  function applyFilters() {
    const q = (search?.value || '').trim().toLowerCase();
    const lv = level?.value || 'all';
    const cat = category?.value || 'all';
    let visible = [];

    cards.forEach((c) => {
      const matchQ = !q || (c.dataset.search || '').includes(q);
      const matchL = lv === 'all' || c.dataset.level === lv;
      const cats = (c.dataset.categories || '').split(' ').filter(Boolean);
      const matchC = cat === 'all' || cats.includes(cat);
      const show = matchQ && matchL && matchC;
      c.classList.toggle('hidden', !show);
      if (show) visible.push(c);
    });

    if (noRes) noRes.hidden = visible.length !== 0;
    if (!visible.some((c) => c.classList.contains('active')) && visible[0]) {
      showDetail(visible[0].dataset.target);
    }
  }

  [search, level, category].forEach((el) => {
    if (el) el.addEventListener('input', applyFilters);
    if (el) el.addEventListener('change', applyFilters);
  });
}

// run interactivity on server-rendered assessed pages too
if (phase === 'assessed') initResultsInteractivity();
