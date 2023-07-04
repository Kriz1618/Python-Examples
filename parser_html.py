from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        print(f">>> Multi-line Comment\n{data}") if "\n" in data else print(f">>> Single-line Comment\n{data}")

    def handle_data(self, data: str) -> None:
        if data != "\n":
            print(f">>> Data\n{data}")
            
html = """<!--[if IE 9]>IE9-specific content \n <![endif]-->"""
html += "<div> Welcome to HackerRank</div>"
html += "<!--[if IE 9]>IE9-specific content<![endif]-->"

parser = MyHTMLParser()
parser.feed(html)
parser.close()