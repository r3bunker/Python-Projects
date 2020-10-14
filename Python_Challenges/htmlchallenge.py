import webbrowser as wb


def makeHTML(self):
    f = open("Summersale.html", "x")
    html = ("""
    <html>
        <body>
            <h1>
                Stay tuned for our amazing Summer Sale
            </h1>
        </body>
    </html>
    """)

    f.write(html)
    f.close()


url = "Summersale.html"
wb.open(url)


if __name__ == "__main__":
    pass
