import json
from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent.parent


def export_html_report(company_profile, score_summary, questions, recommendations, scenario=None, filename="assessment_report.html"):
    items = questions["items"]
    html = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='utf-8'><title>Industry 5.0 SME Readiness Report</title>",
        "<style>body{font-family:Arial,sans-serif; margin:24px; color:#1f2937;} h1,h2,h3{color:#0f172a;} .card{border:1px solid #dbe4f0; padding:16px; border-radius:8px; margin-bottom:16px;} table{border-collapse:collapse; width:100%;} td,th{padding:8px; border:1px solid #dbe4f0; text-align:left;} .meta{color:#475569;}</style>",
        "</head><body>",
        f"<h1>Industry 5.0 SME Readiness Assessment Report</h1>",
        f"<div class='card'><h2>Executive Summary</h2><p><strong>Company:</strong> {company_profile.get('company_name', 'Not provided')}</p>",
        f"<p><strong>Industry:</strong> {company_profile.get('industry', 'Not provided')} | <strong>Size:</strong> {company_profile.get('company_size', 'Not provided')}</p>",
        f"<p><strong>Assessment date:</strong> {company_profile.get('assessment_date', 'Not provided')}</p>",
        f"<p><strong>Overall maturity score:</strong> {score_summary.get('overall_score', 0):.2f} | <strong>Maturity level:</strong> {score_summary.get('maturity_level', 'N/A')}</p></div>",
        "<div class='card'><h2>Top Recommendations</h2><ul>",
    ]
    for rec in recommendations[:5]:
        html.append(f"<li><strong>{rec['construct']}</strong>: {rec['suggested_action']}</li>")
    html.append("</ul></div>")
    if scenario:
        html.append(f"<div class='card'><h2>What-if Scenario</h2><p>New overall score: {scenario['overall_score']:.2f}; change: {scenario['change']:.2f}</p></div>")

    html.append("<div class='card'><h2>Question Summary</h2><table><tr><th>ID</th><th>Dimension</th><th>Construct</th><th>Score</th></tr>")
    for item in items:
        score = score_summary.get('scores', {}).get(item['id'], 0)
        html.append(f"<tr><td>{item['id']}</td><td>{item['dimension']}</td><td>{item['construct']}</td><td>{score}</td></tr>")
    html.append("</table></div>")
    html.append("<div class='card'><h2>Methodology</h2><p>The software is research-informed and uses a seven-dimension maturity model based on Latino (2025), with project-specific extensions for evidence capture, dashboards, sensitivity analysis, and a decision-support roadmap.</p>")
    html.append("<p>Research-derived framework: [RESEARCH-DERIVED]. Project features: [PROJECT EXTENSION].</p></div>")
    html.append("</body></html>")
    path = ROOT / filename
    path.write_text("\n".join(html), encoding="utf-8")
    return str(path)


def export_pdf_report(company_profile, score_summary, questions, recommendations, filename="assessment_report.pdf"):
    path = ROOT / filename
    doc = SimpleDocTemplate(str(path), pagesize=A4, title="Industry 5.0 SME Readiness Report")
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph("Industry 5.0 SME Readiness Assessment Report", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Company: {company_profile.get('company_name', 'Not provided')}", styles['Normal']))
    story.append(Paragraph(f"Industry: {company_profile.get('industry', 'Not provided')}", styles['Normal']))
    story.append(Paragraph(f"Overall Score: {score_summary.get('overall_score', 0):.2f}", styles['Normal']))
    story.append(Paragraph(f"Maturity Level: {score_summary.get('maturity_level', 'N/A')}", styles['Normal']))
    story.append(Spacer(1, 12))
    table_data = [["Construct", "Priority", "Action"]]
    for rec in recommendations[:5]:
        table_data.append([rec["construct"], rec["priority"], rec["suggested_action"]])
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0f172a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dbe4f0')),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))
    doc.build(story)
    return str(path)


def export_assessment_bundle(company_profile, score_summary, questions, recommendations, scenario=None):
    html_path = export_html_report(company_profile, score_summary, questions, recommendations, scenario=scenario, filename="assessment_report.html")
    pdf_path = export_pdf_report(company_profile, score_summary, questions, recommendations, filename="assessment_report.pdf")
    return {"html": html_path, "pdf": pdf_path}
