from os.path import exists

from configparser import ConfigParser


class ParseConfig:

    def __init__(self):
        """Initialize configuration parser."""
        self.config = ConfigParser()
        self.file_check = exists('.\\config.ini')

        # Check and Create `config.ini`.
        if not self.file_check:
            self.setup()
            self.write_file()

    def setup(self, ):
        """Define sections and its variables."""
        # Sections
        self.config['Screen Resolution'] = {}
        self.config['Pygame Configuration'] = {}

        sr = self.config['Screen Resolution']
        pc = self.config['Pygame Configuration']

        # Screen Resolution
        sr['height'] = '720'  # Int
        sr['widgh'] = '1280'  # Int

        # Pygame Configuration
        pc['fps'] = '60'  # Int

    def write_file(self):
        """Write the `config.ini` file."""
        print('Writing `config.ini`...')

        with open('config.ini', 'w') as config_file:
            self.config.write(config_file)


if __name__ == '__main__':
    config = ParseConfig()
