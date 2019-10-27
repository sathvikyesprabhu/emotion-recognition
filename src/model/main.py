import torch
import argparse
import logging
import coloredlogs

import config

# Setup colorful logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)


if __name__ == '__main__':
    # CLI
    parser = argparse.ArgumentParser(description=f'CLI')
    parser.add_argument('--phase', type=str, default='train')
    parser.add_argument('--load', type=bool, default=False)
    args = parser.parse_args()

    if args.phase == 'train':
        # TODO Code training loop
        # TODO Code validation loop
        pass

    elif args.phase == 'test':
        # TODO Code testing loop
        pass

    else:
        raise ValueError('Choose one of train/validate/test')
