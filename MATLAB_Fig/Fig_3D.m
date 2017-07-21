 P=[0.0229    0.6882     0.6178   0.9727    0.3973    0.5611;
0.0667    0.626       0.5478   0.9367    0.8219    0.3265;
0.8617    0.0714     0.0478   0.0596    0.6986    0.1029;
0.8157    0.0967    0.0669    0.079      0.6438    0.1575;
0.8175    0.0495    0.0318    0.1048    0.6986    0.0923;
0.998      0.1846    0.1338    0.0556    0.4795    0.2549;
0.998      0.1846    0.1338    0.0556    0.4795    0.2549;
0.9595     0.1928    0.1401    0.0037    0.5205   0.2381];
for i=1:4;
x(1+12*(i-1):12*i)=i/10;
end
for i=1:6
y(i:6:42+i)=i;
end
z=[];
for i=1:8
z=[z P(i,:)];
end
[xi,yi]=meshgrid(linspace(min(x),max(x),50),linspace(min(y),max(y),80));
zi=griddata(x,y,z,xi,yi,'cubic');
mesh(xi,yi,zi)
hold on
 plot3(x,y,z,'*')