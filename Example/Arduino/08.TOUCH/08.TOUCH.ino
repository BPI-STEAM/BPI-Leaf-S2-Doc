 void setup() 
{ 
  Serial.begin(115200); 
      delay(1000); // give me time to bring up serial monitor 
      Serial.println("Leaf-S2 Touch Test");    
}  
void loop(){ 
  Serial.println(touchRead(T2));  // get value using T0->D9  
  delay(100); 
} 
