int pinled = 9;
void setup() {
  pinMode(pinled, OUTPUT);
}

void loop() {
 digitalWrite(pinled, HIGH);  // turn the LED on (HIGH is the voltage level)
 delay(1000);                      // wait for a second
 digitalWrite(pinled, LOW);   // turn the LED off by making the voltage LOW
 delay(1000);                      // wait for a second
}
