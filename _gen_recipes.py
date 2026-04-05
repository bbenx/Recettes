# -*- coding: utf-8 -*-
"""
20 recettes · céto aligné objectif perso (ordre de grandeur cohérent)
- Cible journalière (1 jour = 4 repas du planning) : ~1750 kcal, ~120 g prot, ~132 g lipides,
  ~20 g glucides nets (céto plus strict) → lipides ~68 % des kcal, prot ~27 % des kcal.
- Protéines : œufs, poulet (÷4), sardines, maquereau, ricotta, gruyère ; repas avec poulet : dose de
  **poudre isolat** en grammes (réf. **30 g poudre ≈ 20 g prot** — ajuster selon étiquette).
- Repas salés : 2 prot + 2 légumes pauvres en glucides + 3 portions « fruits »
  = uniquement fruits rouges en petites quantités (mix congelé), réparties en 3 lignes
- Pas d’avoine, pas de galettes de riz, pas d’ananas / pomme / raisin en quantité (trop de sucre)
- Lipides : beurre (cuisson), huile d’olive (cuisson), **huile de noix uniquement en finition / cru** (jamais chauffée).
Macros affichés : arrondis cohérents avec la somme journalière cible (glucides ≈ nets).
"""
def _b3():
    """3 × 15g baies = ~45g / repas salé (≈ 3–4 g gluc. nets)."""
    return ["15g mix fruits rouges", "15g mix fruits rouges", "15g mix fruits rouges"]


RECIPES = [
    # Petit-déj : ~438 kcal · 29P · 34L · 4G (plafond gluc. journée à 20 g)
    ("01", "Œufs · Beurre · Gruyère · Avocat", "t-ptdej", "Petit dej · céto",
     ["3 œufs brouillés", "11g beurre (cuisson)", "9g huile de noix (finition, cru)", "15g gruyère râpé", "40g avocat"],
     [],
     438, 29, 34, 4),
    ("02", "Œufs · Ricotta · Épinards · Huile", "t-ptdej", "Petit dej · céto",
     ["2 œufs", "100g ricotta", "150g épinards surgelés", "1 c.à.c. huile d'olive (cuisson)", "9g huile de noix (finition, cru)"],
     [],
     438, 29, 34, 4),
    ("03", "Sardines · Œuf · Concombre · Beurre", "t-ptdej", "Petit dej · céto",
     ["½ boîte sardines", "1 œuf dur", "100g concombre", "9g beurre", "6g huile de noix (finition, cru)", "citron"],
     [],
     438, 29, 34, 4),
    ("04", "Omelette · Champignons · Gruyère", "t-ptdej", "Petit dej · céto",
     ["3 œufs", "120g champignons surgelés", "20g gruyère râpé", "9g beurre (cuisson)", "6g huile de noix (finition, cru)"],
     [],
     438, 29, 34, 4),
    ("05", "Maquereau · Ricotta · Tomate cerise", "t-ptdej", "Petit dej · céto",
     ["½ boîte maquereau", "80g ricotta", "6 tomates cerises", "1 c.à.c. huile d'olive (cuisson)", "9g huile de noix (finition, cru)"],
     [],
     438, 29, 34, 4),
    # Déjeuner : ~499 kcal · 31P · 39L · 6G (+ 3×15g baies)
    ("06", "Poulet · Sardines · Brocoli courgette", "t-dej", "Déjeuner · céto 2P+2L+3F",
     ["35g poulet", "½ boîte sardines", "15g gruyère râpé", "180g brocoli surgelé", "100g courgette surgelée", "36g poudre isolat"],
     _b3(),
     499, 31, 39, 6),
    ("07", "Œufs · Poulet · Chou-fleur poivron", "t-dej", "Déjeuner · céto 2P+2L+3F",
     ["2 œufs au plat", "25g poulet", "9g beurre (cuisson)", "6g huile de noix (finition, cru)", "200g chou-fleur surgelé", "80g poivron surgelé", "26g poudre isolat"],
     _b3(),
     499, 31, 39, 6),
    ("08", "Maquereau · Ricotta · Haricots champignons", "t-dej", "Déjeuner · céto 2P+2L+3F",
     ["1 boîte maquereau", "70g ricotta", "1 c.à.c. huile d'olive (cuisson)", "9g huile de noix (finition, cru)", "100g haricots verts surgelés", "100g champignons surgelés"],
     _b3(),
     499, 31, 39, 6),
    ("09", "Sardines · Œufs · Épinards courgette", "t-dej", "Déjeuner · céto 2P+2L+3F",
     ["1 boîte sardines", "2 œufs dur", "15g gruyère râpé", "150g épinards surgelés", "100g courgette surgelée"],
     _b3(),
     499, 31, 39, 6),
    ("10", "Poulet · Maquereau · Brocoli champignons", "t-dej", "Déjeuner · céto 2P+2L+3F",
     ["30g poulet", "½ boîte maquereau", "9g beurre (cuisson)", "6g huile de noix (finition, cru)", "150g brocoli surgelé", "80g champignons surgelés", "31g poudre isolat"],
     _b3(),
     499, 31, 39, 6),
    # 16h : ~388 kcal · 29P · 28L · 5G
    ("11", "Œufs · Sardines · Concombre tomate", "t-milieu", "16h · céto 2P+2L+3F",
     ["2 œufs durs", "¼ boîte sardines", "15g gruyère", "80g concombre", "4 tomates cerises"],
     _b3(),
     388, 29, 28, 5),
    ("12", "Ricotta · Sardines · Salade huile", "t-milieu", "16h · céto 2P+2L+3F",
     ["90g ricotta", "½ boîte sardines", "1 c.à.c. huile d'olive (salade)", "9g huile de noix (finition, cru)", "grande poignée salade", "½ concombre"],
     _b3(),
     388, 29, 28, 5),
    ("13", "Poulet · Œuf · Courgette haricots", "t-milieu", "16h · céto 2P+2L+3F",
     ["25g poulet", "1 œuf dur", "6g beurre (cuisson)", "4g huile de noix (finition, cru)", "100g courgette surgelée", "80g haricots verts surgelés", "26g poudre isolat"],
     _b3(),
     388, 29, 28, 5),
    ("14", "Maquereau · Ricotta · Poivron chou-fleur", "t-milieu", "16h · céto 2P+2L+3F",
     ["½ boîte maquereau", "60g ricotta", "1 c.à.c. huile d'olive (cuisson)", "9g huile de noix (finition, cru)", "80g poivron surgelé", "100g chou-fleur surgelé"],
     _b3(),
     388, 29, 28, 5),
    ("15", "Œufs · Poulet · Champignons épinards", "t-milieu", "16h · céto 2P+2L+3F",
     ["2 œufs", "18g poulet", "9g beurre (cuisson)", "6g huile de noix (finition, cru)", "100g champignons surgelés", "80g épinards surgelés", "18g poudre isolat"],
     _b3(),
     388, 29, 28, 5),
    # Dîner : ~423 kcal · 31P · 31L · 5G
    ("16", "Poulet · Sardines · Courgette brocoli", "t-diner", "Dîner · céto 2P+2L+3F",
     ["38g poulet", "½ boîte sardines", "12g beurre (cuisson)", "8g huile de noix (finition, cru)", "150g courgette surgelée", "120g brocoli surgelé", "39g poudre isolat"],
     _b3(),
     423, 31, 31, 5),
    ("17", "Œufs · Maquereau · Chou-fleur haricots", "t-diner", "Dîner · céto 2P+2L+3F",
     ["3 œufs au plat", "½ boîte maquereau", "15g gruyère", "180g chou-fleur surgelé", "100g haricots verts surgelés"],
     _b3(),
     423, 31, 31, 5),
    ("18", "Sardines · Ricotta · Épinards poivron", "t-diner", "Dîner · céto 2P+2L+3F",
     ["1 boîte sardines", "80g ricotta", "1 c.à.c. huile d'olive (cuisson)", "9g huile de noix (finition, cru)", "150g épinards surgelés", "80g poivron surgelé"],
     _b3(),
     423, 31, 31, 5),
    ("19", "Poulet · Œufs · Champignons courgette", "t-diner", "Dîner · céto 2P+2L+3F",
     ["33g poulet", "2 œufs", "12g beurre (cuisson)", "8g huile de noix (finition, cru)", "120g champignons surgelés", "120g courgette surgelée", "34g poudre isolat"],
     _b3(),
     423, 31, 31, 5),
    ("20", "Maquereau · Poulet · Brocoli épinards", "t-diner", "Dîner · céto 2P+2L+3F",
     ["½ boîte maquereau", "28g poulet", "9g beurre (cuisson)", "6g huile de noix (finition, cru)", "130g brocoli surgelé", "100g épinards surgelés", "28g poudre isolat"],
     _b3(),
     423, 31, 31, 5),
]

def ing_spans(norm, fruits):
    parts = [f'<span class="ing">{t}</span>' for t in norm]
    parts += [f'<span class="ing fruit">{t}</span>' for t in fruits]
    return "".join(parts)

def card_html(r):
    num, title, tcls, tlabel, norm, fruits, kcal, p, l, g = r
    ings = ing_spans(norm, fruits)
    return f'''      <div id="recette-{num}" class="recipe-card">
        <div class="recipe-top">
          <div class="rnum">{num}</div>
          <div style="flex:1"><div class="rtitle">{title}</div><div><span class="rtype {tcls}">{tlabel}</span></div></div>
        </div>
        <div class="recipe-ings">
          {ings}
        </div>
        <div class="recipe-macros">
          <div class="mac"><div class="mac-v kcal">{kcal}</div><div class="mac-l">kcal</div></div>
          <div class="mac"><div class="mac-v">{p}g</div><div class="mac-l">protéines</div></div>
          <div class="mac"><div class="mac-v">{l}g</div><div class="mac-l">lipides</div></div>
          <div class="mac"><div class="mac-v">{g}g</div><div class="mac-l">glucides</div></div>
        </div>
      </div>
'''

def plan_row(time, dot, num, kcal):
    r = RECIPES[int(num) - 1]
    title = r[1]
    short = title if len(title) < 40 else title[:37] + "…"
    return f'''          <div class="meal-row-wrap"><div class="meal-row" data-recipe="{num}" role="button" tabindex="0"><div class="meal-time">{time}</div><div class="mdot {dot}"></div><div class="meal-name">R{num} — {short}</div><div class="meal-k">{kcal}</div></div><div class="meal-detail" aria-hidden="true"></div></div>'''

DAYS_RAW = [
    ("LUNDI", "🏋️ Calistho", "01", "06", "11", "16"),
    ("MARDI", "🏃 Run 5km", "02", "07", "12", "17"),
    ("MERCREDI", "🏋️ Calistho", "03", "08", "13", "18"),
    ("JEUDI", "🏃 Run 5km", "04", "09", "14", "19"),
    ("VENDREDI", "🏋️ Calistho", "05", "10", "15", "20"),
]


def day_block(name, sport, b, l, m, d):
    rows = [b, l, m, d]
    ktot = sum(RECIPES[int(x) - 1][6] for x in rows)
    ptot = sum(RECIPES[int(x) - 1][7] for x in rows)
    ltot = sum(RECIPES[int(x) - 1][8] for x in rows)
    gtot = sum(RECIPES[int(x) - 1][9] for x in rows)
    kb = RECIPES[int(b) - 1][6]
    kl = RECIPES[int(l) - 1][6]
    km = RECIPES[int(m) - 1][6]
    kd = RECIPES[int(d) - 1][6]
    return f'''      <div class="day-card">
        <div class="day-head">
          <div class="day-name">{name}</div>
          <span class="day-sport">{sport}</span>
          <div class="day-totals">
            <div class="day-kcal">~{ktot} kcal</div>
            <div class="day-macros">P {ptot}g · L {ltot}g · G {gtot}g</div>
          </div>
        </div>
        <div class="day-meals">
{plan_row("7h30", "d-ptdej", b, kb)}
{plan_row("12h30", "d-dej", l, kl)}
{plan_row("16h00", "d-milieu", m, km)}
{plan_row("19h30", "d-diner", d, kd)}
        </div>
      </div>
'''


def build_week_need_html():
    """Somme des ingrédients sur 5 jours : chaque recette R01–R20 est utilisée 1×."""
    import re
    from collections import defaultdict

    acc = defaultdict(float)
    eggs = 0
    fish_s = 0.0
    fish_m = 0.0
    olive_cac = 0
    lemons = 0
    frac = {"¼": 0.25, "½": 0.5, "1": 1.0}

    def ingest(lines):
        nonlocal eggs, fish_s, fish_m, olive_cac, lemons
        for line in lines:
            if "½ concombre" in line:
                acc["concombre g"] += 180
            if "grande poignée salade" in line:
                acc["salade g"] += 60
            if re.search(r"citron", line) and "huile" not in line.lower():
                lemons += 1
            m = re.search(r"(\d+)\s*œufs?", line)
            if m:
                eggs += int(m.group(1))
            m = re.search(r"(\d+)g\s+poulet", line)
            if m:
                acc["poulet g"] += int(m.group(1))
            m = re.search(r"(\d+)g\s+poudre isolat", line)
            if m:
                acc["poudre g"] += int(m.group(1))
            pairs = [
                (r"(\d+)g\s+beurre", "beurre g"),
                (r"(\d+)g\s+huile de noix", "huile noix g"),
                (r"(\d+)g\s+gruyère", "gruyère g"),
                (r"(\d+)g\s+ricotta", "ricotta g"),
                (r"(\d+)g\s+avocat", "avocat g"),
                (r"(\d+)g\s+concombre", "concombre g"),
                (r"(\d+)g\s+brocoli", "brocoli g"),
                (r"(\d+)g\s+courgette", "courgette g"),
                (r"(\d+)g\s+chou-fleur", "chou-fleur g"),
                (r"(\d+)g\s+poivron", "poivron g"),
                (r"(\d+)g\s+épinards", "épinards g"),
                (r"(\d+)g\s+haricots verts", "haricots g"),
                (r"(\d+)g\s+champignons", "champignons g"),
                (r"(\d+)g\s+mix fruits rouges", "baies g"),
            ]
            for pat, key in pairs:
                m = re.search(pat, line)
                if m:
                    acc[key] += int(m.group(1))
            m = re.search(r"(\d+)\s+tomates?\s+cerises", line)
            if m:
                acc["tomates cerises"] += int(m.group(1))
            m = re.search(r"(¼|½|1)\s*boîte\s+sardines", line)
            if m:
                fish_s += frac[m.group(1)]
            m = re.search(r"(¼|½|1)\s*boîte\s+maquereau", line)
            if m:
                fish_m += frac[m.group(1)]
            if "1 c.à.c." in line and "huile" in line:
                olive_cac += 1

    for r in RECIPES:
        norm = r[4]
        fr = r[5]
        ingest(list(norm) + (list(fr) if fr else []))

    def row(lab, val):
        return f'      <div class="week-need-row"><span>{lab}</span><span>{val}</span></div>'

    def sub(t):
        return f'      <div class="week-need-sub">{t}</div>'

    def fmt_sard(x):
        if abs(x - 4.25) < 0.01:
            return "4¼ boîtes"
        if abs(x - 3.5) < 0.01:
            return "3½ boîtes"
        return f"{x:.2f} boîtes".replace(".", ",")

    lines = [
        '    <div class="week-need">',
        '      <div class="week-need-title">📋 Besoin exact · 5 jours (lun–ven)</div>',
        '      <p class="week-need-intro">Total des 20 repas du planning. Vérifie ton stock avant les courses ; '
        "½ concombre ≈ 180 g et 1 poignée de salade ≈ 60 g (ordre de grandeur).</p>",
        sub("Protéines · volaille"),
        row("Œufs", f"{eggs} pièces"),
        row("Blanc / filet de poulet (cru)", f"{int(acc['poulet g'])} g"),
        row("Poudre isolat (à peser)", f"{int(acc['poudre g'])} g"),
        sub("Poisson en boîte"),
        row("Sardines", fmt_sard(fish_s)),
        row("Maquereau", fmt_sard(fish_m)),
        sub("Laitages"),
        row("Ricotta", f"{int(acc['ricotta g'])} g"),
        row("Gruyère râpé", f"{int(acc['gruyère g'])} g"),
        sub("Lipides"),
        row("Beurre (cuisson)", f"{int(acc['beurre g'])} g"),
        row("Huile d’olive", f"{olive_cac} c. à café (~{olive_cac * 5} ml si 5 ml/c.)"),
        row("Huile de noix (finition cru)", f"{int(acc['huile noix g'])} g (~{int(acc['huile noix g']) + 10} ml env.)"),
        sub("Frais"),
        row("Avocat", f"{int(acc['avocat g'])} g"),
        row("Concombre", f"{int(acc['concombre g'])} g"),
        row("Tomates cerises", f"{int(acc['tomates cerises'])} pièces"),
        row("Salade (feuilles)", f"{int(acc['salade g'])} g"),
        row("Citrons", f"{lemons} pièce" + ("s" if lemons != 1 else "")),
        sub("Surgelés"),
        row("Brocoli", f"{int(acc['brocoli g'])} g"),
        row("Courgette", f"{int(acc['courgette g'])} g"),
        row("Chou-fleur", f"{int(acc['chou-fleur g'])} g"),
        row("Poivron", f"{int(acc['poivron g'])} g"),
        row("Épinards", f"{int(acc['épinards g'])} g"),
        row("Haricots verts", f"{int(acc['haricots g'])} g"),
        row("Champignons", f"{int(acc['champignons g'])} g"),
        sub("Baies"),
        row("Mix fruits rouges", f"{int(acc['baies g'])} g"),
        "    </div>",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    cards = "\n".join(card_html(r) for r in RECIPES)
    plan = "\n".join(day_block(*row) for row in DAYS_RAW)
    base = "/Users/ben/Desktop/plan-repas-pwa"
    idx_path = f"{base}/index.html"
    html = open(idx_path, encoding="utf-8").read()
    a = html.index('    <div id="recettes" class="section active">')
    b = html.index("    <!-- PLANNING -->", a)
    c = html.index('    <div id="planning" class="section">', b)
    d = html.index("    <!-- COURSES -->", c)
    intro = (
        '    <div id="recettes" class="section active">\n'
        '      <p style="font-size:11px;color:var(--muted);margin:0 0 14px;line-height:1.45">'
        '<strong>Céto (repères affichés)</strong> : une journée type du planning ≈ <strong>~1750 kcal</strong>, '
        '<strong>~120 g prot</strong>, <strong>~132 g lipides</strong>, <strong>~20 g glucides nets</strong> '
        '(céto plus strict ; lipides ~68 % des kcal). '
        'Repas salés : 2 protéines + 2 légumes « verts » + <strong>3×15 g mix fruits rouges</strong> '
        '(= 45 g / repas). <strong>Huile d’olive</strong> ou <strong>beurre</strong> pour la cuisson ; '
        '<strong>huile de noix</strong> uniquement en <strong>finition à cru</strong> (jamais chauffée). '
        'Pas d’avoine ni de galettes de riz. '
        'Les portions listées sont des guides ; viandes = <strong>poids cru</strong> (perte d’eau à la cuisson selon le produit). '
        '<strong>Poulet</strong> en quantité <strong>÷4</strong> : chaque recette concernée indique le <strong>grammage exact de poudre isolat</strong> à peser '
        '(référence <strong>30 g poudre ≈ 20 g prot</strong> ; adapter si ton produit diffère). '
        'Repères macros des cartes inchangés. Ajuste au poids réel si besoin.</p>\n\n'
    )
    new_rec = intro + cards + "\n    </div>\n\n"
    new_plan = (
        '    <!-- PLANNING -->\n'
        '    <div id="planning" class="section">\n\n'
        + plan
        + "\n    </div>\n\n"
    )
    html = html[:a] + new_rec + new_plan + html[d:]
    wn = build_week_need_html()
    ws = "<!-- WEEK_NEED_START -->"
    we = "<!-- WEEK_NEED_END -->"
    if ws in html and we in html:
        i0 = html.index(ws) + len(ws)
        i1 = html.index(we, i0)
        html = html[:i0] + "\n" + wn + "\n\n    " + html[i1:]
    open(idx_path, "w", encoding="utf-8").write(html)
    print("index.html patched")
