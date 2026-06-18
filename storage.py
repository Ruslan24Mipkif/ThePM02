import os

DB_FILE = "diary_data.txt"

def SaveToFile(dt, wk, hr):
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(f"{dt}|{wk}|{hr}\n")

def LoadFiles():
    if not os.path.exists(DB_FILE):
        return []
    
    data_list = []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split("|")
                if len(parts) == 3:
                    data_list.append({
                        "d": parts[0], 
                        "w": parts[1], 
                        "h": float(parts[2])
                    })
    return data_list

def RewriteAll(items):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        for i in items:
            f.write(f"{i['d']}|{i['w']}|{i['h']}\n")
