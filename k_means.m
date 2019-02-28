%clear all;
%   k-means algorithm
k = 3;
t = 1000;
a = 0.001;
% training data set:
%{
X = zeros(2,1000);
n = length(X);
rd = unidrnd(3,n);

    % one-hot matrix:
    oh = [0,0,1;0,1,0;1,0,0];
for i=1:n
    N1 = [-3;-3] + sqrt(2)*randn(2,1);
    N2 = [2;4] + sqrt(0.5)*randn(2,1);
    N3 = [4;0] + sqrt(1)*randn(2,1);
    D = [N1,N2,N3];
    X(:,i) = D*oh(:,rd(i));
end
%plot(X(1,:),X(2,:),'.')
%}
X = csvread('data.csv');
n = length(X);
%u = csvread('u.csv');
%u = (randn(2,3))*1;
ds = zeros(1,3);
label = zeros(1,n);
for i=1:n
    for j=1:k
        ds(1,j) = norm(X(:,i)-u(:,j),1);
    end
    label(i) = find(ds==min(ds),1);
end
s = zeros(2,3);
m = zeros(1,3);
for r=1:t
    for i=1:k
        s = zeros(2,3);
        m = zeros(1,3);
        for j=1:n
            if label(j)==1
                s(:,1) = s(:,1)+X(:,j);
                m(i) = m(i)+1;
            elseif label(j)==2
                s(:,2) = s(:,2)+X(:,j);
                m(i) = m(i)+1;
            else
                s(:,3) = s(:,3)+X(:,j);
                m(i) = m(i)+1;
            end
        end
        u(:,i) = (s(i)/m(i));
    end
end

for i=1:n
    if label(i)==1
        plot(X(1,i),X(2,i),'or');hold on;
    end
    if label(i)==2
        plot(X(1,i),X(2,i),'ob');hold on;
    end
    if label(i)==3
        plot(X(1,i),X(2,i),'og');hold on;
    end
end

%plot(u(1,:),u(2,:),'om');
%figure;
%plot(X(1,:),X(2,:),'ok');
