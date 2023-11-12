class student:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = []

    def info(self, hodnoceni):
        self.hodnoceni.append(hodnoceni)

    def informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Příjmení: {self.prijmeni}")
        print("Hodnocení:", self.hodnoceni)


martin = student("Martin", "Hruška")
martin.info(100)
martin.informace()
