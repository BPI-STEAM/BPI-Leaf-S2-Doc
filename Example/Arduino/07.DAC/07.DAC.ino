void setup() { 
}  
void loop() { 
  // put your main code here, to run repeatedly: 
  for(int i=0;i<10;i++){     dacWrite(17,i*25);     delay(200); 
  } 
  for(int j=10;j>0;j--){     dacWrite(17,j*25);     delay(200); 
  } 
} 
