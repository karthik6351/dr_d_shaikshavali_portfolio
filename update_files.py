import os
import re

ref_dir = r'C:\Users\gonug\.gemini\antigravity-ide\brain\ecfb7897-422c-46c6-84ea-bd01e4cdfb8b\scratch\reference_portfolio'
dest_dir = r'd:\karthik\education\Projects\Mango_Labz_Projects\Portfolio\Shaikshavali_portfolio'

# 1. Copy and modify style.css
with open(os.path.join(ref_dir, 'style.css'), 'r', encoding='utf-8') as f:
    css = f.read()

# Replace colors for Emerald Green & Silver
css = css.replace('--accent-primary: #1b2a4a;', '--accent-primary: #064e3b;')
css = css.replace('--accent-secondary: #c49a2a;', '--accent-secondary: #94a3b8;')
css = css.replace('--accent-tertiary: #2d4a7c;', '--accent-tertiary: #047857;')
css = css.replace('rgba(196, 154, 42, 0.08)', 'rgba(148, 163, 184, 0.08)')
css = css.replace('--accent-gradient: linear-gradient(135deg, #1b2a4a 0%, #2d4a7c 100%);', '--accent-gradient: linear-gradient(135deg, #064e3b 0%, #047857 100%);')
css = css.replace('--gold-gradient: linear-gradient(135deg, #c49a2a 0%, #d4af37 50%, #e8c84a 100%);', '--gold-gradient: linear-gradient(135deg, #94a3b8 0%, #cbd5e1 50%, #e2e8f0 100%);')
css = css.replace('--text-accent: #c49a2a;', '--text-accent: #059669;')
css = css.replace('rgba(196, 154, 42, 0.25)', 'rgba(148, 163, 184, 0.25)')
css = css.replace('rgba(196, 154, 42, 0.15)', 'rgba(148, 163, 184, 0.15)')
css = css.replace('--bg-hero: linear-gradient(160deg, #faf8f5 0%, #f0ece4 40%, #e8e2d8 100%);', '--bg-hero: linear-gradient(160deg, #f0fdf4 0%, #dcfce7 40%, #bbf7d0 100%);')
css = css.replace('--bg-primary: #faf8f5;', '--bg-primary: #f8fafc;')

with open(os.path.join(dest_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Copy and modify script.js
with open(os.path.join(ref_dir, 'script.js'), 'r', encoding='utf-8') as f:
    js = f.read()

# Replace typing text strings
js = re.sub(r'const roles = \[.*?\];', 'const roles = ["Assistant Professor", "Researcher", "VLSI Expert", "Ph.D Scholar"];', js, flags=re.DOTALL)

with open(os.path.join(dest_dir, 'script.js'), 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated style.css and script.js')
