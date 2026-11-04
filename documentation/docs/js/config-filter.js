// Tag filter for the table of all configurations (pages/configurations/Overview.md).
// The table sits in <div class="config-table">; each row's Tags cell holds
// <span class="cfg-tag">...</span> elements written by tested-configs/lib/make_pages.py.
// Written with Claude Code.
'use strict';

function setupConfigFilters() {
  document.querySelectorAll('.config-table').forEach((box) => {
    const table = box.querySelector('table');
    if (!table || box.querySelector('.cfg-filter')) return;
    const rows = Array.from(table.tBodies[0].rows);
    const tags = [];
    rows.forEach((r) => r.querySelectorAll('.cfg-tag').forEach((s) => {
      if (!tags.includes(s.textContent)) tags.push(s.textContent);
    }));

    const bar = document.createElement('div');
    bar.className = 'cfg-filter';
    const count = document.createElement('span');
    count.className = 'cfg-count';
    let active = null;

    function apply() {
      let shown = 0;
      rows.forEach((r) => {
        const has = !active || Array.from(r.querySelectorAll('.cfg-tag')).some((s) => s.textContent === active);
        r.hidden = !has;
        if (has) shown += 1;
      });
      bar.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.tag === (active || ''))));
      count.textContent = `${shown} of ${rows.length} shown`;
    }

    ['', ...tags].forEach((tag) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'cfg-tag';
      b.dataset.tag = tag;
      b.textContent = tag || 'All';
      b.addEventListener('click', () => { active = (tag && active !== tag) ? tag : null; apply(); });
      bar.appendChild(b);
    });
    // clicking a tag inside the table filters by it too
    rows.forEach((r) => r.querySelectorAll('.cfg-tag').forEach((s) => {
      s.addEventListener('click', () => { active = s.textContent; apply(); });
    }));
    bar.appendChild(count);
    box.insertBefore(bar, box.firstChild);
    apply();
  });
}

// Material's instant navigation swaps pages without a reload; document$ fires on each page.
if (typeof document$ !== 'undefined') {
  document$.subscribe(setupConfigFilters);
} else {
  document.addEventListener('DOMContentLoaded', setupConfigFilters);
}
