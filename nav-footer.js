/* ============================================================
   webflowmigrationexpert.com: shared navbar + footer component
   Edit the markup below once and it updates on every page that
   loads this script.
   ============================================================ */
(function(){

  var NAV_HTML =
    '<div class="wrap">' +
      '<a class="logo" href="/"><span class="mark">W</span>Webflow<span>Migration</span>Expert</a>' +
      '<button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks">' +
        '<span></span><span></span><span></span>' +
      '</button>' +
      '<div class="nav-links" id="navLinks">' +
        '<div class="dropdown">' +
          '<button class="pill dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false">' +
            'Migrations' +
            '<span class="caret" aria-hidden="true"></span>' +
          '</button>' +
          '<div class="dropdown-menu">' +
            '<a href="/shopify-to-webflow.html">Shopify to Webflow Migration</a>' +
            '<a href="/wordpress-to-webflow.html">WordPress to Webflow Migration</a>' +
            '<a href="/wix-to-webflow.html">Wix to Webflow Migration</a>' +
            '<a href="/squarespace-to-webflow.html">Squarespace to Webflow Migration</a>' +
            '<a href="/html-to-webflow.html">HTML to Webflow Migration</a>' +
            '<a href="/figma-to-webflow.html">Figma to Webflow Migration</a>' +
          '</div>' +
        '</div>' +
        '<a class="pill" href="/#portfolio">Portfolio</a>' +
        '<a class="pill" href="/case-studies/">Case Studies</a>' +
        '<a class="pill" href="/blog/">Blog</a>' +
        '<a class="pill" href="/about.html">About</a>' +
        '<a class="nav-cta btn-primary" href="/#book">Book a free call</a>' +
      '</div>' +
    '</div>';

  var FOOTER_HTML =
    '<div class="wrap footer-grid">' +
      '<div class="footer-brand">' +
        '<a class="logo" href="/"><span class="mark">W</span>Webflow<span>Migration</span>Expert</a>' +
        '<p>Certified Webflow Expert migrations from Shopify, WordPress, Wix, Squarespace, and AI site builders, without losing your rankings or your design.</p>' +
        '<a class="footer-email" href="mailto:hello@webflowmigrationexpert.com">hello@webflowmigrationexpert.com</a>' +
      '</div>' +
      '<div class="footer-col">' +
        '<span class="footer-col-title">Migrations</span>' +
        '<a href="/shopify-to-webflow.html">Shopify to Webflow Migration</a>' +
        '<a href="/wordpress-to-webflow.html">WordPress to Webflow Migration</a>' +
        '<a href="/wix-to-webflow.html">Wix to Webflow Migration</a>' +
        '<a href="/squarespace-to-webflow.html">Squarespace to Webflow Migration</a>' +
        '<a href="/html-to-webflow.html">HTML to Webflow Migration</a>' +
        '<a href="/figma-to-webflow.html">Figma to Webflow Migration</a>' +
      '</div>' +
      '<div class="footer-col">' +
        '<span class="footer-col-title">Explore</span>' +
        '<a href="/">Home</a>' +
        '<a href="/about.html">About</a>' +
        '<a href="/#portfolio">Portfolio</a>' +
        '<a href="/case-studies/">Case Studies</a>' +
        '<a href="/blog/">Blog</a>' +
        '<a href="/#faq">FAQ</a>' +
      '</div>' +
      '<div class="footer-col">' +
        '<span class="footer-col-title">Get started</span>' +
        '<a href="/#book">Book a free call</a>' +
        '<a href="mailto:hello@webflowmigrationexpert.com">Email us</a>' +
      '</div>' +
    '</div>' +
    '<div class="wrap footer-bottom">' +
      '<p>&copy; ' + new Date().getFullYear() + ' Webflow Migration Expert. All rights reserved.</p>' +
      '<p>Not affiliated with Webflow, Inc.</p>' +
    '</div>';

  customElements.define('site-nav', class extends HTMLElement{
    connectedCallback(){ this.innerHTML = '<nav>' + NAV_HTML + '</nav>'; }
  });

  customElements.define('site-footer', class extends HTMLElement{
    connectedCallback(){ this.innerHTML = '<footer>' + FOOTER_HTML + '</footer>'; }
  });

  /* ---------- Mobile menu + dropdown ---------- */
  function closeMobileMenu(){
    var links = document.getElementById('navLinks');
    var toggle = document.querySelector('.nav-toggle');
    if(links) links.classList.remove('open');
    if(toggle) toggle.setAttribute('aria-expanded','false');
  }
  function closeAllDropdowns(){
    document.querySelectorAll('.dropdown.open').forEach(function(dd){
      dd.classList.remove('open');
      var t = dd.querySelector('.dropdown-trigger');
      if(t) t.setAttribute('aria-expanded','false');
    });
  }

  document.addEventListener('click', function(e){
    var navToggle = e.target.closest && e.target.closest('.nav-toggle');
    if(navToggle){
      var links = document.getElementById('navLinks');
      var isOpen = links.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      return;
    }

    var trigger = e.target.closest && e.target.closest('.dropdown-trigger');
    if(trigger){
      e.stopPropagation();
      var dd = trigger.closest('.dropdown');
      var isOpen = dd.classList.contains('open');
      closeAllDropdowns();
      if(!isOpen){
        dd.classList.add('open');
        trigger.setAttribute('aria-expanded','true');
      }
      return;
    }

    var clickedNavLink = e.target.closest && e.target.closest('.nav-links a');
    var clickedInsideNavLinks = e.target.closest && e.target.closest('.nav-links');
    if(clickedNavLink || !clickedInsideNavLinks){
      closeMobileMenu();
    }
    closeAllDropdowns();
  });

  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){ closeAllDropdowns(); closeMobileMenu(); }
  });

})();
