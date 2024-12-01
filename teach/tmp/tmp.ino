// Built-in LED turn-on and turn-off using acceleration with minimum delay 100 milliseconds for Arduino Uno

const int builtinLedPin = 13; // Built-in LED pin is always 13 on Arduino Uno
unsigned long previousMillis = 0; // Variable to store the last time the LED was turned on or off

void setup() {
  pinMode(builtinLedPin, OUTPUT); // Initialize the built-in LED pin as an output
}

void loop() {
  unsigned long currentMillis = millis(); // Get the current time in milliseconds
  
  // Turn on the built-in LED using acceleration with minimum delay 100 milliseconds
  if (currentMillis - previousMillis >= 100) {
    digitalWrite(builtinLedPin, HIGH); // Turn on the built-in LED
    previousMillis = currentMillis; // Update the last time the LED was turned on
    
    // Simulate some work or delay before turning off the LED
    delay(5000);
    
    // Turn off the built-in LED using acceleration with minimum delay 100 milliseconds
    if (currentMillis - previousMillis >= 100) {
      digitalWrite(builtinLedPin, LOW); // Turn off the built-in LED
      previousMillis = currentMillis; // Update the last time the LED was turned off
    }
  }
  
  // Keep the loop running forever
  delay(1);
}