class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Asus ROG"))
    laptop.add_child(TreeNode("Notebook"))

    cellphone = TreeNode("Mobile Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("OnePlus"))
    cellphone.add_child(TreeNode("RedMi"))

    tv = TreeNode("TeleVision")
    tv.add_child(TreeNode("SONY"))
    tv.add_child(TreeNode("PHILLIPS"))

    root.add_child(laptop)
    root.add_child(mobilephone)
    root.add_child(television)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
