root_path = 'pic';
% X_path = strcat(root_path, '/', 'white', '/');
% Y_path = strcat(root_path, '/', 'gan', '/');
X_path = strcat(root_path, '/', 'real', '/');
Y_path = strcat(root_path, '/', 'CycleGan_test', '/');

X_list=dir(fullfile(X_path));
Y_list=dir(fullfile(Y_path));
j = 3;
fsim_res = [];
fsimc_res = [];

for i=3:size(X_list, 1)
    X_list(i).name;
    Y_list(j).name;
    j = j + 1;
    
    X = imread(strcat(X_path, X_list(i).name));
    Y = imread(strcat(Y_path, Y_list(i).name));
%     size(X)
%     size(Y)
    Y = imresize(Y, [250 250]);
%     size(Y)
    [FSIM, FSIMc] = FeatureSIM(X, Y);
    
    fsim_res = [fsim_res, FSIM];
    fsimc_res = [fsimc_res, FSIM];
end

fsim_ave = sum(fsim_res) / size(fsim_res, 2)
fsimc_ave = sum(fsimc_res) / size(fsimc_res, 2)
