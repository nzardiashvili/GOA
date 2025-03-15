def abbrev_name(name):
    name = name.split()
    initials = [n[0].upper() for n in names]
    return ".".join(initials) + "."
print(abbrev_name("nino zardiashvili"))