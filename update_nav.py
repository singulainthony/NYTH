import re
import os

rootdir = 'Business/northyorktechhelp-site'
all_html = []
for root, dirs, filenames in os.walk(rootdir):
    for f in filenames:
        if f.endswith('.html'):
            all_html.append(os.path.join(root, f))

new_menu = """                <li><a href="/#about">About</a></li>
                <li><a href="/#services">Services</a></li>
                <li><a href="/artificial-intelligence/">Artificial Intelligence</a></li>
                <li><a href="/#areas">Areas</a></li>
                <li><a href="/#faq">FAQ</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/contact.html" class="nav-cta">Contact</a></li>"""

for file_path in all_html:
    with open(file_path, 'r') as f:
        content = f.read()

    # Match the entire <ul> block regardless of what's inside
    # Using re.DOTALL to match across newlines
    new_content = re.sub(r'(<ul class="nav-menu">).*?(</ul>)', r'\1\n' + new_menu + r'\n            \2', content, flags=re.DOTALL)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
