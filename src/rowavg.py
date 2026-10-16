"""Average whitespace-separated numbers per line."""


def averages(lines):
    out = []
    for line in lines:
        parts = line.split()
        try:
            out.append(sum(float(p) for p in parts) / len(parts) if parts else None)
        except ValueError:
            out.append(None)
    return out


def averages_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return averages(handle)
