import os

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_path = os.path.abspath(os.path.dirname(__file__))
photos_path = os.path.join(base_path, 'assets', 'photos')

DEBUG = False
def enable_debug():
    global DEBUG
    DEBUG = True
    if not os.path.exists(os.path.join(os.getcwd(), 'pullout_debug')):
        os.makedirs(os.path.join(os.getcwd(), 'pullout_debug'), exist_ok=True)
    else:
        for file in os.listdir(os.path.join(os.getcwd(), 'pullout_debug')):
            os.remove(os.path.join(os.getcwd(), 'pullout_debug', file))