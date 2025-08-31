from pathlib import Path
import os
import sys
import traceback

from pypdf import PdfWriter
from pypdf.constants import PageLabelStyle


def wrap(f):
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            traceback.print_stack(file=sys.stderr)
            print(f"\033[91m{e}\033[0m", file=sys.stderr)
    return wrapped


@wrap
def writeFullScore():
    writer = PdfWriter()
    writer.append("01 - Full score - Soir sur la plaine.pdf")
    writer.append(
        "01 - Full score alt ending - Soir sur la plaine.pdf", pages=(28, 29))
    writer.append("soir_plaine_commentary.pdf")
    # writer.append(notes_file)
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("Full Score", 2)
    writer.add_outline_item("Editorial Commentary", 28)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Instrumentation")
    writer.set_page_label(2, 29, style=PageLabelStyle.DECIMAL)
    writer.write("Lili Boulanger - Soir sur la plaine pour orchestre.pdf")


@wrap
def writeReduction(coverNumber: int, withAlternateEnding: bool):
    writer = PdfWriter()
    letter = ["A", "B"][coverNumber]
    writer.append("02 - ReductionCover - Soir sur la plaine.pdf",
                  [coverNumber, 2])
    lastPage = 20
    pages = list(range(0, 19))
    if withAlternateEnding:
        pages.append(21)
        lastPage += 1
    writer.append(f"02 - Reduction{letter} - Soir sur la plaine.pdf", pages)
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("Reduction", 2)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Foreword")
    writer.set_page_label(2, lastPage, style=PageLabelStyle.DECIMAL)
    writer.write("Lili Boulanger - Soir sur la plaine pour orchestre, "
                 f"réduction version {letter}.pdf")

@wrap
def setPageLayout(filename: str, rightLayout: bool):
    writer = PdfWriter(Path(filename))
    writer.set_page_layout("/TwoPageRight" if rightLayout else "/TwoPageLeft")
    writer.write(filename)


def main():
    print("Processing Full Score")
    writeFullScore()
    print("Processing Reduction A")
    writeReduction(0, True)
    print("Processing Reduction B")
    writeReduction(1, False)
    for partFilename in os.listdir("parts_output"):
        if not partFilename.endswith("pdf"):
            continue
        print(f'Processing Part "{partFilename}"')
        setPageLayout(f"parts_output/{partFilename}", "Harpe 1" not in partFilename)


if __name__ == "__main__":
    main()
