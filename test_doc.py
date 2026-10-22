# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from builder_helper import (
    add_styled_paragraph, add_heading_1, add_heading_2, add_heading_3,
    style_table, set_cell_background, set_cell_margins
)

def build_document():
    doc = docx.Document()

    # Page Setup: A4, Margins 20mm (left 30mm for binding)
    sections = doc.sections
    for s in sections:
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(3.0)
        s.right_margin = Cm(1.5)

    # Title Area
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_meta.paragraph_format.first_line_indent = Cm(0)
    p_meta.paragraph_format.line_spacing = 1.15
    p_meta.paragraph_format.space_after = Pt(12)
    r = p_meta.add_run("Программа психолого-педагогического сопровождения\nОбразовательная организация: г. Тобольск, Тюменская область\nДата разработки: 22 октября 2026 г.")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = RGBColor(80, 80, 80)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.first_line_indent = Cm(0)
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(8)
    p_title.paragraph_format.line_spacing = 1.15
    run_t = p_title.add_run("ПРОГРАММА ПСИХОЛОГО-ПЕДАГОГИЧЕСКОГО СОПРОВОЖДЕНИЯ\nПРОФЕССИОНАЛЬНОГО САМООПРЕДЕЛЕНИЯ ОБУЧАЮЩЕЙСЯ 10 КЛАССА\n«МАРШРУТ ВОЗМОЖНОСТЕЙ: ОТ ЕСТЕСТВЕННОНАУЧНОГО ИНТЕРЕСА К СУВЕРЕННОМУ ВЫБОРУ»")
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(16)
    run_t.bold = True
    run_t.font.color.rgb = RGBColor(0, 32, 96)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.first_line_indent = Cm(0)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run("(Случай Полины, 16 лет, 10 класс, г. Тобольск, Тюменская область)")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(13)
    run_sub.italic = True

    # AI Declaration
    p_ai = doc.add_paragraph()
    p_ai.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ai.paragraph_format.first_line_indent = Cm(1.25)
    p_ai.paragraph_format.space_after = Pt(12)
    p_ai.paragraph_format.line_spacing = 1.15
    run_ai_lbl = p_ai.add_run("Декларация об использовании технологий искусственного интеллекта: ")
    run_ai_lbl.font.name = 'Times New Roman'
    run_ai_lbl.font.size = Pt(11)
    run_ai_lbl.bold = True
    run_ai_txt = p_ai.add_run("В соответствии с регламентом выполнения работы декларируется, что инструменты генеративного искусственного интеллекта привлекались автором на предварительном ориентировочном этапе исключительно для агрегации статистических сведений и мониторинга региональных образовательных платформ Тюменской области. Концептуальный психолого-педагогический анализ случая, диагностический инструментарий с критериями ветвления, технология медиативных переговоров с семьей, авторский цифровой продукт («Интерактивный навигатор») и система рефлексии разработаны автором самостоятельно.")
    run_ai_txt.font.name = 'Times New Roman'
    run_ai_txt.font.size = Pt(11)
    run_ai_txt.italic = True

    print("Document header and declaration created.")
    doc.save("programma_soprovozhdeniya_polina.docx")

if __name__ == "__main__":
    build_document()
