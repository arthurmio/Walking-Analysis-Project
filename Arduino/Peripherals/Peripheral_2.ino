// #include <Arduino_LSM9DS1.h>
#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ArduinoBLE.h>

Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

BLEService BLEuler("1002");
BLEFloatCharacteristic YawBLE("2001", BLERead | BLENotify);
BLEFloatCharacteristic PitchBLE("2002", BLERead | BLENotify);
BLEFloatCharacteristic RollBLE("2003", BLERead | BLENotify);

//float yaw, pitch, roll;


void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

  BLE.begin();
  bno.begin();
  
  BLE.setDeviceName("Arduino Nano 33 BLE Sense");
  BLE.setLocalName("IMU Euler Angles 2");
  
  BLE.setAdvertisedService(BLEuler);

  BLEuler.addCharacteristic(YawBLE);
  BLEuler.addCharacteristic(PitchBLE);
  BLEuler.addCharacteristic(RollBLE);
  
  BLE.addService(BLEuler);
  BLE.setConnectable(true);
  BLE.setAdvertisingInterval(100);
  BLE.advertise();
  Serial.println("Bluetooth Device Active, Waiting for Connections...");

  bno.setExtCrystalUse(true);
}

void loop() {
  BLEDevice central = BLE.central();

  if(central) {
    Serial.print("Connected to Central: ");
    Serial.println(central.address());
    
    while(central.connected()) {
      digitalWrite(LED_BUILTIN, HIGH);

      imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
      
      YawBLE.writeValue(euler.x());    
      PitchBLE.writeValue(euler.y());
      RollBLE.writeValue(euler.z());
      
    }
  }
  digitalWrite(LED_BUILTIN, LOW);
  Serial.print("Disconnected from Central: ");
  Serial.println(BLE.address());
}
