/* Fault-code lookup (Plan 4d). Progressive enhancement: without this script the make pages are plain tables and
   browser find works. It normalizes what a technician types with the same grammar as solar_kb.codes.code_key
   (filler words such as "event" or "error no." go, spaces and case go, zero padding goes, vendor prefixes stay)
   and matches exact keys first, then printed ranges containing the number, then the bare number. */
(function () {
  'use strict';
  var FILLER = /^\s*(?:(?:(?:event|error|alarm|code|no|number|nr|id)\b\.?|#)\s*)+/i;
  var CODE = /^([a-z]*)-?(\d+)(?:-(\d+))?$/;

  function parseKey(text) {
    var s = String(text || '').trim().replace(FILLER, '').replace(/\s+/g, '').toLowerCase();
    var m = CODE.exec(s);
    if (m) {
      var start = parseInt(m[2], 10), end = m[3] ? parseInt(m[3], 10) : null;
      return { key: m[1] + start + (end !== null ? '-' + end : ''), prefix: m[1], number: start, end: end };
    }
    return { key: s.replace(/[^a-z0-9]/g, ''), prefix: '', number: null, end: null };
  }

  function matchKind(entry, q) {
    if (entry.key === q.key) { return 'exact'; }
    if (q.number !== null && q.end === null) {
      var e = parseKey(entry.key);
      var ranged = entry.from !== null && entry.from !== undefined;
      if (ranged && entry.from <= q.number && q.number <= entry.to && e.prefix === q.prefix) { return 'range'; }
      if (!ranged && e.number === q.number) { return 'number'; }
    }
    return null;
  }

  function rank(entries, q) {
    var kinds = ['exact', 'range', 'number'], i, hits;
    for (i = 0; i < kinds.length; i++) {
      hits = entries.filter(function (e) { return matchKind(e, q) === kinds[i]; });
      if (hits.length) { return hits; }
    }
    return entries.filter(function (e) { return q.key && e.key.indexOf(q.key) !== -1; });
  }

  function rowEntries(form) {
    var rows = document.querySelectorAll('tr[data-key]');
    return Array.prototype.map.call(rows, function (tr) {
      return { key: tr.getAttribute('data-key'), row: tr,
               from: tr.hasAttribute('data-from') ? parseInt(tr.getAttribute('data-from'), 10) : null,
               to: tr.hasAttribute('data-to') ? parseInt(tr.getAttribute('data-to'), 10) : null };
    });
  }

  function filterRows(form, text) {
    var entries = rowEntries(form), q = parseKey(text), results = form.querySelector('.fc-results');
    if (!q.key) {
      entries.forEach(function (e) { e.row.hidden = false; });
      results.textContent = '';
      return;
    }
    var hits = rank(entries, q);
    entries.forEach(function (e) { e.row.hidden = hits.indexOf(e) === -1; });
    results.textContent = hits.length ? '' : 'No code matches "' + text + '" on this page.';
  }

  function flatten(data) {
    var out = [], names = data._names || {};
    Object.keys(data).forEach(function (make) {
      if (make === '_names') { return; }
      var makeName = (names[make] && names[make].name) || make;
      Object.keys(data[make]).forEach(function (family) {
        var familyName = (names[make] && names[make].families && names[make].families[family]) || family;
        Object.keys(data[make][family]).forEach(function (key) {
          var c = data[make][family][key];
          out.push({ key: key, id: c.id, code: c.code, label: c.label || '', from: c.from, to: c.to,
                     makeName: makeName, familyName: familyName });
        });
      });
    });
    return out;
  }

  function lookup(form, entries, text) {
    var q = parseKey(text), results = form.querySelector('.fc-results');
    while (results.firstChild) { results.removeChild(results.firstChild); }
    if (!q.key) { return; }
    var hits = rank(entries, q).slice(0, 50);
    if (!hits.length) {
      var li = document.createElement('li');
      li.className = 'empty';
      li.textContent = 'No code matches "' + text + '".';
      results.appendChild(li);
      return;
    }
    hits.forEach(function (h) {
      var li = document.createElement('li'), a = document.createElement('a');
      a.href = h.id.replace(/^fc:/, '');  /* a record page beside this index */
      a.textContent = h.makeName + ' ' + h.familyName + ' ' + h.code;
      li.appendChild(a);
      if (h.label) { li.appendChild(document.createTextNode(' — ' + h.label)); }
      results.appendChild(li);
    });
  }

  function init() {
    var form = document.querySelector('[data-fc-lookup]');
    if (!form) { return; }
    var input = form.querySelector('input[type=search]'), url = form.getAttribute('data-codes'), entries = null;
    form.hidden = false;
    form.addEventListener('submit', function (ev) { ev.preventDefault(); });
    input.addEventListener('input', function () {
      if (!url) { filterRows(form, input.value); return; }
      if (entries) { lookup(form, entries, input.value); return; }
      fetch(url).then(function (r) { return r.json(); }).then(function (data) {
        entries = flatten(data);
        lookup(form, entries, input.value);
      }).catch(function () { form.querySelector('.fc-results').textContent = 'The code table could not be loaded.'; });
    });
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
