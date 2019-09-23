void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  String command = "";  
  while(Serial.available() > 0){
      command = Serial.readString();
      Serial.println("I received: " + command);
  }

  if(command.equals("Hora")){
    Serial.println("Son las 8:30 pm");
  }
  
  delay(100);
}
