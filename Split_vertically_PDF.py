import PyPDF2
import copy

input_file = "かなでるからだ.pdf"  # 見開き原稿
output_file = "かなでるからだ_split.pdf"  # 分割したPDFの保存

pdf_reader = PyPDF2.PdfReader(input_file)
pdf_writer = PyPDF2.PdfWriter()

for i in range(len(pdf_reader.pages)):
    p1 = pdf_reader.pages[i]
    p2 = copy.copy(p1)

    x0, y0 = map(float, p1.mediabox.lower_left)
    x1, y1 = map(float, p1.mediabox.upper_right)

    p1_lower_left = (x0, y0)
    # 右寄せに調整（ここでは中央から右側に3%の位置に分割）　中央分割の時は0.5
    p1_upper_right = (x1 - 0.47 * (x1 - x0), y1)
    # 右寄せに調整（ここでは中央から右側に3%の位置に分割）
    p2_lower_left = (x1 - 0.47 * (x1 - x0), y0)
    p2_upper_right = (x1, y1)

    if abs(y1 - y0) > abs(x1 - x0):
        p1_upper_right = (x1, (y0 + y1) / 2)
        p2_lower_left = (x0, (y0 + y1) / 2)

    p1.cropbox.lower_left = p1_lower_left
    p1.cropbox.upper_right = p1_upper_right
    p2.cropbox.lower_left = p2_lower_left
    p2.cropbox.upper_right = p2_upper_right

    if abs(y1 - y0) > abs(x1 - x0):
        p1, p2 = p2, p1

    pdf_writer.add_page(p1)
    pdf_writer.add_page(p2)

with open(output_file, mode="wb") as f:
    pdf_writer.write(f)
