#define LED_CHANNEL_0     0    //设置通道0 
#define LED_TIMER_13_BIT  13   //设置13位定时器
#define LED_BASE_FREQ     5000 //设置定时器频率位5000Hz 
#define LED_PIN            13  //设置LED灯 

int brightness = 0;    // LED亮度
int fadeAmount = 1;    // LED数量
 
//设置led灯的亮度 
void ledcAnalogWrite(uint32_t value, uint32_t valueMax = 255) { 
  //计算占空比 
  uint32_t duty = (LED_BASE_FREQ / valueMax) * min(value, valueMax); 
  //设置占空比 
  ledcWrite(LED_CHANNEL_0, duty); 
}  
void setup() { 
  ledcSetup(LED_CHANNEL_0, LED_BASE_FREQ, LED_TIMER_13_BIT);   ledcAttachPin(LED_PIN, LED_CHANNEL_0); 
}  
void loop() { 
  ledcAnalogWrite(brightness);   brightness += fadeAmount; 
 
  if (brightness <= 0 || brightness >= 255) { 
       fadeAmount = -fadeAmount; 
  }   
  delay(30); 
}
