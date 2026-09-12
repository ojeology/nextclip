import subprocess

OPS = [
    # 1. TRUE emptiness test for the mid-content banner (script tags are not content)
    ('''        var b = frame.contentDocument && frame.contentDocument.body;
        empty = !b || b.children.length === 0;''',
     '''        var b = frame.contentDocument && frame.contentDocument.body;
        empty = !b || Array.prototype.filter.call(b.children || [], function (c) { return c.tagName !== "SCRIPT"; }).length === 0;'''),
    # 2. same true test for the desktop rail
    ('''        try {
          var b = rd.body;
          if (!b || b.children.length === 0) { s3.remove(); return; }
        } catch (e) { /* cross-origin = creative live */ }''',
     '''        try {
          var b = rd.body;
          var real = b ? Array.prototype.filter.call(b.children || [], function (c) { return c.tagName !== "SCRIPT"; }).length : 0;
          if (!real) { s3.remove(); return; }
        } catch (e) { /* cross-origin = creative live */ }'''),
]

# 3. remove the entire diagnostics block (from its comment through the verdict timer)
p = 'assets/ad-slot.js'
s = open(p).read()
start_marker = "    /* diagnostics (always-on during the confirmation window; self-remove) */"
assert s.count(start_marker) == 1, "diag start"
start = s.index(start_marker)
end_marker = "    }, 52000);\n"
assert s.count(end_marker) == 1, "diag end"
end = s.index(end_marker) + len(end_marker)
s = s[:start] + s[end:]

# apply the emptiness fixes
for old, new in OPS:
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)

# 4. header: v5, diagnostics removed
old = "/* BRYME advertising component v4 (ad-slot.js twin). */"
assert s.count(old) == 1
s = s.replace(old, "/* BRYME advertising component v5 (ad-slot.js twin): diagnostic overlay removed; unfilled units collapse via true content test (script tags != content). */")

open(p, 'w').write(s)
assert subprocess.run(['node', '--check', p], capture_output=True, text=True).returncode == 0
assert 'bryme-ad-debug' not in s and 'dlog' not in s, "debug remnants"
print("v5: diagnostics removed, true fill tests in, syntax OK")
