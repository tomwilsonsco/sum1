"""Module main.py"""
import logging
import os
import sys

import torch


def main() -> None:
    """
    Entry point

    :return:
        None
    """

    logger: logging.Logger = logging.getLogger(__name__)

    # Device Selection: Setting a graphics processing unit as the default device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Device Message
    if device == 'cuda':
        logger.info('# of %s devices: %s', device.upper(),
                    torch.cuda.device_count())
    else:
        logger.info('Device: %s', device.upper())

    # Delete Cache Points
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import src.functions.cache

    main()
