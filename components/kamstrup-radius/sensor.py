import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    CONF_SENSOR,
    CONF_ID,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_POWER_FACTOR,
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
    UNIT_VOLT,
    UNIT_AMPERE,
    UNIT_WATT,
    UNIT_VOLT_AMPS_REACTIVE,
    UNIT_KILOWATT_HOURS ,
    UNIT_VOLT_AMPS_REACTIVE_HOURS,
)

DEPENDENCIES = ['uart']
CONF_ENCRYPTION_KEY =       "encryptionkey"
CONF_AUTHENTICATION_KEY =   "authenticationkey"
CONF_ACTIVEPOWERIMPORT =    "activepowerimport"
CONF_ACTIVEPOWEREXPORT =    "activepowerexport"
CONF_ACTIVEPOWERIMPORTL1 =  "activepowerimportl1"
CONF_ACTIVEPOWEREXPORTL1 =  "activepowerexportl1"
CONF_ACTIVEPOWERIMPORTL2 =  "activepowerimportl2"
CONF_ACTIVEPOWEREXPORTL2 =  "activepowerexportl2"
CONF_ACTIVEPOWERIMPORTL3 =  "activepowerimportl3"
CONF_ACTIVEPOWEREXPORTL3 =  "activepowerexportl3"
CONF_REACTIVEPOWERIMPORT =  "reactivepowerimport"
CONF_REACTIVEPOWEREXPORT =  "reactivepowerexport"
CONF_POWERFACTORL1 =        "powerfactorl1"
CONF_POWERFACTORL2 =        "powerfactorl2"
CONF_POWERFACTORL3 =        "powerfactorl3"
CONF_POWERFACTORTOTAL =     "powerfactortotal"
CONF_VOLTAGEL1 =            "voltagel1"
CONF_VOLTAGEL2 =            "voltagel2"
CONF_VOLTAGEL3 =            "voltagel3"
CONF_CURRENTL1 =            "currentl1"
CONF_CURRENTL2 =            "currentl2"
CONF_CURRENTL3 =            "currentl3"
CONF_ACTIVEENERGYIMPORT =   "activeenergyimport"
CONF_ACTIVEENERGYEXPORT =   "activeenergyexport"
CONF_ACTIVEENERGYIMPORTL1 = "activeenergyimportl1"
CONF_ACTIVEENERGYEXPORTL1 = "activeenergyexportl1"
CONF_ACTIVEENERGYIMPORTL2 = "activeenergyimportl2"
CONF_ACTIVEENERGYEXPORTL2 = "activeenergyexportl2"
CONF_ACTIVEENERGYIMPORTL3 = "activeenergyimportl3"
CONF_ACTIVEENERGYEXPORTL3 = "activeenergyexportl3"
CONF_REACTIVEENERGYIMPORT = "reactiveenergyimport"
CONF_REACTIVEENERGYEXPORT = "reactiveenergyexport"

kamstrup_radius_ns = cg.esphome_ns.namespace('kamstrup_radius')
KamstrupRadiusSensor = kamstrup_radius_ns.class_(
    'KamstrupRadiusSensor', sensor.Sensor, cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(KamstrupRadiusSensor),
            cv.Required(CONF_ENCRYPTION_KEY): cv.All(cv.string, cv.Length(min=32, max=32)),
            cv.Required(CONF_AUTHENTICATION_KEY): cv.All(cv.string, cv.Length(min=32, max=32)),
            cv.Optional(CONF_ACTIVEPOWERIMPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWEREXPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWERIMPORTL1): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWEREXPORTL1): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWERIMPORTL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWEREXPORTL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWERIMPORTL3): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEPOWEREXPORTL3): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_REACTIVEPOWERIMPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT_AMPS_REACTIVE,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_REACTIVEPOWEREXPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT_AMPS_REACTIVE,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWERFACTORL1): sensor.sensor_schema(
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER_FACTOR,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWERFACTORL2): sensor.sensor_schema(
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER_FACTOR,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWERFACTORL3): sensor.sensor_schema(
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER_FACTOR,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWERFACTORTOTAL): sensor.sensor_schema(
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER_FACTOR,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_VOLTAGEL1): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_VOLTAGEL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_VOLTAGEL3): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENTL1): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENTL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENTL3): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYIMPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYEXPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYIMPORTL1): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYEXPORTL1): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYIMPORTL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYEXPORTL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYIMPORTL3): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ACTIVEENERGYEXPORTL3): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_REACTIVEENERGYIMPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT_AMPS_REACTIVE_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_REACTIVEENERGYEXPORT): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT_AMPS_REACTIVE_HOURS,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_MEASUREMENT,
            )
        }
    ).extend(uart.UART_DEVICE_SCHEMA)
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "kamstrup_radius",
    baud_rate=2400,
    require_tx=False,
    require_rx=True,
    data_bits=8,
    parity=None,
    stop_bits=1,
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    cg.add(var.set_encryption_key(config[CONF_ENCRYPTION_KEY]))
    cg.add(var.set_authentication_key(config[CONF_AUTHENTICATION_KEY]))

    if CONF_ACTIVEPOWERIMPORT in config:
        conf = config[CONF_ACTIVEPOWERIMPORT]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerimport_sensor(sens))
    if CONF_ACTIVEPOWEREXPORT in config:
        conf = config[CONF_ACTIVEPOWEREXPORT]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerexport_sensor(sens))
    if CONF_ACTIVEPOWERIMPORTL1 in config:
        conf = config[CONF_ACTIVEPOWERIMPORTL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerimportl1_sensor(sens))
    if CONF_ACTIVEPOWEREXPORTL1 in config:
        conf = config[CONF_ACTIVEPOWEREXPORTL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerexportl1_sensor(sens))
    if CONF_ACTIVEPOWERIMPORTL2 in config:
        conf = config[CONF_ACTIVEPOWERIMPORTL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerimportl2_sensor(sens))
    if CONF_ACTIVEPOWEREXPORTL2 in config:
        conf = config[CONF_ACTIVEPOWEREXPORTL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerexportl2_sensor(sens))
    if CONF_ACTIVEPOWERIMPORTL3 in config:
        conf = config[CONF_ACTIVEPOWERIMPORTL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerimportl3_sensor(sens))
    if CONF_ACTIVEPOWEREXPORTL3 in config:
        conf = config[CONF_ACTIVEPOWEREXPORTL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activepowerexportl3_sensor(sens))
    if CONF_POWERFACTORL1 in config:
        conf = config[CONF_POWERFACTORL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_powerfactorl1_sensor(sens))
    if CONF_POWERFACTORL2 in config:
        conf = config[CONF_POWERFACTORL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_powerfactorl2_sensor(sens))
    if CONF_POWERFACTORL3 in config:
        conf = config[CONF_POWERFACTORL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_powerfactorl3_sensor(sens))
    if CONF_POWERFACTORTOTAL in config:
        conf = config[CONF_POWERFACTORTOTAL]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_powerfactortotal_sensor(sens))
    if CONF_VOLTAGEL1 in config:
        conf = config[CONF_VOLTAGEL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_voltagel1_sensor(sens))
    if CONF_VOLTAGEL2 in config:
        conf = config[CONF_VOLTAGEL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_voltagel2_sensor(sens))
    if CONF_VOLTAGEL3 in config:
        conf = config[CONF_VOLTAGEL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_voltagel3_sensor(sens))
    if CONF_CURRENTL1 in config:
        conf = config[CONF_CURRENTL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_currentl1_sensor(sens))
    if CONF_CURRENTL2 in config:
        conf = config[CONF_CURRENTL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_currentl2_sensor(sens))
    if CONF_CURRENTL3 in config:
        conf = config[CONF_CURRENTL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_currentl3_sensor(sens))
    if CONF_ACTIVEENERGYIMPORT in config:
        conf = config[CONF_ACTIVEENERGYIMPORT]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyimport_sensor(sens))
    if CONF_ACTIVEENERGYEXPORT in config:
        conf = config[CONF_ACTIVEENERGYEXPORT]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyexport_sensor(sens))
    if CONF_ACTIVEENERGYIMPORTL1 in config:
        conf = config[CONF_ACTIVEENERGYIMPORTL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyimportl1_sensor(sens))
    if CONF_ACTIVEENERGYEXPORTL1 in config:
        conf = config[CONF_ACTIVEENERGYEXPORTL1]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyexportl1_sensor(sens))
    if CONF_ACTIVEENERGYIMPORTL2 in config:
        conf = config[CONF_ACTIVEENERGYIMPORTL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyimportl2_sensor(sens))
    if CONF_ACTIVEENERGYEXPORTL2 in config:
        conf = config[CONF_ACTIVEENERGYEXPORTL2]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyexportl2_sensor(sens))
    if CONF_ACTIVEENERGYIMPORTL3 in config:
        conf = config[CONF_ACTIVEENERGYIMPORTL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyimportl3_sensor(sens))
    if CONF_ACTIVEENERGYEXPORTL3 in config:
        conf = config[CONF_ACTIVEENERGYEXPORTL3]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_activeenergyexportl3_sensor(sens))
    if CONF_REACTIVEENERGYIMPORT in config:
        conf = config[CONF_REACTIVEENERGYIMPORT]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_reactiveenergyimport_sensor(sens))
    if CONF_REACTIVEENERGYEXPORT in config:
        conf = config[CONF_REACTIVEENERGYEXPORT]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_reactiveenergyexport_sensor(sens))