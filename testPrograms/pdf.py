# from reportlab.pdfgen import canvas

# def create_pdf(data):
#   """
#   Creates a PDF with the given data.

#   Args:
#     data: A dictionary containing data to be added to the PDF.
#   """
#   c = canvas.Canvas("data_pdf.pdf")

#   # Add title and other elements based on data
#   c.drawString(100, 750, f"Title: {data['title']}")
#   c.drawString(100, 700, f"Description: {data['description']}")

#   # Add other elements like images, tables, etc. using appropriate methods

#   c.save()

# if __name__ == "__main__":
#   data = {
#     "title": "My Report",
#     "description": "This is a sample report generated with Python."
#   }
#   create_pdf(data)




from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_bill_pdf(data):
  """
  Creates a bill PDF with the given data.

  Args:
    data: A dictionary containing bill information.
  """
  c = canvas.Canvas("bill.pdf")

  # Company information
  c.setFont("Helvetica", 16)
  c.drawString(inch, 7.5 * inch, data["company_name"])
  c.drawString(inch, 7 * inch, f"Address: {data['company_address']}")
  c.drawString(inch, 6.5 * inch, f"Phone: {data['company_phone']}")

  # Bill details
  c.setFont("Helvetica-Bold", 14)
  c.drawString(6 * inch, 7.5 * inch, "Bill")
  c.setFont("Helvetica", 12)
  c.drawString(6 * inch, 7 * inch, f"Bill number: {data['bill_number']}")
  c.drawString(6 * inch, 6.5 * inch, f"Date: {data['date']}")
  c.drawString(6 * inch, 6 * inch, f"Due date: {data['due_date']}")

  # Customer information
  c.setFont("Helvetica-Bold", 12)
  c.drawString(inch, 5.5 * inch, "Bill To:")
  c.setFont("Helvetica", 10)
  c.drawString(inch, 5 * inch, f"{data['customer_name']}")
  c.drawString(inch, 4.5 * inch, f"{data['customer_address']}")

  # Itemized list
  y_pos = 4 * inch
  c.setFont("Helvetica-Bold", 10)
  c.drawString(inch, y_pos, "Description")
  c.drawString(3 * inch, y_pos, "Quantity")
  c.drawString(4.5 * inch, y_pos, "Unit Price")
  c.drawString(6 * inch, y_pos, "Total")
  y_pos -= 0.2 * inch
  c.line(inch, y_pos, 6 * inch, y_pos)

  for item in data["items"]:
    c.setFont("Helvetica", 10)
    c.drawString(inch, y_pos - 0.2 * inch, item["description"])
    c.drawString(3 * inch, y_pos - 0.2 * inch, str(item["quantity"]))
    c.drawString(4.5 * inch, y_pos - 0.2 * inch, f"{item['unit_price']:.2f}")
    c.drawString(6 * inch, y_pos - 0.2 * inch, f"{item['total']:.2f}")
    y_pos -= 0.2 * inch

  # Summary
  c.setFont("Helvetica-Bold", 12)
  c.drawString(inch, y_pos - 0.5 * inch, "Subtotal:")
  c.drawString(6 * inch, y_pos - 0.5 * inch, f"{data['subtotal']:.2f}")
  c.drawString(inch, y_pos - 1 * inch, "Taxes:")
  c.drawString(6 * inch, y_pos - 1 * inch, f"{data['taxes']:.2f}")
  c.setFont("Helvetica-Bold", 14)
  c.drawString(inch, y_pos - 1.5 * inch, "Total:")
  c.drawString(6 * inch, y_pos - 1.5 * inch, f"{data['total']:.2f}")

  # Payment instructions
  c.setFont("Helvetica", 10)
  c.drawString(inch, y_pos - 2.5 * inch, "Payment instructions:")
  c.drawString(inch, y_pos - 3 * inch, f"{data['payment_instructions']}")

  c.save()

if __name__ == "__main__":
  bill_data = {
    "company_name": "Your Company Name",
    "company_address": "Your Company Address",
    "company_phone": "Your Company Phone",
    "bill_number":1,
    "date":1/1/20,
    "due_date":2/1/20,
    "customer_name":"hello",
    "customer_address":"sdjb",
    "items":[
      {"description":"abc","quantity":24,"unit_price":10,"total":240}
      ],
    "payment_instructions":"card",
    "subtotal":12.33,
    "taxes":10,
    "total":102.00,
  }
  create_bill_pdf(bill_data)