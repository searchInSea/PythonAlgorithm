%�����������
sampleNum = 50;   %�����������
x1 = 10.*rand([sampleNum,1]);   %�������0-10
offset = 2*rand([sampleNum,1])-1;  %�����������
y = 2*x1+3;
plot(x1,y)
hold on
y = y+offset;
plot(x1,y, 'g*')


