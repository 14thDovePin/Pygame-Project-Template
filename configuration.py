from os.path import exists

from configparser import ConfigParser


# Configuration File Structure
CFS = {
    "Pygame Configuration": {  # [Section]
        "fps": 60,             # Key = Value
        "screen_height": 720,
        "screen_width": 1280,
    },
}
# Configuration File Name
CFN = '.\\config.ini'


class ParseConfig:

    def __init__(self):
        """Initialize configuration parsing."""
        # Pull configuration file structure for `config.ini`.
        self.structure = CFS
        self.sections = self.structure.keys()

        # Check and create `config.ini`.
        file_check = exists(CFN)
        if not file_check:
            self._create()

        # The final data from `config.ini`.
        self.data = {}

        self._pull_data()

    def _create(self, ):
        """Define and write the `config.ini` file."""
        config = ConfigParser()

        # Loop through the data structure.
        for section in self.sections:
            sub_section = self.structure[section]
            keys = sub_section.keys()

            # Create section.
            config[section] = {}
            so = config[section]  # Section Object

            # Add key-value pairs.
            for k in keys:
                value = sub_section[k]
                so[k] = str(value)

        # Write the `config.ini` file.
        with open('config.ini', 'w') as config_file:
            config.write(config_file)

    def _pull_data(self):
        """Pull the data from `config.ini`."""
        config = ConfigParser()

        # Create reference for data type conversion.
        type_ref = {}

        # Loop through the `CFS`.
        for section in self.sections:
            sub_section = self.structure[section]
            keys = sub_section.keys()

            for k in keys:
                value = sub_section[k]

                # Store `key: type(value)`.
                type_ref[k] = type(value)

        # Read configuration file.
        config.read(CFN)

        # Loop through its data structure.
        sections = config.sections()
        for section in sections:
            section = config[section]
            keys = section.keys()

            # Check keys.
            for k in keys:
                if k not in type_ref:
                    raise('ConfigurationFileError KeyError')

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
            raise('ConfigurationFileError ValueTypeMismatch')


if __name__ == '__main__':
    config = ParseConfig().data

    keys = config.keys()
    print('Key: Value | DataType\n')
    for k in keys:
        value = config[k]
        print(f'{k}: {value} | {type(value)}')
