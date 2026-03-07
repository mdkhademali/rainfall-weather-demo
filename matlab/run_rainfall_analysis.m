
% Rainfall Statistical Analysis

data = readtable('../data/sample_rainfall_data.csv');

rain = data.rainfall_mm;

mean_rain = mean(rain);
std_rain = std(rain);

disp("Mean Rainfall:");
disp(mean_rain);

disp("Standard Deviation:");
disp(std_rain);

figure
plot(rain)
title('Rainfall Time Series')
xlabel('Day')
ylabel('Rainfall (mm)')
