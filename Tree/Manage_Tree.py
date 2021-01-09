class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + " (" + self.designation + ")"
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vedant","Infrastructure Head")
    infra_head.add_child(TreeNode("Avani","Cloud Manager"))
    infra_head.add_child(TreeNode("Malav", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Nilam","HR Head")

    hr_head.add_child(TreeNode("Vansh","Recruitment Manager"))
    hr_head.add_child(TreeNode("Purva", "Policy Manager"))

    ceo = TreeNode("Ved", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("Name")
    root_node.print_tree("Designation")
    root_node.print_tree("Both")
