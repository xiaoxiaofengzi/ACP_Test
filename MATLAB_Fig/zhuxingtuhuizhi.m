clc
clear
aa = randn(20,4);
aa(1,:)
bb = [1 2 3 3;1 1 1 1];
cc = [1 1 1;1 1 2];
%bar(aa*10);
figure; 
%bar(aa(1,:)*10,'stacked');
bar(bb,'stacked');
hold on
bar(cc,'stacked');
hold on