class DataFormatting:
    def __init__(self):
        pass

    def votes(self, data):
        return int(data.text.split(" ")[0].replace(".", ""))

    def setDecimals(self, entry, decimals):
        return float(f'{float(entry):.{decimals}f}')

    def percentage(self, data):
        return self.setDecimals(float(data.text.split("%")[0].replace(",", ".")) / 100, 4)

    def thousands(self, entry):
        return f'{entry:,}'
