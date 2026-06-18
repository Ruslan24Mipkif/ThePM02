import storage

def GetSum():
    all_res = storage.LoadFiles()
    s = 0
    for item in all_res:
        s += item['h']
    return s

def KillRecord(idx):
    all_res = storage.LoadFiles()
    if 0 <= idx < len(all_res):
        removed = all_res.pop(idx)
        storage.RewriteAll(all_res)
        return True, removed['w']
    return False, "Ошибка"

def MakeList():
    data = storage.LoadFiles()
    lines = []
    for i, x in enumerate(data):
        lines.append(f"[{i}] {x['d']} >> {x['w']} ({x['h']} ч.)")
    return lines
