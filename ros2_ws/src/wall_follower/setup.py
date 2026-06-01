from glob import glob
import os

from setuptools import setup

package_name = 'wall_follower'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Samrudh',
    maintainer_email='example@gmail.com',
    description='ROS2 Wall Following Robot',
    license='MIT',
    entry_points={
        'console_scripts': [
            'wall_follower_node = wall_follower.wall_follower_node:main',
            'telemetry_node = wall_follower.telemetry_node:main',
            'teleop_node = wall_follower.teleop_node:main'
        ],
    },
)
