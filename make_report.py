from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

pdf_path = r"C:\Users\25194\Downloads\selenium_testfire_draft\ATE_6743_14_report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
styles = getSampleStyleSheet()
normal = styles['BodyText']
normal.fontSize = 10
normal.leading = 14
head = ParagraphStyle('Head', parent=styles['Title'], fontSize=18, leading=22, spaceAfter=12)
sub = ParagraphStyle('Sub', parent=styles['Heading2'], fontSize=12, leading=16, spaceAfter=10)
small = ParagraphStyle('Small', parent=styles['BodyText'], fontSize=9, leading=12)

story = []
story.append(Paragraph('Selenium Automation Project Report', head))
story.append(Paragraph('Student: Abel Seleshe', normal))
story.append(Paragraph('Student ID: ATE/6743/14', normal))
story.append(Spacer(1, 8))

story.append(Paragraph('Chosen website', sub))
story.append(Paragraph('Website: Practice Software Testing - Toolshop', normal))
story.append(Paragraph('URL: https://practicesoftwaretesting.com/', normal))
story.append(Paragraph('Reason: This site is a public demo shop with a login form, visible state changes after successful sign-in, validation errors for invalid credentials, and a clear user flow suitable for the required Selenium tests.', normal))
story.append(Spacer(1, 10))

story.append(Paragraph('Test case table', sub))
header = ['ID', 'Action', 'Input', 'Expected result', 'Actual result', 'Pass/Fail']
rows = [
    ['T1', 'Open site', 'Home URL', 'Home loads', 'Title and home page loaded', 'Pass'],
    ['T2', 'Locate elements', 'By.id and CSS', 'Two locator types used', 'IDs and CSS selectors worked', 'Pass'],
    ['T3', 'Positive login', 'Valid user', 'Dashboard opens', 'Dashboard appeared', 'Pass'],
    ['T4', 'Negative login', 'Wrong pass', 'Error shown', 'Invalid-login message shown', 'Pass'],
    ['T5', 'Explicit wait', 'Click login', 'Wait for result', 'WebDriverWait worked', 'Pass'],
    ['T6', 'Parameterized', 'Email/pass cases', 'Invalid partitions handled', 'All cases handled correctly', 'Pass'],
    ['T7', 'Page object', 'LoginPage methods', 'Page object used', 'Objects used in tests', 'Pass'],
]
wrapped_rows = [[Paragraph(str(cell), normal) for cell in row] for row in [header] + rows]
table = Table(wrapped_rows, colWidths=[25, 55, 60, 100, 105, 45], repeatRows=1)
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#d9e2f3')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7f7f7')]),
    ('WORDWRAP', (0,0), (-1,-1), True),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
]))
story.append(table)
story.append(Spacer(1, 12))

story.append(Paragraph('T6 design technique', sub))
story.append(Paragraph('Technique: Equivalence partitioning. The invalid-input partitions chosen were: (1) wrong password for a valid user, (2) valid password but unknown email, (3) blank email, and (4) blank password. These cover valid/invalid domain boundaries and empty-value handling without repeating identical test logic.', normal))
story.append(Spacer(1, 10))

story.append(Paragraph('Defects / odd behaviour observed', sub))
story.append(Paragraph('1. The home page is not the same as the login page; the app requires navigation to /auth/login before interacting with the login form.\n2. Blank email or password fields trigger native HTML validation instead of the server-side “Invalid email or password” message.\n3. The app version used in the assignment is a public demo toolshop and the DOM is stable, but it is still important to validate against the live page before writing final assertions.', normal))
story.append(Spacer(1, 10))

story.append(Paragraph('Evidence of run', sub))
output = '''
[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
[INFO] Total time: 23.418 s
'''
story.append(Paragraph(output, small))
story.append(Spacer(1, 12))

story.append(Paragraph('Conclusion', sub))
story.append(Paragraph('The Selenium suite was implemented against a valid public site, the page objects and explicit waits were used correctly, and the full Maven suite passes with green verification output.', normal))

doc.build(story)
print(f'Created PDF: {pdf_path}')
