import argparse
import os

from cysport import create_app


def parse_args():
    """ Parse Arguments """
        
    parser = argparse.ArgumentParser(description='Run the server.') 
    parser.add_argument('--config', type=str, help='Config filename', required=True)

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    # Parse args
    args = parse_args()

    # Convert the relative path to the absolute path
    config_filename = os.path.abspath(args.config)
    
    # Create the app 
    app = create_app(config_filename)

    # Run the server
    app.run()
