
#include <Arduino_LSM9DS1.h>
#include <SensorFusion.h>

float AccX, AccY, AccZ, GyX, GyY, GyZ ,MagX , MagY, MagZ;
float pitch, roll, yaw;
float deltat;

SF fusion;

void setup()
{
  Serial.begin(115200);
  IMU.begin();
}

void loop() {
  // put your main code here, to run repeatedly:

  delay(500);

  IMU.readAcceleration(AccX, AccY, AccZ);
  IMU.readGyroscope(GyX, GyY, GyZ);
  IMU.readMagneticField(MagX, MagY, MagZ);

  deltat = fusion.deltatUpdate();

  // update the filter, which computes orientation:
  fusion.MadgwickUpdate(GyX, GyY, GyZ, AccX, AccY, AccZ, MagX, MagY, MagZ, deltat);
   
  pitch = fusion.getPitch();
  roll = fusion.getRoll();    
  yaw = fusion.getYaw();
  
  //Serial.printf("Acceleration : \n X : %f, Y : %f, Z : %f\r\n Gyroscope :\n X : %f, Y : %f,Z : %f\r\n Magnetic :\n X : %f, Y : %f, Z : %f\r\n\n ", AccX, AccY, AccZ, GyX, GyY, GyZ, MagX, MagY, MagZ);

  Serial.print("Pitch :");
  Serial.println(pitch);
  Serial.print("\n Roll :");
  Serial.println(roll);
  Serial.print("\n Yaw :");
  Serial.println(yaw);
  Serial.print("\n\n");
  }
   
   

  
