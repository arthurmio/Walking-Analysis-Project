#include <Arduino_LSM9DS1.h>
 

void setup()
{
  Serial.begin(115200);
  IMU.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  float AccX, AccY, AccZ;
  float GyX, GyY, GyZ;
  float MagX, MagY, MagZ;

  IMU.readAcceleration(AccX, AccY, AccZ);
  IMU.readGyroscope(GyX, GyY, GyZ);
  IMU.readMagneticField(MagX, MagY, MagZ);

  Serial.printf("Acceleration : \n X : %f, Y : %f, Z : %f\r\n Gyroscope :\n X : %f, Y : %f,Z : %f\r\n Magnetic :\n X : %f, Y : %f, Z : %f\r\n\n ", AccX, AccY, AccZ, GyX, GyY, GyZ, MagX, MagY, MagZ);

  }
   
   

  
