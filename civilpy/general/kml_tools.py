import simplekml

kml = simplekml.Kml()


def create_pin(name, coords):
    pin = kml.newpoint(name=name, coords=coords)

    return pin


def save_kml_file(output_path):
    kml.save(output_path)

