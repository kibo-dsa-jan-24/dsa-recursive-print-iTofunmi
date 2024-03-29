class Print:

    def recursive_print(self, f):
        line = f.readline()
        # Task 1
        if line == "":
            return
        remove_space = line.replace("/n" , " " )
        print(remove_space)
        self.recursive_print(f)

    def print_file(self, filename):
        f = open(filename)
        self.recursive_print(f)
        f.close()

    def recursive_print_reverse(self, f):
        line = f.readline()
        # Task 2
        # continue implementation here

    def print_file_reverse(self, filename):
        f = open(filename)
        if line == "":
            return
        remove_space = line.replace("/n" , " " )
        self.recursive_print_reverse(f)
        print(remove_space)
        f.close()

if __name__ == "__main__":
    p = Print()
    print("Printing file:\n==============")
    p.print_file("examples/sample.txt")
    print()

    print("Printing file in reverse:\n=========================")
    p.print_file_reverse("examples/sample.txt")
    print()
