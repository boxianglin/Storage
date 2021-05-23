clear
close all

prompt = 'Enter the value of ∆t: ';
% set t_max= x then coloumns needed = x / delta_t + 1
% row = 1/ (0.01) + 1 = 11 (by default x[0,1]
delta_t = input(prompt);

prompt1 = 'Enter the value of T(max): ';
column = input(prompt1) / delta_t + 1 ;
row = 11;

% 2-D array with all zeros for exact solution
arr1 = zeros(row,column);

% initial variables for exact solution
result = 0;
arr1_x = 0;
arr1_t = 0;

% exact solution
% taking 14 terms
for i = 1:row
    for j = 1:column
        for k = 1:14
            result = result + 4/(k*pi)^2*sin(k*pi/2)*sin(k*pi*arr1_x)*exp(-0.5*(k*pi)^2*arr1_t);
        end
        arr1(i,j) = result;
        arr1_t = arr1_t + delta_t;     
        result = 0;
    end
    arr1_t = 0;
    arr1_x = arr1_x + 0.1;
end

% Numerical Computing Solution
% (Initial Condition)
arr2 = zeros(row,column);
x_num = 0;
for i = 1 : row
    if(x_num>0.5)
        arr2(i,1) = 1-x_num;
    else
        arr2(i,1) = x_num;
    end
    x_num = x_num + 0.1;
end

% applied explicit differences to calculate other points
% applied boundary condition as well
dt = delta_t;
dx = 0.1;
for j = 2: column
    for i = 1:row
        if (i == 1 || i == row)
            arr2(i,j) = 0;
        else
            arr2(i,j) =0.5 *dt/(dx)^2*(arr2(i+1, j-1)-2*arr2(i,j-1)+arr2(i-1,j-1))+arr2(i,j-1); 
        end
    end
end


% Error |Exact - Numerical|
error = zeros(row, column);
for i = 1 : row
    for j = 1 : column
        error(i,j) = abs(arr1(i,j)- arr2(i,j));
    end
end



%% plot Portion
x_ = 0:0.1:1;

prompt_1 = 'Enter the value of t to get the graph u(x,t) at t =: ' ;
t = input(prompt_1);
exctVal = arr1(:, t/delta_t+1 );
numVal = arr2(:, t/delta_t+1 );
plot (x_,numVal,x_,exctVal,'lineWidth', 2);
hold off
xlabel('x');
s = num2str(t);
txt = ['u(x,t), t= ', s];
ylabel(txt);
legend('Numerical','Exact');
