%�����������
sampleNum = 100;   %�����������
TrainFunNum = 30;
x1 = sort(10.*rand([sampleNum,1]));   %�������0-10
offset = 2*rand([sampleNum,1])-1;  %�����������
y = 2*x1+3;
plot(x1,y)
hold on
y = y+offset;
plot(x1,y, 'g*')
%���ڱ��������̷���
var = zeros([sampleNum-1,1]);
%�����зֵ�
cutPointVect = zeros([TrainFunNum,1]);
%�зֺ�����ÿһ��ľ�ֵ
averVect = zeros([TrainFunNum,2]);
%ִ��ѭ������TrainFunNum��������
for TrainIdx = 1:TrainFunNum
    %�ֱ����ÿ���зֵ㣬�������
    for Pi = 1:sampleNum-1
        cutPoint = (x1(Pi) + x1(Pi+1))/2;
        aver1 = mean(y(1:Pi));
        aver2 = mean(y(Pi+1:sampleNum));
        var(Pi) = sum((y(1:Pi)-aver1).^2)+sum((y(Pi+1:sampleNum)-aver2).^2);
    end
    %�ҵ�������С�ĵ㣬��Ϊ�зֵ�
    [valTmp,index] = min(var);
    cutPointVect(TrainIdx) = index;
    averVect(TrainIdx,1) = mean(y(1:index));
    averVect(TrainIdx,2) = mean(y(index+1:sampleNum));
    %���в���Ϊ��һ�ֵ�ѵ������
    y=[(y(1:index)-averVect(TrainIdx,1));(y(index+1:sampleNum)-averVect(TrainIdx,2))];
end
%����ع���������ͼ��
yTmp = zeros([sampleNum,1]);
for TrainIdx = 1:TrainFunNum
    yTmp(1:cutPointVect(TrainIdx)) = yTmp(1:cutPointVect(TrainIdx)) + averVect(TrainIdx,1);
    yTmp(cutPointVect(TrainIdx)+1:sampleNum) = yTmp(cutPointVect(TrainIdx)+1:sampleNum) + averVect(TrainIdx,2);
end
%��ɫΪ���ռ�����
plot(x1,yTmp,'r--')
