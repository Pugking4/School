def addVertBar(filename):
    filepath = f"Misc\\maimaiRandomChartData\\{filename}"
    with open(filepath,encoding="utf8") as f:
        lines = f.read().splitlines()

    with open(filepath, "w",encoding="utf8") as f:
        for line in lines:
            f.write(line + "|")