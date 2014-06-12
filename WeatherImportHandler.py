import xml.sax

class WeatherImportHandler(xml.sax.ContentHandler):
    temperature = None
    def startElement(self, name, attrs):
        if self.temperature is not None:         # Wir wollen nur das erste Element
            return
        if name == "temperature":
            self.temperature = attrs['value']