"""Put the QuantumBeat app inside the team's deck (no website needed).

usage: python3 make_deck.py <duplicated.pptx> <out.pptx> <app-demo.mp4> <poster.jpg> <shots_dir>

<duplicated.pptx> is the original deck after the pptx skill's add_slide.py copied slide 11
into position 12, so the new slide keeps the template's header, pill, boxes and footer.

Result:
  slide 12  'Try Our QuantumBeat App': app demo video + info boxes + "open the app" link to slide 13
  slide 13  the real app, ready; tapping 'Run sample scan' (in Slide Show) goes to slide 14
  slide 14  the app scanning; advances by itself after 0.9 s
  slide 15  the app's result
Slide 11 points to slide 12, and every footer is renumbered.
"""
import json
import sys
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

src, out, video, poster, shots = sys.argv[1:6]
shots = Path(shots)
hot = json.loads((shots / 'hotspot.json').read_text())

prs = Presentation(src)
SW, SH = prs.slide_width, prs.slide_height
slides = list(prs.slides)
new = slides[11]          # copy of slide 11, now at position 12
s11 = slides[10]
PURPLE = RGBColor(0x73, 0x57, 0xD6)
CYAN = RGBColor(0x43, 0xD9, 0xE6)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def by_name(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    raise KeyError(name)


def set_text(shape, text):
    """Replace a shape's text but keep the first run's formatting."""
    tf = shape.text_frame
    p0 = tf.paragraphs[0]
    for extra in tf.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)
    runs = p0.runs
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    runs[0].text = text
    return runs[0]


def add_transition(slide, adv_ms=None):
    """Fade transition; optionally auto-advance after adv_ms (works in Slide Show)."""
    el = slide._element
    old = el.find(qn('p:transition'))
    if old is not None:
        el.remove(old)
    tr = etree.Element(qn('p:transition'))
    tr.set('spd', 'fast')
    if adv_ms is not None:
        tr.set('advTm', str(adv_ms))
    etree.SubElement(tr, qn('p:fade'))
    # schema order: cSld, clrMapOvr, transition, timing, extLst
    anchor = el.find(qn('p:clrMapOvr'))
    if anchor is None:
        anchor = el.find(qn('p:cSld'))
    anchor.addnext(tr)


def pill(slide, text, left, top, width, height, name, size=13):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shp.name = name
    shp.adjustments[0] = 0.5
    shp.fill.solid(); shp.fill.fore_color.rgb = PURPLE
    shp.line.fill.background()
    shp.shadow.inherit = False
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = Inches(0.12); tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = True; r.font.color.rgb = WHITE; r.font.name = 'Calibri'
    return shp


def move_slide(prs, old_index, new_index):
    lst = prs.slides._sldIdLst
    el = list(lst)[old_index]
    lst.remove(el)
    lst.insert(new_index, el)


# ---- the three app screens (added at the end, then moved after slide 12) --------------
blank = next(l for l in prs.slide_layouts if l.name == 'Blank')
app_slides = []
for fname, alt in [('app-1-ready.jpg', 'QuantumBeat app, ready to run a sample scan'),
                   ('app-2-processing.jpg', 'QuantumBeat app processing a sample scan'),
                   ('app-3-result.jpg', 'QuantumBeat app result: 72 BPM, 34 beat gaps, 3 flagged')]:
    s = prs.slides.add_slide(blank)
    for ph in list(s.placeholders):
        ph._element.getparent().remove(ph._element)
    pic = s.shapes.add_picture(str(shots / fname), 0, 0, SW, SH)
    pic.name = 'app-screen'
    pic._element.nvPicPr.cNvPr.set('descr', alt)
    app_slides.append(s)
ready, scanning, result = app_slides

# tappable outline over the app's own "Run sample scan" button -> scanning screen
vw, vh = hot['viewport']; b = hot['button']
bx, by, bw, bh = (int(SW * b['x'] / vw), int(SH * b['y'] / vh), int(SW * b['width'] / vw), int(SH * b['height'] / vh))
pad = Inches(0.06)
ring = ready.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx - pad, by - pad, bw + 2 * pad, bh + 2 * pad)
ring.name = 'run-scan-hotspot'
ring.adjustments[0] = 0.3
ring.fill.solid(); ring.fill.fore_color.rgb = CYAN
fill_clr = ring.fill._xPr.find(qn('a:solidFill'))[0]
etree.SubElement(fill_clr, qn('a:alpha')).set('val', '1000')   # ~invisible fill, still tappable
ring.line.color.rgb = WHITE; ring.line.width = Pt(2.25)
ring.shadow.inherit = False
ring.click_action.target_slide = scanning
pill(ready, 'Tap “Run sample scan” to try the app  →', Inches(5.0), Inches(0.36), Inches(4.3), Inches(0.42), 'hint-pill')
pill(result, 'Scan complete: 3 unusual beat gaps flagged', Inches(5.0), Inches(0.36), Inches(4.3), Inches(0.42), 'result-pill')
add_transition(ready)
add_transition(scanning, adv_ms=900)
add_transition(result)
n = len(prs.slides)
for k in range(3):
    move_slide(prs, n - 3 + k, 12 + k)

# ---- slide 12 content -----------------------------------------------------------------
T = {
    'title-11': 'Try Our QuantumBeat App',
    'question-11': 'How does our app show QuantumBeat in action?',
    'demo-subtitle': 'Our web app, built into the next three slides',
    'demo-1-label': 'WHAT IT IS',
    'demo-1-prompt': 'A web app our team built to demo the idea',
    'demo-2-label': 'TRY IT YOURSELF',
    'demo-3-label': 'WHAT IT DOES',
    'demo-3-prompt': 'Measures beat gaps, flags z-scores above 1.5',
    'demo-4-label': 'SAMPLE RESULT',
    'demo-4-prompt': '72 BPM · 34 beat gaps · 3 gaps flagged',
    'demo-5-label': 'LIMITATIONS',
    'demo-5-prompt': 'Synthetic data only. Not a diagnosis.',
    'demo-note': 'In Slide Show (press Play), tap the video to watch a sample scan, or tap “Open the app” '
                 'to use it on the next slide. No internet needed.',
}
for name, text in T.items():
    set_text(by_name(new, name), text)
link_run = set_text(by_name(new, 'demo-2-prompt'), 'Open the app (next slide)  →')
link_run.font.underline = True
link_run.font.bold = True
link_run.font.color.rgb = PURPLE
by_name(new, 'demo-2-prompt').click_action.target_slide = ready
by_name(new, 'demo-2-box').click_action.target_slide = ready

for sh in new.shapes:
    if sh.name.endswith('-11'):
        sh.name = sh.name[:-3] + '-12'

# swap the simulation picture for the app demo video (16:9, centred in the visual box)
pic = by_name(new, 'Picture 38')
rId = pic._element.blipFill.blip.rEmbed
pic._element.getparent().remove(pic._element)
new.part.drop_rel(rId)
box = by_name(new, 'demonstration-visual-box')
h = box.height - Inches(0.24)
w = int(h * 16 / 9)
movie = new.shapes.add_movie(video, box.left + (box.width - w) // 2, box.top + (box.height - h) // 2, w, h,
                             poster_frame_image=poster, mime_type='video/mp4')
movie.name = 'app-demo-video'

# slide 11 points to the app slide
set_text(by_name(s11, 'demo-5-prompt'), 'Live app demo on the next slide (slide 12)')

# ---- renumber every footer "NN / total" ------------------------------------------------
total = len(prs.slides)
for i, slide in enumerate(prs.slides, start=1):
    for sh in slide.shapes:
        if sh.name.startswith('footer-num') and sh.has_text_frame:
            set_text(sh, f'{i:02d} / {total}')

prs.save(out)
print('saved', out, 'slides:', total)
