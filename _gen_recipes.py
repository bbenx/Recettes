# -*- coding: utf-8 -*-
"""
20 recettes · borderline kéto / très bas glucides
Protéines animales : œufs, poulet, maquereau, sardines uniquement
Glucides surtout : légumes, fruits rouges congelés, avoine, galettes riz, lentilles, patate douce, skyr, lait soja
"""
RECIPES = [
    # 01–05 Petit déj
    ("01", "Skyr · Amandes", "t-ptdej", "Petit dej · LC",
     ["180g skyr 0%", "12g amandes"],
     [],
     285, 28, 14, 8),
    ("02", "Œufs · Ricotta · Légumes surgelés", "t-ptdej", "Petit dej · LC",
     ["3 œufs", "80g ricotta", "150g mélange poivron courgette surgelé"],
     [],
     385, 32, 24, 9),
    ("03", "Lait soja · Œufs durs", "t-ptdej", "Petit dej · LC",
     ["300ml lait de soja non sucré", "2 œufs durs"],
     [],
     248, 22, 14, 4),
    ("04", "Flocons d'avoine · Skyr", "t-ptdej", "Petit dej · glucides",
     ["30g flocons d'avoine cuits à l'eau", "120g skyr 0%", "cannelle"],
     [],
     320, 26, 6, 28),
    ("05", "Sardines · Galettes de riz", "t-ptdej", "Petit dej · glucides",
     ["½ boîte sardines", "2 galettes de riz", "tomate", "citron"],
     [],
     338, 28, 16, 22),
    # 06–10 Déjeuner
    ("06", "Poulet · Brocoli · Chou-fleur surgelés", "t-dej", "Déjeuner · LC",
     ["150g poulet", "250g brocoli chou-fleur surgelés vapeur", "1 c.à.s. huile"],
     [],
     385, 48, 16, 12),
    ("07", "Poulet · Lentilles · Épinards", "t-dej", "Déjeuner · glucides",
     ["130g poulet", "80g lentilles cuites", "100g épinards surgelés", "ail"],
     [],
     398, 44, 8, 28),
    ("08", "Œufs · Courgettes · Haricots verts", "t-dej", "Déjeuner · LC",
     ["2 œufs", "200g courgettes haricots verts surgelés", "10g beurre"],
     [],
     315, 22, 22, 14),
    ("09", "Poulet · Patate douce · Carottes surgelées", "t-dej", "Déjeuner · glucides",
     ["140g poulet", "100g patate douce cuite", "100g carottes surgelées"],
     [],
     385, 42, 8, 32),
    ("10", "Maquereau · Salade · Tomate", "t-dej", "Déjeuner · LC",
     ["1 boîte maquereau", "grande salade", "1 tomate", "citron"],
     [],
     365, 34, 22, 8),
    # 11–15 16h
    ("11", "Skyr · Noix · Fruits rouges", "t-milieu", "16h · LC",
     ["200g skyr", "12g noix"],
     ["80g mix fruits rouges congelés"],
     275, 27, 10, 18),
    ("12", "Œufs durs · Galette de riz", "t-milieu", "16h · glucides",
     ["2 œufs durs", "1 galette de riz"],
     [],
     235, 16, 12, 11),
    ("13", "Ricotta · Tomate", "t-milieu", "16h · LC",
     ["150g ricotta", "1 tomate", "herbes"],
     [],
     228, 20, 14, 6),
    ("14", "Poulet froid · Concombre", "t-milieu", "16h · LC",
     ["120g poulet cuit", "½ concombre", "vinaigre"],
     [],
     215, 38, 5, 3),
    ("15", "Sardines · Galette de riz", "t-milieu", "16h · glucides",
     ["60g sardines", "1 galette de riz", "citron"],
     [],
     248, 22, 12, 12),
    # 16–20 Dîner
    ("16", "Maquereau · Chou-fleur rôti surgelé", "t-diner", "Dîner · LC",
     ["1 boîte maquereau", "250g chou-fleur surgelé au four", "1 c.à.s. huile"],
     [],
     415, 36, 26, 10),
    ("17", "Sardines · Œufs · Salade", "t-diner", "Dîner · LC",
     ["1 boîte sardines", "2 œufs durs", "salade", "tomate"],
     [],
     395, 34, 26, 6),
    ("18", "Poulet · Épinards · Bouillon", "t-diner", "Dîner · LC",
     ["150g poulet", "250g épinards surgelés", "10g beurre", "un peu de bouillon"],
     [],
     368, 46, 16, 8),
    ("19", "Omelette · Champignons surgelés", "t-diner", "Dîner · LC",
     ["3 œufs", "150g champignons surgelés", "10g beurre"],
     [],
     328, 22, 24, 6),
    ("20", "Poulet · Poivrons courgettes surgelés", "t-diner", "Dîner · LC",
     ["140g poulet", "220g poivrons courgettes surgelés", "sauce soja 1 c.à.s."],
     [],
     365, 44, 10, 14),
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
    short = title if len(title) < 46 else title[:43] + "…"
    return f'''          <div class="meal-row-wrap"><div class="meal-row" data-recipe="{num}" role="button" tabindex="0"><div class="meal-time">{time}</div><div class="mdot {dot}"></div><div class="meal-name">R{num} — {short}</div><div class="meal-k">{kcal}</div></div><div class="meal-detail" aria-hidden="true"></div></div>'''

DAYS_RAW = [
    ("LUNDI", "🏋️ Calistho", "01", "06", "11", "16"),
    ("MARDI", "🏃 Run 5km", "02", "07", "12", "17"),
    ("MERCREDI", "🏋️ Calistho", "03", "08", "13", "18"),
    ("JEUDI", "🏃 Run 5km", "04", "09", "14", "19"),
    ("VENDREDI", "🏋️ Calistho", "05", "10", "15", "20"),
]

def day_kcal(b, l, m, d):
    return sum(RECIPES[int(x) - 1][6] for x in (b, l, m, d))

DAYS = [(a, b, c, d, e, f, day_kcal(c, d, e, f)) for a, b, c, d, e, f in DAYS_RAW]

def day_block(name, sport, b, l, m, d, ktot):
    kb = RECIPES[int(b)-1][6]
    kl = RECIPES[int(l)-1][6]
    km = RECIPES[int(m)-1][6]
    kd = RECIPES[int(d)-1][6]
    return f'''      <div class="day-card">
        <div class="day-head">
          <div class="day-name">{name}</div>
          <span class="day-sport">{sport}</span>
          <div class="day-kcal">~{ktot} kcal</div>
        </div>
        <div class="day-meals">
{plan_row("7h30", "d-ptdej", b, kb)}
{plan_row("12h30", "d-dej", l, kl)}
{plan_row("16h00", "d-milieu", m, km)}
{plan_row("19h30", "d-diner", d, kd)}
        </div>
      </div>
'''

if __name__ == "__main__":
    cards = "\n".join(card_html(r) for r in RECIPES)
    plan = "\n".join(day_block(*x) for x in DAYS)
    base = "/Users/ben/Desktop/plan-repas-pwa"
    idx_path = f"{base}/index.html"
    html = open(idx_path, encoding="utf-8").read()
    a = html.index('    <div id="recettes" class="section active">')
    b = html.index("    <!-- PLANNING -->", a)
    c = html.index('    <div id="planning" class="section">', b)
    d = html.index("    <!-- COURSES -->", c)
    new_rec = (
        '    <div id="recettes" class="section active">\n'
        '      <p style="font-size:11px;color:var(--muted);margin:0 0 14px;line-height:1.45">'
        'Glucides = estimations. Les repas avec pastille « glucides » apportent avoine, galettes de riz, lentilles ou patate douce ; '
        'les autres : surtout légumes surgelés / frais, fruits rouges congelés, skyr et lait de soja.</p>\n\n'
        + cards
        + "\n    </div>\n\n"
    )
    new_plan = (
        '    <!-- PLANNING -->\n'
        '    <div id="planning" class="section">\n\n'
        + plan
        + "\n    </div>\n\n"
    )
    html = html[:a] + new_rec + new_plan + html[d:]
    open(idx_path, "w", encoding="utf-8").write(html)
    print("index.html patched")
