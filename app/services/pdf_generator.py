import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from datetime import datetime

def generate_pdf_report(
    topic,
    synthesis,
    geopolitical,
    technical,
    risk,
    sources
):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/report_{datetime.utcnow().timestamp()}.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story = []

    # TITLE
    title = f"P3XK4D0R Intelligence Briefing"

    story.append(
        Paragraph(title, styles["Title"])
    )

    story.append(Spacer(1, 20))

    # TOPIC
    story.append(
        Paragraph(f"<b>Topic:</b> {topic}", styles["BodyText"])
    )

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.utcnow()}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # EXEC SUMMARY
    story.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    clean_synthesis = (
        synthesis
        .replace("\\n", "<br/>")
    )

    story.append(
            Paragraph(clean_synthesis, styles["BodyText"])
    )

    story.append(Spacer(1, 20))

    # GEO
    
    story.append(
        Paragraph(
            "Geopolitical Analysis",
            styles["Heading1"]
        )
    )

    clean_GA = (
        geopolitical
        .replace("\\n", "<br/>")
    )

    story.append(
        Paragraph(clean_GA, styles["BodyText"])
    )

    story.append(Spacer(1, 20))

    # TECH

    story.append(
        Paragraph(
            "Technical Analysis",
            styles["Heading1"]
        )
    )

    clean_TE = (
        technical
        .replace("\\n", "<br/>")
    )

    story.append(
        Paragraph(clean_TE, styles["BodyText"])
    )

    story.append(Spacer(1, 20))

    # RISK
    
    story.append(
        Paragraph(
            "Risk Assessment",
            styles["Heading1"]
        )
    )

    clean_RI = (
        risk
        .replace("\\n", "<br/>")
    )

    story.append(
        Paragraph(clean_RI, styles["BodyText"])
    )

    story.append(Spacer(1, 20))

    # SOURCES
    
    story.append(
        Paragraph(
            "Sources",
            styles["Heading1"]
        )
    )

    for source in sources:

        url = source.get("url", "")

        story.append(
            Paragraph(url, styles["BodyText"])
        )

    doc.build(story)

    return filename