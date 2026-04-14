#!/usr/bin/env python3
"""
Update April 9 blog posts to match old post styling:
1. Replace simple CTA boxes with styled versions
2. Add Related Articles section
3. Add Author bio paragraph
"""

import re
import os

BLOG_DIR = "/Users/anonymouspro/.openclaw/workspace/Business/northyorktechhelp-site/blog"

# Author bio paragraph to add
AUTHOR_BIO = '''<p style="margin-top: 40px; padding-top: 30px; border-top: 1px solid #E2E8F0; color: #64748B; font-size: 14px;">
    <em>Anthony is a tech support specialist serving seniors in North York, Willowdale, and surrounding areas. He provides patient, in-home technology help including scam protection, computer security, and digital literacy. He holds a Bachelor of Commerce from TMU and certifications in AI Engineering from IBM and Google.</em>
</p>'''

# All available April 9 blog posts
ALL_POSTS = {
    "avoiding-fake-tech-support-calls-what-toronto-seniors-need-to-know.html": "Avoiding Fake Tech Support Calls: What Toronto Seniors Need to Know",
    "beginners-guide-to-using-whatsapp-for-family-chats-in-toronto.html": "Beginner's Guide to Using WhatsApp for Family Chats in Toronto",
    "best-free-apps-for-health-tracking-on-smartphones-for-toronto-seniors.html": "Best Free Apps for Health Tracking on Smartphones for Toronto Seniors",
    "easy-calendar-apps-setup-for-remembering-appointments-in-north-york.html": "Easy Calendar Apps Setup for Remembering Appointments in North York",
    "easy-guide-to-setting-up-facetime-for-toronto-seniors-to-stay-connected.html": "Easy Guide to Setting Up FaceTime for Toronto Seniors to Stay Connected",
    "guide-to-virtual-reality-headsets-for-entertainment-senior-friendly-setup.html": "Guide to Virtual Reality Headsets for Entertainment: Senior-Friendly Setup",
    "how-to-download-and-use-ebooks-on-kindles-for-north-york-readers.html": "How to Download and Use eBooks on Kindles for North York Readers",
    "how-to-update-your-android-phone-safely-tips-for-north-york-residents-over-65.html": "How to Update Your Android Phone Safely: Tips for North York Residents Over 65",
    "how-to-use-google-maps-for-navigation-essential-for-toronto-seniors.html": "How to Use Google Maps for Navigation: Essential for Toronto Seniors",
    "how-toronto-seniors-can-use-voice-to-text-on-ipads-for-easier-typing.html": "How Toronto Seniors Can Use Voice-to-Text on iPads for Easier Typing",
    "introduction-to-podcast-apps-relaxing-listening-for-toronto-seniors.html": "Introduction to Podcast Apps: Relaxing Listening for Toronto Seniors",
    "north-york-advice-managing-multiple-email-accounts-on-one-device.html": "North York Advice: Managing Multiple Email Accounts on One Device",
    "north-york-guide-setting-up-password-managers-for-easy-senior-access.html": "North York Guide: Setting Up Password Managers for Easy Senior Access",
    "north-york-local-fixing-bluetooth-connection-issues-with-headphones.html": "North York Local: Fixing Bluetooth Connection Issues with Headphones",
    "north-york-tech-essentials-how-seniors-can-set-up-home-security-cameras.html": "North York Tech Essentials: How Seniors Can Set Up Home Security Cameras",
    "north-york-tech-help-how-to-connect-your-smart-tv-to-the-internet.html": "North York Tech Help: How to Connect Your Smart TV to the Internet",
    "north-york-tech-support-fixing-common-laptop-freezes-for-seniors.html": "North York Tech Support: Fixing Common Laptop Freezes for Seniors",
    "protecting-personal-data-online-privacy-tips-for-north-york-seniors.html": "Protecting Personal Data: Online Privacy Tips for North York Seniors",
    "safe-online-shopping-tips-for-seniors-in-north-york-during-holiday-seasons.html": "Safe Online Shopping Tips for Seniors in North York During Holiday Seasons",
    "senior-tech-security-enabling-two-factor-authentication-in-toronto.html": "Senior Tech Security: Enabling Two-Factor Authentication in Toronto",
    "simple-steps-to-organize-email-inboxes-for-busy-north-york-retirees.html": "Simple Steps to Organize Email Inboxes for Busy North York Retirees",
    "spotting-ai-generated-scams-awareness-guide-for-toronto-seniors.html": "Spotting AI-Generated Scams: Awareness Guide for Toronto Seniors",
    "top-10-ways-north-york-seniors-can-protect-against-phone-scams-in-2026.html": "Top 10 Ways North York Seniors Can Protect Against Phone Scams in 2026",
    "troubleshooting-wifi-dropouts-quick-fixes-for-toronto-home-networks.html": "Troubleshooting WiFi Dropouts: Quick Fixes for Toronto Home Networks",
    "why-north-york-seniors-should-backup-their-devices-to-icloud-and-how.html": "Why North York Seniors Should Backup Their Devices to iCloud (and How)"
}

def get_related_articles(filename):
    related = []
    # Simple strategy: pick 4 other posts from the list
    for f, title in ALL_POSTS.items():
        if f != filename:
            related.append((f, title))
            if len(related) >= 4:
                break
    return related

def build_related_articles_html(related):
    html = "<h2>Related Articles</h2>\n<ul>\n"
    for filename, title in related:
        html += f'    <li><a href="{filename}">{title}</a></li>\n'
    html += "</ul>"
    return html

def process_file(filename):
    filepath = os.path.join(BLOG_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the cta class containing div
    # Looks for: <div class="cta-box">(.*?)</div>
    pattern = r'<div class="cta-box">(.*?)</div>'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"No CTA box found in {filename}")
        return
        
    cta_content = match.group(1)
    
    # Extract existing Heading (h3) and first paragraph
    h3_match = re.search(r'<h3>(.*?)</h3>', cta_content, re.DOTALL)
    h3_text = h3_match.group(1).strip() if h3_match else "Need Help?"
    
    p_match = re.search(r'<p>(.*?)</p>', cta_content, re.DOTALL)
    p_text = p_match.group(1).strip() if p_match else "Ready to improve your tech skills?"
    
    new_cta = f'''<div class="cta-box">
    <h3>{h3_text}</h3>
    <p>{p_text}</p>
    <p style="font-size: 1.25rem; margin: 20px 0;"><strong>$45/hour with satisfaction guaranteed</strong></p>
    <a href="tel:289-203-4346" class="btn btn-primary" style="font-size: 1.1rem; padding: 15px 30px;">Call or Text: 289-203-4346</a>
    <p style="margin-top: 15px; font-size: 14px;">Serving North York, Willowdale, Bayview Village, Don Mills & surrounding areas</p>
</div>'''

    # Replace CTA
    old_cta_block = match.group(0)
    content = content.replace(old_cta_block, new_cta)
    
    # Add Related Articles and Bio
    related = get_related_articles(filename)
    related_html = build_related_articles_html(related)
    
    new_content = f"{related_html}\n\n{AUTHOR_BIO}"
    
    # Insert before the last </div> followed by </div></article>
    # Looking for: </div>\n            </div>\n        </div>\n    </article>
    # Actually, looking at the WhatsApp file:
    # </div>\n            </div>\n        </div>\n    </article>
    # Or just before the final </article>
    
    insert_point = '</div>\n            </div>' # Looks like it ends in div, div
    if insert_point in content:
        content = content.replace(insert_point, f"{new_content}\n\n{insert_point}")
    else:
        # Fallback
        print(f"Could not find insert point for {filename}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")

for filename in ALL_POSTS.keys():
    process_file(filename)
