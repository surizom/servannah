from gooey import Gooey, GooeyParser
import os
import subprocess
import socket


@Gooey(language='french')
def parse_args():
    parser = GooeyParser(description="Outil de partage de fichier en réseau local")
    parser.add_argument('dirName', help='Nom du répértoire',
                        widget="DirChooser")
    return parser.parse_args()


if __name__ == '__main__':
    conf = parse_args()

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("Initialisation ....")
    print("Partage en cours du dossier sur le réseau local à l'adresse http://" +
          local_ip + ":5000 ....")
    os.system("serve " + conf.dirName)
