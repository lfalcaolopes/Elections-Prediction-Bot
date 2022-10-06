class DataFormatting:
    def __init__(self):
        pass

    def votes(self, data):
        return int(data.text.split(" ")[0].replace(".", ""))

    def percentage(self, data):
        return float("{:.4f}".format(float(data.text.split("%")[0].replace(",", ".")) / 100))
