from os.path import exists

from configparser import ConfigParser


STRUCTURE = {  # Configuration Structure
    "Pygame Configuration": {
        "fps": 60,
        "screen_height": 720,
        "screen_width": 1280,
    },
}


class ParseConfig:

    def __init__(self):
        """Initialize configuration parser."""
        self.file_check = exists('.\\config.ini')

        # The data structure for `config.ini`.
        self.structure = STRUCTURE
        self.sections = self.structure.keys()

        # The data pulled from `config.ini`.
        self.data = {}

        # Check and create `config.ini`.
        if not self.file_check:
            config = self._setup()
            self._write_file(config)

        self._pull_data()

    def _setup(self, ):
        """Define sections and its variables."""
        config = ConfigParser()

        # Loop through the data structure.
        for section in self.sections:
            sub_section = self.structure[section]

            # Create section.
            config[section] = {}

            # Add Key-Value pairs.
            keys = sub_section.keys()
            for k in keys:
                value = sub_section[k]
                config[section][k] = str(value)

        return config

    def _write_file(self, config):
        """Write the `config.ini` file."""
        print('Writing `config.ini`...')

        with open('config.ini', 'w') as config_file:
            config.write(config_file)

    def _pull_data(self):
        """Pull the data from `config.ini`."""
        config = ConfigParser()

        # Create reference for data type conversion.
        type_ref = {}

        # Loop through the data structure.
        for section in self.sections:
            sub_section = self.structure[section]
            keys = sub_section.keys()

            for k in keys:
                value = sub_section[k]

                # Store key-value pair types.
                type_ref[k] = type(value)

        # Read configuration file.
        config.read('.\\config.ini')

        # Loop through its data structure.
        sections = config.sections()
        for section in sections:
            section = config[section]
            keys = section.keys()

            # Check keys.
            for k in keys:
                if k not in type_ref:
                    raise('IniFileError KeyError')

            for k in keys:
                # Store and convert its key-values pairs.
                value = section[k]
                value = self._convert(type_ref, k, value)
                self.data[k] = value

    def _convert(self, type_ref: dict, key, value):
        """Return a value with its corresponding data type."""
        convert_type = type_ref[key]

        try:
            # Int
            if convert_type == int: return int(value)

            # Float
            elif convert_type == float: return float(value)

            # String
            elif convert_type == str: return value

            # Bool
            elif convert_type == bool:
                if value.lower() == 'true': return True
                elif value.lower() == 'false': return False

            # None
            elif convert_type == None: return None

        except:
            raise('IniFileError Value_TypeMismatch')


if __name__ == '__main__':
    config = ParseConfig().data

    keys = config.keys()
    print('Key: Value | DataType\n')
    for k in keys:
        value = config[k]
        print(f'{k}: {value} | {type(value)}')
