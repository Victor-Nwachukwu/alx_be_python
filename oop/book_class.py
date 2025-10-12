class Book:
    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    def __del__(self):
        print(f"Deleting {self.author}")

    def __str__(self):
        return f"{self.author} by {self.title}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.author}', '{self.title}', {self.year})"