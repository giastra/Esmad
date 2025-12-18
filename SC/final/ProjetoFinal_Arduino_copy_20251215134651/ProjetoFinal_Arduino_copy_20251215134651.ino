#include <SPI.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <MFRC522.h>
#include <virtuabotixRTC.h>
#include <Servo.h>
virtuabotixRTC myRTC(7, 6, 5);//leitor
LiquidCrystal_I2C lcd(0x27, 16, 2); //painel
Servo myservo;//create servo object to control a servo

//sensor nfc
#define SS_PIN 10
#define RST_PIN 5
MFRC522 rfid(SS_PIN, RST_PIN);

String texto = "";

int pos = 0;
Servo servo_9;

void setup() {
  Serial.begin(9600);
  SPI.begin(); // init SPI bus
  rfid.PCD_Init(); // init MFRC522
  lcd.init();              // Initialize the LCD display screen
  lcd.backlight();  

  Serial.println("Tap RFID/NFC Tag on reader");
  
  myservo.attach(9);//attachs the servo on pin 9 to servo object
  myservo.write(0);//back to 0 degrees 

  Serial.begin(9600);
  // Set the current date, and time in the following format:
  // seconds, minutes, hours, day of the week, day of the month, month, year
  myRTC.setDS1302Time(0, 39, 16, 7, 4, 12, 2025);
  
  servo_9.attach(9);
}

void loop() {
  if (rfid.PICC_IsNewCardPresent()) { // new tag is available
    if (rfid.PICC_ReadCardSerial()) { // NUID has been readed
      MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
      //Serial.print("RFID/NFC Tag Type: ");
      //Serial.println(rfid.PICC_GetTypeName(piccType));

      // print NUID in Serial Monitor in the hex format
      Serial.print("UID:");
      for (int i = 0; i < rfid.uid.size; i++) {
        Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(rfid.uid.uidByte[i], HEX);
        texto +=rfid.uid.uidByte[i];
        
        if (texto == "89 0F A3 D3"){
          for (pos = 0; pos <= 90; pos += 1) {
          // tell servo to go to position in variable 'pos'
          servo_9.write(pos);
          // wait 15 ms for servo to reach the position
          delay(5); // Wait for 15 millisecond(s)
      }
        }
      Serial.println();

      rfid.PICC_HaltA(); // halt PICC
      rfid.PCD_StopCrypto1(); // stop encryption on PCD

       myRTC.updateTime();

  // Pinta o horario no console
  Serial.print("Current Date / Time: ");
  Serial.print(myRTC.dayofmonth);
  Serial.print("/");
  Serial.print(myRTC.month);
  Serial.print("/");
  Serial.print(myRTC.year);
  Serial.print(myRTC.hours);
  Serial.print(":");
  Serial.print(myRTC.minutes);

  // Escreve no lcd 
  lcd.setCursor(2, 0);     // Go to position column 2 & row 1
  lcd.print("Porta A"); // Print "Hello, World!"
  lcd.setCursor(0, 1);     // Go to position column 1 & row 2
  lcd.print(myRTC.dayofmonth);
  lcd.print("/");
  lcd.print(myRTC.month);
  lcd.print("/");
  lcd.print(myRTC.year);
  lcd.print("  ");
  lcd.print(myRTC.hours);
  lcd.print(":");
  lcd.print(myRTC.minutes);
  lcd.print(":");
  lcd.println(myRTC.seconds);

  // Delay so the program doesn't print non-stop
  delay(500);
    }
  }
}
}