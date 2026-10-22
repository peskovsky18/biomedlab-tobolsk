# -*- coding: utf-8 -*-
"""
Главный исполняемый скрипт сборки полного комплекта документов по кейсу Полины.
Создает идеально оформленный документ Word (programma_soprovozhdeniya_polina.docx)
в соответствии с ГОСТ (TNR 14, 1.5 интервал, абзац 1.25 см, выравнивание по ширине).
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

from section1_analysis import add_section_1
from section2_diagnostics import add_section_2
from section3_interaction import add_section_3
from section4_digital_product import add_section_4
from section5_reflection import add_section_5
from section6_presentation import add_section_6

def generate_full_program():
    print("Starting document assembly...")
    doc = docx.Document()

    # Page Setup: A4, standard academic margins
    sections = doc.sections
    for s in sections:
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(3.0)
        s.right_margin = Cm(1.5)

    # Document Header / Meta
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_meta.paragraph_format.first_line_indent = Cm(0)
    p_meta.paragraph_format.line_spacing = 1.15
    p_meta.paragraph_format.space_after = Pt(12)
    r = p_meta.add_run("Программа психолого-педагогического сопровождения\nОбразовательная организация: г. Тобольск, Тюменская область\nУчебный год: 2026/2027 (10 класс)\nДата составления: 22 октября 2026 г.")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = RGBColor(90, 90, 90)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.first_line_indent = Cm(0)
    p_title.paragraph_format.space_before = Pt(14)
    p_title.paragraph_format.space_after = Pt(8)
    p_title.paragraph_format.line_spacing = 1.15
    run_t = p_title.add_run("ПРОГРАММА ПСИХОЛОГО-ПЕДАГОГИЧЕСКОГО СОПРОВОЖДЕНИЯ\nПРОФЕССИОНАЛЬНОГО САМООПРЕДЕЛЕНИЯ ОБУЧАЮЩЕЙСЯ 10 КЛАССА\n«МАРШРУТ ВОЗМОЖНОСТЕЙ: ОТ ЕСТЕСТВЕННОНАУЧНОГО ИНТЕРЕСА К СУВЕРЕННОМУ ВЫБОРУ»")
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(15)
    run_t.bold = True
    run_t.font.color.rgb = RGBColor(0, 32, 96)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.first_line_indent = Cm(0)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run("(Индивидуальный кейс: Полина, 16 лет, 10 класс, г. Тобольск, Тюменская область)")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(13)
    run_sub.italic = True

    # AI Declaration
    p_ai = doc.add_paragraph()
    p_ai.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ai.paragraph_format.first_line_indent = Cm(1.25)
    p_ai.paragraph_format.space_after = Pt(14)
    p_ai.paragraph_format.line_spacing = 1.15
    run_ai_lbl = p_ai.add_run("Декларация об использовании технологий искусственного интеллекта: ")
    run_ai_lbl.font.name = 'Times New Roman'
    run_ai_lbl.font.size = Pt(11)
    run_ai_lbl.bold = True
    run_ai_txt = p_ai.add_run("В соответствии с регламентом аттестационной работы декларируется, что генеративные инструменты искусственного интеллекта применялись автором исключительно на предварительном этапе для агрегации статистических сведений и мониторинга региональных образовательных платформ Тюменской области. Концептуальный психолого-педагогический анализ случая, формулирование противоречий и целей, этическая диагностическая батарея с алгоритмами интерпретации и ветвления, медиативная переговорная технология «Семейный совет», авторский цифровой продукт («Интерактивный навигатор маршрутов») и рефлексивные карты разработаны автором самостоятельно.")
    run_ai_txt.font.name = 'Times New Roman'
    run_ai_txt.font.size = Pt(11)
    run_ai_txt.italic = True

    # Adding Sections
    print("Adding Section 1: Situation Analysis...")
    add_section_1(doc)

    print("Adding Section 2: Ethics & Diagnostics...")
    add_section_2(doc)

    print("Adding Section 3: Stakeholders Interaction...")
    add_section_3(doc)

    print("Adding Section 4: Digital Product...")
    add_section_4(doc)

    print("Adding Section 5: Reflection & Program Monitoring...")
    add_section_5(doc)

    print("Adding Section 6: Presentation Script & Defense Cases...")
    add_section_6(doc)

    output_filename = "programma_soprovozhdeniya_polina.docx"
    doc.save(output_filename)
    print(f"Document successfully created and saved as '{output_filename}'.")

if __name__ == "__main__":
    generate_full_program()
