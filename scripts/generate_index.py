from pathlib import Path


class IndexBuilder:

    def __init__(self):

        self.root = Path.cwd()
        self.site = self.root / "_site"
        self.output_file = self.site / "index.html"

    # -------------------------
    # TROVA ARTICOLI
    # -------------------------

    def get_articles(self):

        if not self.site.exists():
            return []

        return [
            f for f in self.site.glob("*.html")
            if f.name != "index.html"
        ]

    # -------------------------
    # CREA INDEX HTML
    # -------------------------

    def build_index(self, articles):

        items = ""

        for a in articles:

            title = a.stem.replace("-", " ").title()

            items += f"""
            <li style="margin:10px 0;">
                <a href="{a.name}">{title}</a>
            </li>
            """

        return f"""
<!doctype html>
<html lang="it">
<head>
    <meta charset="utf-8">
    <title>Lingue-Fluente</title>
</head>

<body style="max-width:700px;margin:auto;font-family:Arial;line-height:1.6">

    <h1>📚 Lingue-Fluente</h1>

    <p>Impara le lingue in modo semplice e costante.</p>

    <h2>Articoli</h2>

    <ul>
        {items}
    </ul>

</body>
</html>
"""

    # -------------------------
    # RUN
    # -------------------------

    def run(self):

        articles = self.get_articles()

        print(f"📦 ARTICLES FOUND: {len(articles)}")

        html = self.build_index(articles)

        self.output_file.write_text(html, encoding="utf-8")

        print("✅ INDEX CREATED:", self.output_file)


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    IndexBuilder().run()
