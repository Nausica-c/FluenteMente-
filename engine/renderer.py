class Renderer:

    def render(self, data):
        """
        Trasforma un articolo semplice in una pagina HTML bella
        """

        title = data.get("title", "Articolo")
        keyword = data.get("keyword", "")
        content = data.get("content", "")

        return f"""
<!doctype html>
<html lang="it">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>

    <style>
        body {{
            max-width: 750px;
            margin: auto;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            background: #ffffff;
            color: #111;
        }}

        h1 {{
            font-size: 32px;
            margin-bottom: 10px;
        }}

        h2 {{
            margin-top: 30px;
            color: #222;
        }}

        .tag {{
            display: inline-block;
            padding: 4px 10px;
            background: #f0f0f0;
            border-radius: 6px;
            font-size: 12px;
            margin-bottom: 20px;
        }}

        .footer {{
            margin-top: 50px;
            font-size: 13px;
            color: #777;
            text-align: center;
        }}
    </style>
</head>

<body>

    <h1>{title}</h1>

    <div class="tag">📘 {keyword}</div>

    <div class="content">
        {content}
    </div>

    <div class="footer">
        Lingue-Fluente • impara con semplicità
    </div>

</body>

</html>
"""
