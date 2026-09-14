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

# ---------------- Shopify (2) ----------------
POSTS.append(dict(
    slug="shopify-to-webflow-product-data-migration",
    tag="Shopify",
    title="Shopify to Webflow: Migrating Your Product Catalog Without Losing SEO | Webflow Migration Expert",
    description="What actually happens to your Shopify product titles, descriptions, images, and metafields when you migrate to Webflow, and how product pages keep ranking.",
    headline="Shopify to Webflow: Migrating Your Product Catalog Without Losing SEO",
    read_time="5 min read",
    card_desc="What happens to your product data, and how product pages keep ranking.",
    body="""
    <p>Product data is the part of a Shopify migration people worry about most, and the part that actually moves the cleanest. Here's what happens to it, field by field.</p>

    <h2>What carries over directly</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Titles, descriptions, images, variants, and collections map into Webflow's CMS as structured fields, not pasted-in text</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Existing page titles and meta descriptions get mapped into Webflow's SEO fields per product, not left blank</li>
    </ul>

    <h2>What needs deliberate work: metafields and structured data</h2>
    <p>Shopify metafields (size charts, custom specs, anything outside the standard fields) don't have a generic destination, they get mapped to custom CMS fields one by one during the audit. Product structured data (schema.org markup that powers rich results in search) also doesn't carry over automatically and has to be rebuilt so product pages keep the same search appearance they had on Shopify.</p>

    <h2>Why this protects rankings, not just data</h2>
    <p>Search engines rank product pages partly on that structured data and matched metadata, not just the visible copy. Skipping this step is how a migration keeps the words on the page but quietly loses the ranking signals underneath it. Treating it as a checklist item during the audit, not an afterthought, is what keeps product pages performing the same after launch as before it.</p>
""",
    cta_h3="Have a large Shopify catalog to migrate?",
    cta_p="Get a free 15-minute call to see what the audit would look like for your catalog.",
    cta_href="/shopify-to-webflow.html#book",
))

POSTS.append(dict(
    slug="shopify-to-webflow-redirect-map",
    tag="Shopify",
    title="Shopify to Webflow: Building a Redirect Map That Actually Works | Webflow Migration Expert",
    description="How a proper 301 redirect map protects a Shopify store's rankings during a Webflow migration, and the mistakes that quietly break it.",
    headline="Shopify to Webflow: Building a Redirect Map That Actually Works",
    read_time="4 min read",
    card_desc="The redirect map is what protects your rankings. Here's how to get it right.",
    body="""
    <p>A redirect map is the single most important technical piece of a Shopify migration, and also the easiest to get almost right, which is worse than getting it obviously wrong.</p>

    <h2>What a redirect map actually is</h2>
    <p>Every URL on your current Shopify store gets an entry, old URL, new URL, as a 301 (permanent) redirect. That includes product pages, collection pages, blog posts, and any standalone pages, not just your homepage and top nav links.</p>

    <h2>Where redirect maps usually break</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Redirect chains: a URL that redirects to another URL that also redirects, instead of straight to the final destination</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Missed URLs: seasonal collections, discontinued products still ranking, or paginated category pages that get forgotten</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>302 (temporary) redirects used where a 301 was needed, which tells search engines the move isn't permanent</li>
    </ul>

    <h2>How it should actually happen</h2>
    <p>The map gets built during the audit, before any design or build work starts, pulled from your actual current sitemap and search console data rather than guessed at from memory. Webflow supports redirects natively in project settings, so once the map is built it's a configuration step, not custom development.</p>
""",
    cta_h3="Not sure what your current URL structure even is?",
    cta_p="Get a free 15-minute call and we'll pull it together as part of the audit.",
    cta_href="/shopify-to-webflow.html#book",
))

# ---------------- WordPress (2) ----------------
POSTS.append(dict(
    slug="wordpress-to-webflow-plugins-explained",
    tag="WordPress",
    title="WordPress to Webflow: What Happens to Your Plugins | Webflow Migration Expert",
    description="A plugin-by-plugin look at what carries over when you migrate from WordPress to Webflow, and what gets replaced by native functionality.",
    headline="WordPress to Webflow: What Happens to Your Plugins",
    read_time="4 min read",
    card_desc="A plugin-by-plugin look at what carries over and what gets replaced.",
    body="""
    <p>Every WordPress site is really a stack of plugins wearing a theme. Migrating to Webflow means going through that stack one plugin at a time and deciding what each one actually needs to become.</p>

    <h2>SEO plugins (Yoast, RankMath, and similar)</h2>
    <p>The meta titles, descriptions, and Open Graph settings stored in these plugins get mapped into Webflow's built-in SEO fields, which exist natively per page and per CMS item, no plugin required.</p>

    <h2>Form plugins</h2>
    <p>Contact forms, quote requests, anything collecting submissions moves to Webflow's native form element, connected to Formspree or a similar service. Field names and required fields get matched exactly so nothing in your notification emails or spreadsheets changes shape.</p>

    <h2>Page builder plugins (Elementor, Divi, and similar)</h2>
    <p>This is the one that doesn't map field by field. Page builder markup is rebuilt directly in Webflow's own visual canvas, which is the actual point of the migration, not a technicality to work around.</p>

    <h2>Caching, security, and backup plugins</h2>
    <p>These stop being necessary entirely. Webflow hosts, handles SSL, CDN, and uptime as part of the platform, so there's nothing left for these plugins to protect.</p>
""",
    cta_h3="Wondering what your specific plugin stack turns into?",
    cta_p="Get a free 15-minute call and a plugin-by-plugin read on your site.",
    cta_href="/wordpress-to-webflow.html#book",
))

POSTS.append(dict(
    slug="wordpress-to-webflow-large-blog-migration",
    tag="WordPress",
    title="WordPress to Webflow: Migrating a Large Blog Without Losing Traffic | Webflow Migration Expert",
    description="How to move a large WordPress blog into Webflow's CMS without breaking category pages, pagination, or the URLs that already rank.",
    headline="WordPress to Webflow: Migrating a Large Blog Without Losing Traffic",
    read_time="5 min read",
    card_desc="Moving hundreds of posts without breaking what already ranks.",
    body="""
    <p>A blog with a few hundred posts isn't riskier to migrate than a five-page site, it's just less forgiving of shortcuts. Here's what actually matters at that scale.</p>

    <h2>Categories and tags become CMS structure, not labels</h2>
    <p>In Webflow, categories and tags are modeled as their own CMS collections, referenced by each post, rather than plain text labels. That's what keeps category archive pages, filtering, and related-post logic working the way they did on WordPress, not just the posts themselves.</p>

    <h2>Pagination and archive pages</h2>
    <p>Category pages, tag pages, and paginated archives all need their own redirect entries, not just individual posts. This is the part of a large blog migration that gets missed most often, because it's easy to map the visible posts and forget the list pages that organize them.</p>

    <h2>Prioritizing the redirect map by traffic</h2>
    <p>With hundreds of URLs, the map gets built in order of what's actually driving traffic and rankings right now, pulled from analytics and search console, so the highest-value posts are verified first rather than treated the same as a post from three years ago with no traffic.</p>

    <h2>The payoff</h2>
    <p>Done this way, a large blog migration protects the specific posts and pages your traffic depends on, while giving you a CMS that's actually easier to manage at that volume than WordPress's admin ever was.</p>
""",
    cta_h3="Have a large WordPress blog to move?",
    cta_p="Get a free 15-minute call to talk through scope and timeline for your archive size.",
    cta_href="/wordpress-to-webflow.html#book",
))

# ---------------- Wix (2) ----------------
POSTS.append(dict(
    slug="wix-to-webflow-seo-settings",
    tag="Wix",
    title="Wix to Webflow: What Happens to Your Wix SEO Settings | Webflow Migration Expert",
    description="Wix's SEO panel settings don't export. Here's what has to be manually rebuilt in Webflow, and why that's often an improvement.",
    headline="Wix to Webflow: What Happens to Your Wix SEO Settings",
    read_time="4 min read",
    card_desc="Wix SEO settings don't export. Here's what gets rebuilt, and why that's often better.",
    body="""
    <p>Like Wix content, Wix's SEO settings don't come with an export button. Page titles, meta descriptions, and any structured data configured through Wix's SEO panel have to be pulled from the live site and re-entered, the same manual process as the content itself.</p>

    <h2>What gets rebuilt</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Page titles and meta descriptions, pulled from the live site and entered into Webflow's per-page SEO fields</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Open Graph and social sharing settings, matched so links still preview correctly when shared</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>URL structure, mapped to a redirect plan since Wix and Webflow don't format URLs the same way by default</li>
    </ul>

    <h2>Why this is often a net improvement, not just a copy job</h2>
    <p>Wix sites frequently have thin or default SEO settings left over from the template, half-written meta descriptions, generic titles, missing alt text. Rebuilding this by hand is the natural point to fix it properly rather than migrate the same gaps onto a new platform.</p>

    <h2>What doesn't change</h2>
    <p>Whatever is already ranking well keeps its position, protected by the redirect map regardless of how the underlying settings get rebuilt. Improving weak pages and protecting strong ones happen in the same pass.</p>
""",
    cta_h3="Curious how your current Wix SEO actually looks?",
    cta_p="Get a free 15-minute call and an honest read on what's there now.",
    cta_href="/wix-to-webflow.html#book",
))

POSTS.append(dict(
    slug="wix-to-webflow-interactions",
    tag="Wix",
    title="Wix to Webflow: Rebuilding Your Site's Interactions and Animations | Webflow Migration Expert",
    description="Wix effects and animations don't carry over automatically. How hover states, scroll effects, and transitions get rebuilt natively in Webflow.",
    headline="Wix to Webflow: Rebuilding Your Site's Interactions and Animations",
    read_time="4 min read",
    card_desc="Hover states and scroll effects don't export. Here's how they get rebuilt.",
    body="""
    <p>Any hover states, scroll effects, or entrance animations built with Wix's effects panel are configuration inside Wix itself, not portable code, so they get rebuilt rather than transferred.</p>

    <h2>How Webflow handles this differently</h2>
    <p>Webflow's native interactions panel builds hover, scroll, click, and page-load animations as timeline-based triggers tied directly to elements and classes, the same underlying approach as Wix's effects but with more control over timing, easing, and what triggers what.</p>

    <h2>What gets prioritized</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Interactions tied to core conversion moments (buttons, forms, key visuals) get rebuilt first and tested carefully</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Decorative-only effects are flagged during the audit so you can decide if they're worth rebuilding at all</li>
    </ul>

    <h2>Why this usually ends up faster and smoother</h2>
    <p>Webflow renders interactions with cleaner, more efficient code than Wix's editor tends to output, which is part of why sites migrated off Wix often feel noticeably snappier even before any other optimization work happens.</p>
""",
    cta_h3="Have specific animations you don't want to lose?",
    cta_p="Get a free 15-minute call and walk me through what your site does now.",
    cta_href="/wix-to-webflow.html#book",
))

# ---------------- Squarespace (2) ----------------
POSTS.append(dict(
    slug="squarespace-to-webflow-custom-code",
    tag="Squarespace",
    title="Squarespace to Webflow: Migrating Custom Code Blocks the Right Way | Webflow Migration Expert",
    description="Injected Squarespace code blocks are the part that doesn't export cleanly. Here's how they get rebuilt properly in Webflow instead of pasted back in.",
    headline="Squarespace to Webflow: Migrating Custom Code Blocks the Right Way",
    read_time="4 min read",
    card_desc="Custom code blocks are where Squarespace exports fall apart. Here's the fix.",
    body="""
    <p>Squarespace's content export is genuinely useful, but it stops being useful the moment your site relies on injected custom code, which most design-conscious Squarespace sites eventually do.</p>

    <h2>What custom code blocks usually are</h2>
    <p>Workarounds. Custom code on Squarespace tends to exist because the block editor couldn't natively do something, a specific layout, a third-party embed, a tracking script, a small interactive element. That code is tied to Squarespace's specific page structure and doesn't run correctly dropped into a different platform.</p>

    <h2>How it gets handled instead</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Each code block gets identified during the audit and matched to what it's actually trying to achieve, not just what it currently contains</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Where Webflow has a native element or interaction for it, that replaces the code entirely, cleaner and easier to maintain going forward</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Where custom code genuinely is the right tool (specific third-party embeds, tracking scripts), it gets rebuilt scoped correctly to Webflow's structure</li>
    </ul>

    <h2>The outcome</h2>
    <p>A site that does everything the old one did, without a collection of legacy workarounds that only made sense inside Squarespace's editor in the first place.</p>
""",
    cta_h3="Not sure how much custom code your site actually has?",
    cta_p="Get a free 15-minute call and we'll find out together during the audit.",
    cta_href="/squarespace-to-webflow.html#book",
))

POSTS.append(dict(
    slug="squarespace-to-webflow-commerce",
    tag="Squarespace",
    title="Squarespace to Webflow: What Happens to Your Squarespace Commerce | Webflow Migration Expert",
    description="Squarespace Commerce doesn't move to Webflow directly. The two real paths for migrating a Squarespace store, and how to pick between them.",
    headline="Squarespace to Webflow: What Happens to Your Squarespace Commerce",
    read_time="4 min read",
    card_desc="Squarespace Commerce doesn't move directly. Here are the two real paths.",
    body="""
    <p>If your Squarespace site sells anything, the commerce layer is the part that needs its own plan, separate from the design and content migration.</p>

    <h2>Path one: Webflow's native e-commerce</h2>
    <p>For simpler catalogs with standard variants and payment needs, Webflow's own e-commerce can replace Squarespace Commerce entirely. Products, checkout, and cart all run natively in Webflow.</p>

    <h2>Path two: a specialized commerce platform behind a Webflow front end</h2>
    <p>For larger catalogs, subscriptions, or inventory needs Squarespace Commerce was already stretching to cover, the better move is often a Webflow front end paired with a commerce platform built for that complexity, rather than forcing it into either Squarespace or Webflow's native tools.</p>

    <h2>What carries over either way</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Product titles, descriptions, and images migrate as structured data, not copy-pasted text</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Product page URLs get the same redirect-map treatment as every other page, so rankings on your best-selling products are protected</li>
    </ul>

    <p>Which path fits gets decided during the audit, based on catalog size and what you actually need from checkout, not assumed upfront.</p>
""",
    cta_h3="Selling through Squarespace right now?",
    cta_p="Get a free 15-minute call to figure out which commerce path fits your store.",
    cta_href="/squarespace-to-webflow.html#book",
))

# ---------------- HTML (2) ----------------
POSTS.append(dict(
    slug="html-to-webflow-cms-collections",
    tag="HTML",
    title="HTML to Webflow: Turning Repeated Static Pages Into a CMS Collection | Webflow Migration Expert",
    description="If your static site has a folder of near-identical HTML pages, those become a single templated Webflow CMS collection. Here's how that works.",
    headline="HTML to Webflow: Turning Repeated Static Pages Into a CMS Collection",
    read_time="4 min read",
    card_desc="A folder of near-identical pages becomes one editable CMS collection.",
    body="""
    <p>A lot of static HTML sites have a folder like this: dozens of product pages, team bios, or case studies, each one a separate HTML file that's really the same layout with different content pasted in. That pattern has a specific, much better home in Webflow.</p>

    <h2>What a CMS collection actually does</h2>
    <p>Instead of dozens of separate files, you get one collection template and one item per entry. Update the template once, styling changes apply everywhere. Add a new entry through a form, no new file, no copy-pasting a layout.</p>

    <h2>How the migration works</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>The audit identifies which pages are really one repeated pattern, not treated as one-off pages</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Each existing page's content gets pulled into structured CMS fields (title, image, body, whatever the pattern needs)</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Each item's URL gets mapped in the redirect plan so nothing that currently ranks moves without a redirect</li>
    </ul>

    <h2>Why this matters beyond convenience</h2>
    <p>This is usually the single biggest quality-of-life upgrade in an HTML migration. What used to require opening a code editor to add a new case study or product becomes a form anyone on the team can fill out.</p>
""",
    cta_h3="Have a folder of repeated static pages?",
    cta_p="Get a free 15-minute call and we'll see what it looks like as a CMS collection.",
    cta_href="/html-to-webflow.html#book",
))

POSTS.append(dict(
    slug="html-to-webflow-metadata",
    tag="HTML",
    title="HTML to Webflow: Preserving the SEO Metadata Already in Your Code | Webflow Migration Expert",
    description="Title tags, meta descriptions, and structured data already sitting in your static HTML need to be carried over deliberately. Here's what that involves.",
    headline="HTML to Webflow: Preserving the SEO Metadata Already in Your Code",
    read_time="4 min read",
    card_desc="Metadata already in your code needs to be carried over deliberately, not assumed.",
    body="""
    <p>A hand-coded site often has better metadata than people expect, someone wrote real title tags and meta descriptions at some point. The risk in a migration isn't that this data is hard to find, it's that it's easy to overlook because it's sitting quietly in the `&lt;head&gt;` of each file.</p>

    <h2>What gets pulled from the source files</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Title tags and meta descriptions, mapped one-to-one into Webflow's per-page or per-CMS-item SEO fields</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Open Graph tags and existing structured data (schema.org markup), rebuilt so search appearance doesn't change</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Canonical tags and any existing redirects already in place, factored into the new redirect map rather than ignored</li>
    </ul>

    <h2>Why access to the source matters here</h2>
    <p>This is part of why we ask for FTP or Git access rather than working from what's visible on the live pages, some of this metadata (canonical tags, certain schema types) doesn't render visibly and has to be read from the actual source.</p>

    <h2>The result</h2>
    <p>Whatever SEO groundwork already exists in your code comes with you to Webflow intact, rather than getting quietly reset to blank defaults during the rebuild.</p>
""",
    cta_h3="Want to know what metadata your current site actually has?",
    cta_p="Get a free 15-minute call and we'll pull it during the audit.",
    cta_href="/html-to-webflow.html#book",
))

# ---------------- Figma (2) ----------------
POSTS.append(dict(
    slug="figma-to-webflow-auto-layout",
    tag="Figma",
    title="Figma to Webflow: How Auto Layout Translates to a Real Website | Webflow Migration Expert",
    description="Figma's Auto Layout and Webflow's flexbox and grid tools work on the same underlying logic. Here's how that turns a design file into a responsive build.",
    headline="Figma to Webflow: How Auto Layout Translates to a Real Website",
    read_time="5 min read",
    card_desc="Auto Layout and Webflow's layout tools share the same logic. Here's how that helps.",
    body="""
    <p>The reason a well-structured Figma file builds so much faster and more accurately than a flat design comp is Auto Layout, and it's worth understanding why.</p>

    <h2>Auto Layout and flexbox solve the same problem</h2>
    <p>Figma's Auto Layout, spacing, padding, and alignment rules on a frame, maps closely onto the flexbox and grid tools Webflow's Designer is built on. A frame with Auto Layout spacing of 16px between items translates directly into a real, responsive gap in the build, not a guess based on how far apart things look in a static frame.</p>

    <h2>What that means in practice</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Components with Auto Layout wrap and reflow correctly at every breakpoint, not just the one Figma frame you designed</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Padding and spacing values transfer as exact numbers instead of being eyeballed from a screenshot</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Nested Auto Layout frames (a card inside a grid inside a section) map to nested flex and grid structures that stay editable, not flattened into fixed positions</li>
    </ul>

    <h2>What happens without it</h2>
    <p>A flat, non-Auto-Layout Figma file still builds, it just means more interpretation: guessing spacing, guessing what should happen between breakpoints, guessing which elements were meant to be reusable components. That's exactly the gap a proper briefing process is meant to close.</p>
""",
    cta_h3="Not sure if your Figma file uses Auto Layout properly?",
    cta_p="Get a free 15-minute call and send over the file, I'll tell you honestly.",
    cta_href="/figma-to-webflow.html#book",
))

POSTS.append(dict(
    slug="figma-to-webflow-cms-driven-site",
    tag="Figma",
    title="Figma to Webflow: Building a CMS-Driven Site From a Static Design | Webflow Migration Expert",
    description="A Figma file shows one example of each page type. Turning that into a real site means identifying what should be a CMS collection before development starts.",
    headline="Figma to Webflow: Building a CMS-Driven Site From a Static Design",
    read_time="4 min read",
    card_desc="A Figma file shows one example. A real site needs a plan for the rest.",
    body="""
    <p>Your Figma file almost certainly shows one blog post, one team member card, one case study, not the fifty you'll eventually have. Deciding what's structural before development starts is what makes the site scale instead of becoming unmanageable at post number six.</p>

    <h2>Spotting what should be a CMS collection</h2>
    <p>Any frame that represents a category of content rather than a single fixed page, blog posts, team members, case studies, testimonials, service listings, is a candidate for a CMS collection with its own template, not a one-off static page.</p>

    <h2>Why this has to happen before the build, not after</h2>
    <ul>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>Retrofitting a static page into a CMS collection later means rebuilding it, not adjusting it</li>
      <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>CMS structure affects how components are built in the Designer from the start, which fields are dynamic, which parts of a card template repeat</li>
    </ul>

    <h2>What this looks like during the build plan</h2>
    <p>Every Figma frame gets mapped to either a static page or a CMS collection template before any Designer work starts, so the structure is decided deliberately rather than discovered halfway through the build.</p>

    <h2>The payoff</h2>
    <p>A site where adding the fiftieth blog post or team member is a form submission, the same experience as the first one, not a design decision that has to get made all over again.</p>
""",
    cta_h3="Planning a site with blog posts, team members, or case studies?",
    cta_p="Get a free 15-minute call and we'll map the CMS structure before anything gets built.",
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


# The WordPress checklist post is hand-written outside this generator (predates
# it), so it's registered here manually purely for related-post cross-linking.
EXTRA_REGISTRY = [
    dict(slug="wordpress-to-webflow-migration-checklist", tag="WordPress",
         headline="The WordPress to Webflow Migration Checklist"),
]

def build_registry(posts):
    reg = {}
    for p in list(posts) + EXTRA_REGISTRY:
        reg.setdefault(p["tag"], []).append({"slug": p["slug"], "headline": p["headline"]})
    return reg

def related_html(tag, own_slug, registry):
    others = [e for e in registry.get(tag, []) if e["slug"] != own_slug]
    if not others:
        return ""
    items = "".join(f'<li><a href="/blog/{e["slug"]}.html">{e["headline"]}</a></li>' for e in others)
    return f'''
    <div class="related-posts">
      <h3>More on {tag} to Webflow</h3>
      <ul>{items}</ul>
    </div>
'''

REGISTRY = build_registry(POSTS)

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
        + related_html(p["tag"], p["slug"], REGISTRY) \
        + TAIL_TEMPLATE.format(cta_h3=p["cta_h3"], cta_p=p["cta_p"], cta_href=p["cta_href"])
    path = os.path.join(outdir, p["slug"] + ".html")
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path, len(html))

# print card snippets for blog/index.html
print("\n--- CARDS ---")
for p in POSTS:
    print(f'<a class="blog-card" href="/blog/{p["slug"]}.html"><span class="tag">{p["tag"]}</span><h3>{p["headline"]}</h3><p>{p["card_desc"]}</p><span class="meta">{p["read_time"]}</span></a>')
