/*
  Central
*/

#include <ArduinoBLE.h>


void setup() {
  Serial.begin(9600);
  while (!Serial);

  // initialize the BLE hardware
  BLE.begin();

  Serial.println("BLE Central - IMU");

  // start scanning for peripherals
  BLE.scanForUuid("590d65c7-3a0a-4023-a05a-6aaf2f22441c");
}

void loop() {
  // check if a peripheral has been discovered
  BLEDevice peripheral = BLE.available();

  if (peripheral) {
    // discovered a peripheral, print out address, local name, and advertised service
    Serial.print("Found ");
    Serial.print(peripheral.address());
    Serial.print(" '");
    Serial.print(peripheral.localName());
    Serial.print("' ");
    Serial.print(peripheral.advertisedServiceUuid());
    Serial.println();

    if (peripheral.localName() != "IMU Euler Angles") {
      return;
    }

    // stop scanning
    BLE.stopScan();

    controlLed(peripheral);

    // peripheral disconnected, start scanning again
    BLE.scanForUuid("590d65c7-3a0a-4023-a05a-6aaf2f22441c");
  }
}

void controlLed(BLEDevice peripheral) {
  // connect to the peripheral
  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }

 

  // retrieve the LED characteristic
  BLECharacteristic YawSlave = peripheral.characteristic("00000004-0000-1000-8000-00805f9b34fb");
  BLECharacteristic PitchSlave = peripheral.characteristic("00000005-0000-1000-8000-00805f9b34fb");
  BLECharacteristic RollSlave = peripheral.characteristic("00000006-0000-1000-8000-00805f9b34fb");
  

 // while (peripheral.connected()) {
    // while the peripheral is connected

Serial.println("properties: ");
            Serial.println(YawSlave.properties());

if (!YawSlave.canWrite()){
   Serial.println("canWrite False");}

if (!YawSlave.canSubscribe()){
   Serial.println("canSubscribe False");}


if(!YawSlave.canRead()){
      Serial.println("canRead False");}


if(!YawSlave.valueUpdated()){
      Serial.println("valueUpdated False");}
     
  while (peripheral.connected()) {
//if (YawSlave.valueUpdated()) {

uint16_t holdvalues[6] = {1,2,3,4,5,6} ;

YawSlave.readValue(holdvalues, 6);
byte rawValue0 = holdvalues[0];
byte rawValue1 = holdvalues[1];
byte rawValue2 = holdvalues[2];
byte rawValue3 = holdvalues[3];
byte rawValue4 = holdvalues[4];
byte rawValue5 = holdvalues[5];

    Serial.print("value 0: ");
    Serial.print(rawValue0);
    Serial.print("  value 1: ");
    Serial.print(rawValue1);
    Serial.print("  value 2: ");
    Serial.print(rawValue2);
      Serial.print("  value 3: ");
    Serial.print(rawValue3);
    Serial.print("  value 4: ");
    Serial.print(rawValue4);
    Serial.print("  value 5: ");
    Serial.println(rawValue5); 
   
   // printData(YawSlave.value(), YawSlave.valueLength());
    delay(500);
     /*if (YawSlave.read()) {
      Serial.println("characteristic value read");

      byte yaw = 0;
      YawSlave.readValue(yaw);
      Serial.println("Printing IMU axis : ");
      Serial.println("Yaw : ");
      Serial.println(yaw);


     } 
     else {
      Serial.println("error reading characteristic value");
     }
    

    delay(100);*/
  }

  Serial.println("Peripheral disconnected");
}
