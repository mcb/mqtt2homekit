import argparse
import logging

from mqtt2homekit.bridge import MQTTBridge

logging.basicConfig(level=logging.DEBUG)


def main():

    parser = argparse.ArgumentParser(
            prog="mqtt2homekit",
            description="Transparently bridge an MQTT topic tree",
            epilog="Using %(prog)s v0.2"
    )

    parser.add_argument('--persist', default='bridge.state', help='Persist to file')
    parser.add_argument('-b','--broker', default='mqtt.eclipseprojects.io', 
                        help='URL to use for MQTT broker')
    parser.add_argument('-n','--name', default='MQTT Bridge', help='Name of MQTT Bridge')
    parser.add_argument('--prefix', default='HomeKit', help='MQTT Topic Prefix')
    parser.add_argument('--username', help='Username for MQTT broker if any' )
    parser.add_argument('--password', help='Password for MQTT broker if any' )

    args = parser.parse_args()

    MQTTBridge(args.name, persist_file=args.persist, mqtt_server=args.broker, 
               prefix=args.prefix).driver.start()


if __name__ == '__main__':
    main()
