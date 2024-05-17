#include "kamstrup_radius_sensor.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace kamstrup_radius {

static const char *const TAG = "kamstrup-radius.sensor";

uint8_t receiveBuffer[500];
uint8_t decryptedFrameBuffer[500];
VectorView decryptedFrame(decryptedFrameBuffer,0);
MbusStreamParser streamParser(receiveBuffer, sizeof(receiveBuffer));

void KamstrupRadiusSensor::loop() {
  uint8_t data;
  while (this->available() > 0) {
    if (streamParser.pushData(this->read())) {
      VectorView frame = streamParser.getFrame();
      if (streamParser.getContentType() == MbusStreamParser::COMPLETE_FRAME) {
        ESP_LOGV(TAG, "Frame complete");
        if(!decrypt(frame))
        {
          ESP_LOGW(TAG, "Decryption failed");
          return;
        }
        else{
          ESP_LOGV(TAG, "Frame decrypted successfully");
        }
        MeterData md = parseMbusFrame(decryptedFrame);
        sendData(md);
      }
    }
  }
}

void KamstrupRadiusSensor::sendData(MeterData md) {
  ESP_LOGV(TAG, "Sending data");
  if (activepowerimport_sensor_ != nullptr && md.activePowerPlusValid)
    activepowerimport_sensor_->publish_state(md.activePowerPlus);

  if (activepowerexport_sensor_ != nullptr && md.activePowerMinusValid)
    activepowerexport_sensor_->publish_state(md.activePowerMinus);

  if (activepowerimportl1_sensor_ != nullptr && md.activePowerPlusValidL1)
      activepowerimportl1_sensor_->publish_state(md.activePowerPlusL1);

  if (activepowerexportl1_sensor_ != nullptr && md.activePowerMinusValidL1)
      activepowerexportl1_sensor_->publish_state(md.activePowerMinusL1);

  if (activepowerimportl2_sensor_ != nullptr && md.activePowerPlusValidL2)
      activepowerimportl2_sensor_->publish_state(md.activePowerPlusL2);

  if (activepowerexportl2_sensor_ != nullptr && md.activePowerMinusValidL2)
      activepowerexportl2_sensor_->publish_state(md.activePowerMinusL2);

  if (activepowerimportl3_sensor_ != nullptr && md.activePowerPlusValidL3)
      activepowerimportl3_sensor_->publish_state(md.activePowerPlusL3);

  if (activepowerexportl3_sensor_ != nullptr && md.activePowerMinusValidL3)
      activepowerexportl3_sensor_->publish_state(md.activePowerMinusL3);

  if (reactivepowerimport_sensor_ != nullptr && md.reactivePowerPlusValid)
      reactivepowerimport_sensor_->publish_state(md.reactivePowerPlus);

  if (reactivepowerexport_sensor_ != nullptr && md.reactivePowerMinusValid)
      reactivepowerexport_sensor_->publish_state(md.reactivePowerMinus);

  if (powerfactorl1_sensor_ != nullptr && md.powerFactorValidL1)
      powerfactorl1_sensor_->publish_state(md.powerFactorL1);

  if (powerfactorl2_sensor_ != nullptr && md.powerFactorValidL2)
      powerfactorl2_sensor_->publish_state(md.powerFactorL2);

  if (powerfactorl3_sensor_ != nullptr && md.powerFactorValidL3)
      powerfactorl3_sensor_->publish_state(md.powerFactorL3);

  if (powerfactortotal_sensor_ != nullptr && md.powerFactorTotalValid)
      powerfactortotal_sensor_->publish_state(md.powerFactorTotal);

  if (voltagel1_sensor_ != nullptr && md.voltageL1Valid)
      voltagel1_sensor_->publish_state(md.voltageL1);

  if (voltagel2_sensor_ != nullptr && md.voltageL2Valid)
      voltagel2_sensor_->publish_state(md.voltageL2);

  if (voltagel3_sensor_ != nullptr && md.voltageL3Valid)
      voltagel3_sensor_->publish_state(md.voltageL3);

  if (currentl1_sensor_ != nullptr && md.centiAmpereL1Valid)
      currentl1_sensor_->publish_state(md.centiAmpereL1/100.);

  if (currentl2_sensor_ != nullptr && md.centiAmpereL2Valid)
      currentl2_sensor_->publish_state(md.centiAmpereL2/100.);

  if (currentl3_sensor_ != nullptr && md.centiAmpereL3Valid)
      currentl3_sensor_->publish_state(md.centiAmpereL3/100.);

  if (activeenergyimport_sensor_ != nullptr && md.activeImportWhValid)
      activeenergyimport_sensor_->publish_state(md.activeImportWh/1000.);

  if (activeenergyexport_sensor_ != nullptr && md.activeExportWhValid)
      activeenergyexport_sensor_->publish_state(md.activeExportWh/1000.);

  if (activeenergyimportl1_sensor_ != nullptr && md.activeImportWhValidL1)
      activeenergyimportl1_sensor_->publish_state(md.activeImportWhL1/1000.);

  if (activeenergyexportl1_sensor_ != nullptr && md.activeExportWhValidL1)
      activeenergyexportl1_sensor_->publish_state(md.activeExportWhL1/1000.);

  if (activeenergyimportl2_sensor_ != nullptr && md.activeImportWhValidL2)
      activeenergyimportl2_sensor_->publish_state(md.activeImportWhL2/1000.);

  if (activeenergyexportl2_sensor_ != nullptr && md.activeExportWhValidL2)
      activeenergyexportl2_sensor_->publish_state(md.activeExportWhL2/1000.);

  if (activeenergyimportl3_sensor_ != nullptr && md.activeImportWhValidL3)
      activeenergyimportl3_sensor_->publish_state(md.activeImportWhL3/1000.);

  if (activeenergyexportl3_sensor_ != nullptr && md.activeExportWhValidL3)
      activeenergyexportl3_sensor_->publish_state(md.activeExportWhL3/1000.);

  if (reactiveenergyimport_sensor_ != nullptr && md.reactiveImportWhValid)
      reactiveenergyimport_sensor_->publish_state(md.reactiveImportWh/1000.);

  if (reactiveenergyexport_sensor_ != nullptr && md.reactiveExportWhValid)
      reactiveenergyexport_sensor_->publish_state(md.reactiveExportWh/1000.);
}

void KamstrupRadiusSensor::dump_config() { LOG_SENSOR("", "KamstrupRadius Sensor", this); }

bool KamstrupRadiusSensor::decrypt(const VectorView& frame){

  if(frame.size() < headersize+footersize+12+18){
    ESP_LOGW(TAG, "Invalid frame size.");
  }
  memcpy(decryptedFrameBuffer, &frame.front(), frame.size());
    
  uint8_t system_title[8];
  memcpy(system_title, decryptedFrameBuffer+headersize+2, 8);
  
  uint8_t initialization_vector[12];
  memcpy(initialization_vector,system_title,8);
  memcpy(initialization_vector+8,decryptedFrameBuffer+headersize+14,4);
  
  uint8_t additional_authenticated_data[17];
  memcpy(additional_authenticated_data,decryptedFrameBuffer+headersize+13,1);
  memcpy(additional_authenticated_data+1,authentication_key,16);
  
  uint8_t authentication_tag[12];
  memcpy(authentication_tag,decryptedFrameBuffer+headersize+frame.size()-headersize-footersize-12,12);
 
  uint8_t cipher_text[frame.size()-headersize-footersize-18-12];
  memcpy(cipher_text,decryptedFrameBuffer+headersize+18,frame.size()-headersize-footersize-12-18);
 
  uint8_t plaintext[sizeof(cipher_text)];

  mbedtls_gcm_init(&m_ctx);
  int success = mbedtls_gcm_setkey(&m_ctx, MBEDTLS_CIPHER_ID_AES, encryption_key, sizeof(encryption_key)*8);
  if (0 != success ) {
    ESP_LOGW(TAG, "Setkey failed: %i" ,success);
    return false;
  }
  success = mbedtls_gcm_auth_decrypt(&m_ctx, sizeof(cipher_text), initialization_vector, sizeof(initialization_vector), 
    additional_authenticated_data, sizeof(additional_authenticated_data), authentication_tag, sizeof(authentication_tag), 
    cipher_text, plaintext);
  if (0 != success) {
    ESP_LOGW(TAG, "authdecrypt failed: %i" ,success);
    return false;
  }
  mbedtls_gcm_free(&m_ctx);
    
  //copy replace encrypted data with decrypted for mbusparser library. Checksum not updated. Hopefully not needed
  memcpy(decryptedFrameBuffer+headersize+18,plaintext,sizeof(plaintext));
  decryptedFrame = VectorView(decryptedFrameBuffer,frame.size());
  
  return true;
}

}  // namespace kamstrup_radius
}  // namespace esphome