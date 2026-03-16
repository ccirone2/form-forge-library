import stencils

# Choose a built-in theme: THEME_MODERN (default), THEME_CLASSIC, THEME_MINIMAL
stencils.set_theme(stencils.THEME_MODERN)

# Or create a custom theme:
# from docx.shared import RGBColor
# stencils.set_theme(stencils.DocTheme(
#     color_title=RGBColor(0x1B, 0x5E, 0x6E),
#     color_subtitle=RGBColor(0x3A, 0x7A, 0x8C),
#     color_muted=RGBColor(0x5A, 0x7A, 0x85),
#     color_footer=RGBColor(0x4D, 0x6E, 0x78),
#     color_accent=RGBColor(0x0D, 0x3D, 0x4A),
#     font_body="Segoe UI",
#     font_heading="Segoe UI Semibold",
#     font_caption="Segoe UI Semilight",
#     size_body=11, size_title=26,
#     size_heading1=16, size_heading2=13, size_heading3=12,
#     size_heading4=11, size_heading5=11, size_heading6=11,
#     size_subtitle=12, size_table=10, size_caption=9, size_footer=8,
#     margin_top=1.0, margin_bottom=0.75, margin_left=1.0, margin_right=1.0,
# ))


def generate_docx(data):
    doc = stencils.new_doc(data.get("title", "Document"))
    stencils.table_section(doc, "Form Data", [(k, v) for k, v in data.items()])
    stencils.footer(doc)
    return stencils.finalize(doc)
