#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ArduinoBLE.h>

#define BLE_BUFFER_SIZES             20
/* Device name which can be scene in BLE scanning software. */
#define BLE_DEVICE_NAME                "Arduino Nano 33 BLE Sense"
/* Local name which should pop up when scanning for BLE devices. */
#define BLE_LOCAL_NAME                "IMU Euler Angles"
/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

BLEService BLEuler("590d65c7-3a0a-4023-a05a-6aaf2f22441c");
BLECharacteristic YawBLE("0004", BLERead | BLENotify /*| BLEBroadcast */, BLE_BUFFER_SIZES);
BLECharacteristic PitchBLE("0005", BLERead | BLENotify /*| BLEBroadcast*/, BLE_BUFFER_SIZES);
BLECharacteristic RollBLE("0006", BLERead | BLENotify /*| BLEBroadcast*/, BLE_BUFFER_SIZES);

/* Common global buffer will be used to write to the BLE characteristics. */
char bleBuffer[BLE_BUFFER_SIZES];


void setup() {
  
  Serial.begin(115200);
  while(!Serial);

  pinMode(LED_BUILTIN, OUTPUT);
  
  BLE.begin();
  bno.begin();
    
  BLE.setDeviceName(BLE_DEVICE_NAME);
  BLE.setLocalName(BLE_LOCAL_NAME);
  BLE.setAdvertisedService(BLEuler);
  /* A seperate characteristic is used for each X, Y, and Z axis. */
  BLEuler.addCharacteristic(YawBLE);
  BLEuler.addCharacteristic(PitchBLE);
  BLEuler.addCharacteristic(RollBLE);

  BLE.addService(BLEuler);
  BLE.advertise();
  /* 
   * Initialises the IMU sensor, and starts the periodic reading of the 
   * sensor using a Mbed OS thread. The data is placed in a circular 
   * buffer and can be read whenever.
   */
  bno.setExtCrystalUse(true);
  
}

void loop() {

  

  BLEDevice central = BLE.central();
    if(central)
    {
        int writeLength;
        /* 
         * If a BLE device is connected, gyroscope data will start being read, 
         * and the data will be written to each BLE characteristic. The same 
         * data will also be output through serial so it can be plotted using 
         * Serial Plotter. 
         */
        while(central.connected())
        {            
            digitalWrite(LED_BUILTIN, HIGH);
            imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
            /* 
             * sprintf is used to convert the read float value to a string 
             * which is stored in bleBuffer. This string is then written to 
             * the BLE characteristic. 
             */
            writeLength = sprintf(bleBuffer, "%f", euler.x());
            YawBLE.writeValue(bleBuffer, writeLength); 
            
            writeLength = sprintf(bleBuffer, "%f", euler.y());
            PitchBLE.writeValue(bleBuffer, writeLength);   
               
            writeLength = sprintf(bleBuffer, "%f", euler.z());
            RollBLE.writeValue(bleBuffer, writeLength);      

            Serial.print("Yaw: ");
            Serial.print(euler.x());
            Serial.print(" Pitch: ");
            Serial.print(euler.y());
            Serial.print(" Roll: ");
            Serial.print(euler.z());
            Serial.print("\t\t\n");

            delay(BNO055_SAMPLERATE_DELAY_MS);
        }

        digitalWrite(LED_BUILTIN, LOW);
        Serial.print("Disconnected from central");
    }

}
