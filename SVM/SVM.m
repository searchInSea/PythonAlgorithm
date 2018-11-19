%���������
sampleNum = 50;   %�����������
x1 = 10.*rand([sampleNum,1]);   %�������0-10
x2 = x1;   %����㰴�ո�ֱ�߻���,��ɫ��
offset = 5*rand([sampleNum,1])+1;  %�������ƫ��
plot(x1,x2)
x2(1:sampleNum/2) = x2(1:sampleNum/2) - offset(1:sampleNum/2);   %ǰһ��ĵ�����ƫ��
%��һ��ĵ�����ƫ��
x2(sampleNum/2+1:sampleNum) = x2(sampleNum/2+1:sampleNum) + offset(sampleNum/2+1:sampleNum);
hold on
plot(x1(1:sampleNum/2),x2(1:sampleNum/2),'g*')
plot(x1(sampleNum/2+1:sampleNum),x2(sampleNum/2+1:sampleNum),'r+')
y=ones([sampleNum,1]);
y(1:sampleNum/2) = -1;

X = [x1,x2];
% X = [4.48019713464051,0.268620961714016;
%     5.69358183284932,3.58725318221380;
%     0.614014422908470,5.79929665056787;
%     4.96288885639885,10.8182650136114;];
% sampleNum = 3;
% X = [[3,3];[4,3];[1,1]];
% plot(X(:,1),X(:,2), 'r^')
% y = [1;1;-1];
H = (y*y').*(X*X');
f = ones([sampleNum,1])*(-1);
A = diag(ones([1,sampleNum])*(-1));
b = zeros([sampleNum,1]);
Aeq = y';
beq = 0;
% options = optimset('Algorithm','active-set');
options = optimset('Algorithm','interior-point-convex');
% options = optimset('Algorithm','trust-region-reflective');
[alpha,valT] = quadprog(H,f,A,b,Aeq,beq,[],[],zeros([sampleNum,1]),options)

w = (alpha.*y)'*X
B=0;
for si=1:sampleNum
    B = B+y(si) - (alpha.*y)'*X*(X(si,:)');
end
B = B/sampleNum
hold on
x2Tem = -w(1)/w(2)*X(:,1)-B/w(2);
plot(X(:,1),x2Tem, '-r')   %���ֽ��,��ɫ����




