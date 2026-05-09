from pathlib import Path
from engine.renderer import Renderer


class SiteBuilder:

    def __init__(self):

        self.root = Path.cwd()
        self.posts = self.root / "_posts"
        self.output = self.root / "_site"

        self.output.mkdir(exist_ok=True)

        self.renderer = Renderer()

        print("🚀 SITE BUILDER START")
        print("📍 ROOT:", self.root)
        print("📁 POSTS:", self.posts)
        print("📦 OUTPUT:", self.output)

    # -------------------------
    # LEGGE I POST
    # -------------------------

    def get_posts(self):

        if not self.posts.exists():
            print("❌ _posts non esiste")
            return []

        return list(self.posts.glob("*.md"))

    # -------------------------
    # PARSE SEMPLICE FILE
    # -------------------------

    def parse_post(self, path):

        text = path.read_text(encoding="utf-8")

        # 🔥 VERSIONE SEMPLICE (NO LIB COMPLESSA)
        return {
            "title": path.stem.replace("-", " ").title(),
            "keyword": path.stem,
            "content": f"<p>{text}</p>"
        }

    # -------------------------
    # BUILD SITO
    # -------------------------

    def build(self):

        posts = self.get_posts()

        print(f"📦 POSTS TROVATI: {len(posts)}")

        for post in posts:

            print(f"✍️ BUILDING: {post.name}")

            data = self.parse_post(post)

            html = self.renderer.render(data)

            output_file = self.output / f"{post.stem}.html"

            output_file.write_text(html, encoding="utf-8")

            print(f"✅ SAVED: {output_file.name}")

        print("🏁 DONE")


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    SiteBuilder().build()
