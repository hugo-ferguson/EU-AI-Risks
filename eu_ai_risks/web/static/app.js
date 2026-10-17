// Disable buttons on submit so a slow request isn't sent twice
function onSubmit(formId, buttonId, label, noteId) {
  const form = document.getElementById(formId);
  if (!form) return;
  form.addEventListener('submit', () => {
    const button = document.getElementById(buttonId);
    button.disabled = true;
    button.textContent = label;
    const note = noteId && document.getElementById(noteId);
    if (note) note.hidden = false;
  });
}

onSubmit('upload-form', 'upload-btn', 'Uploading...');
onSubmit('assess-form', 'run-btn', 'Running...', 'run-note');

// Filter findings by search text and risk level
const search = document.getElementById('search-input');
const level = document.getElementById('level-filter');
const findings = Array.from(document.querySelectorAll('.finding'));
const noResults = document.getElementById('no-results');

function applyFilters() {
  const query = (search.value || '').trim().toLowerCase();
  const wanted = level.value;
  let visible = 0;
  findings.forEach((finding) => {
    const show = (!query || finding.dataset.search.includes(query))
      && (wanted === 'all' || finding.dataset.level === wanted);
    finding.hidden = !show;
    if (show) visible += 1;
  });
  noResults.hidden = visible !== 0;
}

if (search && level) {
  search.addEventListener('input', applyFilters);
  level.addEventListener('change', applyFilters);
}

