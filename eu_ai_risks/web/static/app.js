const form = document.querySelector('#assessment-form');
const runButtons = [document.querySelector('#run-btn'), document.querySelector('#hero-run-btn')].filter(Boolean);
const fileInput = document.querySelector('#requirements-file');
const fileLabel = document.querySelector('#file-label');
const fileHelper = document.querySelector('#file-helper');
const dropzone = document.querySelector('#dropzone');
const statusBox = document.querySelector('.nav-status');

if (fileInput) {
  fileInput.addEventListener('change', () => {
    const file = fileInput.files?.[0];
    if (!file) return;
    fileLabel.textContent = file.name;
    fileHelper.textContent = 'Ready to run assessment';
    dropzone.classList.add('has-file');
  });
}

if (form) {
  form.addEventListener('submit', () => {
    runButtons.forEach((button) => {
      button.disabled = true;
      const label = button.querySelector('span');
      if (label) label.textContent = 'Running...';
      const icon = button.querySelector('svg');
      if (icon) icon.classList.remove('spin');
    });
    if (statusBox) statusBox.lastChild.textContent = ' Running assessment from uploaded requirements document...';
  });
}

const findingCards = Array.from(document.querySelectorAll('.finding-card'));
const detailPanels = Array.from(document.querySelectorAll('.detail-panel'));
const searchInput = document.querySelector('#search-input');
const levelFilter = document.querySelector('#level-filter');
const categoryFilter = document.querySelector('#category-filter');
const noResults = document.querySelector('#no-results');

function showDetail(targetId) {
  findingCards.forEach((card) => card.classList.toggle('active', card.dataset.target === targetId));
  detailPanels.forEach((panel) => panel.classList.toggle('hidden', panel.id !== targetId));
}

findingCards.forEach((card) => {
  card.addEventListener('click', () => showDetail(card.dataset.target));
});

function applyFilters() {
  const query = (searchInput?.value || '').trim().toLowerCase();
  const level = levelFilter?.value || 'all';
  const category = categoryFilter?.value || 'all';
  let visible = [];

  findingCards.forEach((card) => {
    const matchesQuery = !query || (card.dataset.search || '').includes(query);
    const matchesLevel = level === 'all' || card.dataset.level === level;
    const categories = (card.dataset.categories || '').split(' ').filter(Boolean);
    const matchesCategory = category === 'all' || categories.includes(category);
    const isVisible = matchesQuery && matchesLevel && matchesCategory;
    card.classList.toggle('hidden', !isVisible);
    if (isVisible) visible.push(card);
  });

  noResults.hidden = visible.length !== 0;
  const activeVisible = visible.some((card) => card.classList.contains('active'));
  if (!activeVisible && visible[0]) showDetail(visible[0].dataset.target);
}

[searchInput, levelFilter, categoryFilter].forEach((element) => {
  if (element) element.addEventListener('input', applyFilters);
  if (element) element.addEventListener('change', applyFilters);
});
