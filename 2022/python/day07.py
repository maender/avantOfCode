MAX_SPACE = 70000000
NEEDED = 30000000

class File:
    def __init__(self, name, size, parent_dir) -> None:
        self.name = name
        self.size = size
        self.parent_dir = parent_dir

    def __repr__(self) -> str:
        return f"- {self.name} (file, size={self.size})"


class Dir:
    def __init__(self, name, parent_dir):
        self.name = name
        self.sub_dirs = []
        self.parent_dir = parent_dir
        self.files = []
        self.size = 0

    def set_parent(self, parent):
        self.parent_dir = parent

    def add_sub_dir(self, sub_dir):
        self.sub_dirs.append(sub_dir)

    def add_file(self, infos):
        f = File(infos[1], int(infos[0]), self)
        for fi in self.files:
            if fi.name == f.name and fi.size == f.size: return
        self.files.append(f)
        self.size += f.size
        parent = self.parent_dir
        while parent is not None:
            parent.size += f.size
            parent = parent.parent_dir
        # print(f"add {f} to {self}")

    def parse_ls(self, lines, i):
        while i < len(lines) and not lines[i].startswith('$'):
            infos = lines[i].replace('\n', '').split()
            if infos[0] == 'dir':
                new_dir = Dir(infos[1], self)
                self.add_sub_dir(new_dir)
            else: self.add_file(infos)
            i += 1
        return i

    def print(self, tabs=0):
        print(f"{'  '*tabs}{self}")
        for sub in self.sub_dirs:
            sub.print(tabs+1)
        for file in self.files:
            print(f"{'  '*tabs}{file}")

    def find_size(self, size, out=[]):
        if self.size <= size and self not in out: out.append(self)
        for dir in self.sub_dirs:
            dir.find_size(size, out)
        return out

    def find_sizegt(self, size, out=[]):
        if self.size >= size and self not in out:
            out.append(self)
        for dir in self.sub_dirs:
            dir.find_sizegt(size, out)
        return out

    def __repr__(self) -> str:
        return f"- {self.name} (dir)"


def change_dir(curr_dir, line):
    name = line.split()[1]
    # print(f"change from {curr_dir.name if curr_dir else None} to {name}")
    if name == '..': return curr_dir.parent_dir
    if curr_dir is None:
        return Dir(name, curr_dir)
    for dir in curr_dir.sub_dirs:
        if dir.name == name:
            return dir

if __name__ == '__main__':
    with open('./resources/day07.csv', 'r') as f:
        root_dir = None
        curr_dir = None
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith('$'):
                command = lines[i].replace('$', '').strip()
                if command.startswith('cd'):
                    curr_dir = change_dir(curr_dir, command)
                    if root_dir is None: root_dir = curr_dir
                    i += 1
                elif command.startswith('ls'):
                    i += 1
                    i = curr_dir.parse_ls(lines, i)
    free_space = MAX_SPACE - root_dir.size
    needed_space = NEEDED - free_space
    print(needed_space)
    l = root_dir.find_sizegt(needed_space)
    size = MAX_SPACE
    for dir in l:
        if dir.size < size: size = dir.size
    print(size)
