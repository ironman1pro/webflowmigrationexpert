import re, json, os

SITE = "https://webflowmigrationexpert.com"
OG_IMAGE = SITE + "/images/og-image.png"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="shortcut icon" href="/favicon.ico">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/shared.css">
{schema}
<link rel="canonical" href="{url}">
{breadcrumb_schema}
</head>
<body>

<site-nav></site-nav>

<main>
"""

TAIL = """
</main>

<site-footer></site-footer>

<script src="/nav-footer.js" defer></script>
</body>
</html>
"""

DEFAULT_PROCESS = [
    ("Audit", "Full inventory of your pages, content, URLs, and everything ranking that needs to survive the move."),
    ("Migration plan", "A URL-by-URL redirect map and a build plan so nothing gets lost or orphaned in the switch."),
    ("Build in Webflow", "Your site rebuilt clean in Webflow, content migrated, tested on staging before anyone else sees it."),
    ("Launch &amp; handoff", "DNS cutover, redirects verified, and a short walkthrough so you can edit the new site yourself."),
]

def problem_card(icon_path, title, body):
    return f'''        <div class="card">
          <div class="card-icon"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7">{icon_path}</svg></div>
          <h3>{title}</h3>
          <p>{body}</p>
        </div>
'''

def faq_item(q, a):
    return f'''      <details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>
'''

def process_step(title, body):
    return f'''        <div class="process-step">
          <h3>{title}</h3>
          <p>{body}</p>
        </div>
'''

def strip_html(s):
    return re.sub("<[^<]+?>", "", s)

def faq_schema(faqs):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": strip_html(q),
                "acceptedAnswer": {"@type": "Answer", "text": strip_html(a)}
            } for q, a in faqs
        ]
    }
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'


def breadcrumb_schema(slug, crumb_label):
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": strip_html(crumb_label), "item": f"{SITE}/{slug}.html"},
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'


def page(slug, eyebrow, headline, sub, title, description, problems, note_title, note_body,
         faqs, platform_value, process_steps=None, process_h2=None, process_sub=None):
    problem_html = "".join(problem_card(*p) for p in problems)
    faq_html = "".join(faq_item(q, a) for q, a in faqs)
    steps = process_steps or DEFAULT_PROCESS
    process_html = "".join(process_step(*s) for s in steps)
    process_h2 = process_h2 or "A migration that doesn't touch your live site until it's ready."
    process_sub = process_sub or "Your current site stays live and untouched until the new one is tested and approved."
    crumb_label = eyebrow.replace(" to Webflow", " &rarr; Webflow")

    body = f'''
  <!-- ============ PAGE HERO ============ -->
  <section class="page-hero">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><span>{crumb_label}</span></nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{headline}</h1>
      <p>{sub}</p>
      <div class="hero-cta" style="justify-content:flex-start; margin-top:28px;">
        <a class="btn-primary" href="#book">Book your free migration call</a>
      </div>
    </div>
  </section>

  <!-- ============ TRUST STATS ============ -->
  <section class="trust" style="padding:44px 0; margin-top:24px;">
    <div class="wrap">
      <div class="trust-grid">
        <div class="trust-stat"><strong>42</strong><span>Projects delivered</span></div>
        <a class="trust-stat trust-stat-link" href="https://www.upwork.com/freelancers/webflow1" target="_blank" rel="noopener"><strong>4.9 &#9733;</strong><span>Rating on Upwork</span></a>
        <div class="trust-stat"><strong>Certified</strong><span>Webflow Expert</span></div>
      </div>
    </div>
  </section>

  <!-- ============ PROBLEM ============ -->
  <section>
    <div class="wrap">
      <span class="eyebrow">What's actually costing you</span>
      <h2>The real reasons teams leave</h2>
      <div class="card-grid">
{problem_html}      </div>
    </div>
  </section>

  <!-- ============ PLATFORM NOTE ============ -->
  <section style="background:var(--bg-alt);">
    <div class="wrap" style="max-width:760px;">
      <span class="eyebrow">Worth knowing upfront</span>
      <h2>{note_title}</h2>
      <p class="section-sub" style="margin-top:18px; max-width:100%;">{note_body}</p>
    </div>
  </section>

  <!-- ============ PROCESS ============ -->
  <section>
    <div class="wrap">
      <span class="eyebrow">How it works</span>
      <h2>{process_h2}</h2>
      <p class="section-sub">{process_sub}</p>
      <div class="process-grid">
{process_html}      </div>
    </div>
  </section>

  <!-- ============ FAQ ============ -->
  <section id="faq" style="background:var(--bg-alt);">
    <div class="wrap center">
      <span class="eyebrow">Questions</span>
      <h2>Before you book a call</h2>
    </div>
    <div class="faq-list">
{faq_html}    </div>
  </section>

  <!-- ============ BOOK ============ -->
  <section id="book" class="book">
    <div class="wrap book-inner">
      <span class="eyebrow">Get started</span>
      <h2>Book your free 15-minute migration call</h2>
      <p class="section-sub center">Tell me about your current site. I'll reply with honest feedback on whether Webflow's the right move.</p>

      <form class="book-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
        <input type="hidden" name="source_page" value="{platform_value}">
        <div class="form-row">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="form-row">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="form-row">
          <label for="url">Current website URL</label>
          <input type="url" id="url" name="url" placeholder="https://">
        </div>
        <div class="form-row">
          <label for="notes">What's not working right now?</label>
          <textarea id="notes" name="notes"></textarea>
        </div>
        <button type="submit" class="btn-primary">Request my free call</button>
      </form>
      <p class="book-note">No pitch deck, no pressure. If Webflow isn't the right move for you, I'll say so.</p>
    </div>
  </section>
'''
    schema = faq_schema(faqs)
    bschema = breadcrumb_schema(slug, crumb_label)
    url = f"{SITE}/{slug}.html"
    return HEAD.format(title=title, description=description, schema=schema,
                        url=url, og_image=OG_IMAGE, breadcrumb_schema=bschema) + body + TAIL


PAGES = []

# ---------------- Shopify ---------------- (keyword: "shopify to webflow")
PAGES.append(dict(
    slug="shopify-to-webflow",
    eyebrow="Shopify to Webflow",
    headline="Move your storefront to Webflow without breaking checkout.",
    sub="Keep your products, payments, and conversions working, while fixing what Shopify's theme system can't.",
    title="Shopify to Webflow Migration | Webflow Migration Expert",
    description="Migrate your Shopify store to Webflow without losing checkout, product data, or search rankings. Certified Webflow Expert.",
    problems=[
        ('<rect x="3" y="6" width="14" height="10" rx="2"/><path d="M6 6V4.5A2.5 2.5 0 018.5 2h3A2.5 2.5 0 0114 4.5V6"/>',
         "Boxed in by your theme",
         "Shopify themes look like Shopify themes. Custom layouts, non-standard pages, and brand-specific design usually mean fighting Liquid or paying for app after app."),
        ('<circle cx="10" cy="10" r="7"/><path d="M10 6v4l3 2"/>',
         "Apps slowing you down",
         "Every app you install to patch a gap adds another script to your storefront. Page speed and Core Web Vitals take the hit, and so does conversion."),
        ('<path d="M10 2l6.5 3.5v9L10 18l-6.5-3.5v-9L10 2z"/><path d="M10 9v5M10 6.2v.1"/>',
         "Content pages feel like an afterthought",
         "Shopify is built for product pages. Landing pages, blog content, and anything design-heavy end up feeling bolted on."),
    ],
    note_title="Your checkout options, explained honestly.",
    note_body="Two real paths, depending on your catalog. Simpler stores can move to Webflow's own e-commerce entirely, checkout included. Larger catalogs usually keep Shopify running for checkout, with Webflow rebuilding the storefront around it for design and speed. We'll settle which one fits during the audit.",
    faqs=[
        ("Do I lose my product data?", "No. Product titles, descriptions, images, variants, and collections all carry over as part of the migration, whichever checkout path we land on."),
        ("Can I keep using Shopify Payments?", "In most setups, yes. If we keep Shopify running for checkout behind a Webflow front end, your existing payment processor and fulfillment stay exactly as they are."),
        ("Will my product pages still rank?", "That's the point of the redirect map and metadata carryover built into every migration. Nothing changes on Google's end unless a URL actually moves without a redirect, which we won't let happen."),
        ("What happens to my Shopify apps?", "We audit what each app is actually doing for you. Some get replaced by native Webflow functionality, some stay if you're keeping Shopify for checkout. Nothing gets dropped without a plan for what replaces it."),
    ],
    platform_value="Shopify",
))

# ---------------- WordPress ---------------- (keyword: "wordpress to webflow")
PAGES.append(dict(
    slug="wordpress-to-webflow",
    eyebrow="WordPress to Webflow",
    headline="Leave plugin bloat and security patches behind.",
    sub="Keep every page and blog post's rankings intact, while getting off a stack of plugins, updates, and hosting headaches.",
    title="WordPress to Webflow Migration | Webflow Migration Expert",
    description="Migrate your WordPress site to Webflow without losing your blog's SEO rankings. No more plugins, security patches, or slow hosting.",
    problems=[
        ('<path d="M10 3v4M10 13v4M3 10h4M13 10h4"/><circle cx="10" cy="10" r="2.5"/>',
         "A plugin for everything",
         "SEO plugin, form plugin, page builder plugin, caching plugin, security plugin. Each one is a dependency that can break on the next update."),
        ('<rect x="3" y="4" width="14" height="12" rx="2"/><path d="M3 8h14"/>',
         "Stuck maintaining hosting",
         "Updates, backups, and security patches are your job now, or your host's, at a monthly cost that adds up whether you touch the site or not."),
        ('<circle cx="10" cy="10" r="7"/><path d="M10 6v4l3 2"/>',
         "Page builder bloat",
         "Elementor, Divi, and similar builders generate heavy, messy code under the hood, even when the page looks simple."),
    ],
    note_title="Your blog's rankings are the whole ballgame.",
    note_body="Years of ranking blog content is the first thing a bad migration destroys. Every URL, title, meta description, and internal link gets mapped and preserved, with redirects on anything that changes. This is the most common way DIY migrations lose traffic, and it's entirely avoidable.",
    faqs=[
        ("Will my blog posts keep their rankings?", "That's the priority of the whole migration plan. URLs, metadata, and internal links are mapped and preserved, with redirects on anything that changes."),
        ("What about my WordPress plugins?", "We audit what each plugin does and replace it with native Webflow functionality where one exists (forms, SEO fields, CMS collections). Nothing gets left behind without a plan."),
        ("Do I still need to manage hosting and updates after this?", "No. Webflow hosts the site, handles SSL, CDN, and uptime, so there's no more plugin updates or security patching on your end."),
        ("Can Webflow's CMS handle a large blog?", "Yes, Webflow's CMS is built for exactly this: structured content, categories, and templated blog layouts that scale to hundreds of posts."),
    ],
    platform_value="WordPress",
))

# ---------------- Wix ---------------- (keyword: "wix to webflow")
PAGES.append(dict(
    slug="wix-to-webflow",
    eyebrow="Wix to Webflow",
    headline="Rebuild past Wix's design ceiling.",
    sub="For teams who've hit Wix's limits and want a site that loads faster, ranks better, and doesn't look like a template.",
    title="Wix to Webflow Migration | Webflow Migration Expert",
    description="Migrate your Wix site to Webflow for real custom design, faster load times, and better SEO. Certified Webflow Expert.",
    problems=[
        ('<rect x="3" y="6" width="14" height="10" rx="2"/><path d="M6 6V4.5A2.5 2.5 0 018.5 2h3A2.5 2.5 0 0114 4.5V6"/>',
         "Design ceiling",
         "Wix's drag-and-drop editor is easy to start with and hard to outgrow. Custom interactions and non-standard layouts run into real limits fast."),
        ('<circle cx="10" cy="10" r="7"/><path d="M10 6v4l3 2"/>',
         "Speed and SEO limitations",
         "Wix has improved, but sites still tend to ship heavier code than a hand-built Webflow site, and that gap shows up in Core Web Vitals and rankings."),
        ('<path d="M10 2l6.5 3.5v9L10 18l-6.5-3.5v-9L10 2z"/><path d="M10 9v5M10 6.2v.1"/>',
         "Locked into the platform",
         "Wix doesn't offer a clean way to export your site. If you ever want to leave, you're rebuilding from scratch, which is exactly what this migration is for."),
    ],
    note_title="Wix migrations take more manual work, and that's fine.",
    note_body="Wix doesn't offer a clean content export, so moving your pages, copy, and images is manual work on our end, factored into the timeline upfront. What you get is a site built from real code instead of a proprietary editor, the whole reason to make this move.",
    faqs=[
        ("Can you actually get my content out of Wix?", "Yes. Wix doesn't offer a clean export, so content is migrated manually as part of the build, page copy, images, and structure all carried over into Webflow."),
        ("Will my site actually look different, or just live on a new platform?", "Different, in the ways that matter. You get a custom design built to spec instead of a template, not just a copy of your current Wix site hosted somewhere else."),
        ("Is my Wix SEO going to carry over?", "Existing rankings are protected with a redirect map and matched metadata. If your Wix site was under-optimized to begin with, this is also a natural point to fix that."),
        ("How long does a Wix migration take?", "Slightly longer than a WordPress migration on average, because of the manual content transfer, but you'll get a firm timeline after the audit, not a guess."),
    ],
    platform_value="Wix",
))

# ---------------- Squarespace ---------------- (keyword: "squarespace to webflow")
PAGES.append(dict(
    slug="squarespace-to-webflow",
    eyebrow="Squarespace to Webflow",
    headline="Get the design freedom Squarespace won't give you.",
    sub="For design-conscious teams who've hit the limits of template editing and want full control without losing what already ranks.",
    title="Squarespace to Webflow Migration | Webflow Migration Expert",
    description="Migrate your Squarespace site to Webflow without losing your SEO rankings. Real custom design, faster load times, no more template constraints.",
    problems=[
        ('<rect x="3" y="6" width="14" height="10" rx="2"/><path d="M6 6V4.5A2.5 2.5 0 018.5 2h3A2.5 2.5 0 0114 4.5V6"/>',
         "Every site looks like Squarespace",
         "The templates are polished, but they're also everywhere. Standing out means fighting the block editor for anything outside its defaults."),
        ('<path d="M10 3v4M10 13v4M3 10h4M13 10h4"/><circle cx="10" cy="10" r="2.5"/>',
         "Custom code feels bolted on",
         "Injected code blocks and workarounds are the only way to get real custom behavior, and they tend to break on the next template update."),
        ('<circle cx="10" cy="10" r="7"/><path d="M10 6v4l3 2"/>',
         "E-commerce features locked behind tiers",
         "Real store functionality means upgrading plans and still working within Squarespace's checkout and product limitations."),
    ],
    note_title="Squarespace exports cleanly, custom code usually doesn't.",
    note_body="Squarespace offers a real content export, so pages and posts move over in reasonable shape. Custom code blocks are where it gets messy, those get rebuilt properly rather than pasted in as another workaround. Redirects and metadata get the same treatment as any migration, so rankings carry over.",
    faqs=[
        ("Will my Squarespace content export cleanly?", "Mostly, yes. Pages and blog content export in usable shape, though formatting and any custom code blocks get manually rebuilt to work properly in Webflow rather than copied as-is."),
        ("Will I lose my search rankings?", "Not if the migration is done properly, with a full redirect map and matched metadata. That's standard on every migration, not an add-on."),
        ("Can Webflow match Squarespace's design polish?", "Webflow can go further, since you're not working inside a template. Anything you've seen a Squarespace site do, and most things you haven't, are possible."),
        ("What about my Squarespace store?", "Depending on your catalog size, either Webflow's native e-commerce replaces it fully, or we keep your existing checkout running behind a rebuilt Webflow front end. We'll figure out which fits during the audit."),
    ],
    platform_value="Squarespace",
))

# ---------------- HTML/static ---------------- (keyword: "html to webflow")
PAGES.append(dict(
    slug="html-to-webflow",
    eyebrow="HTML to Webflow",
    headline="Turn a static HTML site into one you can actually edit.",
    sub="For hand-coded, template-built, or inherited sites where every change means touching code.",
    title="HTML to Webflow Migration | Webflow Migration Expert",
    description="Migrate a static HTML site to Webflow and get a real visual editor, a CMS, and faster hosting, without losing your existing search rankings.",
    problems=[
        ('<path d="M10 3v4M10 13v4M3 10h4M13 10h4"/><circle cx="10" cy="10" r="2.5"/>',
         "Every edit needs a developer",
         "No visual editor, no CMS. Updating a headline or swapping an image means opening the code, or paying someone who will."),
        ('<rect x="3" y="4" width="14" height="12" rx="2"/><path d="M3 8h14"/>',
         "Hosting and security are on you",
         "SSL renewals, server uptime, and security patches all sit with whoever's hosting the static files, usually you, usually forgotten about until something breaks."),
        ('<circle cx="10" cy="10" r="7"/><path d="M10 6v4l3 2"/>',
         "Mobile and speed were an afterthought",
         "A lot of hand-coded sites predate mobile-first design entirely, and it shows in how they perform on a phone and in Core Web Vitals."),
    ],
    note_title="This is usually the cleanest migration there is.",
    note_body="No proprietary export format, no plugin ecosystem, no page builder markup to untangle, just content sitting in the code. That makes this one of the more straightforward migrations to scope: we pull URLs and content from the source files, map redirects, and rebuild in Webflow with a CMS behind the parts that should be editable.",
    faqs=[
        ("Do I need to give you access to my hosting or GitHub?", "Yes, FTP, a Git repo, or however your files are currently hosted. That's how we pull your existing pages and content accurately rather than working from screenshots."),
        ("Will my URLs and rankings carry over?", "Yes. Existing URLs get mapped to their Webflow equivalents with redirects on anything that changes, the same as any other migration."),
        ("Can you turn static pages into something I can edit myself?", "That's the main point of this migration. Content that makes sense as a blog post, product, or repeatable page type gets moved into Webflow's CMS so you can edit it without touching code."),
        ("Is this faster or cheaper than other migrations?", "Often faster to scope, since there's no plugin or app ecosystem to audit. Final cost still depends on how many pages and how custom the new design is."),
    ],
    platform_value="HTML/static",
))

# ---------------- Figma ---------------- (keyword: "figma to webflow")
PAGES.append(dict(
    slug="figma-to-webflow",
    eyebrow="Figma to Webflow",
    headline="Turn your Figma design into a real, working website.",
    sub="For designers and founders with a finished design that needs to be built properly: responsive, interactive, and structured the way Webflow actually works.",
    title="Figma to Webflow Development | Webflow Migration Expert",
    description="Turn your Figma design into a fully responsive, editable Webflow site. Pixel-accurate builds with interactions, CMS structure, and clean class naming.",
    problems=[
        ('<rect x="3" y="6" width="14" height="10" rx="2"/><path d="M6 6V4.5A2.5 2.5 0 018.5 2h3A2.5 2.5 0 0114 4.5V6"/>',
         "Figma isn't responsive",
         "A static frame doesn't tell you what happens between breakpoints. That interpretation gets done badly, or not at all, by a lot of Figma-to-Webflow builds."),
        ('<path d="M10 3v4M10 13v4M3 10h4M13 10h4"/><circle cx="10" cy="10" r="2.5"/>',
         "Messy class structure",
         "Webflow rewards a clean, reusable class system. A lot of freelance builds skip this and hand you an unmaintainable project full of one-off classes."),
        ('<circle cx="10" cy="10" r="7"/><path d="M10 6v4l3 2"/>',
         "Interactions and states get lost",
         "Hover states, scroll animations, and prototype interactions in Figma don't translate automatically. Someone has to actually build them."),
    ],
    note_title="New build or replacing a live site, the approach differs.",
    note_body="Brand new site with nothing live yet: we go straight from your Figma file to a published build, no redirects needed. Redesigning something live: your current URLs and rankings still matter, and that gets folded into the build plan.",
    faqs=[
        ("Do you need the Figma file, or can you work from screenshots?", "The actual Figma file, with layers and components intact. That's what makes breakpoints, spacing, and reusable components accurate instead of guessed at."),
        ("Will the build match my design exactly?", "Yes, spacing, typography, and layout are built to match your file precisely, across breakpoints, not just on desktop."),
        ("What about interactions and animations in my prototype?", "Hover states, scroll triggers, and page transitions from your Figma prototype get rebuilt as real Webflow interactions, not left out."),
        ("Will I be able to edit the site myself after handoff?", "Yes. Content that should be editable (blog posts, team members, case studies) gets built into Webflow's CMS, with a walkthrough so you're not locked out of your own site."),
    ],
    platform_value="Figma",
    process_steps=[
        ("Design review", "Full review of your Figma file: components, breakpoints, states, and interactions that need to carry over into a working site."),
        ("Build plan", "Every Figma frame mapped to a Webflow page, with responsive breakpoints and CMS structure defined before development starts."),
        ("Build in Webflow", "Your design built clean in Webflow with a reusable class system, tested across breakpoints before anyone else sees it."),
        ("Launch &amp; handoff", "Published live (or DNS cutover if replacing an existing site), plus a walkthrough so you can edit the new site yourself."),
    ],
    process_h2="From Figma file to published site, without losing the design in translation.",
    process_sub="You'll see the build on staging before anything goes live, so you can check it against the Figma file yourself.",
))

for p in PAGES:
    p.setdefault("process_steps", None)
    p.setdefault("process_h2", None)
    p.setdefault("process_sub", None)

outdir = "/home/claude/wme"
for p in PAGES:
    html = page(
        p["slug"], p["eyebrow"], p["headline"], p["sub"], p["title"], p["description"],
        p["problems"], p["note_title"], p["note_body"], p["faqs"], p["platform_value"],
        process_steps=p["process_steps"], process_h2=p["process_h2"], process_sub=p["process_sub"],
    )
    path = os.path.join(outdir, p["slug"] + ".html")
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path, len(html))
