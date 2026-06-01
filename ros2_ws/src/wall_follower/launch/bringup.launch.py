from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    serial_port = LaunchConfiguration('serial_port')
    enable_teleop = LaunchConfiguration('enable_teleop')

    telemetry_node = Node(
        package='wall_follower',
        executable='telemetry_node',
        output='screen',
        parameters=[{'serial_port': serial_port}]
    )

    wall_follower_node = Node(
        package='wall_follower',
        executable='wall_follower_node',
        output='screen',
        condition=UnlessCondition(enable_teleop)
    )

    teleop_node = Node(
        package='wall_follower',
        executable='teleop_node',
        output='screen',
        condition=IfCondition(enable_teleop)
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'serial_port',
            default_value='/dev/ttyUSB0',
            description='Serial port connected to the ESP32'
        ),
        DeclareLaunchArgument(
            'enable_teleop',
            default_value='false',
            description='Run keyboard teleop instead of autonomous following'
        ),
        telemetry_node,
        wall_follower_node,
        teleop_node
    ])
