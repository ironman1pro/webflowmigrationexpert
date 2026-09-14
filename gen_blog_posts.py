import os, json, re

SITE = "https://webflowmigrationexpert.com"
OG_IMAGE = SITE + "/images/og-image.png"
PUB_DATE = "2026-09-14"

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
<meta property="og:type" content="article">
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
<link rel="canonical" href="{url}">
{breadcrumb_schema}
{article_schema}
</head>
<body>

<site-nav></site-nav>

<main>
  <section class="page-hero" style="padding-bottom:0;">
    <div class="wrap" style="max-width:700px;">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/blog/">Blog</a><span class="sep">/</span><span>{headline}</span></nav>
      <span class="eyebrow">{tag}</span>
      <h1 style="font-size:clamp(28px,4vw,42px);">{headline}</h1>
      <div class="post-meta">
        <span>Webflow Migration Expert</span>
        <span>&middot;</span>
        <span>{read_time}</span>
      </div>
    </div>
  </section>

  <article class="post-body">
"""

TAIL_TEMPLATE = """
    <div class="post-cta">
      <h3>{cta_h3}</h3>
      <p>{cta_p}</p>
      <a class="btn-primary" href="{cta_href}">Book your free call</a>
    </div>
  </article>
</main>

<site-footer></site-footer>

<script src="/nav-footer.js" defer></script>
</body>
</html>
"""

POSTS = []

# ---------------- Shopify ----------------
POSTS.append(dict(
    slug="shopify-to-webflow-checkout-explained",
    tag="Shopify",
    title="Shopify to Webflow: What Happens to Your Checkout | Webflow Migration Expert",
    description="The honest answer on what happens to your Shopify checkout when you migrate to Webflow, and the two real paths to choose between.",
    headline="Shopify to Webflow: What Actually Happens to Your Checkout",
    read_time="5 min read",
    card_desc="The one question every Shopify migration starts with, and the honest answer.",
    body="""
    <p>This is the first question every Shopify store owner asks, and the honest answer is: it depends on your catalog. There are two real paths, not one, and picking the wrong one is the most common mistake in a Shopify migration.</p>

    <h2>Path one: full Webflow e-commerce</h2>
    <p>For simpler stores, smaller catalogs, straightforward variants, standard payment needs, Webflow's own e-commerce can fully replace Shopify. Checkout, product pages, and cart all run natively in Webflow, and Shopify drops out of the picture entirely.</p>

    <h2>Path two: Webflow front end, Shopify checkout</h2>
    <p>For larger catalogs or stores that depend on Shopify-specific apps, subscriptions, or a particular payment setup, the better move is usually a Webflow front end with Shopify running quietly behind it for checkout and fulfillment. You get the design freedom and speed of Webflow without rebuilding a complex commerce backend from scratch.</p>

    <h2>How to know which one you need</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Under a few hundred SKUs with simple variants: Webflow e-commerce is usually enough</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Subscriptions, complex shipping rules, or Shopify-specific apps you rely on: keep Shopify for checkout</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Either way, your product data, images, and collections carry over as part of the migration</li>
    </ul>

    <p>This gets decided during the audit, before any build work starts, not guessed at halfway through.</p>
""",
    cta_h3="Not sure which path fits your store?",
    cta_p="Get a free 15-minute call and a straight answer before you commit to either.",
    cta_href="/shopify-to-webflow.html#book",
))

# ---------------- Wix ----------------
POSTS.append(dict(
    slug="wix-to-webflow-content-export",
    tag="Wix",
    title="Wix to Webflow: Why You Can't Just Export and Reupload | Webflow Migration Expert",
    description="Wix doesn't offer a clean content export. Here's what that actually means for a Wix to Webflow migration timeline.",
    headline="Wix to Webflow: Why You Can't Just Export and Reupload",
    read_time="4 min read",
    card_desc="Wix doesn't offer a clean export. Here's what that means for your timeline.",
    body="""
    <p>WordPress has an export button. Wix doesn't. If you're planning a Wix to Webflow migration expecting to click one button and get your content out, that's the first thing to unlearn.</p>

    <h2>What Wix actually gives you</h2>
    <p>Wix locks your content inside its own editor with no structured export format. There's no XML dump, no CSV of pages, nothing that maps cleanly onto a new platform. Your pages, copy, and images all exist, they're just not portable in the way WordPress or Squarespace content is.</p>

    <h2>What that means in practice</h2>
    <p>Content has to be pulled manually: page by page, copy and images captured directly from the live site rather than an export file. It's more labor, not more risk, and it's factored into the migration timeline upfront rather than discovered halfway through.</p>

    <h2>What doesn't change</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Your URLs still get mapped with redirects, so rankings are protected the same as any migration</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Metadata gets carried over or improved, not left blank</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>You end up with a real, editable site instead of a Wix export problem to solve again later</li>
    </ul>

    <p>A Wix migration usually runs a bit longer than a WordPress one for exactly this reason. That's not a red flag, it's just what an honest timeline looks like.</p>
""",
    cta_h3="Planning a move off Wix?",
    cta_p="Get a free 15-minute call and a realistic timeline before you start.",
    cta_href="/wix-to-webflow.html#book",
))

# ---------------- Squarespace ----------------
POSTS.append(dict(
    slug="squarespace-to-webflow-what-survives",
    tag="Squarespace",
    title="Squarespace to Webflow: What Survives the Move | Webflow Migration Expert",
    description="What carries over cleanly in a Squarespace to Webflow migration, and what needs to be rebuilt rather than copied.",
    headline="Squarespace to Webflow: What Survives the Move (and What Doesn't)",
    read_time="4 min read",
    card_desc="What exports cleanly from Squarespace, and what has to be rebuilt.",
    body="""
    <p>Squarespace sits between Wix and WordPress on portability. It offers a real content export, unlike Wix, but it's not a clean 1:1 transfer either. Here's what actually moves and what needs rebuilding.</p>

    <h2>What survives</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Page and blog post content exports in reasonably usable shape</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Images and basic structure generally carry over without much rework</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>URLs and rankings, protected with a redirect map the same as any migration</li>
    </ul>

    <h2>What doesn't</h2>
    <p>Custom code blocks and injected scripts are where Squarespace exports fall apart. Anything you added as a workaround for a limitation Squarespace's editor imposed gets rebuilt properly in Webflow rather than pasted back in as another patch. It's usually a small part of the site by volume, but it's the part that takes real attention.</p>

    <h2>The upside</h2>
    <p>This is also the natural point to fix design constraints you'd been working around. Templates that limited layout options, e-commerce features locked behind a plan tier, all of that goes away once the site is rebuilt on Webflow's own terms instead of inside someone else's block editor.</p>
""",
    cta_h3="Curious what your Squarespace site would look like on Webflow?",
    cta_p="Get a free 15-minute call to see what actually needs rebuilding.",
    cta_href="/squarespace-to-webflow.html#book",
))

# ---------------- HTML ----------------
POSTS.append(dict(
    slug="html-to-webflow-easiest-migration",
    tag="HTML",
    title="Static HTML to Webflow: The Simplest Migration There Is | Webflow Migration Expert",
    description="Why migrating a static HTML site to Webflow tends to be the cleanest migration of all, and what to prepare before you start.",
    headline="Static HTML to Webflow: The Easiest Migration You'll Ever Do",
    read_time="4 min read",
    card_desc="No plugins, no proprietary export. Here's why static HTML migrates cleanly.",
    body="""
    <p>Of every migration path, a plain static HTML site is usually the most straightforward. No plugin ecosystem to untangle, no proprietary export format to fight, just markup and content that's already sitting there in the code.</p>

    <h2>Why it's simpler</h2>
    <p>WordPress migrations mean auditing plugins. Wix migrations mean manually extracting content with no export tool. A static HTML site has neither problem: the content is in the files, and pulling it out accurately is mostly a matter of having access to them.</p>

    <h2>What we actually need from you</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>FTP access, a Git repo, or however the files are currently hosted</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>A list of any forms or integrations currently wired into the site</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Nothing else. There's no export tool to wrestle with</li>
    </ul>

    <h2>What you get that you didn't have</h2>
    <p>The real upgrade isn't speed, hand-coded HTML can already be fast. It's editability. Once content that makes sense as a blog post, service, or repeatable page type gets moved into Webflow's CMS, updates stop requiring a developer or a code editor.</p>
""",
    cta_h3="Have a static site ready to move?",
    cta_p="Get a free 15-minute call to see how fast this one could actually go.",
    cta_href="/html-to-webflow.html#book",
))

# ---------------- Figma ----------------
POSTS.append(dict(
    slug="figma-to-webflow-briefing-a-developer",
    tag="Figma",
    title="Figma to Webflow: How to Brief a Developer So Nothing Gets Lost | Webflow Migration Expert",
    description="What to hand over with your Figma file so a Webflow build actually matches your design, breakpoints and interactions included.",
    headline="Figma to Webflow: How to Brief a Developer So Nothing Gets Lost",
    read_time="5 min read",
    card_desc="What to hand over with your Figma file so nothing gets lost in the build.",
    body="""
    <p>A Figma file alone isn't a full brief. It shows what the design looks like on one frame, not what happens between breakpoints, how something should behave on hover, or which parts should be editable later. Here's what closes that gap.</p>

    <h2>The Figma file itself, not a screenshot</h2>
    <p>Layers, components, and auto-layout intact. A flattened export loses exactly the information that makes spacing and component reuse accurate instead of estimated.</p>

    <h2>Breakpoints, even rough ones</h2>
    <p>If your file only shows desktop, say so, and say what should happen on mobile. Without that, someone is interpreting your intent instead of building it, and interpretation is where builds start looking different from the design.</p>

    <h2>Interactions and states</h2>
    <p>Hover states, scroll animations, prototype transitions, anything Figma's own prototyping mode shows needs to be called out explicitly if it should exist in the live build. It doesn't translate automatically.</p>

    <h2>What should be editable later</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Blog posts, team members, case studies: anything repeatable belongs in a CMS collection, not a static page</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Say this upfront. Retrofitting CMS structure after a static build costs more than planning for it</li>
    </ul>

    <h2>New build, or replacing something live</h2>
    <p>If this design replaces an existing site, your current URLs and rankings matter and need a redirect plan. If it's a brand new site, that step doesn't apply. Either way, say which one it is before the build starts.</p>
""",
    cta_h3="Have a Figma file ready to build?",
    cta_p="Get a free 15-minute call to talk through your file and what it needs.",
    cta_href="/figma-to-webflow.html#book",
))


def strip_html(s):
    return re.sub("<[^<]+?>", "", s)

def breadcrumb_schema(slug, headline):
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": strip_html(headline), "item": f"{SITE}/blog/{slug}.html"},
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'

def article_schema(slug, headline, description, url):
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": strip_html(headline),
        "description": description,
        "image": OG_IMAGE,
        "author": {"@type": "Organization", "name": "Webflow Migration Expert", "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "Webflow Migration Expert", "logo": {"@type": "ImageObject", "url": SITE + "/apple-touch-icon.png"}},
        "datePublished": PUB_DATE,
        "dateModified": PUB_DATE,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'


outdir = "/home/claude/wme/blog"
for p in POSTS:
    url = f"{SITE}/blog/{p['slug']}.html"
    html = HEAD.format(
        title=p["title"], description=p["description"], tag=p["tag"], headline=p["headline"],
        read_time=p["read_time"], url=url, og_image=OG_IMAGE,
        breadcrumb_schema=breadcrumb_schema(p["slug"], p["headline"]),
        article_schema=article_schema(p["slug"], p["headline"], p["description"], url),
    ) \
        + p["body"] \
        + TAIL_TEMPLATE.format(cta_h3=p["cta_h3"], cta_p=p["cta_p"], cta_href=p["cta_href"])
    path = os.path.join(outdir, p["slug"] + ".html")
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path, len(html))

# print card snippets for blog/index.html
print("\n--- CARDS ---")
for p in POSTS:
    print(f'<a class="blog-card" href="/blog/{p["slug"]}.html"><span class="tag">{p["tag"]}</span><h3>{p["headline"]}</h3><p>{p["card_desc"]}</p><span class="meta">{p["read_time"]}</span></a>')
