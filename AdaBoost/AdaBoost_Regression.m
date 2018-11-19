%生成随机样点
sampleNum = 50;   %生成样点个数
x1 = 10.*rand([sampleNum,1]);   %随机生成0-10
offset = 2*rand([sampleNum,1])-1;  %产生随机噪声
y = 2*x1+3;
plot(x1,y)
hold on
y = y+offset;
plot(x1,y, 'g*')


