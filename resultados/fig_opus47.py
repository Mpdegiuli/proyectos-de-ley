"""Figure 1: Opus 4.7, interleaved run (corazon_cruzado). Usage: python fig_opus47.py <corazon_codificacion.csv> <out.png>"""
import csv, sys, collections
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if '/inter/Inter-' in f:
        fm.fontManager.addfont(f)
plt.rcParams['font.family'] = ['Inter', 'DejaVu Sans']
src, out = sys.argv[1], sys.argv[2]
rec = collections.Counter(); tot = collections.Counter()
for x in csv.DictReader(open(src, encoding='utf-8')):
    c = int(x['condicion'])
    if 14 <= c <= 17 and x['estrategia'] in ('recursiva', 'iterativa'):
        k = (x['idioma'], x['casa'].endswith('-razona'), c)
        tot[k] += 1; rec[k] += x['estrategia'] == 'recursiva'
assert all(v == 20 for v in tot.values()) and len(tot) == 16, tot
SURF, INK, INK2, GRID = '#fcfcfb', '#0b0b0b', '#52514e', '#e4e3df'
BASE, HEART = '#2a78d6', '#e34948'
groups = [(False, 14, 16, '“recursive”\nnamed first'),
          (False, 15, 17, '“iterative”\nnamed first'),
          (True, 14, 16, '“recursive”\nnamed first'),
          (True, 15, 17, '“iterative”\nnamed first')]
fig, axes = plt.subplots(1, 2, figsize=(11, 5.4), sharey=True, facecolor=SURF)
w = 0.34
for ax, (lang, title) in zip(axes, (('en', 'English prompts'), ('es', 'Spanish prompts'))):
    ax.set_facecolor(SURF)
    for i, (th, cb, ch, lab) in enumerate(groups):
        b, h = rec[(lang, th, cb)], rec[(lang, th, ch)]
        for dx, v, col in ((-w/2 - 0.01, b, BASE), (w/2 + 0.01, h, HEART)):
            ax.bar(i + dx, v, w, color=col, zorder=3)
            if v == 0:
                ax.plot([i + dx - w/2, i + dx + w/2], [0.12, 0.12], color=col, lw=2.5, zorder=3, solid_capstyle='butt')
            ax.text(i + dx, v + 0.5, str(v), ha='center', va='bottom', fontsize=11, color=INK, fontweight='medium')
    ax.set_xticks(range(4)); ax.set_xticklabels([g[3] for g in groups], fontsize=9.5, color=INK2, linespacing=1.3)
    ax.set_ylim(0, 22.5); ax.set_yticks([0, 5, 10, 15, 20])
    ax.tick_params(axis='y', colors=INK2, labelsize=9, length=0); ax.tick_params(axis='x', length=0, pad=6)
    ax.yaxis.grid(True, color=GRID, lw=0.8, zorder=0); ax.set_axisbelow(True)
    for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#b9b8b2')
    ax.axvline(1.5, color=GRID, lw=0.8, zorder=1)
    ax.set_title(title, loc='left', fontsize=12, color=INK, fontweight='medium', pad=10)
    for xc, lab in ((0.5, 'No thinking request'), (2.5, 'Thinking requested, not used')):
        ax.text(xc, -0.215, lab, transform=ax.get_xaxis_transform(), ha='center', va='top', fontsize=10, color=INK, fontweight='medium')
        ax.plot([xc - 0.85, xc + 0.85], [-0.19, -0.19], transform=ax.get_xaxis_transform(), color='#b9b8b2', lw=0.8, clip_on=False)
axes[0].set_ylabel('Recursive answers out of 20', fontsize=10, color=INK2)
from matplotlib.patches import Patch
fig.legend(handles=[Patch(color=BASE, label='No image'), Patch(color=HEART, label='Heart image, “looking at the image”')],
           loc='upper left', bbox_to_anchor=(0.004, 0.875), ncol=2, frameon=False, fontsize=10, labelcolor=INK2, handlelength=1.2, columnspacing=1.6)
fig.suptitle('Claude Opus 4.7: whether a heart means recursion depends on language, word order and the API call',
             x=0.012, y=0.975, ha='left', fontsize=12.5, color=INK, fontweight='semibold')
fig.text(0.012, 0.9, 'Recursive answers out of 20 per cell. One interleaved run of 320 calls, 12 November 2026.',
         ha='left', fontsize=9.5, color=INK2)
fig.subplots_adjust(left=0.065, right=0.985, top=0.74, bottom=0.2, wspace=0.06)
fig.savefig(out, dpi=200, facecolor=SURF)
print({k: rec[k] for k in sorted(rec)})
