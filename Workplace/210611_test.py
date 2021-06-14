import configparser

config = configparser.ConfigParser()
config.read('Pipeline.config')

panel = config['PANEL']['mgi_exome_v5']
print(panel)
