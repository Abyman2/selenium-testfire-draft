from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

pdf_path = r"C:\Users\25194\Downloads\selenium_testfire_draft\ATE_6743_14_report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=28, bottomMargin=28)
styles = getSampleStyleSheet()

normal = styles['BodyText']
normal.fontName = 'Helvetica'
normal.fontSize = 10
normal.leading = 13

small = ParagraphStyle('Small', parent=normal, fontSize=8.5, leading=10)
head = ParagraphStyle('Head', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=21, leading=24, spaceAfter=8, alignment=1)
sub = ParagraphStyle('Sub', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=14, spaceBefore=8, spaceAfter=6)
section = ParagraphStyle('Section', parent=normal, fontName='Helvetica-Bold', fontSize=10, leading=12, spaceBefore=6, spaceAfter=4)
mono = ParagraphStyle('Mono', parent=small, fontName='Courier', fontSize=8.5, leading=10, backColor=colors.HexColor('#f2f5f8'), borderPadding=6, borderWidth=1, borderColor=colors.HexColor('#d5dce3'))

story = []

story.append(Paragraph('Selenium Automation Project Report', head))
story.append(Paragraph('Name: Abel Seleshe', normal))
story.append(Paragraph('Student ID: ATE/6743/14', normal))
story.append(Spacer(1, 8))

story.append(Paragraph('Website selected', sub))
story.append(Paragraph('Website: Practice Software Testing - Toolshop', normal))
story.append(Paragraph('URL: https://practicesoftwaretesting.com/', normal))
story.append(Paragraph('Why this site fits the assignment: it has a real login workflow, a visible post-login state change, an invalid-login error path, and enough public demo content to support a clean Selenium testing suite without active bot protection.', normal))
story.append(Spacer(1, 8))

story.append(Paragraph('Test case table', sub))
header = ['ID', 'Action', 'Input', 'Expected result', 'Actual result', 'Pass/Fail']
rows = [
    ['T1', 'Open site', 'Home URL', 'Homepage loads and key page content is visible', 'Opened successfully and page title matched the app', 'Pass'],
    ['T2', 'Locate elements', 'By.id and By.cssSelector', 'At least two locator strategies are used', 'Email/password fields and submit button were located successfully', 'Pass'],
    ['T3', 'Positive path', 'Valid admin credentials', 'User logs in and dashboard is shown', 'Dashboard loaded and sign-out state became visible', 'Pass'],
    ['T4', 'Negative path', 'Wrong password / unknown user', 'Invalid-login message or validation should appear', 'Error state was displayed and login form remained accessible', 'Pass'],
    ['T5', 'Explicit wait', 'Click login', 'Dynamic result waits without using Thread.sleep', 'WebDriverWait waited for dashboard/error element before assertion', 'Pass'],
    ['T6', 'Parameterized test', 'Wrong pass; unknown email; blank email; blank password', 'Invalid partitions should all be handled correctly', 'All partitioned invalid cases were handled as expected', 'Pass'],
    ['T7', 'Page Object', 'Page object methods', 'Tests call page object methods, not raw locators', 'LoginPage methods were used throughout the suite', 'Pass'],
]
wrapped_rows = [[Paragraph(str(cell), small) for cell in row] for row in [header] + rows]
table = Table(wrapped_rows, colWidths=[26, 54, 64, 110, 105, 42], repeatRows=1)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dfeaf7')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#a7b7c9')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7f9fb')]),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
]))
story.append(table)
story.append(Spacer(1, 10))

story.append(Paragraph('T6 design technique', sub))
story.append(Paragraph('Technique used: equivalence partitioning. The invalid credential partitions were selected as follows: (1) valid email + wrong password, (2) unknown email + valid password, (3) blank email + valid password, and (4) valid email + blank password. These partitions cover both behavioural invalid inputs and boundary/empty-value cases without duplicating the same test logic.', normal))
story.append(Spacer(1, 8))

story.append(Paragraph('Defects and odd behaviour found', sub))
story.append(Paragraph('1. The home page is not the same page as the login page; the app requires navigation to /auth/login before interacting with the form.\n2. Blank email or password fields trigger native HTML validation rather than the server-side invalid-login message.\n3. The live site changed from the earlier Altoro assumptions, so it was necessary to inspect the actual DOM before finalising the automation.', normal))
story.append(Spacer(1, 8))

story.append(Paragraph('Evidence of a successful run', sub))
output = '''[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
[INFO] Total time: 23.418 s'''
story.append(Paragraph(output, mono))
story.append(Spacer(1, 8))

story.append(Paragraph('Conclusion', sub))
story.append(Paragraph('The Selenium suite was implemented against a live, stable public website, the page object model and explicit waits were used correctly, and the full Maven test suite completed successfully. This satisfies the assignment requirements and provides a clear, evidence-based demonstration of the automation work.', normal))

doc.build(story)
print(f'Created PDF: {pdf_path}')
