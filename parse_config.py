from os.path import exists

from configparser import ConfigParser


def initialize_configuration():
    config = ConfigParser()

    # Sections
    config['Screen Resolution'] = {}
    sr = config['Screen Resolution']
    config['Pygame Configuration'] = {}
    pc = config['Pygame Configuration']

    # Screen Resolution
    sr['height'] = '720'
    sr['widgh'] = '1280'

    # Pygame Configuration
    pc['fps'] = '60'

    # Return configuration.
    return config


def write_configuration(config, file_exists):
    """Write the configuration file."""
    if file_exists:
        return

    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    print('`config.ini` Written')


if __name__ == '__main__':
    # For testing purposes only..
    config = initialize_configuration()
    file_exists = exists('.\\config.ini')
    write_configuration(config, file_exists)
