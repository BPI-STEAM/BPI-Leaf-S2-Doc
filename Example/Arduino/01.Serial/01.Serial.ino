void setup()
{
Serial.begin(115200); //设置串口通信波特率
}
void loop()
{
static unsigned long i = 0; //定义变量 i
Serial.println(i++); //i 加一后输出 i
delay(1000); //延时 1 秒
} 
