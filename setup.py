
from setuptools import setup, find_packages

setup(
    name='reiners_chat',
    version='1.0.1',
    author='Hendrik Huyskens',
    author_email='hendrik.huyskens@rl-institut.de',
    description='Tool to quickly open chats',
    packages=["reiners_chat"],
    entry_points={
        'gui_scripts': [
            'reiners_chat = reiners_chat.chat:run',
        ]
    },
)
