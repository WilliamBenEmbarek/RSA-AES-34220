function [k1,k2,k3,k4,k5,k6,k7,k8] = Keys( keyB,shift )
    %KEYS Summary of this function goes here
    %   Detailed explanation goes here
    for i = 0:shift*25
        keyB = [keyB(2:end) keyB(1)];
    end
    k1 = keyB(1)+keyB(2);
    k2 = keyB(3)+keyB(4);
    k3 = keyB(5)+keyB(6);
    k4 = keyB(7)+keyB(8);
    k5 = keyB(9)+keyB(10);
    k6 = keyB(11)+keyB(12);
    k7 = keyB(13)+keyB(14);
    k8 = keyB(15)+keyB(16);
    
end

