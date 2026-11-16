"""Add a 'Try Our QuantumBeat App' slide after slide 11 of the team's deck.

usage: python3 make_deck.py <duplicated.pptx> <out.pptx> <app-demo.mp4> <poster.jpg>

<duplicated.pptx> is the original deck after skills' add_slide.py has copied slide 11
into position 12, so the new slide keeps the template's header, pill, boxes and footer.
"""
import sys
from pptx import Presentation
from pptx.util import Inches

src, out, video, poster = sys.argv[1:5]
prs = Presentation(src)
slides = list(prs.slides)
total = len(slides)
new = slides[11]          # the copy of slide 11, now at position 12
s11 = slides[10]


def by_name(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    raise KeyError(name)


def set_text(shape, text, link=None):
    """Replace a shape's text but keep the first run's formatting."""
    tf = shape.text_frame
    p0 = tf.paragraphs[0]
    for extra in tf.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)
    runs = p0.runs
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    runs[0].text = text
    if link:
        runs[0].hyperlink.address = link


# ---- new slide content -------------------------------------------------------
T = {
    'title-11': 'Try Our QuantumBeat App',
    'question-11': 'How does our app show QuantumBeat in action?',
    'demo-subtitle': 'Interactive web app · works offline in any web browser',
    'demo-1-label': 'WHAT IT IS',
    'demo-1-prompt': 'A web app our team built to demo the idea',
    'demo-2-label': 'HOW TO OPEN IT',
    'demo-3-label': 'WHAT IT DOES',
    'demo-3-prompt': 'Measures beat gaps, flags z-scores above 1.5',
    'demo-4-label': 'SAMPLE RESULT (IN THE VIDEO)',
    'demo-4-prompt': '72 BPM · 34 beat gaps · 3 gaps flagged',
    'demo-5-label': 'LIMITATIONS',
    'demo-5-prompt': 'Synthetic data only. Not a diagnosis.',
    'demo-note': 'Click the video to watch the app run a sample scan. To use the app live, keep '
                 'QuantumBeat_App.html in the same folder as this presentation.',
}
for name, text in T.items():
    set_text(by_name(new, name), text)
set_text(by_name(new, 'demo-2-prompt'), 'Click here: QuantumBeat_App.html', link='QuantumBeat_App.html')

# rename the copied shapes so the new slide's objects are not called "...-11"
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
left = box.left + (box.width - w) // 2
top = box.top + (box.height - h) // 2
movie = new.shapes.add_movie(video, left, top, w, h, poster_frame_image=poster, mime_type='video/mp4')
movie.name = 'app-demo-video'

# slide 11 now points to the app slide
set_text(by_name(s11, 'demo-5-prompt'), 'Live app demo on the next slide (slide 12)')

# ---- renumber every footer "NN / total" ---------------------------------------
for i, slide in enumerate(prs.slides, start=1):
    for sh in slide.shapes:
        if sh.name.startswith('footer-num') and sh.has_text_frame:
            set_text(sh, f'{i:02d} / {total}')

prs.save(out)
print('saved', out, 'slides:', total)
