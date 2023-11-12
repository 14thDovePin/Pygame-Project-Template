from os.path import exists

from configparser import ConfigParser


class ParseConfig:

    def __init__(self):
        """Initialize configuration parser."""
        self.config = ConfigParser()
        self.file_check = exists('.\\config.ini')

        # Data Structure for `config.ini`.
        self.structure = {
            "Pygame Configuration": {
                "fps": 60,
            },
            "Screen Resolution": {
                "height": 720,
                "width": 1280,
            },
        }

        # Check and Create `config.ini`.
        if not self.file_check:
            self.setup()
            self.write_file()

    def setup(self, ):
        """Define sections and its variables."""
        sections = self.structure.keys()

        # Loop through the data structure.
        for section in sections:
            sub_section = self.structure[section]

            # Create section.
            self.config[section] = {}

            # Add Key-Value pairs.
            keys = sub_section.keys()
            for k in keys:
                value = sub_section[k]
                self.config[section][k] = str(value)

    def write_file(self):
        """Write the `config.ini` file."""
        print('Writing `config.ini`...')

        with open('config.ini', 'w') as config_file:
            self.config.write(config_file)

    def pull(self):
        """Pull configurations from `config.ini`."""
        pass


if __name__ == '__main__':
    config = ParseConfig()
    config.pull()
