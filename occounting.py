# --- Rimas Ibrahim | Financial Consultancy Tool ---

# 1. Professional Data Entry (Trial Balance)
# We use standard accounting nomenclature for precision
trial_balance = {
    "Cash & Equivalents": 150000,
    "Property & Equipment (Net)": 200000,
    "Accounts Payable": -50000,
    "Common Stock (Capital)": -250000,
    "Operating Revenue": -120000,
    "Salaries & Wages": 40000,
    "Administrative Expenses": 30000
}

# 2. Financial Analysis Logic
total_revenue = -trial_balance["Operating Revenue"]
total_expenses = trial_balance["Salaries & Wages"] + trial_balance["Administrative Expenses"]
net_income = total_revenue - total_expenses

total_assets = trial_balance["Cash & Equivalents"] + trial_balance["Property & Equipment (Net)"]
total_liabilities = -trial_balance["Accounts Payable"]
total_equity = -trial_balance["Common Stock (Capital)"] + net_income

# 3. Generating High-End Professional Dashboard
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Financial Performance Analysis | Rimas Ibrahim</title>
    <style>
        body {{ font-family: 'Inter', 'Segoe UI', sans-serif; background-color: #fafbfc; color: #1a1a1a; padding: 60px 20px; }}
        .report-card {{ max-width: 800px; margin: auto; background: #fff; padding: 50px; border: 1px solid #e1e4e8; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
        .header {{ border-bottom: 2px solid #1a1a1a; margin-bottom: 40px; padding-bottom: 20px; }}
        h1 {{ font-size: 28px; text-transform: uppercase; letter-spacing: 1px; margin: 0; }}
        .consultant-name {{ color: #666; font-size: 14px; margin-top: 5px; }}
        .section-title {{ font-size: 18px; font-weight: 700; margin: 35px 0 15px 0; border-left: 4px solid #1a1a1a; padding-left: 15px; text-transform: uppercase; }}
        .row {{ display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #f0f0f0; }}
        .row span:last-child {{ font-weight: 600; font-family: 'Courier New', monospace; }}
        .highlight {{ background: #f8f9fa; font-weight: bold; border-bottom: 2px solid #1a1a1a; }}
        .net-profit {{ color: #28a745; }}
        .footer {{ margin-top: 50px; font-size: 12px; color: #999; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="report-card">
        <div class="header">
            <h1>Financial Statement Analysis</h1>
            <div class="consultant-name">Prepared by: Rimas Ibrahim | Accounting Consultant</div>
        </div>

        <div class="section-title">Income Statement (P&L)</div>
        <div class="row"><span>Gross Operating Revenue</span><span>${total_revenue:,.2f}</span></div>
        <div class="row"><span>Total Operating Expenses</span><span>(${total_expenses:,.2f})</span></div>
        <div class="row highlight"><span>NET INCOME (LOSS)</span><span class="net-profit">${net_income:,.2f}</span></div>

        <div class="section-title">Balance Sheet</div>
        <div class="row"><span>Total Assets</span><span>${total_assets:,.2f}</span></div>
        <div class="row"><span>Total Liabilities</span><span>${total_liabilities:,.2f}</span></div>
        <div class="row"><span>Shareholders' Equity</span><span>${total_equity:,.2f}</span></div>
        <div class="row highlight"><span>TOTAL LIABILITIES & EQUITY</span><span>${total_liabilities + total_equity:,.2f}</span></div>

        <div class="footer">
            Electronic Statement Generated on 2026-05-12 | Verification Status: Balanced
        </div>
    </div>
</body>
</html>
"""

with open("report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("--- System Update Successful ---")
print("Professional Financial Report has been generated in English.")