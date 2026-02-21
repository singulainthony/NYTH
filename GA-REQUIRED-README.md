# ⚠️ IMPORTANT: Google Analytics Required on All Pages

## Your GA Tracking ID
**G-09LNNVFN7C**

## Pages That Currently Have GA ✓
- index.html ✓
- contact.html ✓
- thank-you.html ✓
- blog/index.html ✓
- blog/transfer-photos-iphone-to-computer.html ✓
- blog/neighbor-kid-ai-teacher.html ✓
- blog/how-to-spot-tech-scams.html ✓
- blog/iphone-running-slow-fix.html ✓
- blog/organize-photos-iphone.html ✓
- blog/computer-running-slow-fixes.html ✓
- artificial-intelligence/index.html ✓

## Code to Add to Every New Page

Paste this immediately after `<meta charset="UTF-8">` in the `<head>` section:

```html
<!-- Preconnect for performance -->
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">

<!-- Google tag (gtag.js) - Placed early for optimal detection -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-09LNNVFN7C"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-09LNNVFN7C');
</script>
```

## Template Available
Use `/Business/northyorktechhelp-site/page-template-with-ga.html` as your starting point for new pages.

## Why This Matters
- Tracks all website visitors
- Shows which pages are most popular
- Helps understand where leads come from
- Essential for measuring marketing effectiveness

## Last Updated
February 21, 2026 - Added GA to all existing pages
