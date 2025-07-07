from pypdf import PdfWriter
from pypdf.constants import PageLabelStyle

score_file = "01 - Full score - Soir sur la plaine.pdf"
alternate_ending_file = "01 - Full score alt ending - Soir sur la plaine.pdf"
# notes_file = "tailleferre_harp_concertino_commentary.pdf"
output_file = "Lili Boulanger - Soir sur la plaine pour orchestre.pdf"

def main():
    writer = PdfWriter()
    writer.append(score_file)
    writer.append(alternate_ending_file, pages=(28, 29))
    # writer.append(notes_file)
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("Full Score", 2)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Instrumentation")
    writer.set_page_label(2, 28, style=PageLabelStyle.DECIMAL)
    writer.write(output_file)

if __name__ == "__main__":
    main()