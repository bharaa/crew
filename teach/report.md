```c
// The circuit:
// - LED connected from digital pin 13 to GND
// (Note: most Arduinos have an on-board LED connected to digital pin 13)

void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(5000);              // wait for 5 seconds
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(2000);              // wait for 2 seconds
}
```