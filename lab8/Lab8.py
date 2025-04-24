class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year
    
    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"
    
    def __eq__(self, other):
        if isinstance(other, ArchiveItem):
            return self.uid == other.uid
        return False
    
    def is_recent(self, n):
        current_year = 2025
        return (current_year - self.year) <= n


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Book -> {super().__str__()}, Author: {self.author}, Pages: {self.pages}"


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi
    
    def __str__(self):
        return f"Article -> {super().__str__()}, Journal: {self.journal}, DOI: {self.doi}"


class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration
    
    def __str__(self):
        return f"Podcast -> {super().__str__()}, Host: {self.host}, Duration: {self.duration} mins"


def save_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            if isinstance(item, Book):
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")


def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            item_type = fields[0]
            
            if item_type == "Book":
                items.append(Book(fields[1], fields[2], int(fields[3]), fields[4], int(fields[5])))
            elif item_type == "Article":
                items.append(Article(fields[1], fields[2], int(fields[3]), fields[4], fields[5]))
            elif item_type == "Podcast":
                items.append(Podcast(fields[1], fields[2], int(fields[3]), fields[4], int(fields[5])))
    
    return items


items = [
    Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
    Book("B002", "Python Crash Course", 2022, "Eric Matthes", 544),
    Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
    Article("A102", "Machine Learning Applications", 2020, "Science", "10.1234/ml789"),
    Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
    Podcast("P302", "Data Science Weekly", 2021, "John Smith", 60)
]

save_to_file(items, "archive.txt")

loaded_items = load_from_file("archive.txt")

print("All Archive Items:")
for item in loaded_items:
    print(item)

print("\nRecent Items:")
for item in loaded_items:
    if item.is_recent(5):
        print(item)

print("\nArticles with DOI starting '10.1234':")
for item in loaded_items:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)