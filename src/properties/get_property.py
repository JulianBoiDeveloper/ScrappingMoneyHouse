import configparser

def get_property(file_path, key):
    config = configparser.ConfigParser()
    config.read(file_path)

    value = config.get('DEFAULT', key)
    return value