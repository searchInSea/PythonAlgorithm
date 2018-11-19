%生成随机样点
sampleNum = 100;   %生成样点个数
TrainFunNum = 30;
x1 = sort(10.*rand([sampleNum,1]));   %随机生成0-10
offset = 2*rand([sampleNum,1])-1;  %产生随机噪声
y = 2*x1+3;
plot(x1,y)
hold on
y = y+offset;
plot(x1,y, 'g*')
%用于保存计算过程方差
var = zeros([sampleNum-1,1]);
%保存切分点
cutPointVect = zeros([TrainFunNum,1]);
%切分函数，每一类的均值
averVect = zeros([TrainFunNum,2]);
%执行循环，共TrainFunNum个分类器
for TrainIdx = 1:TrainFunNum
    %分别计算每个切分点，求出方差
    for Pi = 1:sampleNum-1
        cutPoint = (x1(Pi) + x1(Pi+1))/2;
        aver1 = mean(y(1:Pi));
        aver2 = mean(y(Pi+1:sampleNum));
        var(Pi) = sum((y(1:Pi)-aver1).^2)+sum((y(Pi+1:sampleNum)-aver2).^2);
    end
    %找到方差最小的点，作为切分点
    [valTmp,index] = min(var);
    cutPointVect(TrainIdx) = index;
    averVect(TrainIdx,1) = mean(y(1:index));
    averVect(TrainIdx,2) = mean(y(index+1:sampleNum));
    %将残差作为下一轮的训练数据
    y=[(y(1:index)-averVect(TrainIdx,1));(y(index+1:sampleNum)-averVect(TrainIdx,2))];
end
%计算回归结果，画出图形
yTmp = zeros([sampleNum,1]);
for TrainIdx = 1:TrainFunNum
    yTmp(1:cutPointVect(TrainIdx)) = yTmp(1:cutPointVect(TrainIdx)) + averVect(TrainIdx,1);
    yTmp(cutPointVect(TrainIdx)+1:sampleNum) = yTmp(cutPointVect(TrainIdx)+1:sampleNum) + averVect(TrainIdx,2);
end
%红色为最终计算结果
plot(x1,yTmp,'r--')
