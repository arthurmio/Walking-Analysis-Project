#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ArduinoBLE.h>

Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);
char *Tabperiph[] = {"IMU Euler Angles", "IMU Euler Angles 2", "IMU Euler Angles 3", "IMU Euler Angles 4", "IMU Euler Angles 5", "IMU Euler Angles 6"};
char *addr[] = {"1001", "1002", "1003", "1004", "1005", "1006"};



// récupération des données des caractéristiques
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


//affichage des caractéristiques
void printChar(BLECharacteristic c1, BLECharacteristic c2, BLECharacteristic c3){
  c1.read();
  c2.read();
  c3.read();
  
  float f1=getData(c1.value(), c1.valueLength());
  float f2=getData(c2.value(), c2.valueLength());
  float f3=getData(c3.value(), c3.valueLength());

  // affichage slave
  Serial.print(",");
  Serial.print(f1); //Yaw
  Serial.print(",");
  Serial.print(f2); //Pitch
  Serial.print(",");
  Serial.println(f3); //Roll
  
}

void setup() {
  Serial.begin(115200);

  BLE.begin();
  bno.begin();
  BLE.scan();

  bno.setExtCrystalUse(true);
}

void loop() {
  //time rebouclage
  long myTime = millis();
  float myMinutes = myTime/1000.0;
  
  
  
 // if(peripheral){
    for (int i=0; i<7; i++){
      BLE.scan();
      BLEDevice peripheral = BLE.available();
      
      if(peripheral.localName()==Tabperiph[i]){
        BLE.stopScan();
      
//        if(peripheral.connect()){
//          Serial.println("Connect1");
//        }
//        else{ return; }
//      
//        if(peripheral.discoverAttributes()){
//          Serial.println("Connect2");
//        }
//        else{ return; }

        peripheral.connect();
        peripheral.discoverAttributes();
      
        BLEService euler=peripheral.service(addr[i]);
        BLECharacteristic yaw=euler.characteristic("2001");
        BLECharacteristic pitch=euler.characteristic("2002");
        BLECharacteristic roll=euler.characteristic("2003");

        Serial.print(myMinutes);
        Serial.print(",");
        Serial.print(i+1);
        printChar(yaw, pitch, roll);
        peripheral.disconnect();
        delay(100);
        
      }   
    }
    imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
    //Affichage master
    Serial.print(myMinutes);
    Serial.print(",");
    Serial.print("7");
    Serial.print(",");
    Serial.print(euler.x()); //Yaw
    Serial.print(",");
    Serial.print(euler.y()); //Pitch
    Serial.print(",");
    Serial.println(euler.z()); //Roll
    
 /* }
    else{
          peripheral.disconnect();
          return;
        }*/
  
  BLE.scan();
//  Serial.println("rescan");

}
