class Item:
    def __init__(self, name, class_chr):
        self.pack = 1
        self.name = name
        if class_chr == "Big pencil":
            self.wood = 70 * self.pack
            self.coal = 30 * self.pack

        elif class_chr == "Small pencil":
            self.wood = 60 * self.pack
            self.coal = 40 * self.pack

    def show_info(self):
        print(f"""name {self.name} | package - {self.pack} 
        WOOD - {self.wood * self.pack} 
        COAL - {self.coal * self.pack}""")

    def show_pack(self):
        return self.pack

    def add_pack(self, cout_pack):
        self.pack += cout_pack


pencil = Item("Pen1", "Big pencil")
pencil.show_info()
print(f"You have {pencil.show_pack()} pack. Do you want to buy more?(Yes or No)\n")
question = input("")
if question == "Yes":
    pack_cout = int(input("How many you want buy?\n"))
    pencil.add_pack(pack_cout)
    pencil.show_info()

else:
    print("Goodbye!!!")
