ECG_collection = [];
for i = 1:length(DREAMER.Data)
    ECG_trials = DREAMER.Data{1, i}.ECG.baseline;
    new_ECG_trials = [];
    
    for j = 1:length(ECG_trials)
        new_ECG_trials(j) = ECG_trials(:, 1);
    end
    
    ECG_collection(i) = (new_ECG_trials);
end
