#!/usr/bin/env python3
"""
Build Eligiendo Mi Camino website v5 — SUPER MODERN.
Brand: #F57B21 naranja, #F3E0C4 beige, #26282B negro, Poppins Bold
Slogan: El momento de elegir es el momento de mostrarse
UX: scroll-triggered animations, gradient mesh, glass morphism, interactive demo mockups

v5 changes:
- Remove "Powered by Anthropic" badges (partners + footer)
- Partners: remove WB & DECRG, keep DRELM/Anthropic/uDocz/UPC, 4-col grid
- DRELM: government seal SVG icon
- UPC: university shield SVG icon
- Heading: "Socios" / "Partners" (not "in Peru")
- New DECRG Evaluation section after partners
- Career Coach: 8 steps, 12 sessions
- Math Tutor: ~4,000 questions everywhere
- Fix "tutorizamos" -> "enseñamos"
"""

import base64, os

def read_file(path):
    with open(path, 'r') as f:
        return f.read().strip()

def img_to_b64(path):
    try:
        with open(path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
        ext = path.split('.')[-1].lower()
        mime = {'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg'}.get(ext,'image/png')
        return f'data:{mime};base64,{data}'
    except:
        return None

# === Assets ===
GALLITO_IMG = read_file(r'C:\Users\cosmo\Downloads\AI Career Coach\Website\gallito_img.txt')
GALLITO_MINI = read_file(r'C:\Users\cosmo\Downloads\AI Career Coach\Website\gallito_mini.txt')
WBG_LOGO_B64 = 'data:image/png;base64,' + read_file(r'C:\Users\cosmo\Downloads\AI Career Coach\wbg-logo-b64.txt')

# Try horizontal WB logo
wb_horiz = img_to_b64(r'C:\Users\cosmo\Downloads\Director Libre\el director libre\Horizontal\color\png\WBG_S-Horizontal-RGB-web.png')
if wb_horiz:
    WBG_LOGO_B64 = wb_horiz

# Anthropic logo
ANTHROPIC_LOGO = img_to_b64(r'C:\Users\cosmo\Downloads\Eligiendo Mi Camino\06_Logos_y_Branding\page3_img1_xref185.jpeg')
if not ANTHROPIC_LOGO:
    ANTHROPIC_LOGO = ''

# uDocz/DRELM from login screenshot - use branding folder image
UDOCZ_DRELM_IMG = img_to_b64(r'C:\Users\cosmo\Downloads\Eligiendo Mi Camino\06_Logos_y_Branding\WhatsApp Image 2026-02-14 at 3.06.34 PM.jpeg')

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Eligiendo Mi Camino | World Bank</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script>
tailwind.config = {{
  theme: {{
    extend: {{
      colors: {{
        brand: {{ 50:'#FFF8F0',100:'#FEECD4',200:'#FDD5A8',300:'#FCB66F',400:'#F57B21',500:'#E06A10',600:'#B85510',700:'#8F4210' }},
        beige: {{ 50:'#FFFCF7',100:'#F3E0C4',200:'#E8D0A8',300:'#D4B88A' }},
        dark: {{ 50:'#E8E8E9',100:'#B9BABF',200:'#8A8C94',300:'#5C5E66',400:'#3A3C42',500:'#26282B',600:'#1E2023',700:'#16171A',800:'#0D0E10' }},
        wb: {{ blue:'#003366', light:'#0072BC' }}
      }},
      fontFamily: {{
        display: ['Poppins', 'system-ui', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif']
      }}
    }}
  }}
}}
</script>
<style>
*{{ box-sizing:border-box; }}
html {{ scroll-behavior: smooth; }}
body {{ font-family: 'Inter', system-ui, sans-serif; overflow-x:hidden; }}
h1,h2,h3,h4,h5,.font-display {{ font-family: 'Poppins', system-ui, sans-serif; }}

/* === GRADIENT MESH === */
.mesh-hero {{
  background:
    radial-gradient(ellipse 80% 60% at 70% 20%, rgba(245,123,33,0.12) 0%, transparent 60%),
    radial-gradient(ellipse 60% 80% at 20% 80%, rgba(243,224,196,0.15) 0%, transparent 60%),
    radial-gradient(ellipse 50% 50% at 50% 50%, rgba(245,123,33,0.04) 0%, transparent 80%),
    linear-gradient(180deg, #0D0E10 0%, #16171A 40%, #1E2023 70%, #26282B 100%);
}}
.mesh-dark {{
  background:
    radial-gradient(ellipse 70% 50% at 80% 30%, rgba(245,123,33,0.08) 0%, transparent 60%),
    linear-gradient(180deg, #16171A 0%, #1E2023 50%, #26282B 100%);
}}

/* === GLASS === */
.glass {{ background: rgba(255,255,255,0.04); backdrop-filter: blur(20px) saturate(1.2); border: 1px solid rgba(255,255,255,0.07); }}
.glass-white {{ background: rgba(255,255,255,0.85); backdrop-filter: blur(20px); border: 1px solid rgba(0,0,0,0.06); }}
.glass-brand {{ background: rgba(245,123,33,0.06); backdrop-filter: blur(12px); border: 1px solid rgba(245,123,33,0.12); }}

/* === ANIMATIONS === */
@keyframes float {{ 0%,100%{{ transform:translateY(0) rotate(0deg); }} 50%{{ transform:translateY(-12px) rotate(1deg); }} }}
@keyframes pulse-glow {{ 0%,100%{{ opacity:0.4; transform:scale(1); }} 50%{{ opacity:0.7; transform:scale(1.05); }} }}
@keyframes gradient-x {{ 0%{{ background-position:0% 50%; }} 50%{{ background-position:100% 50%; }} 100%{{ background-position:0% 50%; }} }}
@keyframes slide-up {{ from {{ opacity:0; transform:translateY(40px); }} to {{ opacity:1; transform:translateY(0); }} }}
@keyframes slide-in-left {{ from {{ opacity:0; transform:translateX(-30px); }} to {{ opacity:1; transform:translateX(0); }} }}
@keyframes slide-in-right {{ from {{ opacity:0; transform:translateX(30px); }} to {{ opacity:1; transform:translateX(0); }} }}
@keyframes count-up {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}
@keyframes shimmer {{ 0%{{ background-position:-200% 0; }} 100%{{ background-position:200% 0; }} }}

.float-anim {{ animation: float 5s ease-in-out infinite; }}
.pulse-glow {{ animation: pulse-glow 4s ease-in-out infinite; }}
.gradient-text {{ background: linear-gradient(135deg, #F57B21, #FCB66F, #F57B21); background-size: 200% auto; animation: gradient-x 4s ease infinite; -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.shimmer {{ background: linear-gradient(90deg, transparent, rgba(245,123,33,0.1), transparent); background-size: 200% 100%; animation: shimmer 3s infinite; }}

/* Scroll reveal */
.reveal {{ opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); }}
.reveal.visible {{ opacity: 1; transform: translateY(0); }}
.reveal-left {{ opacity: 0; transform: translateX(-30px); transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); }}
.reveal-left.visible {{ opacity: 1; transform: translateX(0); }}
.reveal-right {{ opacity: 0; transform: translateX(30px); transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); }}
.reveal-right.visible {{ opacity: 1; transform: translateX(0); }}
.stagger-1 {{ transition-delay: 0.1s; }}
.stagger-2 {{ transition-delay: 0.2s; }}
.stagger-3 {{ transition-delay: 0.3s; }}
.stagger-4 {{ transition-delay: 0.4s; }}
.stagger-5 {{ transition-delay: 0.5s; }}
.stagger-6 {{ transition-delay: 0.6s; }}
.stagger-7 {{ transition-delay: 0.7s; }}
.stagger-8 {{ transition-delay: 0.8s; }}

/* Card hover */
.card-modern {{ transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); }}
.card-modern:hover {{ transform: translateY(-8px); box-shadow: 0 30px 60px -12px rgba(245,123,33,0.15), 0 18px 36px -18px rgba(0,0,0,0.2); }}

/* Stripe */
.stripe {{ height: 3px; background: linear-gradient(90deg, #F57B21 0%, #F57B21 50%, #003366 50%, #003366 100%); }}
.stripe-thin {{ height: 2px; background: linear-gradient(90deg, transparent, #F57B21, transparent); }}

/* Lang toggle */
[data-lang="en"] {{ display: none; }}
html[lang="en"] [data-lang="en"] {{ display: block; }}
html[lang="en"] [data-lang="es"] {{ display: none; }}
html[lang="en"] [data-lang-i="en"] {{ display: inline; }}
html[lang="en"] [data-lang-i="es"] {{ display: none; }}
html[lang="es"] [data-lang-i="en"] {{ display: none; }}
html[lang="es"] [data-lang-i="es"] {{ display: inline; }}

/* Nav states */
.nav-top a, .nav-top span {{ color: #26282B !important; }}
.nav-top .lang-btn {{ color: #26282B !important; border-color: rgba(38,40,43,0.2) !important; }}
.nav-top .nav-brand {{ color: #26282B !important; }}
.nav-scrolled a, .nav-scrolled span {{ color: rgba(255,255,255,0.5) !important; }}
.nav-scrolled .lang-btn {{ color: rgba(255,255,255,0.5) !important; border-color: rgba(255,255,255,0.2) !important; }}
.nav-scrolled .nav-brand {{ color: rgba(255,255,255,0.9) !important; }}
.nav-scrolled a:hover {{ color: #F57B21 !important; }}
.nav-top a:hover {{ color: #F57B21 !important; }}
.nav-top .nav-toolkit, .nav-scrolled .nav-toolkit {{ color: white !important; }}

/* Scrollbar */
::-webkit-scrollbar {{ width:5px; }}
::-webkit-scrollbar-track {{ background:#16171A; }}
::-webkit-scrollbar-thumb {{ background:#F57B21; border-radius:10px; }}

/* Phone mockup */
.phone-frame {{
  width: 260px; height: 520px;
  border: 3px solid rgba(255,255,255,0.15);
  border-radius: 36px;
  overflow: hidden;
  position: relative;
  background: #1a1a1a;
  box-shadow: 0 40px 80px -20px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.05);
}}
.phone-notch {{
  position: absolute; top: 0; left: 50%; transform: translateX(-50%);
  width: 100px; height: 24px; background: #1a1a1a; border-radius: 0 0 16px 16px; z-index: 10;
}}
.phone-content {{
  width: 100%; height: 100%; overflow: hidden;
}}
.phone-content img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; }}

/* Stat counter */
.stat-number {{ font-variant-numeric: tabular-nums; }}

/* Nav active */
nav a.active {{ color: #F57B21; }}

/* Tooltip */
.tooltip {{ position: relative; }}
.tooltip::after {{
  content: attr(data-tip); position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%);
  padding: 4px 10px; background: #26282B; color: #F3E0C4; font-size: 10px; border-radius: 6px;
  white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity 0.2s;
}}
.tooltip:hover::after {{ opacity: 1; }}

/* Demo browser frame */
.browser-frame {{
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 40px 80px -20px rgba(0,0,0,0.4);
}}
.browser-bar {{
  background: rgba(30,32,35,0.95);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.browser-dot {{ width: 10px; height: 10px; border-radius: 50%; }}

/* === MOBILE RESPONSIVE === */
@media (max-width: 640px) {{
  /* Hero title scaling */
  .hero-title {{ font-size: 2.8rem !important; }}
  /* Stats row: wrap and center */
  .stats-row {{ flex-wrap: wrap; justify-content: center; gap: 1rem !important; }}
  .stats-row > div {{ text-align: center; }}
  .stat-number {{ font-size: 1.5rem !important; }}
  /* Feature grids */
  .feature-grid-3 {{ grid-template-columns: 1fr !important; }}
  .feature-grid-2 {{ grid-template-columns: 1fr !important; }}
  /* Career coach steps grid */
  .steps-grid {{ grid-template-columns: repeat(2, 1fr) !important; }}
  /* General padding adjustments */
  section {{ padding-top: 3rem; padding-bottom: 3rem; }}
  .section-title {{ font-size: 1.75rem !important; }}
  /* Toolkit content grid */
  .toolkit-grid {{ grid-template-columns: 1fr !important; }}
  /* Phone frame */
  .phone-frame {{ width: 200px; height: 400px; }}
  /* Fix overflow */
  .overflow-fix {{ overflow-x: hidden; }}
}}

@media (max-width: 480px) {{
  .hero-title {{ font-size: 2.2rem !important; }}
  .stats-row {{ gap: 0.5rem !important; }}
  .stat-number {{ font-size: 1.25rem !important; }}
}}

</style>
</head>
<body class="bg-dark-800 text-white overflow-x-hidden">

<script>
// Language toggle
function toggleLang() {{
  const h = document.documentElement;
  const n = h.lang === 'es' ? 'en' : 'es';
  h.lang = n;
  document.querySelectorAll('.lang-btn').forEach(b => b.textContent = n === 'es' ? 'EN' : 'ES');
}}
// Toolkit code
function checkCode() {{
  const v = document.getElementById('codeInput').value.trim();
  if (v === 'WB-TTL-2026') {{
    document.getElementById('tkLock').style.display = 'none';
    document.getElementById('tkContent').classList.remove('hidden');
    document.getElementById('tkContent').classList.add('block');
    document.getElementById('codeErr').style.display = 'none';
  }} else {{
    document.getElementById('codeErr').style.display = 'block';
  }}
}}
// Scroll reveal
const observer = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{ e.target.classList.add('visible'); }}
  }});
}}, {{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }});
document.addEventListener('DOMContentLoaded', () => {{
  document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => observer.observe(el));
}});
// Navbar scroll
window.addEventListener('scroll', () => {{
  const nav = document.getElementById('mainNav');
  if (window.scrollY > 50) {{
    nav.classList.add('bg-dark-800/95','shadow-lg','shadow-black/20','nav-scrolled');
    nav.classList.remove('bg-white/95','shadow-md','shadow-black/5','nav-top');
  }} else {{
    nav.classList.remove('bg-dark-800/95','shadow-lg','shadow-black/20','nav-scrolled');
    nav.classList.add('bg-white/95','shadow-md','shadow-black/5','nav-top');
  }}
}});
// Mobile menu
function toggleMob() {{ document.getElementById('mob').classList.toggle('hidden'); }}
</script>

<!-- ════════════ NAV ════════════ -->
<nav id="mainNav" class="fixed top-0 w-full z-50 bg-white/95 shadow-md shadow-black/5 nav-top backdrop-blur-xl transition-all duration-500">
<div class="stripe"></div>
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex justify-between items-center h-16">
    <div class="flex items-center gap-3">
      <img src="{WBG_LOGO_B64}" alt="World Bank Group" class="h-7 w-auto">
      <div class="w-px h-6 bg-dark-100"></div>
      <img src="{GALLITO_MINI}" alt="Gallito" class="h-7 w-auto">
      <span class="nav-brand hidden sm:inline font-display font-bold text-sm tracking-tight">Eligiendo Mi Camino</span>
    </div>
    <div class="hidden md:flex items-center gap-6 text-[11px] font-semibold uppercase tracking-[0.15em]">
      <a href="#about" class="hover:text-brand-400 transition-colors duration-300"><span data-lang-i="es">Programa</span><span data-lang-i="en">Program</span></a>
      <a href="#math" class="hover:text-brand-400 transition-colors duration-300"><span data-lang-i="es">Tutor Matem&aacute;tica</span><span data-lang-i="en">Math Tutor</span></a>
      <a href="#coach" class="hover:text-brand-400 transition-colors duration-300"><span data-lang-i="es">Coach</span><span data-lang-i="en">Coach</span></a>
      <a href="#partners" class="hover:text-brand-400 transition-colors duration-300"><span data-lang-i="es">Socios</span><span data-lang-i="en">Partners</span></a>
      <a href="#toolkit" class="nav-toolkit px-4 py-1.5 bg-brand-400 text-white rounded-full hover:bg-brand-500 transition-all duration-300 normal-case tracking-normal text-xs font-bold">Toolkit</a>
      <button onclick="toggleLang()" class="lang-btn w-8 h-8 border rounded-full text-[10px] font-bold hover:border-brand-400 hover:text-brand-400 transition-all duration-300">EN</button>
    </div>
    <button onclick="toggleMob()" class="md:hidden p-2 text-dark-400"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg></button>
  </div>
</div>
<div id="mob" class="hidden md:hidden bg-dark-700/95 backdrop-blur-xl border-t border-white/5 px-6 py-4 space-y-3">
  <a href="#about" class="block py-2 text-sm font-semibold text-white/70" onclick="toggleMob()"><span data-lang-i="es">Programa</span><span data-lang-i="en">Program</span></a>
  <a href="#math" class="block py-2 text-sm font-semibold text-white/70" onclick="toggleMob()"><span data-lang-i="es">Tutor Matem&aacute;tica</span><span data-lang-i="en">Math Tutor</span></a>
  <a href="#coach" class="block py-2 text-sm font-semibold text-white/70" onclick="toggleMob()"><span data-lang-i="es">Coach Vocacional</span><span data-lang-i="en">Career Coach</span></a>
  <a href="#toolkit" class="block py-2 text-sm font-bold text-brand-400" onclick="toggleMob()">Toolkit</a>
  <button onclick="toggleLang()" class="lang-btn px-3 py-1 border border-white/20 rounded-full text-xs font-bold text-white/50">EN</button>
</div>
</nav>

<!-- ════════════ HERO ════════════ -->
<section class="bg-white min-h-screen flex items-center relative overflow-hidden">
  <!-- Decorative elements -->
  <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-50 rounded-full -translate-y-1/4 translate-x-1/4 opacity-60"></div>
  <div class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-beige-100/30 rounded-full translate-y-1/4 -translate-x-1/4"></div>
  <div class="absolute top-1/3 left-[15%] w-2 h-2 bg-brand-400 rounded-full pulse-glow"></div>
  <div class="absolute top-2/3 right-[20%] w-1.5 h-1.5 bg-brand-200 rounded-full pulse-glow" style="animation-delay:2s"></div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-16 relative z-10 w-full">
    <div class="grid lg:grid-cols-12 gap-10 items-center">

      <!-- Left: text -->
      <div class="lg:col-span-7">
        <div class="inline-flex items-center gap-2.5 bg-dark-500 rounded-full px-5 py-2.5 mb-10" style="animation: slide-up 0.6s ease-out both;">
          <img src="{WBG_LOGO_B64}" alt="WB" class="h-4 w-auto brightness-0 invert opacity-60">
          <div class="w-px h-3 bg-white/10"></div>
          <span class="text-[11px] font-medium text-white/60 tracking-wide">WBG Innovation Award &mdash; "From Learning to Earning"</span>
        </div>

        <div data-lang="es">
          <p class="text-brand-400 font-display font-bold text-xs uppercase tracking-[0.3em] mb-4" style="animation: slide-up 0.6s ease-out 0.1s both;">Programa Educativo &bull; Lima, Peru</p>
          <h1 class="font-display font-black leading-[0.9] mb-6" style="animation: slide-up 0.7s ease-out 0.15s both;">
            <span class="hero-title text-5xl sm:text-6xl lg:text-[5.5rem] text-dark-500">Eligiendo</span><br>
            <span class="hero-title text-5xl sm:text-6xl lg:text-[5.5rem] gradient-text">Mi Camino</span>
          </h1>
          <p class="font-display text-base sm:text-xl font-semibold italic text-dark-200 mb-6 max-w-lg" style="animation: slide-up 0.7s ease-out 0.2s both;">
            &ldquo;El momento de elegir<br>es el momento de mostrarse&rdquo;
          </p>
          <p class="text-dark-200 text-sm sm:text-[15px] leading-relaxed mb-10 max-w-lg" style="animation: slide-up 0.7s ease-out 0.25s both;">Dos herramientas de IA para estudiantes de 5to de secundaria en 100 colegios p&uacute;blicos de Lima: un <strong class="text-dark-500">Tutor de Matem&aacute;ticas</strong> que diagnostica y ense&ntilde;a, y un <strong class="text-dark-500">Coach Vocacional</strong> que gu&iacute;a decisiones de carrera con datos reales del mercado laboral peruano.</p>
        </div>
        <div data-lang="en">
          <p class="text-brand-400 font-display font-bold text-xs uppercase tracking-[0.3em] mb-4">Education Program &bull; Lima, Peru</p>
          <h1 class="font-display font-black leading-[0.9] mb-6">
            <span class="hero-title text-5xl sm:text-6xl lg:text-[5.5rem] text-dark-500">Choosing</span><br>
            <span class="hero-title text-5xl sm:text-6xl lg:text-[5.5rem] gradient-text">My Path</span>
          </h1>
          <p class="font-display text-lg sm:text-xl font-semibold italic text-dark-200 mb-6 max-w-lg">
            &ldquo;The moment to choose<br>is the moment to show yourself&rdquo;
          </p>
          <p class="text-dark-200 text-[15px] leading-relaxed mb-10 max-w-lg">Two AI-powered tools for 5th-year secondary students across 100 public schools in Lima: an <strong class="text-dark-500">AI Math Tutor</strong> that diagnoses and teaches, and an <strong class="text-dark-500">AI Career Coach</strong> that guides career decisions with real labor market data.</p>
        </div>

        <div class="flex flex-col sm:flex-row flex-wrap gap-3 sm:gap-4 mb-12" style="animation: slide-up 0.7s ease-out 0.3s both;">
          <a href="#about" class="group relative px-6 sm:px-8 py-3.5 sm:py-4 bg-brand-400 text-white rounded-2xl font-display font-bold text-sm overflow-hidden transition-all duration-300 hover:shadow-[0_20px_40px_-12px_rgba(245,123,33,0.4)] hover:scale-[1.02] text-center">
            <span class="relative z-10"><span data-lang-i="es">Conocer el programa</span><span data-lang-i="en">Learn more</span></span>
          </a>
          <a href="#toolkit" class="px-6 sm:px-8 py-3.5 sm:py-4 bg-dark-500 text-white/80 rounded-2xl font-display font-bold text-sm transition-all duration-300 hover:bg-dark-400 text-center">
            <span data-lang-i="es">Toolkit para replicar</span><span data-lang-i="en">Replication toolkit</span>
          </a>
        </div>

        <!-- Stats row -->
        <div class="stats-row flex flex-wrap gap-4 sm:gap-10" style="animation: slide-up 0.7s ease-out 0.35s both;">
          <div><div class="text-2xl sm:text-4xl font-display font-black gradient-text stat-number">100</div><div class="text-[10px] text-dark-200 mt-1 uppercase tracking-wider"><span data-lang-i="es">colegios</span><span data-lang-i="en">schools</span></div></div>
          <div class="w-px bg-dark-50 hidden sm:block"></div>
          <div><div class="text-2xl sm:text-4xl font-display font-black gradient-text stat-number">6,300</div><div class="text-[10px] text-dark-200 mt-1 uppercase tracking-wider"><span data-lang-i="es">estudiantes</span><span data-lang-i="en">students</span></div></div>
          <div class="w-px bg-dark-50 hidden sm:block"></div>
          <div><div class="text-2xl sm:text-4xl font-display font-black gradient-text stat-number">400</div><div class="text-[10px] text-dark-200 mt-1 uppercase tracking-wider"><span data-lang-i="es">docentes</span><span data-lang-i="en">teachers</span></div></div>
          <div class="w-px bg-dark-50 hidden sm:block"></div>
          <div><div class="text-2xl sm:text-4xl font-display font-black text-dark-500 stat-number">RCT</div><div class="text-[10px] text-dark-200 mt-1 uppercase tracking-wider"><span data-lang-i="es">evaluaci&oacute;n</span><span data-lang-i="en">evaluation</span></div></div>
        </div>
      </div>

      <!-- Right: Gallito -->
      <div class="lg:col-span-5 flex flex-col items-center" style="animation: slide-in-right 0.8s ease-out 0.3s both;">
        <div class="relative">
          <div class="absolute -inset-16 bg-brand-400/8 rounded-full blur-[80px]"></div>
          <video src="gallito_video.mp4" autoplay loop muted playsinline class="relative z-10 h-56 sm:h-64 lg:h-80 w-auto" style="mix-blend-mode: multiply;" poster="{GALLITO_IMG}"></video>
        </div>
        <div class="relative z-10 mt-8 bg-beige-50 border border-beige-100 rounded-3xl p-5 max-w-[300px] text-center">
          <div data-lang="es">
            <p class="font-display font-bold gradient-text text-sm">Gallito de las Rocas</p>
            <p class="text-dark-200 text-[11px] leading-relaxed mt-2">Ave emblem&aacute;tica peruana que simboliza el momento decisivo en que el estudiante est&aacute; listo para <strong class="text-dark-500">mostrarse tal como es frente al mundo</strong> y tomar una decisi&oacute;n sobre su futuro.</p>
          </div>
          <div data-lang="en">
            <p class="font-display font-bold gradient-text text-sm">Andean Cock-of-the-Rock</p>
            <p class="text-dark-200 text-[11px] leading-relaxed mt-2">Peru's iconic national bird, symbolizing the decisive moment when a student is ready to <strong class="text-dark-500">show the world who they truly are</strong> and make a decision about their future.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Scroll indicator -->
  <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 text-dark-200">
    <span class="text-[9px] uppercase tracking-[0.3em]">Scroll</span>
    <div class="w-5 h-8 border border-dark-100 rounded-full flex justify-center pt-1.5"><div class="w-1 h-2 bg-brand-400 rounded-full animate-bounce"></div></div>
  </div>
</section>

<!-- ════════════ ABOUT ════════════ -->
<section id="about" class="py-24 bg-white relative overflow-hidden">
<div class="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-50 rounded-full -translate-y-1/2 translate-x-1/2 opacity-50"></div>
<div class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-beige-100/30 rounded-full translate-y-1/2 -translate-x-1/2"></div>
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
  <div data-lang="es">
    <div class="text-center mb-20 reveal">
      <div class="inline-flex items-center gap-2 bg-brand-50 px-4 py-1.5 rounded-full text-[10px] font-bold text-brand-500 uppercase tracking-[0.2em] mb-4">
        <i class="fas fa-globe-americas text-brand-400"></i> Banco Mundial &mdash; LAC Education
      </div>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-black text-dark-500">El Programa</h2>
    </div>
    <div class="grid lg:grid-cols-2 gap-16 mb-20">
      <div class="reveal-left">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 bg-red-50 rounded-2xl flex items-center justify-center"><i class="fas fa-exclamation-triangle text-red-400"></i></div>
          <h3 class="font-display text-2xl font-black text-dark-500">El Problema</h3>
        </div>
        <p class="text-dark-200 text-[15px] leading-[1.8] mb-5">En Am&eacute;rica Latina, el 56% de los ni&ntilde;os no puede leer un texto simple a los 10 a&ntilde;os. En Per&uacute;, el <strong class="text-dark-500">70% de los estudiantes que terminan secundaria no acceden a educaci&oacute;n superior</strong>, y la mayor&iacute;a termina en empleo informal.</p>
        <p class="text-dark-200 text-[15px] leading-[1.8]">La tutor&iacute;a individual y la orientaci&oacute;n vocacional funcionan, pero son demasiado costosas para escalar. <strong class="text-dark-500">La IA puede cambiar esto</strong> &mdash; pero solo si se dise&ntilde;a correctamente.</p>
      </div>
      <div class="reveal-right">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 bg-green-50 rounded-2xl flex items-center justify-center"><i class="fas fa-check-circle text-green-500"></i></div>
          <h3 class="font-display text-2xl font-black text-dark-500">La Soluci&oacute;n</h3>
        </div>
        <p class="text-dark-200 text-[15px] leading-[1.8] mb-6">Dos herramientas de IA que operan en paralelo durante el semestre escolar en 100 colegios p&uacute;blicos de Lima, lanz&aacute;ndose el <strong class="text-dark-500">16 de marzo de 2026</strong>.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <a href="#math" class="group p-5 bg-dark-500 rounded-2xl text-white card-modern block">
            <p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-wider mb-1.5">Componente 1</p>
            <p class="font-display font-bold text-sm mb-1">Tutor de Matem&aacute;ticas</p>
            <p class="text-white/40 text-[10px]">~4,000 preguntas diagn&oacute;sticas</p>
            <i class="fas fa-arrow-right text-brand-400 text-xs mt-3 block group-hover:translate-x-1 transition-transform"></i>
          </a>
          <a href="#coach" class="group p-5 bg-gradient-to-br from-brand-400 to-brand-500 rounded-2xl text-white card-modern block">
            <p class="text-white/70 font-display font-bold text-[10px] uppercase tracking-wider mb-1.5">Componente 2</p>
            <p class="font-display font-bold text-sm mb-1">Coach Vocacional</p>
            <p class="text-white/60 text-[10px]">142 ocupaciones, 12 sectores</p>
            <i class="fas fa-arrow-right text-white/80 text-xs mt-3 block group-hover:translate-x-1 transition-transform"></i>
          </a>
        </div>
      </div>
    </div>
    <!-- Quote -->
    <div class="reveal max-w-3xl mx-auto">
      <div class="relative bg-beige-50 rounded-3xl p-8 border border-beige-100">
        <div class="absolute -top-4 left-8 w-8 h-8 bg-brand-400 rounded-xl flex items-center justify-center text-white text-sm">&ldquo;</div>
        <p class="text-dark-300 text-[15px] italic leading-relaxed pl-4">La pregunta no es si la tutor&iacute;a con IA funciona en teor&iacute;a. Es si funciona dentro de las restricciones reales: horario regular de matem&aacute;ticas, laboratorios de c&oacute;mputo existentes, docentes regulares, sin presupuesto adicional. <strong class="text-dark-500">Si funciona aqu&iacute;, el camino a escala nacional es claro.</strong></p>
      </div>
    </div>
  </div>
  <div data-lang="en">
    <div class="text-center mb-20 reveal">
      <div class="inline-flex items-center gap-2 bg-brand-50 px-4 py-1.5 rounded-full text-[10px] font-bold text-brand-500 uppercase tracking-[0.2em] mb-4">
        <i class="fas fa-globe-americas text-brand-400"></i> World Bank &mdash; LAC Education
      </div>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-black text-dark-500">The Program</h2>
    </div>
    <div class="grid lg:grid-cols-2 gap-16 mb-20">
      <div class="reveal-left">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 bg-red-50 rounded-2xl flex items-center justify-center"><i class="fas fa-exclamation-triangle text-red-400"></i></div>
          <h3 class="font-display text-2xl font-black text-dark-500">The Problem</h3>
        </div>
        <p class="text-dark-200 text-[15px] leading-[1.8] mb-5">Across Latin America, 56% of children cannot read a simple text by age 10. In Peru, <strong class="text-dark-500">70% of students finishing secondary school do not access higher education</strong>, and most end up in informal employment.</p>
        <p class="text-dark-200 text-[15px] leading-[1.8]">One-on-one tutoring and career guidance work, but they're too expensive to scale. <strong class="text-dark-500">AI can change this</strong> &mdash; but only if designed right.</p>
      </div>
      <div class="reveal-right">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 bg-green-50 rounded-2xl flex items-center justify-center"><i class="fas fa-check-circle text-green-500"></i></div>
          <h3 class="font-display text-2xl font-black text-dark-500">The Solution</h3>
        </div>
        <p class="text-dark-200 text-[15px] leading-[1.8] mb-6">Two AI tools operating in parallel throughout the school semester across 100 public schools in Lima, launching <strong class="text-dark-500">March 16, 2026</strong>.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <a href="#math" class="group p-5 bg-dark-500 rounded-2xl text-white card-modern block"><p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-wider mb-1.5">Component 1</p><p class="font-display font-bold text-sm mb-1">AI Math Tutor</p><p class="text-white/40 text-[10px]">~4,000 diagnostic questions</p><i class="fas fa-arrow-right text-brand-400 text-xs mt-3 block group-hover:translate-x-1 transition-transform"></i></a>
          <a href="#coach" class="group p-5 bg-gradient-to-br from-brand-400 to-brand-500 rounded-2xl text-white card-modern block"><p class="text-white/70 font-display font-bold text-[10px] uppercase tracking-wider mb-1.5">Component 2</p><p class="font-display font-bold text-sm mb-1">AI Career Coach</p><p class="text-white/60 text-[10px]">142 occupations, 12 sectors</p><i class="fas fa-arrow-right text-white/80 text-xs mt-3 block group-hover:translate-x-1 transition-transform"></i></a>
        </div>
      </div>
    </div>
    <div class="reveal max-w-3xl mx-auto">
      <div class="relative bg-beige-50 rounded-3xl p-8 border border-beige-100">
        <div class="absolute -top-4 left-8 w-8 h-8 bg-brand-400 rounded-xl flex items-center justify-center text-white text-sm">&ldquo;</div>
        <p class="text-dark-300 text-[15px] italic leading-relaxed pl-4">The question is not whether AI tutoring works in theory. It is whether it works within real constraints: regular math hours, existing computer labs, normal teachers, no additional budget. <strong class="text-dark-500">If it works here, the path to national scale is clear.</strong></p>
      </div>
    </div>
  </div>
</div>
</section>

<!-- ════════════ MATH TUTOR ════════════ -->
<section id="math" class="py-24 mesh-dark text-white relative overflow-hidden">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
  <div class="grid lg:grid-cols-2 gap-16 items-center">
    <!-- Left: content -->
    <div>
      <div data-lang="es">
        <div class="reveal flex items-center gap-3 mb-3">
          <div class="w-14 h-14 bg-gradient-to-br from-brand-400 to-brand-600 rounded-2xl flex items-center justify-center shadow-lg shadow-brand-400/20"><i class="fas fa-square-root-alt text-white text-xl"></i></div>
          <div><p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-[0.25em]">Componente 1</p><h2 class="font-display text-3xl sm:text-4xl font-black">Tutor de Matem&aacute;ticas</h2></div>
        </div>
        <p class="reveal text-white/40 text-[15px] max-w-lg mb-10 mt-4 leading-relaxed">La mayor&iacute;a de chatbots dan respuestas en vez de ayudar a pensar. Nosotros <strong class="text-white/70">diagnosticamos primero, luego ense&ntilde;amos</strong>.</p>
        <div class="space-y-4 mb-10">
          <div class="reveal stagger-1 glass rounded-2xl p-5 card-modern flex gap-4 items-start">
            <div class="w-11 h-11 shrink-0 bg-red-500/15 rounded-xl flex items-center justify-center"><i class="fas fa-crosshairs text-red-400"></i></div>
            <div><h4 class="font-display font-bold text-sm mb-1">Diagn&oacute;stico Preciso</h4><p class="text-white/35 text-xs leading-relaxed">~4,000 preguntas del curr&iacute;culo peruano de 5to. Identifica el error conceptual espec&iacute;fico. 4 competencias, 16 temas, 80 subtemas.</p></div>
          </div>
          <div class="reveal stagger-2 glass rounded-2xl p-5 card-modern flex gap-4 items-start">
            <div class="w-11 h-11 shrink-0 bg-blue-500/15 rounded-xl flex items-center justify-center"><i class="fas fa-robot text-blue-400"></i></div>
            <div><h4 class="font-display font-bold text-sm mb-1">Tutor&iacute;a Personalizada</h4><p class="text-white/35 text-xs leading-relaxed">Sesiones socr&aacute;ticas adaptadas al error espec&iacute;fico. Modo escuela (guiado) y modo casa (exploraci&oacute;n libre).</p></div>
          </div>
          <div class="reveal stagger-3 glass rounded-2xl p-5 card-modern flex gap-4 items-start">
            <div class="w-11 h-11 shrink-0 bg-green-500/15 rounded-xl flex items-center justify-center"><i class="fas fa-brain text-green-400"></i></div>
            <div><h4 class="font-display font-bold text-sm mb-1">3 Innovaciones Pedag&oacute;gicas</h4><p class="text-white/35 text-xs leading-relaxed">Pr&aacute;ctica de recuperaci&oacute;n, reflexi&oacute;n sobre errores propios, detecci&oacute;n de errores en otros.</p></div>
          </div>
        </div>
        <div class="reveal glass rounded-2xl p-4 inline-flex flex-wrap items-center gap-3 text-xs">
          <span class="text-brand-400 font-display font-bold">2 horas por semana</span>
          <div class="w-1 h-1 bg-white/15 rounded-full"></div>
          <span class="text-white/30">Integrado en hora de matem&aacute;ticas</span>
          <div class="w-1 h-1 bg-white/15 rounded-full"></div>
          <span class="text-white/30">Dashboard docente</span>
        </div>
      </div>
      <div data-lang="en">
        <div class="reveal flex items-center gap-3 mb-3">
          <div class="w-14 h-14 bg-gradient-to-br from-brand-400 to-brand-600 rounded-2xl flex items-center justify-center shadow-lg shadow-brand-400/20"><i class="fas fa-square-root-alt text-white text-xl"></i></div>
          <div><p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-[0.25em]">Component 1</p><h2 class="font-display text-3xl sm:text-4xl font-black">AI Math Tutor</h2></div>
        </div>
        <p class="reveal text-white/40 text-[15px] max-w-lg mb-10 mt-4 leading-relaxed">Most chatbots give answers instead of helping students think. We <strong class="text-white/70">diagnose first, then tutor</strong>.</p>
        <div class="space-y-4 mb-10">
          <div class="reveal stagger-1 glass rounded-2xl p-5 card-modern flex gap-4 items-start"><div class="w-11 h-11 shrink-0 bg-red-500/15 rounded-xl flex items-center justify-center"><i class="fas fa-crosshairs text-red-400"></i></div><div><h4 class="font-display font-bold text-sm mb-1">Precise Diagnosis</h4><p class="text-white/35 text-xs leading-relaxed">~4,000 questions from Peru's 5th-year curriculum. Identifies each student's specific conceptual error. 4 competencies, 16 topics, 80 subtopics.</p></div></div>
          <div class="reveal stagger-2 glass rounded-2xl p-5 card-modern flex gap-4 items-start"><div class="w-11 h-11 shrink-0 bg-blue-500/15 rounded-xl flex items-center justify-center"><i class="fas fa-robot text-blue-400"></i></div><div><h4 class="font-display font-bold text-sm mb-1">Personalized Tutoring</h4><p class="text-white/35 text-xs leading-relaxed">Socratic sessions adapted to the specific error. School mode (teacher-guided) and home mode (free exploration).</p></div></div>
          <div class="reveal stagger-3 glass rounded-2xl p-5 card-modern flex gap-4 items-start"><div class="w-11 h-11 shrink-0 bg-green-500/15 rounded-xl flex items-center justify-center"><i class="fas fa-brain text-green-400"></i></div><div><h4 class="font-display font-bold text-sm mb-1">3 Pedagogical Innovations</h4><p class="text-white/35 text-xs leading-relaxed">Retrieval practice, error reflection, and error detection in others &mdash; based on learning science.</p></div></div>
        </div>
        <div class="reveal glass rounded-2xl p-4 inline-flex flex-wrap items-center gap-3 text-xs"><span class="text-brand-400 font-display font-bold">2 hours per week</span><div class="w-1 h-1 bg-white/15 rounded-full"></div><span class="text-white/30">Integrated into regular math hours</span><div class="w-1 h-1 bg-white/15 rounded-full"></div><span class="text-white/30">Real-time teacher dashboard</span></div>
      </div>
    </div>

    <!-- Right: Demo mockup -->
    <div class="reveal-right hidden lg:block">
      <div class="browser-frame">
        <div class="browser-bar">
          <div class="browser-dot bg-red-400"></div>
          <div class="browser-dot bg-yellow-400"></div>
          <div class="browser-dot bg-green-400"></div>
          <div class="flex-1 ml-3 bg-white/5 rounded-md px-3 py-1 text-[10px] text-white/30 font-mono">test.schools.udocz.com</div>
        </div>
        <div class="bg-[#4F7BF7] p-8 min-h-[380px] flex flex-col items-center justify-center text-center">
          <div class="bg-white rounded-2xl p-8 max-w-[280px] shadow-2xl">
            <div class="flex items-center justify-center gap-3 mb-4">
              <span class="font-display font-bold text-[#4F7BF7] text-lg italic">uDocz</span>
              <span class="text-dark-200">|</span>
              <span class="font-display font-black text-dark-500 text-lg">DRELM</span>
            </div>
            <p class="text-dark-300 font-display font-semibold text-sm mb-4">Bienvenido</p>
            <div class="flex gap-0 mb-5 bg-gray-100 rounded-lg p-0.5">
              <div class="flex-1 bg-[#4F7BF7] text-white rounded-md py-1.5 text-xs font-semibold">Soy estudiante</div>
              <div class="flex-1 text-dark-300 py-1.5 text-xs font-semibold">Soy profesor</div>
            </div>
            <div class="space-y-2.5 mb-4">
              <div class="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-left text-xs text-dark-200">DNI</div>
              <div class="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-left text-xs text-dark-200">Contrase&ntilde;a</div>
            </div>
            <div class="w-full bg-[#4F7BF7] text-white rounded-lg py-2.5 text-xs font-semibold">Iniciar sesi&oacute;n</div>
          </div>
          <p class="text-white font-bold text-xs mt-5">Un proyecto del Banco Mundial y uDocz</p>
        </div>
      </div>
      <p class="text-center text-white/20 text-[10px] mt-4 font-display"><span data-lang-i="es">Plataforma de tutor&iacute;a de matem&aacute;ticas &mdash; test.schools.udocz.com</span><span data-lang-i="en">Math tutoring platform &mdash; test.schools.udocz.com</span></p>
    </div>
  </div>
</div>
</section>

<!-- ════════════ CAREER COACH ════════════ -->
<section id="coach" class="py-24 bg-white relative overflow-hidden">
<div class="absolute top-0 left-0 w-[400px] h-[400px] bg-brand-50 rounded-full -translate-y-1/2 -translate-x-1/2 opacity-40"></div>
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
  <div class="grid lg:grid-cols-2 gap-16 items-start">
    <!-- Left: Demo mockup -->
    <div class="reveal-left hidden lg:block order-1 lg:order-1">
      <div class="browser-frame border-dark-400">
        <div class="browser-bar bg-dark-600">
          <div class="browser-dot bg-red-400"></div>
          <div class="browser-dot bg-yellow-400"></div>
          <div class="browser-dot bg-green-400"></div>
          <div class="flex-1 ml-3 bg-white/5 rounded-md px-3 py-1 text-[10px] text-white/30 font-mono">eligiendo-mi-camino.app</div>
        </div>
        <div class="bg-[#FFF8F0] min-h-[420px] flex">
          <!-- Sidebar mockup — 8 steps -->
          <div class="w-[180px] shrink-0 bg-white border-r border-beige-100 p-3">
            <div class="flex items-center gap-2 mb-4">
              <img src="{GALLITO_MINI}" alt="" class="h-5 w-auto">
              <span class="font-display font-bold text-dark-500 text-[10px]">Eligiendo Mi Camino</span>
            </div>
            <div class="mb-3">
              <div class="w-full bg-brand-100 rounded-full h-1.5 mb-1"><div class="bg-brand-400 h-1.5 rounded-full" style="width:12%"></div></div>
              <span class="text-[8px] text-dark-200">Progreso 0%</span>
            </div>
            <div class="space-y-1 text-[9px]">
              <div class="flex items-center gap-1.5 p-1.5 bg-brand-50 rounded-md text-brand-500 font-semibold"><div class="w-3 h-3 bg-brand-400 rounded-full flex items-center justify-center text-white text-[6px]">1</div>Autoconocimiento</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">2</div>Mitos Vocac.</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">3</div>Test RIASEC</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">4</div>Expl. de Rutas</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">5</div>Expl. Ocupacional</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">6</div>Investigaci&oacute;n</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">7</div>Validaci&oacute;n</div>
              <div class="flex items-center gap-1.5 p-1.5 text-dark-200"><div class="w-3 h-3 bg-gray-200 rounded-full text-[6px] flex items-center justify-center text-gray-400">8</div>Decisi&oacute;n y Plan</div>
            </div>
          </div>
          <!-- Content mockup -->
          <div class="flex-1 p-4 overflow-hidden">
            <div class="flex items-start gap-3 mb-4">
              <img src="{GALLITO_MINI}" alt="" class="h-8 w-auto mt-1">
              <div class="bg-white rounded-2xl rounded-tl-sm p-3 shadow-sm border border-beige-100 max-w-[250px]">
                <p class="font-display font-bold text-dark-500 text-lg">Hola <span>&#128075;</span></p>
                <p class="text-dark-300 text-[10px] leading-relaxed mt-1">Terminar el colegio es un momento importante. Este programa te ayuda paso a paso.</p>
              </div>
            </div>
            <div class="bg-white rounded-2xl p-3 shadow-sm border border-beige-100 mb-3">
              <p class="font-display font-bold text-dark-500 text-[11px] mb-2">De cada 100 j&oacute;venes peruanos...</p>
              <div class="grid grid-cols-4 gap-1.5 text-center">
                <div class="bg-green-50 rounded-lg p-1.5"><p class="font-display font-black text-green-600 text-sm">45</p><p class="text-[7px] text-dark-300">Trabajan</p></div>
                <div class="bg-purple-50 rounded-lg p-1.5"><p class="font-display font-black text-purple-600 text-sm">26</p><p class="text-[7px] text-dark-300">Estudian</p></div>
                <div class="bg-blue-50 rounded-lg p-1.5"><p class="font-display font-black text-blue-600 text-sm">12</p><p class="text-[7px] text-dark-300">Ambos</p></div>
                <div class="bg-red-50 rounded-lg p-1.5"><p class="font-display font-black text-red-500 text-sm">17</p><p class="text-[7px] text-dark-300">NINIs</p></div>
              </div>
            </div>
            <div class="bg-white rounded-2xl p-3 shadow-sm border border-beige-100">
              <p class="text-[10px] text-dark-400 mb-1.5"><i class="fas fa-heart text-red-400 mr-1"></i> Tu Ikigai &mdash; el hilo de tu camino</p>
              <div class="grid grid-cols-3 gap-1">
                <div class="bg-red-50 rounded-lg p-1.5 text-center"><p class="text-[7px] font-semibold text-red-500">Lo que me gusta</p></div>
                <div class="bg-yellow-50 rounded-lg p-1.5 text-center"><p class="text-[7px] font-semibold text-yellow-600">Lo que hago bien</p></div>
                <div class="bg-green-50 rounded-lg p-1.5 text-center"><p class="text-[7px] font-semibold text-green-600">Mercado laboral</p></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <p class="text-center text-dark-200 text-[10px] mt-4 font-display"><span data-lang-i="es">Interfaz del Coach Vocacional con IA</span><span data-lang-i="en">AI Career Coach Interface</span></p>
    </div>

    <!-- Right: content -->
    <div class="order-2 lg:order-2">
      <div data-lang="es">
        <div class="reveal flex items-center gap-3 mb-3">
          <div class="w-14 h-14 bg-gradient-to-br from-brand-400 to-brand-600 rounded-2xl flex items-center justify-center shadow-lg shadow-brand-400/20"><i class="fas fa-compass text-white text-xl"></i></div>
          <div><p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-[0.25em]">Componente 2 &mdash; "Eligiendo Mi Camino"</p><h2 class="font-display text-3xl sm:text-4xl font-black text-dark-500">Coach Vocacional</h2></div>
        </div>
        <p class="reveal text-dark-200 text-[15px] max-w-lg mb-8 mt-4 leading-relaxed">Orientaci&oacute;n vocacional personalizada para TODOS los estudiantes: universidad, carreras t&eacute;cnicas o mercado laboral directo. <strong class="text-dark-500">142 ocupaciones en 12 sectores</strong> con datos del Ministerio de Trabajo.</p>

        <!-- 3 pillars -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-10 reveal">
          <div class="bg-beige-50 rounded-2xl p-4 text-center card-modern border border-beige-100"><div class="text-2xl mb-1">&#10084;&#65039;</div><p class="font-display font-bold text-dark-500 text-xs">Autoconocimiento</p><p class="text-dark-200 text-[9px] mt-0.5">Qui&eacute;n soy</p></div>
          <div class="bg-beige-50 rounded-2xl p-4 text-center card-modern border border-beige-100"><div class="text-2xl mb-1">&#127758;</div><p class="font-display font-bold text-dark-500 text-xs">Exploraci&oacute;n</p><p class="text-dark-200 text-[9px] mt-0.5">Opciones reales</p></div>
          <div class="bg-beige-50 rounded-2xl p-4 text-center card-modern border border-beige-100"><div class="text-2xl mb-1">&#127919;</div><p class="font-display font-bold text-dark-500 text-xs">Decisi&oacute;n</p><p class="text-dark-200 text-[9px] mt-0.5">Plan concreto</p></div>
        </div>

        <!-- 8 Steps -->
        <h3 class="reveal font-display font-bold text-dark-400 text-[11px] uppercase tracking-[0.2em] mb-5"><i class="fas fa-route text-brand-400 mr-2"></i>8 Pasos &mdash; 12 sesiones de 90 min</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
          <div class="reveal stagger-1 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">1</span></div><p class="font-display font-bold text-dark-500 text-xs">Autoconocimiento</p></div>
          <div class="reveal stagger-2 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">2</span></div><p class="font-display font-bold text-dark-500 text-xs">Mitos Vocacionales</p></div>
          <div class="reveal stagger-3 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">3</span></div><p class="font-display font-bold text-dark-500 text-xs">Test de Intereses RIASEC</p></div>
          <div class="reveal stagger-4 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">4</span></div><p class="font-display font-bold text-dark-500 text-xs">Exploraci&oacute;n de Rutas</p></div>
          <div class="reveal stagger-5 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">5</span></div><p class="font-display font-bold text-dark-500 text-xs">Explorador Ocupacional</p></div>
          <div class="reveal stagger-6 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">6</span></div><p class="font-display font-bold text-dark-500 text-xs">Investigaci&oacute;n</p></div>
          <div class="reveal stagger-7 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">7</span></div><p class="font-display font-bold text-dark-500 text-xs">Validaci&oacute;n</p></div>
          <div class="reveal stagger-8 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">8</span></div><p class="font-display font-bold text-dark-500 text-xs">Decisi&oacute;n y Plan</p></div>
        </div>
      </div>
      <div data-lang="en">
        <div class="reveal flex items-center gap-3 mb-3">
          <div class="w-14 h-14 bg-gradient-to-br from-brand-400 to-brand-600 rounded-2xl flex items-center justify-center shadow-lg shadow-brand-400/20"><i class="fas fa-compass text-white text-xl"></i></div>
          <div><p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-[0.25em]">Component 2 &mdash; "Eligiendo Mi Camino"</p><h2 class="font-display text-3xl sm:text-4xl font-black text-dark-500">AI Career Coach</h2></div>
        </div>
        <p class="reveal text-dark-200 text-[15px] max-w-lg mb-8 mt-4 leading-relaxed">Personalized career guidance for ALL students: university, technical careers, or direct employment. <strong class="text-dark-500">142 occupations across 12 sectors</strong> with Ministry of Labor data.</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-10 reveal">
          <div class="bg-beige-50 rounded-2xl p-4 text-center card-modern border border-beige-100"><div class="text-2xl mb-1">&#10084;&#65039;</div><p class="font-display font-bold text-dark-500 text-xs">Self-Knowledge</p><p class="text-dark-200 text-[9px] mt-0.5">Who I am</p></div>
          <div class="bg-beige-50 rounded-2xl p-4 text-center card-modern border border-beige-100"><div class="text-2xl mb-1">&#127758;</div><p class="font-display font-bold text-dark-500 text-xs">Exploration</p><p class="text-dark-200 text-[9px] mt-0.5">Real options</p></div>
          <div class="bg-beige-50 rounded-2xl p-4 text-center card-modern border border-beige-100"><div class="text-2xl mb-1">&#127919;</div><p class="font-display font-bold text-dark-500 text-xs">Decision</p><p class="text-dark-200 text-[9px] mt-0.5">Concrete plan</p></div>
        </div>
        <h3 class="reveal font-display font-bold text-dark-400 text-[11px] uppercase tracking-[0.2em] mb-5"><i class="fas fa-route text-brand-400 mr-2"></i>8 Steps &mdash; 12 sessions of 90 min</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
          <div class="reveal stagger-1 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">1</span></div><p class="font-display font-bold text-dark-500 text-xs">Self-Discovery</p></div>
          <div class="reveal stagger-2 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">2</span></div><p class="font-display font-bold text-dark-500 text-xs">Vocational Myths</p></div>
          <div class="reveal stagger-3 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">3</span></div><p class="font-display font-bold text-dark-500 text-xs">Interest Test (RIASEC)</p></div>
          <div class="reveal stagger-4 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">4</span></div><p class="font-display font-bold text-dark-500 text-xs">Pathway Exploration</p></div>
          <div class="reveal stagger-5 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">5</span></div><p class="font-display font-bold text-dark-500 text-xs">Occupation Explorer</p></div>
          <div class="reveal stagger-6 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">6</span></div><p class="font-display font-bold text-dark-500 text-xs">Research</p></div>
          <div class="reveal stagger-7 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">7</span></div><p class="font-display font-bold text-dark-500 text-xs">Validation</p></div>
          <div class="reveal stagger-8 bg-white rounded-xl p-3.5 border border-beige-100 card-modern"><div class="flex items-center gap-2 mb-1.5"><span class="w-6 h-6 bg-brand-400 rounded-lg flex items-center justify-center text-white font-display font-black text-[10px]">8</span></div><p class="font-display font-bold text-dark-500 text-xs">Decision &amp; Plan</p></div>
        </div>
      </div>
    </div>
  </div>
</div>
</section>

<!-- ════════════ PARTNERS ════════════ -->
<section id="partners" class="py-20 mesh-dark text-white relative overflow-hidden">
<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
  <div class="reveal mb-12">
    <p class="text-brand-400 font-display font-bold text-[10px] uppercase tracking-[0.3em] mb-3"><span data-lang-i="es">Ecosistema de Socios</span><span data-lang-i="en">Partner Ecosystem</span></p>
    <h2 class="font-display text-3xl sm:text-4xl font-black"><span data-lang-i="es">Socios</span><span data-lang-i="en">Partners</span></h2>
  </div>
  <div class="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-5">
    <!-- DRELM with government seal -->
    <div class="reveal stagger-1 glass rounded-2xl p-6 card-modern text-center">
      <div class="h-14 flex items-center justify-center mb-3">
        <svg viewBox="0 0 80 100" class="h-12 w-auto" xmlns="http://www.w3.org/2000/svg">
          <path d="M40 5 L75 20 L75 55 C75 75 60 90 40 95 C20 90 5 75 5 55 L5 20 Z" fill="none" stroke="#8B0000" stroke-width="3"/>
          <path d="M40 12 L68 24 L68 53 C68 70 55 83 40 88 C25 83 12 70 12 53 L12 24 Z" fill="#8B0000" fill-opacity="0.1" stroke="#8B0000" stroke-width="1.5"/>
          <path d="M30 35 L40 25 L50 35 L50 55 L30 55 Z" fill="#8B0000" fill-opacity="0.8"/>
          <rect x="34" y="45" width="5" height="10" rx="1" fill="white" fill-opacity="0.9"/>
          <rect x="41" y="45" width="5" height="10" rx="1" fill="white" fill-opacity="0.9"/>
          <circle cx="40" cy="35" r="3" fill="white" fill-opacity="0.9"/>
          <path d="M25 60 L40 68 L55 60" fill="none" stroke="#8B0000" stroke-width="2"/>
        </svg>
      </div>
      <p class="font-display font-bold text-white/90 text-sm">DRELM</p>
      <p class="text-white/30 text-[9px] mt-1">Gobierno del Per&uacute;</p>
      <p class="text-white/25 text-[9px] mt-0.5"><span data-lang-i="es">Acceso a colegios</span><span data-lang-i="en">School access</span></p>
    </div>
    <!-- Anthropic -->
    <div class="reveal stagger-2 glass rounded-2xl p-6 card-modern text-center">
      <div class="h-14 flex items-center justify-center mb-3">
        <div class="flex flex-col items-center gap-0.5">
          <div class="flex items-center gap-1.5">
            <svg viewBox="0 0 78 60" class="h-6 w-auto" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M56.3 0H43.7L65.3 60h12.6L56.3 0zM21.7 0L0 60h12.9l4.4-12h22.8l4.4 12H57.4L35.7 0H21.7zm-0.8 38L28.7 16l7.8 22H20.9z" fill="#D4451A"/></svg>
          </div>
        </div>
      </div>
      <p class="font-display font-bold text-white/90 text-sm">Anthropic</p>
      <p class="text-white/25 text-[9px] mt-1"><span data-lang-i="es">Tokens de IA (Claude)</span><span data-lang-i="en">AI tokens (Claude)</span></p>
    </div>
    <!-- uDocz -->
    <div class="reveal stagger-3 glass rounded-2xl p-6 card-modern text-center">
      <div class="h-14 flex items-center justify-center mb-3">
        <div class="flex items-center gap-1">
          <svg viewBox="0 0 24 24" class="w-6 h-6" fill="none"><rect x="2" y="4" width="14" height="16" rx="2" stroke="#2563EB" stroke-width="2"/><path d="M18 8h2a2 2 0 012 2v8a2 2 0 01-2 2h-2" stroke="#2563EB" stroke-width="2"/><path d="M6 9h6M6 13h4" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg>
          <span style="font-family:'Poppins',sans-serif;font-weight:700;font-style:italic;font-size:20px;color:#2563EB">uDocz</span>
        </div>
      </div>
      <p class="font-display font-bold text-white/90 text-sm">uDocz</p>
      <p class="text-white/25 text-[9px] mt-1"><span data-lang-i="es">Plataforma EdTech</span><span data-lang-i="en">EdTech platform</span></p>
    </div>
    <!-- UPC with university shield -->
    <div class="reveal stagger-4 glass rounded-2xl p-6 card-modern text-center">
      <div class="h-14 flex items-center justify-center mb-3">
        <svg viewBox="0 0 80 100" class="h-12 w-auto" xmlns="http://www.w3.org/2000/svg">
          <path d="M40 5 L72 18 L72 50 C72 72 58 86 40 92 C22 86 8 72 8 50 L8 18 Z" fill="#003C71" fill-opacity="0.15" stroke="#003C71" stroke-width="3"/>
          <path d="M40 15 L64 25 L64 48 C64 66 54 78 40 83 C26 78 16 66 16 48 L16 25 Z" fill="none" stroke="#003C71" stroke-width="1.5"/>
          <text x="40" y="48" text-anchor="middle" font-family="Poppins,sans-serif" font-weight="900" font-size="20" fill="#003C71">UPC</text>
          <path d="M28 58 L40 64 L52 58" fill="none" stroke="#003C71" stroke-width="2"/>
          <circle cx="40" cy="28" r="4" fill="none" stroke="#003C71" stroke-width="1.5"/>
          <path d="M38 26 L40 22 L42 26" fill="none" stroke="#003C71" stroke-width="1.5"/>
        </svg>
      </div>
      <p class="font-display font-bold text-white/90 text-sm">UPC</p>
      <p class="text-white/30 text-[8px] mt-1 leading-tight">Universidad Peruana de<br>Ciencias Aplicadas</p>
      <p class="text-white/25 text-[9px] mt-0.5"><span data-lang-i="es">Capacitaci&oacute;n docente</span><span data-lang-i="en">Teacher training</span></p>
    </div>
  </div>
</div>
</section>

<!-- ════════════ DECRG EVALUATION ════════════ -->
<section id="evaluation" class="py-24 bg-white relative overflow-hidden">
<div class="absolute top-0 right-0 w-[400px] h-[400px] bg-brand-50 rounded-full -translate-y-1/3 translate-x-1/3 opacity-30"></div>
<div class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-beige-100/20 rounded-full translate-y-1/3 -translate-x-1/3"></div>
<div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

  <!-- Spanish -->
  <div data-lang="es">
    <div class="text-center mb-14 reveal">
      <div class="inline-flex items-center gap-2 bg-wb-blue/10 px-5 py-2 rounded-full text-[10px] font-bold text-wb-blue uppercase tracking-[0.2em] mb-4">
        <i class="fas fa-flask text-wb-light"></i> Desarrollo de Investigaci&oacute;n &mdash; AI/DD Initiative
      </div>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-black text-dark-500">Evaluaci&oacute;n de Impacto</h2>
    </div>

    <!-- Research question -->
    <div class="reveal max-w-3xl mx-auto mb-10">
      <div class="relative bg-gradient-to-br from-wb-blue/5 to-brand-50 rounded-3xl p-8 border border-wb-blue/10">
        <div class="absolute -top-4 left-8 w-8 h-8 bg-wb-blue rounded-xl flex items-center justify-center text-white text-xs font-bold"><i class="fas fa-question"></i></div>
        <p class="text-dark-400 text-[15px] italic leading-relaxed pl-4 font-display font-semibold">&iquest;Puede la tutor&iacute;a con IA mejorar los resultados en matem&aacute;ticas y ayudar a los estudiantes a conectar su educaci&oacute;n con oportunidades laborales reales, dentro de las restricciones reales de los colegios p&uacute;blicos?</p>
      </div>
    </div>

    <!-- Description -->
    <div class="reveal mb-10">
      <p class="text-dark-200 text-[15px] leading-[1.8] mb-5">La iniciativa AI/DD del Grupo de Investigaci&oacute;n en Desarrollo (DECRG) realizar&aacute; una evaluaci&oacute;n rigurosa de una intervenci&oacute;n impulsada por IA para estudiantes de &uacute;ltimo a&ntilde;o de secundaria en Lima, Per&uacute;, implementada por la Direcci&oacute;n Regional de Educaci&oacute;n de Lima Metropolitana (DRELM) como un Premio de Innovaci&oacute;n del GBM. El estudio examina si un tutor de matem&aacute;ticas con IA y un coach vocacional con IA pueden mejorar los resultados de aprendizaje y alinear mejor las habilidades y planes de carrera de los estudiantes con las necesidades del mercado laboral en sectores econ&oacute;micos clave. La intervenci&oacute;n opera completamente dentro de la capacidad docente existente, las horas de clase y la infraestructura escolar.</p>
      <p class="text-dark-300 text-sm font-semibold"><i class="fas fa-users text-wb-light mr-2"></i>Liderado conjuntamente por Ezequiel Molina (LAC Education) y Carolina Lopez (Development Research Group).</p>
    </div>

    <!-- Key details glass card -->
    <div class="reveal grid sm:grid-cols-3 gap-4 max-w-3xl mx-auto">
      <div class="bg-gradient-to-br from-wb-blue/5 to-white rounded-2xl p-6 text-center border border-wb-blue/10 card-modern">
        <div class="inline-flex items-center justify-center w-12 h-12 bg-wb-blue/10 rounded-2xl mb-3"><i class="fas fa-vials text-wb-blue text-lg"></i></div>
        <p class="font-display font-black text-wb-blue text-lg">RCT</p>
        <p class="text-dark-200 text-[10px] mt-1">Ensayo Controlado<br>Aleatorizado</p>
      </div>
      <div class="bg-gradient-to-br from-brand-50 to-white rounded-2xl p-6 text-center border border-brand-100 card-modern">
        <div class="inline-flex items-center justify-center w-12 h-12 bg-brand-400/10 rounded-2xl mb-3"><i class="fas fa-school text-brand-400 text-lg"></i></div>
        <p class="font-display font-black text-brand-400 text-lg">100</p>
        <p class="text-dark-200 text-[10px] mt-1">Colegios<br>p&uacute;blicos</p>
      </div>
      <div class="bg-gradient-to-br from-green-50 to-white rounded-2xl p-6 text-center border border-green-100 card-modern">
        <div class="inline-flex items-center justify-center w-12 h-12 bg-green-100 rounded-2xl mb-3"><i class="fas fa-user-graduate text-green-600 text-lg"></i></div>
        <p class="font-display font-black text-green-600 text-lg">6,300</p>
        <p class="text-dark-200 text-[10px] mt-1">Estudiantes<br>participantes</p>
      </div>
    </div>
  </div>

  <!-- English -->
  <div data-lang="en">
    <div class="text-center mb-14 reveal">
      <div class="inline-flex items-center gap-2 bg-wb-blue/10 px-5 py-2 rounded-full text-[10px] font-bold text-wb-blue uppercase tracking-[0.2em] mb-4">
        <i class="fas fa-flask text-wb-light"></i> Development Research &mdash; AI/DD Initiative
      </div>
      <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-black text-dark-500">Impact Evaluation</h2>
    </div>

    <!-- Research question -->
    <div class="reveal max-w-3xl mx-auto mb-10">
      <div class="relative bg-gradient-to-br from-wb-blue/5 to-brand-50 rounded-3xl p-8 border border-wb-blue/10">
        <div class="absolute -top-4 left-8 w-8 h-8 bg-wb-blue rounded-xl flex items-center justify-center text-white text-xs font-bold"><i class="fas fa-question"></i></div>
        <p class="text-dark-400 text-[15px] italic leading-relaxed pl-4 font-display font-semibold">Can AI tutoring improve math outcomes and help students connect their education to real job opportunities, within the real constraints of public schools?</p>
      </div>
    </div>

    <!-- Description -->
    <div class="reveal mb-10">
      <p class="text-dark-200 text-[15px] leading-[1.8] mb-5">The Development Research Group's AI/DD initiative will conduct a rigorous evaluation of an AI-powered intervention for senior secondary students in Lima, Peru, implemented by the Regional Directorate of Education of Lima (DRELM) as a WBG Innovation Award. The study examines whether an AI math tutor and an AI career coach can improve learning outcomes and better align students' skills and career plans with labor market needs in key economic sectors. The intervention operates fully within existing teacher capacity, class hours, and school infrastructure.</p>
      <p class="text-dark-300 text-sm font-semibold"><i class="fas fa-users text-wb-light mr-2"></i>Jointly led by Ezequiel Molina (LAC Education) and Carolina Lopez (Development Research Group).</p>
    </div>

    <!-- Key details glass card -->
    <div class="reveal grid sm:grid-cols-3 gap-4 max-w-3xl mx-auto">
      <div class="bg-gradient-to-br from-wb-blue/5 to-white rounded-2xl p-6 text-center border border-wb-blue/10 card-modern">
        <div class="inline-flex items-center justify-center w-12 h-12 bg-wb-blue/10 rounded-2xl mb-3"><i class="fas fa-vials text-wb-blue text-lg"></i></div>
        <p class="font-display font-black text-wb-blue text-lg">RCT</p>
        <p class="text-dark-200 text-[10px] mt-1">Randomized Controlled<br>Trial</p>
      </div>
      <div class="bg-gradient-to-br from-brand-50 to-white rounded-2xl p-6 text-center border border-brand-100 card-modern">
        <div class="inline-flex items-center justify-center w-12 h-12 bg-brand-400/10 rounded-2xl mb-3"><i class="fas fa-school text-brand-400 text-lg"></i></div>
        <p class="font-display font-black text-brand-400 text-lg">100</p>
        <p class="text-dark-200 text-[10px] mt-1">Public<br>schools</p>
      </div>
      <div class="bg-gradient-to-br from-green-50 to-white rounded-2xl p-6 text-center border border-green-100 card-modern">
        <div class="inline-flex items-center justify-center w-12 h-12 bg-green-100 rounded-2xl mb-3"><i class="fas fa-user-graduate text-green-600 text-lg"></i></div>
        <p class="font-display font-black text-green-600 text-lg">6,300</p>
        <p class="text-dark-200 text-[10px] mt-1">Participating<br>students</p>
      </div>
    </div>
  </div>

</div>
</section>

<!-- ════════════ TOOLKIT ════════════ -->
<section id="toolkit" class="py-24 bg-dark-800 text-white relative overflow-hidden">
<div class="absolute top-0 right-0 w-[600px] h-[600px] bg-brand-400/3 rounded-full -translate-y-1/2 translate-x-1/2"></div>
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
  <div class="text-center mb-14 reveal">
    <div class="inline-flex items-center gap-2 bg-brand-400/10 border border-brand-400/20 px-5 py-2 rounded-full text-xs font-display font-bold text-brand-400 mb-5">
      <i class="fas fa-lock"></i> World Bank TTL Exclusive
    </div>
    <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-black"><span data-lang-i="es">Toolkit de Replicaci&oacute;n</span><span data-lang-i="en">Replication Toolkit</span></h2>
    <p class="text-white/25 mt-4 max-w-xl mx-auto text-sm leading-relaxed"><span data-lang-i="es">Recursos para TTLs del Banco Mundial que desean replicar este programa en otros pa&iacute;ses.</span><span data-lang-i="en">Resources for World Bank TTLs seeking to replicate this program in other countries.</span></p>
  </div>

  <!-- Lock -->
  <div id="tkLock" class="max-w-sm mx-auto mb-12 reveal">
    <div class="glass rounded-3xl p-10 text-center border border-white/5">
      <div class="w-16 h-16 bg-brand-400/10 rounded-2xl flex items-center justify-center mx-auto mb-5"><i class="fas fa-key text-brand-400 text-2xl"></i></div>
      <label class="block text-xs text-white/30 mb-4 font-semibold"><span data-lang-i="es">Ingresa el c&oacute;digo de acceso</span><span data-lang-i="en">Enter access code</span></label>
      <div class="flex gap-2">
        <input id="codeInput" type="text" placeholder="WB-TTL-XXXX" class="flex-1 px-4 py-3.5 bg-white/5 border border-white/10 rounded-xl text-white placeholder-white/15 focus:outline-none focus:ring-2 focus:ring-brand-400 focus:border-transparent text-center font-mono text-lg tracking-[0.2em]" onkeypress="if(event.key==='Enter')checkCode()">
        <button onclick="checkCode()" class="px-6 py-3.5 bg-brand-400 text-white font-display font-bold rounded-xl hover:bg-brand-500 transition-all duration-300 text-sm hover:shadow-lg hover:shadow-brand-400/20"><span data-lang-i="es">Entrar</span><span data-lang-i="en">Enter</span></button>
      </div>
      <p id="codeErr" class="text-red-400 text-xs mt-3" style="display:none"><i class="fas fa-times-circle mr-1"></i><span data-lang-i="es">C&oacute;digo incorrecto</span><span data-lang-i="en">Incorrect code</span></p>
    </div>
  </div>

  <!-- Content (hidden) -->
  <div id="tkContent" class="hidden max-w-5xl mx-auto">
    <div class="glass rounded-3xl p-8 mb-8 border border-brand-400/10">
      <h3 class="font-display text-xl font-bold gradient-text mb-2"><span data-lang-i="es">Bienvenido al Toolkit</span><span data-lang-i="en">Welcome to the Toolkit</span></h3>
      <p class="text-white/40 text-sm"><span data-lang-i="es">Informaci&oacute;n t&eacute;cnica y operativa para adaptar "Eligiendo Mi Camino" a otro pa&iacute;s.</span><span data-lang-i="en">Technical and operational information to adapt "Eligiendo Mi Camino" to another country.</span></p>
    </div>
    <div class="grid lg:grid-cols-2 gap-5 mb-8">
      <div class="glass rounded-2xl p-6 card-modern"><div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 bg-brand-400/15 rounded-xl flex items-center justify-center text-brand-400 font-display font-black">1</div><h4 class="font-display font-bold">Localization</h4></div><div class="space-y-2.5 text-xs text-white/40"><p><strong class="text-white/70">Math Tutor:</strong> Replace curriculum diagnostics. Need ~4,000 items + knowledge graph.</p><p><strong class="text-white/70">Career Coach:</strong> Local labor data, education pathways, scholarship DB, RIASEC validation.</p><p><strong class="text-white/70">Cultural:</strong> Mascot/branding, family simulator, teen language adaptation.</p></div></div>
      <div class="glass rounded-2xl p-6 card-modern"><div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 bg-brand-400/15 rounded-xl flex items-center justify-center text-brand-400 font-display font-black">2</div><h4 class="font-display font-bold">Institutional Setup</h4></div><div class="space-y-2.5 text-xs text-white/40"><p><strong class="text-white/70">Ministry:</strong> Secure Education Ministry buy-in. Peru needed DRELM for curriculum alignment.</p><p><strong class="text-white/70">Partners:</strong> EdTech platform, AI provider, university for teacher training.</p><p><strong class="text-white/70">Pilot:</strong> Start 5-10 schools. Include diverse sample. Collect baseline data.</p></div></div>
      <div class="glass rounded-2xl p-6 card-modern"><div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 bg-brand-400/15 rounded-xl flex items-center justify-center text-brand-400 font-display font-black">3</div><h4 class="font-display font-bold">Technical Requirements</h4></div><div class="space-y-2.5 text-xs text-white/40"><p><strong class="text-white/70">Math:</strong> Diagnostic bank + knowledge graph + Socratic engine + retrieval practice.</p><p><strong class="text-white/70">Career:</strong> LLM with safety guardrails + RAG system + RIASEC + parent simulator.</p><p><strong class="text-white/70">Privacy:</strong> Student data (minors). Local data protection. No PII in AI prompts.</p></div></div>
      <div class="glass rounded-2xl p-6 card-modern"><div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 bg-brand-400/15 rounded-xl flex items-center justify-center text-brand-400 font-display font-black">4</div><h4 class="font-display font-bold">Timeline &amp; Budget</h4></div><div class="space-y-2.5 text-xs text-white/40"><p><strong class="text-white/70">Phase 1 (3mo):</strong> Design, stakeholder mapping, institutional agreements.</p><p><strong class="text-white/70">Phase 2 (4mo):</strong> Development, content, AI prompts, teacher training materials.</p><p><strong class="text-white/70">Phase 3 (3mo):</strong> Pilot 5-10 schools. Phase 4 (6mo+): Scale 50+ schools.</p></div></div>
    </div>
    <div class="glass rounded-3xl p-6 border border-brand-400/15">
      <h3 class="font-display font-bold gradient-text text-sm mb-4"><i class="fas fa-lightbulb mr-2"></i>Key Lessons from Peru</h3>
      <div class="grid sm:grid-cols-2 gap-3 text-xs text-white/40">
        <p><strong class="text-white/70"><i class="fas fa-check text-brand-400 mr-1.5"></i>AI = facilitator, not advisor.</strong> AI must ONLY ask questions and present info.</p>
        <p><strong class="text-white/70"><i class="fas fa-check text-brand-400 mr-1.5"></i>Include ALL pathways.</strong> 70% won't attend university. Treat all routes equally.</p>
        <p><strong class="text-white/70"><i class="fas fa-check text-brand-400 mr-1.5"></i>Family matters.</strong> Parent opinion is #1 factor. Parent simulator was most valued.</p>
        <p><strong class="text-white/70"><i class="fas fa-check text-brand-400 mr-1.5"></i>90-min sessions.</strong> Design sessions that fit local school schedules.</p>
        <p><strong class="text-white/70"><i class="fas fa-check text-brand-400 mr-1.5"></i>Diagnose first, tutor second.</strong> Most AI tools fail without understanding the error.</p>
        <p><strong class="text-white/70"><i class="fas fa-check text-brand-400 mr-1.5"></i>Onboarding = success.</strong> Teacher training quality correlates directly with adoption.</p>
      </div>
    </div>
    <p class="text-center text-white/10 text-[10px] mt-8">Contact: project team through your World Bank regional office. Code: share only with authorized TTLs.</p>
  </div>
</div>
</section>

<!-- ════════════ FOOTER ════════════ -->
<footer class="bg-dark-800 pt-8 pb-4 border-t border-white/5">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex flex-col md:flex-row justify-between items-center gap-6">
    <div class="flex items-center gap-3">
      <img src="{WBG_LOGO_B64}" alt="WB" class="h-5 w-auto brightness-0 invert opacity-30">
      <div class="w-px h-4 bg-white/5"></div>
      <img src="{GALLITO_MINI}" alt="Gallito" class="h-5 w-auto opacity-40">
      <div>
        <p class="font-display font-bold text-white/50 text-xs">Eligiendo Mi Camino</p>
        <p class="text-white/15 text-[9px]"><span data-lang-i="es">IA para el aprendizaje y las decisiones vocacionales</span><span data-lang-i="en">AI for learning and career decisions</span></p>
      </div>
    </div>
    <div class="text-white/10 text-[10px]">
      <span>&copy; 2026 World Bank Group. LAC Education.</span>
    </div>
  </div>
</div>
<div class="stripe mt-6"></div>
</footer>

</body>
</html>'''

# Write
out = r'C:\Users\cosmo\Downloads\AI Career Coach\Website\index.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'v5 written: {len(html):,} bytes')
print(f'Toolkit code: WB-TTL-2026')
