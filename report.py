import pandas as pd
from fpdf import FPDF

# Step 1: Read Data
df = pd.read_csv('data.csv')

# Step 2: Analyze Data
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
top_salesperson = df.loc[df['Sales'].idxmax(), 'Name']

# Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum().to_dict()

# Step 3: Generate PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Sales Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDFReport()
pdf.add_page()

# Add Summary
pdf.chapter_title('Summary')
summary_text = (
    f"Total Sales: ${total_sales:.2f}\n"
    f"Average Sales: ${average_sales:.2f}\n"
    f"Highest Sales: ${max_sales:.2f} by {top_salesperson}\n"
)
pdf.chapter_body(summary_text)

# Add Sales by Region
pdf.chapter_title('Sales by Region')
for region, sales in sales_by_region.items():
    pdf.cell(0, 10, f"{region}: ${sales:.2f}", 0, 1)

# Save PDF
pdf.output('sales_report.pdf')
print("PDF report generated as 'sales_report.pdf'")
