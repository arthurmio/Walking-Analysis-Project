#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ArduinoBLE.h>

Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

union dat{
  unsigned char asdf[4];
  float zxcv;
};

float getData(const unsigned char data[], int length) {
  dat dat;
  for (int i = 0; i < length; i++) {
    dat.asdf[i] = data[i]; 
    }
  return dat.zxcv;
}

void printChar(BLECharacteristic c1, BLECharacteristic c2, BLECharacteristic c3){
  c1.read();
  c2.read();
  c3.read();

  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  
  float f1=getData(c1.value(), c1.valueLength());
  float f2=getData(c2.value(), c2.valueLength());
  float f3=getData(c3.value(), c3.valueLength());
  Serial.println("SLAVE ");
  Serial.print("Yaw : ");
  Serial.print(f1);
  Serial.print(", ");
  Serial.print("Pitch : ");
  Serial.print(f2);
  Serial.print(", ");
  Serial.print("Roll : ");
  Serial.println(f3);
  
  Serial.print('\n');

  Serial.println("MASTER ");
  Serial.print("Yaw: ");
  Serial.print(euler.x());
  Serial.print(" Pitch: ");
  Serial.print(euler.y());
  Serial.print(" Roll: ");
  Serial.print(euler.z());
  Serial.print("\t\t\n");
  
}

void setup() {
  Serial.begin(115200);

  BLE.begin();
  bno.begin();
  BLE.scan();

  bno.setExtCrystalUse(true);
}

void loop() {
  BLEDevice peripheral = BLE.available();

  
  
  if(peripheral){
    if(peripheral.localName()=="IMU Euler Angles"){
      BLE.stopScan();
      if(peripheral.connect()){
        Serial.println("Connect1");
      }
      else{
        return;
      }
      if(peripheral.discoverAttributes()){
        Serial.println("Connect2");
      }
      else{
        return;
      }
      BLEService euler=peripheral.service("1001");
      BLECharacteristic yaw=euler.characteristic("2001");
      BLECharacteristic pitch=euler.characteristic("2002");
      BLECharacteristic roll=euler.characteristic("2003");
     
       
      while(peripheral.connected()){
        printChar(yaw, pitch, roll);
        delay (50);
      }
        
    }
    else{
          peripheral.disconnect();
          return;
        }
  }
  BLE.scan();
  Serial.println("rescan");

  delay(2000);
}
