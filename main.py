from link_shortener import LinkShortener


urls = [
    "https://walla.co.il",
    "https://nana.co.il"
]
ls=LinkShortener()
for url in urls:
    id = ls.shorten(url)
    print(id)