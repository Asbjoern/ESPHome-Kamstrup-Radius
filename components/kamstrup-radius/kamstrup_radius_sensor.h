#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"
#include <stdlib.h>
#include "gcm.h"
#include "mbusparser.h"

namespace esphome {
namespace kamstrup_radius {

class KamstrupRadiusSensor : public sensor::Sensor, public Component, public uart::UARTDevice {
 public:
  void loop() override;
  void dump_config() override;
  void set_encryption_key(String key) { hexStr2bArr(encryption_key, key.c_str(), sizeof(encryption_key)); }
  void set_authentication_key(String key){ hexStr2bArr(authentication_key, key.c_str(), sizeof(authentication_key)); }

  void set_activepowerimport_sensor(sensor::Sensor *obj) { activepowerimport_sensor_ = obj; }
  void set_activepowerexport_sensor(sensor::Sensor *obj) { activepowerexport_sensor_ = obj; }
  void set_activepowerimportl1_sensor(sensor::Sensor *obj) { activepowerimportl1_sensor_ = obj; }
  void set_activepowerexportl1_sensor(sensor::Sensor *obj) { activepowerexportl1_sensor_ = obj; }
  void set_activepowerimportl2_sensor(sensor::Sensor *obj) { activepowerimportl2_sensor_ = obj; }
  void set_activepowerexportl2_sensor(sensor::Sensor *obj) { activepowerexportl2_sensor_ = obj; }
  void set_activepowerimportl3_sensor(sensor::Sensor *obj) { activepowerimportl3_sensor_ = obj; }
  void set_activepowerexportl3_sensor(sensor::Sensor *obj) { activepowerexportl3_sensor_ = obj; }
  void set_reactivepowerimport_sensor(sensor::Sensor *obj) { reactivepowerimport_sensor_ = obj; }
  void set_reactivepowerexport_sensor(sensor::Sensor *obj) { reactivepowerexport_sensor_ = obj; }
  void set_powerfactorl1_sensor(sensor::Sensor *obj) { powerfactorl1_sensor_ = obj; }
  void set_powerfactorl2_sensor(sensor::Sensor *obj) { powerfactorl2_sensor_ = obj; }
  void set_powerfactorl3_sensor(sensor::Sensor *obj) { powerfactorl3_sensor_ = obj; }
  void set_powerfactortotal_sensor(sensor::Sensor *obj) { powerfactortotal_sensor_ = obj; }
  void set_voltagel1_sensor(sensor::Sensor *obj) { voltagel1_sensor_ = obj; }
  void set_voltagel2_sensor(sensor::Sensor *obj) { voltagel2_sensor_ = obj; }
  void set_voltagel3_sensor(sensor::Sensor *obj) { voltagel3_sensor_ = obj; }
  void set_currentl1_sensor(sensor::Sensor *obj) { currentl1_sensor_ = obj; }
  void set_currentl2_sensor(sensor::Sensor *obj) { currentl2_sensor_ = obj; }
  void set_currentl3_sensor(sensor::Sensor *obj) { currentl3_sensor_ = obj; }
  void set_activeenergyimport_sensor(sensor::Sensor *obj) { activeenergyimport_sensor_ = obj; }
  void set_activeenergyexport_sensor(sensor::Sensor *obj) { activeenergyexport_sensor_ = obj; }
  void set_activeenergyimportl1_sensor(sensor::Sensor *obj) { activeenergyimportl1_sensor_ = obj; }
  void set_activeenergyexportl1_sensor(sensor::Sensor *obj) { activeenergyexportl1_sensor_ = obj; }
  void set_activeenergyimportl2_sensor(sensor::Sensor *obj) { activeenergyimportl2_sensor_ = obj; }
  void set_activeenergyexportl2_sensor(sensor::Sensor *obj) { activeenergyexportl2_sensor_ = obj; }
  void set_activeenergyimportl3_sensor(sensor::Sensor *obj) { activeenergyimportl3_sensor_ = obj; }
  void set_activeenergyexportl3_sensor(sensor::Sensor *obj) { activeenergyexportl3_sensor_ = obj; }
  void set_reactiveenergyimport_sensor(sensor::Sensor *obj) { reactiveenergyimport_sensor_ = obj; }
  void set_reactiveenergyexport_sensor(sensor::Sensor *obj) { reactiveenergyexport_sensor_ = obj; }
  
 protected:
  void sendData(MeterData md);
  void hexStr2bArr(uint8_t *dest, const char *source, int bytes_n)
  {
    uint8_t *dst = dest;
    uint8_t *end = dest + sizeof(bytes_n);
    unsigned int u;

    while (dest < end && sscanf(source, "%2x", &u) == 1)
    {
        *dst++ = u;
        source += 2;
    }
}
  
 private:
  const size_t headersize = 11;
  const size_t footersize = 3;
  uint8_t encryption_key[16];
  uint8_t authentication_key[16];
  sensor::Sensor *activepowerimport_sensor_{nullptr};
  sensor::Sensor *activepowerexport_sensor_{nullptr};
  sensor::Sensor *activepowerimportl1_sensor_{nullptr};
  sensor::Sensor *activepowerexportl1_sensor_{nullptr};
  sensor::Sensor *activepowerimportl2_sensor_{nullptr};
  sensor::Sensor *activepowerexportl2_sensor_{nullptr};
  sensor::Sensor *activepowerimportl3_sensor_{nullptr};
  sensor::Sensor *activepowerexportl3_sensor_{nullptr};
  sensor::Sensor *reactivepowerimport_sensor_{nullptr};
  sensor::Sensor *reactivepowerexport_sensor_{nullptr};
  sensor::Sensor *powerfactorl1_sensor_{nullptr};
  sensor::Sensor *powerfactorl2_sensor_{nullptr};
  sensor::Sensor *powerfactorl3_sensor_{nullptr};
  sensor::Sensor *powerfactortotal_sensor_{nullptr};
  sensor::Sensor *voltagel1_sensor_{nullptr};
  sensor::Sensor *voltagel2_sensor_{nullptr};
  sensor::Sensor *voltagel3_sensor_{nullptr};
  sensor::Sensor *currentl1_sensor_{nullptr};
  sensor::Sensor *currentl2_sensor_{nullptr};
  sensor::Sensor *currentl3_sensor_{nullptr};
  sensor::Sensor *activeenergyimport_sensor_{nullptr};
  sensor::Sensor *activeenergyexport_sensor_{nullptr};
  sensor::Sensor *activeenergyimportl1_sensor_{nullptr};
  sensor::Sensor *activeenergyexportl1_sensor_{nullptr};
  sensor::Sensor *activeenergyimportl2_sensor_{nullptr};
  sensor::Sensor *activeenergyexportl2_sensor_{nullptr};
  sensor::Sensor *activeenergyimportl3_sensor_{nullptr};
  sensor::Sensor *activeenergyexportl3_sensor_{nullptr};
  sensor::Sensor *reactiveenergyimport_sensor_{nullptr};
  sensor::Sensor *reactiveenergyexport_sensor_{nullptr};

  mbedtls_gcm_context m_ctx;
  bool decrypt(const VectorView& frame);

};

}  // namespace kamstrup_radius
}  // namespace esphome
